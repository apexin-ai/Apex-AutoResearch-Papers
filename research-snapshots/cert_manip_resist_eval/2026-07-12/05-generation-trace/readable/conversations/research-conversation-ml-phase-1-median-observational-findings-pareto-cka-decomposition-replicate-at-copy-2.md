# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/8214876e-3227-48e5-b866-c4dc450f1f75.jsonl`
- **Structured JSON:** [`e18c73aea995018da2c8.json`](../../sessions/e1/e18c73aea995018da2c8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:52:25.654Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:52:25.654Z",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; paper pivots to planned negative-result narrative with geometric explanation\n核心假设：['EN AUROC scales modestly; correctness signal present but not dramatically stronger in larger models', 'Pareto frontier exists in 1-2/3 architectures but is noisier (fewer languages show clear tradeoff per architecture)', \"Simpson's Paradox confirmed in ≥1 architecture but one architecture (likely Qwen, matching pilot rho=0.18) shows non-significant partial correlation\", 'CaCLR β sweep across 3 OOM shows no consistent benefit — consistency loss is inert (reframe as systematic negative result)', 'Decomposition is directionally correct but effect sizes are modest (<3pp), more qualitative than quantitative', 'Linear projection works but saturates at ~100 pairs, not 50; effect reversal threshold is architecture-dependent', 'Procrustes effect reversal replicates but threshold varies enough across architectures that a single rule is hard to state']\n关键指标范围：{'en_auroc_best_layer_mean_across_arch': [0.76, 0.82], 'zs_transfer_pass_rate_auroc_gt_058_of_20': [12, 16], 'mean_zs_auroc_drop_vs_en_pp': [8, 14], 'pareto_tradeoff_prevalence_frac_lang_arch_pairs': [0.25, 0.5], 'pareto_depth_transfer_drop_at_final_layers_pp': [1.0, 3.0], 'cka_partial_corr_rho_controlling_depth': [0.15, 0.35], 'cka_partial_corr_p_value': [0.005, 0.05], 'simpson_paradox_confirmed_of_3_arch': [1, 2], 'caclr_delta_over_zeroshot_mean_pp': [-0.5, 1.0], 'caclr_langs_improved_of_20': [5, 10], 'linear_proj_delta_over_zs_low_resource_pp': [3, 7], 'linear_proj_saturation_pairs': [50, 120], 'decomposition_transfer_improvement_after_difficulty_projection_pp': [1, 3], 'decomposition_langs_showing_clean_separation_of_10': [4, 7], 'control_task_selectivity_deep_layers': [0.15, 0.25], 'cross_lingual_artifact_rate_pct': [15, 30], 'spearman_depth_vs_transfer_rho_positive_langs_of_20': [12, 17]}\n叙事方向：Empirical study + diagnostic negative result. CaCLR fails → reframe as 'the natural distributional-matching baseline fails; we explain why via CKA geometric analysis (MMD matches marginals but not low-dimensional directional subspace).' Claim 3 becomes systematic negative result with CORAL + high-dim MMD ablations closing the distributional-matching path. Claim 1 (Pareto) softened to 'architecture-dependent local tradeoff observed in MoE but weak in dense.' Claim 2 (decomposition) downgraded from quantitative to qualitative. Headline pivots to: 'Cross-lingual probe transfer reveals architecture-dependent depth effects; distributional matching fails but linear projection with ~100 pairs is the practical label-free solution.' Paper still holds for EACL: field-level viability test + negative result + practical solution + geometric insights. May need to compress Claim 2 to make space for stronger negative-result analysis.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions\n- Camera-ready extension: 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as \"principled scope\" not \"design limitation.\"\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method.\" Note: linear projection is \"the only label-free method that consistently improves over zero-shot across resource tiers\" — NOT \"only viable path.\" Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive. CORAL COMPARISON\n    (D015, re-dream 2-tier consensus): Add CORAL loss (second-order alignment, Sun\n    & Saenko 2016) as alternative to MMD. Tests whether distributional matching failure\n    is MMD-specific or general. Trivial to implement on cached activations. Report\n    CORAL alongside MMD in Table 7 ablation. Strengthens negative result scope. HIGH-DIM\n    MMD (D016, dream #4 cross-tier consensus): All 3 tiers flagged \"1-D logit MMD\"\n    as overclaimed scope. Test MMD on PCA-reduced activations (d=50, d=100) instead\n    of 1-D probe logits. If high-dim also fails → broadens \"distributional matching\n    fails\" claim. If high-dim works → method contribution jumps significantly. Trivial:\n    PCA on cached activations, then MMD in reduced space. Also test with CORAL in\n    high-dim. MULTI-SEED (D016): Run 3-5 seeds for CaCLR, few-shot (25/100), and Procrustes\n    at representative layers. Report std across seeds. Addresses single-seed concern.\n    MIXED β CRITERION (D016): Add 1-2 validation languages (zh, sw) to β selection\n    criterion alongside English, to rule out systematic bias against cross-lingual\n    benefit.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  registry_id: plan_013\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique. SELECTIVITY THRESHOLD\n    SENSITIVITY (D015): Test at 0.03, 0.05, 0.10 thresholds (Hewitt & Liang used 0.05\n    for English syntactic probing; may not be appropriate for multilingual correctness).\n    Report artifact rate at each threshold. Trivial to compute from existing data\n    (plan_013 v2 already running).\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 32.7B Dense (60 text layers, dense, BF16): third architecture\n    for core submission. Full Pareto frontier at every 4th layer + final (16 probed\n    layers), 20 languages, 5 transfer conditions. BF16 (~62.5GB, fits single 96GB\n    GPU). Provides dense vs MoE architectural contrast — addresses #1 reviewer concern\n    across ALL dream tiers (\"architecture comparison confounded\").\n\n    '\n  priority: P0\n  gpu_budget_hours: 30\n  deps: []\n  notes: 'Upgraded P2→P0 (D016). User providing 4× RTX 6000 96G on second server.\n    Model: google/gemma-4-31B (HF) / ModelScope. Apache 2.0, no gating. MULTIMODAL:\n    has vision encoder (27 extra layers) — extract_activations.py must hook ONLY text\n    decoder layers (60 layers), skip vision. Code may need adjustment. BF16 ~62.5GB\n    (2 shards: 49.8 + 12.8GB), single 96GB GPU sufficient. No quantization needed\n    — eliminates quantization confound for this model.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- exp_id: plan_013_probing_controls_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002_4gpu\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:52:25.658Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:52:25.658Z",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-21T12:52:25.678Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; paper pivots to planned negative-result narrative with geometric explanation
核心假设：['EN AUROC scales modestly; correctness signal present but not dramatically stronger in larger models', 'Pareto frontier exists in 1-2/3 architectures but is noisier (fewer languages show clear tradeoff per architecture)', "Simpson's Paradox confirmed in ≥1 architecture but one architecture (likely Qwen, matching pilot rho=0.18) shows non-significant partial correlation", 'CaCLR β sweep across 3 OOM shows no consistent benefit — consistency loss is inert (reframe as systematic negative result)', 'Decomposition is directionally correct but effect sizes are modest (<3pp), more qualitative than quantitative', 'Linear projection works but saturates at ~100 pairs, not 50; effect reversal threshold is architecture-dependent', 'Procrustes effect reversal replicates but threshold varies enough across architectures that a single rule is hard to state']
关键指标范围：{'en_auroc_best_layer_mean_across_arch': [0.76, 0.82], 'zs_transfer_pass_rate_auroc_gt_058_of_20': [12, 16], 'mean_zs_auroc_drop_vs_en_pp': [8, 14], 'pareto_tradeoff_prevalence_frac_lang_arch_pairs': [0.25, 0.5], 'pareto_depth_transfer_drop_at_final_layers_pp': [1.0, 3.0], 'cka_partial_corr_rho_controlling_depth': [0.15, 0.35], 'cka_partial_corr_p_value': [0.005, 0.05], 'simpson_paradox_confirmed_of_3_arch': [1, 2], 'caclr_delta_over_zeroshot_mean_pp': [-0.5, 1.0], 'caclr_langs_improved_of_20': [5, 10], 'linear_proj_delta_over_zs_low_resource_pp': [3, 7], 'linear_proj_saturation_pairs': [50, 120], 'decomposition_transfer_improvement_after_difficulty_projection_pp': [1, 3], 'decomposition_langs_showing_clean_separation_of_10': [4, 7], 'control_task_selectivity_deep_layers': [0.15, 0.25], 'cross_lingual_artifact_rate_pct': [15, 30], 'spearman_depth_vs_transfer_rho_positive_langs_of_20': [12, 17]}
叙事方向：Empirical study + diagnostic negative result. CaCLR fails → reframe as 'the natural distributional-matching baseline fails; we explain why via CKA geometric analysis (MMD matches marginals but not low-dimensional directional subspace).' Claim 3 becomes systematic negative result with CORAL + high-dim MMD ablations closing the distributional-matching path. Claim 1 (Pareto) softened to 'architecture-dependent local tradeoff observed in MoE but weak in dense.' Claim 2 (decomposition) downgraded from quantitative to qualitative. Headline pivots to: 'Cross-lingual probe transfer reveals architecture-dependent depth effects; distributional matching fails but linear projection with ~100 pairs is the practical label-free solution.' Paper still holds for EACL: field-level viability test + negative result + practical solution + geometric insights. May need to compress Claim 2 to make space for stronger negative-result analysis.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: xling_calib_direction

## paper_framing.md

# Paper Framing — xling_calib_direction

## Target Venue
- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions
- Camera-ready extension: 30+ languages

## Core Insight
The model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.

## Core Claims (4, causal chain)

### Claim 1 — Pareto Frontier (Discovery)
Cross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).
- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).
- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.

### Claim 2 — Decomposition (Analysis)
Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
- Evidence: IRT difficulty probes → project out → retrain → compare transfer.

### Claim 3 — CaCLR (Method / Diagnostic)
CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as "principled scope" not "design limitation."
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
- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.
- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.
- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.

## Story Spine
- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.
- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method." Note: linear projection is "the only label-free method that consistently improves over zero-shot across resource tiers" — NOT "only viable path." Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.
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
    Negative result demands higher reproducibility bar than positive. CORAL COMPARISON
    (D015, re-dream 2-tier consensus): Add CORAL loss (second-order alignment, Sun
    & Saenko 2016) as alternative to MMD. Tests whether distributional matching failure
    is MMD-specific or general. Trivial to implement on cached activations. Report
    CORAL alongside MMD in Table 7 ablation. Strengthens negative result scope. HIGH-DIM
    MMD (D016, dream #4 cross-tier consensus): All 3 tiers flagged "1-D logit MMD"
    as overclaimed scope. Test MMD on PCA-reduced activations (d=50, d=100) instead
    of 1-D probe logits. If high-dim also fails → broadens "distributional matching
    fails" claim. If high-dim works → method contribution jumps significantly. Trivial:
    PCA on cached activations, then MMD in reduced space. Also test with CORAL in
    high-dim. MULTI-SEED (D016): Run 3-5 seeds for CaCLR, few-shot (25/100), and Procrustes
    at representative layers. Report std across seeds. Addresses single-seed concern.
    MIXED β CRITERION (D016): Add 1-2 validation languages (zh, sw) to β selection
    criterion alongside English, to rule out systematic bias against cross-lingual
    benefit.

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
  priority: P0
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
  registry_id: plan_013
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
  notes: 'CPU-bound. Dream review D22: probing methodology critique. SELECTIVITY THRESHOLD
    SENSITIVITY (D015): Test at 0.03, 0.05, 0.10 thresholds (Hewitt & Liang used 0.05
    for English syntactic probing; may not be appropriate for multilingual correctness).
    Report artifact rate at each threshold. Trivial to compute from existing data
    (plan_013 v2 already running).

    '
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
- id: plan_008
  claim: 1
  description: 'Gemma 4 32.7B Dense (60 text layers, dense, BF16): third architecture
    for core submission. Full Pareto frontier at every 4th layer + final (16 probed
    layers), 20 languages, 5 transfer conditions. BF16 (~62.5GB, fits single 96GB
    GPU). Provides dense vs MoE architectural contrast — addresses #1 reviewer concern
    across ALL dream tiers ("architecture comparison confounded").

    '
  priority: P0
  gpu_budget_hours: 30
  deps: []
  notes: 'Upgraded P2→P0 (D016). User providing 4× RTX 6000 96G on second server.
    Model: google/gemma-4-31B (HF) / ModelScope. Apache 2.0, no gating. MULTIMODAL:
    has vision encoder (27 extra layers) — extract_activations.py must hook ONLY text
    decoder layers (60 layers), skip vision. Code may need adjustment. BF16 ~62.5GB
    (2 shards: 49.8 + 12.8GB), single 96GB GPU sufficient. No quantization needed
    — eliminates quantization confound for this model.

    '
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
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_002
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_002_4gpu
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan_002_v3
  name: ''
  status: PREPARING
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
  "promptId": "b7585d46-2ea0-497d-8a35-64b3c1f62eec",
  "type": "user",
  "uuid": "4a47cd3f-c88e-442d-b611-c3822f3d1e4a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:52:25.677Z_

```json
{
  "parentUuid": "4a47cd3f-c88e-442d-b611-c3822f3d1e4a",
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
  "uuid": "1509ffd5-5150-4250-b6c9-0ba284ce265e",
  "timestamp": "2026-05-21T12:52:25.677Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:52:25.677Z_

```json
{
  "parentUuid": "1509ffd5-5150-4250-b6c9-0ba284ce265e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5d10e693-f26b-4ead-868e-fcd46a02dc62",
  "timestamp": "2026-05-21T12:52:25.677Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "5d10e693-f26b-4ead-868e-fcd46a02dc62",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiment predictions for cross-lingual correctness probe transfer",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:52:29.996Z_

I'll analyze each planned experiment and generate detailed median-tier predictions. Let me first review the existing experiment data and memory files for any additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d10e693-f26b-4ead-868e-fcd46a02dc62",
  "isSidechain": false,
  "requestId": "req_011CbFkCh3tNqTNb8Hz2vuvT",
  "type": "assistant",
  "uuid": "ab51674b-2185-4660-9e39-030c6a9a34d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01479zLdA7WWnnLCGABW37fE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 30741,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 121,
          "cache_read_input_tokens": 30741,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-21T12:52:30.929Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Lk9NeaW9knX3WWBmg7Ur3m`</summary>

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
  "parentUuid": "ab51674b-2185-4660-9e39-030c6a9a34d0",
  "isSidechain": false,
  "requestId": "req_011CbFkCh3tNqTNb8Hz2vuvT",
  "type": "assistant",
  "uuid": "7c2b31f0-8e1c-4811-bbc9-8a070368a1e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01479zLdA7WWnnLCGABW37fE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 30741,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 121,
          "cache_read_input_tokens": 30741,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-21T12:52:30.949Z_

<details><summary>↩ Tool result · `toolu_01Lk9NeaW9knX3WWBmg7Ur3m`</summary>

```text
config/approvals.yaml
config/backend.yaml
config/feishu.yaml
workspace.yaml
idea_generator/ideas.yaml
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
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
config/projects/xling_calib_direction.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/meta.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/meta.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/meta.yaml
projects/xling_calib_direction/writing_plan.yaml
projects/xling_calib_direction/literature_map.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/meta.yaml
projects/xling_calib_direction/artifacts/manifest.yaml
projects/xling_calib_direction/artifacts/review_issues.yaml
projects/xling_calib_direction/paper_provenance.yaml
global/approvals.yaml
config/pending_approval_notifications.yaml
config/venue_registry.yaml
config/venue_rules/corl-2026.yaml
config/venue_rules/emnlp-2026.yaml
config/crons.yaml
projects/xling_calib_direction/mistakes.yaml
projects/xling_calib_direction/decisions.yaml
projects/xling_calib_direction/dream_registry.yaml
projects/xling_calib_direction/experiment_plan.yaml
projects/xling_calib_direction/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c2b31f0-8e1c-4811-bbc9-8a070368a1e3",
  "isSidechain": false,
  "promptId": "b7585d46-2ea0-497d-8a35-64b3c1f62eec",
  "type": "user",
  "uuid": "9affd0db-00e3-45e3-addd-f7b131f31f9d",
  "toolUseResult": {
    "filenames": [
      "config/approvals.yaml",
      "config/backend.yaml",
      "config/feishu.yaml",
      "workspace.yaml",
      "idea_generator/ideas.yaml",
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
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
      "config/projects/xling_calib_direction.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/meta.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/meta.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/meta.yaml",
      "projects/xling_calib_direction/writing_plan.yaml",
      "projects/xling_calib_direction/literature_map.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/meta.yaml",
      "projects/xling_calib_direction/artifacts/manifest.yaml",
      "projects/xling_calib_direction/artifacts/review_issues.yaml",
      "projects/xling_calib_direction/paper_provenance.yaml",
      "global/approvals.yaml",
      "config/pending_approval_notifications.yaml",
      "config/venue_registry.yaml",
      "config/venue_rules/corl-2026.yaml",
      "config/venue_rules/emnlp-2026.yaml",
      "config/crons.yaml",
      "projects/xling_calib_direction/mistakes.yaml",
      "projects/xling_calib_direction/decisions.yaml",
      "projects/xling_calib_direction/dream_registry.yaml",
      "projects/xling_calib_direction/experiment_plan.yaml",
      "projects/xling_calib_direction/registry.yaml"
    ],
    "durationMs": 12,
    "numFiles": 64,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7c2b31f0-8e1c-4811-bbc9-8a070368a1e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T12:52:33.802Z_

<details open><summary>🔧 Tool call — Read · `toolu_017d8wTgW1ZPBvQjFX6Cf2NS`</summary>

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
  "parentUuid": "9affd0db-00e3-45e3-addd-f7b131f31f9d",
  "isSidechain": false,
  "requestId": "req_011CbFkD5UGV5CpGGHvm6d7d",
  "type": "assistant",
  "uuid": "8c07a84c-9d92-4bbb-a48a-4d4428dd2291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gw2hZvYaEqnR7BA8RU64Fx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 30741,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 30741,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1628
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

_source line 12 · 2026-05-21T12:52:33.812Z_

<details><summary>↩ Tool result · `toolu_017d8wTgW1ZPBvQjFX6Cf2NS`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract
5	    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,
6	    train English correctness probes (logistic regression + 2-layer MLP), evaluate
7	    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,
8	    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global
9	    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.
10	
11	    '
12	  priority: P0
13	  gpu_budget_hours: 80
14	  deps: []
15	  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required
16	    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative
17	    layers on subset — extend plan_010).
18	
19	    '
20	- id: plan_002
21	  claim: 1
22	  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract
23	    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.
24	    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).
25	    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.
26	
27	    '
28	  priority: P0
29	  gpu_budget_hours: 40
30	  deps: []
31	  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).
32	    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).
33	    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).
34	
35	    '
36	  registry_id: plan_002_v3
37	- id: plan_003
38	  claim: 3
39	  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +
40	    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English
41	    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned
42	    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations
43	    from probe_train only; evaluate exclusively on eval portion. No train split exists
44	    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient
45	    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across
46	    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α
47	    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results
48	    (50% depth + EN-optimal) alongside per-language oracle.
49	
50	    '
51	  priority: P0
52	  gpu_budget_hours: 20
53	  deps:
54	  - plan_001
55	  - plan_002
56	  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS
57	    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert
58	    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional
59	    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,
60	    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic
61	    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion
62	    (d) Initialization: from standard LR solution or from scratch (e) Batch size for
63	    MMD computation (f) Whether MMD items overlap with BCE training items or held-out
64	    (g) Parallel set size per language + translation quality note for low-resource
65	    Negative result demands higher reproducibility bar than positive. CORAL COMPARISON
66	    (D015, re-dream 2-tier consensus): Add CORAL loss (second-order alignment, Sun
67	    & Saenko 2016) as alternative to MMD. Tests whether distributional matching failure
68	    is MMD-specific or general. Trivial to implement on cached activations. Report
69	    CORAL alongside MMD in Table 7 ablation. Strengthens negative result scope. HIGH-DIM
70	    MMD (D016, dream #4 cross-tier consensus): All 3 tiers flagged "1-D logit MMD"
71	    as overclaimed scope. Test MMD on PCA-reduced activations (d=50, d=100) instead
72	    of 1-D probe logits. If high-dim also fails → broadens "distributional matching
73	    fails" claim. If high-dim works → method contribution jumps significantly. Trivial:
74	    PCA on cached activations, then MMD in reduced space. Also test with CORAL in
75	    high-dim. MULTI-SEED (D016): Run 3-5 seeds for CaCLR, few-shot (25/100), and Procrustes
76	    at representative layers. Report std across seeds. Addresses single-seed concern.
77	    MIXED β CRITERION (D016): Add 1-2 validation languages (zh, sw) to β selection
78	    criterion alongside English, to rule out systematic bias against cross-lingual
79	    benefit.
80	
81	    '
82	- id: plan_004
83	  claim: 2
84	  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge
85	    regression on human difficulty scores per Civelli et al.), project out difficulty
86	    direction from activations, retrain correctness probes on residuals, evaluate
87	    transfer. 10 representative languages × 8 representative layers per model (20-90%
88	    depth).
89	
90	    '
91	  priority: P0
92	  gpu_budget_hours: 15
93	  deps:
94	  - plan_001
95	  - plan_002
96	  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification
97	    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,
98	    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.
99	    Reduced grid is sufficient because decomposition tests a qualitative hypothesis
100	    (does projecting out difficulty help or hurt?), not a per-language quantitative
101	    claim. Include random-direction control to rule out dimensionality-reduction artifacts.
102	
103	    '
104	- id: plan_005
105	  claim: 4
106	  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence
107	    direction (prompt model for confidence score, fit probe), compute cosine similarity
108	    with correctness direction across 20 languages × 2 architectures. Analyze by resource
109	    tier (high/mid/low) and language family.
110	
111	    '
112	  priority: P1
113	  gpu_budget_hours: 10
114	  deps:
115	  - plan_001
116	  - plan_002
117	- id: plan_006
118	  claim: 1
119	  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at
120	    each probed layer for both models. Compare English accuracy, cross-lingual transfer
121	    degradation, and calibration quality. Test hypothesis: linear probes transfer
122	    better cross-lingually.
123	
124	    '
125	  priority: P1
126	  gpu_budget_hours: 5
127	  deps:
128	  - plan_001
129	  - plan_002
130	  notes: CPU-bound, uses cached activations.
131	- id: plan_007
132	  claim: 1
133	  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele
134	    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.
135	
136	    '
137	  priority: P1
138	  gpu_budget_hours: 30
139	  deps:
140	  - plan_001
141	  - plan_002
142	  - plan_003
143	- id: plan_010
144	  claim: 1
145	  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative
146	    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at
147	    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization
148	    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download
149	    of FP16 weights for subset only, then delete. May need to do sequentially due
150	    to disk constraints.
151	
152	    '
153	  priority: P1
154	  gpu_budget_hours: 10
155	  deps:
156	  - plan_001
157	  - plan_002
158	- id: plan_011
159	  claim:
160	  - 1
161	  - 4
162	  description: 'CKA cross-lingual representation similarity analysis: compute CKA
163	    (linear kernel) between English and each target language at every probed layer
164	    for both models. Full-scale validation of pilot finding: correctness direction
165	    is a robust low-dimensional subspace feature that persists despite global CKA
166	    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA
167	    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)
168	    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,
169	    and critical threshold analysis.
170	
171	    '
172	  priority: P0
173	  gpu_budget_hours: 5
174	  deps:
175	  - plan_001
176	  - plan_002
177	  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).
178	    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen
179	    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):
180	    pooled correlation has depth confound. Pilot per-language Spearman almost all
181	    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language
182	    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),
183	    not within-language depth effects. Supportable claim: "languages with higher CKA
184	    exhibit less transfer degradation" (between-language, qualitative at n=5). NOT
185	    supportable: "CKA predicts within- language degradation across depth." Full-scale
186	    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest
187	    test, n=20 per layer), (b) partial correlation controlling for normalized depth
188	    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if
189	    CKA adds no explanatory power beyond depth, downgrade framing from "geometric
190	    analysis" to "suggestive correlation", (c) per-language Spearman with denser layer
191	    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose
192	    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength
193	    difference (qualitative). Frame as "geometric/correlational analysis" NOT "mechanistic
194	    explanation" (Dream RD6/RD9).
195	
196	    '
197	- id: plan_012
198	  claim: 1
199	  description: 'Linear projection sensitivity analysis: vary number of parallel pairs
200	    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data
201	    requirement for this surprisingly strong baseline. Both models × 5 representative
202	    layers × 20 languages.
203	
204	    '
205	  priority: P1
206	  gpu_budget_hours: 2
207	  deps:
208	  - plan_001
209	  - plan_002
210	  notes: CPU-bound, uses cached activations. Dream review D11.
211	- id: plan_013
212	  claim: 1
213	  registry_id: plan_013
214	  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly
215	    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)
216	    across layers and languages. Validates that high AUROC reflects genuine correctness
217	    direction, not memorized dataset artifacts or probe capacity.
218	
219	    '
220	  priority: P1
221	  gpu_budget_hours: 2
222	  deps:
223	  - plan_001
224	  - plan_002
225	  notes: 'CPU-bound. Dream review D22: probing methodology critique. SELECTIVITY THRESHOLD
226	    SENSITIVITY (D015): Test at 0.03, 0.05, 0.10 thresholds (Hewitt & Liang used 0.05
227	    for English syntactic probing; may not be appropriate for multilingual correctness).
228	    Report artifact rate at each threshold. Trivial to compute from existing data
229	    (plan_013 v2 already running).
230	
231	    '
232	- id: plan_008
233	  claim: 1
234	  description: 'Gemma 4 32.7B Dense (60 text layers, dense, BF16): third architecture
235	    for core submission. Full Pareto frontier at every 4th layer + final (16 probed
236	    layers), 20 languages, 5 transfer conditions. BF16 (~62.5GB, fits single 96GB
237	    GPU). Provides dense vs MoE architectural contrast — addresses #1 reviewer concern
238	    across ALL dream tiers ("architecture comparison confounded").
239	
240	    '
241	  priority: P0
242	  gpu_budget_hours: 30
243	  deps: []
244	  notes: 'Upgraded P2→P0 (D016). User providing 4× RTX 6000 96G on second server.
245	    Model: google/gemma-4-31B (HF) / ModelScope. Apache 2.0, no gating. MULTIMODAL:
246	    has vision encoder (27 extra layers) — extract_activations.py must hook ONLY text
247	    decoder layers (60 layers), skip vision. Code may need adjustment. BF16 ~62.5GB
248	    (2 shards: 49.8 + 12.8GB), single 96GB GPU sufficient. No quantization needed
249	    — eliminates quantization confound for this model.
250	
251	    '
252	- id: plan_009
253	  claim: 1
254	  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.
255	    Leverages GlobalMMLU/Belebele full language sets.
256	
257	    '
258	  priority: P2
259	  gpu_budget_hours: 50
260	  deps:
261	  - plan_001
262	  - plan_002
263	- id: mvp_validation
264	  claim: 1
265	  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'
266	  priority: P0
267	  registry_id: mvp_001
268	  gpu_budget_hours: 2
269	  deps: []
270	- id: mvp_complementary
271	  claim: 1
272	  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'
273	  priority: P1
274	  registry_id: mvp_002
275	  gpu_budget_hours: 2
276	  deps:
277	  - mvp_validation
278	- id: mvp_llama_control
279	  claim: 1
280	  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'
281	  priority: P1
282	  registry_id: mvp_003
283	  gpu_budget_hours: 3
284	  deps:
285	  - mvp_validation
286	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c07a84c-9d92-4bbb-a48a-4d4428dd2291",
  "isSidechain": false,
  "promptId": "b7585d46-2ea0-497d-8a35-64b3c1f62eec",
  "type": "user",
  "uuid": "c83aed1e-b574-4841-933b-e22a67318713",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  registry_id: plan_002_v3\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive. CORAL COMPARISON\n    (D015, re-dream 2-tier consensus): Add CORAL loss (second-order alignment, Sun\n    & Saenko 2016) as alternative to MMD. Tests whether distributional matching failure\n    is MMD-specific or general. Trivial to implement on cached activations. Report\n    CORAL alongside MMD in Table 7 ablation. Strengthens negative result scope. HIGH-DIM\n    MMD (D016, dream #4 cross-tier consensus): All 3 tiers flagged \"1-D logit MMD\"\n    as overclaimed scope. Test MMD on PCA-reduced activations (d=50, d=100) instead\n    of 1-D probe logits. If high-dim also fails → broadens \"distributional matching\n    fails\" claim. If high-dim works → method contribution jumps significantly. Trivial:\n    PCA on cached activations, then MMD in reduced space. Also test with CORAL in\n    high-dim. MULTI-SEED (D016): Run 3-5 seeds for CaCLR, few-shot (25/100), and Procrustes\n    at representative layers. Report std across seeds. Addresses single-seed concern.\n    MIXED β CRITERION (D016): Add 1-2 validation languages (zh, sw) to β selection\n    criterion alongside English, to rule out systematic bias against cross-lingual\n    benefit.\n\n    '\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n- id: plan_013\n  claim: 1\n  registry_id: plan_013\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique. SELECTIVITY THRESHOLD\n    SENSITIVITY (D015): Test at 0.03, 0.05, 0.10 thresholds (Hewitt & Liang used 0.05\n    for English syntactic probing; may not be appropriate for multilingual correctness).\n    Report artifact rate at each threshold. Trivial to compute from existing data\n    (plan_013 v2 already running).\n\n    '\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 32.7B Dense (60 text layers, dense, BF16): third architecture\n    for core submission. Full Pareto frontier at every 4th layer + final (16 probed\n    layers), 20 languages, 5 transfer conditions. BF16 (~62.5GB, fits single 96GB\n    GPU). Provides dense vs MoE architectural contrast — addresses #1 reviewer concern\n    across ALL dream tiers (\"architecture comparison confounded\").\n\n    '\n  priority: P0\n  gpu_budget_hours: 30\n  deps: []\n  notes: 'Upgraded P2→P0 (D016). User providing 4× RTX 6000 96G on second server.\n    Model: google/gemma-4-31B (HF) / ModelScope. Apache 2.0, no gating. MULTIMODAL:\n    has vision encoder (27 extra layers) — extract_activations.py must hook ONLY text\n    decoder layers (60 layers), skip vision. Code may need adjustment. BF16 ~62.5GB\n    (2 shards: 49.8 + 12.8GB), single 96GB GPU sufficient. No quantization needed\n    — eliminates quantization confound for this model.\n\n    '\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n",
      "numLines": 286,
      "startLine": 1,
      "totalLines": 286
    }
  },
  "sourceToolAssistantUUID": "8c07a84c-9d92-4bbb-a48a-4d4428dd2291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T12:52:34.280Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W6UBtQUUhaAFPJ3dWYyj9R`</summary>

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
  "parentUuid": "c83aed1e-b574-4841-933b-e22a67318713",
  "isSidechain": false,
  "requestId": "req_011CbFkD5UGV5CpGGHvm6d7d",
  "type": "assistant",
  "uuid": "56ad2925-f6c3-46cf-8b68-3b9fc989a857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gw2hZvYaEqnR7BA8RU64Fx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 30741,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 30741,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1628
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

_source line 14 · 2026-05-21T12:52:34.291Z_

<details><summary>↩ Tool result · `toolu_01W6UBtQUUhaAFPJ3dWYyj9R`</summary>

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
284	    status: DONE
285	    retry_count: 0
286	    created_at: '2026-05-21T01:04:11.073Z'
287	    updated_at: '2026-05-21T12:13:02.350Z'
288	    conclusion: failed
289	    spec:
290	      command: python3 probing_controls_v2.py (PID 47972)
291	      server: westd-13176
292	      pid: 47972
293	      data_path: /root/xling_calib_direction/data/globalmmlu
294	      data_count: -1
295	      model_name: Qwen2.5-7B-Instruct
296	      seed: 42
297	      note: 已产出 L0 结果，从 PREPARING 补正状态
298	    completed_at: '2026-05-21T12:13:02.350Z'
299	  plan_002:
300	    status: DONE
301	    retry_count: 3
302	    created_at: '2026-05-21T11:46:06.605Z'
303	    updated_at: '2026-05-21T12:01:45.355Z'
304	    hypothesis: 'Cross-lingual correctness direction transfers across languages in
305	      Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed
306	      layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC
307	      ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern
308	      (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides
309	      architectural contrast to dense Qwen models.'
310	    server: westd-13176
311	    gpu: cuda:0
312	    account: root
313	    reproduce:
314	      server: westd-13176
315	      gpu: cuda:0
316	      started_at: '2026-05-21T11:47:17.654Z'
317	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
318	        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache
319	        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1
320	        && cd /root/xling_calib_direction && python -u code/extract_activations.py
321	        --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/
322	        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47
323	        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir
324	        /root/autodl-tmp/activations/llama4_scout/"
325	      finished_at: '2026-05-21T12:01:43.858Z'
326	      training_hours: 0.24
327	    failure_reason: 'CUDA OOM: CUDA out of memory. Tried to allocate 160.00 MiB. GPU
328	      0 has a total capacity of 94.97 GiB of which 25.81 MiB is free. Including non-PyTorch
329	      memory, this process has 94.94 GiB memory in use. Of the allocated memory 93.27
330	      GiB is allocated by PyTorch, a'
331	    completed_at: '2026-05-21T11:48:15.052Z'
332	    extra:
333	      hook_events:
334	      - event: on_failed
335	        action: agent
336	        ts: '2026-05-21T11:48:16.350219+00:00'
337	      - event: on_failed
338	        action: agent
339	        ts: '2026-05-21T11:54:20.808886+00:00'
340	      - event: on_failed
341	        action: agent
342	        ts: '2026-05-21T12:01:45.990550+00:00'
343	      previous_failure:
344	        conclusion: failed
345	    spec:
346	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
347	        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache
348	        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1
349	        && cd /root/xling_calib_direction && python -u code/extract_activations.py
350	        --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/
351	        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47
352	        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir
353	        /root/autodl-tmp/activations/llama4_scout/"
354	      server: westd-13176
355	      gpu:
356	      - cuda:0
357	      pid: '477148'
358	      log_path: ~/runs/xling_calib_direction/plan_002.log
359	      submitted_at: '2026-05-21T11:58:12.099Z'
360	      submitted_via: submit_training_job
361	      backend: tmux
362	      account: root
363	      wall_clock_seconds: 212.4
364	      gpu_hours: 0.06
365	    pid: '477148'
366	    log_path: ~/runs/xling_calib_direction/plan_002.log
367	    conclusion: failed
368	  plan_002_4gpu:
369	    status: DONE
370	    retry_count: 0
371	    created_at: '2026-05-21T12:06:14.731Z'
372	    updated_at: '2026-05-21T12:24:23.098Z'
373	    hypothesis: 'Cross-lingual correctness direction transfers across languages in
374	      Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed
375	      layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC
376	      ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern
377	      (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides
378	      architectural contrast to dense Qwen models. Retry of plan_002 with 4 GPUs (single-GPU
379	      OOM confirmed by dry-run).'
380	    parent: plan_002
381	    spec:
382	      command: python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/...
383	        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47
384	        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir
385	        /root/autodl-tmp/activations/llama4_scout/
386	      server: westd-13176
387	      gpu:
388	      - cuda:0
389	      - cuda:1
390	      - cuda:2
391	      - cuda:3
392	      data_path: cais/mmlu + CohereForAI/Global-MMLU (cached at /root/autodl-tmp/.hf_cache)
393	      data_count: ~14K test samples per language, 20 languages
394	      model_name: RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16
395	      seed: 42
396	      note: '4-GPU required (single GPU OOM). 3 code fixes: AutoModelForImageTextToText,
397	        language_model.model.layers, language_model.model.norm. Dry-run validated
398	        66s/sample.'
399	    server: westd-13176
400	    gpu: cuda:0,cuda:1,cuda:2,cuda:3
401	    account: root
402	    pid: '468430'
403	    log_path: ~/runs/xling_calib_direction/plan_002_4gpu.log
404	    reproduce:
405	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
406	        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache
407	        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1
408	        && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /root/xling_calib_direction
409	        && python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/
410	        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47
411	        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir
412	        /root/autodl-tmp/activations/llama4_scout/"
413	      finished_at: '2026-05-21T12:10:25.168Z'
414	    failure_reason: 'CUDA OOM: CUDA out of memory. Tried to allocate 40.00 MiB. GPU
415	      1 has a total capacity of 94.97 GiB of which 32.50 MiB is free. Process 482839
416	      has 88.03 GiB memory in use. Including non-PyTorch memory, this process has
417	      6.90 GiB memory in use. Of the allocated m'
418	    conclusion: failed
419	    completed_at: '2026-05-21T12:10:25.858Z'
420	    extra:
421	      hook_events:
422	      - event: on_failed
423	        action: agent
424	        ts: '2026-05-21T12:10:27.165461+00:00'
425	    notes: '根因纠正(Director): OOM 不是 compressed_tensors 解压问题，而是 Qwen3 dry run (PID 482839)
426	      占着 GPU 1-3（88 GiB）。4卡 dry run 在 clean GPU 上是成功的。已 kill 482839 并重新提交 plan_002_v3。'
427	  plan_002_v3:
428	    status: RUNNING
429	    retry_count: 0
430	    created_at: '2026-05-21T12:24:23.888Z'
431	    updated_at: '2026-05-21T12:47:13.329Z'
432	    hypothesis: 'Cross-lingual correctness direction transfers across languages in
433	      Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed
434	      layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC
435	      ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern
436	      (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides
437	      architectural contrast to dense Qwen models. Retry after killing Qwen3 dry run
438	      (PID 482839) that was occupying GPU 1-3.'
439	    parent: plan_002_4gpu
440	    spec:
441	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
442	        base && ... && python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/
443	        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47
444	        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir
445	        /root/autodl-tmp/activations/llama4_scout/"
446	      server: westd-13176
447	      gpu:
448	      - cuda:0
449	      - cuda:1
450	      - cuda:2
451	      - cuda:3
452	      pid: '934594'
453	      log_path: ~/runs/xling_calib_direction/plan_002_v3.log
454	      submitted_at: '2026-05-21T12:26:41.691Z'
455	      submitted_via: submit_training_job
456	      backend: tmux
457	      account: root
458	      data_path: cais/mmlu + CohereForAI/Global-MMLU (cached at /root/autodl-tmp/.hf_cache)
459	      data_count: ~14K test samples per language, 20 languages
460	      model_name: RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16
461	      seed: 42
462	      checkpoint_source: N/A (activation extraction, not eval)
463	      eval_data: N/A (activation extraction, not eval)
464	      note: Retry after killing Qwen3 dry run (PID 482839). 4 GPU clean confirmed.
465	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56ad2925-f6c3-46cf-8b68-3b9fc989a857",
  "isSidechain": false,
  "promptId": "b7585d46-2ea0-497d-8a35-64b3c1f62eec",
  "type": "user",
  "uuid": "405bd269-0790-499f-815d-6062f18b9218",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml",
      "content": "baseline: null\nexperiments:\n  mvp_001:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T14:17:02.273Z'\n    updated_at: '2026-05-20T20:26:56.163Z'\n    hypothesis: 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性\n      probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在\n      layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp\n      for ≥3/5 语言）。\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/xling_calib_direction && bash run_mvp.sh\"\n      server: westd-13176\n      gpu:\n      - cuda:0\n      pid: '9845'\n      log_path: ~/runs/xling_calib_direction/mvp_001.log\n      submitted_at: '2026-05-20T16:29:25.456Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 6824.1\n      gpu_hours: 1.9\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7541\n      en_best_layer: 27\n      en_best_ece_raw: 0.1951\n      temp_scaling_fixed:\n        L24:\n          T: 0.67\n          ECE_cal: 0.2205\n        L27:\n          T: 0.62\n          ECE_cal: 0.2216\n        note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens\n          ECE.\n      en_auroc_range:\n      - 0.6113\n      - 0.7541\n      layer_depth_delta: 0.1428\n      layers_tested:\n      - 0\n      - 4\n      - 8\n      - 12\n      - 16\n      - 20\n      - 24\n      - 27\n      zs_pass_langs:\n      - zh\n      - ar\n      - hi\n      - ko\n      zs_fail_langs:\n      - sw\n      best_zs_auroc:\n        zh: 0.686\n        ar: 0.651\n        hi: 0.652\n        ko: 0.648\n        sw: 0.56\n      mean_shift_delta_ece:\n        zh: -0.36\n        ar: -0.06\n        hi: 2.22\n        sw: 6.44\n        ko: 0.01\n      pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n        D006.\n      p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n      p2: PASS (4/5)\n      p3: PASS (14.28pp)\n      p4: FAIL (0/5, mean-shift no improvement)\n    checkpoint_path: /root/xling_calib_direction/probes/\n    log_path: /root/xling_calib_direction/results/summary.txt\n    completed_at: '2026-05-20T18:23:09.593Z'\n  mvp_002:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T16:26:27.143Z'\n    updated_at: '2026-05-20T19:29:01.161Z'\n    hypothesis: Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与\n      mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际\n      28 层，index 0-27）\n    parent: mvp_001\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/xling_calib_direction && bash run_mvp_002.sh\"\n      server: westd-13176\n      gpu:\n      - cuda:1\n      pid: '11397'\n      log_path: ~/runs/xling_calib_direction/mvp_002.log\n      submitted_at: '2026-05-20T17:01:16.028Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 6874.5\n      gpu_hours: 1.91\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7481\n      en_best_layer: 26\n      en_auroc_range:\n      - 0.6229\n      - 0.7481\n      layer_depth_delta: 0.1251\n      best_zs_auroc:\n        zh: 0.6774\n        ar: 0.6302\n        hi: 0.6068\n        sw: 0.5467\n        ko: 0.6678\n      best_zs_layer:\n        zh: 26\n        ar: 26\n        hi: 22\n        sw: 22\n        ko: 26\n      pass_fail:\n        P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n        P2_zs_auroc: PASS (4/5)\n        P3_layer_delta: PASS (12.51pp)\n        P4_mean_shift: FAIL (0/5, zero delta)\n        overall: PARTIAL\n    log_path: /root/xling_calib_direction/results_mvp002/summary.txt\n    checkpoint_path: /root/xling_calib_direction/probes_mvp002/\n    completed_at: '2026-05-20T18:55:50.484Z'\n  mvp_003:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T18:27:06.449Z'\n    updated_at: '2026-05-20T20:48:56.916Z'\n    hypothesis: 'Cross-lingual correctness direction is model-agnostic: an English-trained\n      linear probe on Llama-3.1-8B-Instruct internal representations will transfer\n      to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the\n      pattern observed in Qwen2.5-7B-Instruct (mvp_001).'\n    parent: mvp_001\n    spec:\n      command: CUDA_VISIBLE_DEVICES=2 bash /root/xling_calib_direction/run_mvp_003.sh\n      server: westd-13176\n      data_path: cais/mmlu + CohereForAI/Global-MMLU\n      data_count: ~14K test samples per language\n      model_name: LLM-Research/Meta-Llama-3.1-8B-Instruct (ModelScope)\n      seed: 42\n      gpu: cuda:2\n      tmux_session: mvp_003\n      log_path: /root/xling_calib_direction/mvp_003.log\n      checkpoint_source: LLM-Research/Meta-Llama-3.1-8B-Instruct\n      eval_data: cais/mmlu + CohereForAI/Global-MMLU\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7284\n      en_best_layer: 31\n      en_best_ece_raw: 0.2052\n      en_auroc_range:\n      - 0.6331\n      - 0.7284\n      layer_depth_delta: 0.0953\n      layers_tested:\n      - 0\n      - 4\n      - 8\n      - 12\n      - 16\n      - 20\n      - 24\n      - 28\n      - 31\n      best_zs_auroc:\n        zh: 0.64\n        ar: 0.6146\n        hi: 0.5935\n        ko: 0.6481\n        sw: 0.5838\n      best_zs_layer:\n        zh: 20\n        ar: 31\n        hi: 31\n        ko: 31\n        sw: 16\n      zs_pass_langs:\n      - zh\n      - ar\n      - hi\n      - ko\n      - sw\n      zs_fail_langs: []\n      pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n      note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n        P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n        is rank-invariant.'\n      cka_vs_degradation:\n        overall_rho: -0.3982\n        overall_p: 0.0068\n        per_lang:\n          ar:\n            rho: -0.2833\n            p: 0.46\n          hi:\n            rho: -0.6667\n            p: 0.0499\n          ko:\n            rho: 0.25\n            p: 0.5165\n          sw:\n            rho: -0.5833\n            p: 0.0992\n          zh:\n            rho: -0.4833\n            p: 0.1875\n    checkpoint_path: /root/xling_calib_direction/probes_mvp003/\n    log_path: /root/xling_calib_direction/results_mvp003/summary.txt\n    completed_at: '2026-05-20T20:34:43.102Z'\n  plan_013:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-21T00:39:58.089Z'\n    updated_at: '2026-05-21T00:59:20.023Z'\n    hypothesis: 'English correctness probes capture genuine linguistic signal: 5-fold\n      CV with PCA(100) dimensionality reduction shows real AUROC significantly above\n      permuted-label baseline (0.746 vs 0.484 at best layer), with selectivity (Hewitt\n      & Liang 2019) concentrated in later layers (L20-L27), confirming the probe is\n      not exploiting spurious high-dimensional correlations.'\n    parent: mvp_001\n    spec:\n      command: python probing_controls_v2.py (5-fold CV + PCA-100)\n      server: westd-13176\n      data_path: /root/xling_calib_direction/activations/layer*_en.pt\n      data_count: ~14K MMLU test samples\n      model_name: Qwen2.5-7B-Instruct (activations from mvp_001)\n      seed: 42\n      checkpoint_source: mvp_001 activations\n      eval_data: same activations, 5-fold CV\n    conclusion: success\n    metrics:\n      method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n      selectivity_hewitt_liang:\n        L0: 0.02\n        L4: 0.037\n        L8: 0.036\n        L12: 0.042\n        L16: 0.123\n        L20: 0.244\n        L24: 0.248\n        L27: 0.262\n      real_auroc:\n        L0: 0.501\n        L4: 0.524\n        L8: 0.529\n        L12: 0.53\n        L16: 0.615\n        L20: 0.733\n        L24: 0.738\n        L27: 0.746\n      permuted_auroc:\n        L0: 0.481\n        L4: 0.487\n        L8: 0.493\n        L12: 0.488\n        L16: 0.492\n        L20: 0.489\n        L24: 0.49\n        L27: 0.484\n      pca_variance_retained:\n        L0: 0.922\n        L4: 0.912\n        L8: 0.885\n        L12: 0.868\n        L16: 0.783\n        L20: 0.738\n        L24: 0.844\n        L27: 0.794\n      note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n        concentrated in L20-L27. PCA(100) retains 73-92% variance.\n    checkpoint_path: /root/xling_calib_direction/results/probing_controls.csv\n    log_path: /root/xling_calib_direction/results/probing_controls.csv\n    completed_at: '2026-05-21T00:59:20.023Z'\n  plan_013_probing_controls_v2:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-21T01:04:11.073Z'\n    updated_at: '2026-05-21T12:13:02.350Z'\n    conclusion: failed\n    spec:\n      command: python3 probing_controls_v2.py (PID 47972)\n      server: westd-13176\n      pid: 47972\n      data_path: /root/xling_calib_direction/data/globalmmlu\n      data_count: -1\n      model_name: Qwen2.5-7B-Instruct\n      seed: 42\n      note: 已产出 L0 结果，从 PREPARING 补正状态\n    completed_at: '2026-05-21T12:13:02.350Z'\n  plan_002:\n    status: DONE\n    retry_count: 3\n    created_at: '2026-05-21T11:46:06.605Z'\n    updated_at: '2026-05-21T12:01:45.355Z'\n    hypothesis: 'Cross-lingual correctness direction transfers across languages in\n      Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed\n      layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC\n      ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern\n      (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides\n      architectural contrast to dense Qwen models.'\n    server: westd-13176\n    gpu: cuda:0\n    account: root\n    reproduce:\n      server: westd-13176\n      gpu: cuda:0\n      started_at: '2026-05-21T11:47:17.654Z'\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache\n        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1\n        && cd /root/xling_calib_direction && python -u code/extract_activations.py\n        --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\"\n      finished_at: '2026-05-21T12:01:43.858Z'\n      training_hours: 0.24\n    failure_reason: 'CUDA OOM: CUDA out of memory. Tried to allocate 160.00 MiB. GPU\n      0 has a total capacity of 94.97 GiB of which 25.81 MiB is free. Including non-PyTorch\n      memory, this process has 94.94 GiB memory in use. Of the allocated memory 93.27\n      GiB is allocated by PyTorch, a'\n    completed_at: '2026-05-21T11:48:15.052Z'\n    extra:\n      hook_events:\n      - event: on_failed\n        action: agent\n        ts: '2026-05-21T11:48:16.350219+00:00'\n      - event: on_failed\n        action: agent\n        ts: '2026-05-21T11:54:20.808886+00:00'\n      - event: on_failed\n        action: agent\n        ts: '2026-05-21T12:01:45.990550+00:00'\n      previous_failure:\n        conclusion: failed\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache\n        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1\n        && cd /root/xling_calib_direction && python -u code/extract_activations.py\n        --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\"\n      server: westd-13176\n      gpu:\n      - cuda:0\n      pid: '477148'\n      log_path: ~/runs/xling_calib_direction/plan_002.log\n      submitted_at: '2026-05-21T11:58:12.099Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 212.4\n      gpu_hours: 0.06\n    pid: '477148'\n    log_path: ~/runs/xling_calib_direction/plan_002.log\n    conclusion: failed\n  plan_002_4gpu:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-21T12:06:14.731Z'\n    updated_at: '2026-05-21T12:24:23.098Z'\n    hypothesis: 'Cross-lingual correctness direction transfers across languages in\n      Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed\n      layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC\n      ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern\n      (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides\n      architectural contrast to dense Qwen models. Retry of plan_002 with 4 GPUs (single-GPU\n      OOM confirmed by dry-run).'\n    parent: plan_002\n    spec:\n      command: python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/...\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\n      server: westd-13176\n      gpu:\n      - cuda:0\n      - cuda:1\n      - cuda:2\n      - cuda:3\n      data_path: cais/mmlu + CohereForAI/Global-MMLU (cached at /root/autodl-tmp/.hf_cache)\n      data_count: ~14K test samples per language, 20 languages\n      model_name: RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16\n      seed: 42\n      note: '4-GPU required (single GPU OOM). 3 code fixes: AutoModelForImageTextToText,\n        language_model.model.layers, language_model.model.norm. Dry-run validated\n        66s/sample.'\n    server: westd-13176\n    gpu: cuda:0,cuda:1,cuda:2,cuda:3\n    account: root\n    pid: '468430'\n    log_path: ~/runs/xling_calib_direction/plan_002_4gpu.log\n    reproduce:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache\n        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1\n        && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /root/xling_calib_direction\n        && python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\"\n      finished_at: '2026-05-21T12:10:25.168Z'\n    failure_reason: 'CUDA OOM: CUDA out of memory. Tried to allocate 40.00 MiB. GPU\n      1 has a total capacity of 94.97 GiB of which 32.50 MiB is free. Process 482839\n      has 88.03 GiB memory in use. Including non-PyTorch memory, this process has\n      6.90 GiB memory in use. Of the allocated m'\n    conclusion: failed\n    completed_at: '2026-05-21T12:10:25.858Z'\n    extra:\n      hook_events:\n      - event: on_failed\n        action: agent\n        ts: '2026-05-21T12:10:27.165461+00:00'\n    notes: '根因纠正(Director): OOM 不是 compressed_tensors 解压问题，而是 Qwen3 dry run (PID 482839)\n      占着 GPU 1-3（88 GiB）。4卡 dry run 在 clean GPU 上是成功的。已 kill 482839 并重新提交 plan_002_v3。'\n  plan_002_v3:\n    status: RUNNING\n    retry_count: 0\n    created_at: '2026-05-21T12:24:23.888Z'\n    updated_at: '2026-05-21T12:47:13.329Z'\n    hypothesis: 'Cross-lingual correctness direction transfers across languages in\n      Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed\n      layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC\n      ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern\n      (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides\n      architectural contrast to dense Qwen models. Retry after killing Qwen3 dry run\n      (PID 482839) that was occupying GPU 1-3.'\n    parent: plan_002_4gpu\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && ... && python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\"\n      server: westd-13176\n      gpu:\n      - cuda:0\n      - cuda:1\n      - cuda:2\n      - cuda:3\n      pid: '934594'\n      log_path: ~/runs/xling_calib_direction/plan_002_v3.log\n      submitted_at: '2026-05-21T12:26:41.691Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      data_path: cais/mmlu + CohereForAI/Global-MMLU (cached at /root/autodl-tmp/.hf_cache)\n      data_count: ~14K test samples per language, 20 languages\n      model_name: RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16\n      seed: 42\n      checkpoint_source: N/A (activation extraction, not eval)\n      eval_data: N/A (activation extraction, not eval)\n      note: Retry after killing Qwen3 dry run (PID 482839). 4 GPU clean confirmed.\n",
      "numLines": 465,
      "startLine": 1,
      "totalLines": 465
    }
  },
  "sourceToolAssistantUUID": "56ad2925-f6c3-46cf-8b68-3b9fc989a857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T12:52:34.675Z_

<details open><summary>🔧 Tool call — Read · `toolu_013xj92siqpvwauqzCbgTWGp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "405bd269-0790-499f-815d-6062f18b9218",
  "isSidechain": false,
  "requestId": "req_011CbFkD5UGV5CpGGHvm6d7d",
  "type": "assistant",
  "uuid": "7cadedf1-31fa-47d5-8271-e43e5543ab89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gw2hZvYaEqnR7BA8RU64Fx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 30741,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 30741,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1628
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "7cadedf1-31fa-47d5-8271-e43e5543ab89",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiment predictions for cross-lingual correctness probe transfer",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Tool result

_source line 18 · 2026-05-21T12:52:35.081Z_

<details><summary>↩ Tool result · `toolu_013xj92siqpvwauqzCbgTWGp`</summary>

```text
1	tier: median
2	narrative_guidance: 'CaCLR consistency loss (MMD) 在完整 β sweep 中无显著 AUROC 提升，转为 negative
3	  result framing。 几何解释：MMD 匹配边际分布但无法对齐低维 directional structure——correctness 方向占据 1-3
4	  维子空间， MMD 在 1-D probe logit 空间操作无法捕捉旋转。Linear projection 直接学习子空间旋转故成功。 Simpson''s
5	  Paradox 仅在 Llama 4 Scout 上显著（partial rho~0.29, p~0.02），Qwen3-235B 上 trending 但不显著（rho~0.16,
6	  p~0.07）——用 hedged language 报告为架构依赖发现。Claim 2 decomposition 定性分离成立但 prescriptive
7	  预测力弱——弱化为 ''descriptive separation observed''。 标题转向 ''When Does Cross-Lingual Calibration
8	  Transfer Work? Geometric Analysis and Practical Solutions.'' 强化三个实用贡献：(1) linear
9	  projection ~70 pairs 推荐方案，(2) Procrustes effect reversal 阈值 ~0.55 作为 practitioner
10	  guidance，(3) ~30% low-resource probing artifacts 作为 methodological warning。 仍可投
11	  EACL——thorough empirical study + 架构依赖几何洞见 + systematic negative result + 实用指导。
12	
13	  '
14	imagined_experiments:
15	- name: Full Pareto Frontier — Qwen3-235B-A22B (MoE, INT4)
16	  plan_id: plan_001
17	  description: '94 层 MoE 模型，每 4 层取一层（24 probed layers），20 种语言，5 种 transfer 条件。 MoE
18	    路由机制在深层创建更强的语言特异化，产生比 7B pilot 更清晰的 Pareto tradeoff。
19	
20	    '
21	  expected_results:
22	    en_best_auroc: 0.78
23	    en_best_layer: 80
24	    en_best_layer_depth_pct: 0.851
25	    en_auroc_range:
26	    - 0.58
27	    - 0.78
28	    en_best_ece_raw: 0.185
29	    transfer_optimal_layer_mean: 68
30	    transfer_optimal_depth_pct: 0.723
31	    en_transfer_layer_gap_pp: 2.8
32	    zs_pass_rate: 0.75
33	    zs_pass_count: 15
34	    zs_mean_auroc_en_optimal: 0.66
35	    zs_mean_auroc_transfer_optimal: 0.682
36	    pareto_significant_langs: 15
37	    pareto_spearman_rho_median: -0.42
38	    pareto_spearman_rho_range:
39	    - -0.68
40	    - 0.15
41	    pareto_langs_negative_rho: 16
42	    best_zs_auroc_by_tier:
43	      HIGH_mean: 0.725
44	      MID_mean: 0.672
45	      LOW_mean: 0.575
46	    linear_proj_200_mean_auroc: 0.692
47	    few_shot_25_mean_auroc: 0.678
48	    few_shot_100_mean_auroc: 0.712
49	    mean_shift_delta_auroc: 0.0
50	  result_rationale: 'Qwen3-235B 的 MoE 路由在深层为不同语言激活不同 expert，加剧表征语言特异化。 EN best AUROC
51	    从 7B 的 0.754 提升至 ~0.78（+2.6pp），符合模型规模 scaling 预期（22B active params vs 7B, correctness
52	    signal 在更大模型中更强但非线性增长）。EN-optimal 在 L80（85% depth）， 而非最终层——MoE 最终层 expert 过度特化导致
53	    probe 质量微降。Pareto tradeoff 比 7B 更清晰： MoE 架构下 CKA cliff 更陡（L64-L80 急剧下降），transfer-optimal
54	    在 L68（72% depth）， EN-optimal 与 transfer-optimal 相差 ~12 层（~3pp AUROC gap），远大于 7B
55	    pilot 的 L24 vs L27（~2pp）。 ZS pass rate 75%（15/20）: HIGH 6/6 全通过（共享训练数据充分），MID
56	    6/6 通过（>0.60）， LOW 仅 3/6 通过（yo/am/my 低于 0.55）。Mean-shift 仍然恒等于 0（数学不变性）。 Linear
57	    projection 在低资源语言上提升 +0.04-0.08 但在高资源语言上可能微损。
58	
59	    '
60	  tables:
61	  - name: Per-Language ZS AUROC at EN-Optimal Layer (L80)
62	    data: '| Tier | Language | ZS AUROC | Best ZS Layer | Pareto rho | Pareto p |
63	
64	      |------|----------|----------|---------------|------------|----------|
65	
66	      | HIGH | zh       | 0.732    | L68           | -0.52      | 0.009   |
67	
68	      | HIGH | es       | 0.741    | L72           | -0.48      | 0.017   |
69	
70	      | HIGH | fr       | 0.738    | L72           | -0.45      | 0.027   |
71	
72	      | HIGH | de       | 0.720    | L68           | -0.55      | 0.005   |
73	
74	      | HIGH | pt       | 0.730    | L72           | -0.41      | 0.046   |
75	
76	      | HIGH | ja       | 0.710    | L64           | -0.58      | 0.003   |
77	
78	      | MID  | ar       | 0.690    | L64           | -0.50      | 0.013   |
79	
80	      | MID  | ru       | 0.700    | L68           | -0.44      | 0.031   |
81	
82	      | MID  | ko       | 0.685    | L64           | -0.47      | 0.021   |
83	
84	      | MID  | hi       | 0.665    | L60           | -0.38      | 0.068   |
85	
86	      | MID  | vi       | 0.678    | L64           | -0.42      | 0.041   |
87	
88	      | MID  | tr       | 0.655    | L60           | -0.35      | 0.093   |
89	
90	      | LOW  | sw       | 0.592    | L56           | -0.30      | 0.153   |
91	
92	      | LOW  | bn       | 0.608    | L60           | -0.32      | 0.126   |
93	
94	      | LOW  | th       | 0.620    | L60           | -0.37      | 0.075   |
95	
96	      | LOW  | te       | 0.568    | L56           | -0.22      | 0.301   |
97	
98	      | LOW  | yo       | 0.542    | L52           | -0.18      | 0.398   |
99	
100	      | LOW  | am       | 0.530    | L48           | 0.05       | 0.815   |
101	
102	      '
103	  - name: Transfer Method Comparison (mean across 20 languages, L80)
104	    data: '| Method              | Mean AUROC | ΔAUROC vs ZS | Sig (paired perm) |
105	
106	      |---------------------|------------|--------------|-------------------|
107	
108	      | Zero-shot           | 0.660      | —            | —                 |
109	
110	      | Mean-shift          | 0.660      | 0.000        | n/a               |
111	
112	      | CaCLR (best β=0.01) | 0.662      | +0.002       | p=0.42            |
113	
114	      | Linear proj (50)    | 0.678      | +0.018       | p=0.008           |
115	
116	      | Linear proj (200)   | 0.692      | +0.032       | p<0.001           |
117	
118	      | Few-shot 25         | 0.678      | +0.018       | p=0.006           |
119	
120	      | Few-shot 100        | 0.712      | +0.052       | p<0.001           |
121	
122	      '
123	  figures_description:
124	  - 'Pareto scatter plot: 20 个子图（每语言一个），x=EN AUROC, y=ZS AUROC， 每点为一个 probed layer（24
125	    点），颜色编码深度（浅=浅层，深=深层）， Pareto frontier 用虚线连接。HIGH 语言子图显示清晰的右下弯折（深层 EN 高但 ZS 低），
126	    LOW 语言子图点密集在左下区域，frontier 不明显。
127	
128	    '
129	  - 'Layer-wise AUROC heatmap: x=20 languages（按 tier 排列），y=24 probed layers（按深度），
130	    颜色=ZS AUROC。右上角（深层+低资源）呈冷色（低 AUROC），左中区域（中层+高资源）呈暖色。 EN 列单独标注显示 AUROC 随深度单调增加。
131	
132	    '
133	  analysis: 'Qwen3-235B 的 MoE 架构产生了比 7B pilot 更清晰的 Pareto frontier：16/20 语言的 depth-transfer
134	    rho 为负值，其中 15 个在 p<0.10 显著。Pareto 强度与资源 tier 强相关 （HIGH rho median=-0.49, MID=-0.43,
135	    LOW=-0.27），因为低资源语言整体 AUROC 低、 depth variation 也小。MoE 路由机制加速了深层表征的语言特异化——L64-L80
136	    的 expert 激活 模式在不同语言间差异显著增大，解释了 transfer cliff 为何比 dense 7B 更陡。 EN-optimal（L80）vs
137	    transfer-optimal（L68）的 gap 为实际部署提供了明确的 layer selection guidance。
138	
139	    '
140	- name: Full Pareto Frontier — Llama 4 Scout (MoE, W4A16)
141	  plan_id: plan_002
142	  description: '48 层 17B-16E MoE，每 4 层取一层（12 probed layers），20 语言，5 transfer 条件。 Llama
143	    架构族在 pilot 中显示弱 Pareto，full-scale 预期延续此模式但 MoE 可能略增 Pareto 强度。
144	
145	    '
146	  expected_results:
147	    en_best_auroc: 0.76
148	    en_best_layer: 44
149	    en_best_layer_depth_pct: 0.917
150	    en_auroc_range:
151	    - 0.6
152	    - 0.76
153	    en_best_ece_raw: 0.195
154	    transfer_optimal_layer_mean: 36
155	    transfer_optimal_depth_pct: 0.75
156	    en_transfer_layer_gap_pp: 1.5
157	    zs_pass_rate: 0.7
158	    zs_pass_count: 14
159	    zs_mean_auroc_en_optimal: 0.643
160	    zs_mean_auroc_transfer_optimal: 0.655
161	    pareto_significant_langs: 11
162	    pareto_spearman_rho_median: -0.28
163	    pareto_spearman_rho_range:
164	    - -0.55
165	    - 0.35
166	    pareto_langs_negative_rho: 13
167	    best_zs_auroc_by_tier:
168	      HIGH_mean: 0.705
169	      MID_mean: 0.652
170	      LOW_mean: 0.558
171	    linear_proj_200_mean_auroc: 0.673
172	    few_shot_25_mean_auroc: 0.662
173	    few_shot_100_mean_auroc: 0.693
174	    mean_shift_delta_auroc: 0.0
175	  result_rationale: 'Llama 4 Scout 延续 Llama-3.1-8B pilot 的弱 Pareto 模式：pilot 中仅 2/5
176	    语言显示 depth-transfer tradeoff（ar/ko 随深度改善），full-scale 中约 7/20 语言不显示 tradeoff 或方向相反。EN
177	    AUROC 从 pilot 的 0.728 提升至 0.76（Llama 4 Scout 更大），但提升幅度 小于 Qwen3 的 scaling，因为 Llama
178	    4 的 16-expert MoE 在浅层就开始 expert specialization， correctness signal 在中层已经 plateau。Pareto
179	    弱于 Qwen3 的根本原因：Llama CKA decline 更渐进（slope -0.015/layer vs Qwen 的 -0.025/layer），导致
180	    transfer 不出现急剧 cliff， tradeoff 分散在更宽的层范围内。EN-optimal（L44）vs transfer-optimal（L36）gap
181	    仅 ~1.5pp， 相比 Qwen3 的 ~2.8pp 更小。一些语言（ar, ko, vi）在全深度范围 AUROC 单调增加， 无 tradeoff——pilot
182	    中 ar/ko 的异常模式在 full-scale 中得到确认和扩展。
183	
184	    '
185	  tables:
186	  - name: Per-Language Pareto Strength Comparison (Qwen3 vs Llama 4)
187	    data: '| Tier | Language | Qwen3 rho | Qwen3 p | Llama4 rho | Llama4 p | Pattern       |
188	
189	      |------|----------|-----------|---------|------------|----------|---------------|
190	
191	      | HIGH | zh       | -0.52     | 0.009   | -0.40      | 0.198    | Both negative
192	      |
193	
194	      | HIGH | es       | -0.48     | 0.017   | -0.35      | 0.265    | Both negative
195	      |
196	
197	      | HIGH | ja       | -0.58     | 0.003   | -0.48      | 0.115    | Both negative
198	      |
199	
200	      | MID  | ar       | -0.50     | 0.013   | +0.15      | 0.641    | DIVERGENT     |
201	
202	      | MID  | ko       | -0.47     | 0.021   | +0.22      | 0.489    | DIVERGENT     |
203	
204	      | MID  | hi       | -0.38     | 0.068   | -0.55      | 0.065    | Both negative
205	      |
206	
207	      | LOW  | sw       | -0.30     | 0.153   | -0.25      | 0.432    | Weak both     |
208	
209	      | LOW  | yo       | -0.18     | 0.398   | +0.10      | 0.758    | Neither sig   |
210	
211	      '
212	  - name: Architecture Comparison Summary
213	    data: '| Metric                        | Qwen3-235B | Llama 4 Scout |
214	
215	      |-------------------------------|------------|---------------|
216	
217	      | EN best AUROC                 | 0.78       | 0.76          |
218	
219	      | Mean ZS AUROC (EN-opt layer)  | 0.660      | 0.643         |
220	
221	      | Pareto significant langs (/20)| 15         | 11            |
222	
223	      | Median per-lang Pareto rho    | -0.42      | -0.28         |
224	
225	      | CKA cliff onset (% depth)    | ~68%       | ~55%          |
226	
227	      | CKA slope (cliff region)      | -0.025/L   | -0.015/L      |
228	
229	      '
230	  figures_description:
231	  - '双模型 Pareto 对比图：左右两列分别为 Qwen3-235B 和 Llama 4 Scout，每行一个 resource tier （HIGH/MID/LOW），每子图叠加该
232	    tier 所有语言的 Pareto frontier（不同颜色）。 Qwen3 列显示 frontier 弯折更尖锐，Llama 4 列更平缓。
233	
234	    '
235	  analysis: '两个 MoE 架构的 Pareto 差异确认了 pilot 的架构依赖性发现。关键差异不在 MoE vs dense， 而在 CKA depth
236	    gradient 的斜率：Qwen3 的急剧 CKA cliff 创建清晰 tradeoff， Llama 4 的渐进下降使 tradeoff 分散。ar/ko
237	    在 Llama 4 上随深度改善的异常模式扩展到 full-scale——这些语言在 Llama tokenizer 中有较好的 subword coverage，深层
238	    expert specialization 反而增强了 correctness signal。此架构依赖性是 observational（n=2 架构， 混杂
239	    scale/layer count/training data），不做因果归因。
240	
241	    '
242	- name: CaCLR Implementation and Negative Result
243	  plan_id: plan_003
244	  description: 'CaCLR (BCE + α·SB-ECE + β·MMD) 完整实现与评估。β sweep 横跨 3 OOM (0.001-1.0)。
245	    Median tier 预期：consistency loss 无效，转为 negative result + geometric explanation。
246	
247	    '
248	  expected_results:
249	    caclr_mean_delta_auroc_vs_zs: 0.002
250	    caclr_best_beta: 0.01
251	    caclr_best_alpha: 0.3
252	    beta_sweep:
253	      beta_0.001:
254	        mean_delta_auroc: 0.001
255	        p_vs_zs: 0.71
256	      beta_0.01:
257	        mean_delta_auroc: 0.003
258	        p_vs_zs: 0.42
259	      beta_0.1:
260	        mean_delta_auroc: -0.002
261	        p_vs_zs: 0.58
262	      beta_1.0:
263	        mean_delta_auroc: -0.008
264	        p_vs_zs: 0.12
265	    alpha_sweep:
266	      alpha_0.01:
267	        mean_delta_ece: -0.2
268	        mean_delta_auroc: 0.0
269	      alpha_0.1:
270	        mean_delta_ece: -0.5
271	        mean_delta_auroc: -0.001
272	      alpha_1.0:
273	        mean_delta_ece: -1.5
274	        mean_delta_auroc: -0.004
275	      alpha_10.0:
276	        mean_delta_ece: -2.1
277	        mean_delta_auroc: -0.012
278	    component_ablation:
279	      bce_only:
280	        auroc: 0.66
281	        ece: 0.192
282	      bce_sbece:
283	        auroc: 0.658
284	        ece: 0.178
285	      bce_mmd:
286	        auroc: 0.662
287	        ece: 0.19
288	      bce_sbece_mmd:
289	        auroc: 0.661
290	        ece: 0.176
291	    method_comparison_mean_20lang:
292	      zero_shot: 0.66
293	      mean_shift: 0.66
294	      caclr_best: 0.662
295	      linear_proj_50: 0.678
296	      linear_proj_200: 0.692
297	      few_shot_25: 0.678
298	      few_shot_100: 0.712
299	    caclr_per_tier_delta:
300	      HIGH: 0.001
301	      MID: 0.003
302	      LOW: 0.002
303	    implementation_spec:
304	      mmd_kernel: Gaussian RBF, median heuristic bandwidth
305	      optimizer: Adam, lr=1e-3, cosine schedule
306	      epochs: 50
307	      early_stopping: patience=10 on val BCE loss
308	      initialization: from standard LR solution
309	      batch_size: 256
310	      mmd_items: same as BCE (probe_train split)
311	      parallel_set_size_range:
312	      - 8200
313	      - 12800
314	  result_rationale: 'CaCLR 的 MMD consistency loss 在 1-D probe logit 空间操作——这是设计层面的根本局限。
315	    Correctness direction 是高维 activation 空间中的低维子空间特征（~1-3 维），MMD 匹配 probe logit 的边际分布（均值和方差）但无法对齐子空间内的方向结构。具体地：两种语言的
316	    probe logit 分布可能有相似的均值和方差（MMD 小），但 correctness direction 在 activation 空间中的朝向不同——MMD
317	    无法检测或纠正这种旋转。β=0.001-0.01 时 consistency loss 太弱， 无实质效果；β=0.1-1.0 时 consistency
318	    loss 开始干扰 BCE 训练（AUROC 下降），因为 强制匹配边际分布反而破坏了 EN probe 已经学到的 correctness direction。这不是
319	    hyperparameter 问题——是根本的 architectural mismatch。α (SB-ECE) 对 ECE 有轻微改善 是预期的（ECE
320	    loss 直接优化 calibration），但与 cross-lingual transfer 无关。 Linear projection 成功因为它直接学习子空间旋转矩阵（Procrustes
321	    alignment）， 绕过了 distributional matching 的局限。这一对比（MMD 失败 vs linear projection 成功）
322	    提供了对 Zhao et al. (2019) conditional-marginal mismatch theory 的实证验证。
323	
324	    '
325	  tables:
326	  - name: β Sweep Results (Qwen3-235B, L80, mean across 20 languages)
327	    data: '| β     | Mean AUROC | ΔAUROC vs ZS | 95% Bootstrap CI    | Cohen''s d
328	      | Interpretation     |
329	
330	      |-------|------------|--------------|---------------------|-----------|--------------------|
331	
332	      | 0     | 0.660      | —            | —                   | —         | ZS baseline        |
333	
334	      | 0.001 | 0.661      | +0.001       | [-0.004, +0.006]    | 0.03      | Negligible         |
335	
336	      | 0.01  | 0.663      | +0.003       | [-0.003, +0.009]    | 0.07      | Negligible         |
337	
338	      | 0.1   | 0.658      | -0.002       | [-0.008, +0.004]    | 0.05      | Negligible         |
339	
340	      | 1.0   | 0.652      | -0.008       | [-0.015, -0.001]    | 0.19      | Slight
341	      degradation |
342	
343	      '
344	  - name: CaCLR vs All Methods (mean 20 languages, both models)
345	    data: '| Method            | Qwen3 AUROC | Llama4 AUROC | Mean  | Req. labels
346	      | Req. parallel |
347	
348	      |-------------------|-------------|--------------|-------|-------------|---------------|
349	
350	      | Zero-shot         | 0.660       | 0.643        | 0.652 | 0           | 0             |
351	
352	      | Mean-shift        | 0.660       | 0.643        | 0.652 | 0           | N (mean
353	      only) |
354	
355	      | CaCLR (best)      | 0.662       | 0.645        | 0.654 | 0           | ~10K
356	      parallel |
357	
358	      | Linear proj (50)  | 0.678       | 0.660        | 0.669 | 0           | 50
359	      pairs      |
360	
361	      | Linear proj (200) | 0.692       | 0.673        | 0.683 | 0           | 200
362	      pairs     |
363	
364	      | Few-shot 25       | 0.678       | 0.662        | 0.670 | 25          | 0             |
365	
366	      | Few-shot 100      | 0.712       | 0.693        | 0.703 | 100         | 0             |
367	
368	      '
369	  - name: CKA Subspace Analysis — Why MMD Fails
370	    data: '| Language Tier | Mean subspace angle (EN-target) | MMD after CaCLR | Angle
371	      after CaCLR | Interpretation            |
372	
373	      |--------------|----------------------------------|-----------------|--------------------|-----------------------------|
374	
375	      | HIGH         | 12°                              | 0.02 → 0.01     | 12° →
376	      11°         | MMD reduces, angle unchanged |
377	
378	      | MID          | 24°                              | 0.05 → 0.02     | 24° →
379	      23°         | MMD reduces, angle unchanged |
380	
381	      | LOW          | 42°                              | 0.12 → 0.05     | 42° →
382	      40°         | MMD reduces, angle unchanged |
383	
384	      '
385	  figures_description:
386	  - 'β sweep 图：x=β (log scale)，y=ΔAUROC vs zero-shot，每条线为一个 resource tier， shaded
387	    area 为 bootstrap 95% CI。所有线段在 y=0 附近震荡，β=1.0 时向下偏离。 水平虚线标注 linear projection 和
388	    few-shot 的 ΔAUROC 作为对比。
389	
390	    '
391	  - '几何解释概念图：左侧显示 MMD 操作空间（1-D logit 分布），EN 和 target 分布重叠 但 correctness direction
392	    指向不同方向（3D activation 空间投影）；右侧显示 linear projection 直接旋转子空间使 direction 对齐。
393	
394	    '
395	  analysis: 'CaCLR negative result 的核心贡献不是 method 本身，而是 (1) systematic β sweep 关闭
396	    MMD distributional-matching 路径（3 OOM, component ablation, 两个架构 × 20 语言）， (2) CKA
397	    subspace analysis 提供几何解释——MMD 成功减小了 marginal distance 但完全 无法对齐 correctness subspace
398	    的方向（subspace angle 几乎不变）。这验证了 Zhao et al. (2019) 的理论预测：当 conditional distributions
399	    P(Y|X) 在域间不同时， marginal matching 必然失败。在 correctness probing 中，P(correct|activation)
400	    的 条件结构在不同语言间确实不同（语言特异的 capability 成分），因此 MMD 注定无效。 Constructive path: linear projection
401	    以 50-80 parallel pairs 的极低成本解决了 subspace alignment 问题，是明确的 practical recommendation。
402	
403	    '
404	- name: Difficulty-Controlled Decomposition Ablation
405	  plan_id: plan_004
406	  description: 'IRT difficulty probes → project out difficulty direction → retrain
407	    correctness probes → evaluate transfer。 10 代表语言 × 8 代表层 × 两个模型。含 random-direction
408	    control。 Median tier: 定性分离成立但 prescriptive 预测能力不可靠。
409	
410	    '
411	  expected_results:
412	    mean_delta_auroc_difficulty_projected: 0.012
413	    delta_auroc_range:
414	    - -0.008
415	    - 0.025
416	    langs_with_positive_delta: 7
417	    langs_with_negative_delta: 3
418	    random_direction_mean_delta: 0.005
419	    difficulty_vs_random_ratio: 2.4
420	    difficulty_probe_r2: 0.35
421	    per_lang_results:
422	      zh:
423	        delta: 0.008
424	        sig: false
425	      es:
426	        delta: 0.01
427	        sig: false
428	      fr:
429	        delta: 0.012
430	        sig: true
431	      de:
432	        delta: 0.015
433	        sig: true
434	      hi:
435	        delta: 0.022
436	        sig: true
437	      ru:
438	        delta: 0.018
439	        sig: true
440	      ko:
441	        delta: -0.005
442	        sig: false
443	      tr:
444	        delta: 0.02
445	        sig: true
446	      sw:
447	        delta: -0.008
448	        sig: false
449	      bn:
450	        delta: 0.025
451	        sig: true
452	    prescriptive_accuracy: 0.58
453	  result_rationale: 'Difficulty decomposition 的定性逻辑成立：difficulty 成分确实是跨语言共享的（IRT difficulty
454	    与语言无关），project out 后 residual 应该更 capability-specific。但 prescriptive 力弱 的原因有三：(1)
455	    IRT difficulty probe 的 R²=0.35 意味着 difficulty direction 只解释了 35% 的方差，projection
456	    不完全；(2) difficulty 和 capability 在 activation 空间中不正交—— projection 同时移除了部分 capability
457	    信息（ko/sw 中 AUROC 下降）；(3) 不同语言中 difficulty-capability 纠缠程度不同——高资源语言 capability
458	    独立于 difficulty（projection 帮助），低资源语言两者纠缠更深（projection 效果不确定）。Random-direction control
459	    显示 ~40% 的效果来自纯维度缩减（从高维投影到低维本身就降噪），只有 ~60% 是 difficulty-specific。这足以支持 "descriptive
460	    separation observed" 但不足以支持 "prescriptive decomposition predicts optimal strategy"。Prescriptive
461	    accuracy 仅 58% （随机猜 50%），几乎无实际预测价值。
462	
463	    '
464	  tables:
465	  - name: Decomposition Results by Language (Qwen3-235B, 8-layer mean)
466	    data: '| Language | Tier | Full AUROC | Diff-projected AUROC | ΔAUROC  | Random-proj
467	      AUROC | Rand ΔAUROC |
468	
469	      |----------|------|------------|----------------------|---------|-------------------|-------------|
470	
471	      | zh       | HIGH | 0.725      | 0.733                | +0.008  | 0.729             |
472	      +0.004      |
473	
474	      | es       | HIGH | 0.735      | 0.745                | +0.010  | 0.740             |
475	      +0.005      |
476	
477	      | fr       | HIGH | 0.732      | 0.744                | +0.012  | 0.737             |
478	      +0.005      |
479	
480	      | de       | HIGH | 0.715      | 0.730                | +0.015  | 0.721             |
481	      +0.006      |
482	
483	      | hi       | MID  | 0.658      | 0.680                | +0.022  | 0.665             |
484	      +0.007      |
485	
486	      | ru       | MID  | 0.695      | 0.713                | +0.018  | 0.702             |
487	      +0.007      |
488	
489	      | ko       | MID  | 0.680      | 0.675                | -0.005  | 0.683             |
490	      +0.003      |
491	
492	      | tr       | MID  | 0.650      | 0.670                | +0.020  | 0.656             |
493	      +0.006      |
494	
495	      | sw       | LOW  | 0.585      | 0.577                | -0.008  | 0.588             |
496	      +0.003      |
497	
498	      | bn       | LOW  | 0.602      | 0.627                | +0.025  | 0.608             |
499	      +0.006      |
500	
501	      '
502	  figures_description:
503	  - '分解可视化：x=capability ΔAUROC (difficulty-projected - full)，y=difficulty  component
504	    strength (IRT probe R²)，每点为一个语言。右上象限（高 difficulty 解释力 +  positive ΔAUROC）包含 hi/bn/tr（projection
505	    帮助且 difficulty 信号强），左下象限包含 ko/sw（projection 损害或无效）。椭圆标注资源 tier。
506	
507	    '
508	  analysis: 'Decomposition 分析支持 "correctness transfer 确实包含 difficulty-shared 和 capability-specific
509	    两个成分" 的定性结论，但 prescriptive accuracy (58%) 与随机猜测差距过小（chance=50%）， 无法作为实际策略选择工具。弱化
510	    Claim 2 为 "descriptive separation observed in most language-architecture combinations;
511	    however, the decomposition does not reliably predict optimal alignment strategy."
512	    纸面贡献仍在：这是首次在跨语言 probing 中尝试 difficulty- capability 分解，定性结果与 Civelli et al. 的 difficulty
513	    transfer 文献一致。 ko/sw 的反常模式（projection 损害 AUROC）值得单独分析——可能是因为这些语言的 difficulty ordering
514	    与英语差异较大（文化特异的知识题目分布不同）。
515	
516	    '
517	- name: Cross-Lingual Orthogonality Analysis
518	  plan_id: plan_005
519	  description: '提取 verbalized confidence direction，计算与 correctness direction 的 cosine
520	    similarity， 20 语言 × 2 架构。作为 Claim 4 的 supporting evidence（subsection）。
521	
522	    '
523	  expected_results:
524	    mean_cosine_all: 0.038
525	    cosine_range:
526	    - 0.008
527	    - 0.142
528	    langs_below_0.05: 14
529	    langs_below_0.10: 18
530	    langs_above_0.10: 2
531	    per_tier_mean_cosine:
532	      HIGH: 0.028
533	      MID: 0.042
534	      LOW: 0.072
535	    architecture_comparison:
536	      qwen3_mean: 0.035
537	      llama4_mean: 0.041
538	    outlier_langs:
539	    - am
540	    - yo
541	    outlier_cosine:
542	    - 0.142
543	    - 0.118
544	  result_rationale: 'Miao & Ungar (2026) 在 English 7-8B 模型上发现 cosine < 0.04。跨语言扩展时，
545	    HIGH 资源语言复现此结果（模型在这些语言上有足够训练数据，correctness 和 confidence direction 分化清晰）。MID 语言
546	    cosine 略高（0.04-0.06）因为 confidence direction 在 中资源语言上更嘈杂（模型对这些语言的 verbalized confidence
547	    不够稳定）。LOW 语言中 am/yo 出现较高 cosine（>0.10）——这不是真正的 correctness-confidence alignment，
548	    而是 probe capacity artifact：在低资源语言上两个 direction 都很弱，cosine 被噪声主导。 plan_013 control
549	    task 将确认这些语言的 selectivity 低于阈值。整体结论不变： orthogonality 是跨语言稳健的结构性质，output-based
550	    calibration 的局限性与语言无关。 两个架构差异微小（0.035 vs 0.041），不具有统计显著性。
551	
552	    '
553	  tables:
554	  - name: Cosine Similarity by Resource Tier
555	    data: '| Tier | n  | Mean cosine | Std  | Min   | Max   | < 0.05 | < 0.10 |
556	
557	      |------|----|-------------|------|-------|-------|--------|--------|
558	
559	      | HIGH | 6  | 0.028       | 0.012| 0.012 | 0.045 | 5      | 6      |
560	
561	      | MID  | 8  | 0.042       | 0.018| 0.018 | 0.075 | 5      | 8      |
562	
563	      | LOW  | 6  | 0.072       | 0.042| 0.025 | 0.142 | 2      | 4      |
564	
565	      '
566	  figures_description:
567	  - 'Bar chart: 20 语言按 cosine 升序排列，颜色编码 resource tier。 水平虚线标注 Miao & Ungar 的 0.04
568	    阈值和 0.10 artifact 阈值。 大多数 bar 在 0.04 以下，仅 am/yo 突出。
569	
570	    '
571	  analysis: 'Orthogonality 作为 subsection supporting evidence 充分：18/20 语言 cosine <
572	    0.10， 14/20 < 0.05。结论简洁："output-based calibration 的结构性局限（correctness-confidence
573	    orthogonality）跨语言稳健，强化了 probe-based 方法的必要性。" am/yo 的高 cosine 值须与 plan_013 control
574	    task 结果交叉验证，确认是 probe artifact 而非真实 alignment。
575	
576	    '
577	- name: Probe Complexity Comparison (LR vs 2-layer MLP)
578	  plan_id: plan_006
579	  description: '每层每模型对比 logistic regression 和 2-layer MLP 的 EN accuracy、cross-lingual
580	    transfer degradation 和 calibration quality。CPU-bound，使用缓存 activations。
581	
582	    '
583	  expected_results:
584	    lr_en_best_auroc_qwen3: 0.78
585	    mlp_en_best_auroc_qwen3: 0.802
586	    lr_mean_zs_auroc_qwen3: 0.66
587	    mlp_mean_zs_auroc_qwen3: 0.632
588	    lr_transfer_gap_qwen3: 0.12
589	    mlp_transfer_gap_qwen3: 0.17
590	    lr_en_best_auroc_llama4: 0.76
591	    mlp_en_best_auroc_llama4: 0.778
592	    lr_mean_zs_auroc_llama4: 0.643
593	    mlp_mean_zs_auroc_llama4: 0.618
594	    mlp_en_advantage_pp: 2.0
595	    lr_transfer_advantage_pp: 2.8
596	    lr_preferred_for_transfer: true
597	  result_rationale: 'MLP（2 层, ~256 hidden units）有更多参数来拟合 EN correctness signal，EN
598	    AUROC 提升 ~2pp。但额外容量同时学到了 EN-specific 的 activation pattern（如 English 特有的 token
599	    position bias, subject-verb agreement cues），这些 pattern 不跨语言迁移。 LR 被迫学习更简洁的 direction（1
600	    个超平面），这个 direction 更可能对应语言无关的 correctness subspace。Transfer gap（EN - mean ZS）:
601	    LR 12pp vs MLP 17pp——MLP 多出的 5pp gap 恰好对应其 EN advantage 的 2pp + 额外 3pp 的 EN-specific
602	    overfitting。 这为 paper 的方法论选择（使用 LR probe）提供了实证支持。
603	
604	    '
605	  tables:
606	  - name: LR vs MLP Transfer Comparison (mean across 20 languages)
607	    data: '| Metric                    | Qwen3 LR | Qwen3 MLP | Llama4 LR | Llama4
608	      MLP |
609	
610	      |---------------------------|----------|-----------|-----------|------------|
611	
612	      | EN best AUROC             | 0.780    | 0.802     | 0.760     | 0.778      |
613	
614	      | Mean ZS AUROC             | 0.660    | 0.632     | 0.643     | 0.618      |
615	
616	      | Transfer gap (EN - ZS)    | 0.120    | 0.170     | 0.117     | 0.160      |
617	
618	      | EN ECE                    | 0.185    | 0.172     | 0.195     | 0.182      |
619	
620	      | Mean ZS ECE               | 0.225    | 0.252     | 0.232     | 0.260      |
621	
622	      | ZS pass rate (>0.60)      | 75%      | 60%       | 70%       | 55%        |
623	
624	      '
625	  figures_description:
626	  - 'Paired scatter plot: x=LR ZS AUROC, y=MLP ZS AUROC, 每点一个语言， 对角线 y=x 标注。大多数点在对角线下方（MLP
627	    worse），尤其是低资源语言。
628	
629	    '
630	  analysis: 'LR vs MLP 对比验证了 linear probe 是 cross-lingual transfer 的正确选择。 MLP 的额外容量在
631	    EN 上有用但在迁移中有害——这与 Hewitt & Liang (2019) 关于 probe complexity 的讨论一致。Paper 方法论选择（LR）有实证支持。
632	
633	    '
634	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
635	  plan_id: plan_007
636	  description: '在 Belebele（阅读理解）和 MMLU-ProX（翻译 MMLU）上评估 best probes + 所有 transfer
637	    方法，验证 generalization beyond GlobalMMLU。20 语言 × 2 模型。
638	
639	    '
640	  expected_results:
641	    belebele:
642	      en_best_auroc: 0.74
643	      mean_zs_auroc: 0.625
644	      zs_pass_rate: 0.6
645	      pareto_preserved: true
646	      pareto_strength: weaker than GlobalMMLU
647	      rank_correlation_with_globalmmlu: 0.82
648	    mmlu_prox:
649	      en_best_auroc: 0.77
650	      mean_zs_auroc: 0.648
651	      zs_pass_rate: 0.7
652	      pareto_preserved: true
653	      pareto_strength: comparable to GlobalMMLU
654	      rank_correlation_with_globalmmlu: 0.91
655	    linear_proj_generalizes: true
656	    caclr_still_inert: true
657	    cross_benchmark_lang_ranking_rho: 0.88
658	  result_rationale: 'Belebele 是阅读理解任务，与 GlobalMMLU 的知识型 MCQA 不同——correctness signal
659	    的性质不完全相同（RC 依赖 passage comprehension, MCQA 依赖 parametric knowledge）， 所以 EN AUROC
660	    略低（0.74 vs 0.78）且 transfer 更差。但 Pareto 结构保留，因为 depth-transferability tradeoff
661	    是 representation geometry 的性质，不依赖特定任务。 MMLU-ProX 与 GlobalMMLU 高度相关（同源翻译数据），所以模式几乎一致。
662	    Language ranking 在 benchmarks 间高度相关（rho=0.88）——确认结果不是 benchmark-specific。 CaCLR
663	    在两个 benchmark 上仍无效，linear projection 仍有效——泛化性确认。
664	
665	    '
666	  tables:
667	  - name: Cross-Benchmark Comparison (mean across 20 languages, Qwen3-235B)
668	    data: '| Metric             | GlobalMMLU | Belebele | MMLU-ProX |
669	
670	      |--------------------|------------|----------|-----------|
671	
672	      | EN best AUROC      | 0.78       | 0.74     | 0.77      |
673	
674	      | Mean ZS AUROC      | 0.660      | 0.625    | 0.648     |
675	
676	      | ZS pass rate       | 75%        | 60%      | 70%       |
677	
678	      | Pareto langs (/20) | 15         | 12       | 14        |
679	
680	      | Linear proj Δ      | +0.032     | +0.028   | +0.030    |
681	
682	      | CaCLR Δ            | +0.002     | +0.001   | +0.002    |
683	
684	      '
685	  figures_description:
686	  - '三 benchmark 平行坐标图：每条线为一个语言，x 轴为三个 benchmark， y 轴为 ZS AUROC。线条颜色编码 resource tier。大多数线大致平行（ranking
687	    一致）， 但 Belebele 整体偏低。交叉的线表示 benchmark-specific 的语言排名变化。
688	
689	    '
690	  analysis: 'Cross-benchmark 泛化确认了主要发现的稳健性。Belebele 上 Pareto 更弱是预期的 （RC task 的 correctness
691	    signal 与 knowledge MCQA 不同），但关键模式（架构差异、 resource tier 梯度、CaCLR 无效、linear projection
692	    有效）在所有 benchmark 上一致。 这为 paper 的 claim 提供了必要的泛化验证。
693	
694	    '
695	- name: Quantization Validation Ablation
696	  plan_id: plan_010
697	  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4
698	    vs FP16 for Qwen3-235B at 5 layers, 5% subset. 验证量化不扭曲 correctness signal。
699	
700	    '
701	  expected_results:
702	    llama4_w4a16_vs_fp16:
703	      mean_abs_delta_auroc: 0.005
704	      max_abs_delta_auroc: 0.009
705	      direction: mixed (2 positive, 3 negative)
706	      cka_fp16_vs_quant: 0.985
707	    qwen3_int4_vs_fp16:
708	      mean_abs_delta_auroc: 0.006
709	      max_abs_delta_auroc: 0.011
710	      direction: mixed (3 positive, 2 negative)
711	      cka_fp16_vs_quant: 0.978
712	    quantization_safe: true
713	  result_rationale: '4-bit weight quantization 保留了 activation 空间的大部分结构——correctness
714	    signal 是高维 activation 空间中的低维子空间特征，quantization noise 主要分布在与 correctness direction
715	    正交的维度上（根据 random projection 理论，低维结构 在高维 noise 下稳健）。ΔAUROC < 0.01 在 bootstrap CI
716	    内，不影响任何结论。 Qwen3 的 MoE 量化略有更大 delta（expert routing 决策在 INT4 下可能微变）， 但仍在可接受范围。CKA(FP16,
717	    quant) > 0.97 确认 activation 空间整体结构保留。
718	
719	    '
720	  tables:
721	  - name: Quantization Validation (per-layer ΔAUROC)
722	    data: '| Model      | Layer (% depth) | FP16 AUROC | Quant AUROC | ΔAUROC  |
723	
724	      |------------|-----------------|------------|-------------|---------|
725	
726	      | Llama4     | L8 (17%)        | 0.632      | 0.629       | -0.003  |
727	
728	      | Llama4     | L16 (33%)       | 0.685      | 0.688       | +0.003  |
729	
730	      | Llama4     | L24 (50%)       | 0.720      | 0.715       | -0.005  |
731	
732	      | Llama4     | L36 (75%)       | 0.748      | 0.741       | -0.007  |
733	
734	      | Llama4     | L44 (92%)       | 0.760      | 0.762       | +0.002  |
735	
736	      | Qwen3      | L16 (17%)       | 0.628      | 0.622       | -0.006  |
737	
738	      | Qwen3      | L36 (38%)       | 0.702      | 0.705       | +0.003  |
739	
740	      | Qwen3      | L52 (55%)       | 0.738      | 0.734       | -0.004  |
741	
742	      | Qwen3      | L68 (72%)       | 0.768      | 0.772       | +0.004  |
743	
744	      | Qwen3      | L80 (85%)       | 0.780      | 0.769       | -0.011  |
745	
746	      '
747	  figures_description:
748	  - 'Bland-Altman plot: x=(FP16+Quant)/2, y=FP16-Quant, 每点为一层。 水平虚线标注 ±0.01 tolerance
749	    band。所有点在 band 内。
750	
751	    '
752	  analysis: 'Quantization validation 通过——所有 ΔAUROC < 0.012，CKA > 0.97。 Qwen3 L80 的
753	    ΔAUROC=-0.011 是最大偏差，但仍在 bootstrap CI 范围内 且不影响 EN-optimal layer 的选择。Paper 中报告为
754	    "quantization artifacts are negligible for correctness probing (max |ΔAUROC| <
755	    0.012 across all validated layers)"。
756	
757	    '
758	- name: Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis
759	  plan_id: plan_011
760	  description: 'Linear CKA between EN and 20 target languages at every probed layer,
761	    both models. 核心分析：partial correlation controlling for depth（Simpson''s Paradox
762	    验证）。 Median tier: 仅 Llama 4 Scout 上显著，Qwen3 上 trending but not significant。
763	
764	    '
765	  expected_results:
766	    qwen3:
767	      raw_spearman_cka_auroc: -0.22
768	      raw_p: 0.001
769	      partial_spearman_ctrl_depth: 0.16
770	      partial_p: 0.072
771	      significant: false
772	      per_layer_positive_rho_count: 17
773	      per_layer_total: 24
774	      per_layer_significant_count: 5
775	      cka_cliff_onset_layer: 64
776	      cka_cliff_onset_depth_pct: 0.68
777	      cka_final_layer_mean: 0.1
778	      cka_peak_layer: 36
779	      cka_peak_mean: 0.81
780	    llama4:
781	      raw_spearman_cka_auroc: -0.28
782	      raw_p: 0.001
783	      partial_spearman_ctrl_depth: 0.29
784	      partial_p: 0.018
785	      significant: true
786	      per_layer_positive_rho_count: 10
787	      per_layer_total: 12
788	      per_layer_significant_count: 4
789	      cka_cliff_onset_layer: 24
790	      cka_cliff_onset_depth_pct: 0.5
791	      cka_final_layer_mean: 0.22
792	      cka_peak_layer: 12
793	      cka_peak_mean: 0.82
794	    simpson_paradox_confirmed: partial (1/2 architectures)
795	    subspace_angle_analysis:
796	      qwen3_mean_angle_HIGH: 10
797	      qwen3_mean_angle_MID: 22
798	      qwen3_mean_angle_LOW: 45
799	      llama4_mean_angle_HIGH: 12
800	      llama4_mean_angle_MID: 25
801	      llama4_mean_angle_LOW: 40
802	    cka_transfer_collapse_threshold: 0.32
803	    bootstrap_ci_partial_rho_qwen3:
804	    - -0.02
805	    - 0.34
806	    bootstrap_ci_partial_rho_llama4:
807	    - 0.06
808	    - 0.5
809	  result_rationale: 'Simpson''s Paradox 的架构依赖性源于 CKA-depth gradient 的形状差异。 Llama 4
810	    Scout 的 CKA depth gradient 更陡峭（从 peak 0.82 at L12 到 final 0.22 at L48, slope ~
811	    -0.017/layer），这使得 depth confound 更强——controlling for depth 释放了更多 CKA 的独立解释力（partial
812	    rho=0.29, p=0.018）。Qwen3 的 CKA decline 起始更晚 （L64 才开始急降）且更集中在最深层，depth confound
813	    的影响不均匀——前 60% 层几乎 无 CKA 变化，后 30% 急降——这种非线性使得 linear partial correlation 效果较差 （partial
814	    rho=0.16, p=0.072）。这不意味 CKA 在 Qwen3 上无解释力，而是 linear depth control 不够——可能需要 non-linear
815	    depth control（如 depth²）才能捕捉 Qwen3 的 step-function-like CKA profile。但 paper 应诚实报告：standard
816	    partial correlation 仅在 Llama 上显著。Per-layer analysis: 两个模型 70-83% 的 per-layer rho
817	    为正（Qwen 17/24, Llama 10/12），但因每层仅 n=20 语言，个别层的 significance 有限。Full-scale 的 n=20
818	    per layer 比 pilot 的 n=5 有更多 power，但仍不足以让所有 per-layer rho 显著。 Subspace angle 分析提供定量补充：HIGH
819	    语言角度小（10-12°）→ 零样本迁移好， LOW 语言角度大（40-45°）→ 需要 alignment。CKA collapse threshold
820	    ~0.32 是 transfer 从 "reasonable" 骤降到 "chance-level" 的拐点。
821	
822	    '
823	  tables:
824	  - name: Simpson's Paradox — Raw vs Partial Correlation
825	    data: '| Model       | n   | Raw rho | Raw p   | Partial rho | Partial p | Boot
826	      95% CI      | Sig?   |
827	
828	      |-------------|-----|---------|---------|-------------|-----------|------------------|--------|
829	
830	      | Qwen3-235B  | 480 | -0.22   | <0.001  | +0.16       | 0.072     | [-0.02,
831	      +0.34]   | No     |
832	
833	      | Llama4 Scout| 240 | -0.28   | <0.001  | +0.29       | 0.018     | [+0.06,
834	      +0.50]   | Yes    |
835	
836	      | Pilot Llama | 45  | -0.16   | 0.294   | +0.41       | 0.006     | [+0.12,
837	      +0.65]   | Yes    |
838	
839	      | Pilot Qwen  | 40  | -0.16   | 0.310   | +0.18       | 0.274     | [-0.15,
840	      +0.48]   | No     |
841	
842	      '
843	  - name: Per-Layer Cross-Language Spearman (CKA vs AUROC, n=20 per layer)
844	    data: '| Layer group        | Qwen3 median rho | Qwen3 sig layers | Llama4 median
845	      rho | Llama4 sig layers |
846	
847	      |--------------------|------------------|------------------|-------------------|-------------------|
848	
849	      | 0-25% depth        | +0.15            | 0/6              | +0.22             |
850	      1/3               |
851	
852	      | 25-50% depth       | +0.38            | 2/6              | +0.45             |
853	      2/3               |
854	
855	      | 50-75% depth       | +0.42            | 2/6              | +0.52             |
856	      2/3               |
857	
858	      | 75-100% depth      | +0.28            | 1/6              | +0.35             |
859	      1/3               |
860	
861	      '
862	  - name: CKA Depth Profile (mean across 20 languages)
863	    data: '| Depth % | Qwen3 Layer | Qwen3 CKA | Llama4 Layer | Llama4 CKA |
864	
865	      |---------|-------------|-----------|--------------|------------|
866	
867	      | 0%      | 0           | 0.72      | 0            | 0.60       |
868	
869	      | 17%     | 16          | 0.75      | 8            | 0.80       |
870	
871	      | 34%     | 32          | 0.80      | 16           | 0.76       |
872	
873	      | 51%     | 48          | 0.78      | 24           | 0.58       |
874	
875	      | 68%     | 64          | 0.62      | 32           | 0.42       |
876	
877	      | 77%     | 72          | 0.40      | 36           | 0.35       |
878	
879	      | 85%     | 80          | 0.25      | 40           | 0.30       |
880	
881	      | 94%     | 88          | 0.14      | 44           | 0.25       |
882	
883	      | 100%    | 92          | 0.10      | 48           | 0.22       |
884	
885	      '
886	  - name: Subspace Angle Analysis (correctness direction EN vs target)
887	    data: '| Tier | Qwen3 mean angle | Llama4 mean angle | Mean ZS AUROC | Interpretation         |
888	
889	      |------|------------------|-------------------|---------------|------------------------|
890	
891	      | HIGH | 10°              | 12°               | 0.715         | Near-aligned           |
892	
893	      | MID  | 22°              | 25°               | 0.662         | Modest rotation        |
894	
895	      | LOW  | 45°              | 40°               | 0.567         | Substantial
896	      misalignment|
897	
898	      '
899	  figures_description:
900	  - 'Simpson''s Paradox 可视化（核心图）：scatter plot, x=CKA, y=ZS AUROC。 每点为一个 (layer, language)
901	    pair。颜色编码 normalized depth (0-1)。 左图 Qwen3 (480 points)，右图 Llama4 (240 points)。
902	    Overall trend line 斜率为负（黑色虚线），per-depth-bin trend lines 斜率为正 （彩色实线，对应不同深度 bin）。Sign
903	    reversal 清晰可见。 Annotation: "Raw rho=−0.22 (p<0.001) vs Partial rho=+0.16 (p=0.07)"
904	    for Qwen3, "Raw rho=−0.28 (p<0.001) vs Partial rho=+0.29 (p=0.018)" for Llama4.
905	
906	    '
907	  - 'CKA × layer × language heatmap: 两个 panel（一个 per model），x=20 languages （按 mean
908	    CKA 排序），y=probed layers。颜色=CKA 值。显示 CKA cliff 在 Qwen3 上 更突然（L64 以上的条带从暖色骤变冷色），在
909	    Llama4 上更渐进。
910	
911	    '
912	  analysis: 'Simpson''s Paradox 在 full-scale 上部分确认：Llama 4 Scout 上统计显著（partial rho=0.29,
913	    p=0.018），Qwen3-235B 上 trending 但不显著（partial rho=0.16, p=0.072）。 这一架构依赖性本身是有意义的发现。Paper
914	    中用 hedged language 报告： "In architectures where the CKA-depth gradient is steep
915	    (Llama 4 Scout), partial correlation controlling for depth reveals a significant
916	    positive relationship between CKA and transfer AUROC (rho=0.29, p=0.018), indicating
917	    that CKA provides genuine explanatory power beyond depth. In architectures with
918	    a delayed, step-function-like CKA decline (Qwen3-235B), the linear partial correlation
919	    is trending but not significant (rho=0.16, p=0.072), possibly because the non-linear
920	    depth-CKA relationship reduces the effectiveness of linear depth control." Subspace
921	    angle analysis 提供了 CKA 分析的定量补充——HIGH 语言角度小（zero-shot 可行）， LOW 语言角度大（需要 alignment）——这与
922	    Procrustes reversal 发现互洽。
923	
924	    '
925	- name: Linear Projection Sensitivity & Procrustes Effect Reversal
926	  plan_id: plan_012
927	  description: 'Vary parallel pairs (10, 20, 50, 100, 200) for linear projection。
928	    两模型 × 5 代表层 × 20 语言。Resource-tier stratified saturation curves。 含 Procrustes effect
929	    reversal 分析。
930	
931	    '
932	  expected_results:
933	    overall_pairs_to_95pct: 70
934	    per_tier_pairs_to_95pct:
935	      HIGH: 35
936	      MID: 55
937	      LOW: 75
938	    saturation_curve:
939	      pairs_10:
940	        pct_of_max: 0.42
941	        mean_delta_auroc: 0.013
942	      pairs_20:
943	        pct_of_max: 0.62
944	        mean_delta_auroc: 0.02
945	      pairs_50:
946	        pct_of_max: 0.84
947	        mean_delta_auroc: 0.027
948	      pairs_100:
949	        pct_of_max: 0.95
950	        mean_delta_auroc: 0.03
951	      pairs_200:
952	        pct_of_max: 1.0
953	        mean_delta_auroc: 0.032
954	    procrustes_reversal:
955	      threshold_estimate: 0.55
956	      threshold_ci_95:
957	      - 0.46
958	      - 0.63
959	      benefit_below_0.50:
960	        mean_delta: 0.058
961	        n_langs: 4
962	      ambiguous_0.50_0.62:
963	        mean_delta: 0.012
964	        n_langs: 8
965	      harm_above_0.62:
966	        mean_delta: -0.018
967	        n_langs: 8
968	    curve_cleanness: 'noisy, especially LOW tier (R² of saturation fit: HIGH=0.96,
969	      MID=0.91, LOW=0.78)'
970	  result_rationale: 'Linear projection（Procrustes alignment）通过学习 EN→target 的旋转矩阵对齐
971	    correctness subspace。Saturation 速度取决于子空间旋转的复杂度：HIGH 语言的 EN-target subspace 角度小（~10°），10-20
972	    pairs 就足以估计一个简单旋转，35 pairs 达到 95%；LOW 语言角度大 （~40-45°），需要更多 pairs 来稳定估计更复杂的旋转，75
973	    pairs 才达到 95%。 Overall 70 pairs（而非 pilot 预估的 ~50 pairs）因为 (1) 20 语言比 5 语言引入更多方差，
974	    (2) 部分低资源语言的 parallel data 翻译质量低（机翻 artifacts），增加了 noise。 Curves 在 LOW tier 不够干净（R²=0.78）——个别语言的饱和曲线不单调（20
975	    pairs 时偶然 好于 50 pairs），因为 parallel pair 的质量方差大。 Procrustes reversal 的机制：当 ZS AUROC
976	    已高（>0.62），EN probe 的 correctness direction 与 target 语言已经 well-aligned（subspace
977	    angle <15°），Procrustes 旋转引入的估计噪声 反而大于 alignment gain→净效果为负。当 ZS AUROC 低（<0.50），严重
978	    misalignment （angle >40°）使得 Procrustes 的 alignment gain 远大于估计噪声→净效果明显为正。 阈值 ~0.55
979	    对应 subspace angle ~20-25° 的平衡点。
980	
981	    '
982	  tables:
983	  - name: Saturation Curves by Resource Tier (Qwen3-235B, L68)
984	    data: '| Pairs | HIGH ΔAUROC | MID ΔAUROC | LOW ΔAUROC | Overall ΔAUROC |
985	
986	      |-------|-------------|------------|------------|----------------|
987	
988	      | 10    | +0.002      | +0.010     | +0.028     | +0.013         |
989	
990	      | 20    | +0.005      | +0.018     | +0.042     | +0.020         |
991	
992	      | 50    | +0.007      | +0.026     | +0.054     | +0.027         |
993	
994	      | 100   | +0.008      | +0.029     | +0.060     | +0.030         |
995	
996	      | 200   | +0.008      | +0.030     | +0.063     | +0.032         |
997	
998	      '
999	  - name: Procrustes Effect Reversal by ZS AUROC Band
1000	    data: '| ZS AUROC band | n langs | Mean Δ from proj | Std   | % positive | Example
1001	      langs |
1002	
1003	      |---------------|---------|------------------|-------|------------|---------------|
1004	
1005	      | < 0.50        | 4       | +0.058           | 0.022 | 100%       | am, yo,
1006	      my, te|
1007	
1008	      | 0.50 - 0.55   | 2       | +0.035           | 0.018 | 100%       | sw, bn        |
1009	
1010	      | 0.55 - 0.60   | 2       | +0.012           | 0.015 | 75%        | th, tr        |
1011	
1012	      | 0.60 - 0.65   | 4       | +0.003           | 0.012 | 50%        | hi, vi,
1013	      ko, ar|
1014	
1015	      | 0.65 - 0.70   | 4       | -0.008           | 0.010 | 25%        | ru, ja,
1016	      de, pt|
1017	
1018	      | > 0.70        | 4       | -0.018           | 0.008 | 0%         | zh, es,
1019	      fr, ...  |
1020	
1021	      '
1022	  figures_description:
1023	  - 'Saturation curve plot: x=number of parallel pairs (log scale), y=ΔAUROC vs zero-shot。
1024	    三条线（HIGH/MID/LOW tier），每条带 shaded bootstrap 95% CI。 HIGH 线快速 plateau（30-40 pairs
1025	    后几乎 flat），LOW 线缓慢上升且 CI 更宽。 Horizontal dashed line 标注 "95% of max improvement"。
1026	
1027	    '
1028	  - 'Procrustes reversal scatter: x=ZS AUROC (zero-shot baseline), y=ΔAUROC from linear
1029	    projection (200 pairs)。每点一个 (language, model) pair，颜色编码 model。 LOESS 拟合曲线显示从正到负的渐变。Vertical
1030	    band 标注 reversal threshold 及 95% CI。
1031	
1032	    '
1033	  analysis: 'Linear projection 的 sample efficiency 是最直接的 practical contribution： 70
1034	    parallel pairs（约 2-3 小时标注工作）达到 95% of maximum improvement。 Resource-tier stratification
1035	    为 practitioners 提供指导：HIGH 语言不需要 projection （可能有害），LOW 语言需要 ~75 pairs。Procrustes
1036	    reversal 是重要的 practitioner caveat： 不加区分地对所有语言做 alignment 会损害已经 well-aligned 的语言。
1037	    建议 deployment strategy: 先测试 zero-shot AUROC，低于 0.55 时使用 linear projection， 高于
1038	    0.62 时直接使用 zero-shot。
1039	
1040	    '
1041	- name: Probing Control Tasks (Hewitt & Liang 2019) — Full Scale
1042	  plan_id: plan_013
1043	  description: '随机排列标签训练 control probes，计算 selectivity (real - control AUROC)， 2 模型
1044	    × 20 语言 × 所有 probed 层。验证 AUROC 反映 genuine correctness direction。
1045	
1046	    '
1047	  expected_results:
1048	    artifact_rate_low_resource: 0.3
1049	    artifact_rate_mid_resource: 0.28
1050	    artifact_rate_high_resource: 0.06
1051	    artifact_threshold_selectivity: 0.05
1052	    overall_artifact_rate: 0.18
1053	    en_selectivity_profile:
1054	      shallow: 0.03
1055	      mid: 0.12
1056	      deep: 0.25
1057	    per_tier_selectivity_deep_layers:
1058	      HIGH: 0.22
1059	      MID: 0.14
1060	      LOW: 0.06
1061	    control_auroc_range:
1062	    - 0.48
1063	    - 0.52
1064	    affected_layer_range: primarily layers 0-40% depth
1065	  result_rationale: 'Pilot（Qwen2.5-7B, EN）显示 selectivity 在浅层低（L0-L12: 0.02-0.04）、深层高
1066	    （L20-L27: 0.24-0.26）。跨语言扩展时，LOW 资源语言的 selectivity 全面下降： (1) 这些语言的 activations
1067	    中 correctness signal 更弱（模型对这些语言"知道"更少）， (2) probe 在小 activation difference 上更依赖
1068	    capacity 来拟合训练集。 LOW 资源语言在深层的 selectivity 仅 ~0.06（vs EN 的 ~0.25），许多 layer-language
1069	    组合的 selectivity < 0.05 artifact threshold。30% 的 LOW resource layer-language 组合为
1070	    artifacts。MID 资源语言出乎意料地也有 ~28% artifact rate——这是因为 MID 资源语言中包含一些 "表面高资源但 knowledge
1071	    coverage 低" 的语言（如 tr, vi: 模型训练数据中 token 多但 MMLU 领域覆盖差）。HIGH 资源语言 artifact rate
1072	    仅 6% （仅在最浅层 L0-L4）。这一发现波及范围比初始预期更广（从 "~28% low-resource" 扩展到 "~28% low + ~28%
1073	    mid"），强化了 methodological warning 的重要性。
1074	
1075	    '
1076	  tables:
1077	  - name: Artifact Rate by Resource Tier and Depth (Qwen3-235B)
1078	    data: '| Depth zone     | HIGH artifact % | MID artifact % | LOW artifact % |
1079	
1080	      |----------------|-----------------|----------------|----------------|
1081	
1082	      | 0-25% depth    | 17%             | 58%            | 83%            |
1083	
1084	      | 25-50% depth   | 4%              | 33%            | 67%            |
1085	
1086	      | 50-75% depth   | 0%              | 17%            | 17%            |
1087	
1088	      | 75-100% depth  | 0%              | 4%             | 0%             |
1089	
1090	      | Overall        | 6%              | 28%            | 30%            |
1091	
1092	      '
1093	  - name: Selectivity at EN-Optimal Layer by Language
1094	    data: '| Tier | Language | Real AUROC | Control AUROC | Selectivity | Artifact?
1095	      |
1096	
1097	      |------|----------|------------|---------------|-------------|-----------|
1098	
1099	      | HIGH | zh       | 0.732      | 0.498         | 0.234       | No        |
1100	
1101	      | HIGH | es       | 0.741      | 0.495         | 0.246       | No        |
1102	
1103	      | MID  | hi       | 0.665      | 0.502         | 0.163       | No        |
1104	
1105	      | MID  | tr       | 0.655      | 0.508         | 0.147       | No        |
1106	
1107	      | LOW  | sw       | 0.592      | 0.505         | 0.087       | No        |
1108	
1109	      | LOW  | bn       | 0.608      | 0.501         | 0.107       | No        |
1110	
1111	      | LOW  | yo       | 0.542      | 0.510         | 0.032       | YES       |
1112	
1113	      | LOW  | am       | 0.530      | 0.512         | 0.018       | YES       |
1114	
1115	      '
1116	  figures_description:
1117	  - 'Selectivity heatmap: x=20 languages (按 tier 排列)，y=probed layers (按深度)， 颜色=selectivity。左下区域（浅层
1118	    + 低资源）为深蓝色（artifact zone, selectivity < 0.05）, 右上区域（深层 + 高资源）为暖色。虚线框标注 artifact
1119	    zone boundary。 第二行小图：同样 heatmap 但二值化（artifact yes/no），清晰显示 30% LOW + 28% MID 覆盖率。
1120	
1121	    '
1122	  analysis: 'Control task 发现是独立的 methodological contribution：首次在 cross-lingual probing
1123	    中 系统性应用 Hewitt & Liang selectivity analysis，发现 ~30% low-resource 和 ~28% mid-resource
1124	    language-layer 组合的 probing results 不可靠。Field-level implication: 所有 cross-lingual
1125	    probing 研究（包括 Xiao et al.）应包含 selectivity checks。 在 paper 中：(1) 用 selectivity
1126	    threshold 过滤不可靠结果后重新报告 main results （确认过滤后结论不变），(2) 将过滤信息作为 methodological recommendation
1127	    在 main body 报告（不只是 appendix），(3) 讨论与 Voita & Titov MDL probes 的关系。
1128	
1129	    '
1130	- name: Gemma 4 31B Dense — Third Architecture
1131	  plan_id: plan_008
1132	  description: 'Dense 架构对照（vs 两个 MoE），60 层 FP16，20+ 语言。 提供 dense vs MoE 架构对比。Camera-ready
1133	    extension。
1134	
1135	    '
1136	  expected_results:
1137	    en_best_auroc: 0.77
1138	    en_best_layer: 52
1139	    en_best_layer_depth_pct: 0.867
1140	    mean_zs_auroc: 0.655
1141	    zs_pass_rate: 0.72
1142	    pareto_strength: intermediate (between Qwen3 and Llama4)
1143	    pareto_significant_langs: 13
1144	    cka_cliff_slope: -0.012
1145	    cka_cliff_onset_depth_pct: 0.6
1146	    partial_rho_cka: 0.22
1147	    partial_p: 0.045
1148	    simpson_significant: true
1149	  result_rationale: 'Dense 架构的 CKA decline 比 MoE 更渐进（无 expert routing 加速特异化）， slope
1150	    ~-0.012/layer vs MoE 的 -0.015 to -0.025。Pareto 强度介于 Qwen3（最强） 和 Llama4（最弱）之间。Simpson''s
1151	    Paradox 在 Gemma 4 上显著（partial rho=0.22, p=0.045）——CKA gradient 斜率介于两者之间，足以使 linear
1152	    partial correlation 有效。 如果 Gemma 4 的 partial correlation 也显著，则 Simpson''s Paradox
1153	    变为 2/3 架构显著， 可强化叙事（但 camera-ready only）。EN AUROC ~0.77 与 Qwen3 的 0.78 接近 （31B
1154	    dense vs 22B active MoE, 参数效率相当）。
1155	
1156	    '
1157	  tables:
1158	  - name: Three-Architecture Comparison (Camera-Ready)
1159	    data: '| Metric                 | Qwen3-235B | Llama4 Scout | Gemma4 31B |
1160	
1161	      |------------------------|------------|--------------|------------|
1162	
1163	      | Type                   | MoE        | MoE          | Dense      |
1164	
1165	      | Active params          | 22B        | 17B          | 31B        |
1166	
1167	      | Layers                 | 94         | 48           | 60         |
1168	
1169	      | EN best AUROC          | 0.78       | 0.76         | 0.77       |
1170	
1171	      | Mean ZS AUROC          | 0.660      | 0.643        | 0.655      |
1172	
1173	      | Pareto sig langs       | 15         | 11           | 13         |
1174	
1175	      | Partial rho (CKA)      | 0.16 (ns)  | 0.29**       | 0.22*      |
1176	
1177	      | CKA cliff slope        | -0.025     | -0.015       | -0.012     |
1178	
1179	      '
1180	  figures_description:
1181	  - '三架构 CKA depth profile 对比：x=normalized depth (0-1)，y=mean CKA (20 langs)。 三条线：Qwen3（late
1182	    sharp cliff），Llama4（early gradual decline）， Gemma4（intermediate）。Annotation 标注
1183	    cliff onset 和 slope。
1184	
1185	    '
1186	  analysis: 'Gemma 4 作为 dense 架构对照，确认 Pareto 和 Simpson''s Paradox 不是 MoE 特有。 三架构对比暗示
1187	    CKA cliff slope 可能是决定 Pareto 强度和 partial correlation 显著性的关键因素——但 n=3 架构仅为 suggestive
1188	    correlation，不能做因果推断。 Camera-ready 增加第三个架构使结论更稳健。
1189	
1190	    '
1191	- name: Extended Language Coverage (50+ Languages)
1192	  plan_id: plan_009
1193	  description: '从 20 扩展至 50+ 语言，利用 GlobalMMLU/Belebele 全语言集。Camera-ready extension。
1194	
1195	    '
1196	  expected_results:
1197	    total_languages: 52
1198	    zs_pass_rate_52: 0.62
1199	    artifact_rate_very_low_resource: 0.48
1200	    new_low_resource_langs_with_artifacts: 18
1201	    resource_tier_gradient_confirmed: true
1202	    rank_correlation_20_vs_52: 0.94
1203	    new_findings: diminishing returns; very-low-resource languages (< 1M tokens in
1204	      training) uniformly fail
1205	    min_zs_auroc: 0.49
1206	    min_zs_lang: Haitian Creole (ht)
1207	  result_rationale: '扩展到 52 语言主要增加低资源语言。新增的 32 语言大多为 LOW 或 VERY-LOW resource， ZS AUROC
1208	    多在 0.50-0.58 范围。Pass rate 从 20 语言的 ~72% 降到 52 语言的 ~62%， 因为新增语言偏向低资源。Resource-tier
1209	    gradient 在更大规模上确认——artifact rate 在 very-low-resource 语言（<1M training tokens）中达
1210	    48%，几乎一半结果不可靠。 但 20 语言的核心发现在 52 语言上完全保持（rank correlation 0.94）。 边际收益递减：每增加一种语言，对核心
1211	    claim 的增量证据很小。 主要贡献是增加统计功效和覆盖度，而非新发现。
1212	
1213	    '
1214	  tables:
1215	  - name: Language Coverage Expansion Summary
1216	    data: '| Tier        | 20-lang count | 52-lang count | Mean ZS AUROC | Artifact
1217	      rate |
1218	
1219	      |-------------|---------------|---------------|---------------|---------------|
1220	
1221	      | HIGH        | 6             | 8             | 0.72          | 4%            |
1222	
1223	      | MID         | 8             | 14            | 0.66          | 22%           |
1224	
1225	      | LOW         | 6             | 18            | 0.57          | 35%           |
1226	
1227	      | VERY-LOW    | 0             | 12            | 0.52          | 48%           |
1228	
1229	      '
1230	  figures_description:
1231	  - 'World map: 52 语言标注在地图上，颜色编码 ZS AUROC（绿=高，红=低）。 清晰显示 Western Europe 和 East Asia
1232	    为绿色，Sub-Saharan Africa 和 Southeast Asia 低资源语言为红色。
1233	
1234	    '
1235	  analysis: Camera-ready 的 52 语言扩展提供了更全面的覆盖，但 story 不变。 VERY-LOW resource 语言（ht, rm,
1236	    fy 等）的 ~48% artifact rate 强化了 probing control 的必要性。Paper 中报告 52 语言结果但 core analysis
1237	    仍基于 20 语言（统计方法学更干净）。
1238	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cadedf1-31fa-47d5-8271-e43e5543ab89",
  "isSidechain": false,
  "promptId": "b7585d46-2ea0-497d-8a35-64b3c1f62eec",
  "type": "user",
  "uuid": "794ca727-d9ab-4e2e-8f0a-31b40edeed9d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/imagined_experiments.yaml",
      "content": "tier: median\nnarrative_guidance: 'CaCLR consistency loss (MMD) 在完整 β sweep 中无显著 AUROC 提升，转为 negative\n  result framing。 几何解释：MMD 匹配边际分布但无法对齐低维 directional structure——correctness 方向占据 1-3\n  维子空间， MMD 在 1-D probe logit 空间操作无法捕捉旋转。Linear projection 直接学习子空间旋转故成功。 Simpson''s\n  Paradox 仅在 Llama 4 Scout 上显著（partial rho~0.29, p~0.02），Qwen3-235B 上 trending 但不显著（rho~0.16,\n  p~0.07）——用 hedged language 报告为架构依赖发现。Claim 2 decomposition 定性分离成立但 prescriptive\n  预测力弱——弱化为 ''descriptive separation observed''。 标题转向 ''When Does Cross-Lingual Calibration\n  Transfer Work? Geometric Analysis and Practical Solutions.'' 强化三个实用贡献：(1) linear\n  projection ~70 pairs 推荐方案，(2) Procrustes effect reversal 阈值 ~0.55 作为 practitioner\n  guidance，(3) ~30% low-resource probing artifacts 作为 methodological warning。 仍可投\n  EACL——thorough empirical study + 架构依赖几何洞见 + systematic negative result + 实用指导。\n\n  '\nimagined_experiments:\n- name: Full Pareto Frontier — Qwen3-235B-A22B (MoE, INT4)\n  plan_id: plan_001\n  description: '94 层 MoE 模型，每 4 层取一层（24 probed layers），20 种语言，5 种 transfer 条件。 MoE\n    路由机制在深层创建更强的语言特异化，产生比 7B pilot 更清晰的 Pareto tradeoff。\n\n    '\n  expected_results:\n    en_best_auroc: 0.78\n    en_best_layer: 80\n    en_best_layer_depth_pct: 0.851\n    en_auroc_range:\n    - 0.58\n    - 0.78\n    en_best_ece_raw: 0.185\n    transfer_optimal_layer_mean: 68\n    transfer_optimal_depth_pct: 0.723\n    en_transfer_layer_gap_pp: 2.8\n    zs_pass_rate: 0.75\n    zs_pass_count: 15\n    zs_mean_auroc_en_optimal: 0.66\n    zs_mean_auroc_transfer_optimal: 0.682\n    pareto_significant_langs: 15\n    pareto_spearman_rho_median: -0.42\n    pareto_spearman_rho_range:\n    - -0.68\n    - 0.15\n    pareto_langs_negative_rho: 16\n    best_zs_auroc_by_tier:\n      HIGH_mean: 0.725\n      MID_mean: 0.672\n      LOW_mean: 0.575\n    linear_proj_200_mean_auroc: 0.692\n    few_shot_25_mean_auroc: 0.678\n    few_shot_100_mean_auroc: 0.712\n    mean_shift_delta_auroc: 0.0\n  result_rationale: 'Qwen3-235B 的 MoE 路由在深层为不同语言激活不同 expert，加剧表征语言特异化。 EN best AUROC\n    从 7B 的 0.754 提升至 ~0.78（+2.6pp），符合模型规模 scaling 预期（22B active params vs 7B, correctness\n    signal 在更大模型中更强但非线性增长）。EN-optimal 在 L80（85% depth）， 而非最终层——MoE 最终层 expert 过度特化导致\n    probe 质量微降。Pareto tradeoff 比 7B 更清晰： MoE 架构下 CKA cliff 更陡（L64-L80 急剧下降），transfer-optimal\n    在 L68（72% depth）， EN-optimal 与 transfer-optimal 相差 ~12 层（~3pp AUROC gap），远大于 7B\n    pilot 的 L24 vs L27（~2pp）。 ZS pass rate 75%（15/20）: HIGH 6/6 全通过（共享训练数据充分），MID\n    6/6 通过（>0.60）， LOW 仅 3/6 通过（yo/am/my 低于 0.55）。Mean-shift 仍然恒等于 0（数学不变性）。 Linear\n    projection 在低资源语言上提升 +0.04-0.08 但在高资源语言上可能微损。\n\n    '\n  tables:\n  - name: Per-Language ZS AUROC at EN-Optimal Layer (L80)\n    data: '| Tier | Language | ZS AUROC | Best ZS Layer | Pareto rho | Pareto p |\n\n      |------|----------|----------|---------------|------------|----------|\n\n      | HIGH | zh       | 0.732    | L68           | -0.52      | 0.009   |\n\n      | HIGH | es       | 0.741    | L72           | -0.48      | 0.017   |\n\n      | HIGH | fr       | 0.738    | L72           | -0.45      | 0.027   |\n\n      | HIGH | de       | 0.720    | L68           | -0.55      | 0.005   |\n\n      | HIGH | pt       | 0.730    | L72           | -0.41      | 0.046   |\n\n      | HIGH | ja       | 0.710    | L64           | -0.58      | 0.003   |\n\n      | MID  | ar       | 0.690    | L64           | -0.50      | 0.013   |\n\n      | MID  | ru       | 0.700    | L68           | -0.44      | 0.031   |\n\n      | MID  | ko       | 0.685    | L64           | -0.47      | 0.021   |\n\n      | MID  | hi       | 0.665    | L60           | -0.38      | 0.068   |\n\n      | MID  | vi       | 0.678    | L64           | -0.42      | 0.041   |\n\n      | MID  | tr       | 0.655    | L60           | -0.35      | 0.093   |\n\n      | LOW  | sw       | 0.592    | L56           | -0.30      | 0.153   |\n\n      | LOW  | bn       | 0.608    | L60           | -0.32      | 0.126   |\n\n      | LOW  | th       | 0.620    | L60           | -0.37      | 0.075   |\n\n      | LOW  | te       | 0.568    | L56           | -0.22      | 0.301   |\n\n      | LOW  | yo       | 0.542    | L52           | -0.18      | 0.398   |\n\n      | LOW  | am       | 0.530    | L48           | 0.05       | 0.815   |\n\n      '\n  - name: Transfer Method Comparison (mean across 20 languages, L80)\n    data: '| Method              | Mean AUROC | ΔAUROC vs ZS | Sig (paired perm) |\n\n      |---------------------|------------|--------------|-------------------|\n\n      | Zero-shot           | 0.660      | —            | —                 |\n\n      | Mean-shift          | 0.660      | 0.000        | n/a               |\n\n      | CaCLR (best β=0.01) | 0.662      | +0.002       | p=0.42            |\n\n      | Linear proj (50)    | 0.678      | +0.018       | p=0.008           |\n\n      | Linear proj (200)   | 0.692      | +0.032       | p<0.001           |\n\n      | Few-shot 25         | 0.678      | +0.018       | p=0.006           |\n\n      | Few-shot 100        | 0.712      | +0.052       | p<0.001           |\n\n      '\n  figures_description:\n  - 'Pareto scatter plot: 20 个子图（每语言一个），x=EN AUROC, y=ZS AUROC， 每点为一个 probed layer（24\n    点），颜色编码深度（浅=浅层，深=深层）， Pareto frontier 用虚线连接。HIGH 语言子图显示清晰的右下弯折（深层 EN 高但 ZS 低），\n    LOW 语言子图点密集在左下区域，frontier 不明显。\n\n    '\n  - 'Layer-wise AUROC heatmap: x=20 languages（按 tier 排列），y=24 probed layers（按深度），\n    颜色=ZS AUROC。右上角（深层+低资源）呈冷色（低 AUROC），左中区域（中层+高资源）呈暖色。 EN 列单独标注显示 AUROC 随深度单调增加。\n\n    '\n  analysis: 'Qwen3-235B 的 MoE 架构产生了比 7B pilot 更清晰的 Pareto frontier：16/20 语言的 depth-transfer\n    rho 为负值，其中 15 个在 p<0.10 显著。Pareto 强度与资源 tier 强相关 （HIGH rho median=-0.49, MID=-0.43,\n    LOW=-0.27），因为低资源语言整体 AUROC 低、 depth variation 也小。MoE 路由机制加速了深层表征的语言特异化——L64-L80\n    的 expert 激活 模式在不同语言间差异显著增大，解释了 transfer cliff 为何比 dense 7B 更陡。 EN-optimal（L80）vs\n    transfer-optimal（L68）的 gap 为实际部署提供了明确的 layer selection guidance。\n\n    '\n- name: Full Pareto Frontier — Llama 4 Scout (MoE, W4A16)\n  plan_id: plan_002\n  description: '48 层 17B-16E MoE，每 4 层取一层（12 probed layers），20 语言，5 transfer 条件。 Llama\n    架构族在 pilot 中显示弱 Pareto，full-scale 预期延续此模式但 MoE 可能略增 Pareto 强度。\n\n    '\n  expected_results:\n    en_best_auroc: 0.76\n    en_best_layer: 44\n    en_best_layer_depth_pct: 0.917\n    en_auroc_range:\n    - 0.6\n    - 0.76\n    en_best_ece_raw: 0.195\n    transfer_optimal_layer_mean: 36\n    transfer_optimal_depth_pct: 0.75\n    en_transfer_layer_gap_pp: 1.5\n    zs_pass_rate: 0.7\n    zs_pass_count: 14\n    zs_mean_auroc_en_optimal: 0.643\n    zs_mean_auroc_transfer_optimal: 0.655\n    pareto_significant_langs: 11\n    pareto_spearman_rho_median: -0.28\n    pareto_spearman_rho_range:\n    - -0.55\n    - 0.35\n    pareto_langs_negative_rho: 13\n    best_zs_auroc_by_tier:\n      HIGH_mean: 0.705\n      MID_mean: 0.652\n      LOW_mean: 0.558\n    linear_proj_200_mean_auroc: 0.673\n    few_shot_25_mean_auroc: 0.662\n    few_shot_100_mean_auroc: 0.693\n    mean_shift_delta_auroc: 0.0\n  result_rationale: 'Llama 4 Scout 延续 Llama-3.1-8B pilot 的弱 Pareto 模式：pilot 中仅 2/5\n    语言显示 depth-transfer tradeoff（ar/ko 随深度改善），full-scale 中约 7/20 语言不显示 tradeoff 或方向相反。EN\n    AUROC 从 pilot 的 0.728 提升至 0.76（Llama 4 Scout 更大），但提升幅度 小于 Qwen3 的 scaling，因为 Llama\n    4 的 16-expert MoE 在浅层就开始 expert specialization， correctness signal 在中层已经 plateau。Pareto\n    弱于 Qwen3 的根本原因：Llama CKA decline 更渐进（slope -0.015/layer vs Qwen 的 -0.025/layer），导致\n    transfer 不出现急剧 cliff， tradeoff 分散在更宽的层范围内。EN-optimal（L44）vs transfer-optimal（L36）gap\n    仅 ~1.5pp， 相比 Qwen3 的 ~2.8pp 更小。一些语言（ar, ko, vi）在全深度范围 AUROC 单调增加， 无 tradeoff——pilot\n    中 ar/ko 的异常模式在 full-scale 中得到确认和扩展。\n\n    '\n  tables:\n  - name: Per-Language Pareto Strength Comparison (Qwen3 vs Llama 4)\n    data: '| Tier | Language | Qwen3 rho | Qwen3 p | Llama4 rho | Llama4 p | Pattern       |\n\n      |------|----------|-----------|---------|------------|----------|---------------|\n\n      | HIGH | zh       | -0.52     | 0.009   | -0.40      | 0.198    | Both negative\n      |\n\n      | HIGH | es       | -0.48     | 0.017   | -0.35      | 0.265    | Both negative\n      |\n\n      | HIGH | ja       | -0.58     | 0.003   | -0.48      | 0.115    | Both negative\n      |\n\n      | MID  | ar       | -0.50     | 0.013   | +0.15      | 0.641    | DIVERGENT     |\n\n      | MID  | ko       | -0.47     | 0.021   | +0.22      | 0.489    | DIVERGENT     |\n\n      | MID  | hi       | -0.38     | 0.068   | -0.55      | 0.065    | Both negative\n      |\n\n      | LOW  | sw       | -0.30     | 0.153   | -0.25      | 0.432    | Weak both     |\n\n      | LOW  | yo       | -0.18     | 0.398   | +0.10      | 0.758    | Neither sig   |\n\n      '\n  - name: Architecture Comparison Summary\n    data: '| Metric                        | Qwen3-235B | Llama 4 Scout |\n\n      |-------------------------------|------------|---------------|\n\n      | EN best AUROC                 | 0.78       | 0.76          |\n\n      | Mean ZS AUROC (EN-opt layer)  | 0.660      | 0.643         |\n\n      | Pareto significant langs (/20)| 15         | 11            |\n\n      | Median per-lang Pareto rho    | -0.42      | -0.28         |\n\n      | CKA cliff onset (% depth)    | ~68%       | ~55%          |\n\n      | CKA slope (cliff region)      | -0.025/L   | -0.015/L      |\n\n      '\n  figures_description:\n  - '双模型 Pareto 对比图：左右两列分别为 Qwen3-235B 和 Llama 4 Scout，每行一个 resource tier （HIGH/MID/LOW），每子图叠加该\n    tier 所有语言的 Pareto frontier（不同颜色）。 Qwen3 列显示 frontier 弯折更尖锐，Llama 4 列更平缓。\n\n    '\n  analysis: '两个 MoE 架构的 Pareto 差异确认了 pilot 的架构依赖性发现。关键差异不在 MoE vs dense， 而在 CKA depth\n    gradient 的斜率：Qwen3 的急剧 CKA cliff 创建清晰 tradeoff， Llama 4 的渐进下降使 tradeoff 分散。ar/ko\n    在 Llama 4 上随深度改善的异常模式扩展到 full-scale——这些语言在 Llama tokenizer 中有较好的 subword coverage，深层\n    expert specialization 反而增强了 correctness signal。此架构依赖性是 observational（n=2 架构， 混杂\n    scale/layer count/training data），不做因果归因。\n\n    '\n- name: CaCLR Implementation and Negative Result\n  plan_id: plan_003\n  description: 'CaCLR (BCE + α·SB-ECE + β·MMD) 完整实现与评估。β sweep 横跨 3 OOM (0.001-1.0)。\n    Median tier 预期：consistency loss 无效，转为 negative result + geometric explanation。\n\n    '\n  expected_results:\n    caclr_mean_delta_auroc_vs_zs: 0.002\n    caclr_best_beta: 0.01\n    caclr_best_alpha: 0.3\n    beta_sweep:\n      beta_0.001:\n        mean_delta_auroc: 0.001\n        p_vs_zs: 0.71\n      beta_0.01:\n        mean_delta_auroc: 0.003\n        p_vs_zs: 0.42\n      beta_0.1:\n        mean_delta_auroc: -0.002\n        p_vs_zs: 0.58\n      beta_1.0:\n        mean_delta_auroc: -0.008\n        p_vs_zs: 0.12\n    alpha_sweep:\n      alpha_0.01:\n        mean_delta_ece: -0.2\n        mean_delta_auroc: 0.0\n      alpha_0.1:\n        mean_delta_ece: -0.5\n        mean_delta_auroc: -0.001\n      alpha_1.0:\n        mean_delta_ece: -1.5\n        mean_delta_auroc: -0.004\n      alpha_10.0:\n        mean_delta_ece: -2.1\n        mean_delta_auroc: -0.012\n    component_ablation:\n      bce_only:\n        auroc: 0.66\n        ece: 0.192\n      bce_sbece:\n        auroc: 0.658\n        ece: 0.178\n      bce_mmd:\n        auroc: 0.662\n        ece: 0.19\n      bce_sbece_mmd:\n        auroc: 0.661\n        ece: 0.176\n    method_comparison_mean_20lang:\n      zero_shot: 0.66\n      mean_shift: 0.66\n      caclr_best: 0.662\n      linear_proj_50: 0.678\n      linear_proj_200: 0.692\n      few_shot_25: 0.678\n      few_shot_100: 0.712\n    caclr_per_tier_delta:\n      HIGH: 0.001\n      MID: 0.003\n      LOW: 0.002\n    implementation_spec:\n      mmd_kernel: Gaussian RBF, median heuristic bandwidth\n      optimizer: Adam, lr=1e-3, cosine schedule\n      epochs: 50\n      early_stopping: patience=10 on val BCE loss\n      initialization: from standard LR solution\n      batch_size: 256\n      mmd_items: same as BCE (probe_train split)\n      parallel_set_size_range:\n      - 8200\n      - 12800\n  result_rationale: 'CaCLR 的 MMD consistency loss 在 1-D probe logit 空间操作——这是设计层面的根本局限。\n    Correctness direction 是高维 activation 空间中的低维子空间特征（~1-3 维），MMD 匹配 probe logit 的边际分布（均值和方差）但无法对齐子空间内的方向结构。具体地：两种语言的\n    probe logit 分布可能有相似的均值和方差（MMD 小），但 correctness direction 在 activation 空间中的朝向不同——MMD\n    无法检测或纠正这种旋转。β=0.001-0.01 时 consistency loss 太弱， 无实质效果；β=0.1-1.0 时 consistency\n    loss 开始干扰 BCE 训练（AUROC 下降），因为 强制匹配边际分布反而破坏了 EN probe 已经学到的 correctness direction。这不是\n    hyperparameter 问题——是根本的 architectural mismatch。α (SB-ECE) 对 ECE 有轻微改善 是预期的（ECE\n    loss 直接优化 calibration），但与 cross-lingual transfer 无关。 Linear projection 成功因为它直接学习子空间旋转矩阵（Procrustes\n    alignment）， 绕过了 distributional matching 的局限。这一对比（MMD 失败 vs linear projection 成功）\n    提供了对 Zhao et al. (2019) conditional-marginal mismatch theory 的实证验证。\n\n    '\n  tables:\n  - name: β Sweep Results (Qwen3-235B, L80, mean across 20 languages)\n    data: '| β     | Mean AUROC | ΔAUROC vs ZS | 95% Bootstrap CI    | Cohen''s d\n      | Interpretation     |\n\n      |-------|------------|--------------|---------------------|-----------|--------------------|\n\n      | 0     | 0.660      | —            | —                   | —         | ZS baseline        |\n\n      | 0.001 | 0.661      | +0.001       | [-0.004, +0.006]    | 0.03      | Negligible         |\n\n      | 0.01  | 0.663      | +0.003       | [-0.003, +0.009]    | 0.07      | Negligible         |\n\n      | 0.1   | 0.658      | -0.002       | [-0.008, +0.004]    | 0.05      | Negligible         |\n\n      | 1.0   | 0.652      | -0.008       | [-0.015, -0.001]    | 0.19      | Slight\n      degradation |\n\n      '\n  - name: CaCLR vs All Methods (mean 20 languages, both models)\n    data: '| Method            | Qwen3 AUROC | Llama4 AUROC | Mean  | Req. labels\n      | Req. parallel |\n\n      |-------------------|-------------|--------------|-------|-------------|---------------|\n\n      | Zero-shot         | 0.660       | 0.643        | 0.652 | 0           | 0             |\n\n      | Mean-shift        | 0.660       | 0.643        | 0.652 | 0           | N (mean\n      only) |\n\n      | CaCLR (best)      | 0.662       | 0.645        | 0.654 | 0           | ~10K\n      parallel |\n\n      | Linear proj (50)  | 0.678       | 0.660        | 0.669 | 0           | 50\n      pairs      |\n\n      | Linear proj (200) | 0.692       | 0.673        | 0.683 | 0           | 200\n      pairs     |\n\n      | Few-shot 25       | 0.678       | 0.662        | 0.670 | 25          | 0             |\n\n      | Few-shot 100      | 0.712       | 0.693        | 0.703 | 100         | 0             |\n\n      '\n  - name: CKA Subspace Analysis — Why MMD Fails\n    data: '| Language Tier | Mean subspace angle (EN-target) | MMD after CaCLR | Angle\n      after CaCLR | Interpretation            |\n\n      |--------------|----------------------------------|-----------------|--------------------|-----------------------------|\n\n      | HIGH         | 12°                              | 0.02 → 0.01     | 12° →\n      11°         | MMD reduces, angle unchanged |\n\n      | MID          | 24°                              | 0.05 → 0.02     | 24° →\n      23°         | MMD reduces, angle unchanged |\n\n      | LOW          | 42°                              | 0.12 → 0.05     | 42° →\n      40°         | MMD reduces, angle unchanged |\n\n      '\n  figures_description:\n  - 'β sweep 图：x=β (log scale)，y=ΔAUROC vs zero-shot，每条线为一个 resource tier， shaded\n    area 为 bootstrap 95% CI。所有线段在 y=0 附近震荡，β=1.0 时向下偏离。 水平虚线标注 linear projection 和\n    few-shot 的 ΔAUROC 作为对比。\n\n    '\n  - '几何解释概念图：左侧显示 MMD 操作空间（1-D logit 分布），EN 和 target 分布重叠 但 correctness direction\n    指向不同方向（3D activation 空间投影）；右侧显示 linear projection 直接旋转子空间使 direction 对齐。\n\n    '\n  analysis: 'CaCLR negative result 的核心贡献不是 method 本身，而是 (1) systematic β sweep 关闭\n    MMD distributional-matching 路径（3 OOM, component ablation, 两个架构 × 20 语言）， (2) CKA\n    subspace analysis 提供几何解释——MMD 成功减小了 marginal distance 但完全 无法对齐 correctness subspace\n    的方向（subspace angle 几乎不变）。这验证了 Zhao et al. (2019) 的理论预测：当 conditional distributions\n    P(Y|X) 在域间不同时， marginal matching 必然失败。在 correctness probing 中，P(correct|activation)\n    的 条件结构在不同语言间确实不同（语言特异的 capability 成分），因此 MMD 注定无效。 Constructive path: linear projection\n    以 50-80 parallel pairs 的极低成本解决了 subspace alignment 问题，是明确的 practical recommendation。\n\n    '\n- name: Difficulty-Controlled Decomposition Ablation\n  plan_id: plan_004\n  description: 'IRT difficulty probes → project out difficulty direction → retrain\n    correctness probes → evaluate transfer。 10 代表语言 × 8 代表层 × 两个模型。含 random-direction\n    control。 Median tier: 定性分离成立但 prescriptive 预测能力不可靠。\n\n    '\n  expected_results:\n    mean_delta_auroc_difficulty_projected: 0.012\n    delta_auroc_range:\n    - -0.008\n    - 0.025\n    langs_with_positive_delta: 7\n    langs_with_negative_delta: 3\n    random_direction_mean_delta: 0.005\n    difficulty_vs_random_ratio: 2.4\n    difficulty_probe_r2: 0.35\n    per_lang_results:\n      zh:\n        delta: 0.008\n        sig: false\n      es:\n        delta: 0.01\n        sig: false\n      fr:\n        delta: 0.012\n        sig: true\n      de:\n        delta: 0.015\n        sig: true\n      hi:\n        delta: 0.022\n        sig: true\n      ru:\n        delta: 0.018\n        sig: true\n      ko:\n        delta: -0.005\n        sig: false\n      tr:\n        delta: 0.02\n        sig: true\n      sw:\n        delta: -0.008\n        sig: false\n      bn:\n        delta: 0.025\n        sig: true\n    prescriptive_accuracy: 0.58\n  result_rationale: 'Difficulty decomposition 的定性逻辑成立：difficulty 成分确实是跨语言共享的（IRT difficulty\n    与语言无关），project out 后 residual 应该更 capability-specific。但 prescriptive 力弱 的原因有三：(1)\n    IRT difficulty probe 的 R²=0.35 意味着 difficulty direction 只解释了 35% 的方差，projection\n    不完全；(2) difficulty 和 capability 在 activation 空间中不正交—— projection 同时移除了部分 capability\n    信息（ko/sw 中 AUROC 下降）；(3) 不同语言中 difficulty-capability 纠缠程度不同——高资源语言 capability\n    独立于 difficulty（projection 帮助），低资源语言两者纠缠更深（projection 效果不确定）。Random-direction control\n    显示 ~40% 的效果来自纯维度缩减（从高维投影到低维本身就降噪），只有 ~60% 是 difficulty-specific。这足以支持 \"descriptive\n    separation observed\" 但不足以支持 \"prescriptive decomposition predicts optimal strategy\"。Prescriptive\n    accuracy 仅 58% （随机猜 50%），几乎无实际预测价值。\n\n    '\n  tables:\n  - name: Decomposition Results by Language (Qwen3-235B, 8-layer mean)\n    data: '| Language | Tier | Full AUROC | Diff-projected AUROC | ΔAUROC  | Random-proj\n      AUROC | Rand ΔAUROC |\n\n      |----------|------|------------|----------------------|---------|-------------------|-------------|\n\n      | zh       | HIGH | 0.725      | 0.733                | +0.008  | 0.729             |\n      +0.004      |\n\n      | es       | HIGH | 0.735      | 0.745                | +0.010  | 0.740             |\n      +0.005      |\n\n      | fr       | HIGH | 0.732      | 0.744                | +0.012  | 0.737             |\n      +0.005      |\n\n      | de       | HIGH | 0.715      | 0.730                | +0.015  | 0.721             |\n      +0.006      |\n\n      | hi       | MID  | 0.658      | 0.680                | +0.022  | 0.665             |\n      +0.007      |\n\n      | ru       | MID  | 0.695      | 0.713                | +0.018  | 0.702             |\n      +0.007      |\n\n      | ko       | MID  | 0.680      | 0.675                | -0.005  | 0.683             |\n      +0.003      |\n\n      | tr       | MID  | 0.650      | 0.670                | +0.020  | 0.656             |\n      +0.006      |\n\n      | sw       | LOW  | 0.585      | 0.577                | -0.008  | 0.588             |\n      +0.003      |\n\n      | bn       | LOW  | 0.602      | 0.627                | +0.025  | 0.608             |\n      +0.006      |\n\n      '\n  figures_description:\n  - '分解可视化：x=capability ΔAUROC (difficulty-projected - full)，y=difficulty  component\n    strength (IRT probe R²)，每点为一个语言。右上象限（高 difficulty 解释力 +  positive ΔAUROC）包含 hi/bn/tr（projection\n    帮助且 difficulty 信号强），左下象限包含 ko/sw（projection 损害或无效）。椭圆标注资源 tier。\n\n    '\n  analysis: 'Decomposition 分析支持 \"correctness transfer 确实包含 difficulty-shared 和 capability-specific\n    两个成分\" 的定性结论，但 prescriptive accuracy (58%) 与随机猜测差距过小（chance=50%）， 无法作为实际策略选择工具。弱化\n    Claim 2 为 \"descriptive separation observed in most language-architecture combinations;\n    however, the decomposition does not reliably predict optimal alignment strategy.\"\n    纸面贡献仍在：这是首次在跨语言 probing 中尝试 difficulty- capability 分解，定性结果与 Civelli et al. 的 difficulty\n    transfer 文献一致。 ko/sw 的反常模式（projection 损害 AUROC）值得单独分析——可能是因为这些语言的 difficulty ordering\n    与英语差异较大（文化特异的知识题目分布不同）。\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: '提取 verbalized confidence direction，计算与 correctness direction 的 cosine\n    similarity， 20 语言 × 2 架构。作为 Claim 4 的 supporting evidence（subsection）。\n\n    '\n  expected_results:\n    mean_cosine_all: 0.038\n    cosine_range:\n    - 0.008\n    - 0.142\n    langs_below_0.05: 14\n    langs_below_0.10: 18\n    langs_above_0.10: 2\n    per_tier_mean_cosine:\n      HIGH: 0.028\n      MID: 0.042\n      LOW: 0.072\n    architecture_comparison:\n      qwen3_mean: 0.035\n      llama4_mean: 0.041\n    outlier_langs:\n    - am\n    - yo\n    outlier_cosine:\n    - 0.142\n    - 0.118\n  result_rationale: 'Miao & Ungar (2026) 在 English 7-8B 模型上发现 cosine < 0.04。跨语言扩展时，\n    HIGH 资源语言复现此结果（模型在这些语言上有足够训练数据，correctness 和 confidence direction 分化清晰）。MID 语言\n    cosine 略高（0.04-0.06）因为 confidence direction 在 中资源语言上更嘈杂（模型对这些语言的 verbalized confidence\n    不够稳定）。LOW 语言中 am/yo 出现较高 cosine（>0.10）——这不是真正的 correctness-confidence alignment，\n    而是 probe capacity artifact：在低资源语言上两个 direction 都很弱，cosine 被噪声主导。 plan_013 control\n    task 将确认这些语言的 selectivity 低于阈值。整体结论不变： orthogonality 是跨语言稳健的结构性质，output-based\n    calibration 的局限性与语言无关。 两个架构差异微小（0.035 vs 0.041），不具有统计显著性。\n\n    '\n  tables:\n  - name: Cosine Similarity by Resource Tier\n    data: '| Tier | n  | Mean cosine | Std  | Min   | Max   | < 0.05 | < 0.10 |\n\n      |------|----|-------------|------|-------|-------|--------|--------|\n\n      | HIGH | 6  | 0.028       | 0.012| 0.012 | 0.045 | 5      | 6      |\n\n      | MID  | 8  | 0.042       | 0.018| 0.018 | 0.075 | 5      | 8      |\n\n      | LOW  | 6  | 0.072       | 0.042| 0.025 | 0.142 | 2      | 4      |\n\n      '\n  figures_description:\n  - 'Bar chart: 20 语言按 cosine 升序排列，颜色编码 resource tier。 水平虚线标注 Miao & Ungar 的 0.04\n    阈值和 0.10 artifact 阈值。 大多数 bar 在 0.04 以下，仅 am/yo 突出。\n\n    '\n  analysis: 'Orthogonality 作为 subsection supporting evidence 充分：18/20 语言 cosine <\n    0.10， 14/20 < 0.05。结论简洁：\"output-based calibration 的结构性局限（correctness-confidence\n    orthogonality）跨语言稳健，强化了 probe-based 方法的必要性。\" am/yo 的高 cosine 值须与 plan_013 control\n    task 结果交叉验证，确认是 probe artifact 而非真实 alignment。\n\n    '\n- name: Probe Complexity Comparison (LR vs 2-layer MLP)\n  plan_id: plan_006\n  description: '每层每模型对比 logistic regression 和 2-layer MLP 的 EN accuracy、cross-lingual\n    transfer degradation 和 calibration quality。CPU-bound，使用缓存 activations。\n\n    '\n  expected_results:\n    lr_en_best_auroc_qwen3: 0.78\n    mlp_en_best_auroc_qwen3: 0.802\n    lr_mean_zs_auroc_qwen3: 0.66\n    mlp_mean_zs_auroc_qwen3: 0.632\n    lr_transfer_gap_qwen3: 0.12\n    mlp_transfer_gap_qwen3: 0.17\n    lr_en_best_auroc_llama4: 0.76\n    mlp_en_best_auroc_llama4: 0.778\n    lr_mean_zs_auroc_llama4: 0.643\n    mlp_mean_zs_auroc_llama4: 0.618\n    mlp_en_advantage_pp: 2.0\n    lr_transfer_advantage_pp: 2.8\n    lr_preferred_for_transfer: true\n  result_rationale: 'MLP（2 层, ~256 hidden units）有更多参数来拟合 EN correctness signal，EN\n    AUROC 提升 ~2pp。但额外容量同时学到了 EN-specific 的 activation pattern（如 English 特有的 token\n    position bias, subject-verb agreement cues），这些 pattern 不跨语言迁移。 LR 被迫学习更简洁的 direction（1\n    个超平面），这个 direction 更可能对应语言无关的 correctness subspace。Transfer gap（EN - mean ZS）:\n    LR 12pp vs MLP 17pp——MLP 多出的 5pp gap 恰好对应其 EN advantage 的 2pp + 额外 3pp 的 EN-specific\n    overfitting。 这为 paper 的方法论选择（使用 LR probe）提供了实证支持。\n\n    '\n  tables:\n  - name: LR vs MLP Transfer Comparison (mean across 20 languages)\n    data: '| Metric                    | Qwen3 LR | Qwen3 MLP | Llama4 LR | Llama4\n      MLP |\n\n      |---------------------------|----------|-----------|-----------|------------|\n\n      | EN best AUROC             | 0.780    | 0.802     | 0.760     | 0.778      |\n\n      | Mean ZS AUROC             | 0.660    | 0.632     | 0.643     | 0.618      |\n\n      | Transfer gap (EN - ZS)    | 0.120    | 0.170     | 0.117     | 0.160      |\n\n      | EN ECE                    | 0.185    | 0.172     | 0.195     | 0.182      |\n\n      | Mean ZS ECE               | 0.225    | 0.252     | 0.232     | 0.260      |\n\n      | ZS pass rate (>0.60)      | 75%      | 60%       | 70%       | 55%        |\n\n      '\n  figures_description:\n  - 'Paired scatter plot: x=LR ZS AUROC, y=MLP ZS AUROC, 每点一个语言， 对角线 y=x 标注。大多数点在对角线下方（MLP\n    worse），尤其是低资源语言。\n\n    '\n  analysis: 'LR vs MLP 对比验证了 linear probe 是 cross-lingual transfer 的正确选择。 MLP 的额外容量在\n    EN 上有用但在迁移中有害——这与 Hewitt & Liang (2019) 关于 probe complexity 的讨论一致。Paper 方法论选择（LR）有实证支持。\n\n    '\n- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: '在 Belebele（阅读理解）和 MMLU-ProX（翻译 MMLU）上评估 best probes + 所有 transfer\n    方法，验证 generalization beyond GlobalMMLU。20 语言 × 2 模型。\n\n    '\n  expected_results:\n    belebele:\n      en_best_auroc: 0.74\n      mean_zs_auroc: 0.625\n      zs_pass_rate: 0.6\n      pareto_preserved: true\n      pareto_strength: weaker than GlobalMMLU\n      rank_correlation_with_globalmmlu: 0.82\n    mmlu_prox:\n      en_best_auroc: 0.77\n      mean_zs_auroc: 0.648\n      zs_pass_rate: 0.7\n      pareto_preserved: true\n      pareto_strength: comparable to GlobalMMLU\n      rank_correlation_with_globalmmlu: 0.91\n    linear_proj_generalizes: true\n    caclr_still_inert: true\n    cross_benchmark_lang_ranking_rho: 0.88\n  result_rationale: 'Belebele 是阅读理解任务，与 GlobalMMLU 的知识型 MCQA 不同——correctness signal\n    的性质不完全相同（RC 依赖 passage comprehension, MCQA 依赖 parametric knowledge）， 所以 EN AUROC\n    略低（0.74 vs 0.78）且 transfer 更差。但 Pareto 结构保留，因为 depth-transferability tradeoff\n    是 representation geometry 的性质，不依赖特定任务。 MMLU-ProX 与 GlobalMMLU 高度相关（同源翻译数据），所以模式几乎一致。\n    Language ranking 在 benchmarks 间高度相关（rho=0.88）——确认结果不是 benchmark-specific。 CaCLR\n    在两个 benchmark 上仍无效，linear projection 仍有效——泛化性确认。\n\n    '\n  tables:\n  - name: Cross-Benchmark Comparison (mean across 20 languages, Qwen3-235B)\n    data: '| Metric             | GlobalMMLU | Belebele | MMLU-ProX |\n\n      |--------------------|------------|----------|-----------|\n\n      | EN best AUROC      | 0.78       | 0.74     | 0.77      |\n\n      | Mean ZS AUROC      | 0.660      | 0.625    | 0.648     |\n\n      | ZS pass rate       | 75%        | 60%      | 70%       |\n\n      | Pareto langs (/20) | 15         | 12       | 14        |\n\n      | Linear proj Δ      | +0.032     | +0.028   | +0.030    |\n\n      | CaCLR Δ            | +0.002     | +0.001   | +0.002    |\n\n      '\n  figures_description:\n  - '三 benchmark 平行坐标图：每条线为一个语言，x 轴为三个 benchmark， y 轴为 ZS AUROC。线条颜色编码 resource tier。大多数线大致平行（ranking\n    一致）， 但 Belebele 整体偏低。交叉的线表示 benchmark-specific 的语言排名变化。\n\n    '\n  analysis: 'Cross-benchmark 泛化确认了主要发现的稳健性。Belebele 上 Pareto 更弱是预期的 （RC task 的 correctness\n    signal 与 knowledge MCQA 不同），但关键模式（架构差异、 resource tier 梯度、CaCLR 无效、linear projection\n    有效）在所有 benchmark 上一致。 这为 paper 的 claim 提供了必要的泛化验证。\n\n    '\n- name: Quantization Validation Ablation\n  plan_id: plan_010\n  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4\n    vs FP16 for Qwen3-235B at 5 layers, 5% subset. 验证量化不扭曲 correctness signal。\n\n    '\n  expected_results:\n    llama4_w4a16_vs_fp16:\n      mean_abs_delta_auroc: 0.005\n      max_abs_delta_auroc: 0.009\n      direction: mixed (2 positive, 3 negative)\n      cka_fp16_vs_quant: 0.985\n    qwen3_int4_vs_fp16:\n      mean_abs_delta_auroc: 0.006\n      max_abs_delta_auroc: 0.011\n      direction: mixed (3 positive, 2 negative)\n      cka_fp16_vs_quant: 0.978\n    quantization_safe: true\n  result_rationale: '4-bit weight quantization 保留了 activation 空间的大部分结构——correctness\n    signal 是高维 activation 空间中的低维子空间特征，quantization noise 主要分布在与 correctness direction\n    正交的维度上（根据 random projection 理论，低维结构 在高维 noise 下稳健）。ΔAUROC < 0.01 在 bootstrap CI\n    内，不影响任何结论。 Qwen3 的 MoE 量化略有更大 delta（expert routing 决策在 INT4 下可能微变）， 但仍在可接受范围。CKA(FP16,\n    quant) > 0.97 确认 activation 空间整体结构保留。\n\n    '\n  tables:\n  - name: Quantization Validation (per-layer ΔAUROC)\n    data: '| Model      | Layer (% depth) | FP16 AUROC | Quant AUROC | ΔAUROC  |\n\n      |------------|-----------------|------------|-------------|---------|\n\n      | Llama4     | L8 (17%)        | 0.632      | 0.629       | -0.003  |\n\n      | Llama4     | L16 (33%)       | 0.685      | 0.688       | +0.003  |\n\n      | Llama4     | L24 (50%)       | 0.720      | 0.715       | -0.005  |\n\n      | Llama4     | L36 (75%)       | 0.748      | 0.741       | -0.007  |\n\n      | Llama4     | L44 (92%)       | 0.760      | 0.762       | +0.002  |\n\n      | Qwen3      | L16 (17%)       | 0.628      | 0.622       | -0.006  |\n\n      | Qwen3      | L36 (38%)       | 0.702      | 0.705       | +0.003  |\n\n      | Qwen3      | L52 (55%)       | 0.738      | 0.734       | -0.004  |\n\n      | Qwen3      | L68 (72%)       | 0.768      | 0.772       | +0.004  |\n\n      | Qwen3      | L80 (85%)       | 0.780      | 0.769       | -0.011  |\n\n      '\n  figures_description:\n  - 'Bland-Altman plot: x=(FP16+Quant)/2, y=FP16-Quant, 每点为一层。 水平虚线标注 ±0.01 tolerance\n    band。所有点在 band 内。\n\n    '\n  analysis: 'Quantization validation 通过——所有 ΔAUROC < 0.012，CKA > 0.97。 Qwen3 L80 的\n    ΔAUROC=-0.011 是最大偏差，但仍在 bootstrap CI 范围内 且不影响 EN-optimal layer 的选择。Paper 中报告为\n    \"quantization artifacts are negligible for correctness probing (max |ΔAUROC| <\n    0.012 across all validated layers)\"。\n\n    '\n- name: Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis\n  plan_id: plan_011\n  description: 'Linear CKA between EN and 20 target languages at every probed layer,\n    both models. 核心分析：partial correlation controlling for depth（Simpson''s Paradox\n    验证）。 Median tier: 仅 Llama 4 Scout 上显著，Qwen3 上 trending but not significant。\n\n    '\n  expected_results:\n    qwen3:\n      raw_spearman_cka_auroc: -0.22\n      raw_p: 0.001\n      partial_spearman_ctrl_depth: 0.16\n      partial_p: 0.072\n      significant: false\n      per_layer_positive_rho_count: 17\n      per_layer_total: 24\n      per_layer_significant_count: 5\n      cka_cliff_onset_layer: 64\n      cka_cliff_onset_depth_pct: 0.68\n      cka_final_layer_mean: 0.1\n      cka_peak_layer: 36\n      cka_peak_mean: 0.81\n    llama4:\n      raw_spearman_cka_auroc: -0.28\n      raw_p: 0.001\n      partial_spearman_ctrl_depth: 0.29\n      partial_p: 0.018\n      significant: true\n      per_layer_positive_rho_count: 10\n      per_layer_total: 12\n      per_layer_significant_count: 4\n      cka_cliff_onset_layer: 24\n      cka_cliff_onset_depth_pct: 0.5\n      cka_final_layer_mean: 0.22\n      cka_peak_layer: 12\n      cka_peak_mean: 0.82\n    simpson_paradox_confirmed: partial (1/2 architectures)\n    subspace_angle_analysis:\n      qwen3_mean_angle_HIGH: 10\n      qwen3_mean_angle_MID: 22\n      qwen3_mean_angle_LOW: 45\n      llama4_mean_angle_HIGH: 12\n      llama4_mean_angle_MID: 25\n      llama4_mean_angle_LOW: 40\n    cka_transfer_collapse_threshold: 0.32\n    bootstrap_ci_partial_rho_qwen3:\n    - -0.02\n    - 0.34\n    bootstrap_ci_partial_rho_llama4:\n    - 0.06\n    - 0.5\n  result_rationale: 'Simpson''s Paradox 的架构依赖性源于 CKA-depth gradient 的形状差异。 Llama 4\n    Scout 的 CKA depth gradient 更陡峭（从 peak 0.82 at L12 到 final 0.22 at L48, slope ~\n    -0.017/layer），这使得 depth confound 更强——controlling for depth 释放了更多 CKA 的独立解释力（partial\n    rho=0.29, p=0.018）。Qwen3 的 CKA decline 起始更晚 （L64 才开始急降）且更集中在最深层，depth confound\n    的影响不均匀——前 60% 层几乎 无 CKA 变化，后 30% 急降——这种非线性使得 linear partial correlation 效果较差 （partial\n    rho=0.16, p=0.072）。这不意味 CKA 在 Qwen3 上无解释力，而是 linear depth control 不够——可能需要 non-linear\n    depth control（如 depth²）才能捕捉 Qwen3 的 step-function-like CKA profile。但 paper 应诚实报告：standard\n    partial correlation 仅在 Llama 上显著。Per-layer analysis: 两个模型 70-83% 的 per-layer rho\n    为正（Qwen 17/24, Llama 10/12），但因每层仅 n=20 语言，个别层的 significance 有限。Full-scale 的 n=20\n    per layer 比 pilot 的 n=5 有更多 power，但仍不足以让所有 per-layer rho 显著。 Subspace angle 分析提供定量补充：HIGH\n    语言角度小（10-12°）→ 零样本迁移好， LOW 语言角度大（40-45°）→ 需要 alignment。CKA collapse threshold\n    ~0.32 是 transfer 从 \"reasonable\" 骤降到 \"chance-level\" 的拐点。\n\n    '\n  tables:\n  - name: Simpson's Paradox — Raw vs Partial Correlation\n    data: '| Model       | n   | Raw rho | Raw p   | Partial rho | Partial p | Boot\n      95% CI      | Sig?   |\n\n      |-------------|-----|---------|---------|-------------|-----------|------------------|--------|\n\n      | Qwen3-235B  | 480 | -0.22   | <0.001  | +0.16       | 0.072     | [-0.02,\n      +0.34]   | No     |\n\n      | Llama4 Scout| 240 | -0.28   | <0.001  | +0.29       | 0.018     | [+0.06,\n      +0.50]   | Yes    |\n\n      | Pilot Llama | 45  | -0.16   | 0.294   | +0.41       | 0.006     | [+0.12,\n      +0.65]   | Yes    |\n\n      | Pilot Qwen  | 40  | -0.16   | 0.310   | +0.18       | 0.274     | [-0.15,\n      +0.48]   | No     |\n\n      '\n  - name: Per-Layer Cross-Language Spearman (CKA vs AUROC, n=20 per layer)\n    data: '| Layer group        | Qwen3 median rho | Qwen3 sig layers | Llama4 median\n      rho | Llama4 sig layers |\n\n      |--------------------|------------------|------------------|-------------------|-------------------|\n\n      | 0-25% depth        | +0.15            | 0/6              | +0.22             |\n      1/3               |\n\n      | 25-50% depth       | +0.38            | 2/6              | +0.45             |\n      2/3               |\n\n      | 50-75% depth       | +0.42            | 2/6              | +0.52             |\n      2/3               |\n\n      | 75-100% depth      | +0.28            | 1/6              | +0.35             |\n      1/3               |\n\n      '\n  - name: CKA Depth Profile (mean across 20 languages)\n    data: '| Depth % | Qwen3 Layer | Qwen3 CKA | Llama4 Layer | Llama4 CKA |\n\n      |---------|-------------|-----------|--------------|------------|\n\n      | 0%      | 0           | 0.72      | 0            | 0.60       |\n\n      | 17%     | 16          | 0.75      | 8            | 0.80       |\n\n      | 34%     | 32          | 0.80      | 16           | 0.76       |\n\n      | 51%     | 48          | 0.78      | 24           | 0.58       |\n\n      | 68%     | 64          | 0.62      | 32           | 0.42       |\n\n      | 77%     | 72          | 0.40      | 36           | 0.35       |\n\n      | 85%     | 80          | 0.25      | 40           | 0.30       |\n\n      | 94%     | 88          | 0.14      | 44           | 0.25       |\n\n      | 100%    | 92          | 0.10      | 48           | 0.22       |\n\n      '\n  - name: Subspace Angle Analysis (correctness direction EN vs target)\n    data: '| Tier | Qwen3 mean angle | Llama4 mean angle | Mean ZS AUROC | Interpretation         |\n\n      |------|------------------|-------------------|---------------|------------------------|\n\n      | HIGH | 10°              | 12°               | 0.715         | Near-aligned           |\n\n      | MID  | 22°              | 25°               | 0.662         | Modest rotation        |\n\n      | LOW  | 45°              | 40°               | 0.567         | Substantial\n      misalignment|\n\n      '\n  figures_description:\n  - 'Simpson''s Paradox 可视化（核心图）：scatter plot, x=CKA, y=ZS AUROC。 每点为一个 (layer, language)\n    pair。颜色编码 normalized depth (0-1)。 左图 Qwen3 (480 points)，右图 Llama4 (240 points)。\n    Overall trend line 斜率为负（黑色虚线），per-depth-bin trend lines 斜率为正 （彩色实线，对应不同深度 bin）。Sign\n    reversal 清晰可见。 Annotation: \"Raw rho=−0.22 (p<0.001) vs Partial rho=+0.16 (p=0.07)\"\n    for Qwen3, \"Raw rho=−0.28 (p<0.001) vs Partial rho=+0.29 (p=0.018)\" for Llama4.\n\n    '\n  - 'CKA × layer × language heatmap: 两个 panel（一个 per model），x=20 languages （按 mean\n    CKA 排序），y=probed layers。颜色=CKA 值。显示 CKA cliff 在 Qwen3 上 更突然（L64 以上的条带从暖色骤变冷色），在\n    Llama4 上更渐进。\n\n    '\n  analysis: 'Simpson''s Paradox 在 full-scale 上部分确认：Llama 4 Scout 上统计显著（partial rho=0.29,\n    p=0.018），Qwen3-235B 上 trending 但不显著（partial rho=0.16, p=0.072）。 这一架构依赖性本身是有意义的发现。Paper\n    中用 hedged language 报告： \"In architectures where the CKA-depth gradient is steep\n    (Llama 4 Scout), partial correlation controlling for depth reveals a significant\n    positive relationship between CKA and transfer AUROC (rho=0.29, p=0.018), indicating\n    that CKA provides genuine explanatory power beyond depth. In architectures with\n    a delayed, step-function-like CKA decline (Qwen3-235B), the linear partial correlation\n    is trending but not significant (rho=0.16, p=0.072), possibly because the non-linear\n    depth-CKA relationship reduces the effectiveness of linear depth control.\" Subspace\n    angle analysis 提供了 CKA 分析的定量补充——HIGH 语言角度小（zero-shot 可行）， LOW 语言角度大（需要 alignment）——这与\n    Procrustes reversal 发现互洽。\n\n    '\n- name: Linear Projection Sensitivity & Procrustes Effect Reversal\n  plan_id: plan_012\n  description: 'Vary parallel pairs (10, 20, 50, 100, 200) for linear projection。\n    两模型 × 5 代表层 × 20 语言。Resource-tier stratified saturation curves。 含 Procrustes effect\n    reversal 分析。\n\n    '\n  expected_results:\n    overall_pairs_to_95pct: 70\n    per_tier_pairs_to_95pct:\n      HIGH: 35\n      MID: 55\n      LOW: 75\n    saturation_curve:\n      pairs_10:\n        pct_of_max: 0.42\n        mean_delta_auroc: 0.013\n      pairs_20:\n        pct_of_max: 0.62\n        mean_delta_auroc: 0.02\n      pairs_50:\n        pct_of_max: 0.84\n        mean_delta_auroc: 0.027\n      pairs_100:\n        pct_of_max: 0.95\n        mean_delta_auroc: 0.03\n      pairs_200:\n        pct_of_max: 1.0\n        mean_delta_auroc: 0.032\n    procrustes_reversal:\n      threshold_estimate: 0.55\n      threshold_ci_95:\n      - 0.46\n      - 0.63\n      benefit_below_0.50:\n        mean_delta: 0.058\n        n_langs: 4\n      ambiguous_0.50_0.62:\n        mean_delta: 0.012\n        n_langs: 8\n      harm_above_0.62:\n        mean_delta: -0.018\n        n_langs: 8\n    curve_cleanness: 'noisy, especially LOW tier (R² of saturation fit: HIGH=0.96,\n      MID=0.91, LOW=0.78)'\n  result_rationale: 'Linear projection（Procrustes alignment）通过学习 EN→target 的旋转矩阵对齐\n    correctness subspace。Saturation 速度取决于子空间旋转的复杂度：HIGH 语言的 EN-target subspace 角度小（~10°），10-20\n    pairs 就足以估计一个简单旋转，35 pairs 达到 95%；LOW 语言角度大 （~40-45°），需要更多 pairs 来稳定估计更复杂的旋转，75\n    pairs 才达到 95%。 Overall 70 pairs（而非 pilot 预估的 ~50 pairs）因为 (1) 20 语言比 5 语言引入更多方差，\n    (2) 部分低资源语言的 parallel data 翻译质量低（机翻 artifacts），增加了 noise。 Curves 在 LOW tier 不够干净（R²=0.78）——个别语言的饱和曲线不单调（20\n    pairs 时偶然 好于 50 pairs），因为 parallel pair 的质量方差大。 Procrustes reversal 的机制：当 ZS AUROC\n    已高（>0.62），EN probe 的 correctness direction 与 target 语言已经 well-aligned（subspace\n    angle <15°），Procrustes 旋转引入的估计噪声 反而大于 alignment gain→净效果为负。当 ZS AUROC 低（<0.50），严重\n    misalignment （angle >40°）使得 Procrustes 的 alignment gain 远大于估计噪声→净效果明显为正。 阈值 ~0.55\n    对应 subspace angle ~20-25° 的平衡点。\n\n    '\n  tables:\n  - name: Saturation Curves by Resource Tier (Qwen3-235B, L68)\n    data: '| Pairs | HIGH ΔAUROC | MID ΔAUROC | LOW ΔAUROC | Overall ΔAUROC |\n\n      |-------|-------------|------------|------------|----------------|\n\n      | 10    | +0.002      | +0.010     | +0.028     | +0.013         |\n\n      | 20    | +0.005      | +0.018     | +0.042     | +0.020         |\n\n      | 50    | +0.007      | +0.026     | +0.054     | +0.027         |\n\n      | 100   | +0.008      | +0.029     | +0.060     | +0.030         |\n\n      | 200   | +0.008      | +0.030     | +0.063     | +0.032         |\n\n      '\n  - name: Procrustes Effect Reversal by ZS AUROC Band\n    data: '| ZS AUROC band | n langs | Mean Δ from proj | Std   | % positive | Example\n      langs |\n\n      |---------------|---------|------------------|-------|------------|---------------|\n\n      | < 0.50        | 4       | +0.058           | 0.022 | 100%       | am, yo,\n      my, te|\n\n      | 0.50 - 0.55   | 2       | +0.035           | 0.018 | 100%       | sw, bn        |\n\n      | 0.55 - 0.60   | 2       | +0.012           | 0.015 | 75%        | th, tr        |\n\n      | 0.60 - 0.65   | 4       | +0.003           | 0.012 | 50%        | hi, vi,\n      ko, ar|\n\n      | 0.65 - 0.70   | 4       | -0.008           | 0.010 | 25%        | ru, ja,\n      de, pt|\n\n      | > 0.70        | 4       | -0.018           | 0.008 | 0%         | zh, es,\n      fr, ...  |\n\n      '\n  figures_description:\n  - 'Saturation curve plot: x=number of parallel pairs (log scale), y=ΔAUROC vs zero-shot。\n    三条线（HIGH/MID/LOW tier），每条带 shaded bootstrap 95% CI。 HIGH 线快速 plateau（30-40 pairs\n    后几乎 flat），LOW 线缓慢上升且 CI 更宽。 Horizontal dashed line 标注 \"95% of max improvement\"。\n\n    '\n  - 'Procrustes reversal scatter: x=ZS AUROC (zero-shot baseline), y=ΔAUROC from linear\n    projection (200 pairs)。每点一个 (language, model) pair，颜色编码 model。 LOESS 拟合曲线显示从正到负的渐变。Vertical\n    band 标注 reversal threshold 及 95% CI。\n\n    '\n  analysis: 'Linear projection 的 sample efficiency 是最直接的 practical contribution： 70\n    parallel pairs（约 2-3 小时标注工作）达到 95% of maximum improvement。 Resource-tier stratification\n    为 practitioners 提供指导：HIGH 语言不需要 projection （可能有害），LOW 语言需要 ~75 pairs。Procrustes\n    reversal 是重要的 practitioner caveat： 不加区分地对所有语言做 alignment 会损害已经 well-aligned 的语言。\n    建议 deployment strategy: 先测试 zero-shot AUROC，低于 0.55 时使用 linear projection， 高于\n    0.62 时直接使用 zero-shot。\n\n    '\n- name: Probing Control Tasks (Hewitt & Liang 2019) — Full Scale\n  plan_id: plan_013\n  description: '随机排列标签训练 control probes，计算 selectivity (real - control AUROC)， 2 模型\n    × 20 语言 × 所有 probed 层。验证 AUROC 反映 genuine correctness direction。\n\n    '\n  expected_results:\n    artifact_rate_low_resource: 0.3\n    artifact_rate_mid_resource: 0.28\n    artifact_rate_high_resource: 0.06\n    artifact_threshold_selectivity: 0.05\n    overall_artifact_rate: 0.18\n    en_selectivity_profile:\n      shallow: 0.03\n      mid: 0.12\n      deep: 0.25\n    per_tier_selectivity_deep_layers:\n      HIGH: 0.22\n      MID: 0.14\n      LOW: 0.06\n    control_auroc_range:\n    - 0.48\n    - 0.52\n    affected_layer_range: primarily layers 0-40% depth\n  result_rationale: 'Pilot（Qwen2.5-7B, EN）显示 selectivity 在浅层低（L0-L12: 0.02-0.04）、深层高\n    （L20-L27: 0.24-0.26）。跨语言扩展时，LOW 资源语言的 selectivity 全面下降： (1) 这些语言的 activations\n    中 correctness signal 更弱（模型对这些语言\"知道\"更少）， (2) probe 在小 activation difference 上更依赖\n    capacity 来拟合训练集。 LOW 资源语言在深层的 selectivity 仅 ~0.06（vs EN 的 ~0.25），许多 layer-language\n    组合的 selectivity < 0.05 artifact threshold。30% 的 LOW resource layer-language 组合为\n    artifacts。MID 资源语言出乎意料地也有 ~28% artifact rate——这是因为 MID 资源语言中包含一些 \"表面高资源但 knowledge\n    coverage 低\" 的语言（如 tr, vi: 模型训练数据中 token 多但 MMLU 领域覆盖差）。HIGH 资源语言 artifact rate\n    仅 6% （仅在最浅层 L0-L4）。这一发现波及范围比初始预期更广（从 \"~28% low-resource\" 扩展到 \"~28% low + ~28%\n    mid\"），强化了 methodological warning 的重要性。\n\n    '\n  tables:\n  - name: Artifact Rate by Resource Tier and Depth (Qwen3-235B)\n    data: '| Depth zone     | HIGH artifact % | MID artifact % | LOW artifact % |\n\n      |----------------|-----------------|----------------|----------------|\n\n      | 0-25% depth    | 17%             | 58%            | 83%            |\n\n      | 25-50% depth   | 4%              | 33%            | 67%            |\n\n      | 50-75% depth   | 0%              | 17%            | 17%            |\n\n      | 75-100% depth  | 0%              | 4%             | 0%             |\n\n      | Overall        | 6%              | 28%            | 30%            |\n\n      '\n  - name: Selectivity at EN-Optimal Layer by Language\n    data: '| Tier | Language | Real AUROC | Control AUROC | Selectivity | Artifact?\n      |\n\n      |------|----------|------------|---------------|-------------|-----------|\n\n      | HIGH | zh       | 0.732      | 0.498         | 0.234       | No        |\n\n      | HIGH | es       | 0.741      | 0.495         | 0.246       | No        |\n\n      | MID  | hi       | 0.665      | 0.502         | 0.163       | No        |\n\n      | MID  | tr       | 0.655      | 0.508         | 0.147       | No        |\n\n      | LOW  | sw       | 0.592      | 0.505         | 0.087       | No        |\n\n      | LOW  | bn       | 0.608      | 0.501         | 0.107       | No        |\n\n      | LOW  | yo       | 0.542      | 0.510         | 0.032       | YES       |\n\n      | LOW  | am       | 0.530      | 0.512         | 0.018       | YES       |\n\n      '\n  figures_description:\n  - 'Selectivity heatmap: x=20 languages (按 tier 排列)，y=probed layers (按深度)， 颜色=selectivity。左下区域（浅层\n    + 低资源）为深蓝色（artifact zone, selectivity < 0.05）, 右上区域（深层 + 高资源）为暖色。虚线框标注 artifact\n    zone boundary。 第二行小图：同样 heatmap 但二值化（artifact yes/no），清晰显示 30% LOW + 28% MID 覆盖率。\n\n    '\n  analysis: 'Control task 发现是独立的 methodological contribution：首次在 cross-lingual probing\n    中 系统性应用 Hewitt & Liang selectivity analysis，发现 ~30% low-resource 和 ~28% mid-resource\n    language-layer 组合的 probing results 不可靠。Field-level implication: 所有 cross-lingual\n    probing 研究（包括 Xiao et al.）应包含 selectivity checks。 在 paper 中：(1) 用 selectivity\n    threshold 过滤不可靠结果后重新报告 main results （确认过滤后结论不变），(2) 将过滤信息作为 methodological recommendation\n    在 main body 报告（不只是 appendix），(3) 讨论与 Voita & Titov MDL probes 的关系。\n\n    '\n- name: Gemma 4 31B Dense — Third Architecture\n  plan_id: plan_008\n  description: 'Dense 架构对照（vs 两个 MoE），60 层 FP16，20+ 语言。 提供 dense vs MoE 架构对比。Camera-ready\n    extension。\n\n    '\n  expected_results:\n    en_best_auroc: 0.77\n    en_best_layer: 52\n    en_best_layer_depth_pct: 0.867\n    mean_zs_auroc: 0.655\n    zs_pass_rate: 0.72\n    pareto_strength: intermediate (between Qwen3 and Llama4)\n    pareto_significant_langs: 13\n    cka_cliff_slope: -0.012\n    cka_cliff_onset_depth_pct: 0.6\n    partial_rho_cka: 0.22\n    partial_p: 0.045\n    simpson_significant: true\n  result_rationale: 'Dense 架构的 CKA decline 比 MoE 更渐进（无 expert routing 加速特异化）， slope\n    ~-0.012/layer vs MoE 的 -0.015 to -0.025。Pareto 强度介于 Qwen3（最强） 和 Llama4（最弱）之间。Simpson''s\n    Paradox 在 Gemma 4 上显著（partial rho=0.22, p=0.045）——CKA gradient 斜率介于两者之间，足以使 linear\n    partial correlation 有效。 如果 Gemma 4 的 partial correlation 也显著，则 Simpson''s Paradox\n    变为 2/3 架构显著， 可强化叙事（但 camera-ready only）。EN AUROC ~0.77 与 Qwen3 的 0.78 接近 （31B\n    dense vs 22B active MoE, 参数效率相当）。\n\n    '\n  tables:\n  - name: Three-Architecture Comparison (Camera-Ready)\n    data: '| Metric                 | Qwen3-235B | Llama4 Scout | Gemma4 31B |\n\n      |------------------------|------------|--------------|------------|\n\n      | Type                   | MoE        | MoE          | Dense      |\n\n      | Active params          | 22B        | 17B          | 31B        |\n\n      | Layers                 | 94         | 48           | 60         |\n\n      | EN best AUROC          | 0.78       | 0.76         | 0.77       |\n\n      | Mean ZS AUROC          | 0.660      | 0.643        | 0.655      |\n\n      | Pareto sig langs       | 15         | 11           | 13         |\n\n      | Partial rho (CKA)      | 0.16 (ns)  | 0.29**       | 0.22*      |\n\n      | CKA cliff slope        | -0.025     | -0.015       | -0.012     |\n\n      '\n  figures_description:\n  - '三架构 CKA depth profile 对比：x=normalized depth (0-1)，y=mean CKA (20 langs)。 三条线：Qwen3（late\n    sharp cliff），Llama4（early gradual decline）， Gemma4（intermediate）。Annotation 标注\n    cliff onset 和 slope。\n\n    '\n  analysis: 'Gemma 4 作为 dense 架构对照，确认 Pareto 和 Simpson''s Paradox 不是 MoE 特有。 三架构对比暗示\n    CKA cliff slope 可能是决定 Pareto 强度和 partial correlation 显著性的关键因素——但 n=3 架构仅为 suggestive\n    correlation，不能做因果推断。 Camera-ready 增加第三个架构使结论更稳健。\n\n    '\n- name: Extended Language Coverage (50+ Languages)\n  plan_id: plan_009\n  description: '从 20 扩展至 50+ 语言，利用 GlobalMMLU/Belebele 全语言集。Camera-ready extension。\n\n    '\n  expected_results:\n    total_languages: 52\n    zs_pass_rate_52: 0.62\n    artifact_rate_very_low_resource: 0.48\n    new_low_resource_langs_with_artifacts: 18\n    resource_tier_gradient_confirmed: true\n    rank_correlation_20_vs_52: 0.94\n    new_findings: diminishing returns; very-low-resource languages (< 1M tokens in\n      training) uniformly fail\n    min_zs_auroc: 0.49\n    min_zs_lang: Haitian Creole (ht)\n  result_rationale: '扩展到 52 语言主要增加低资源语言。新增的 32 语言大多为 LOW 或 VERY-LOW resource， ZS AUROC\n    多在 0.50-0.58 范围。Pass rate 从 20 语言的 ~72% 降到 52 语言的 ~62%， 因为新增语言偏向低资源。Resource-tier\n    gradient 在更大规模上确认——artifact rate 在 very-low-resource 语言（<1M training tokens）中达\n    48%，几乎一半结果不可靠。 但 20 语言的核心发现在 52 语言上完全保持（rank correlation 0.94）。 边际收益递减：每增加一种语言，对核心\n    claim 的增量证据很小。 主要贡献是增加统计功效和覆盖度，而非新发现。\n\n    '\n  tables:\n  - name: Language Coverage Expansion Summary\n    data: '| Tier        | 20-lang count | 52-lang count | Mean ZS AUROC | Artifact\n      rate |\n\n      |-------------|---------------|---------------|---------------|---------------|\n\n      | HIGH        | 6             | 8             | 0.72          | 4%            |\n\n      | MID         | 8             | 14            | 0.66          | 22%           |\n\n      | LOW         | 6             | 18            | 0.57          | 35%           |\n\n      | VERY-LOW    | 0             | 12            | 0.52          | 48%           |\n\n      '\n  figures_description:\n  - 'World map: 52 语言标注在地图上，颜色编码 ZS AUROC（绿=高，红=低）。 清晰显示 Western Europe 和 East Asia\n    为绿色，Sub-Saharan Africa 和 Southeast Asia 低资源语言为红色。\n\n    '\n  analysis: Camera-ready 的 52 语言扩展提供了更全面的覆盖，但 story 不变。 VERY-LOW resource 语言（ht, rm,\n    fy 等）的 ~48% artifact rate 强化了 probing control 的必要性。Paper 中报告 52 语言结果但 core analysis\n    仍基于 20 语言（统计方法学更干净）。\n",
      "numLines": 1238,
      "startLine": 1,
      "totalLines": 1238
    }
  },
  "sourceToolAssistantUUID": "7cadedf1-31fa-47d5-8271-e43e5543ab89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19 · 2026-05-21T12:52:35.158Z_

````json
{
  "parentUuid": "794ca727-d9ab-4e2e-8f0a-31b40edeed9d",
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
  "uuid": "04ce0fc2-d63c-41a3-b174-bb618dc8464e",
  "timestamp": "2026-05-21T12:52:35.158Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "04ce0fc2-d63c-41a3-b174-bb618dc8464e",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiment predictions for cross-lingual correctness probe transfer",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Assistant

_source line 22 · 2026-05-21T12:53:02.330Z_

<details><summary>Logged reasoning block</summary>

```text
I have the previous dream report's median imagined experiments. Now I need to read the existing data carefully and generate the detailed median-tier predictions for each planned experiment. Let me also check what experiments are planned vs done.

From the experiment_plan, the planned experiments (status != DONE) are:
- plan_001: Full Pareto Frontier — Qwen3-235B-A22B (planned)
- plan_002: Full Pareto Frontier — Llama 4 Scout (registry_id: plan_002_v3, RUNNING/PREPARING)
- plan_003: CaCLR implementation (planned)


- plan_004: Difficulty-controlled ablation (planned)
- plan_005: Cross-lingual orthogonality (planned)
- plan_006: Probe complexity comparison (planned)
- plan_007: Additional benchmark evaluation (planned)
- plan_008: Gemma 4 Dense (planned)
- plan_009: Extended language coverage (planned)
- plan_010: Quantization validation (planned)
- plan_011: CKA analysis (planned)
- plan_012: Linear projection sensitivity (planned)

The completed experiments are the three MVP validations and plan_013.

Now I'm generating detailed median-tier predictions for each planned experiment with result rationales, using the previous dream report as a reference for the expected level of detail. I need to ensure the predictions align with the median tier parameter ranges: English AUROC between 0.76-0.82, zero-shot transfer pass rates of 12-16 out of 20, mean zero-shot AUROC drops of 8-14 percentage points versus English, and Pareto tradeoff prevalence between 0.25-0.5 across language-architecture pairs. Writing YAML metrics...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04ce0fc2-d63c-41a3-b174-bb618dc8464e",
  "isSidechain": false,
  "requestId": "req_011CbFkDPVUiivmrJX2v7vRg",
  "type": "assistant",
  "uuid": "854e0eae-f974-474f-a9f7-1b04cce4a480",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jk2E9RiXR4KWjmRJFcM2Ui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42818,
      "cache_read_input_tokens": 75187,
      "output_tokens": 1808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1808,
          "cache_read_input_tokens": 75187,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-21T13:00:37.406Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project context. I need to read the previous dream report's median tier to understand what was already generated, and then produce my own detailed median-tier predictions for each planned experiment.

Let me check what experiments are "planned" status (not DONE) to know which ones I need to generate predictions for.

From the experiment plan:
- plan_001: planned (Qwen3-235B full Pareto)
- plan_002: planned/RUNNING (Llama 4 Scout full Pareto) 
- plan_003: planned (CaCLR)


- plan_004: planned (Difficulty decomposition)
- plan_005: planned (Cross-lingual orthogonality)
- plan_006: planned (Probe complexity)
- plan_007: planned (Additional benchmarks)
- plan_008: planned (Gemma 4 Dense)
- plan_009: planned (Extended language coverage)
- plan_010: planned (Quantization validation)
- plan_011: planned (CKA analysis)
- plan_012: planned (Linear projection sensitivity)
- plan_013: DONE (Probing controls)

I've already reviewed the previous dream report's median imagined experiments, which gives me the baseline to work from.

Now I'm working through each experiment systematically using the median tier parameters from the user's prompt. I need to instantiate the specific ranges for metrics like English AUROC performance, zero-shot transfer success rates, cross-lingual degradation patterns, Pareto frontier prevalence, and the CKA partial correlation statistics to build out my own detailed version. Now I'm looking at the correlation between depth and transfer effectiveness across the multilingual samples. I need to generate a comprehensive YAML output covering all the planned experiments, so let me work through each one systematically to produce detailed metrics that align with the median tier definitions. I'm looking at the selectivity range of 0.24-0.26 for the control task, then setting performance targets for the median tier across three architectures to hit an overall mean AUROC around 0.783, which falls nicely within the [0.76, 0.82] range. For zero-shot transfer, I need to aim for 12-16 passing languages out of 20 to hit that 60-80% success rate. Now I'm ready to build out the comprehensive YAML configuration, making sure to carefully calibrate each model's expected performance based on what we learned from the pilots.

For CaCLR specifically in the median tier, the delta over zero-shot should hover near zero with maybe a tiny positive effect, and only about 5-10 languages showing improvement—which really underscores that CaCLR isn't delivering much here, though it's not completely inert either. The mean effect being negligible is the story, and that's what the numbers should reflect. I'm going to write out the full YAML now with the same level of detail as the previous report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "854e0eae-f974-474f-a9f7-1b04cce4a480",
  "isSidechain": false,
  "requestId": "req_011CbFkDPVUiivmrJX2v7vRg",
  "type": "assistant",
  "uuid": "4c076b89-4bdf-431f-b778-c363749292bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017g6UKLJKN4u9bDBA3fcBgm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42818,
      "cache_read_input_tokens": 75187,
      "output_tokens": 1808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1808,
          "cache_read_input_tokens": 75187,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 24 · 2026-05-21T13:00:37.408Z_

Now let me review the CORAL/high-dim MMD details and the decisions file for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c076b89-4bdf-431f-b778-c363749292bf",
  "isSidechain": false,
  "requestId": "req_011CbFkDPVUiivmrJX2v7vRg",
  "type": "assistant",
  "uuid": "00fa3dec-7850-4faa-877a-6f94a9dcebff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017g6UKLJKN4u9bDBA3fcBgm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42818,
      "cache_read_input_tokens": 75187,
      "output_tokens": 1808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1808,
          "cache_read_input_tokens": 75187,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 25 · 2026-05-21T13:00:37.411Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NBHQe6xJVt7hbzNqVNyR9H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00fa3dec-7850-4faa-877a-6f94a9dcebff",
  "isSidechain": false,
  "requestId": "req_011CbFkDPVUiivmrJX2v7vRg",
  "type": "assistant",
  "uuid": "c6700746-82fa-486b-9c72-a1cc7ee5d110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017g6UKLJKN4u9bDBA3fcBgm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42818,
      "cache_read_input_tokens": 75187,
      "output_tokens": 1808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1808,
          "cache_read_input_tokens": 75187,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-21T13:00:37.422Z_

<details><summary>↩ Tool result · `toolu_01NBHQe6xJVt7hbzNqVNyR9H`</summary>

```text
1	_next_id: 19
2	decisions:
3	- id: D001
4	  date: 2026-05-20 13:49 UTC
5	  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B
6	  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &
7	    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B
8	    的大资源。
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-20 13:53 UTC
13	  summary: MVP 模型固定为 Qwen2.5-7B-Instruct
14	  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为
15	    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。
16	  related_experiments: []
17	  depends_on: []
18	- id: D003
19	  date: 2026-05-20 18:25 UTC
20	  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言
21	  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用
22	    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。
23	  related_experiments:
24	  - exp_id: mvp_001
25	    role: trigger
26	    result: P4 ΔAUROC=0 暴露标准设计缺陷
27	  depends_on: []
28	- id: D004
29	  date: 2026-05-20 18:52 UTC
30	  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'
31	  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth
32	    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift
33	    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift
34	    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。
35	  related_experiments:
36	  - exp_id: mvp_001
37	    role: primary
38	    result: P1✅P2✅P3✅P4❌, core hypothesis supported
39	  depends_on: []
40	- id: D005
41	  date: 2026-05-20 20:14 UTC
42	  summary: 'Dream review (3/6 weak reject) processed: 13 confirmed actions, 5 observations,
43	    3 ignores. Framing updated with conditional CaCLR narrative + 6 new reviewer concerns.
44	    3 new P1 experiments added (CKA, linproj sensitivity, control tasks). Proceeding
45	    with re-dream after changes.'
46	  rationale: 'Dream dream_20260520T185641 scored best=4/6 median=3/6 worst=3/6. Key
47	    structural issues identified across all 3 tiers: (1) no statistical tests — added
48	    as cross-cutting requirement; (2) CaCLR framing incoherent — redesigned as conditional
49	    narrative with two paths; (3) missing related work (domain adaptation theory,
50	    alignment literature, probing critiques) — added to paper_framing.md. Two-tier
51	    issues: (4) no mechanistic explanation — added plan_011 CKA analysis; (5) arbitrary
52	    AUROC threshold — added sensitivity analysis requirement; (6) probing methodology
53	    — added plan_013 control tasks. CaCLR consistency loss value is the key data-dependent
54	    risk (O3). Core 4-claim structure preserved; framing strengthened not weakened.
55	    No venue downgrade — issues are addressable via experiments and framing improvements.'
56	  related_experiments:
57	  - exp_id: plan_003
58	    role: affected
59	    result: CaCLR conditional narrative added
60	  - exp_id: plan_011
61	    role: new
62	    result: CKA mechanistic analysis (P1, 5 GPU-hrs)
63	  - exp_id: plan_012
64	    role: new
65	    result: Linear projection sensitivity (P1, 2 GPU-hrs)
66	  - exp_id: plan_013
67	    role: new
68	    result: Probing control tasks (P1, 2 GPU-hrs)
69	  depends_on:
70	  - D004
71	- id: D006
72	  date: 2026-05-20 20:23 UTC
73	  summary: 'MVP gate re-evaluation after P1 leakage fix: 2/4 PASS, still proceed to
74	    research phase'
75	  rationale: 'M005 reveals temp scaling data leakage — P1 ECE now FAIL (0.2216 > 0.15).
76	    Gate drops from 3/4 to 2/4 PASS. However, the 2 passing criteria (P2: cross-lingual
77	    transfer 4/5 langs, P3: layer depth effect 14.28pp) are the hypothesis-critical
78	    ones that validate "correctness direction exists and transfers cross-lingually."
79	    P1 ECE failure means raw probes are poorly calibrated — this is exactly the problem
80	    CaCLR is designed to solve, and actually strengthens the paper''s motivation ("probe-based
81	    calibration needs CaCLR because naive probes fail on calibration"). P4 mean-shift
82	    failure was already attributed to criteria design error (D003). Research phase
83	    continues with strengthened CaCLR motivation. The 0.15 ECE threshold for P1 was
84	    always somewhat arbitrary — discrimination (AUROC=0.754) is the primary signal
85	    that correctness information is linearly accessible.'
86	  related_experiments:
87	  - exp_id: mvp_001
88	    role: gate_check
89	    result: 2/4 PASS (P2+P3), P1 ECE FAIL after leakage fix
90	  - exp_id: plan_003
91	    role: motivated_by
92	    result: CaCLR motivation strengthened by raw probe calibration failure
93	  depends_on:
94	  - D004
95	  - D005
96	- id: D007
97	  date: 2026-05-20 20:31 UTC
98	  summary: 'mvp_003 (Llama-3.1-8B) cross-architecture validation: 3/4 PASS, Pareto
99	    architecture-dependence confirmed as core finding'
100	  rationale: 'mvp_003 gate 3/4 PASS (P1 PASS without temp scaling, P2 5/5, P3 7.85pp,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6700746-82fa-486b-9c72-a1cc7ee5d110",
  "isSidechain": false,
  "promptId": "b7585d46-2ea0-497d-8a35-64b3c1f62eec",
  "type": "user",
  "uuid": "879dce66-3407-41c7-acee-814ec6674ac9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml",
      "content": "_next_id: 19\ndecisions:\n- id: D001\n  date: 2026-05-20 13:49 UTC\n  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B\n  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &\n    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B\n    的大资源。\n  related_experiments: []\n  depends_on: []\n- id: D002\n  date: 2026-05-20 13:53 UTC\n  summary: MVP 模型固定为 Qwen2.5-7B-Instruct\n  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为\n    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。\n  related_experiments: []\n  depends_on: []\n- id: D003\n  date: 2026-05-20 18:25 UTC\n  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言\n  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用\n    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。\n  related_experiments:\n  - exp_id: mvp_001\n    role: trigger\n    result: P4 ΔAUROC=0 暴露标准设计缺陷\n  depends_on: []\n- id: D004\n  date: 2026-05-20 18:52 UTC\n  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'\n  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth\n    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift\n    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift\n    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。\n  related_experiments:\n  - exp_id: mvp_001\n    role: primary\n    result: P1✅P2✅P3✅P4❌, core hypothesis supported\n  depends_on: []\n- id: D005\n  date: 2026-05-20 20:14 UTC\n  summary: 'Dream review (3/6 weak reject) processed: 13 confirmed actions, 5 observations,\n    3 ignores. Framing updated with conditional CaCLR narrative + 6 new reviewer concerns.\n    3 new P1 experiments added (CKA, linproj sensitivity, control tasks). Proceeding\n    with re-dream after changes.'\n  rationale: 'Dream dream_20260520T185641 scored best=4/6 median=3/6 worst=3/6. Key\n    structural issues identified across all 3 tiers: (1) no statistical tests — added\n    as cross-cutting requirement; (2) CaCLR framing incoherent — redesigned as conditional\n    narrative with two paths; (3) missing related work (domain adaptation theory,\n    alignment literature, probing critiques) — added to paper_framing.md. Two-tier\n    issues: (4) no mechanistic explanation — added plan_011 CKA analysis; (5) arbitrary\n    AUROC threshold — added sensitivity analysis requirement; (6) probing methodology\n    — added plan_013 control tasks. CaCLR consistency loss value is the key data-dependent\n    risk (O3). Core 4-claim structure preserved; framing strengthened not weakened.\n    No venue downgrade — issues are addressable via experiments and framing improvements.'\n  related_experiments:\n  - exp_id: plan_003\n    role: affected\n    result: CaCLR conditional narrative added\n  - exp_id: plan_011\n    role: new\n    result: CKA mechanistic analysis (P1, 5 GPU-hrs)\n  - exp_id: plan_012\n    role: new\n    result: Linear projection sensitivity (P1, 2 GPU-hrs)\n  - exp_id: plan_013\n    role: new\n    result: Probing control tasks (P1, 2 GPU-hrs)\n  depends_on:\n  - D004\n- id: D006\n  date: 2026-05-20 20:23 UTC\n  summary: 'MVP gate re-evaluation after P1 leakage fix: 2/4 PASS, still proceed to\n    research phase'\n  rationale: 'M005 reveals temp scaling data leakage — P1 ECE now FAIL (0.2216 > 0.15).\n    Gate drops from 3/4 to 2/4 PASS. However, the 2 passing criteria (P2: cross-lingual\n    transfer 4/5 langs, P3: layer depth effect 14.28pp) are the hypothesis-critical\n    ones that validate \"correctness direction exists and transfers cross-lingually.\"\n    P1 ECE failure means raw probes are poorly calibrated — this is exactly the problem\n    CaCLR is designed to solve, and actually strengthens the paper''s motivation (\"probe-based\n    calibration needs CaCLR because naive probes fail on calibration\"). P4 mean-shift\n    failure was already attributed to criteria design error (D003). Research phase\n    continues with strengthened CaCLR motivation. The 0.15 ECE threshold for P1 was\n    always somewhat arbitrary — discrimination (AUROC=0.754) is the primary signal\n    that correctness information is linearly accessible.'\n  related_experiments:\n  - exp_id: mvp_001\n    role: gate_check\n    result: 2/4 PASS (P2+P3), P1 ECE FAIL after leakage fix\n  - exp_id: plan_003\n    role: motivated_by\n    result: CaCLR motivation strengthened by raw probe calibration failure\n  depends_on:\n  - D004\n  - D005\n- id: D007\n  date: 2026-05-20 20:31 UTC\n  summary: 'mvp_003 (Llama-3.1-8B) cross-architecture validation: 3/4 PASS, Pareto\n    architecture-dependence confirmed as core finding'\n  rationale: 'mvp_003 gate 3/4 PASS (P1 PASS without temp scaling, P2 5/5, P3 7.85pp,",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 343
    }
  },
  "sourceToolAssistantUUID": "c6700746-82fa-486b-9c72-a1cc7ee5d110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T13:00:37.574Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W39QnhixuMyqdZZ4rMpznJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_provenance.yaml",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "879dce66-3407-41c7-acee-814ec6674ac9",
  "isSidechain": false,
  "requestId": "req_011CbFkDPVUiivmrJX2v7vRg",
  "type": "assistant",
  "uuid": "ac90a448-2bde-4346-94b2-187dd15dfcdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017g6UKLJKN4u9bDBA3fcBgm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42818,
      "cache_read_input_tokens": 75187,
      "output_tokens": 1808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1808,
          "cache_read_input_tokens": 75187,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 28 · 2026-05-21T13:00:37.582Z_

<details><summary>↩ Tool result · `toolu_01W39QnhixuMyqdZZ4rMpznJ`</summary>

```text
1	paper:
2	  title: ''
3	  version: 26
4	  generated_at: '2026-05-21T10:34:42.023610+00:00'
5	claims:
6	- id: C001
7	  location:
8	    section: introduction
9	    paragraph: 0
10	    sentence: 0
11	  text: deeper layers generally improve both English probe quality and cross-lingual
12	    transfer (Spearman rho > 0.7, p < 0.05 for 4 of 5 languages)
13	  type: quantitative
14	  evidence:
15	  - exp_id: mvp_001
16	    detail: Qwen2.5-7B layer-wise EN+ZS AUROC trends
17	  - exp_id: mvp_003
18	    detail: Llama-3.1-8B layer-wise EN+ZS AUROC trends
19	  decisions: []
20	  deprecated: false
21	- id: C002
22	  location:
23	    section: introduction
24	    paragraph: 0
25	    sentence: 0
26	  text: final 1-3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer
27	    degradation (1.5-4pp in 3 of 5 languages)
28	  type: quantitative
29	  evidence:
30	  - exp_id: mvp_001
31	    detail: 'Qwen L24->L27: EN AUROC improves but ZS degrades in zh/hi/sw'
32	  - exp_id: mvp_002
33	    detail: Qwen complementary layers confirm L22-L26 ZS peak
34	  decisions: []
35	  deprecated: false
36	- id: C003
37	  location:
38	    section: introduction
39	    paragraph: 0
40	    sentence: 0
41	  text: deeper layers generally improve both English probe quality and cross-lingual
42	    transfer, but Pareto frontier reveals local tradeoff at deepest layers
43	  type: qualitative
44	  evidence:
45	  - exp_id: mvp_001
46	    detail: Qwen Pareto analysis
47	  - exp_id: mvp_003
48	    detail: Llama Pareto analysis
49	  decisions: []
50	  deprecated: false
51	- id: C004
52	  location:
53	    section: method
54	    paragraph: 0
55	    sentence: 0
56	  text: English pilot selectivity concentrated in deeper layers (L20+ > 0.20, shallow
57	    L0-L12 < 0.05)
58	  type: quantitative
59	  evidence:
60	  - exp_id: plan_013
61	    detail: 'Qwen2.5-7B English selectivity: L20=0.244, L24=0.248, L27=0.262; L0=0.02,
62	      L4=0.037, L8=0.036, L12=0.042'
63	  decisions: []
64	  deprecated: false
65	- id: C005
66	  location:
67	    section: related_work
68	    paragraph: 0
69	    sentence: 0
70	  text: English pilot selectivity concentrated in deeper layers (L20+ > 0.20, shallow
71	    < 0.05)
72	  type: quantitative
73	  evidence:
74	  - exp_id: plan_013
75	    detail: Qwen2.5-7B English selectivity data
76	  decisions: []
77	  deprecated: false
78	tables: []
79	figures: []
80	_completeness:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac90a448-2bde-4346-94b2-187dd15dfcdc",
  "isSidechain": false,
  "promptId": "b7585d46-2ea0-497d-8a35-64b3c1f62eec",
  "type": "user",
  "uuid": "9c9d87c4-9ae8-46fd-8885-d47139b0ea2b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_provenance.yaml",
      "content": "paper:\n  title: ''\n  version: 26\n  generated_at: '2026-05-21T10:34:42.023610+00:00'\nclaims:\n- id: C001\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: deeper layers generally improve both English probe quality and cross-lingual\n    transfer (Spearman rho > 0.7, p < 0.05 for 4 of 5 languages)\n  type: quantitative\n  evidence:\n  - exp_id: mvp_001\n    detail: Qwen2.5-7B layer-wise EN+ZS AUROC trends\n  - exp_id: mvp_003\n    detail: Llama-3.1-8B layer-wise EN+ZS AUROC trends\n  decisions: []\n  deprecated: false\n- id: C002\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: final 1-3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer\n    degradation (1.5-4pp in 3 of 5 languages)\n  type: quantitative\n  evidence:\n  - exp_id: mvp_001\n    detail: 'Qwen L24->L27: EN AUROC improves but ZS degrades in zh/hi/sw'\n  - exp_id: mvp_002\n    detail: Qwen complementary layers confirm L22-L26 ZS peak\n  decisions: []\n  deprecated: false\n- id: C003\n  location:\n    section: introduction\n    paragraph: 0\n    sentence: 0\n  text: deeper layers generally improve both English probe quality and cross-lingual\n    transfer, but Pareto frontier reveals local tradeoff at deepest layers\n  type: qualitative\n  evidence:\n  - exp_id: mvp_001\n    detail: Qwen Pareto analysis\n  - exp_id: mvp_003\n    detail: Llama Pareto analysis\n  decisions: []\n  deprecated: false\n- id: C004\n  location:\n    section: method\n    paragraph: 0\n    sentence: 0\n  text: English pilot selectivity concentrated in deeper layers (L20+ > 0.20, shallow\n    L0-L12 < 0.05)\n  type: quantitative\n  evidence:\n  - exp_id: plan_013\n    detail: 'Qwen2.5-7B English selectivity: L20=0.244, L24=0.248, L27=0.262; L0=0.02,\n      L4=0.037, L8=0.036, L12=0.042'\n  decisions: []\n  deprecated: false\n- id: C005\n  location:\n    section: related_work\n    paragraph: 0\n    sentence: 0\n  text: English pilot selectivity concentrated in deeper layers (L20+ > 0.20, shallow\n    < 0.05)\n  type: quantitative\n  evidence:\n  - exp_id: plan_013\n    detail: Qwen2.5-7B English selectivity data\n  decisions: []\n  deprecated: false\ntables: []\nfigures: []\n_completeness:",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 91
    }
  },
  "sourceToolAssistantUUID": "ac90a448-2bde-4346-94b2-187dd15dfcdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "9c9d87c4-9ae8-46fd-8885-d47139b0ea2b",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiment predictions for cross-lingual correctness probe transfer",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Assistant

_source line 31 · 2026-05-21T13:09:08.025Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me produce the comprehensive YAML for the median tier predictions. I need to cover all planned experiments:

1. plan_001 - Qwen3-235B Full Pareto
2. plan_002 - Llama 4 Scout Full Pareto
3. plan_003 - CaCLR
4. plan_004 - Difficulty decomposition
5. plan_005 - Cross-lingual orthogonality
6. plan_006 - Probe complexity comparison
7. plan_007 - Additional benchmarks


8. plan_008 - Gemma 4 Dense
9. plan_009 - Extended languages
10. plan_010 - Quantization validation
11. plan_011 - CKA analysis
12. plan_012 - Linear projection sensitivity

For each plan, I need to provide detailed expected_results, result_rationale, tables, figures_description, and analysis. I'm aligning everything with the median tier key metrics, using the en_auroc_best_layer_mean_across_arch range of [0.76, 0.82] with a mean of 0.79, where Qwen3 should hit 0.81 and Llama4 around 0.77.

Now I'm working through the specific metric ranges: zero-shot transfer pass rates around 70%, cross-lingual AUROC drops averaging 11 percentage points, pareto tradeoff prevalence at roughly 35% of language-architecture pairs, transfer depth drops near 2 percentage points at final layers, and CKA partial correlations varying by architecture with statistical significance thresholds.

Simpson's paradox confirmation in 1-2 of 3 architectures, negligible gains from contrastive learning around 0.3 percentage points with inconsistent language improvements, linear projection showing modest 5 percentage point gains on low-resource languages with about 80 saturation pairs, and decomposition methods yielding around 2 percentage points improvement with clean separation visible in roughly half the languages tested.

Now I'm looking at selectivity metrics in deeper layers around 0.20, cross-lingual artifact rates hovering near 22%, and positive transfer correlations appearing in about 14 of 20 languages. For the Qwen3-235B model with 94 layers and 22B active parameters, I'm estimating English performance around 0.81 AUROC with the best signal likely emerging in the 76-84 layer range, and expecting zero-shot transfer success in roughly 15 of 20 languages.

The Llama 4 Scout shows weaker Pareto effects with only 7 of 20 languages demonstrating the pattern, while Gemma 4's intermediate performance sits around 0.79 AUROC. Averaging across these three architectures gives me 0.79, which fits nicely within the expected range.

Now I'm calculating the zero-shot AUROC drops more precisely—the mean drop from about 0.79 to 0.68 is roughly 11 percentage points, which aligns with the expected 8-14 point range. For CaCLR, the delta over zero-shot is negligible at around 0.3 percentage points, and the beta sweep doesn't reveal any consistent improvements, so most languages show noise rather than real gains.

I need to make sure my predictions are well-calibrated to the median tier ranges before drafting the full YAML, so let me recalibrate the numbers carefully and start with plan_001's specifications.

For plan_001 (Qwen3-235B), I'm setting the English best AUROC at 0.81 with the optimal layer at L80, which represents about 85% of the 94-layer model. The zero-shot pass rate is 15 out of 20 languages, with a mean zero-shot AUROC of 0.69 at the English-optimal layer and 0.71 at the transfer-optimal layer. Eight languages show Pareto-significant tradeoffs, and the median correlation between English and zero-shot performance for those languages is around -0.45. The English-to-transfer gap is approximately 12 percentage points.

For plan_002 (Llama 4 Scout), the English best AUROC is 0.77 with the optimal layer at L44 (about 92% of 48 layers), the zero-shot pass rate drops to 13 out of 20, and the mean zero-shot AUROC is 0.66, with only 5 languages showing Pareto-significant tradeoffs.

For plan_008 (Gemma 4 31B), the English best AUROC is 0.79 with the optimal layer at L52 (87% of 60 layers), the zero-shot pass rate is 14 out of 20, and the mean zero-shot AUROC is 0.68 with 7 languages showing Pareto-significant tradeoffs. The English-to-transfer gap is around 11 percentage points.

Now I'm verifying the aggregate metrics: the mean English best AUROC across all three models is 0.79, the mean zero-shot pass rate is 14 languages, and the mean zero-shot drop is approximately 11 percentage points. Looking at Pareto prevalence, Qwen3 shows the strongest effect at 40%, Llama4 is weaker at 25%, and Gemma4 is intermediate at 35%.

Simpson's paradox appears in the data with significant partial correlations for Llama4 and Gemma4, confirming the phenomenon in 2 out of 3 models. The CaCLR intervention shows a modest improvement of 0.3 percentage points across 8 languages, and linear projection analysis reveals a 5 percentage point gain for low-resource languages.

Now I'm checking the remaining metrics—decomposition shows a 1.8 percentage point improvement with clean separation in 5 out of 10 cases, the control task validates selectivity and artifact rates within expected ranges, and across the 20 languages tested, 14 show positive Spearman correlation between depth and transfer performance. All the numbers check out against their calibration targets, so I'm ready to generate the YAML configuration. I need to clarify what this metric actually measures—it's the correlation between layer depth and zero-shot transfer AUROC across languages. Most languages show a positive relationship (12-17 out of 20), meaning deeper layers generally improve transfer performance, but the Pareto tradeoff appears as a local effect at the deepest layers where English AUROC continues rising while transfer performance drops.

Now I'm working through the full YAML configuration and need to carefully evaluate CaCLR in the median tier. The β parameter sweep shows minimal gains across all values—β=0.01 gives the best result at around +0.3pp but it's not statistically significant, while larger values like β=1.0 actually hurt performance. CORAL and high-dimensional MMD approaches also fail to produce significant improvements, and the multi-seed variance is tight enough (0.003-0.005) that these differences are well within noise.

Looking at the cross-language results, only 8 out of 20 languages show positive deltas and none reach significance individually. The component ablation reveals that SB-ECE provides a slight ECE improvement but doesn't help AUROC. What's particularly telling is that even when I push to higher-dimensional MMD spaces, the distributional matching approach still doesn't work—this suggests the problem isn't about dimensionality but something more fundamental about the approach itself.

I'm ready to generate the full output now with the same level of detail as the reference, using my calibrated numbers and clear rationales for each finding.

Now I need to make sure I include the CORAL comparison, the high-dimensional MMD variants with PCA at d=50 and d=100, results across multiple seeds, and the mixed β criterion using zh and sw validation sets in the CaCLR predictions. I'll keep the YAML concise while ensuring the content is thorough and directly supports the key findings. I should target the center of the range more. Let me use:
- Qwen3: EN best 0.81 (22B active MoE is much bigger than 7B, 235B total)
- Llama4: EN best 0.77 (17B active, smaller)
- Gemma4: EN best 0.79 (31B dense)
- Mean: 0.79 ✓

For ZS:
- Qwen3 mean ZS: 0.69 (drop 12pp)
- Llama4 mean ZS: 0.66 (drop 11pp)
- Gemma4 mean ZS: 0.68 (drop 11pp)
- Overall mean ZS drop: ~11pp ✓

These are slightly more optimistic than the previous dream but still solidly in median range. The median tier describes findings that replicate at scale but with smaller effect sizes and more noise, so I need to be careful not to be too optimistic about improvements. Scaling from 7B to 17-31B active parameters should help, but the correctness signal probably won't be dramatically stronger in the larger models. Looking at the pilot data—Qwen-7B at 0.754 and Llama-8B at 0.728—and accounting for the 3-4x increase in active parameters, I'm estimating more modest gains than simple scaling laws would suggest. I'm finalizing the metrics across these three models—checking that the depth-transfer drops are consistent around 11 percentage points and that the zero-shot pass rates average to 14, then recalculating Qwen3's mean zero-shot score to verify it aligns with the 11pp drop from the English best layer performance. I think the key is that "mean_zs_auroc_drop_vs_en_pp" measures the drop at the EN-optimal layer, but each language can achieve better zero-shot performance at its own transfer-optimal layer. So the metric is comparing EN's best performance against the mean of each language's best performance across all layers—which explains why the drop is smaller than it initially seemed.

Now looking at the Pareto tradeoff prevalence, about a third of the language-architecture pairs show a clear tradeoff between English and zero-shot performance. Qwen3 exhibits this most strongly at 40% of pairs, likely due to its MoE structure and sharp CKA cliff, while Llama4 shows it least frequently at 25% with its more gradual decline.

For the final layer transfer degradation, I'm seeing a range of 1.0 to 3.0 percentage points, with Qwen3 dropping most steeply at 2.5pp in those deepest layers, Llama4 the most gradual at 1.2pp, and Gemma4 falling in between. The partial correlation between architecture and transfer performance shows Qwen3 trending toward significance but not quite there, while Llama4 reaches statistical significance with a correlation of 0.31.

Looking at the Simpson's paradox check, I've got 2 out of 3 architectures showing significant effects—Llama4 and Gemma4 both cross the significance threshold. The pilot data for Qwen3 showed a non-significant result that's holding up even with the expanded dataset, whereas Llama4's strong pilot effect of 0.41 appears to be attenuating slightly at full scale but still maintaining significance.

Now I'm moving into the detailed experimental design for plan_003, laying out the parameter sweeps and ablation studies I need to run—testing different β and α values across multiple loss function combinations to isolate which components are driving the performance gains.

Looking at the multi-seed results across all the distributional matching variants, they're consistently underperforming in the median tier, whether it's 1-D or high-dimensional MMD, or CORAL with different dimensionalities—none of them show significant improvements, which suggests the issue isn't specific to one approach but rather that distributional matching itself isn't helping here. The multi-seed runs show CaCLR has higher variance than the zero-shot baseline despite a modest mean improvement.

Now I'm realizing the CaCLR language improvements are scattered across the 20 languages with only 25-50% showing gains, and the mean delta is so small it's essentially noise—some languages improve slightly while others degrade, so there's no meaningful pattern emerging by resource tier or language family. I should draft a comprehensive YAML summary that captures all these negative results and the instability findings.

Before I do that, let me recalibrate the linear projection metrics: the saturation point sits around 85 pairs for reaching 95% of maximum performance, which is higher than the optimistic 50-pair estimate but more realistic than 200. This means at just 10 pairs you're only hitting about 35% of the asymptotic performance, and 20 pairs gets you to roughly 55%.

For the Procrustes effect reversal threshold, the pilot suggested around 0.50, but with more noise in the median tier, I'm estimating it's closer to 0.55 with a 95% confidence interval spanning 0.45 to 0.65—architecture-dependent variation.

Now I'm looking at the decomposition approach: the transfer improvement after difficulty projection is around 1.8pp, and about 5 out of 10 languages show clean separation in the decomposition signal.

The orthogonality metrics vary significantly by resource tier—HIGH tier shows clear orthogonality at 0.03, while LOW tier is noisier at 0.07 with some values exceeding 0.10.

For probe complexity, the MLP performs better on English by 2pp over logistic regression, but it actually hurts zero-shot transfer by 3pp, so logistic regression is the better choice for transfer scenarios.

The pattern holds up on additional benchmarks but with weaker effects.

Quantization introduces negligible artifacts under 1pp AUROC, with CKA similarity between quantized and FP16 models exceeding 0.97. Extended language coverage to 52 languages reveals that very-low-resource languages mostly fail and artifact rates climb substantially. Plan 013 is already marked complete for English, so the full-scale control tasks across languages would fold into the other experiments rather than stand alone. Looking at the user's request more carefully — they want predictions only for planned experiments, not completed ones. So plan_013 is out since it's marked DONE. Let me count through the registry: plans 001 through 012 are all showing planned status, giving me 12 experiments to generate predictions for.

The control task metrics are important baseline measurements that would naturally be validated as part of the full-scale experiments in plans 001, 002, and 008. I'll embed those cross-lingual control task results within plan_001's analysis since that's where the most comprehensive data would surface. Now I need to structure this as YAML and make sure it's organized clearly, even though it'll be quite extensive.

For the CKA analysis, the partial correlations controlling for depth are the critical findings—Llama4 and Gemma4 both show significant Simpson's Paradox effects while Qwen3 trends toward significance, which gives us solid ground to claim the paradox with appropriately hedged language. The subspace angle measurements show a clear geometric pattern where high-resource languages cluster near-aligned at 10-14°, mid-tier languages rotate moderately at 20-28°, and low-resource languages show substantial misalignment at 38-48°, all correlating with resource tier and zero-shot performance. I'm confident in these findings across the board.

Now I'm structuring the experimental plan into eight distinct components—starting with the full Pareto sweeps for Qwen3 and Llama4, then the domain adaptation experiments with CaCLR, followed by difficulty decomposition, cross-lingual orthogonality analysis, probe complexity comparisons, and additional benchmark validation—making sure the YAML captures all the planned experiments without gaps.

I need to clarify what the pareto_tradeoff_prevalence metric actually measures: it's the fraction of language-architecture pairs where deeper layers show a clear negative correlation between English performance and transfer performance, indicating a genuine depth-transfer tradeoff rather than just noise. So the local tradeoff is specifically when the EN-optimal and transfer-optimal layers diverge, with measurable performance loss at the EN-optimal point. Breaking down the prevalence across architectures—Qwen3 shows the strongest effect at around 50%, Llama4 the weakest at 25%, and Gemma4 somewhere in between—which averages out to roughly 37% across all language-architecture pairs.

Now I need to work through the YAML configuration with these calibrated numbers, making sure the depth-transfer correlation metrics are internally consistent, particularly for the Qwen3 experiment where I'm tracking how many languages show positive correlation between depth and transfer performance. I'm trying to pin down exactly which 20 languages are being tested—whether that includes English or is 20 non-English languages for transfer evaluation. Looking at the plan, it seems to list 19 non-English languages plus English, so I need to clarify if the "of_20" metric counts English as trivially positive or if it's strictly the 20 transfer target languages.

For now, I'll treat it as 20 non-English languages: Qwen3 shows positive depth-transfer correlation in roughly 15 of them, with most HIGH performers having strong results across difficulty levels, while about 10 languages show clear local Pareto tradeoffs. Llama4's pattern is still coming into focus.

Llama4 has positive correlation in about 13 of the 20 languages with roughly 5 showing Pareto tradeoffs, and Gemma4 sits at 14 positive with 7 Pareto cases. Averaging across the three models gives me 14 languages with positive correlation and about 37% exhibiting Pareto tradeoffs—both metrics fall right where I'd expect them to. Now I need to write out the YAML configuration and figure out which tables and visualizations will best capture each experiment's findings.

For the Qwen3 experiment, I'll need a table showing per-language zero-shot AUROC at the EN-optimal layer along with tier information and the best zero-shot layer, plus a transfer method comparison table and Pareto scatter plots with a layer-wise heatmap. Llama4 follows a similar structure with per-language results and an architecture comparison between the two models, alongside dual-model Pareto plots. The CaCLR experiment requires tables for the β sweep, overall method comparison, ablation studies on CORAL and high-dimensional MMD, and multi-seed variance, with corresponding visualizations showing the sweep with confidence bands and a geometric explanation. For decomposition, I'm planning per-language results and random-direction controls with a difficulty-capability scatter plot, and the orthogonality analysis will have cosine similarity broken down by resource tier and language in bar chart form.

Moving forward, I'll compare linear regression versus MLP classifiers with paired scatter plots, cross-benchmark performance with parallel coordinates, and add Gemma4 as a third architecture with CKA depth profiles. Extended language coverage gets a world map visualization, quantization effects are shown through per-layer AUROC changes in a Bland-Altman plot, and the CKA analysis includes Simpson's Paradox comparisons, per-layer cross-language correlations, depth profiles, subspace angles, and corresponding heatmaps. The linear projection plan is still being finalized.

For plan_012, I'm completing the saturation curves by tier and adding a Procrustes effect reversal table with corresponding scatter plot. Now I'm verifying the transfer AUROC drop metric at final layers—checking how much transfer performance degrades when moving from the transfer-optimal layer to the EN-optimal layer across the three models, which averages around 1 percentage point.

Everything validates correctly. Now I'm writing out the full YAML configuration, which will be quite extensive. I need to organize the Qwen3 per-language table across 20 languages total, assigning them to resource tiers based on the plan_002 language set: zh, ar, hi, sw, ko, es, fr, de, ru, tr, bn, ja, pt, vi, te, id, pl, nl, uk. I'm grouping these into HIGH tier (zh, es, fr, de, pt, ja), MID tier (hi, ru, ko, tr, ar, vi, id, pl), and LOW tier (sw, bn, te, uk, nl). I'm reconsidering the language distribution — Dutch and Ukrainian probably deserve mid-tier status given their training data availability, while Turkish and Indonesian should move up as well. Let me settle on a cleaner breakdown: six high-resource languages, eight mid-tier, and five low-resource ones, which gives me a solid 19 non-English languages to work with. For the actual tables and experiments, I don't need to exhaustively list all twenty languages — a representative sample will keep things manageable while still being thorough. Now I'm ready to write out the final YAML configuration and do a final check on the CaCLR language improvement metrics.

Looking at the delta distribution, only about 8 out of 19 languages show positive improvement, which is roughly 42%, and those gains are modest at 0.2 to 1.5 percentage points. The remaining 11 languages show declines ranging from -1.2 to +0.1 percentage points with no clear pattern tied to resource tier. When I add mixed validation languages like Mandarin and Swahili, the hyperparameter selection still favors β=0.01, though it becomes fragile — using only English validation would push the selection toward β=0.003 instead. I need to be more careful about the layer probing numbers for Qwen3-235B, which has 94 layers total, so sampling every fourth layer gives me 24 probe points. I'm settling on L84 as the EN-optimal layer for Qwen3—that's the 22nd probed layer out of 24—though the exact choice matters less for the tables. For transfer-optimal, I expect a more noticeable shift away from EN-optimal compared to the pilot.

Looking at the pattern: in the smaller model, EN and transfer peaks were only 1-7 layers apart, but scaling up to 235B layers, that gap widens to 8-16 layers. This makes sense because MoE experts likely specialize more aggressively at scale.

So the tradeoff is clear: L84 gives the best English performance at 0.81 AUROC, while L72 peaks for cross-lingual transfer at 0.70 AUROC. Moving from L72 to L84 gains just 1 percentage point on English but costs 2 percentage points on transfer—a reasonable Pareto frontier. Now I need to build out the per-language breakdown to show where different languages fall on this spectrum.

Generating language performance table... Compiling the performance metrics across resource tiers...

I'm reconsidering the tier assignments since Indonesian and Ukrainian actually have moderate training data, so they shouldn't be grouped with truly low-resource languages like Swahili and Bengali. Let me reorganize into three tiers: HIGH with six languages averaging around 0.74, MID with eight languages around 0.69, and LOW with five languages around 0.61, which gives a more accurate picture of the zero-shot performance distribution.

Now I'm calculating the weighted mean across these tiers to get 0.685 at the EN-optimal layer, and cross-checking this against the expected drop from English's 0.81 baseline—the math checks out to roughly an 11 percentage point decline, which aligns with the reported range. all 19 languages pass the threshold, but the metric expects only 12-16 to pass, meaning 4-8 should fail. I need to lower some scores, particularly in the LOW tier and possibly some MID languages, to match the expected failure rate.

Looking at the pilot data, the metric counts non-English languages only, so I'm targeting around 14 passing and 5 failing out of the ~19-20 non-English languages. Telugu should definitely fail, and I'll need to identify other low-resource languages that would realistically underperform. Looking at the borderline cases more carefully—Indonesian and Ukrainian actually have decent training data, so they'd likely pass. For the truly low-resource languages that would fail below 0.58, Telugu is the clearest candidate, with Swahili and Bengali probably joining it, though the exact cutoffs depend on how much the larger model actually improves performance on these underrepresented languages. Looking at the actual scores for Llama4 Scout across those languages, I'm seeing a lot of failures below the 0.58 threshold. But that contradicts what I know about Llama-3.1-8B performing well on multilingual tasks, so scaling up to 17B shouldn't make things worse. I think I'm misinterpreting the metric—it's probably showing the range across different architectures rather than per-language breakdowns, so Qwen3 might hit 16/19 passing while Llama4 bottoms out around 12/19, with Gemma4 somewhere in between. Looking at the pilot results, scaling up to Llama 4 Scout should actually improve performance on languages like Swahili, so the failures I'm seeing might be concentrated in untested languages like Telugu and Bengali rather than the ones that already passed. If I account for that pattern, Llama 4 would land around 14-15 passing tests, which fits within the [12, 16] range if that's meant to be an average across all three model architectures. I'm settling on approximate pass rates across the three models—Qwen at 16/19, Llama at 14/19, and Gemma at 15/19—which average to 15 and stay consistent with the target range. Rather than keep refining the language-by-language breakdowns, I'll move forward with writing the YAML configuration using these calibrated numbers, and I should double-check that Llama 4 Scout's layer probing setup is correctly described as 12 probed layers from its 48 total. Now I need to nail down the CaCLR experiment specifics—it leverages cached activations from the earlier plans and tests across 2 models and 20 languages with systematic sweeps over β and α parameters, plus CORAL comparisons and high-dimensional MMD analysis across multiple seeds. The best configuration lands at α=0.3, β=0.01, achieving a mean AUROC of 0.686 on Qwen3 at layer 72, which edges out the zero-shot baseline of 0.683.

However, the improvement is marginal and statistically insignificant at p=0.38. The gains are inconsistent across languages—only 8 out of 19 show positive deltas ranging from +0.1 to +1.2 percentage points, while the remaining 11 show flat or negative performance. Looking at the β sweep holding α fixed at 0.3, the results are fairly flat across the range, with β=0.01 performing marginally better than alternatives but none reaching statistical significance.

When I examine the CORAL and high-dimensional MMD approaches, they similarly show modest improvements around +0.2 to +0.5 percentage points with p-values well above 0.05, indicating these gains are indistinguishable from noise. The only statistically significant result is the degradation at β=1.0 with a -1.2pp drop at p=0.04, suggesting that higher regularization values actually harm performance.

Looking at the multi-seed variance across different methods, the standard deviations range from ±0.002 to ±0.006, and CaCLR's claimed +0.3pp improvement falls well within this noise margin. This confirms that the apparent gains from these domain adaptation techniques are artifacts of random variation rather than genuine improvements. I'm now compiling the method comparison table to show how these approaches stack up against the baseline. I'm looking at the performance metrics across these models and need to clarify which columns represent which — they should be Qwen3 and Llama4. I'll simplify by averaging across both models for the overview table instead. Before I finalize the YAML, I need to verify the language count metric: whether it's 8 out of 20 total languages or 8 out of 19 non-English ones. Since we're working with 19 non-English languages in the plan, I'll use 8/19, which is roughly 42% and falls within the [5, 10] range. Now I'm ready to write the YAML configuration.

Writing YAML structure... Writing YAML output... The transfer-optimal layer sits around L36 with a mean zero-shot performance of 0.68, creating just a 2pp drop at the final layers—the numbers are consistent. Now I'm working through the Gemma 4 31B predictions, accounting for its 60 text layers and dense architecture. The model should peak around L52 for English performance at 0.79, with transfer-optimal performance around L44, and the zero-shot drop from English-optimal to the broader multilingual set comes to about 11pp with intermediate Pareto strength.

Looking at the architectural patterns, Qwen3's steepest CKA cliff suggests the strongest Pareto effect, while Llama4's gradual decline indicates the weakest. Gemma4's dense architecture without MoE routing produces smoother representation changes across layers, giving it intermediate Pareto strength compared to the others. For the Simpson's Paradox analysis, the pilot results show Llama-8B with a significant partial correlation of 0.41, while Qwen-7B's 0.18 doesn't reach significance, and I'm expecting similar patterns to emerge at full scale with Llama4 Scout.

At full scale, Llama4 Scout shows a significant partial rho of 0.31, Gemma4 31B reaches significance at 0.24, but Qwen3-235B remains non-significant at 0.18 because its bimodal CKA pattern—nearly flat for the first 60% of layers then dropping sharply—creates a non-linear relationship that linear partial correlation can't effectively capture. Gemma4's significance stems from its gradual CKA decline across the dense architecture, which linear methods handle more effectively.

The Simpson's paradox check confirms 2 out of 3 architectures show the expected pattern, the partial correlation coefficients cluster around 0.24 with a reasonable range, and two models reach statistical significance. Everything validates, so I'm ready to write this up. One more thing to note though—in the linear projection sensitivity analysis, saturation appears around 85 pairs, which is higher than the pilot's estimate of 50.

Looking at when the projection actually helps versus hurts, there's a clear threshold around 0.58 zero-shot AUROC. Below that, projection boosts performance by about 5 percentage points for low-tier predictions. Above it, the effect reverses and actually degrades performance slightly. But this threshold varies by architecture—Qwen3 sits higher at 0.60, Llama4 lower at 0.55, and Gemma4 right around 0.58—which is itself an important finding about how model families respond differently to this intervention.

The sample efficiency curves also check out: high-tier predictions saturate quickly at around 30 pairs since they involve minimal rotation, mid-tier needs about 60, and low-tier requires over 100 because of the larger subspace changes and noisier parallel data. Overall, hitting 95% of the benefit takes roughly 85 pairs, which fits nicely within the 50-120 range I was seeing.

Writing the YAML structure now...

Now I'm mapping out the narrative for the median tier: CaCLR fails with a clear geometric explanation, Pareto effects replicate but vary by architecture, Simpson's Paradox shows up in two of the three cases, the decomposition stays qualitative rather than quantitative, and linear projection with those 85 pairs becomes the practical workaround. The Procrustes reversal threshold shifts across architectures around 0.55-0.60, there's roughly a 22% cross-lingual artifact rate, and the paper reframes itself as an empirical study with a systematic negative result, practical solution, and geometric insights—still a solid contribution.

For the title, I'm considering either the longer version emphasizing architecture-dependent effects and distributional matching failure, or the tighter question-based framing about when cross-lingual calibration actually transfers. I'll go with the more concise one.

Now I need to be precise about the Qwen3 layer sampling—94 total layers, probed every 4th layer gives me 24 checkpoints, with the EN-optimal probe landing at layer 84, which is about 89% depth into the model.

For transfer, the sweet spot appears to be around layers 68-72, but I'm reconsidering whether the deepest layers are actually best for English performance. The pilot showed Qwen-7B peaked at layer 27 (97% depth), which would suggest layer 91 for Qwen3, but we only probe at 88 and 92. The MoE architecture might cause performance to plateau or even decline at the very final layer due to over-specialization, so layer 88 at 94% depth seems like the safer choice for EN-optimal rather than pushing all the way to 92.

Looking at the actual numbers, layer 84 gives the cleanest peak at 0.81, with a slight dip to 0.808 at layer 88 and 0.80 at layer 92. This pattern suggests the sweet spot is a few layers before the end where expert routing hasn't become too specialized for individual query types. Though this contradicts the pilot where layer 27 was final and still optimal, so maybe the final probed layer L92 is actually the right call here.

Let me settle on L88 as the English-optimal layer—that's 94% depth, comparable to the pilot's 97%. For transfer, L68 or L72 at 72% depth seems better. The gap between them is about 20 layers, and while English performance only drops 1 percentage point from 0.81 to 0.80, zero-shot performance across the 19 languages improves from 0.68 to 0.705 at the shallower layer. Looking at the zero-shot performance at L84 versus L68, I'm seeing a 2.5pp drop when moving to the transfer-optimal layer, which aligns with the Pareto tradeoff metric. Let me settle on L84 as the final choice—I've been oscillating too much between options. The mean zero-shot at L84 is 0.685, dropping to 0.71 at L68, while the English AUROC gain is only 1pp, so I need to recalculate what the actual performance delta looks like across languages. I'm refining the estimates by model—Qwen3 shows a 9pp drop with a mean ZS of 0.72, while Llama4 and Gemma4 each drop 11pp with means of 0.66 and 0.68 respectively, bringing the average drop across all three architectures to 10pp.

Now I'm checking the consistency: Qwen3's best-per-language mean of 0.72 is indeed higher than its transfer-optimal layer performance at 0.715, which makes sense since individual languages peak at different layers. For the zero-shot pass rates, I'm looking at which Qwen3 best-per-language values fall below 0.58—the high-resource languages all exceed 0.70, so they pass, while the mid-resource group ranges from 0.66 to 0.74.

For the low-resource languages, I'm adjusting the values to get the right balance: Telugu at 0.54 and Bengali at 0.57 fail the threshold, while Swahili, Indonesian, and Ukrainian pass. This gives me 17 out of 19 languages passing overall, but I need to verify this aligns with the mean of 0.72 across all groups.

Let me recalculate: the high-resource group averages 0.76, mid-resource averages 0.71, and low-resource averages around 0.59, which totals to about 0.695—still short of 0.72. I'm bumping up the mid and low groups slightly, pushing the low-resource mean to 0.612 and the overall mean to 0.708. Getting closer, so I'll increase the high-resource group to 0.78 to hit that target more precisely.

That gets me to 0.717, which rounds to 0.72. Now I'm looking at the pass rates: with Turkish failing in the mid tier and Telugu and Bengali failing in the low tier, that's three failures total, leaving 16 out of 19 languages passing—right in the acceptable range. I'm finishing the HIGH category with the remaining languages, then calculating the grand mean across all three tiers. The overall drop from English is about 11 percentage points, which aligns well with my target for Qwen3, and the consistency across different model architectures (Qwen3, Llama4, and Gemma4 all around 11-12pp) validates this approach. I'm also tracking the zero-shot pass rate, which shows 16 out of 19 languages passing for Qwen3.

For Llama4 Scout, I'm aiming for a slightly larger drop of 12 percentage points given it's a smaller model, which gives me 14 out of 19 languages passing. I'm being careful about which languages fail—making sure Hindi passes since it performed reasonably well in the baseline, and instead having Telugu, Bengali, Swahili, Turkish, and Ukrainian fall just below the threshold.

For Gemma4, with an 11 percentage point drop, I get 15 out of 19 passing with Telugu, Bengali, Swahili, and Turkish failing. The cross-architecture average works out to exactly 15 languages passing, which sits nicely in my target range. Now I'm ready to write out the YAML with all these calibrated numbers, and I'll also include the ablation results from the CaCLR experiment showing the CORAL variants.

Looking at the high-dimensional MMD and CORAL comparisons, the best performer is MMD at d=50 with a 0.5 percentage point gain, followed closely by CORAL at d=50 with 0.6 percentage points, but neither reaches statistical significance. Even pushing to higher dimensions only adds another 0.2 to 0.4 percentage points of improvement—not enough to cross the significance threshold. This actually strengthens the negative finding: distributional matching doesn't work whether I'm using one dimension or fifty, and it holds across both MMD and CORAL loss functions.

The subspace angle analysis reveals why—these methods reduce the marginal distance between distributions but fail to correct the angular misalignment between subspaces. Only direct rotation methods like Procrustes or linear projection actually fix that problem.

Now I'm reconsidering the language improvement count. If I define "improved" as any positive change, then with 19 languages and a mean delta of +0.3 percentage points, I'd expect roughly half to show gains just from noise, so the actual count of improved languages should reflect that baseline rather than the 8 out of 19 I've been using.

But the metric range of 5-10 suggests a stricter threshold—probably something like a 0.5 percentage point improvement or statistical significance per language. Working through the math with a standard deviation around 1 percentage point, a 0.5 percentage point threshold would give me roughly 8 languages showing improvement, which fits nicely within that 5-10 range.

Now I'm organizing the key metrics I need to include in the output: Qwen3 with an English AUROC of 0.81 and 16 out of 19 zero-shot passes, Llama4 at 0.77 with 14 passes, and Gemma4 at 0.79 with 15 passes, along with their respective Pareto frontier distributions across languages.

For the analysis results, I'm noting that CaCLR shows a modest +0.3pp mean improvement with 8 languages crossing the 0.5pp threshold, the linear projection approach saturates around 85 pairs with a reversal point near 0.58, decomposition yields +1.8pp with clean separation in half the cases, and the control experiments show a 22% artifact rate with low selectivity at 0.20.

Let me finalize the calculation for Qwen3's mean zero-shot performance across languages to ensure consistency before I write out the full YAML output. Looking at the impact of optimizing individual language layers, even if Turkish improves from 0.57 to 0.60, the overall mean barely budges to 0.696. So the zero-shot performance drop across these models is consistently around 11 percentage points—Qwen3 and Llama4 both show this pattern, with English performance in the high 70s to low 80s dropping to means around 0.66-0.70 across languages.

Now I'm working through the pass counts for zero-shot performance. For Qwen3, if I account for Turkish potentially reaching 0.60 at its best layer rather than staying at 0.57, that would push the passing languages from 16 to 17 out of 19, with only Telugu and Bengali falling below the threshold. Though 17 is above the expected range of 12-16, that's because this is a single architecture rather than a cross-architecture mean.

Looking at the other models, Llama4 gets 14 passing languages and Gemma4 gets 15, which when averaged gives around 15.3 across the three architectures. The range [12, 16] likely represents the spread across individual architectures—with Qwen3 at the high end around 16 and Llama4 at the low end around 12.

For Qwen3, I'm marking three languages as failing (Turkish and Bengali both below 0.58, plus Ukrainian which has limited Cyrillic coverage), leaving 16 passing. For Llama4, getting down to 12 passing means 7 failures, which seems steep for a 109B parameter model like Llama-3.1, so I should reconsider this distribution. I'm settling on Llama4 at 12/19 to honor the stated range, which means accepting 7 failing languages including some unexpected ones like Hindi that passed in the pilot—this suggests the full test set is genuinely harder than the initial sample. So 13 passes for Llama4 gets me close to the target range. Looking at the breakdown, the passing languages cluster around 0.60-0.74 with a mean near 0.67, while the six failures sit lower at 0.50-0.56 averaging around 0.53. Let me calculate the overall mean to see if this configuration works. I'm settling on 0.77 for English with a mean zero-shot drop of around 11 percentage points across the 13 passing languages, while the 6 failing languages average around 0.55. Now I'm fine-tuning the individual language scores to match these targets, assigning specific performance values for each language in both groups. I've settled on these performance drops—they're all within the acceptable range and the mean of about 11 percentage points works well. Now I'm moving forward with writing the YAML output. I'll structure it similarly to the previous report, using representative languages in the tables for readability while noting where I'm showing a subset, and I'll keep the narrative in Chinese with English column headers to match the earlier format. Aiming for around 1000-1200 words total.

Writing YAML structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c9d87c4-9ae8-46fd-8885-d47139b0ea2b",
  "isSidechain": false,
  "requestId": "req_011CbFkpxAEZSG9xgfeNppuu",
  "type": "assistant",
  "uuid": "e99f2cb5-0d73-4eb4-92a9-e14aa78f2f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBHLyq65fLKKxBk3Wu6tZ6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 80130,
      "output_tokens": 25186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 25186,
          "cache_read_input_tokens": 80130,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 32 · 2026-05-21T13:11:02.527Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive context. Let me produce the detailed median-tier imagined experiments YAML. I need to cover all planned experiments (not DONE ones). Let me be thorough and precise, grounding every prediction in the median tier definition and providing clear rationales.

Let me enumerate the planned experiments again:
1. plan_001 - Qwen3-235B Full Pareto
2. plan_002 - Llama 4 Scout Full Pareto
3. plan_003 - CaCLR
4. plan_004 - Difficulty decomposition


5. plan_005 - Cross-lingual orthogonality
6. plan_006 - Probe complexity (LR vs MLP)
7. plan_007 - Additional benchmarks (Belebele + MMLU-ProX)
8. plan_008 - Gemma 4 31B Dense
9. plan_009 - Extended language coverage (50+)
10. plan_010 - Quantization validation
11. plan_011 - CKA analysis + Simpson's Paradox
12. plan_012 - Linear projection sensitivity

Now I'm calibrating each prediction carefully, starting with the mean EN AUROC across architectures.

For the three main models, I'm estimating Qwen3-235B at around 0.81 given its size and MoE design, Llama 4 Scout closer to 0.77 with its smaller active parameters, and Gemma 4 31B at 0.79 as a dense model, which averages to about 0.79. On zero-shot transfer, I'm expecting roughly 14 out of 20 language-architecture pairs to pass, and the AUROC drop compared to English should be around 11 percentage points. For Pareto prevalence, I'm estimating about 38% of language-architecture pairs will show a clear performance tradeoff.

Now I'm looking at the depth-transfer drop at final layers, which appears to be around 2 percentage points, and examining the CKA partial correlations which vary by architecture between 0.15 and 0.35. Simpson's paradox seems to hold for 1 or 2 of the 3 cases tested. The CaCLR approach shows minimal impact at around 0.3 percentage points, improving roughly 7 out of 20 languages. Linear projection on low-resource languages shows about a 5 percentage point improvement, reaching saturation around 80 language-architecture pairs, while the decomposition method yields roughly 2 percentage points of improvement with fairly clean separation across most cases.

Control selectivity in deeper layers sits around 0.20, artifact rates hover near 22%, and about 14 out of 20 languages show positive Spearman correlations. Now I'm drafting the comprehensive YAML configuration to capture all these findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e99f2cb5-0d73-4eb4-92a9-e14aa78f2f1c",
  "isSidechain": false,
  "requestId": "req_011CbFkpxAEZSG9xgfeNppuu",
  "type": "assistant",
  "uuid": "69fab88e-f618-431b-b456-6b52aa18f5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrVonFh2FmTyPXs48b2Xuq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 80130,
      "output_tokens": 25186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 25186,
          "cache_read_input_tokens": 80130,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 33 · 2026-05-21T13:18:30.310Z_

Now I have all the context needed. Let me produce the detailed median-tier predictions.

```yaml
tier: median
narrative_guidance: >
  Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise.
  CaCLR consistency loss is inert across the full β sweep; paper pivots to planned negative-result narrative with
  geometric explanation (MMD matches marginals but not low-dimensional directional subspace). Simpson's Paradox
  confirmed in 1-2 of 3 architectures (Llama 4 Scout significant, Qwen3-235B trending, Gemma 4 borderline).
  Claim 2 (decomposition) downgraded from quantitative prescriptive to qualitative descriptive.
  Headline pivots to: "Cross-lingual probe transfer reveals architecture-dependent depth effects; distributional
  matching fails but linear projection with ~80 parallel pairs is the practical label-free solution."
  Paper holds for EACL: field-level viability test + negative result + practical solution + geometric insights.
  Compress Claim 2 to subsection to make space for stronger negative-result analysis and CKA geometric section.

imagined_experiments:
  # ============================================================
  # plan_001 — Qwen3-235B-A22B Full Pareto Frontier (MoE, INT4)
  # ============================================================
  - name: "Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT4)"
    plan_id: plan_001
    description: >
      94-layer MoE 模型，24 probed layers (每4层取1), 20 languages × 5 transfer conditions。
      MoE routing 在深层创建更强的语言特异化，产生比 7B pilot 更清晰但仍非普遍的 Pareto tradeoff。
    expected_results:
      en_best_auroc: 0.81
      en_best_layer: L80
      en_best_layer_depth_pct: 0.851
      en_auroc_range: [0.59, 0.81]
      en_best_ece_raw: 0.178
      layer_depth_delta_pp: 22.0
      transfer_optimal_layer_mean: L68
      transfer_optimal_depth_pct: 0.723
      en_transfer_layer_gap_auroc_pp: 2.5
      zs_pass_count_of_20: 15
      zs_pass_rate: 0.75
      zs_mean_auroc_at_en_optimal_layer: 0.668
      zs_mean_auroc_at_transfer_optimal_layer: 0.688
      mean_zs_auroc_drop_vs_en_pp: 12.2
      pareto_langs_with_negative_depth_transfer_rho: 14
      pareto_langs_significant_negative_rho: 9
      pareto_spearman_rho_median: -0.38
      pareto_spearman_rho_range: [-0.65, 0.20]
      pareto_depth_transfer_drop_final_layers_pp: 2.3
      best_zs_auroc_by_tier:
        HIGH_mean: 0.728  # zh/es/fr/de/pt/ja
        MID_mean: 0.678   # ar/ru/ko/hi/vi/tr
        LOW_mean: 0.582   # sw/bn/te/id/nl/uk or yo/am etc
      best_zs_auroc_per_lang:
        zh: 0.738
        es: 0.745
        fr: 0.740
        de: 0.725
        pt: 0.732
        ja: 0.710
        ar: 0.695
        ru: 0.705
        ko: 0.688
        hi: 0.670
        vi: 0.680
        tr: 0.660
        sw: 0.598
        bn: 0.612
        te: 0.572
        id: 0.690
        pl: 0.698
        nl: 0.720
        uk: 0.695
        yo: 0.535
      mean_shift_delta_auroc: 0.0
      linear_proj_200_mean_auroc: 0.698
      few_shot_25_mean_auroc: 0.685
      few_shot_100_mean_auroc: 0.718
      spearman_depth_vs_transfer_positive_langs: 14
    result_rationale: >
      Qwen3-235B 的 22B active MoE 参数从 7B pilot (EN AUROC 0.754) 提升到 ~0.81，
      符合 correctness signal 随模型规模 sublinear scaling 的预期——22B/7B ≈ 3x 参数但 AUROC
      提升仅 ~6pp，因为 correctness direction 的 linear accessibility 在 7B 时已接近 ceiling。
      MoE routing 在深层（L64+）为不同语言激活不同 expert subset，加速 representation 语言特异化。
      CKA 在 L64-L80 急剧下降（slope ~-0.022/layer），创造比 7B pilot 更清晰的 Pareto cliff。
      但 "更清晰" 不等于 "普遍"：仍有 6/20 语言（主要 ar/ko + 部分低资源）不显示负 rho 或方向相反，
      因为 (1) ar/ko 在 Qwen 训练数据中比例足够高，MoE routing 未完全将其与 EN 分离；
      (2) 极低资源语言（yo/am）全深度 AUROC 都低，depth variation 太小无法检测 tradeoff。
      15/20 languages ZS AUROC > 0.58 — 新增 10 语言中 5 个通过（es/fr/de 等 HIGH 语言全通过），
      但 yo 可能低于阈值。Mean-shift 仍然恒等于 0（数学不变性不随模型规模变化）。
      Transfer-optimal layer 在 L68（72% depth）而非 EN-optimal L80，gap ~2.5pp，
      比 7B pilot 的 L24 vs L27 (~1.5pp) 更大但非剧烈——MoE 架构放大了 gap 但非无限放大。
    tables:
      - name: "Table 1: Per-Language ZS AUROC and Pareto Statistics (Qwen3-235B, EN-optimal L80)"
        data: |
          | Tier | Language | ZS AUROC | Best ZS Layer | Spearman ρ | p-value | Pattern          |
          |------|----------|----------|---------------|------------|---------|------------------|
          | HIGH | zh       | 0.738    | L68           | -0.48      | 0.018   | Clear tradeoff   |
          | HIGH | es       | 0.745    | L72           | -0.44      | 0.031   | Clear tradeoff   |
          | HIGH | fr       | 0.740    | L72           | -0.42      | 0.041   | Clear tradeoff   |
          | HIGH | de       | 0.725    | L64           | -0.51      | 0.011   | Clear tradeoff   |
          | HIGH | pt       | 0.732    | L68           | -0.39      | 0.059   | Trending         |
          | HIGH | ja       | 0.710    | L64           | -0.55      | 0.005   | Clear tradeoff   |
          | MID  | ar       | 0.695    | L72           | -0.22      | 0.301   | Weak/absent      |
          | MID  | ru       | 0.705    | L68           | -0.46      | 0.024   | Clear tradeoff   |
          | MID  | ko       | 0.688    | L68           | +0.08      | 0.711   | No tradeoff      |
          | MID  | hi       | 0.670    | L60           | -0.40      | 0.052   | Trending         |
          | MID  | vi       | 0.680    | L64           | -0.38      | 0.068   | Trending         |
          | MID  | tr       | 0.660    | L56           | -0.35      | 0.093   | Trending         |
          | MID  | id       | 0.690    | L68           | -0.43      | 0.036   | Clear tradeoff   |
          | LOW  | sw       | 0.598    | L52           | -0.28      | 0.184   | Weak             |
          | LOW  | bn       | 0.612    | L56           | -0.33      | 0.115   | Weak             |
          | LOW  | te       | 0.572    | L48           | -0.19      | 0.374   | Weak             |
          | LOW  | pl       | 0.698    | L68           | -0.45      | 0.027   | Clear tradeoff   |
          | LOW  | nl       | 0.720    | L68           | -0.47      | 0.021   | Clear tradeoff   |
          | LOW  | uk       | 0.695    | L64           | -0.41      | 0.046   | Clear tradeoff   |
          | LOW  | yo       | 0.535    | L44           | +0.12      | 0.578   | No tradeoff      |
      - name: "Table 2: Transfer Method Comparison (mean across 20 languages, EN-optimal layer)"
        data: |
          | Method              | Mean AUROC | Δ vs ZS (pp) | Paired perm p | Req. labels | Req. parallel |
          |---------------------|------------|--------------|---------------|-------------|---------------|
          | Zero-shot           | 0.668      | —            | —             | 0           | 0             |
          | Mean-shift          | 0.668      | 0.0          | n/a           | 0           | N (mean only) |
          | CaCLR (best β=0.01) | 0.671      | +0.3         | p=0.38        | 0           | ~10K parallel |
          | Linear proj (50)    | 0.684      | +1.6         | p=0.012       | 0           | 50 pairs      |
          | Linear proj (200)   | 0.698      | +3.0         | p<0.001       | 0           | 200 pairs     |
          | Few-shot 25         | 0.685      | +1.7         | p=0.008       | 25          | 0             |
          | Few-shot 100        | 0.718      | +5.0         | p<0.001       | 100         | 0             |
    figures_description:
      - >
        Pareto scatter plot (Figure 2): 4×5 grid (20 languages), x=EN AUROC, y=ZS AUROC,
        each point is a probed layer (24 dots), color encodes normalized depth (light→deep).
        HIGH-resource subplots show clear right-downward bend at deepest layers;
        LOW-resource subplots show compressed point clouds in lower-left region with no clear frontier.
        ar/ko subplots show monotonically ascending trends (no tradeoff).
      - >
        Layer-wise AUROC heatmap (Figure 3): x=20 languages (sorted by tier), y=24 probed layers (by depth),
        color=ZS AUROC. EN column alongside showing monotonic increase. Cool colors (low AUROC) concentrated
        in bottom-right (shallow × low-resource) and top-right corner (deepest × low-resource).
    analysis: >
      Qwen3-235B 的 MoE 架构产生了 pilot 预期的清晰 Pareto，但非所有语言均参与：
      9/20 语言 Spearman ρ 显著为负 (p<0.05)，另 5 个 trending (p<0.10)，6 个不显著或方向相反。
      Pareto 强度与 resource tier 正相关但非完美（pl/nl/uk 虽在 LOW tier 但因与 EN 词汇重叠高，表现接近 HIGH）。
      MoE routing 加速了 L64+ 的语言特异化，但效果分布在 4-8 层的范围内，不是单点 cliff。
      ar/ko 不 show tradeoff 的原因需在 CKA 分析 (plan_011) 中进一步解释——
      可能是这两种语言在 Qwen3 训练数据中占比足够高，expert sharing 保持了 EN-target alignment。

  # ============================================================
  # plan_002 — Llama 4 Scout Full Pareto Frontier (MoE, W4A16)
  # ============================================================
  - name: "Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, W4A16)"
    plan_id: plan_002
    description: >
      48-layer 17B-16E MoE，12 probed layers (每4层取1+final), 20 languages × 5 transfer conditions。
      Llama 架构族在 pilot (3.1-8B) 中显示弱 Pareto，full-scale MoE 预期延续但 Pareto 稍增。
    expected_results:
      en_best_auroc: 0.77
      en_best_layer: L44
      en_best_layer_depth_pct: 0.917
      en_auroc_range: [0.61, 0.77]
      en_best_ece_raw: 0.192
      layer_depth_delta_pp: 16.0
      transfer_optimal_layer_mean: L36
      transfer_optimal_depth_pct: 0.75
      en_transfer_layer_gap_auroc_pp: 1.5
      zs_pass_count_of_20: 14
      zs_pass_rate: 0.70
      zs_mean_auroc_at_en_optimal_layer: 0.648
      zs_mean_auroc_at_transfer_optimal_layer: 0.660
      mean_zs_auroc_drop_vs_en_pp: 11.0
      pareto_langs_with_negative_depth_transfer_rho: 11
      pareto_langs_significant_negative_rho: 5
      pareto_spearman_rho_median: -0.25
      pareto_spearman_rho_range: [-0.52, 0.38]
      pareto_depth_transfer_drop_final_layers_pp: 1.2
      best_zs_auroc_by_tier:
        HIGH_mean: 0.708
        MID_mean: 0.658
        LOW_mean: 0.562
      best_zs_auroc_per_lang:
        zh: 0.718
        es: 0.725
        fr: 0.720
        de: 0.705
        pt: 0.712
        ja: 0.690
        ar: 0.672
        ru: 0.685
        ko: 0.680
        hi: 0.645
        vi: 0.658
        tr: 0.635
        sw: 0.578
        bn: 0.590
        te: 0.555
        id: 0.672
        pl: 0.678
        nl: 0.700
        uk: 0.670
        yo: 0.520
      mean_shift_delta_auroc: 0.0
      linear_proj_200_mean_auroc: 0.678
      few_shot_100_mean_auroc: 0.700
      spearman_depth_vs_transfer_positive_langs: 13
    result_rationale: >
      Llama 4 Scout (17B active) 从 pilot Llama-3.1-8B (EN 0.728) 提升到 ~0.77，
      提升幅度低于 Qwen3 的 scaling，因为 Llama 4 的 16-expert MoE 在中层已开始 expert specialization，
      correctness signal 在 L20-L36 plateau 而非持续爬升到最深层。
      Pilot 中 Llama 的弱 Pareto 模式延续：仅 5/20 语言显著负 rho (p<0.05)，
      另 6 个 trending，9 个不显著或方向相反。ar/ko 延续 pilot 中的正向深度效应
      （ZS AUROC 随深度单调增加，无 tradeoff），扩展到 vi 也呈此模式。
      关键架构差异在 CKA depth gradient：Llama CKA decline 从 ~50% depth 开始渐进下降
      (slope ~-0.013/layer)，而非 Qwen3 的 ~68% depth 后骤降 (slope ~-0.022/layer)。
      渐进 CKA decline → tradeoff 分散在更宽的层范围 → per-language Spearman ρ magnitude 更小。
      EN-optimal (L44) vs transfer-optimal (L36) gap 仅 ~1.5pp vs Qwen3 的 ~2.5pp。
      12 probed layers 的较少层采样（vs Qwen3 的 24 层）也降低了 Spearman 检验功效 (n=12 vs n=24)。
    tables:
      - name: "Table 3: Architecture Comparison — Pareto Strength"
        data: |
          | Metric                         | Qwen3-235B (MoE) | Llama4 Scout (MoE) |
          |--------------------------------|-------------------|--------------------|
          | EN best AUROC                  | 0.81              | 0.77               |
          | Mean ZS AUROC (EN-opt layer)   | 0.668             | 0.648              |
          | Pareto significant langs (/20) | 9                 | 5                  |
          | Median per-lang Pareto ρ       | -0.38             | -0.25              |
          | CKA cliff onset (% depth)      | ~68%              | ~50%               |
          | CKA depth gradient (cliff)     | -0.022/layer      | -0.013/layer       |
          | EN-opt vs Transfer-opt gap (pp)| 2.5               | 1.5                |
      - name: "Table 4: Divergent Languages Between Architectures"
        data: |
          | Language | Qwen3 ρ | Qwen3 p | Llama4 ρ | Llama4 p | Pattern     |
          |----------|---------|---------|----------|----------|-------------|
          | ar       | -0.22   | 0.301   | +0.18    | 0.575    | Divergent   |
          | ko       | +0.08   | 0.711   | +0.32    | 0.311    | Both pos    |
          | vi       | -0.38   | 0.068   | +0.15    | 0.641    | Divergent   |
          | ja       | -0.55   | 0.005   | -0.42    | 0.175    | Both neg    |
          | hi       | -0.40   | 0.052   | -0.48    | 0.115    | Both neg    |
    figures_description:
      - >
        Dual-model Pareto comparison (Figure 4): left=Qwen3-235B, right=Llama4 Scout,
        3 rows (HIGH/MID/LOW tier). Each subplot overlays per-language Pareto frontiers (different colors).
        Qwen3 panels show sharper frontier bends; Llama4 panels show shallower, more diffuse frontiers.
        ar/ko highlighted with dashed lines showing positive slope (no tradeoff) in both models.
    analysis: >
      两个 MoE 架构的 Pareto 差异证实架构依赖性——但差异根源是 CKA gradient shape，
      不是 MoE vs dense (需 Gemma 4 dense 对照验证)。Llama4 的渐进 CKA decline 意味着
      cross-lingual alignment 是渐变退化而非突变，实践意义是：layer selection 对 Llama4 不那么关键，
      任何 50-90% depth 的层都是 reasonable choice，而 Qwen3 有明确的 optimal window (60-75% depth)。
      ar/ko/vi 在 Llama4 上的正向深度效应扩大了 pilot 发现——这些语言在 Llama 训练数据中
      representation 可能与 EN 共享更多 expert（tokenizer 和 training distribution 的差异是
      observational confound，n=2 architectures 不做因果归因）。

  # ============================================================
  # plan_003 — CaCLR Implementation and Negative Result
  # ============================================================
  - name: "CaCLR Implementation and Systematic Negative Result"
    plan_id: plan_003
    description: >
      CaCLR (BCE + α·SB-ECE + β·MMD) 完整实现。β sweep 3 OOM (0.001-1.0)，
      component ablation, CORAL comparison, high-dim MMD (PCA d=50/100), multi-seed, mixed β criterion。
      Median tier: consistency loss inert → negative result + geometric explanation。
    expected_results:
      caclr_mean_delta_auroc_vs_zs_pp: 0.3
      caclr_delta_auroc_range_pp: [-0.8, 1.2]
      caclr_langs_improved_of_20: 8
      caclr_langs_degraded_of_20: 5
      caclr_langs_unchanged_of_20: 7
      caclr_best_beta: 0.01
      caclr_best_alpha: 0.3
      beta_sweep:
        beta_0.001:
          mean_delta_auroc_pp: 0.1
          paired_perm_p: 0.72
          cohen_d: 0.02
        beta_0.01:
          mean_delta_auroc_pp: 0.3
          paired_perm_p: 0.38
          cohen_d: 0.06
        beta_0.1:
          mean_delta_auroc_pp: -0.1
          paired_perm_p: 0.65
          cohen_d: 0.03
        beta_1.0:
          mean_delta_auroc_pp: -0.7
          paired_perm_p: 0.15
          cohen_d: 0.15
      alpha_sweep:
        alpha_0.01: { mean_delta_ece_pp: -0.2, mean_delta_auroc_pp: 0.0 }
        alpha_0.1: { mean_delta_ece_pp: -0.6, mean_delta_auroc_pp: -0.1 }
        alpha_1.0: { mean_delta_ece_pp: -1.8, mean_delta_auroc_pp: -0.5 }
        alpha_10.0: { mean_delta_ece_pp: -2.3, mean_delta_auroc_pp: -1.4 }
      component_ablation:
        bce_only: { auroc: 0.668, ece: 0.190 }
        bce_sbece: { auroc: 0.665, ece: 0.175 }
        bce_mmd: { auroc: 0.670, ece: 0.188 }
        bce_sbece_mmd: { auroc: 0.669, ece: 0.174 }
      coral_comparison:
        coral_mean_delta_auroc_pp: 0.4
        coral_p_vs_zs: 0.32
        coral_conclusion: "also inert — distributional matching failure is general, not MMD-specific"
      high_dim_mmd:
        pca_d50_mean_delta_auroc_pp: 0.5
        pca_d50_p_vs_zs: 0.28
        pca_d100_mean_delta_auroc_pp: 0.2
        pca_d100_p_vs_zs: 0.51
        conclusion: "high-dim MMD also inert — broadens distributional matching failure claim"
      multi_seed_std:
        caclr_auroc_std: 0.003
        few_shot_25_auroc_std: 0.005
        few_shot_100_auroc_std: 0.004
        procrustes_auroc_std: 0.002
      mixed_beta_criterion:
        en_only_best_beta: 0.01
        en_zh_sw_best_beta: 0.01
        conclusion: "mixed criterion selects same β — no systematic bias"
      method_comparison_mean_20lang:
        zero_shot: 0.668
        mean_shift: 0.668
        caclr_best: 0.671
        coral_best: 0.672
        high_dim_mmd_best: 0.673
        linear_proj_50: 0.684
        linear_proj_200: 0.698
        few_shot_25: 0.685
        few_shot_100: 0.718
      implementation_spec:
        mmd_kernel: "Gaussian RBF, bandwidth via median heuristic (recomputed per batch)"
        optimizer: "Adam, lr=5e-4, cosine decay to 1e-5"
        epochs: 50
        early_stopping: "patience=10 on validation BCE loss"
        initialization: "from standard LR solution (warm-start)"
        batch_size: 256
        mmd_items: "same as BCE (probe_train split, 70% of GlobalMMLU test)"
        parallel_set_size_range: [8500, 12200]
        seeds: [42, 137, 256]
    result_rationale: >
      CaCLR 的 MMD consistency loss 在 1-D probe logit 空间操作，这是根本的 architectural mismatch。
      Correctness information 占据高维 activation 空间的 1-3 维子空间；MMD 只能匹配 logit 的
      marginal distribution (均值/方差)，无法检测或纠正 correctness direction 的旋转。
      β=0.001-0.01 时 consistency loss 太弱，等效于 pure BCE；β=0.1-1.0 时 loss 开始干扰
      BCE 训练——强制匹配 marginal 反而扰动了 EN probe 已学到的 correctness direction，AUROC 下降。
      8/20 语言 show 微小正 delta (0.1-1.2pp) 但无一统计显著——这是 noise 而非 signal。
      CORAL (second-order alignment) 和 high-dim MMD (PCA d=50/100) 也无效——
      distributional matching 的失败不限于 MMD kernel 或操作维度，而是因为
      Zhao et al. (2019) 的理论预测成立：P(correct|activation) 的 conditional structure
      在不同语言间不同（language-specific capability component），marginal matching 无法修复
      conditional mismatch。CKA subspace analysis 将提供几何证据：CaCLR 成功减小了
      marginal distance 但 subspace angle 几乎不变（见 plan_011 交叉分析）。
      与此对照，linear projection 直接学习旋转矩阵，绕过 distributional matching 的局限。
      Multi-seed 结果稳定 (std ~0.002-0.005)，排除 single-seed artifact 的可能。
    tables:
      - name: "Table 5: β Sweep Results (Qwen3-235B, L68, mean 20 languages, 3 seeds)"
        data: |
          | β     | Mean AUROC | Δ vs ZS (pp) | 95% Boot CI (pp)  | Cohen's d | Interpretation      |
          |-------|------------|--------------|-------------------|-----------|---------------------|
          | 0     | 0.668      | —            | —                 | —         | ZS baseline         |
          | 0.001 | 0.669      | +0.1         | [-0.5, +0.7]      | 0.02      | Negligible          |
          | 0.01  | 0.671      | +0.3         | [-0.4, +1.0]      | 0.06      | Negligible          |
          | 0.1   | 0.667      | -0.1         | [-0.8, +0.6]      | 0.03      | Negligible          |
          | 1.0   | 0.661      | -0.7         | [-1.4, +0.0]      | 0.15      | Slight degradation  |
      - name: "Table 6: Distributional Matching Ablation (all methods, mean 20 langs)"
        data: |
          | Method               | Operates on | Mean AUROC | Δ vs ZS | p-value | Conclusion |
          |----------------------|-------------|------------|---------|---------|------------|
          | MMD (1-D logit)      | probe logit | 0.671      | +0.3pp  | 0.38    | Inert      |
          | MMD (PCA d=50)       | activations | 0.673      | +0.5pp  | 0.28    | Inert      |
          | MMD (PCA d=100)      | activations | 0.670      | +0.2pp  | 0.51    | Inert      |
          | CORAL (1-D logit)    | probe logit | 0.672      | +0.4pp  | 0.32    | Inert      |
          | CORAL (PCA d=50)     | activations | 0.671      | +0.3pp  | 0.40    | Inert      |
          | Linear projection    | activations | 0.698      | +3.0pp  | <0.001  | Effective  |
          | Few-shot 100         | labels      | 0.718      | +5.0pp  | <0.001  | Effective  |
      - name: "Table 7: CKA Subspace Angle — Why Distributional Matching Fails"
        data: |
          | Language Tier | Mean subspace angle (EN→target) | MMD dist before | MMD dist after CaCLR | Angle after CaCLR | Interpretation                |
          |--------------|----------------------------------|-----------------|----------------------|--------------------|-------------------------------|
          | HIGH         | 11°                              | 0.018           | 0.008                | 10.5°              | MMD reduces, angle unchanged  |
          | MID          | 23°                              | 0.042           | 0.018                | 22°                | MMD reduces, angle unchanged  |
          | LOW          | 44°                              | 0.105           | 0.048                | 42°                | MMD reduces, angle unchanged  |
    figures_description:
      - >
        β sweep plot (Figure 5): x=β (log scale), y=Δ AUROC vs zero-shot (pp). Three lines
        (HIGH/MID/LOW tier), shaded bootstrap 95% CI. All lines oscillate around y=0
        within noise band; β=1.0 dips below zero. Horizontal dashed lines mark linear projection
        (+3.0pp) and few-shot 100 (+5.0pp) for contrast. Message: no β value produces meaningful improvement.
      - >
        Geometric explanation diagram (Figure 6): Left panel shows 1-D logit space with
        overlapping EN/target distributions (MMD small) but correctness direction arrows pointing
        different ways in 3D activation space projection. Right panel shows linear projection
        rotating the target subspace to align with EN. Caption: "MMD matches marginal
        distributions but cannot align the low-dimensional directional structure that carries
        correctness information."
    analysis: >
      CaCLR negative result 贡献在三个层面：(1) Systematic β sweep (3 OOM × 2 architectures × 20 langs)
      关闭了 MMD-based consistency loss 路径；(2) CORAL + high-dim MMD ablation 扩展结论到
      "distributional matching in general fails for correctness probe transfer"——不是 MMD 的问题，
      是 marginal-conditional mismatch 的本质问题；(3) CKA subspace angle analysis 提供几何解释：
      CaCLR 成功减小了 marginal distance 但 correctness subspace angle 几乎不变。
      Constructive framing: CaCLR 是 "the natural baseline that tests the distributional matching
      hypothesis"——其失败不是方法论错误，而是对 Zhao et al. (2019) 理论的实证验证，
      同时指向 linear projection (~80 pairs) 作为 practical recommendation。

  # ============================================================
  # plan_004 — Difficulty-Controlled Decomposition Ablation
  # ============================================================
  - name: "Difficulty-Controlled Decomposition Ablation"
    plan_id: plan_004
    description: >
      IRT difficulty probes → project out difficulty direction → retrain correctness probes → evaluate transfer。
      10 languages × 8 layers × 3 models。含 random-direction control。
      Median tier: 定性分离成立但 prescriptive 能力弱，弱化为 descriptive。
    expected_results:
      mean_delta_auroc_difficulty_projected_pp: 1.8
      delta_auroc_range_pp: [-1.2, 3.5]
      langs_with_positive_delta_of_10: 6
      langs_with_negative_delta_of_10: 2
      langs_with_negligible_delta_of_10: 2
      random_direction_mean_delta_pp: 0.7
      difficulty_vs_random_effect_ratio: 2.6
      difficulty_probe_r2: 0.32
      per_lang_results:
        zh: { delta_pp: 0.8, sig: false }
        es: { delta_pp: 1.2, sig: false }
        fr: { delta_pp: 1.5, sig: true }
        de: { delta_pp: 1.8, sig: true }
        hi: { delta_pp: 2.8, sig: true }
        ru: { delta_pp: 2.2, sig: true }
        ko: { delta_pp: -0.6, sig: false }
        tr: { delta_pp: 2.5, sig: true }
        sw: { delta_pp: -1.2, sig: false }
        bn: { delta_pp: 3.5, sig: true }
      decomposition_clean_separation_count_of_10: 5
      prescriptive_accuracy: 0.56
    result_rationale: >
      Difficulty 成分确实跨语言共享（IRT difficulty 与语言无关），projection 后 residual 更 capability-specific。
      平均 +1.8pp 改善高于 random-direction control 的 +0.7pp，比值 2.6 表明约 60% 的效果是
      difficulty-specific，40% 来自纯维度缩减降噪。但效果 modest (<3pp for most languages)，
      原因：(1) difficulty probe R²=0.32 意味着 projection 不完全——只移除了 32% 的 difficulty 方差；
      (2) difficulty 和 capability 在 activation 空间中不正交——projection 在 ko/sw 中损害了 AUROC，
      因为这些语言的 difficulty-capability 纠缠更深（ko 的 MMLU difficulty ordering 与 EN 差异大，
      sw 的 correctness signal 本身就弱，projection 后更弱）；
      (3) HIGH 资源语言（zh/es）改善小是因为 capability 成分已经 well-aligned（不需要 decomposition），
      MID/LOW 资源语言改善更大是因为 removing difficulty confound 确实帮助——
      但仅在 correctness signal 足够强的 MID 语言上 (hi/ru/tr/bn)。
      Prescriptive accuracy 56% (vs chance 50%) 表明 decomposition 无法可靠预测最优对齐策略。
      弱化 Claim 2 为 "descriptive separation observed; difficulty-capability entanglement varies
      across languages but decomposition does not reliably predict optimal transfer strategy"。
    tables:
      - name: "Table 8: Decomposition Results by Language (Qwen3-235B, 8-layer mean)"
        data: |
          | Language | Tier | Full AUROC | Diff-proj AUROC | Δ (pp) | Random-proj AUROC | Rand Δ (pp) | Diff-specific (pp) |
          |----------|------|------------|-----------------|--------|-------------------|-------------|--------------------|
          | zh       | HIGH | 0.738      | 0.746           | +0.8   | 0.742             | +0.4        | +0.4               |
          | es       | HIGH | 0.745      | 0.757           | +1.2   | 0.751             | +0.6        | +0.6               |
          | fr       | HIGH | 0.740      | 0.755           | +1.5   | 0.747             | +0.7        | +0.8               |
          | de       | HIGH | 0.725      | 0.743           | +1.8   | 0.733             | +0.8        | +1.0               |
          | hi       | MID  | 0.670      | 0.698           | +2.8   | 0.678             | +0.8        | +2.0               |
          | ru       | MID  | 0.705      | 0.727           | +2.2   | 0.713             | +0.8        | +1.4               |
          | ko       | MID  | 0.688      | 0.682           | -0.6   | 0.691             | +0.3        | -0.9               |
          | tr       | MID  | 0.660      | 0.685           | +2.5   | 0.668             | +0.8        | +1.7               |
          | sw       | LOW  | 0.598      | 0.586           | -1.2   | 0.601             | +0.3        | -1.5               |
          | bn       | LOW  | 0.612      | 0.647           | +3.5   | 0.620             | +0.8        | +2.7               |
    figures_description:
      - >
        Decomposition scatter (Figure 7): x=difficulty-specific Δ AUROC (difficulty-projected minus random-projected),
        y=language distance from EN (typological). Color=resource tier. Positive x indicates genuine
        difficulty-capability separation. Most MID languages in upper-right quadrant (separation helps);
        ko and sw in left (separation hurts). Ellipses overlay tier groups.
    analysis: >
      Decomposition 支持 "correctness transfer contains difficulty-shared and capability-specific components"
      的定性结论。6/10 语言 show improvement，其中 5 具有统计显著性，且 difficulty-specific effect
      consistently exceeds random-direction control。但 prescriptive accuracy (56%) 与 chance (50%)
      差距极小——decomposition 不是 reliable strategy selector。
      Paper 中弱化 Claim 2 为 subsection-level descriptive finding，压缩到 ~1 page：
      "We observe that projecting out the shared difficulty component generally improves
      transfer for mid-resource languages (+2-3pp) but can harm low-resource languages where
      difficulty and capability are more entangled. This separation is descriptive rather than
      prescriptive — it explains what transfer contains but does not predict optimal strategy."

  # ============================================================
  # plan_005 — Cross-Lingual Orthogonality Analysis
  # ============================================================
  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: plan_005
    description: >
      提取 verbalized confidence direction，计算与 correctness direction 的 cosine similarity，
      20 languages × 2+ architectures。Supporting evidence for Claim 4 (subsection)。
    expected_results:
      mean_cosine_all_langs: 0.040
      cosine_range: [0.010, 0.148]
      langs_below_0.05: 13
      langs_below_0.10: 17
      langs_above_0.10: 3
      per_tier_mean_cosine:
        HIGH: 0.026
        MID: 0.044
        LOW: 0.075
      architecture_comparison:
        qwen3_mean: 0.037
        llama4_mean: 0.043
        difference_sig: false  # p=0.42
      outlier_langs: [am, yo, te]
      outlier_cosine: [0.148, 0.122, 0.105]
    result_rationale: >
      Miao & Ungar (2026) 在 English 7-8B 上发现 cosine < 0.04。跨语言扩展时：
      HIGH 资源语言复现此结果（模型对这些语言的 correctness 和 confidence direction 都稳定，
      分化清晰）。MID 语言 cosine 略高（0.03-0.06），因为 verbalized confidence 在中资源语言上
      更不稳定（模型在这些语言上的 confidence verbalization 训练数据更少）。
      LOW 资源语言中 am/yo/te 出现较高 cosine (>0.10)——这不是真正的 correctness-confidence
      alignment，而是两个 direction 都很弱时 cosine 被噪声主导的 artifact。
      plan_013 full-scale control task 将确认这些语言的 deep-layer selectivity < 0.05。
      两个架构间差异不显著 (0.037 vs 0.043, p=0.42)——orthogonality 是 representation 的
      structural property，不随架构变化。
    tables:
      - name: "Table 9: Correctness-Confidence Cosine Similarity by Resource Tier"
        data: |
          | Tier | n  | Mean cos | Std   | Min   | Max   | n < 0.05 | n < 0.10 |
          |------|----|----------|-------|-------|-------|----------|----------|
          | HIGH | 6  | 0.026    | 0.010 | 0.010 | 0.042 | 5        | 6        |
          | MID  | 8  | 0.044    | 0.016 | 0.022 | 0.072 | 4        | 8        |
          | LOW  | 6  | 0.075    | 0.038 | 0.030 | 0.148 | 2        | 3        |
    figures_description:
      - >
        Bar chart: 20 languages sorted by cosine ascending, bar color = resource tier.
        Horizontal dashed lines at 0.04 (Miao & Ungar threshold) and 0.10 (noise artifact threshold).
        Most bars below 0.04; am/yo/te protrude above 0.10. Inset: architecture comparison
        (Qwen3 vs Llama4 paired bars for 5 representative languages, showing near-identical values).
    analysis: >
      Orthogonality 作为 subsection supporting evidence 充分：17/20 languages cosine < 0.10,
      13/20 < 0.05。结论 compact：correctness-confidence orthogonality is cross-lingually robust,
      reinforcing the necessity of probe-based calibration methods over output-based approaches.
      am/yo/te 高 cosine 与 plan_013 selectivity analysis 交叉验证——若 selectivity < 0.05,
      则标注为 unreliable measurement。

  # ============================================================
  # plan_006 — Probe Complexity Comparison (LR vs MLP)
  # ============================================================
  - name: "Probe Complexity Comparison (LR vs 2-Layer MLP)"
    plan_id: plan_006
    description: >
      每层每模型对比 logistic regression 和 2-layer MLP 的 EN accuracy、
      cross-lingual transfer degradation 和 calibration quality。CPU-bound。
    expected_results:
      qwen3:
        lr_en_best_auroc: 0.81
        mlp_en_best_auroc: 0.832
        lr_mean_zs_auroc: 0.668
        mlp_mean_zs_auroc: 0.638
        lr_transfer_gap_pp: 14.2
        mlp_transfer_gap_pp: 19.4
      llama4:
        lr_en_best_auroc: 0.77
        mlp_en_best_auroc: 0.792
        lr_mean_zs_auroc: 0.648
        mlp_mean_zs_auroc: 0.622
        lr_transfer_gap_pp: 12.2
        mlp_transfer_gap_pp: 17.0
      mlp_en_advantage_mean_pp: 2.1
      lr_transfer_advantage_mean_pp: 3.0
      lr_preferred_for_transfer: true
      mlp_preferred_for_en_only: true
    result_rationale: >
      MLP (2-layer, 256 hidden units) 多出的参数让它学到 EN-specific activation patterns
      （如英语特有的 token position bias、named entity patterns 等），EN AUROC +2.1pp。
      但这些 EN-specific patterns 不跨语言迁移——MLP 过拟合了 EN distributional structure。
      LR 被迫学习单一 hyperplane（1 个 correctness direction），更可能对应 language-agnostic subspace。
      Transfer gap: LR ~13pp vs MLP ~18pp——MLP 多出的 ~5pp gap 分解为 EN advantage (~2pp)
      + EN-specific overfitting (~3pp)。
      ECE 模式相同：MLP 在 EN 上 ECE 更好（更多参数→更好的概率估计），
      但在 ZS transfer 时 ECE 更差（overfitted probabilities 在新 distribution 上更 miscalibrated）。
    tables:
      - name: "Table 10: LR vs MLP Transfer Comparison"
        data: |
          | Metric                    | Qwen3 LR | Qwen3 MLP | Llama4 LR | Llama4 MLP |
          |---------------------------|----------|-----------|-----------|------------|
          | EN best AUROC             | 0.810    | 0.832     | 0.770     | 0.792      |
          | Mean ZS AUROC             | 0.668    | 0.638     | 0.648     | 0.622      |
          | Transfer gap (pp)         | 14.2     | 19.4      | 12.2      | 17.0       |
          | EN ECE (best layer)       | 0.178    | 0.165     | 0.192     | 0.178      |
          | Mean ZS ECE               | 0.218    | 0.248     | 0.228     | 0.258      |
          | ZS pass rate (>0.58)      | 75%      | 55%       | 70%       | 50%        |
    figures_description:
      - >
        Paired scatter (Figure S1): x=LR ZS AUROC, y=MLP ZS AUROC, each dot a language,
        diagonal y=x line. Most points below diagonal (MLP worse for transfer),
        especially LOW-resource (larger markers). HIGH-resource points cluster near diagonal
        (both methods similar for well-aligned languages).
    analysis: >
      LR vs MLP 验证了 linear probe 是 cross-lingual transfer 的正确方法论选择。
      Paper 中报告为 methodology validation (1-2 paragraphs)，不展开为独立贡献。

  # ============================================================
  # plan_007 — Additional Benchmark Evaluation
  # ============================================================
  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: plan_007
    description: >
      在 Belebele (RC) 和 MMLU-ProX (翻译 MMLU) 上评估 best probes + all transfer methods。
      验证 generalization beyond GlobalMMLU。20 languages × 2 models。
    expected_results:
      belebele:
        en_best_auroc: 0.75
        mean_zs_auroc: 0.632
        zs_pass_rate: 0.60
        pareto_preserved: true
        pareto_strength: "weaker than GlobalMMLU (fewer sig langs)"
        pareto_sig_langs_of_20: 6
        rank_corr_with_globalmmlu: 0.84
        linear_proj_delta_pp: 2.5
        caclr_delta_pp: 0.2
      mmlu_prox:
        en_best_auroc: 0.79
        mean_zs_auroc: 0.658
        zs_pass_rate: 0.72
        pareto_preserved: true
        pareto_strength: "comparable to GlobalMMLU"
        pareto_sig_langs_of_20: 8
        rank_corr_with_globalmmlu: 0.92
        linear_proj_delta_pp: 2.8
        caclr_delta_pp: 0.3
      cross_benchmark_lang_ranking_rho: 0.89
      linear_proj_generalizes: true
      caclr_still_inert: true
    result_rationale: >
      Belebele 是阅读理解（passage-dependent correctness），与 GlobalMMLU 的 parametric knowledge
      不同——correctness signal 的性质部分不同。EN AUROC 略低 (0.75 vs 0.81)，因为 RC correctness
      更依赖 passage comprehension 而非 parametric knowledge，probe 的 linear accessibility
      稍低。Transfer 更差因为 RC 的 cross-lingual alignment 更依赖 word-level translation quality。
      但 Pareto 结构保留——depth-transferability tradeoff 是 representation geometry 的性质。
      MMLU-ProX 与 GlobalMMLU 高度相关（同源翻译数据），模式几乎一致 (rho=0.92)。
      Cross-benchmark language ranking rho=0.89——结果不是 benchmark-specific。
      CaCLR 在两个 benchmark 上仍 inert，linear projection 仍有效——泛化确认。
    tables:
      - name: "Table 11: Cross-Benchmark Consistency (Qwen3-235B)"
        data: |
          | Metric             | GlobalMMLU | Belebele | MMLU-ProX |
          |--------------------|------------|----------|-----------|
          | EN best AUROC      | 0.81       | 0.75     | 0.79      |
          | Mean ZS AUROC      | 0.668      | 0.632    | 0.658     |
          | ZS pass rate       | 75%        | 60%      | 72%       |
          | Pareto sig langs   | 9          | 6        | 8         |
          | Linear proj Δ (pp) | +3.0       | +2.5     | +2.8      |
          | CaCLR Δ (pp)       | +0.3       | +0.2     | +0.3      |
    figures_description:
      - >
        Parallel coordinates (Figure S2): each line = a language, x-axis = 3 benchmarks,
        y-axis = ZS AUROC. Lines colored by resource tier. Mostly parallel (consistent ranking);
        Belebele systematically lower. A few crossing lines indicate benchmark-specific rank changes
        (e.g., ja relatively better on Belebele due to strong RC training data).
    analysis: >
      Cross-benchmark 验证确认主要发现的 robustness。Belebele 上 Pareto 更弱是预期的。
      Key message: "all qualitative findings (architecture dependence, resource-tier gradient,
      CaCLR failure, linear projection effectiveness) generalize across benchmarks."

  # ============================================================
  # plan_008 — Gemma 4 31B Dense (Third Architecture)
  # ============================================================
  - name: "Gemma 4 32.7B Dense — Third Architecture"
    plan_id: plan_008
    description: >
      Dense 架构对照 (vs 两个 MoE)，60 text decoder layers, BF16, 20 languages。
      提供 dense vs MoE architectural contrast。P0 for core submission。
    expected_results:
      en_best_auroc: 0.79
      en_best_layer: L52
      en_best_layer_depth_pct: 0.867
      en_auroc_range: [0.60, 0.79]
      en_best_ece_raw: 0.182
      layer_depth_delta_pp: 19.0
      transfer_optimal_layer_mean: L44
      transfer_optimal_depth_pct: 0.733
      en_transfer_layer_gap_auroc_pp: 1.8
      zs_pass_count_of_20: 14
      zs_pass_rate: 0.70
      zs_mean_auroc_at_en_optimal_layer: 0.660
      mean_zs_auroc_drop_vs_en_pp: 11.0
      pareto_langs_significant_negative_rho: 7
      pareto_spearman_rho_median: -0.32
      pareto_depth_transfer_drop_final_layers_pp: 1.6
      cka_cliff_slope: -0.014
      cka_cliff_onset_depth_pct: 0.58
      partial_rho_cka: 0.24
      partial_p: 0.038
      simpson_significant: true
    result_rationale: >
      Dense 架构的 CKA decline 比 MoE 更线性渐进——无 expert routing 加速特异化机制，
      所有参数共享导致语言 representation 的分化更缓慢。
      CKA slope ~-0.014/layer，介于 Qwen3 (-0.022) 和 Llama4 (-0.013) 之间。
      EN AUROC ~0.79 (31B full params) 接近 Qwen3 的 0.81 (22B active MoE)，
      因为 correctness direction 的 linear accessibility 在 ~20B+ 后已接近 saturation。
      Pareto 强度 intermediate: 7/20 语言显著负 rho (between Qwen3's 9 and Llama4's 5)。
      Simpson's Paradox 在 Gemma 4 上显著 (partial rho=0.24, p=0.038)——
      其 linear-ish CKA decline 使得 linear partial correlation 比 Qwen3 的 step-function
      decline 更有效（Qwen3 partial rho=0.16, p=0.072 不显著，部分因为非线性 depth-CKA 关系）。
      三架构 Simpson's confirmation: Llama4 (显著), Gemma4 (显著), Qwen3 (trending) → 2/3。
      Dense vs MoE 对比核心发现：Pareto 不是 MoE-specific，dense 架构也有但更弱。
      这排除了 "Pareto tradeoff 是 MoE expert routing 的 artifact" 的替代假说。
    tables:
      - name: "Table 12: Three-Architecture Comparison"
        data: |
          | Metric                      | Qwen3-235B (MoE) | Llama4 Scout (MoE) | Gemma4 31B (Dense) |
          |-----------------------------|-------------------|--------------------|---------------------|
          | Type                        | MoE (22B active)  | MoE (17B active)   | Dense (31B)         |
          | Total / Active params       | 235B / 22B        | 109B / 17B         | 31B / 31B           |
          | Layers                      | 94                | 48                 | 60                  |
          | EN best AUROC               | 0.81              | 0.77               | 0.79                |
          | Mean ZS AUROC               | 0.668             | 0.648              | 0.660               |
          | Pareto sig langs (/20)      | 9                 | 5                  | 7                   |
          | Median Pareto ρ             | -0.38             | -0.25              | -0.32               |
          | CKA cliff slope             | -0.022            | -0.013             | -0.014              |
          | Partial ρ (CKA~AUROC|depth) | 0.16 (p=.072)     | 0.29 (p=.018)      | 0.24 (p=.038)       |
          | Simpson's sig?              | Trending          | Yes                | Yes                 |
    figures_description:
      - >
        Three-architecture CKA depth profile (Figure 8): x=normalized depth (0→1),
        y=mean CKA across 20 languages. Three lines: Qwen3 (late sharp cliff after 0.68),
        Llama4 (gradual decline from 0.50), Gemma4 (intermediate, starts ~0.58).
        Shaded regions mark "Pareto zone" where EN-optimal and transfer-optimal diverge.
    analysis: >
      Gemma 4 作为 dense 对照确认 Pareto 不是 MoE artifact。三架构的 CKA cliff slope
      与 Pareto 强度呈清晰的 monotonic relationship (steeper → more languages with tradeoff)，
      但 n=3 仅为 suggestive。Simpson's Paradox 变为 2/3 显著——strengthens geometric narrative。
      Paper 中强调 architecture dependence 是 descriptive finding (各架构 scale/depth/training data
      all differ, 无法 isolate 单一因素)。

  # ============================================================
  # plan_009 — Extended Language Coverage (50+ languages)
  # ============================================================
  - name: "Extended Language Coverage (50+ Languages)"
    plan_id: plan_009
    description: >
      从 20 扩展至 50+ 语言，利用 GlobalMMLU/Belebele 全语言集。Camera-ready extension。
    expected_results:
      total_languages: 52
      zs_pass_rate_52: 0.60
      zs_pass_count_52: 31
      artifact_rate_very_low_resource: 0.45
      new_low_resource_langs_with_artifacts: 16
      resource_tier_gradient_confirmed: true
      rank_correlation_20_vs_52: 0.95
      min_zs_auroc: 0.50
      min_zs_lang: "Haitian Creole (ht)"
      new_findings: >
        Diminishing returns; very-low-resource languages (< 1M training tokens) uniformly
        near chance. Writing system clusters emerge (Cyrillic, Devanagari, Arabic script)
        as moderate predictor of transfer quality within resource tier.
    result_rationale: >
      新增 32 语言大多为 LOW/VERY-LOW resource。Pass rate 从 20 语言的 ~72% 降至 52 语言的 ~60%，
      因为新增语言偏向低资源。Very-low-resource 语言 (ht, rm, fy, gd 等) 的 artifact rate ~45%，
      几乎一半的 layer-language 结果不可靠。但 20 语言的核心发现在 52 语言上完全保持 (rank corr 0.95)。
      主要增量贡献：(1) 统计 power 增加 (n=52 vs n=20 for cross-language analyses)，
      (2) writing system 作为 transfer predictor 的新发现（同脚本语言 pair 的 CKA 更高），
      (3) 覆盖面更全面的 field-level claim。边际收益递减——每新增一种语言，对核心 claim 的增量证据极小。
    tables:
      - name: "Table S1: Language Coverage Expansion Summary"
        data: |
          | Tier      | 20-lang n | 52-lang n | Mean ZS AUROC | Artifact rate | Pass rate |
          |-----------|-----------|-----------|---------------|---------------|-----------|
          | HIGH      | 6         | 10        | 0.72          | 5%            | 100%      |
          | MID       | 8         | 15        | 0.66          | 20%           | 87%       |
          | LOW       | 6         | 16        | 0.58          | 32%           | 56%       |
          | VERY-LOW  | 0         | 11        | 0.53          | 45%           | 27%       |
    figures_description:
      - >
        World map (Figure S3): 52 languages plotted, color = ZS AUROC (green=high, red=low).
        Western Europe and East Asia green; Sub-Saharan Africa and Pacific islands red.
        Inset: writing system clusters with mean CKA.
    analysis: >
      Camera-ready extension。Core story 不变。VERY-LOW resource languages 的高 artifact rate
      reinforces probing control 的必要性。Paper 中 core analysis 仍基于 20 languages (cleaner statistics)，
      52-language results in extended table + map visualization。

  # ============================================================
  # plan_010 — Quantization Validation Ablation
  # ============================================================
  - name: "Quantization Validation Ablation"
    plan_id: plan_010
    description: >
      (a) W4A16 vs FP16 at 5 layers for Llama 4 Scout on 5% subset;
      (b) GPTQ-Int4 vs FP16 at 5 layers for Qwen3-235B on 5% subset.
    expected_results:
      llama4_w4a16_vs_fp16:
        mean_abs_delta_auroc: 0.004
        max_abs_delta_auroc: 0.008
        per_layer_deltas: { L8: -0.002, L16: +0.004, L24: -0.005, L36: +0.003, L44: -0.008 }
        cka_fp16_vs_quant_mean: 0.988
      qwen3_int4_vs_fp16:
        mean_abs_delta_auroc: 0.006
        max_abs_delta_auroc: 0.012
        per_layer_deltas: { L16: -0.005, L36: +0.004, L52: -0.003, L68: +0.006, L80: -0.012 }
        cka_fp16_vs_quant_mean: 0.980
      quantization_safe: true
      conclusion: "All |ΔAUROC| < 0.015, all CKA > 0.97 — quantization artifacts negligible"
    result_rationale: >
      4-bit weight quantization 保留 activation 空间的大部分结构。Correctness direction 是
      低维子空间特征——quantization noise 主要分布在与 correctness direction 正交的高维 null space 中
      (random projection preservation 原理)。Qwen3 的 MoE + INT4 在最深层 (L80) 有稍大 delta
      (-0.012pp) 因为 expert routing 决策在 INT4 下可能微变，但仍在 bootstrap CI 内。
      CKA(FP16, quant) > 0.97 确认 global representation structure 保留。
    tables:
      - name: "Table S2: Quantization Validation Per-Layer"
        data: |
          | Model  | Layer (depth%) | FP16 AUROC | Quant AUROC | ΔAUROC  | CKA     |
          |--------|----------------|------------|-------------|---------|---------|
          | Llama4 | L8 (17%)       | 0.635      | 0.633       | -0.002  | 0.992   |
          | Llama4 | L16 (33%)      | 0.688      | 0.692       | +0.004  | 0.990   |
          | Llama4 | L24 (50%)      | 0.722      | 0.717       | -0.005  | 0.988   |
          | Llama4 | L36 (75%)      | 0.750      | 0.753       | +0.003  | 0.986   |
          | Llama4 | L44 (92%)      | 0.770      | 0.762       | -0.008  | 0.984   |
          | Qwen3  | L16 (17%)      | 0.632      | 0.627       | -0.005  | 0.988   |
          | Qwen3  | L36 (38%)      | 0.708      | 0.712       | +0.004  | 0.984   |
          | Qwen3  | L52 (55%)      | 0.742      | 0.739       | -0.003  | 0.982   |
          | Qwen3  | L68 (72%)      | 0.775      | 0.781       | +0.006  | 0.978   |
          | Qwen3  | L80 (85%)      | 0.810      | 0.798       | -0.012  | 0.972   |
    figures_description:
      - >
        Bland-Altman plot (Figure S4): x=(FP16+Quant)/2, y=(FP16-Quant). Each point = one layer.
        Horizontal dashed lines at ±0.01 tolerance. All points within band except Qwen3 L80
        at -0.012 (slightly outside, annotated). Mean difference line near zero.
    analysis: >
      Quantization safe. 报告为一段话 + appendix table:
      "Quantization artifacts are negligible (max |ΔAUROC| = 0.012, CKA > 0.97 across all layers),
      supporting the validity of our INT4/W4A16 experimental setup."

  # ============================================================
  # plan_011 — CKA Simpson's Paradox + Geometric Analysis
  # ============================================================
  - name: "Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis"
    plan_id: plan_011
    description: >
      Linear CKA (EN vs 20 target languages) at every probed layer, 3 models。
      Core analysis: partial correlation controlling for depth (Simpson's Paradox)。
      Median tier: 1-2/3 architectures significant。
    expected_results:
      qwen3:
        raw_spearman_rho: -0.24
        raw_p: "<0.001"
        partial_rho_ctrl_depth: 0.16
        partial_p: 0.072
        significant: false
        bootstrap_ci_95: [-0.03, 0.35]
        per_layer_positive_rho_count_of_24: 17
        per_layer_significant_count: 5
        cka_cliff_onset_layer: L64
        cka_cliff_onset_depth_pct: 0.68
        cka_final_layer_mean: 0.09
        cka_peak_layer: L36
        cka_peak_mean: 0.82
      llama4:
        raw_spearman_rho: -0.30
        raw_p: "<0.001"
        partial_rho_ctrl_depth: 0.31
        partial_p: 0.012
        significant: true
        bootstrap_ci_95: [0.08, 0.52]
        per_layer_positive_rho_count_of_12: 10
        per_layer_significant_count: 4
        cka_cliff_onset_layer: L24
        cka_cliff_onset_depth_pct: 0.50
        cka_final_layer_mean: 0.20
        cka_peak_layer: L12
        cka_peak_mean: 0.83
      gemma4:
        raw_spearman_rho: -0.26
        raw_p: "<0.001"
        partial_rho_ctrl_depth: 0.24
        partial_p: 0.038
        significant: true
        bootstrap_ci_95: [0.02, 0.45]
        per_layer_positive_rho_count_of_16: 12
        per_layer_significant_count: 4
        cka_cliff_onset_layer: L36
        cka_cliff_onset_depth_pct: 0.60
        cka_final_layer_mean: 0.15
        cka_peak_layer: L20
        cka_peak_mean: 0.80
      simpson_paradox_confirmed_of_3: 2
      cka_transfer_collapse_threshold: 0.30
      subspace_angle_analysis:
        qwen3: { HIGH_angle: 10, MID_angle: 22, LOW_angle: 46 }
        llama4: { HIGH_angle: 13, MID_angle: 26, LOW_angle: 41 }
        gemma4: { HIGH_angle: 11, MID_angle: 24, LOW_angle: 43 }
    result_rationale: >
      Simpson's Paradox 的架构依赖性源于 CKA-depth gradient 的函数形状。
      Llama4 CKA 从 peak 0.83 (L12) 线性下降到 0.20 (L48)——steep linear slope 使得
      linear partial correlation 高效地分离 depth confound (partial rho=0.31, p=0.012)。
      Gemma4 CKA 也近似线性下降 (partial rho=0.24, p=0.038)——intermediate slope 产生
      intermediate partial correlation，也刚好显著。
      Qwen3 的 CKA profile 是 "plateau then cliff"：L0-L64 CKA 几乎不变 (0.75-0.82)，
      L64-L92 急剧下降到 0.09。这种 step-function-like profile 导致 linear partial correlation
      效果差——depth 作为线性控制变量无法有效 capture 非线性 CKA-depth 关系。
      Partial rho=0.16 (p=0.072) trending 但不显著。加入 depth² 作为二次控制项后可能显著，
      但 paper 中应诚实报告 standard method 的结果。
      Per-layer analysis (n=20 languages per layer): 大多数层的 within-layer rho 为正
      (70-83% of layers across models)，但因 n=20 individual significance 有限。
      最有 power 的层在 50-75% depth（CKA variance 最大的区域）。
      Subspace angle 提供互补定量证据：HIGH 语言 ~10-13°（几乎对齐，zero-shot 可行），
      LOW 语言 ~41-46°（严重 misaligned，需要 linear projection）。
      这与 Procrustes reversal (plan_012) 的发现互洽——reversal 阈值对应 ~20-25° angle。
    tables:
      - name: "Table 13: Simpson's Paradox — Raw vs Partial Correlation (3 architectures)"
        data: |
          | Architecture   | n obs | Raw ρ  | Raw p   | Partial ρ | Partial p | Boot 95% CI    | Sig? |
          |----------------|-------|--------|---------|-----------|-----------|----------------|------|
          | Qwen3-235B     | 480   | -0.24  | <0.001  | +0.16     | 0.072     | [-0.03, +0.35] | No   |
          | Llama4 Scout   | 240   | -0.30  | <0.001  | +0.31     | 0.012     | [+0.08, +0.52] | Yes  |
          | Gemma4 31B     | 320   | -0.26  | <0.001  | +0.24     | 0.038     | [+0.02, +0.45] | Yes  |
          | Pilot Llama8B  | 45    | -0.16  | 0.294   | +0.41     | 0.006     | [+0.12, +0.65] | Yes  |
          | Pilot Qwen7B   | 40    | -0.16  | 0.310   | +0.18     | 0.274     | [-0.15, +0.48] | No   |
      - name: "Table 14: CKA Depth Profile Summary"
        data: |
          | Depth %  | Qwen3 CKA | Llama4 CKA | Gemma4 CKA |
          |----------|-----------|------------|------------|
          | 0%       | 0.70      | 0.58       | 0.62       |
          | 17%      | 0.76      | 0.81       | 0.78       |
          | 34%      | 0.82      | 0.75       | 0.75       |
          | 50%      | 0.80      | 0.56       | 0.65       |
          | 68%      | 0.60      | 0.40       | 0.48       |
          | 77%      | 0.38      | 0.32       | 0.38       |
          | 85%      | 0.22      | 0.28       | 0.28       |
          | 100%     | 0.09      | 0.20       | 0.15       |
      - name: "Table 15: Subspace Angle Analysis (Correctness Direction)"
        data: |
          | Tier | Qwen3 angle | Llama4 angle | Gemma4 angle | Mean ZS AUROC | Interpretation          |
          |------|-------------|--------------|--------------|---------------|-------------------------|
          | HIGH | 10°         | 13°          | 11°          | 0.72          | Near-aligned            |
          | MID  | 22°         | 26°          | 24°          | 0.66          | Moderate rotation       |
          | LOW  | 46°         | 41°          | 43°          | 0.57          | Substantial misalignment|
    figures_description:
      - >
        Simpson's Paradox visualization (Figure 9 — core figure): two panels per model (6 total).
        Scatter: x=CKA, y=ZS AUROC. Each point = (layer, language) pair. Color = normalized depth.
        Overall regression line (dashed, negative slope) vs per-depth-bin regression lines (solid, positive slopes).
        Sign reversal visible. Annotations: "Raw ρ=−0.24 vs Partial ρ=+0.16 (p=.072)" for Qwen3,
        "Raw ρ=−0.30 vs Partial ρ=+0.31 (p=.012)" for Llama4,
        "Raw ρ=−0.26 vs Partial ρ=+0.24 (p=.038)" for Gemma4.
      - >
        CKA × layer × language heatmap (Figure 10): three panels (one per model).
        x=20 languages (sorted by mean CKA), y=probed layers (by depth), color=CKA.
        Qwen3 shows late, sharp transition from warm to cool colors (step-function).
        Llama4 shows early, gradual gradient. Gemma4 intermediate.
    analysis: >
      Simpson's Paradox 在 2/3 architectures 统计显著 (Llama4, Gemma4)，Qwen3 trending (p=0.072)。
      Paper 中用 hedged language: "In architectures with near-linear CKA depth gradients
      (Llama 4, Gemma 4), partial correlation controlling for depth reveals a significant
      positive CKA-transfer relationship (ρ=0.24-0.31, p<0.05), confirming that CKA
      provides genuine explanatory power beyond depth. In Qwen3-235B, the step-function-like
      CKA profile limits linear partial correlation effectiveness (ρ=0.16, p=0.072);
      within-layer analysis confirms the positive direction (17/24 layers positive ρ)."
      CKA cliff slope 与 Pareto strength 的 monotonic relationship across 3 architectures
      is suggestive but n=3 is insufficient for formal correlation. Frame as observation.
      Subspace angle analysis provides the most directly interpretable geometric result:
      correctness direction rotates gradually from EN as language distance increases,
      with resource tier as a strong proxy for rotation magnitude.

  # ============================================================
  # plan_012 — Linear Projection Sensitivity & Procrustes Reversal
  # ============================================================
  - name: "Linear Projection Sensitivity & Procrustes Effect Reversal"
    plan_id: plan_012
    description: >
      Vary parallel pairs (10, 20, 50, 100, 200) for linear projection.
      2 models × 5 representative layers × 20 languages。Resource-tier stratified saturation curves。
      Procrustes effect reversal analysis。
    expected_results:
      overall_pairs_to_95pct: 80
      per_tier_pairs_to_95pct:
        HIGH: 38
        MID: 62
        LOW: 95
      saturation_curve:
        pairs_10: { pct_of_max: 0.38, mean_delta_auroc_pp: 1.1 }
        pairs_20: { pct_of_max: 0.58, mean_delta_auroc_pp: 1.7 }
        pairs_50: { pct_of_max: 0.82, mean_delta_auroc_pp: 2.5 }
        pairs_100: { pct_of_max: 0.95, mean_delta_auroc_pp: 2.9 }
        pairs_200: { pct_of_max: 1.00, mean_delta_auroc_pp: 3.0 }
      procrustes_reversal:
        threshold_estimate: 0.57
        threshold_ci_95: [0.48, 0.64]
        benefit_below_0.50: { mean_delta_pp: 5.5, n_langs: 3 }
        ambiguous_0.50_0.60: { mean_delta_pp: 1.8, n_langs: 5 }
        mild_benefit_0.60_0.65: { mean_delta_pp: 0.3, n_langs: 4 }
        harm_above_0.65: { mean_delta_pp: -1.5, n_langs: 8 }
      saturation_r2_by_tier:
        HIGH: 0.97
        MID: 0.92
        LOW: 0.80
      linear_proj_delta_low_resource_pp: 5.0
    result_rationale: >
      Saturation at ~80 pairs (而非 pilot 预估的 ~50)，因为：(1) 20 语言引入更多方差，
      (2) 部分低资源语言的 parallel pair translation quality 低（机翻 artifacts 增加 noise），
      (3) 低资源语言的 subspace angle 更大 (~40-46°)，需要更多样本来估计更复杂的旋转。
      Resource-tier stratification 清晰：HIGH 语言 ~38 pairs (subspace angle ~10-13°, 简单旋转)，
      LOW 语言 ~95 pairs (angle ~41-46°, 更复杂旋转 + translation noise)。
      Procrustes reversal mechanism: 当 ZS AUROC > 0.65 时，EN-target correctness direction
      已 near-aligned (angle <15°)，Procrustes 旋转估计引入的 noise > alignment gain → 净负效果。
      当 ZS AUROC < 0.50 时，严重 misalignment (angle >35°) 使得 alignment gain >> noise。
      Threshold ~0.57 对应 ~20° angle 的平衡点。
      LOW tier 的 curve 不够 clean (R²=0.80)——个别语言 saturation 非单调
      (e.g., sw 在 20 pairs 时偶然好于 50 pairs，因为特定 pair 的 quality variance)。
      Practical recommendation: ~80 parallel pairs for general use;
      skip projection for HIGH-resource languages (ZS AUROC > 0.65)。
    tables:
      - name: "Table 16: Saturation Curves by Resource Tier (Qwen3-235B, L68)"
        data: |
          | Pairs | HIGH Δ (pp) | MID Δ (pp) | LOW Δ (pp) | Overall Δ (pp) |
          |-------|-------------|------------|------------|----------------|
          | 10    | +0.1        | +0.8       | +2.5       | +1.1           |
          | 20    | +0.3        | +1.5       | +3.8       | +1.7           |
          | 50    | +0.4        | +2.3       | +5.2       | +2.5           |
          | 100   | +0.5        | +2.6       | +5.8       | +2.9           |
          | 200   | +0.5        | +2.7       | +6.2       | +3.0           |
      - name: "Table 17: Procrustes Effect Reversal by ZS AUROC Band"
        data: |
          | ZS AUROC band | n langs | Mean Δ (pp) | Std  | % positive | Example langs     |
          |---------------|---------|-------------|------|------------|-------------------|
          | < 0.50        | 3       | +5.5        | 1.8  | 100%       | am, yo, te        |
          | 0.50 - 0.58   | 3       | +3.2        | 1.5  | 100%       | sw, bn, tr        |
          | 0.58 - 0.62   | 2       | +1.2        | 0.9  | 100%       | hi, vi            |
          | 0.62 - 0.67   | 4       | +0.2        | 0.8  | 50%        | ar, ko, id, uk    |
          | 0.67 - 0.72   | 4       | -0.8        | 0.6  | 25%        | ru, ja, de, pt    |
          | > 0.72        | 4       | -1.8        | 0.5  | 0%         | zh, es, fr, nl    |
    figures_description:
      - >
        Saturation curves (Figure 11): x=number of parallel pairs (log scale), y=Δ AUROC (pp).
        Three lines (HIGH/MID/LOW), shaded bootstrap 95% CI. HIGH nearly flat after 40 pairs;
        LOW still climbing at 100 but plateauing by 200. Dashed horizontal line at "95% of max."
      - >
        Procrustes reversal scatter (Figure 12): x=ZS AUROC (zero-shot baseline),
        y=Δ AUROC from linear projection (200 pairs). Each point = (language, model) pair,
        color = model. LOESS fit shows smooth positive-to-negative transition.
        Vertical band marks reversal threshold (0.57, CI [0.48, 0.64]).
        Annotated practitioner guidance: "Use projection below 0.57, zero-shot above."
    analysis: >
      Linear projection 是最直接的 practical contribution：80 parallel pairs (约 3-4 小时标注) 达到
      95% of max improvement。LOW-resource languages benefit most (+5-6pp)，正是最需要帮助的类别。
      Procrustes reversal 是重要的 practitioner caveat——不加区分地做 alignment 会损害已经 well-aligned
      的语言。Deployment recommendation: 先测 zero-shot AUROC，低于 0.57 时 use projection，
      高于 0.65 时直接 zero-shot，0.57-0.65 区间按 language-specific validation 决定。
      Architecture-dependent threshold variation: Qwen3 threshold ~0.55, Llama4 ~0.60
      (Llama4 的 better baseline alignment 意味着 reversal 出现更早)——
      但 n=2 architectures 不足以 parametrize threshold，建议 practitioner 用 ~0.57 ± 0.05。

  # ============================================================
  # plan_013 (full-scale) — Probing Control Tasks
  # ============================================================
  - name: "Probing Control Tasks — Full Scale (20 languages × 3 models)"
    plan_id: plan_013
    description: >
      Hewitt & Liang (2019) control tasks 扩展到 20 languages × 3 architectures × 所有 probed layers。
      验证 AUROC 反映 genuine correctness direction。Selectivity threshold sensitivity analysis。
      Note: English-only pilot DONE (plan_013 registry), 此处为 full cross-lingual extension。
    expected_results:
      overall_artifact_rate_pct: 22
      artifact_rate_by_tier:
        HIGH: 5
        MID: 22
        LOW: 35
      selectivity_deep_layers_mean: 0.20
      selectivity_by_tier_deep_layers:
        HIGH: 0.23
        MID: 0.16
        LOW: 0.08
      control_auroc_range: [0.48, 0.52]
      threshold_sensitivity:
        threshold_0.03: { artifact_rate_pct: 32 }
        threshold_0.05: { artifact_rate_pct: 22 }
        threshold_0.10: { artifact_rate_pct: 12 }
      affected_zone: "primarily 0-40% depth for MID/LOW, 0-20% depth for HIGH"
      cross_lingual_control_finding: >
        ~22% of language-layer combinations have selectivity < 0.05.
        Concentrated in LOW-resource shallow layers (83% of L0-25% depth × LOW tier).
        At EN-optimal depth, only am/yo/te have selectivity < 0.05 (probe capacity artifacts).
    result_rationale: >
      Pilot (Qwen2.5-7B EN-only) 显示 selectivity 在 L20+ 为 0.24-0.26, L0-L12 为 0.02-0.04。
      跨语言扩展时：HIGH 资源语言的 deep-layer selectivity 接近 EN (~0.23)——
      模型对这些语言有足够的 correctness signal 使 real probe >> control probe。
      MID 资源语言 deep-layer selectivity 降至 ~0.16——仍明显超过 threshold 但 gap 缩小，
      因为 (1) correctness signal 更弱, (2) control probe 在更 uniform 的 activation 分布上
      偶尔达到略高 AUROC (0.50→0.51)。
      LOW 资源语言 deep-layer selectivity 仅 ~0.08——部分 language-layer 组合低于 0.05 threshold，
      尤其是 am/yo/te (这些语言在模型训练数据中极少，correctness signal 接近 noise floor)。
      ~22% overall artifact rate (at threshold 0.05) 的 breakdown：
      5% from HIGH (仅最浅层 L0-L4), 22% from MID (shallow+mid layers), 35% from LOW (broad range)。
      Threshold sensitivity: 0.03 更宽松 (32% artifacts)，0.10 更严格 (仅 12%)——
      paper 中报告 0.05 (Hewitt & Liang original) as primary，0.03/0.10 in sensitivity analysis。
      Field-level contribution: 首次在 cross-lingual probing 中系统应用 selectivity analysis。
    tables:
      - name: "Table 18: Artifact Rate by Resource Tier and Depth (3-model mean)"
        data: |
          | Depth zone     | HIGH artifact % | MID artifact % | LOW artifact % | Overall |
          |----------------|-----------------|----------------|----------------|---------|
          | 0-25% depth    | 15%             | 55%            | 80%            | 50%     |
          | 25-50% depth   | 3%              | 28%            | 55%            | 29%     |
          | 50-75% depth   | 0%              | 10%            | 18%            | 9%      |
          | 75-100% depth  | 0%              | 2%             | 5%             | 2%      |
          | Overall        | 5%              | 22%            | 35%            | 22%     |
      - name: "Table 19: Selectivity at EN-Optimal Layer (representative languages)"
        data: |
          | Tier | Language | Real AUROC | Control AUROC | Selectivity | Artifact? |
          |------|----------|------------|---------------|-------------|-----------|
          | HIGH | zh       | 0.738      | 0.502         | 0.236       | No        |
          | HIGH | es       | 0.745      | 0.498         | 0.247       | No        |
          | MID  | hi       | 0.670      | 0.506         | 0.164       | No        |
          | MID  | tr       | 0.660      | 0.510         | 0.150       | No        |
          | LOW  | sw       | 0.598      | 0.508         | 0.090       | No        |
          | LOW  | bn       | 0.612      | 0.504         | 0.108       | No        |
          | LOW  | yo       | 0.535      | 0.512         | 0.023       | YES       |
          | LOW  | am       | 0.530      | 0.515         | 0.015       | YES       |
          | LOW  | te       | 0.572      | 0.518         | 0.054       | Borderline|
    figures_description:
      - >
        Selectivity heatmap (Figure 13): x=20 languages (sorted by tier), y=probed layers (by depth).
        Color=selectivity (blue=artifact zone <0.05, warm=reliable >0.10).
        Clear diagonal pattern: bottom-left (shallow × low-resource) deep blue,
        top-right (deep × high-resource) warm. Dashed contour marks 0.05 threshold boundary.
        Second row: binary heatmap (artifact yes/no), emphasizing the 22% overall rate.
    analysis: >
      Control task 发现是独立的 methodological contribution。在 paper main body 中：
      (1) 用 selectivity threshold 过滤不可靠结果后重新报告 main results (confirm conclusions unchanged);
      (2) 报告 ~22% artifact rate 作为 methodological warning for the field;
      (3) 讨论 implications: "all cross-lingual probing studies should include selectivity checks,
      especially for low-resource languages where probe capacity can mimic genuine signal."
      am/yo 在 EN-optimal depth 的 selectivity < 0.03 确认 plan_005 中这些语言的
      高 cosine similarity 是 noise artifact 而非真实 correctness-confidence alignment。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69fab88e-f618-431b-b456-6b52aa18f5c1",
  "isSidechain": false,
  "requestId": "req_011CbFkpxAEZSG9xgfeNppuu",
  "type": "assistant",
  "uuid": "a37b4ab8-1eed-46ef-9966-ca0957b17e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrVonFh2FmTyPXs48b2Xuq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 80130,
      "output_tokens": 25186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 25186,
          "cache_read_input_tokens": 80130,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "a37b4ab8-1eed-46ef-9966-ca0957b17e32",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiment predictions for cross-lingual correctness probe transfer",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "a37b4ab8-1eed-46ef-9966-ca0957b17e32",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiment predictions for cross-lingual correctness probe transfer",
  "sessionId": "8214876e-3227-48e5-b866-c4dc450f1f75"
}
```

---
