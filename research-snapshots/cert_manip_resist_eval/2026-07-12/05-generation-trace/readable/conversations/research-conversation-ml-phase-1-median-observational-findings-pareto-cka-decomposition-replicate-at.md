# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/4b165f82-4576-4c8e-8e10-460d189b9eb4.jsonl`
- **Structured JSON:** [`5895c5ba3648479b3967.json`](../../sessions/58/5895c5ba3648479b3967.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:43:06.666Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:43:06.666Z",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; paper pivots to planned negative-result narrative with geometric explanation\n核心假设：['EN AUROC scales modestly; correctness signal present but not dramatically stronger in larger models', 'Pareto frontier exists in 1-2/3 architectures but is noisier (fewer languages show clear tradeoff per architecture)', \"Simpson's Paradox confirmed in ≥1 architecture but one architecture (likely Qwen, matching pilot rho=0.18) shows non-significant partial correlation\", 'CaCLR β sweep across 3 OOM shows no consistent benefit — consistency loss is inert (reframe as systematic negative result)', 'Decomposition is directionally correct but effect sizes are modest (<3pp), more qualitative than quantitative', 'Linear projection works but saturates at ~100 pairs, not 50; effect reversal threshold is architecture-dependent', 'Procrustes effect reversal replicates but threshold varies enough across architectures that a single rule is hard to state']\n关键指标范围：{'en_auroc_best_layer_mean_across_arch': [0.76, 0.82], 'zs_transfer_pass_rate_auroc_gt_058_of_20': [12, 16], 'mean_zs_auroc_drop_vs_en_pp': [8, 14], 'pareto_tradeoff_prevalence_frac_lang_arch_pairs': [0.25, 0.5], 'pareto_depth_transfer_drop_at_final_layers_pp': [1.0, 3.0], 'cka_partial_corr_rho_controlling_depth': [0.15, 0.35], 'cka_partial_corr_p_value': [0.005, 0.05], 'simpson_paradox_confirmed_of_3_arch': [1, 2], 'caclr_delta_over_zeroshot_mean_pp': [-0.5, 1.0], 'caclr_langs_improved_of_20': [5, 10], 'linear_proj_delta_over_zs_low_resource_pp': [3, 7], 'linear_proj_saturation_pairs': [50, 120], 'decomposition_transfer_improvement_after_difficulty_projection_pp': [1, 3], 'decomposition_langs_showing_clean_separation_of_10': [4, 7], 'control_task_selectivity_deep_layers': [0.15, 0.25], 'cross_lingual_artifact_rate_pct': [15, 30], 'spearman_depth_vs_transfer_rho_positive_langs_of_20': [12, 17]}\n叙事方向：Empirical study + diagnostic negative result. CaCLR fails → reframe as 'the natural distributional-matching baseline fails; we explain why via CKA geometric analysis (MMD matches marginals but not low-dimensional directional subspace).' Claim 3 becomes systematic negative result with CORAL + high-dim MMD ablations closing the distributional-matching path. Claim 1 (Pareto) softened to 'architecture-dependent local tradeoff observed in MoE but weak in dense.' Claim 2 (decomposition) downgraded from quantitative to qualitative. Headline pivots to: 'Cross-lingual probe transfer reveals architecture-dependent depth effects; distributional matching fails but linear projection with ~100 pairs is the practical label-free solution.' Paper still holds for EACL: field-level viability test + negative result + practical solution + geometric insights. May need to compress Claim 2 to make space for stronger negative-result analysis.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions\n- Camera-ready extension: 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as \"principled scope\" not \"design limitation.\"\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method.\" Note: linear projection is \"the only label-free method that consistently improves over zero-shot across resource tiers\" — NOT \"only viable path.\" Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive. CORAL COMPARISON\n    (D015, re-dream 2-tier consensus): Add CORAL loss (second-order alignment, Sun\n    & Saenko 2016) as alternative to MMD. Tests whether distributional matching failure\n    is MMD-specific or general. Trivial to implement on cached activations. Report\n    CORAL alongside MMD in Table 7 ablation. Strengthens negative result scope. HIGH-DIM\n    MMD (D016, dream #4 cross-tier consensus): All 3 tiers flagged \"1-D logit MMD\"\n    as overclaimed scope. Test MMD on PCA-reduced activations (d=50, d=100) instead\n    of 1-D probe logits. If high-dim also fails → broadens \"distributional matching\n    fails\" claim. If high-dim works → method contribution jumps significantly. Trivial:\n    PCA on cached activations, then MMD in reduced space. Also test with CORAL in\n    high-dim. MULTI-SEED (D016): Run 3-5 seeds for CaCLR, few-shot (25/100), and Procrustes\n    at representative layers. Report std across seeds. Addresses single-seed concern.\n    MIXED β CRITERION (D016): Add 1-2 validation languages (zh, sw) to β selection\n    criterion alongside English, to rule out systematic bias against cross-lingual\n    benefit.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  registry_id: plan_013\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique. SELECTIVITY THRESHOLD\n    SENSITIVITY (D015): Test at 0.03, 0.05, 0.10 thresholds (Hewitt & Liang used 0.05\n    for English syntactic probing; may not be appropriate for multilingual correctness).\n    Report artifact rate at each threshold. Trivial to compute from existing data\n    (plan_013 v2 already running).\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 32.7B Dense (60 text layers, dense, BF16): third architecture\n    for core submission. Full Pareto frontier at every 4th layer + final (16 probed\n    layers), 20 languages, 5 transfer conditions. BF16 (~62.5GB, fits single 96GB\n    GPU). Provides dense vs MoE architectural contrast — addresses #1 reviewer concern\n    across ALL dream tiers (\"architecture comparison confounded\").\n\n    '\n  priority: P0\n  gpu_budget_hours: 30\n  deps: []\n  notes: 'Upgraded P2→P0 (D016). User providing 4× RTX 6000 96G on second server.\n    Model: google/gemma-4-31B (HF) / ModelScope. Apache 2.0, no gating. MULTIMODAL:\n    has vision encoder (27 extra layers) — extract_activations.py must hook ONLY text\n    decoder layers (60 layers), skip vision. Code may need adjustment. BF16 ~62.5GB\n    (2 shards: 49.8 + 12.8GB), single 96GB GPU sufficient. No quantization needed\n    — eliminates quantization confound for this model.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- exp_id: plan_013_probing_controls_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002_4gpu\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:43:06.670Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:43:06.670Z",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-21T12:43:06.689Z_

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
  "promptId": "9df3d60e-882e-47fc-8b7b-582bd933166a",
  "type": "user",
  "uuid": "f1b06d74-022d-448e-98fc-039affe62b58",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:43:06.688Z_

```json
{
  "parentUuid": "f1b06d74-022d-448e-98fc-039affe62b58",
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
  "uuid": "598dc69f-5a3e-4252-81bf-b8475ba0c166",
  "timestamp": "2026-05-21T12:43:06.688Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:43:06.688Z_

```json
{
  "parentUuid": "598dc69f-5a3e-4252-81bf-b8475ba0c166",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bff7497a-4134-4e65-b168-fce51f6b8571",
  "timestamp": "2026-05-21T12:43:06.688Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
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
  "leafUuid": "bff7497a-4134-4e65-b168-fce51f6b8571",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median outcome: Pareto-CKA analysis with CaCLR negative result",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:43:10.282Z_

I'll analyze the experiment plan and generate detailed median-tier predictions. Let me first review any existing files for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bff7497a-4134-4e65-b168-fce51f6b8571",
  "isSidechain": false,
  "requestId": "req_011CbFjVV4RMmmqrB6DV9MTr",
  "type": "assistant",
  "uuid": "af90edaa-74fa-46bd-b731-6837f5adeb92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KX1hUbPUU1A7HMYwFqVTL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18900,
      "cache_read_input_tokens": 11841,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 116,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18900
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

_source line 9 · 2026-05-21T12:43:11.288Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QDZLRU5tFhbWWY7JWJYBF3`</summary>

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
  "parentUuid": "af90edaa-74fa-46bd-b731-6837f5adeb92",
  "isSidechain": false,
  "requestId": "req_011CbFjVV4RMmmqrB6DV9MTr",
  "type": "assistant",
  "uuid": "38d2ee11-90a9-4e80-b1f8-e8a3da70ae10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KX1hUbPUU1A7HMYwFqVTL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18900,
      "cache_read_input_tokens": 11841,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 116,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18900
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

_source line 10 · 2026-05-21T12:43:11.307Z_

<details><summary>↩ Tool result · `toolu_01QDZLRU5tFhbWWY7JWJYBF3`</summary>

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
projects/xling_calib_direction/registry.yaml
projects/xling_calib_direction/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38d2ee11-90a9-4e80-b1f8-e8a3da70ae10",
  "isSidechain": false,
  "promptId": "9df3d60e-882e-47fc-8b7b-582bd933166a",
  "type": "user",
  "uuid": "57e58e42-ffeb-43bf-9790-89d6062b6c47",
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
      "projects/xling_calib_direction/registry.yaml",
      "projects/xling_calib_direction/experiment_plan.yaml"
    ],
    "durationMs": 12,
    "numFiles": 64,
    "truncated": false
  },
  "sourceToolAssistantUUID": "38d2ee11-90a9-4e80-b1f8-e8a3da70ae10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T12:43:13.969Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NRMGRijzWo16M95bXzCWFp`</summary>

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
  "parentUuid": "57e58e42-ffeb-43bf-9790-89d6062b6c47",
  "isSidechain": false,
  "requestId": "req_011CbFjVpn5vXnPCjSwtqQ68",
  "type": "assistant",
  "uuid": "37115dc8-a799-472e-8c8f-4a35885468d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrMXvzFTKGNzYWN27ymiNb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1623,
      "cache_read_input_tokens": 30741,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 30741,
          "cache_creation_input_tokens": 1623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1623
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

_source line 12 · 2026-05-21T12:43:13.977Z_

<details><summary>↩ Tool result · `toolu_01NRMGRijzWo16M95bXzCWFp`</summary>

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
  "parentUuid": "37115dc8-a799-472e-8c8f-4a35885468d2",
  "isSidechain": false,
  "promptId": "9df3d60e-882e-47fc-8b7b-582bd933166a",
  "type": "user",
  "uuid": "6cfa0687-969e-4712-b0bc-58c23fedaa3d",
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
  "sourceToolAssistantUUID": "37115dc8-a799-472e-8c8f-4a35885468d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T12:43:14.224Z_

<details open><summary>🔧 Tool call — Read · `toolu_019HsW1FpU2fcYhYsnZdCxvZ`</summary>

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
  "parentUuid": "6cfa0687-969e-4712-b0bc-58c23fedaa3d",
  "isSidechain": false,
  "requestId": "req_011CbFjVpn5vXnPCjSwtqQ68",
  "type": "assistant",
  "uuid": "f31c180b-f9f1-46c8-8fb5-cf87e8fab8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrMXvzFTKGNzYWN27ymiNb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1623,
      "cache_read_input_tokens": 30741,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 30741,
          "cache_creation_input_tokens": 1623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1623
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

_source line 14 · 2026-05-21T12:43:14.230Z_

<details><summary>↩ Tool result · `toolu_019HsW1FpU2fcYhYsnZdCxvZ`</summary>

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
428	    status: PREPARING
429	    retry_count: 0
430	    created_at: '2026-05-21T12:24:23.888Z'
431	    updated_at: '2026-05-21T12:26:41.717Z'
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
442	        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache
443	        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1
444	        && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /root/xling_calib_direction
445	        && python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/
446	        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47
447	        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir
448	        /root/autodl-tmp/activations/llama4_scout/"
449	      server: westd-13176
450	      gpu:
451	      - cuda:0
452	      - cuda:1
453	      - cuda:2
454	      - cuda:3
455	      pid: '934594'
456	      log_path: ~/runs/xling_calib_direction/plan_002_v3.log
457	      submitted_at: '2026-05-21T12:26:41.691Z'
458	      submitted_via: submit_training_job
459	      backend: tmux
460	      account: root
461	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f31c180b-f9f1-46c8-8fb5-cf87e8fab8c9",
  "isSidechain": false,
  "promptId": "9df3d60e-882e-47fc-8b7b-582bd933166a",
  "type": "user",
  "uuid": "27d2dcb9-8a45-4f02-989e-41902708c176",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml",
      "content": "baseline: null\nexperiments:\n  mvp_001:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T14:17:02.273Z'\n    updated_at: '2026-05-20T20:26:56.163Z'\n    hypothesis: 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性\n      probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在\n      layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp\n      for ≥3/5 语言）。\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/xling_calib_direction && bash run_mvp.sh\"\n      server: westd-13176\n      gpu:\n      - cuda:0\n      pid: '9845'\n      log_path: ~/runs/xling_calib_direction/mvp_001.log\n      submitted_at: '2026-05-20T16:29:25.456Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 6824.1\n      gpu_hours: 1.9\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7541\n      en_best_layer: 27\n      en_best_ece_raw: 0.1951\n      temp_scaling_fixed:\n        L24:\n          T: 0.67\n          ECE_cal: 0.2205\n        L27:\n          T: 0.62\n          ECE_cal: 0.2216\n        note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens\n          ECE.\n      en_auroc_range:\n      - 0.6113\n      - 0.7541\n      layer_depth_delta: 0.1428\n      layers_tested:\n      - 0\n      - 4\n      - 8\n      - 12\n      - 16\n      - 20\n      - 24\n      - 27\n      zs_pass_langs:\n      - zh\n      - ar\n      - hi\n      - ko\n      zs_fail_langs:\n      - sw\n      best_zs_auroc:\n        zh: 0.686\n        ar: 0.651\n        hi: 0.652\n        ko: 0.648\n        sw: 0.56\n      mean_shift_delta_ece:\n        zh: -0.36\n        ar: -0.06\n        hi: 2.22\n        sw: 6.44\n        ko: 0.01\n      pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n        D006.\n      p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n      p2: PASS (4/5)\n      p3: PASS (14.28pp)\n      p4: FAIL (0/5, mean-shift no improvement)\n    checkpoint_path: /root/xling_calib_direction/probes/\n    log_path: /root/xling_calib_direction/results/summary.txt\n    completed_at: '2026-05-20T18:23:09.593Z'\n  mvp_002:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T16:26:27.143Z'\n    updated_at: '2026-05-20T19:29:01.161Z'\n    hypothesis: Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与\n      mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际\n      28 层，index 0-27）\n    parent: mvp_001\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/xling_calib_direction && bash run_mvp_002.sh\"\n      server: westd-13176\n      gpu:\n      - cuda:1\n      pid: '11397'\n      log_path: ~/runs/xling_calib_direction/mvp_002.log\n      submitted_at: '2026-05-20T17:01:16.028Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 6874.5\n      gpu_hours: 1.91\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7481\n      en_best_layer: 26\n      en_auroc_range:\n      - 0.6229\n      - 0.7481\n      layer_depth_delta: 0.1251\n      best_zs_auroc:\n        zh: 0.6774\n        ar: 0.6302\n        hi: 0.6068\n        sw: 0.5467\n        ko: 0.6678\n      best_zs_layer:\n        zh: 26\n        ar: 26\n        hi: 22\n        sw: 22\n        ko: 26\n      pass_fail:\n        P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n        P2_zs_auroc: PASS (4/5)\n        P3_layer_delta: PASS (12.51pp)\n        P4_mean_shift: FAIL (0/5, zero delta)\n        overall: PARTIAL\n    log_path: /root/xling_calib_direction/results_mvp002/summary.txt\n    checkpoint_path: /root/xling_calib_direction/probes_mvp002/\n    completed_at: '2026-05-20T18:55:50.484Z'\n  mvp_003:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T18:27:06.449Z'\n    updated_at: '2026-05-20T20:48:56.916Z'\n    hypothesis: 'Cross-lingual correctness direction is model-agnostic: an English-trained\n      linear probe on Llama-3.1-8B-Instruct internal representations will transfer\n      to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the\n      pattern observed in Qwen2.5-7B-Instruct (mvp_001).'\n    parent: mvp_001\n    spec:\n      command: CUDA_VISIBLE_DEVICES=2 bash /root/xling_calib_direction/run_mvp_003.sh\n      server: westd-13176\n      data_path: cais/mmlu + CohereForAI/Global-MMLU\n      data_count: ~14K test samples per language\n      model_name: LLM-Research/Meta-Llama-3.1-8B-Instruct (ModelScope)\n      seed: 42\n      gpu: cuda:2\n      tmux_session: mvp_003\n      log_path: /root/xling_calib_direction/mvp_003.log\n      checkpoint_source: LLM-Research/Meta-Llama-3.1-8B-Instruct\n      eval_data: cais/mmlu + CohereForAI/Global-MMLU\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7284\n      en_best_layer: 31\n      en_best_ece_raw: 0.2052\n      en_auroc_range:\n      - 0.6331\n      - 0.7284\n      layer_depth_delta: 0.0953\n      layers_tested:\n      - 0\n      - 4\n      - 8\n      - 12\n      - 16\n      - 20\n      - 24\n      - 28\n      - 31\n      best_zs_auroc:\n        zh: 0.64\n        ar: 0.6146\n        hi: 0.5935\n        ko: 0.6481\n        sw: 0.5838\n      best_zs_layer:\n        zh: 20\n        ar: 31\n        hi: 31\n        ko: 31\n        sw: 16\n      zs_pass_langs:\n      - zh\n      - ar\n      - hi\n      - ko\n      - sw\n      zs_fail_langs: []\n      pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n      note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n        P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n        is rank-invariant.'\n      cka_vs_degradation:\n        overall_rho: -0.3982\n        overall_p: 0.0068\n        per_lang:\n          ar:\n            rho: -0.2833\n            p: 0.46\n          hi:\n            rho: -0.6667\n            p: 0.0499\n          ko:\n            rho: 0.25\n            p: 0.5165\n          sw:\n            rho: -0.5833\n            p: 0.0992\n          zh:\n            rho: -0.4833\n            p: 0.1875\n    checkpoint_path: /root/xling_calib_direction/probes_mvp003/\n    log_path: /root/xling_calib_direction/results_mvp003/summary.txt\n    completed_at: '2026-05-20T20:34:43.102Z'\n  plan_013:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-21T00:39:58.089Z'\n    updated_at: '2026-05-21T00:59:20.023Z'\n    hypothesis: 'English correctness probes capture genuine linguistic signal: 5-fold\n      CV with PCA(100) dimensionality reduction shows real AUROC significantly above\n      permuted-label baseline (0.746 vs 0.484 at best layer), with selectivity (Hewitt\n      & Liang 2019) concentrated in later layers (L20-L27), confirming the probe is\n      not exploiting spurious high-dimensional correlations.'\n    parent: mvp_001\n    spec:\n      command: python probing_controls_v2.py (5-fold CV + PCA-100)\n      server: westd-13176\n      data_path: /root/xling_calib_direction/activations/layer*_en.pt\n      data_count: ~14K MMLU test samples\n      model_name: Qwen2.5-7B-Instruct (activations from mvp_001)\n      seed: 42\n      checkpoint_source: mvp_001 activations\n      eval_data: same activations, 5-fold CV\n    conclusion: success\n    metrics:\n      method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n      selectivity_hewitt_liang:\n        L0: 0.02\n        L4: 0.037\n        L8: 0.036\n        L12: 0.042\n        L16: 0.123\n        L20: 0.244\n        L24: 0.248\n        L27: 0.262\n      real_auroc:\n        L0: 0.501\n        L4: 0.524\n        L8: 0.529\n        L12: 0.53\n        L16: 0.615\n        L20: 0.733\n        L24: 0.738\n        L27: 0.746\n      permuted_auroc:\n        L0: 0.481\n        L4: 0.487\n        L8: 0.493\n        L12: 0.488\n        L16: 0.492\n        L20: 0.489\n        L24: 0.49\n        L27: 0.484\n      pca_variance_retained:\n        L0: 0.922\n        L4: 0.912\n        L8: 0.885\n        L12: 0.868\n        L16: 0.783\n        L20: 0.738\n        L24: 0.844\n        L27: 0.794\n      note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n        concentrated in L20-L27. PCA(100) retains 73-92% variance.\n    checkpoint_path: /root/xling_calib_direction/results/probing_controls.csv\n    log_path: /root/xling_calib_direction/results/probing_controls.csv\n    completed_at: '2026-05-21T00:59:20.023Z'\n  plan_013_probing_controls_v2:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-21T01:04:11.073Z'\n    updated_at: '2026-05-21T12:13:02.350Z'\n    conclusion: failed\n    spec:\n      command: python3 probing_controls_v2.py (PID 47972)\n      server: westd-13176\n      pid: 47972\n      data_path: /root/xling_calib_direction/data/globalmmlu\n      data_count: -1\n      model_name: Qwen2.5-7B-Instruct\n      seed: 42\n      note: 已产出 L0 结果，从 PREPARING 补正状态\n    completed_at: '2026-05-21T12:13:02.350Z'\n  plan_002:\n    status: DONE\n    retry_count: 3\n    created_at: '2026-05-21T11:46:06.605Z'\n    updated_at: '2026-05-21T12:01:45.355Z'\n    hypothesis: 'Cross-lingual correctness direction transfers across languages in\n      Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed\n      layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC\n      ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern\n      (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides\n      architectural contrast to dense Qwen models.'\n    server: westd-13176\n    gpu: cuda:0\n    account: root\n    reproduce:\n      server: westd-13176\n      gpu: cuda:0\n      started_at: '2026-05-21T11:47:17.654Z'\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache\n        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1\n        && cd /root/xling_calib_direction && python -u code/extract_activations.py\n        --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\"\n      finished_at: '2026-05-21T12:01:43.858Z'\n      training_hours: 0.24\n    failure_reason: 'CUDA OOM: CUDA out of memory. Tried to allocate 160.00 MiB. GPU\n      0 has a total capacity of 94.97 GiB of which 25.81 MiB is free. Including non-PyTorch\n      memory, this process has 94.94 GiB memory in use. Of the allocated memory 93.27\n      GiB is allocated by PyTorch, a'\n    completed_at: '2026-05-21T11:48:15.052Z'\n    extra:\n      hook_events:\n      - event: on_failed\n        action: agent\n        ts: '2026-05-21T11:48:16.350219+00:00'\n      - event: on_failed\n        action: agent\n        ts: '2026-05-21T11:54:20.808886+00:00'\n      - event: on_failed\n        action: agent\n        ts: '2026-05-21T12:01:45.990550+00:00'\n      previous_failure:\n        conclusion: failed\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache\n        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1\n        && cd /root/xling_calib_direction && python -u code/extract_activations.py\n        --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\"\n      server: westd-13176\n      gpu:\n      - cuda:0\n      pid: '477148'\n      log_path: ~/runs/xling_calib_direction/plan_002.log\n      submitted_at: '2026-05-21T11:58:12.099Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 212.4\n      gpu_hours: 0.06\n    pid: '477148'\n    log_path: ~/runs/xling_calib_direction/plan_002.log\n    conclusion: failed\n  plan_002_4gpu:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-21T12:06:14.731Z'\n    updated_at: '2026-05-21T12:24:23.098Z'\n    hypothesis: 'Cross-lingual correctness direction transfers across languages in\n      Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed\n      layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC\n      ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern\n      (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides\n      architectural contrast to dense Qwen models. Retry of plan_002 with 4 GPUs (single-GPU\n      OOM confirmed by dry-run).'\n    parent: plan_002\n    spec:\n      command: python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/...\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\n      server: westd-13176\n      gpu:\n      - cuda:0\n      - cuda:1\n      - cuda:2\n      - cuda:3\n      data_path: cais/mmlu + CohereForAI/Global-MMLU (cached at /root/autodl-tmp/.hf_cache)\n      data_count: ~14K test samples per language, 20 languages\n      model_name: RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16\n      seed: 42\n      note: '4-GPU required (single GPU OOM). 3 code fixes: AutoModelForImageTextToText,\n        language_model.model.layers, language_model.model.norm. Dry-run validated\n        66s/sample.'\n    server: westd-13176\n    gpu: cuda:0,cuda:1,cuda:2,cuda:3\n    account: root\n    pid: '468430'\n    log_path: ~/runs/xling_calib_direction/plan_002_4gpu.log\n    reproduce:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache\n        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1\n        && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /root/xling_calib_direction\n        && python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\"\n      finished_at: '2026-05-21T12:10:25.168Z'\n    failure_reason: 'CUDA OOM: CUDA out of memory. Tried to allocate 40.00 MiB. GPU\n      1 has a total capacity of 94.97 GiB of which 32.50 MiB is free. Process 482839\n      has 88.03 GiB memory in use. Including non-PyTorch memory, this process has\n      6.90 GiB memory in use. Of the allocated m'\n    conclusion: failed\n    completed_at: '2026-05-21T12:10:25.858Z'\n    extra:\n      hook_events:\n      - event: on_failed\n        action: agent\n        ts: '2026-05-21T12:10:27.165461+00:00'\n    notes: '根因纠正(Director): OOM 不是 compressed_tensors 解压问题，而是 Qwen3 dry run (PID 482839)\n      占着 GPU 1-3（88 GiB）。4卡 dry run 在 clean GPU 上是成功的。已 kill 482839 并重新提交 plan_002_v3。'\n  plan_002_v3:\n    status: PREPARING\n    retry_count: 0\n    created_at: '2026-05-21T12:24:23.888Z'\n    updated_at: '2026-05-21T12:26:41.717Z'\n    hypothesis: 'Cross-lingual correctness direction transfers across languages in\n      Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed\n      layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC\n      ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern\n      (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides\n      architectural contrast to dense Qwen models. Retry after killing Qwen3 dry run\n      (PID 482839) that was occupying GPU 1-3.'\n    parent: plan_002_4gpu\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache\n        && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1\n        && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /root/xling_calib_direction\n        && python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/\n        --model_name llama4_scout_w4a16 --layers 0,4,8,12,16,20,24,28,32,36,40,44,47\n        --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir\n        /root/autodl-tmp/activations/llama4_scout/\"\n      server: westd-13176\n      gpu:\n      - cuda:0\n      - cuda:1\n      - cuda:2\n      - cuda:3\n      pid: '934594'\n      log_path: ~/runs/xling_calib_direction/plan_002_v3.log\n      submitted_at: '2026-05-21T12:26:41.691Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n",
      "numLines": 461,
      "startLine": 1,
      "totalLines": 461
    }
  },
  "sourceToolAssistantUUID": "f31c180b-f9f1-46c8-8fb5-cf87e8fab8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-21T12:43:14.378Z_

````json
{
  "parentUuid": "27d2dcb9-8a45-4f02-989e-41902708c176",
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
  "uuid": "32200456-f991-404e-80f1-7010c0754ff9",
  "timestamp": "2026-05-21T12:43:14.378Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "32200456-f991-404e-80f1-7010c0754ff9",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Median outcome: Pareto-CKA analysis with CaCLR negative result",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

### Assistant

_source line 18 · 2026-05-21T12:43:18.741Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of all the planned experiments and the median tier definition. Let me also check the previous dream reports for median tier to see what was already generated, so I don't duplicate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32200456-f991-404e-80f1-7010c0754ff9",
  "isSidechain": false,
  "requestId": "req_011CbFjW3qu8RvzxiHioWmqZ",
  "type": "assistant",
  "uuid": "e1493058-de6f-4e86-805b-ee8eac6e0c4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBzEi8TYCzpj6mWh1pfHWj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17920,
      "cache_read_input_tokens": 32364,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 32364,
          "cache_creation_input_tokens": 17920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17920
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

_source line 19 · 2026-05-21T12:43:19.131Z_

Let me check the previous dream report for reference and the 20 languages list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1493058-de6f-4e86-805b-ee8eac6e0c4d",
  "isSidechain": false,
  "requestId": "req_011CbFjW3qu8RvzxiHioWmqZ",
  "type": "assistant",
  "uuid": "7f803592-3c1a-4c3d-b6fa-076e654991fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBzEi8TYCzpj6mWh1pfHWj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17920,
      "cache_read_input_tokens": 32364,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 32364,
          "cache_creation_input_tokens": 17920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17920
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

_source line 20 · 2026-05-21T12:43:20.582Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ThDp32eP4YD7qyreSst3gV`</summary>

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
  "parentUuid": "7f803592-3c1a-4c3d-b6fa-076e654991fa",
  "isSidechain": false,
  "requestId": "req_011CbFjW3qu8RvzxiHioWmqZ",
  "type": "assistant",
  "uuid": "db7475fc-57df-493b-9b56-c704240dc486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBzEi8TYCzpj6mWh1pfHWj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17920,
      "cache_read_input_tokens": 32364,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 32364,
          "cache_creation_input_tokens": 17920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17920
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

_source line 21 · 2026-05-21T12:43:20.911Z_

<details><summary>↩ Tool result · `toolu_01ThDp32eP4YD7qyreSst3gV`</summary>

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
  "parentUuid": "db7475fc-57df-493b-9b56-c704240dc486",
  "isSidechain": false,
  "promptId": "9df3d60e-882e-47fc-8b7b-582bd933166a",
  "type": "user",
  "uuid": "daa990e5-641f-4680-8521-2c5f65f7c057",
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
  "sourceToolAssistantUUID": "db7475fc-57df-493b-9b56-c704240dc486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "daa990e5-641f-4680-8521-2c5f65f7c057",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Median outcome: Pareto-CKA analysis with CaCLR negative result",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

### Assistant

_source line 24 · 2026-05-21T12:43:57.124Z_

<details><summary>Logged reasoning block</summary>

```text
I now have a very thorough understanding of the existing median tier dream report. The user is asking me to regenerate the median tier imagined experiments with detailed data and result_rationale for each planned experiment. Let me look at which experiments are "planned" status to make sure I cover all of them.

Looking at the experiment plan, the planned experiments are:
1. plan_001 - Qwen3-235B Pareto (planned)
2. plan_002 - Llama 4 Scout Pareto (planned, currently PREPARING as plan_002_v3)
3. plan_003 - CaCLR (planned)


4. plan_004 - Difficulty decomposition (planned)
5. plan_005 - Cross-lingual orthogonality (planned)
6. plan_006 - Probe complexity comparison (planned)
7. plan_007 - Additional benchmark evaluation (planned)
8. plan_008 - Gemma 4 31B Dense (planned)
9. plan_009 - Extended language coverage (planned)
10. plan_010 - Quantization validation (planned)
11. plan_011 - CKA analysis (planned)
12. plan_012 - Linear projection sensitivity (planned)

Plan_013 is already done, so I need to focus on regenerating the detailed data and rationales for plans 001 through 012.

The three MVPs are complete, so now I'm working on generating median-tier predictions for each planned experiment. The user wants me to expand on the experiment_plan with detailed data for every planned study. I have the median tier definition and pilot data to work from, so I should construct comprehensive YAML predictions calibrated to those metric ranges. Let me build out the full predictions for all planned experiments with careful attention to the median tier thresholds.

Writing detailed experiment predictions... Now I'm looking at additional performance metrics across different transfer learning approaches—examining how contrastive learning and linear projection methods perform on low-resource languages, along with measures of cross-lingual artifacts and the relationship between model depth and transfer success.

The linear regression approach didn't yield positive results, so I'm treating that as architecture-dependent rather than a universal finding. The decomposition analysis is shifting to a more qualitative assessment, and linear projection with around a hundred language pairs seems like the most practical direction forward. I'm working through the consistency constraints for the median tier—ensuring the English AUROC stays in the expected range across different model architectures, keeping zero-shot pass rates between 12 and 16 languages, and maintaining alignment with the AUROC drop metrics I've already outlined. Looking at the remaining metrics from the analysis—decomposition improvements, control task selectivity, artifact rates, and correlation patterns across languages—I'm now ready to compile this into a comprehensive YAML document that captures all the empirical findings. I need to make sure I integrate plan_003's additional components around CORAL comparisons, high-dimensional MMD analysis, and multi-seed validation, since these are crucial for contextualizing the negative results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daa990e5-641f-4680-8521-2c5f65f7c057",
  "isSidechain": false,
  "requestId": "req_011CbFjWY2Yr5UQ4eDkXHfHb",
  "type": "assistant",
  "uuid": "22716d35-7b6a-4b27-9c9d-3f143b1d83c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171WhNsehx8tiXBzvEU9RNr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24912,
      "cache_read_input_tokens": 50284,
      "output_tokens": 29089,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24912,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 29089,
          "cache_read_input_tokens": 50284,
          "cache_creation_input_tokens": 24912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24912
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

_source line 25 · 2026-05-21T12:52:23.793Z_

Now I have full context. Let me generate the comprehensive median-tier imagined experiments.

```yaml
tier: median
narrative_guidance: >
  CaCLR consistency loss (MMD) 在 β sweep 跨 3 OOM 中无统计显著 AUROC 提升，
  CORAL 和 high-dim MMD 消融均失败，distributional matching 路径彻底关闭。
  几何解释：MMD 匹配边际分布但无法对齐低维 directional subspace——correctness
  方向在 activation 空间中占据 1-3 维子空间，旋转角度（HIGH ~11°, LOW ~43°）
  决定迁移质量，MMD 对旋转结构盲目。Linear projection 直接学习旋转故成功。
  Simpson's Paradox 在 Llama 4 Scout 上显著（partial rho~0.28, p~0.02），
  Qwen3-235B 上 trending 但不显著（rho~0.17, p~0.06）——Gemma 4 Dense 上
  边缘显著（rho~0.23, p~0.04），最终 2/3 架构确认。Pareto tradeoff 架构依赖：
  Qwen3 MoE 最强（CKA cliff 陡峭），Llama4 MoE 最弱（CKA decline 渐进），
  Gemma4 Dense 居中。Claim 2 decomposition 定性分离成立（6/10 languages
  clean separation）但 prescriptive accuracy ~60%，弱化为 descriptive。
  标题：'Cross-Lingual Correctness Probe Transfer: Architecture-Dependent
  Depth Effects, a Systematic Negative Result for Distributional Matching,
  and Practical Solutions via Linear Projection.'
  三个 actionable contributions: (1) linear projection ~90 pairs 推荐方案
  （LOW tier 需 ~100, HIGH 需 ~30），(2) Procrustes effect reversal 阈值
  ~0.55 作为 practitioner guidance，(3) 22% overall artifact rate 作为
  methodological warning（首次在 cross-lingual probing 中应用 selectivity
  checks）。仍可投 EACL：field-level viability test + 架构依赖几何洞见 +
  systematic negative result（MMD + CORAL + high-dim MMD 三路关闭）+ 实用指导。
  需压缩 Claim 2 为半页 subsection，腾出空间给更强的 negative-result 消融表。

imagined_experiments:
  - name: "Full Pareto Frontier — Qwen3-235B-A22B (MoE, INT4)"
    plan_id: "plan_001"
    description: >
      94 层 MoE 模型，每 4 层取一层（24 probed layers），20 种语言，train
      English correctness probes (LR + 2-layer MLP)，evaluate 5 transfer
      conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,
      CaCLR)。MoE 路由机制在深层创建语言特异化 expert 激活模式，
      产生比 7B pilot 更清晰但仍有噪声的 Pareto tradeoff。
      register_forward_hook 逐层提取 activation，避免 94 层同时输出 OOM。
    expected_results:
      en_best_auroc: 0.79
      en_best_layer: L80
      en_best_layer_depth_pct: 0.851
      en_auroc_range: [0.57, 0.79]
      en_best_ece_raw: 0.182
      layer_depth_delta_pp: 22.0
      transfer_optimal_layer_mean: L68
      transfer_optimal_depth_pct: 0.723
      en_vs_transfer_optimal_gap_pp: 2.5
      zs_pass_count_of_20: 15
      zs_pass_rate: 0.75
      zs_mean_auroc_at_en_optimal: 0.665
      zs_mean_auroc_at_transfer_optimal: 0.685
      zs_mean_auroc_drop_vs_en_pp: 12.5
      pareto_langs_with_negative_depth_transfer_rho: 16
      pareto_significant_negative_rho_langs: 10
      pareto_spearman_rho_median: -0.40
      pareto_spearman_rho_range: [-0.65, 0.20]
      pareto_depth_transfer_drop_final_layers_pp: 2.5
      best_zs_auroc_by_tier:
        HIGH_mean: 0.722  # zh/es/fr/de/pt/ja
        MID_mean: 0.670   # ar/ru/ko/hi/vi/tr
        LOW_mean: 0.572   # sw/bn/te/th/yo/am/id/nl — 取决于 20 语言定义
      best_zs_auroc_per_lang:
        zh: 0.735
        es: 0.740
        fr: 0.738
        de: 0.718
        pt: 0.728
        ja: 0.708
        ar: 0.692
        ru: 0.698
        ko: 0.682
        hi: 0.660
        vi: 0.675
        tr: 0.652
        sw: 0.588
        bn: 0.605
        te: 0.565
        id: 0.695
        pl: 0.708
        nl: 0.725
        uk: 0.690
        th: 0.618
      per_lang_pareto_rho:
        zh: {rho: -0.50, p: 0.012}
        es: {rho: -0.46, p: 0.023}
        fr: {rho: -0.44, p: 0.031}
        de: {rho: -0.53, p: 0.008}
        pt: {rho: -0.39, p: 0.058}
        ja: {rho: -0.56, p: 0.005}
        ar: {rho: -0.48, p: 0.018}
        ru: {rho: -0.42, p: 0.040}
        ko: {rho: -0.45, p: 0.027}
        hi: {rho: -0.36, p: 0.082}
        vi: {rho: -0.40, p: 0.052}
        tr: {rho: -0.33, p: 0.114}
        sw: {rho: -0.28, p: 0.185}
        bn: {rho: -0.30, p: 0.153}
        te: {rho: -0.20, p: 0.348}
        id: {rho: -0.44, p: 0.031}
        pl: {rho: -0.47, p: 0.021}
        nl: {rho: -0.41, p: 0.047}
        uk: {rho: -0.38, p: 0.068}
        th: {rho: 0.12, p: 0.575}
      mean_shift_delta_auroc: 0.000
      linear_proj_50_mean_auroc: 0.680
      linear_proj_200_mean_auroc: 0.695
      few_shot_25_mean_auroc: 0.680
      few_shot_100_mean_auroc: 0.715
    result_rationale: >
      Qwen3-235B 的 22B active MoE 参数量约为 pilot Qwen2.5-7B 的 3 倍。
      EN AUROC 从 pilot 的 0.754 提升至 ~0.79，符合 scaling 预期但非线性
      增长——correctness signal strength 随模型规模 log-linear 增长，
      3× 参数量预期 ~3-5pp 提升。EN-optimal 层在 L80（85% depth），
      而非最终层 L92——MoE 最终层的 expert routing 过度特化（shared expert
      比例下降），probe 拟合到模型内部的 task-routing metadata 而非 correctness
      signal。

      Pareto tradeoff 比 7B pilot 更清晰但不是所有语言都显著。
      MoE 路由机制在 L64-L80 区间加速语言特异化（不同语言激活不同 expert
      子集），CKA 在此区间急剧下降（cliff onset ~68% depth），
      导致 transfer-optimal（L68）与 EN-optimal（L80）之间产生 ~2.5pp gap。
      16/20 语言 depth-transfer rho 为负（深度增加 → transfer 降低），
      但仅 10 个在 p<0.05 显著——power limitation（每种语言 24 层，
      n=24 的 Spearman 检验 power 有限）。th 出现正 rho（非显著），
      因为 Thai 在 Qwen3 训练数据中代表性较低，深层的 expert specialization
      反而比浅层的 random noise 更有信息量。

      ZS pass rate 75%（15/20 AUROC>0.58）: HIGH 6/6 全通过，
      MID 6/8 通过（hi 和 tr 接近阈值但通过），LOW 3/6 通过
      （te/yo/am 低于 0.58，缺乏足够训练数据使 correctness direction
      在 activation 空间中形成）。Mean-shift 恒等于 0（数学不变性：
      StandardScaler + LR 下 mean-shift 只添加常数 offset，
      AUROC 是 rank metric）。Few-shot 100 提供最高 AUROC（0.715）
      因为它直接在 target 语言 correctness signal 上训练，
      但需要 100 个 correctness labels——与 zero-label 设定不符。
      Linear projection 在 50-200 pairs 范围内提供 label-free 的
      最佳 balance。
    tables:
      - name: "Table 1: Per-Language ZS AUROC at Transfer-Optimal (L68) vs EN-Optimal (L80)"
        data: |
          | Tier | Lang | ZS@L68 | ZS@L80 | Δ(L80-L68) | Pareto ρ | p     |
          |------|------|--------|--------|------------|----------|-------|
          | HIGH | zh   | 0.735  | 0.718  | -0.017     | -0.50    | 0.012 |
          | HIGH | es   | 0.740  | 0.725  | -0.015     | -0.46    | 0.023 |
          | HIGH | fr   | 0.738  | 0.722  | -0.016     | -0.44    | 0.031 |
          | HIGH | de   | 0.718  | 0.700  | -0.018     | -0.53    | 0.008 |
          | HIGH | pt   | 0.728  | 0.715  | -0.013     | -0.39    | 0.058 |
          | HIGH | ja   | 0.708  | 0.688  | -0.020     | -0.56    | 0.005 |
          | MID  | ar   | 0.692  | 0.678  | -0.014     | -0.48    | 0.018 |
          | MID  | ru   | 0.698  | 0.685  | -0.013     | -0.42    | 0.040 |
          | MID  | ko   | 0.682  | 0.668  | -0.014     | -0.45    | 0.027 |
          | MID  | hi   | 0.660  | 0.650  | -0.010     | -0.36    | 0.082 |
          | MID  | vi   | 0.675  | 0.665  | -0.010     | -0.40    | 0.052 |
          | MID  | tr   | 0.652  | 0.645  | -0.007     | -0.33    | 0.114 |
          | LOW  | sw   | 0.588  | 0.578  | -0.010     | -0.28    | 0.185 |
          | LOW  | bn   | 0.605  | 0.595  | -0.010     | -0.30    | 0.153 |
          | LOW  | te   | 0.565  | 0.558  | -0.007     | -0.20    | 0.348 |
          | LOW  | th   | 0.610  | 0.618  | +0.008     | +0.12    | 0.575 |
          | LOW  | id   | 0.695  | 0.685  | -0.010     | -0.44    | 0.031 |
          | MID  | pl   | 0.708  | 0.695  | -0.013     | -0.47    | 0.021 |
          | HIGH | nl   | 0.725  | 0.712  | -0.013     | -0.41    | 0.047 |
          | MID  | uk   | 0.690  | 0.680  | -0.010     | -0.38    | 0.068 |
      - name: "Table 2: Transfer Method Comparison (mean 20 langs, EN-optimal L80)"
        data: |
          | Method             | Mean AUROC | Δ vs ZS  | p (perm) | Req.       |
          |--------------------|------------|----------|----------|------------|
          | Zero-shot          | 0.665      | —        | —        | 0 labels   |
          | Mean-shift         | 0.665      | +0.000   | n/a      | 0 labels   |
          | CaCLR (best β=0.01)| 0.667      | +0.002   | 0.45     | 0 labels   |
          | Linear proj (50)   | 0.680      | +0.015   | 0.012    | 50 pairs   |
          | Linear proj (200)  | 0.695      | +0.030   | <0.001   | 200 pairs  |
          | Few-shot 25        | 0.680      | +0.015   | 0.009    | 25 labels  |
          | Few-shot 100       | 0.715      | +0.050   | <0.001   | 100 labels |
    figures_description:
      - >
        Pareto scatter grid (4×5): 20 子图按 tier 分行（HIGH/MID/LOW/Mixed），
        每子图 x=EN AUROC, y=ZS AUROC，24 个 probed layer 为点，
        颜色编码 normalized depth（浅蓝→深红）。Pareto frontier 虚线连接。
        HIGH 语言子图显示清晰右下弯折（L68-L80 EN 增加但 ZS 下降），
        LOW 语言点聚集左下、frontier 几乎平坦。th 子图 frontier 向右上延伸（无 tradeoff）。
      - >
        Layer-wise AUROC heatmap: x=20 languages（按 mean ZS AUROC 排序），
        y=24 layers（按深度）。颜色=ZS AUROC (diverging colormap: 红=高, 蓝=低)。
        EN 列单独显示单调递增。右下区域（深层+低资源）呈冷色，
        左中区域（中层+高资源）呈暖色。水平虚线标注 transfer-optimal depth。
    analysis: >
      Qwen3-235B 的 MoE 架构在 3 个模型中产生最强 Pareto frontier：
      median per-language rho=-0.40，10/20 在 p<0.05 显著。
      Pareto 强度与 resource tier 相关但不完美
      （HIGH rho median=-0.48, MID=-0.40, LOW=-0.26）——
      LOW 语言整体 AUROC 方差小，depth variation 被 noise 淹没。
      EN-optimal（L80）vs transfer-optimal（L68）的 ~2.5pp gap
      为部署提供 layer selection guidance：如果服务非英语用户，
      L68 是更优选择（牺牲 ~1pp EN 质量换取 ~1.5-2.5pp 跨语言改善）。
      MoE 的 expert routing 加速了深层特异化——L64-L80 的 shared expert
      使用率从 ~40% 降到 ~15%（推测，无法直接测量 routing statistics），
      解释了 CKA cliff 和 transfer cliff 的同步出现。

  - name: "Full Pareto Frontier — Llama 4 Scout (MoE, W4A16)"
    plan_id: "plan_002"
    description: >
      48 层 17B-16E MoE（W4A16 量化），每 4 层取一层（13 probed layers: 
      0,4,8,12,16,20,24,28,32,36,40,44,47），20 语言，5 transfer 条件。
      Llama 架构族在 pilot 中显示弱 Pareto（仅 2/5 语言有 depth-transfer tradeoff），
      full-scale 预期延续此弱模式，MoE 16-expert 架构的 CKA decline 更渐进。
    expected_results:
      en_best_auroc: 0.765
      en_best_layer: L44
      en_best_layer_depth_pct: 0.917
      en_auroc_range: [0.60, 0.765]
      en_best_ece_raw: 0.192
      layer_depth_delta_pp: 16.5
      transfer_optimal_layer_mean: L36
      transfer_optimal_depth_pct: 0.75
      en_vs_transfer_optimal_gap_pp: 1.2
      zs_pass_count_of_20: 14
      zs_pass_rate: 0.70
      zs_mean_auroc_at_en_optimal: 0.648
      zs_mean_auroc_at_transfer_optimal: 0.658
      zs_mean_auroc_drop_vs_en_pp: 11.7
      pareto_langs_with_negative_depth_transfer_rho: 13
      pareto_significant_negative_rho_langs: 6
      pareto_spearman_rho_median: -0.26
      pareto_spearman_rho_range: [-0.52, 0.38]
      pareto_depth_transfer_drop_final_layers_pp: 1.2
      best_zs_auroc_by_tier:
        HIGH_mean: 0.705
        MID_mean: 0.655
        LOW_mean: 0.555
      best_zs_auroc_per_lang:
        zh: 0.710
        es: 0.718
        fr: 0.715
        de: 0.700
        pt: 0.708
        ja: 0.690
        ar: 0.672
        ru: 0.680
        ko: 0.668
        hi: 0.640
        vi: 0.655
        tr: 0.635
        sw: 0.578
        bn: 0.580
        te: 0.545
        id: 0.680
        pl: 0.695
        nl: 0.710
        uk: 0.672
        th: 0.598
      per_lang_pareto_rho:
        zh: {rho: -0.38, p: 0.198}
        es: {rho: -0.33, p: 0.270}
        fr: {rho: -0.30, p: 0.318}
        de: {rho: -0.42, p: 0.154}
        ja: {rho: -0.45, p: 0.124}
        ar: {rho: +0.18, p: 0.556}
        ru: {rho: -0.35, p: 0.241}
        ko: {rho: +0.25, p: 0.410}
        hi: {rho: -0.52, p: 0.068}
        vi: {rho: -0.30, p: 0.318}
        tr: {rho: -0.22, p: 0.472}
        sw: {rho: -0.20, p: 0.512}
        bn: {rho: -0.28, p: 0.355}
        te: {rho: -0.15, p: 0.625}
        id: {rho: -0.40, p: 0.176}
        pt: {rho: -0.32, p: 0.285}
        pl: {rho: -0.38, p: 0.198}
        nl: {rho: -0.35, p: 0.241}
        uk: {rho: -0.30, p: 0.318}
        th: {rho: +0.08, p: 0.795}
      mean_shift_delta_auroc: 0.000
      linear_proj_50_mean_auroc: 0.663
      linear_proj_200_mean_auroc: 0.678
      few_shot_25_mean_auroc: 0.665
      few_shot_100_mean_auroc: 0.698
    result_rationale: >
      Llama 4 Scout 延续 Llama-3.1-8B pilot 的弱 Pareto 模式。
      Pilot 中仅 2/5 语言显示 depth-transfer tradeoff（ar/ko 随深度改善），
      full-scale 中约 7/20 语言不显示 tradeoff 或方向相反。

      根本原因在于 CKA depth gradient 的形状差异。Llama 4 的 CKA decline
      从 ~50% depth 就开始渐进下降（slope ~-0.013/layer），没有 Qwen3 那样的
      急剧 cliff。这意味着 transfer quality 随深度的变化分散在更宽的层范围内，
      而非集中在最深层——Pareto tradeoff 被拉平了。EN-optimal（L44）与
      transfer-optimal（L36）gap 仅 ~1.2pp，远小于 Qwen3 的 ~2.5pp。

      EN AUROC 从 pilot Llama-3.1-8B 的 0.728 提升至 ~0.765（17B active
      params vs 8B），但提升幅度小于 Qwen3 的 scaling，因为 Llama 4 的
      16-expert MoE 在浅层就开始 expert specialization——correctness signal
      在中层（L20-L28）已经 plateau，后续提升主要来自 EN-specific pattern
      而非 language-agnostic correctness direction。

      ar 和 ko 的正 rho（非显著）延续了 pilot 发现：这两种语言在 Llama 4
      tokenizer 中有较好的 subword coverage，深层 expert specialization
      反而增强了 correctness signal——与 Qwen3 上的行为截然不同。
      这确认了 Pareto 的架构依赖性。

      Pareto significance 仅 6/20 语言在 p<0.05 显著——n=13（13 probed layers）
      的 Spearman 检验 power 比 Qwen3（n=24）更低，加上 tradeoff 本身就弱，
      大多数 per-language rho 虽为负但不显著。
    tables:
      - name: "Table 3: Architecture Pareto Strength Comparison"
        data: |
          | Metric                          | Qwen3-235B (MoE) | Llama4 Scout (MoE) |
          |---------------------------------|-------------------|--------------------|
          | EN best AUROC                   | 0.79              | 0.765              |
          | Mean ZS AUROC (EN-opt layer)    | 0.665             | 0.648              |
          | EN-opt vs Transfer-opt gap (pp) | 2.5               | 1.2                |
          | Langs with negative Pareto ρ    | 16/20             | 13/20              |
          | Langs with sig negative ρ       | 10/20             | 6/20               |
          | Median per-lang Pareto ρ        | -0.40             | -0.26              |
          | CKA cliff onset (% depth)       | ~68%              | ~50%               |
          | CKA cliff slope                 | -0.023/layer      | -0.013/layer       |
      - name: "Table 4: Divergent Languages (opposite Pareto direction)"
        data: |
          | Lang | Qwen3 ρ | Qwen3 p | Llama4 ρ | Llama4 p | Interpretation          |
          |------|---------|---------|----------|----------|-------------------------|
          | ar   | -0.48   | 0.018   | +0.18    | 0.556    | Architecture-divergent  |
          | ko   | -0.45   | 0.027   | +0.25    | 0.410    | Architecture-divergent  |
          | th   | +0.12   | 0.575   | +0.08    | 0.795    | No tradeoff on either   |
    figures_description:
      - >
        双模型 Pareto 对比图：左列 Qwen3-235B（24 layers），右列 Llama4 Scout（13 layers）。
        三行对应 HIGH/MID/LOW tier。每子图叠加该 tier 所有语言 Pareto frontier（不同颜色）。
        Qwen3 列 frontier 弯折更尖锐（深层 EN 增加 ZS 急降），
        Llama4 列 frontier 更平缓（深层 EN 和 ZS 共同缓慢增加或平坦）。
        Inset 数字标注 median ρ 和 significant count。
    analysis: >
      两个 MoE 架构的 Pareto 差异确认了 pilot 的架构依赖性发现但加入了 nuance。
      关键驱动因子不是 MoE vs dense，而是 CKA depth gradient 的斜率和 onset timing：
      Qwen3 的 CKA 在 68% depth 后急降（-0.023/layer），Llama4 从 50% depth 
      就开始缓降（-0.013/layer）。Llama4 的 16-expert 架构在浅层就分散了
      specialization pressure，而 Qwen3 的 routing 更集中在深层。
      ar/ko 的架构级 divergence 是最有趣的发现——这些语言在两个架构上
      表现相反，但 n=2 架构不能做因果归因（混杂 tokenizer、training data、
      layer count）。Paper 中报告为 observational。

  - name: "Gemma 4 31B Dense — Third Architecture (Core Submission)"
    plan_id: "plan_008"
    description: >
      Dense 架构对照（vs 两个 MoE），60 text layers（跳过 27 vision layers），
      BF16 无量化，16 probed layers（每 4 层 + final），20 语言，5 transfer 条件。
      提供 dense vs MoE 架构对比，地位从 P2 升至 P0。
      消除量化 confound（唯一 FP16/BF16 模型）。
    expected_results:
      en_best_auroc: 0.775
      en_best_layer: L52
      en_best_layer_depth_pct: 0.867
      en_auroc_range: [0.58, 0.775]
      en_best_ece_raw: 0.188
      transfer_optimal_layer_mean: L44
      transfer_optimal_depth_pct: 0.733
      en_vs_transfer_optimal_gap_pp: 1.8
      zs_pass_count_of_20: 14
      zs_pass_rate: 0.70
      zs_mean_auroc_at_en_optimal: 0.655
      zs_mean_auroc_at_transfer_optimal: 0.670
      zs_mean_auroc_drop_vs_en_pp: 12.0
      pareto_langs_with_negative_depth_transfer_rho: 14
      pareto_significant_negative_rho_langs: 8
      pareto_spearman_rho_median: -0.34
      pareto_spearman_rho_range: [-0.58, 0.22]
      pareto_depth_transfer_drop_final_layers_pp: 1.8
      best_zs_auroc_by_tier:
        HIGH_mean: 0.715
        MID_mean: 0.660
        LOW_mean: 0.562
      cka_cliff_onset_depth_pct: 0.60
      cka_cliff_slope: -0.018
      partial_rho_cka_controlling_depth: 0.23
      partial_p_cka: 0.038
      simpson_paradox_significant: true
      mean_shift_delta_auroc: 0.000
      linear_proj_200_mean_auroc: 0.685
      few_shot_100_mean_auroc: 0.705
    result_rationale: >
      Gemma 4 31B Dense 的行为介于两个 MoE 之间，这是由 CKA depth profile
      的形状决定的。Dense 架构没有 expert routing 来加速深层特异化，
      CKA decline 比 Qwen3 MoE 更渐进（slope -0.018 vs -0.023），
      但比 Llama4 MoE 更陡（-0.018 vs -0.013）。这是因为 dense 架构的
      所有参数都参与每次 forward pass——没有 MoE 的 sparse routing
      来分散或集中 specialization。

      EN AUROC ~0.775 与 Qwen3 的 0.79 接近（31B dense vs 22B active MoE，
      dense 架构的参数利用率更高但 total capacity 受限），
      高于 Llama4 的 0.765（Gemma 4 在 MMLU-like benchmarks 上
      训练更充分——Google 的 instruction tuning 包含大量 knowledge-intensive QA）。

      Pareto 强度居中（median ρ=-0.34, 8/20 显著），
      在 MoE 的强（Qwen3）和弱（Llama4）之间。

      Simpson's Paradox 在 Gemma 4 上边缘显著（partial rho=0.23, p=0.038）——
      CKA gradient 斜率介于两个 MoE 之间，linear partial correlation 有效。
      这使得 Simpson's Paradox 变为 2/3 架构显著（Llama4 + Gemma4），
      Qwen3 trending——可以用更强的 hedged language 报告。

      无量化 confound 使 Gemma 4 成为最"干净"的 data point——
      如果 Qwen3 INT4 或 Llama4 W4A16 的结果有任何异常，
      可与 Gemma 4 BF16 交叉验证。
    tables:
      - name: "Table 5: Three-Architecture Comparison Summary"
        data: |
          | Metric                     | Qwen3-235B | Llama4 Scout | Gemma4 31B |
          |----------------------------|------------|--------------|------------|
          | Type                       | MoE        | MoE          | Dense      |
          | Active params              | 22B        | 17B          | 31B        |
          | Total layers               | 94         | 48           | 60         |
          | Quantization               | INT4       | W4A16        | BF16       |
          | EN best AUROC              | 0.79       | 0.765        | 0.775      |
          | Mean ZS AUROC              | 0.665      | 0.648        | 0.655      |
          | ZS pass rate               | 75%        | 70%          | 70%        |
          | Pareto sig langs (/20)     | 10         | 6            | 8          |
          | Median per-lang ρ          | -0.40      | -0.26        | -0.34      |
          | CKA cliff onset (% depth)  | ~68%       | ~50%         | ~60%       |
          | CKA cliff slope            | -0.023     | -0.013       | -0.018     |
          | Partial ρ (CKA ctrl depth) | 0.17 (ns)  | 0.28**       | 0.23*      |
          | EN-opt vs Xfer-opt gap pp  | 2.5        | 1.2          | 1.8        |
    figures_description:
      - >
        三架构 CKA depth profile：x=normalized depth (0-1), y=mean CKA (20 langs)。
        Qwen3 线先平后急降（L64 cliff），Llama4 线从 L24 渐降，
        Gemma4 线从 L36 中速下降。Vertical bands 标注 cliff onset。
        Inset text 标注 slope 和 partial ρ。
    analysis: >
      Gemma 4 作为 dense 对照消除了 MoE 作为 Pareto 唯一解释的可能——
      dense 架构也有 Pareto tradeoff，只是强度不同。
      三架构数据暗示 CKA cliff slope 可能是预测 Pareto 强度的
      单一最佳 proxy（slope ↑ → Pareto ↑），但 n=3 仅为 suggestive。
      Simpson's Paradox 2/3 显著，1/3 trending——比 1/3 更强的证据，
      纸面叙事可以用 "in 2/3 architectures, controlling for depth
      reveals a significant positive CKA-transfer relationship" 措辞。

  - name: "CaCLR Implementation and Systematic Negative Result"
    plan_id: "plan_003"
    description: >
      CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) 完整实现与评估。
      β sweep 跨 3 OOM (0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0)。
      α sweep (0.01, 0.1, 1.0, 10.0)。Component ablation。
      CORAL 消融（second-order alignment）。High-dim MMD (PCA d=50, d=100)。
      Multi-seed (5 seeds)。Mixed β criterion (zh, sw validation langs)。
      3 models × 20 languages × representative layers。
      Median tier: consistency loss 无效 → systematic negative result。
    expected_results:
      caclr_mean_delta_auroc_vs_zs_pp: 0.3
      caclr_mean_delta_auroc_range_pp: [-0.5, 1.0]
      caclr_best_beta: 0.01
      caclr_best_alpha: 0.3
      caclr_langs_improved_of_20: 8
      caclr_langs_hurt_of_20: 7
      caclr_langs_neutral_of_20: 5
      beta_sweep_qwen3:
        beta_0.001: {mean_delta_auroc_pp: 0.1, p_vs_zs: 0.78, ci_95: [-0.4, 0.6]}
        beta_0.003: {mean_delta_auroc_pp: 0.2, p_vs_zs: 0.62, ci_95: [-0.3, 0.7]}
        beta_0.01:  {mean_delta_auroc_pp: 0.3, p_vs_zs: 0.42, ci_95: [-0.3, 0.9]}
        beta_0.03:  {mean_delta_auroc_pp: 0.1, p_vs_zs: 0.72, ci_95: [-0.5, 0.7]}
        beta_0.1:   {mean_delta_auroc_pp: -0.2, p_vs_zs: 0.55, ci_95: [-0.8, 0.4]}
        beta_0.3:   {mean_delta_auroc_pp: -0.5, p_vs_zs: 0.18, ci_95: [-1.2, 0.2]}
        beta_1.0:   {mean_delta_auroc_pp: -1.2, p_vs_zs: 0.035, ci_95: [-2.0, -0.1]}
      alpha_sweep:
        alpha_0.01: {mean_delta_ece_pp: -0.2, mean_delta_auroc_pp: 0.0}
        alpha_0.1:  {mean_delta_ece_pp: -0.5, mean_delta_auroc_pp: -0.1}
        alpha_1.0:  {mean_delta_ece_pp: -1.8, mean_delta_auroc_pp: -0.5}
        alpha_10.0: {mean_delta_ece_pp: -2.2, mean_delta_auroc_pp: -1.5}
      component_ablation_qwen3:
        bce_only:     {auroc: 0.665, ece: 0.190}
        bce_sbece:    {auroc: 0.662, ece: 0.175}
        bce_mmd:      {auroc: 0.667, ece: 0.188}
        bce_sbece_mmd:{auroc: 0.665, ece: 0.174}
      coral_comparison:
        coral_mean_delta_auroc_pp: 0.2
        coral_p_vs_zs: 0.58
        coral_note: "CORAL (second-order) also inert — distributional matching failure is general, not MMD-specific"
      high_dim_mmd:
        pca_d50_mean_delta_pp: 0.4
        pca_d50_p: 0.38
        pca_d100_mean_delta_pp: 0.5
        pca_d100_p: 0.32
        coral_d50_mean_delta_pp: 0.3
        coral_d50_p: 0.45
        note: "High-dim variants also fail — broadens negative result scope beyond 1-D limitation"
      multi_seed_std:
        caclr_auroc_std: 0.003
        few_shot_25_auroc_std: 0.008
        few_shot_100_auroc_std: 0.005
        procrustes_auroc_std: 0.004
      mixed_beta_criterion:
        en_only_best_beta: 0.01
        mixed_best_beta: 0.003
        mixed_delta_vs_en_criterion: "negligible (0.1pp)"
      method_comparison_mean_20lang:
        zero_shot: 0.656
        mean_shift: 0.656
        caclr_best: 0.659
        coral_best: 0.658
        high_dim_mmd_best: 0.660
        linear_proj_50: 0.674
        linear_proj_100: 0.684
        linear_proj_200: 0.690
        few_shot_25: 0.675
        few_shot_100: 0.706
      implementation_spec:
        mmd_kernel: "Gaussian RBF, bandwidth via median heuristic"
        optimizer: "Adam, lr=1e-3, cosine schedule to 1e-5"
        epochs: 50
        early_stopping: "patience=10 on val BCE loss"
        initialization: "from standard LR solution (warm start)"
        batch_size: 256
        mmd_items: "same as BCE items (probe_train 70% split)"
        parallel_set_size_range: [8500, 12800]
    result_rationale: >
      CaCLR 的 MMD consistency loss 在 probe logit 空间（1-D）操作——
      这是根本性的 architectural limitation，而非 hyperparameter 问题。
      Correctness direction 是高维 activation 空间（d=3584 for Qwen3）中的
      低维子空间特征（~1-3 维）。两种语言的 probe logit 分布可以有相似的
      均值和方差（MMD 趋近 0），但 correctness direction 在 activation 空间中的
      朝向不同——MMD 对旋转结构完全盲目。

      β=0.001-0.01 时 MMD loss 太弱（loss landscape 由 BCE 主导），
      对 probe 参数几乎无影响——ΔAUROC 在 noise level 内波动（±0.3pp）。
      β=0.1-1.0 时 MMD loss 开始干扰 BCE 训练：强制匹配 probe logit
      边际分布会偏移 decision boundary 位置，破坏 EN probe 已学到的
      correctness direction。β=1.0 时 AUROC 显著下降 1.2pp——
      这不是 training failure，而是 MMD 成功匹配了边际分布但代价是
      correctness discrimination 能力的降低。

      CORAL（second-order alignment）也失败——它匹配的是 covariance structure，
      但 correctness direction 的旋转信息不在 marginal covariance 中，
      而在 cross-domain directional alignment 中。
      High-dim MMD (PCA d=50, d=100) 也失败——在 50-100 维的 PCA 空间中
      MMD 仍然只能匹配边际分布，无法对齐低维 correctness subspace 的方向。
      这彻底关闭了 distributional matching 路径（不仅是 1-D MMD，
      也不仅是 MMD 本身，而是整个 marginal/moment matching paradigm）。

      8/20 语言 CaCLR "改善"——但改善量级 < 1pp 且不显著，
      与随机波动一致（multi-seed std ~0.3pp）。
      Mixed β criterion（加入 zh, sw 验证语言）选择的 best β (0.003)
      与 EN-only criterion (0.01) 产生的结果无实质差异——
      排除了 β selection 系统性偏向 EN 的可能。

      对比鲜明：linear projection 以 50 parallel pairs 就实现了
      +1.8pp 显著改善（p=0.012），因为它直接学习 activation space 中的
      旋转矩阵（Procrustes alignment），绕过了 distributional matching 的
      根本局限。这一对比（MMD/CORAL/high-dim 全失败 vs linear projection 成功）
      是 Zhao et al. (2019) conditional-marginal mismatch theory 的
      最清晰实证验证。
    tables:
      - name: "Table 6: β Sweep Results (3 models mean, 20 languages, EN-optimal layer)"
        data: |
          | β     | Mean ΔAUROC (pp) | 95% Boot CI      | Cohen's d | p (perm) | Interpretation      |
          |-------|------------------|------------------|-----------|----------|---------------------|
          | 0     | —                | —                | —         | —        | ZS baseline         |
          | 0.001 | +0.1             | [-0.4, +0.6]     | 0.02      | 0.78     | Negligible          |
          | 0.003 | +0.2             | [-0.3, +0.7]     | 0.05      | 0.62     | Negligible          |
          | 0.01  | +0.3             | [-0.3, +0.9]     | 0.07      | 0.42     | Negligible          |
          | 0.03  | +0.1             | [-0.5, +0.7]     | 0.02      | 0.72     | Negligible          |
          | 0.1   | -0.2             | [-0.8, +0.4]     | 0.05      | 0.55     | Negligible          |
          | 0.3   | -0.5             | [-1.2, +0.2]     | 0.12      | 0.18     | Trending harm       |
          | 1.0   | -1.2             | [-2.0, -0.1]     | 0.28      | 0.035    | Significant harm    |
      - name: "Table 7: Distributional Matching Ablation (closing all paths)"
        data: |
          | Method                    | Space        | Mean Δ (pp) | p     | Path status  |
          |---------------------------|--------------|-------------|-------|--------------|
          | MMD (β=0.01)              | 1-D logit    | +0.3        | 0.42  | CLOSED       |
          | CORAL                     | 1-D logit    | +0.2        | 0.58  | CLOSED       |
          | MMD                       | PCA-50       | +0.4        | 0.38  | CLOSED       |
          | MMD                       | PCA-100      | +0.5        | 0.32  | CLOSED       |
          | CORAL                     | PCA-50       | +0.3        | 0.45  | CLOSED       |
          | Linear projection (50p)   | Full d       | +1.8        | 0.012 | VIABLE       |
          | Linear projection (200p)  | Full d       | +3.4        | <0.001| VIABLE       |
          | Few-shot 25               | —            | +1.9        | 0.009 | VIABLE       |
          | Few-shot 100              | —            | +5.0        | <0.001| VIABLE       |
      - name: "Table 8: CKA Subspace Analysis — Why Distributional Matching Fails"
        data: |
          | Lang Tier | Subspace angle (EN→target) | MMD before | MMD after | Angle after | CORAL after |
          |-----------|---------------------------|------------|-----------|-------------|-------------|
          | HIGH      | 11°                       | 0.025      | 0.008     | 10.5°       | 10.8°       |
          | MID       | 23°                       | 0.058      | 0.018     | 22.5°       | 22.8°       |
          | LOW       | 43°                       | 0.130      | 0.042     | 42.0°       | 42.5°       |
    figures_description:
      - >
        β sweep 图：x=β (log scale), y=ΔAUROC vs ZS (pp), 每条线一个 resource tier,
        shaded area 为 bootstrap 95% CI。所有线在 y=0 附近震荡，β≥0.3 时
        向下偏离。水平虚线标注 linear projection (50p) 和 few-shot 100 的
        ΔAUROC 作为 reference。标注 "distributional matching region" 和
        "direct alignment region"。
      - >
        几何解释概念图 (2-panel)：
        左：MMD 操作视角——2D 投影显示 EN（蓝）和 target（橙）logit 分布，
        MMD 将两个分布边际对齐（均值/方差匹配），但 correctness direction（箭头）
        指向不同方向，MMD 看不到这个旋转。
        右：Linear projection 视角——activation space 中 correctness subspace
        通过 Procrustes rotation 直接对齐，箭头方向一致化。
      - >
        Multi-method bar chart: x=7 methods, y=mean ΔAUROC (pp) vs ZS,
        error bars 为 multi-seed std。MMD/CORAL/high-dim 三簇在 0 附近，
        linear proj 和 few-shot 显著高于 0。清晰视觉对比。
    analysis: >
      CaCLR negative result 的核心贡献是三路关闭 distributional matching：
      (1) 1-D logit MMD 失败——设计层面的维度局限；
      (2) 1-D CORAL 失败——排除 MMD-specific failure；
      (3) High-dim MMD/CORAL (PCA-50/100) 也失败——排除维度局限解释。
      这三路加上 component ablation、multi-seed、mixed β criterion，
      构成了 systematic negative result 的完整证据链。

      几何解释简洁有力：distributional matching（无论 MMD 还是 CORAL，
      无论在什么维度）匹配的是边际/矩统计量，但 cross-lingual correctness
      transfer 的瓶颈是 directional alignment（subspace rotation）。
      CaCLR 成功减小了 MMD distance 但完全未改变 subspace angle——
      这正是 Zhao et al. (2019) 的理论预测在实践中的验证。
      Linear projection 成功因为它直接解决 rotation problem。

      Paper framing: CaCLR 不是 failed novel method，而是 natural baseline
      testing distributional matching hypothesis。Contribution 是
      saving the community from pursuing this path + geometric explanation
      + identifying linear projection as practical solution。

  - name: "Difficulty-Controlled Decomposition Ablation"
    plan_id: "plan_004"
    description: >
      IRT difficulty probes (Ridge regression) → project out difficulty direction →
      retrain correctness probes on residuals → evaluate transfer change。
      10 代表语言 (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) ×
      8 代表层 (20-90% depth uniform) × 3 models。
      含 random-direction control 排除 dimensionality-reduction artifact。
    expected_results:
      difficulty_probe_r2: 0.33
      mean_delta_auroc_after_projection_pp: 1.8
      delta_auroc_range_pp: [-1.0, 3.5]
      langs_with_positive_delta: 7
      langs_with_negative_delta: 3
      langs_showing_clean_separation_of_10: 6
      random_direction_mean_delta_pp: 0.7
      difficulty_vs_random_ratio: 2.6
      prescriptive_accuracy: 0.60
      per_lang_results:
        zh: {delta_pp: 0.8, sig: false, clean_separation: true}
        es: {delta_pp: 1.2, sig: false, clean_separation: true}
        fr: {delta_pp: 1.4, sig: true, clean_separation: true}
        de: {delta_pp: 1.8, sig: true, clean_separation: true}
        hi: {delta_pp: 2.8, sig: true, clean_separation: true}
        ru: {delta_pp: 2.0, sig: true, clean_separation: true}
        ko: {delta_pp: -0.6, sig: false, clean_separation: false}
        tr: {delta_pp: 2.5, sig: true, clean_separation: false}
        sw: {delta_pp: -1.0, sig: false, clean_separation: false}
        bn: {delta_pp: 3.5, sig: true, clean_separation: false}
    result_rationale: >
      Difficulty decomposition 的定性逻辑成立：IRT difficulty 是语言无关属性
      （item difficulty 由人类整体表现定义，与特定语言无关），
      project out 后 residual 应该更 capability-specific、更语言依赖。
      Mean improvement 1.8pp 在 median 范围 [1, 3] 内，modest but real。

      但 prescriptive 能力弱（accuracy 60%, chance=50%）的原因有三：
      (1) IRT difficulty probe R²=0.33——只解释 33% 方差，
      projection 不完全，残余 difficulty signal 仍混杂在 residual 中。
      (2) Difficulty 和 capability 在 activation 空间中不正交——
      projection 同时移除了部分 capability 信息。
      ko 和 sw 中 AUROC 下降就是因为这些语言的 capability direction
      与 difficulty direction 有较大夹角重叠（cos > 0.3）。
      (3) 不同语言中纠缠程度不同——HIGH 资源语言 capability 较独立于
      difficulty（充足训练数据使模型分化了不同能力），
      MID/LOW 语言两者更纠缠。

      Random-direction control 显示 ~40% 的效果来自纯维度缩减
      （从高维投影到低维自然降噪），只有 ~60% 是 difficulty-specific。
      6/10 语言显示"干净分离"（difficulty projection 改善 > random
      projection 改善 + 1 std），但 ko/sw 下降、tr/bn 方向对但不干净。

      结论：弱化 Claim 2 为 "descriptive separation observed in most
      language-architecture combinations; the decomposition identifies
      difficulty-shared and capability-specific components but does not
      reliably predict optimal alignment strategy (prescriptive accuracy
      60%, near chance)." 保留为 ~0.5 页 subsection。
    tables:
      - name: "Table 9: Decomposition Results by Language (3-model mean, 8-layer mean)"
        data: |
          | Lang | Tier | Full AUROC | Diff-proj AUROC | Δ (pp) | Rand-proj AUROC | Rand Δ (pp) | Clean sep? |
          |------|------|------------|-----------------|--------|-----------------|-------------|------------|
          | zh   | HIGH | 0.725      | 0.733           | +0.8   | 0.729           | +0.4        | Yes        |
          | es   | HIGH | 0.732      | 0.744           | +1.2   | 0.738           | +0.6        | Yes        |
          | fr   | HIGH | 0.730      | 0.744           | +1.4   | 0.735           | +0.5        | Yes        |
          | de   | HIGH | 0.712      | 0.730           | +1.8   | 0.719           | +0.7        | Yes        |
          | hi   | MID  | 0.655      | 0.683           | +2.8   | 0.663           | +0.8        | Yes        |
          | ru   | MID  | 0.690      | 0.710           | +2.0   | 0.698           | +0.8        | Yes        |
          | ko   | MID  | 0.678      | 0.672           | -0.6   | 0.681           | +0.3        | No         |
          | tr   | MID  | 0.648      | 0.673           | +2.5   | 0.656           | +0.8        | No (*)     |
          | sw   | LOW  | 0.582      | 0.572           | -1.0   | 0.585           | +0.3        | No         |
          | bn   | LOW  | 0.600      | 0.635           | +3.5   | 0.608           | +0.8        | No (*)     |
          (*) tr/bn: positive delta > random but high variance across layers
    figures_description:
      - >
        Scatter: x=difficulty-specific Δ (difficulty-proj Δ minus random-proj Δ),
        y=difficulty probe R² per language。每点一个语言，颜色=resource tier。
        右上象限 (high R² + positive specific Δ) 包含 hi/de/fr，
        左下象限包含 ko/sw。Horizontal/vertical dashed lines at 0。
    analysis: >
      Decomposition 分析支持定性结论但不足以支撑 standalone claim。
      压缩为 0.5 页 subsection，核心 message：
      "Cross-lingual correctness transfer contains identifiable difficulty-shared
      and capability-specific components. Projecting out difficulty improves
      transfer for 7/10 languages (mean +1.8pp), significantly beyond
      random-direction control (mean +0.7pp). However, prescriptive accuracy
      (60%) is near chance, and the decomposition should be interpreted as
      descriptive rather than prescriptive."
      ko/sw 反常值得一句讨论——可能因为这些语言的 MMLU difficulty ordering
      与英语差异大（culturally-specific knowledge distribution）。

  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: "plan_005"
    description: >
      提取 verbalized confidence direction（prompt 模型输出 confidence score，
      fit probe），计算与 correctness direction 的 cosine similarity，
      20 语言 × 2 architectures (Qwen3 + Llama4)。
      作为 Claim 4 的 supporting evidence（subsection）。
    expected_results:
      mean_cosine_all: 0.040
      cosine_range: [0.010, 0.148]
      langs_below_0.05: 13
      langs_below_0.10: 17
      langs_above_0.10: 3
      per_tier_mean_cosine:
        HIGH: 0.028
        MID: 0.044
        LOW: 0.075
      architecture_comparison:
        qwen3_mean: 0.037
        llama4_mean: 0.043
        architecture_difference_significant: false
      outlier_langs: [am, yo, te]
      outlier_cosines: [0.148, 0.122, 0.105]
    result_rationale: >
      Miao & Ungar (2026) 在 English 7-8B 模型上发现 cosine < 0.04。
      HIGH 资源语言复现此结果（模型在这些语言上有充足训练数据，
      correctness 和 confidence direction 清晰分化）。
      MID 语言 cosine 略升（0.04-0.06）：verbalized confidence 在
      中资源语言上更 noisy（模型对 "I am X% confident" 的内部表征
      不够稳定），confidence probe 拟合的 direction 含更多 noise，
      noise directions 偶然与 correctness 有非零 cosine。
      LOW 语言中 am/yo/te 出现高 cosine (>0.10)——不是真正的
      correctness-confidence alignment，而是 probe capacity artifact：
      两个 direction 都很弱（selectivity < 0.05），cosine 被 noise 主导。
      与 plan_013 control task 交叉验证将确认这些语言的 selectivity
      低于 artifact threshold。

      两个架构差异微小（0.037 vs 0.043），不显著——orthogonality
      是模型结构的普遍性质，不依赖特定架构。
    tables:
      - name: "Table 10: Cosine Similarity by Resource Tier (2-architecture mean)"
        data: |
          | Tier | n  | Mean cos | Std   | Min   | Max   | <0.05 | <0.10 |
          |------|----|----------|-------|-------|-------|-------|-------|
          | HIGH | 6  | 0.028    | 0.011 | 0.010 | 0.042 | 5     | 6     |
          | MID  | 8  | 0.044    | 0.016 | 0.022 | 0.078 | 4     | 8     |
          | LOW  | 6  | 0.075    | 0.038 | 0.028 | 0.148 | 2     | 3     |
    figures_description:
      - >
        Bar chart: 20 语言按 cosine 升序，颜色=resource tier。
        Horizontal lines at 0.04 (Miao & Ungar threshold) 和 0.10 (artifact zone)。
        am/yo/te 三根 bar 突出。Star markers 标注 selectivity < 0.05 的语言。
    analysis: >
      Orthogonality 跨语言稳健（17/20 cosine < 0.10, 13/20 < 0.05），
      支持 "output-based calibration 的结构性局限与语言无关" 的结论。
      作为 0.3 页 subsection，强化 probe-based 方法的必要性论点。
      am/yo/te 的高 cosine 须与 control task 结果交叉验证——
      如果 selectivity 低于 0.05，则标注为 artifact 并从 cosine 分析
      中排除后重新报告（排除后 mean cosine 降至 ~0.035）。

  - name: "Probe Complexity Comparison (LR vs 2-layer MLP)"
    plan_id: "plan_006"
    description: >
      每 probed layer、每 model 对比 LR 和 2-layer MLP (256 hidden units)
      的 EN accuracy、cross-lingual transfer degradation 和 calibration quality。
      CPU-bound，使用缓存 activations。
    expected_results:
      lr_en_best_auroc_mean_3arch: 0.777
      mlp_en_best_auroc_mean_3arch: 0.798
      lr_mean_zs_auroc_mean_3arch: 0.656
      mlp_mean_zs_auroc_mean_3arch: 0.628
      lr_transfer_gap_mean: 0.121
      mlp_transfer_gap_mean: 0.170
      mlp_en_advantage_pp: 2.1
      lr_transfer_advantage_pp: 2.8
      lr_preferred_for_transfer: true
      lr_calibration_zs_ece: 0.228
      mlp_calibration_zs_ece: 0.258
    result_rationale: >
      MLP（2-layer, 256 hidden）有 ~256×d + 256 参数来拟合 EN correctness signal，
      vs LR 的 d+1 参数。额外容量让 MLP 捕获 EN-specific activation pattern
      （token position biases, English-specific syntactic cues），
      EN AUROC 提升 ~2.1pp。但这些 pattern 不跨语言迁移——
      它们是 English 特有的 surface features。

      LR 被迫学习最简洁的 direction（1 个超平面），
      这个 direction 更可能对应 language-agnostic correctness subspace
      （因为只有 1 维，必须选择信息量最大的方向，
      而跨语言共享的 correctness direction 恰好是信息量最大的）。
      Transfer gap: LR 12.1pp vs MLP 17.0pp——MLP 多出的 ~5pp gap
      = 2.1pp EN advantage + ~2.9pp EN-specific overfitting。

      LR 的 ZS ECE（0.228）也优于 MLP（0.258）——
      MLP 的额外容量在 EN 上过拟合 calibration pattern，
      迁移后 miscalibration 更严重。
    tables:
      - name: "Table 11: LR vs MLP Transfer Comparison (mean 3 models × 20 langs)"
        data: |
          | Metric                  | LR     | MLP    | Δ (MLP-LR) |
          |-------------------------|--------|--------|------------|
          | EN best AUROC           | 0.777  | 0.798  | +0.021     |
          | Mean ZS AUROC           | 0.656  | 0.628  | -0.028     |
          | Transfer gap (EN - ZS)  | 0.121  | 0.170  | +0.049     |
          | EN ECE                  | 0.186  | 0.174  | -0.012     |
          | Mean ZS ECE             | 0.228  | 0.258  | +0.030     |
          | ZS pass rate (>0.58)    | 72%    | 58%    | -14%       |
    figures_description:
      - >
        Paired scatter: x=LR ZS AUROC, y=MLP ZS AUROC, 每点一个 (language, model) pair。
        Diagonal y=x line。大多数点在对角线下方（MLP worse for transfer），
        尤其低资源语言偏移更大。颜色=resource tier。
    analysis: >
      LR vs MLP 对比为方法论选择提供实证支持：
      linear probes 是 cross-lingual transfer 的正确选择（牺牲 2pp EN
      质量换取 ~5pp transfer improvement）。这与 Hewitt & Liang (2019)
      的 probe complexity 讨论一致——更简单的 probe 捕获更 generalizable 的 signal。
      Paper 中一句话概括："We use logistic regression probes throughout,
      as 2-layer MLPs achieve 2.1pp higher English AUROC but transfer
      4.9pp worse (Table 11)."

  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: "plan_007"
    description: >
      在 Belebele（阅读理解 MCQA）和 MMLU-ProX（翻译 MMLU）上
      评估 best probes + 所有 transfer methods。20 语言 × 3 models。
      验证 findings generalize beyond GlobalMMLU。
    expected_results:
      belebele:
        en_best_auroc: 0.74
        mean_zs_auroc: 0.622
        zs_pass_rate: 0.60
        pareto_preserved: true
        pareto_strength: "weaker than GlobalMMLU (median ρ=-0.25 vs -0.34)"
        linear_proj_still_effective: true
        caclr_still_inert: true
      mmlu_prox:
        en_best_auroc: 0.77
        mean_zs_auroc: 0.648
        zs_pass_rate: 0.70
        pareto_preserved: true
        pareto_strength: "comparable to GlobalMMLU (median ρ=-0.32 vs -0.34)"
        linear_proj_still_effective: true
        caclr_still_inert: true
      cross_benchmark_lang_ranking_rho: 0.87
      rank_globalmmlu_belebele: 0.82
      rank_globalmmlu_prox: 0.92
    result_rationale: >
      Belebele 是 passage-based RC 任务——correctness signal 依赖
      passage comprehension 而非 parametric knowledge，probe 拟合的
      direction 与 knowledge-MCQA 的 correctness direction 不完全相同。
      EN AUROC 略低（0.74 vs GlobalMMLU 的 ~0.78）因为 RC correctness
      更依赖 attention pattern 而非 stored knowledge direction。
      Transfer 更差（mean ZS 0.622 vs 0.656）因为 passage comprehension
      在不同语言间的 alignment 比 knowledge signal 更差
      （passage encoding 更受 surface-level linguistic features 影响）。

      但 Pareto 结构保留——depth-transferability tradeoff 是
      representation geometry 的性质（CKA decline + language specialization），
      不依赖具体 task。MMLU-ProX 与 GlobalMMLU 高度相关
      （同源翻译数据），模式几乎一致。

      CaCLR 在两个 benchmark 上仍无效（distributional matching
      不受 task 影响），linear projection 仍有效（subspace rotation
      不依赖 task）——泛化性确认。Language ranking 跨 benchmark
      高度相关（rho=0.87）——transfer 质量主要由 language properties
      决定，而非 benchmark。
    tables:
      - name: "Table 12: Cross-Benchmark Comparison (mean 3 models × 20 langs)"
        data: |
          | Metric               | GlobalMMLU | Belebele | MMLU-ProX |
          |----------------------|------------|----------|-----------|
          | EN best AUROC        | 0.777      | 0.740    | 0.770     |
          | Mean ZS AUROC        | 0.656      | 0.622    | 0.648     |
          | ZS pass rate         | 72%        | 60%      | 70%       |
          | Pareto sig langs     | 8 (mean)   | 6 (mean) | 7 (mean)  |
          | Linear proj Δ (pp)   | +3.0       | +2.5     | +2.8      |
          | CaCLR Δ (pp)         | +0.3       | +0.2     | +0.3      |
          | Lang ranking ρ       | —          | 0.82     | 0.92      |
    figures_description:
      - >
        三 benchmark parallel coordinates: 每条线一个语言, x=3 benchmarks,
        y=ZS AUROC。颜色=resource tier。大多数线近似平行（ranking 一致），
        Belebele 整体偏低。少数交叉线标注（benchmark-specific anomalies）。
    analysis: >
      Cross-benchmark 泛化确认主要发现的稳健性。所有 key patterns
      （architecture 差异、resource tier gradient、CaCLR 无效、linear projection 有效）
      在三个 benchmark 上一致。Belebele 上 Pareto 更弱是预期的
      （task difference），不影响结论。

  - name: "Quantization Validation Ablation"
    plan_id: "plan_010"
    description: >
      (a) W4A16 vs FP16 for Llama 4 Scout at 5 representative layers, 5% subset;
      (b) GPTQ-Int4 vs FP16 for Qwen3-235B at 5 representative layers, 5% subset。
      验证量化不扭曲 correctness signal。
    expected_results:
      llama4_w4a16_vs_fp16:
        mean_abs_delta_auroc: 0.005
        max_abs_delta_auroc: 0.008
        cka_fp16_vs_quant: 0.986
      qwen3_int4_vs_fp16:
        mean_abs_delta_auroc: 0.007
        max_abs_delta_auroc: 0.013
        cka_fp16_vs_quant: 0.977
      quantization_safe: true
      note: "All |ΔAUROC| < 0.015, well within bootstrap CI"
    result_rationale: >
      4-bit weight quantization 保留 activation 空间的大部分结构——
      correctness signal 是低维子空间特征，quantization noise 主要分布在
      与 correctness direction 正交的高维空间中（concentration of measure：
      高维空间中随机 noise 几乎不与任何固定低维子空间对齐）。
      ΔAUROC < 0.013 在 bootstrap CI 内，不影响任何结论。

      Qwen3 的 MoE INT4 量化略有更大 delta（max 0.013 vs Llama4 的 0.008），
      因为 MoE 的 expert routing decision 在 INT4 下可能微变
      （routing logits 精度下降导致偶尔选择不同 expert），
      但影响被 expert 间的 redundancy 缓冲——大多数 expert
      学到的 correctness signal 方向相似。

      CKA(FP16, quant) > 0.97 确认 activation 空间整体结构保留。
      Gemma 4 不需要此消融（BF16 无量化）——它本身作为
      quantization-free reference point。
    tables:
      - name: "Table 13: Quantization Validation (per-layer ΔAUROC)"
        data: |
          | Model  | Layer (% depth) | FP16 AUROC | Quant AUROC | ΔAUROC  |
          |--------|-----------------|------------|-------------|---------|
          | Llama4 | L8  (17%)       | 0.630      | 0.627       | -0.003  |
          | Llama4 | L16 (33%)       | 0.682      | 0.685       | +0.003  |
          | Llama4 | L24 (50%)       | 0.718      | 0.714       | -0.004  |
          | Llama4 | L36 (75%)       | 0.745      | 0.739       | -0.006  |
          | Llama4 | L44 (92%)       | 0.762      | 0.764       | +0.002  |
          | Qwen3  | L16 (17%)       | 0.625      | 0.618       | -0.007  |
          | Qwen3  | L36 (38%)       | 0.700      | 0.704       | +0.004  |
          | Qwen3  | L52 (55%)       | 0.735      | 0.730       | -0.005  |
          | Qwen3  | L68 (72%)       | 0.770      | 0.775       | +0.005  |
          | Qwen3  | L80 (85%)       | 0.790      | 0.777       | -0.013  |
    figures_description:
      - >
        Bland-Altman plot: x=(FP16+Quant)/2, y=FP16-Quant。
        每点一层。水平虚线 ±0.015 tolerance band。
        所有点在 band 内。Qwen3 L80 标注为 max outlier。
    analysis: >
      Quantization validation 通过。Paper 中一句话报告：
      "Quantization artifacts are negligible for correctness probing
      (max |ΔAUROC| = 0.013, CKA > 0.97, Appendix B)."
      Qwen3 L80 的 -0.013 是最大偏差但不影响 EN-optimal layer 选择
      （L80 仍是 EN-best 无论量化与否）。

  - name: "Full CKA Analysis & Simpson's Paradox Validation"
    plan_id: "plan_011"
    description: >
      Linear CKA (EN vs 20 target langs) at every probed layer, 3 models。
      核心分析：partial correlation controlling for normalized depth。
      Per-layer cross-language Spearman (n=20 per layer)。
      Subspace angle 定量分析。CKA depth profile 对比。
    expected_results:
      qwen3:
        raw_spearman_rho: -0.24
        raw_p: 0.001
        partial_rho_ctrl_depth: 0.17
        partial_p: 0.062
        significant: false
        per_layer_positive_rho_count_of_24: 17
        per_layer_significant_count: 5
        bootstrap_ci_partial: [-0.01, 0.35]
        cka_cliff_onset_pct: 0.68
        cka_peak_mean: 0.80
        cka_final_mean: 0.11
      llama4:
        raw_spearman_rho: -0.30
        raw_p: 0.001
        partial_rho_ctrl_depth: 0.28
        partial_p: 0.022
        significant: true
        per_layer_positive_rho_count_of_13: 10
        per_layer_significant_count: 4
        bootstrap_ci_partial: [0.05, 0.49]
        cka_cliff_onset_pct: 0.50
        cka_peak_mean: 0.82
        cka_final_mean: 0.22
      gemma4:
        raw_spearman_rho: -0.26
        raw_p: 0.001
        partial_rho_ctrl_depth: 0.23
        partial_p: 0.038
        significant: true
        per_layer_positive_rho_count_of_16: 12
        per_layer_significant_count: 4
        bootstrap_ci_partial: [0.03, 0.42]
        cka_cliff_onset_pct: 0.60
        cka_peak_mean: 0.78
        cka_final_mean: 0.18
      simpson_paradox_confirmed_of_3: 2
      cka_transfer_collapse_threshold: 0.30
      subspace_angle_analysis:
        HIGH_mean_angle: 11
        MID_mean_angle: 23
        LOW_mean_angle: 43
    result_rationale: >
      Simpson's Paradox 的架构依赖性源于 CKA-depth gradient 的函数形状。

      Llama 4 Scout: CKA 从 peak 0.82 (L12) 线性下降到 0.22 (L48),
      slope -0.017/layer。线性 depth confound 强且形状规则——
      linear partial correlation 有效地移除了 depth 效应，
      释放 CKA 的独立解释力（partial rho=0.28, p=0.022）。

      Gemma 4 Dense: CKA 从 peak 0.78 (L16) 下降到 0.18 (L60),
      slope -0.014/layer，也是近似线性。
      Partial rho=0.23, p=0.038——边缘显著。

      Qwen3-235B: CKA profile 非线性——前 60% 层几乎 flat (0.75-0.80),
      然后 L64-L80 急降到 0.25, L80-L92 继续降到 0.11。
      这种 step-function-like profile 使得 linear partial correlation
      效果差——前 60% 层的 depth 变化几乎不带 CKA 变化，
      后 30% 层的 depth 变化带大量 CKA 变化。
      Linear control 无法适应这种非线性（partial rho=0.17, p=0.062, 不显著）。
      但 per-layer analysis 仍支持正关系：17/24 层的 cross-language
      rho 为正（n=20 per layer gives moderate power）。

      CKA collapse threshold ~0.30：当 mean CKA 降到 0.30 以下，
      ZS AUROC 急降——correctness subspace alignment 已经太弱，
      residual shared direction 不足以维持 transfer。

      Subspace angle 分析提供了 CKA 结论的 complementary quantification：
      HIGH 语言角度 ~11°（near-aligned, zero-shot viable），
      LOW 语言角度 ~43°（substantial misalignment, needs projection）。
      这与 Procrustes reversal threshold 互洽
      （reversal at ~0.55 AUROC ↔ ~20-25° angle）。
    tables:
      - name: "Table 14: Simpson's Paradox — Raw vs Partial Correlation (3 architectures)"
        data: |
          | Model        | n obs | Raw ρ  | Raw p   | Partial ρ | Part. p | Boot 95% CI    | Sig? |
          |--------------|-------|--------|---------|-----------|---------|----------------|------|
          | Qwen3-235B   | 480   | -0.24  | <0.001  | +0.17     | 0.062   | [-0.01, +0.35] | No   |
          | Llama4 Scout | 260   | -0.30  | <0.001  | +0.28     | 0.022   | [+0.05, +0.49] | Yes  |
          | Gemma4 31B   | 320   | -0.26  | <0.001  | +0.23     | 0.038   | [+0.03, +0.42] | Yes  |
          | Pilot Llama  | 45    | -0.16  | 0.294   | +0.41     | 0.006   | [+0.12, +0.65] | Yes  |
          | Pilot Qwen   | 40    | -0.16  | 0.310   | +0.18     | 0.274   | [-0.15, +0.48] | No   |
      - name: "Table 15: CKA Depth Profiles (mean across 20 languages)"
        data: |
          | Norm depth | Qwen3 CKA | Llama4 CKA | Gemma4 CKA |
          |------------|-----------|------------|------------|
          | 0.0        | 0.72      | 0.60       | 0.65       |
          | 0.17       | 0.75      | 0.82       | 0.78       |
          | 0.33       | 0.79      | 0.75       | 0.72       |
          | 0.50       | 0.78      | 0.58       | 0.62       |
          | 0.67       | 0.62      | 0.42       | 0.48       |
          | 0.75       | 0.40      | 0.35       | 0.38       |
          | 0.83       | 0.25      | 0.30       | 0.30       |
          | 0.92       | 0.14      | 0.25       | 0.22       |
          | 1.0        | 0.11      | 0.22       | 0.18       |
      - name: "Table 16: Subspace Angle Analysis (correctness direction EN vs target)"
        data: |
          | Tier | n  | Qwen3 angle | Llama4 angle | Gemma4 angle | Mean ZS AUROC |
          |------|----|-------------|--------------|--------------|---------------|
          | HIGH | 6  | 10°         | 12°          | 11°          | 0.714         |
          | MID  | 8  | 22°         | 25°          | 23°          | 0.662         |
          | LOW  | 6  | 45°         | 40°          | 43°          | 0.563         |
    figures_description:
      - >
        Simpson's Paradox visualization (core figure):
        2×3 grid (top row: raw correlation, bottom row: per-depth-bin positive trends)。
        Each column = one architecture。Scatter: x=CKA, y=ZS AUROC,
        color=normalized depth。Top row: overall negative trend line。
        Bottom row: per-depth-bin positive trend lines (3-5 bins, different colors)。
        Sign reversal 清晰可见。Inset: raw ρ 和 partial ρ with p-values。
      - >
        CKA × layer × language heatmap: 3 panels (1 per model)。
        x=20 languages (sorted by mean CKA), y=probed layers。
        颜色=CKA。Qwen3 panel 显示 sharp transition (sudden cold zone),
        Llama4/Gemma4 显示 gradual transition。
    analysis: >
      Simpson's Paradox 在 2/3 架构上显著确认，1/3 trending——
      足以支撑 "geometric analysis" framing（而非仅 "suggestive correlation"）。
      Paper 报告："In 2/3 architectures, controlling for depth reveals
      a significant positive relationship between CKA and transfer AUROC
      (Llama4: ρ=0.28, p=0.022; Gemma4: ρ=0.23, p=0.038).
      Qwen3-235B shows the same trend but does not reach significance
      under linear depth control (ρ=0.17, p=0.062), likely because its
      step-function CKA profile violates the linearity assumption."

      Qwen3 的 non-significance 不是 weakness——it IS the finding：
      CKA-depth relationship 的函数形状决定了 partial correlation 的有效性。
      这为 reviewers 提供了 transparency（承认局限性）同时保持
      overall narrative（CKA 有解释力，但需要适配 depth control method）。

  - name: "Linear Projection Sensitivity & Procrustes Effect Reversal"
    plan_id: "plan_012"
    description: >
      Vary parallel pairs (10, 20, 50, 100, 200) for Procrustes alignment。
      3 models × 5 representative layers × 20 languages。
      Resource-tier stratified saturation curves。
      Procrustes effect reversal analysis by ZS AUROC band。
    expected_results:
      overall_pairs_to_95pct: 88
      per_tier_saturation:
        HIGH: {pairs_95pct: 30, max_delta_pp: 0.8}
        MID:  {pairs_95pct: 65, max_delta_pp: 2.8}
        LOW:  {pairs_95pct: 100, max_delta_pp: 5.8}
      saturation_curve:
        pairs_10:  {pct_of_max: 0.40, mean_delta_pp: 1.2}
        pairs_20:  {pct_of_max: 0.60, mean_delta_pp: 1.8}
        pairs_50:  {pct_of_max: 0.82, mean_delta_pp: 2.5}
        pairs_100: {pct_of_max: 0.96, mean_delta_pp: 2.9}
        pairs_200: {pct_of_max: 1.00, mean_delta_pp: 3.0}
      procrustes_reversal:
        threshold_estimate: 0.55
        threshold_ci_95: [0.47, 0.62]
        benefit_below_0.50: {mean_delta_pp: 5.5, n_langs: 4}
        ambiguous_0.50_0.62: {mean_delta_pp: 1.0, n_langs: 8}
        harm_above_0.62: {mean_delta_pp: -1.5, n_langs: 8}
      saturation_r2_by_tier:
        HIGH: 0.95
        MID: 0.90
        LOW: 0.78
    result_rationale: >
      Saturation at ~88 pairs（而非 pilot 预估的 ~50）因为：
      (1) 20 语言引入比 5 语言更大的方差——saturation point 是
      across-language weighted average，LOW 语言拉高了 overall number；
      (2) 部分低资源语言的 parallel data 翻译质量低（机翻 artifacts），
      增加了 Procrustes 估计的 noise，需要更多 pairs 来稳定。

      Resource-tier stratification 反映 subspace angle 差异：
      HIGH 语言角度小（~11°），10-20 pairs 就足以估计简单旋转，
      30 pairs 达 95%。LOW 语言角度大（~43°），需要 100 pairs
      才稳定估计更复杂的旋转。

      Procrustes reversal 机制：当 ZS AUROC > 0.62，
      EN-target correctness subspace 已经 well-aligned（angle < 15°），
      Procrustes 旋转引入的估计噪声反而大于 alignment gain→净效果负。
      当 ZS AUROC < 0.50，严重 misalignment（angle > 40°）使得
      Procrustes gain 远大于 noise→净效果显著正。
      阈值 ~0.55 对应 ~20-25° angle 的平衡点。

      LOW tier curves noise 更大（R²=0.78）——个别语言的 saturation
      不单调（20 pairs 偶然优于 50 pairs），因为 parallel pair 质量
      方差大。Paper 报告 per-tier saturation + overall 88 pairs recommendation。
    tables:
      - name: "Table 17: Saturation Curves by Resource Tier (3-model mean)"
        data: |
          | Pairs | HIGH Δ(pp) | MID Δ(pp) | LOW Δ(pp) | Overall Δ(pp) |
          |-------|------------|-----------|-----------|---------------|
          | 10    | +0.2       | +1.0      | +2.5      | +1.2          |
          | 20    | +0.4       | +1.6      | +3.8      | +1.8          |
          | 50    | +0.6       | +2.3      | +4.8      | +2.5          |
          | 100   | +0.8       | +2.7      | +5.6      | +2.9          |
          | 200   | +0.8       | +2.8      | +5.8      | +3.0          |
      - name: "Table 18: Procrustes Effect Reversal by ZS AUROC Band"
        data: |
          | ZS AUROC band | n langs | Mean Δ(pp) | % positive | Example langs      |
          |---------------|---------|------------|------------|--------------------|
          | < 0.50        | 4       | +5.5       | 100%       | am, yo, te, (my)   |
          | 0.50 - 0.55   | 2       | +3.2       | 100%       | sw, bn             |
          | 0.55 - 0.60   | 2       | +1.0       | 75%        | th, tr             |
          | 0.60 - 0.65   | 4       | +0.2       | 50%        | hi, vi, ko, ar     |
          | 0.65 - 0.70   | 4       | -0.8       | 25%        | ru, ja, id, uk     |
          | > 0.70        | 4       | -1.5       | 0%         | zh, es, fr, nl     |
    figures_description:
      - >
        Saturation curve: x=pairs (log scale), y=ΔAUROC (pp) vs ZS。
        三条线 (HIGH/MID/LOW tier)，shaded bootstrap 95% CI。
        HIGH 线快速 plateau（~30 pairs），LOW 线缓慢上升且 CI 宽。
        Horizontal dashed line "95% of max"。Annotation: "HIGH: 30 pairs,
        MID: 65 pairs, LOW: 100 pairs"。
      - >
        Procrustes reversal scatter: x=ZS AUROC baseline, y=ΔAUROC from
        linear projection (200 pairs)。每点一个 (language, model) pair,
        颜色=model。LOESS fit 显示从正到负的渐变。
        Vertical band 标注 reversal threshold ~0.55 及 95% CI [0.47, 0.62]。
    analysis: >
      Linear projection 是论文最直接的 practical contribution。
      Deployment recommendation：
      (1) 测试 zero-shot AUROC → 低于 0.55 使用 linear projection（~100 pairs），
      高于 0.62 直接 zero-shot；
      (2) HIGH 资源语言不需要 projection（可能有害 ~1.5pp）；
      (3) LOW 资源语言 ~100 pairs 达到 95% of max improvement。
      ~100 pairs = ~3-4 小时标注工作（如果 parallel data 已有）。

  - name: "Probing Control Tasks — Full Scale (3 models × 20 langs)"
    plan_id: "plan_013"
    description: >
      扩展已完成的 Qwen2.5-7B English control task 至 3 models × 20 languages
      × all probed layers。Train probes on permuted labels，
      compute selectivity = real AUROC - control AUROC。
      Selectivity threshold sensitivity analysis (0.03, 0.05, 0.10)。
    expected_results:
      overall_artifact_rate_threshold_0.05: 0.22
      artifact_rate_by_tier:
        HIGH: 0.05
        MID: 0.22
        LOW: 0.35
      control_task_selectivity_deep_layers_mean: 0.20
      per_tier_selectivity_at_en_optimal:
        HIGH: 0.23
        MID: 0.15
        LOW: 0.07
      control_auroc_range: [0.48, 0.52]
      threshold_sensitivity:
        threshold_0.03: {overall_artifact_rate: 0.18}
        threshold_0.05: {overall_artifact_rate: 0.22}
        threshold_0.10: {overall_artifact_rate: 0.30}
      affected_depth_range: "primarily 0-40% depth for MID/LOW"
      en_selectivity_scales_with_model_size: true
      en_selectivity_deep_range: [0.22, 0.28]
    result_rationale: >
      Pilot (Qwen2.5-7B, EN) 显示 selectivity 在 L20-L27 为 0.24-0.26。
      Full-scale 扩展时：

      (1) EN selectivity 在更大模型上略高（0.22-0.28 range across 3 models）——
      更大模型的 correctness signal 更强，real AUROC 更高，
      而 control AUROC 仍在 ~0.49 附近（permuted labels 不含 signal）。

      (2) HIGH 资源语言的 selectivity 接近 EN（0.23 at deep layers）——
      模型在这些语言上有充足训练数据，correctness direction 清晰。
      Artifact rate 仅 5%（仅在 L0-L4）。

      (3) MID 资源语言 selectivity 中等（0.15 at deep layers）。
      Artifact rate ~22%，主要集中在 0-40% depth——浅层 correctness
      signal 太弱，probe 主要拟合 capacity artifacts。
      tr, vi 等"表面高资源但 knowledge coverage 低"的语言
      artifact rate 偏高（~30%）。

      (4) LOW 资源语言 selectivity 低（0.07 at deep layers）。
      Artifact rate ~35%。yo/am/te 在所有层的 selectivity 都低——
      即使 deep layers 也仅 ~0.03-0.05，接近 artifact threshold。
      这些语言的"positive" ZS AUROC (0.53-0.57) 很可能反映
      probe capacity 而非 genuine correctness transfer。

      Threshold sensitivity: 0.05 是合理选择（Hewitt & Liang 原始值），
      但 paper 应报告 3 个 threshold 结果让读者自行判断。
      从 0.03 到 0.10，artifact rate 从 18% 升到 30%——
      这个 range 覆盖了 median tier 的 [15%, 30%] 范围。
    tables:
      - name: "Table 19: Artifact Rate by Depth Zone and Resource Tier (3-model mean)"
        data: |
          | Depth zone   | HIGH art% | MID art% | LOW art% | Overall |
          |--------------|-----------|----------|----------|---------|
          | 0-25% depth  | 15%       | 55%      | 80%      | 48%     |
          | 25-50% depth | 3%        | 30%      | 62%      | 30%     |
          | 50-75% depth | 0%        | 12%      | 18%      | 10%     |
          | 75-100% depth| 0%        | 3%       | 5%       | 3%      |
          | Overall      | 5%        | 22%      | 35%      | 22%     |
      - name: "Table 20: Selectivity at EN-Optimal Layer by Language (3-model mean)"
        data: |
          | Tier | Lang | Real AUROC | Ctrl AUROC | Selectivity | Artifact? |
          |------|------|------------|------------|-------------|-----------|
          | HIGH | zh   | 0.730      | 0.498      | 0.232       | No        |
          | HIGH | es   | 0.738      | 0.496      | 0.242       | No        |
          | MID  | hi   | 0.660      | 0.504      | 0.156       | No        |
          | MID  | tr   | 0.648      | 0.510      | 0.138       | No        |
          | LOW  | sw   | 0.585      | 0.506      | 0.079       | No        |
          | LOW  | bn   | 0.600      | 0.502      | 0.098       | No        |
          | LOW  | yo   | 0.538      | 0.512      | 0.026       | YES       |
          | LOW  | am   | 0.528      | 0.514      | 0.014       | YES       |
          | LOW  | te   | 0.555      | 0.510      | 0.045       | Marginal  |
    figures_description:
      - >
        Selectivity heatmap: x=20 languages (sorted by tier), y=probed layers (by depth)。
        颜色=selectivity（diverging: red=high, blue=low artifact zone <0.05）。
        Dashed contour at selectivity=0.05 separating reliable/artifact zones。
        Clear pattern: upper-left (deep+HIGH) warm, lower-right (shallow+LOW) cold。
    analysis: >
      Control task finding 是独立 methodological contribution：
      首次在 cross-lingual probing 中系统应用 Hewitt & Liang selectivity，
      发现 22% overall（35% LOW, 22% MID）language-layer 组合不可靠。
      Field-level implication: 所有 cross-lingual probing 研究
      （包括 Xiao et al.）应包含 selectivity checks。

      Paper 中 main body 报告两点：
      (1) 用 selectivity filter 后重新报告 main results（确认结论不变——
      只排除了本来就 AUROC 低的 language-layer 组合）；
      (2) methodological warning + recommendation：
      "We recommend that all future cross-lingual probing studies include
      control task validation, particularly for low-resource languages
      where artifact rates reach 35%."

  - name: "Extended Language Coverage (50+ Languages, Camera-Ready)"
    plan_id: "plan_009"
    description: >
      从 20 扩展至 50+ 语言。Camera-ready extension。
      利用 GlobalMMLU + Belebele 全语言集。
    expected_results:
      total_languages: 52
      zs_pass_rate_52: 0.60
      zs_pass_rate_20_subset: 0.72
      artifact_rate_very_low_resource: 0.50
      resource_tier_gradient_confirmed: true
      rank_correlation_20_vs_52: 0.94
      min_zs_auroc: 0.50
      min_zs_lang: "Haitian Creole (ht)"
    result_rationale: >
      新增 32 语言大多为 LOW/VERY-LOW resource。Pass rate 从 20 语言的
      72% 降到 52 语言的 60%——新增语言偏向低资源。
      VERY-LOW 语言（<1M training tokens）中 ~50% 结果为 probing artifacts
      （selectivity < 0.05）——这些语言的 activations 几乎不含
      distinguishable correctness signal。

      20 语言核心发现在 52 语言上保持（rank correlation 0.94）——
      主要贡献是统计功效和覆盖度，非新发现。
      边际收益递减：每种新语言对 core claims 的增量证据极小。
    tables:
      - name: "Table 21: Language Coverage Expansion"
        data: |
          | Tier      | 20-lang n | 52-lang n | Mean ZS AUROC | Artifact rate |
          |-----------|-----------|-----------|---------------|---------------|
          | HIGH      | 6         | 8         | 0.72          | 4%            |
          | MID       | 8         | 14        | 0.66          | 18%           |
          | LOW       | 6         | 18        | 0.57          | 35%           |
          | VERY-LOW  | 0         | 12        | 0.52          | 50%           |
    figures_description:
      - >
        World map: 52 语言标注，颜色=ZS AUROC (green→red)。
        Western Europe + East Asia green, Sub-Saharan Africa + Oceania red。
    analysis: >
      Camera-ready extension 增强覆盖度但 story 不变。
      Core analysis 仍基于 20 语言（methodology 更干净）。
      52 语言作为 robustness check 放在 appendix + 一段 main body 文字。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22716d35-7b6a-4b27-9c9d-3f143b1d83c5",
  "isSidechain": false,
  "requestId": "req_011CbFjWY2Yr5UQ4eDkXHfHb",
  "type": "assistant",
  "uuid": "1a8fc3b5-f2b6-4263-84ba-0a391e0a0058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171WhNsehx8tiXBzvEU9RNr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24912,
      "cache_read_input_tokens": 50284,
      "output_tokens": 29089,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24912,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 29089,
          "cache_read_input_tokens": 50284,
          "cache_creation_input_tokens": 24912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24912
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "1a8fc3b5-f2b6-4263-84ba-0a391e0a0058",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Median outcome: Pareto-CKA analysis with CaCLR negative result",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; pap…",
  "leafUuid": "1a8fc3b5-f2b6-4263-84ba-0a391e0a0058",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Median outcome: Pareto-CKA analysis with CaCLR negative result",
  "sessionId": "4b165f82-4576-4c8e-8e10-460d189b9eb4"
}
```

---
