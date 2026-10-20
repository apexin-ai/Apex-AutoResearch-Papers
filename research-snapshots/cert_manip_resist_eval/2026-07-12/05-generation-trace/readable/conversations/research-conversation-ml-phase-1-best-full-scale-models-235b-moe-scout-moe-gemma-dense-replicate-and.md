# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Full-scale models (235B MoE + Scout MoE + Gemma Dense) replicate and amplify

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/f5eee182-64f0-49d7-8928-961587304e5d.jsonl`
- **Structured JSON:** [`f577067fbcec3f95b15c.json`](../../sessions/f5/f577067fbcec3f95b15c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:27:07.254Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:27:07.254Z",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Full-scale models (235B MoE + Scout MoE + Gemma Dense) replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement; all 4 claims fully supported with strong effect sizes\n核心假设：['Larger models encode correctness signal more cleanly → EN AUROC scales with model size', 'Pareto frontier (depth-transfer tradeoff at deepest layers) persists at scale and shows clear MoE vs dense architectural contrast', \"Simpson's Paradox in CKA-transfer confirmed across all 3 architectures with bootstrap CIs\", 'CaCLR β > 0: MMD consistency loss on 1-D logits shifts Pareto frontier for ≥10/20 languages', 'Difficulty-capability decomposition yields clean separation with ≥3pp transfer improvement after projection', 'Linear projection saturates at ~30-50 pairs, resource-tier stratification replicates']\n关键指标范围：{'en_auroc_best_layer_mean_across_arch': [0.8, 0.86], 'zs_transfer_pass_rate_auroc_gt_058_of_20': [16, 20], 'mean_zs_auroc_drop_vs_en_pp': [4, 8], 'pareto_tradeoff_prevalence_frac_lang_arch_pairs': [0.5, 0.75], 'pareto_depth_transfer_drop_at_final_layers_pp': [2.0, 6.0], 'cka_partial_corr_rho_controlling_depth': [0.3, 0.55], 'cka_partial_corr_p_value': [0.0001, 0.01], 'simpson_paradox_confirmed_of_3_arch': [3, 3], 'caclr_delta_over_zeroshot_mean_pp': [2.0, 5.0], 'caclr_langs_improved_of_20': [10, 16], 'linear_proj_delta_over_zs_low_resource_pp': [5, 12], 'linear_proj_saturation_pairs': [30, 50], 'decomposition_transfer_improvement_after_difficulty_projection_pp': [3, 6], 'decomposition_langs_showing_clean_separation_of_10': [7, 10], 'control_task_selectivity_deep_layers': [0.2, 0.35], 'cross_lingual_artifact_rate_pct': [5, 15], 'spearman_depth_vs_transfer_rho_positive_langs_of_20': [16, 20]}\n叙事方向：Method contribution paper. CaCLR is a lightweight, label-free method that shifts the Pareto frontier via distributional matching. Story spine intact: orthogonality → Pareto discovery → decomposition explains it → CaCLR solves it → CKA geometric analysis explains why. Headline: 'CaCLR-trained probes reduce non-English ECE by X% requiring zero target-language labels.' All 4 claims at full strength. Linear projection sample efficiency + control task warning are strong empirical contributions in main body.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions\n- Camera-ready extension: 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as \"principled scope\" not \"design limitation.\"\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method.\" Note: linear projection is \"the only label-free method that consistently improves over zero-shot across resource tiers\" — NOT \"only viable path.\" Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive. CORAL COMPARISON\n    (D015, re-dream 2-tier consensus): Add CORAL loss (second-order alignment, Sun\n    & Saenko 2016) as alternative to MMD. Tests whether distributional matching failure\n    is MMD-specific or general. Trivial to implement on cached activations. Report\n    CORAL alongside MMD in Table 7 ablation. Strengthens negative result scope. HIGH-DIM\n    MMD (D016, dream #4 cross-tier consensus): All 3 tiers flagged \"1-D logit MMD\"\n    as overclaimed scope. Test MMD on PCA-reduced activations (d=50, d=100) instead\n    of 1-D probe logits. If high-dim also fails → broadens \"distributional matching\n    fails\" claim. If high-dim works → method contribution jumps significantly. Trivial:\n    PCA on cached activations, then MMD in reduced space. Also test with CORAL in\n    high-dim. MULTI-SEED (D016): Run 3-5 seeds for CaCLR, few-shot (25/100), and Procrustes\n    at representative layers. Report std across seeds. Addresses single-seed concern.\n    MIXED β CRITERION (D016): Add 1-2 validation languages (zh, sw) to β selection\n    criterion alongside English, to rule out systematic bias against cross-lingual\n    benefit.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  registry_id: plan_013\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique. SELECTIVITY THRESHOLD\n    SENSITIVITY (D015): Test at 0.03, 0.05, 0.10 thresholds (Hewitt & Liang used 0.05\n    for English syntactic probing; may not be appropriate for multilingual correctness).\n    Report artifact rate at each threshold. Trivial to compute from existing data\n    (plan_013 v2 already running).\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 32.7B Dense (60 text layers, dense, BF16): third architecture\n    for core submission. Full Pareto frontier at every 4th layer + final (16 probed\n    layers), 20 languages, 5 transfer conditions. BF16 (~62.5GB, fits single 96GB\n    GPU). Provides dense vs MoE architectural contrast — addresses #1 reviewer concern\n    across ALL dream tiers (\"architecture comparison confounded\").\n\n    '\n  priority: P0\n  gpu_budget_hours: 30\n  deps: []\n  notes: 'Upgraded P2→P0 (D016). User providing 4× RTX 6000 96G on second server.\n    Model: google/gemma-4-31B (HF) / ModelScope. Apache 2.0, no gating. MULTIMODAL:\n    has vision encoder (27 extra layers) — extract_activations.py must hook ONLY text\n    decoder layers (60 layers), skip vision. Code may need adjustment. BF16 ~62.5GB\n    (2 shards: 49.8 + 12.8GB), single 96GB GPU sufficient. No quantization needed\n    — eliminates quantization confound for this model.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- exp_id: plan_013_probing_controls_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002_4gpu\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:27:07.258Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:27:07.258Z",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-21T12:27:07.277Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Full-scale models (235B MoE + Scout MoE + Gemma Dense) replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement; all 4 claims fully supported with strong effect sizes
核心假设：['Larger models encode correctness signal more cleanly → EN AUROC scales with model size', 'Pareto frontier (depth-transfer tradeoff at deepest layers) persists at scale and shows clear MoE vs dense architectural contrast', "Simpson's Paradox in CKA-transfer confirmed across all 3 architectures with bootstrap CIs", 'CaCLR β > 0: MMD consistency loss on 1-D logits shifts Pareto frontier for ≥10/20 languages', 'Difficulty-capability decomposition yields clean separation with ≥3pp transfer improvement after projection', 'Linear projection saturates at ~30-50 pairs, resource-tier stratification replicates']
关键指标范围：{'en_auroc_best_layer_mean_across_arch': [0.8, 0.86], 'zs_transfer_pass_rate_auroc_gt_058_of_20': [16, 20], 'mean_zs_auroc_drop_vs_en_pp': [4, 8], 'pareto_tradeoff_prevalence_frac_lang_arch_pairs': [0.5, 0.75], 'pareto_depth_transfer_drop_at_final_layers_pp': [2.0, 6.0], 'cka_partial_corr_rho_controlling_depth': [0.3, 0.55], 'cka_partial_corr_p_value': [0.0001, 0.01], 'simpson_paradox_confirmed_of_3_arch': [3, 3], 'caclr_delta_over_zeroshot_mean_pp': [2.0, 5.0], 'caclr_langs_improved_of_20': [10, 16], 'linear_proj_delta_over_zs_low_resource_pp': [5, 12], 'linear_proj_saturation_pairs': [30, 50], 'decomposition_transfer_improvement_after_difficulty_projection_pp': [3, 6], 'decomposition_langs_showing_clean_separation_of_10': [7, 10], 'control_task_selectivity_deep_layers': [0.2, 0.35], 'cross_lingual_artifact_rate_pct': [5, 15], 'spearman_depth_vs_transfer_rho_positive_langs_of_20': [16, 20]}
叙事方向：Method contribution paper. CaCLR is a lightweight, label-free method that shifts the Pareto frontier via distributional matching. Story spine intact: orthogonality → Pareto discovery → decomposition explains it → CaCLR solves it → CKA geometric analysis explains why. Headline: 'CaCLR-trained probes reduce non-English ECE by X% requiring zero target-language labels.' All 4 claims at full strength. Linear projection sample efficiency + control task warning are strong empirical contributions in main body.

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
  "promptId": "7f6384cd-15ed-4514-b679-c96259e865e9",
  "type": "user",
  "uuid": "967f6c36-ba57-4098-a80e-a66bf97eebe4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:27:07.275Z_

```json
{
  "parentUuid": "967f6c36-ba57-4098-a80e-a66bf97eebe4",
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
  "uuid": "2c4e8e39-7550-463e-8201-a56d7a50e547",
  "timestamp": "2026-05-21T12:27:07.275Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:27:07.275Z_

```json
{
  "parentUuid": "2c4e8e39-7550-463e-8201-a56d7a50e547",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1aca3de9-8cc6-4588-a159-bdb739fc099f",
  "timestamp": "2026-05-21T12:27:07.275Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Full-scale models (235B MoE + Scout MoE + Gemma Dense) replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement;…",
  "leafUuid": "1aca3de9-8cc6-4588-a159-bdb739fc099f",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe transfer and CaCLR calibration",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:27:10.161Z_

我先检查项目中是否有已有的预测文件或相关结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aca3de9-8cc6-4588-a159-bdb739fc099f",
  "isSidechain": false,
  "requestId": "req_011CbFiGm9aQMsiriW75X7H5",
  "type": "assistant",
  "uuid": "ac6dd2c8-33ae-4420-89a3-ef0ec60e1123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMqhCQUAYrsT54AaNHKgRb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18757,
      "cache_read_input_tokens": 11841,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 79,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18757
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

_source line 9 · 2026-05-21T12:27:10.241Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0133Jx6mfo3ThPWfnCW5VvFa`</summary>

```json
{
  "pattern": "**/*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac6dd2c8-33ae-4420-89a3-ef0ec60e1123",
  "isSidechain": false,
  "requestId": "req_011CbFiGm9aQMsiriW75X7H5",
  "type": "assistant",
  "uuid": "87c10463-c5cb-4d31-88b4-de71a1cfbf2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMqhCQUAYrsT54AaNHKgRb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18757,
      "cache_read_input_tokens": 11841,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 79,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18757
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

_source line 10 · 2026-05-21T12:27:10.263Z_

<details><summary>↩ Tool result · `toolu_0133Jx6mfo3ThPWfnCW5VvFa`</summary>

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
  "parentUuid": "87c10463-c5cb-4d31-88b4-de71a1cfbf2d",
  "isSidechain": false,
  "promptId": "7f6384cd-15ed-4514-b679-c96259e865e9",
  "type": "user",
  "uuid": "9d4650b3-c854-47e3-96b9-e46be3c90636",
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
    "durationMs": 14,
    "numFiles": 64,
    "truncated": false
  },
  "sourceToolAssistantUUID": "87c10463-c5cb-4d31-88b4-de71a1cfbf2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T12:27:14.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K9vTyKxwVc9FQmALh8nzWG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d4650b3-c854-47e3-96b9-e46be3c90636",
  "isSidechain": false,
  "requestId": "req_011CbFiGywGMdHLR6YpYjZLc",
  "type": "assistant",
  "uuid": "adc79fb7-163e-4c82-aadd-fb04aaeee4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3iLL5Nowyg3iuZFmqEZHQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1587,
      "cache_read_input_tokens": 30598,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 30598,
          "cache_creation_input_tokens": 1587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1587
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

_source line 12 · 2026-05-21T12:27:14.098Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UqyeGPjzFgvmCXHQyN6Lux`</summary>

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
  "parentUuid": "adc79fb7-163e-4c82-aadd-fb04aaeee4a5",
  "isSidechain": false,
  "requestId": "req_011CbFiGywGMdHLR6YpYjZLc",
  "type": "assistant",
  "uuid": "bb1ee37f-6c33-40cc-a8ef-3f467421fddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3iLL5Nowyg3iuZFmqEZHQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1587,
      "cache_read_input_tokens": 30598,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 30598,
          "cache_creation_input_tokens": 1587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1587
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

_source line 13 · 2026-05-21T12:27:14.112Z_

<details><summary>↩ Tool result · `toolu_01UqyeGPjzFgvmCXHQyN6Lux`</summary>

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
  "parentUuid": "bb1ee37f-6c33-40cc-a8ef-3f467421fddb",
  "isSidechain": false,
  "promptId": "7f6384cd-15ed-4514-b679-c96259e865e9",
  "type": "user",
  "uuid": "0991cd81-8720-47b7-80cf-d87a3c88fd73",
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
  "sourceToolAssistantUUID": "bb1ee37f-6c33-40cc-a8ef-3f467421fddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Full-scale models (235B MoE + Scout MoE + Gemma Dense) replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement;…",
  "leafUuid": "0991cd81-8720-47b7-80cf-d87a3c88fd73",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe transfer and CaCLR calibration",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Tool result

_source line 16 · 2026-05-21T12:27:14.350Z_

<details><summary>↩ Tool result · `toolu_01K9vTyKxwVc9FQmALh8nzWG`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立。以 Simpson''s Paradox 几何洞见为核心新颖性开篇—— raw CKA-transfer
3	  correlation 为负（depth confound），partial correlation controlling for depth 在双架构上均显著为正（p
4	  < 0.01），揭示 within-layer CKA genuinely predicts transfer quality。CaCLR 作为正面方法贡献（+3.5pp
5	  mean over ZS），不是 headline 但 构成因果链第三环。标题强调 ''geometric analysis reveals when and
6	  why cross-lingual calibration transfer succeeds''。四条 claim 完整因果链保留：Pareto discovery（architecture-
7	  dependent depth-transferability tradeoff）→ Decomposition analysis（difficulty vs
8	  capability separation）→ CaCLR method（consistency loss provides measurable gain at
9	  deep layers）→ CKA geometric explanation（Simpson''s Paradox, subspace persistence）。
10	  Control task warning（28% low-resource artifacts）和 linear projection sample efficiency
11	  （~42 pairs to 95%）作为加分实证贡献。Procrustes effect reversal（threshold ~0.52） 为 practitioner
12	  提供直接指导。无需弱化任何 claims。
13	
14	  '
15	imagined_experiments:
16	- name: Full Pareto Frontier — Qwen3-235B-A22B
17	  plan_id: plan_001
18	  description: '94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th), 20
19	    typologically diverse languages, English logistic regression probes, 5 transfer
20	    conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100,
21	    CaCLR。重点验证 MVP 发现的 strong depth-transferability tradeoff 是否在大模型上保持。
22	
23	    '
24	  expected_results:
25	    en_best_auroc: 0.81
26	    en_best_layer_idx: 72
27	    en_auroc_range:
28	    - 0.58
29	    - 0.81
30	    en_ece_raw_best: 0.168
31	    zs_mean_auroc_20lang_best_transfer_layer: 0.72
32	    zs_best_transfer_layer_idx: 52
33	    zs_pass_rate_20lang: 0.9
34	    zs_fail_langs:
35	    - yo
36	    - te
37	    zs_auroc_by_tier:
38	      HIGH_mean: 0.76
39	      MID_mean: 0.72
40	      LOW_mean: 0.63
41	    zs_auroc_selected:
42	      zh: 0.77
43	      es: 0.76
44	      fr: 0.76
45	      de: 0.77
46	      ja: 0.75
47	      nl: 0.76
48	      pt: 0.75
49	      it: 0.75
50	      ar: 0.73
51	      hi: 0.71
52	      ko: 0.72
53	      tr: 0.71
54	      ru: 0.74
55	      vi: 0.7
56	      th: 0.69
57	      sw: 0.63
58	      bn: 0.65
59	      yo: 0.57
60	      ig: 0.61
61	      te: 0.58
62	    per_lang_spearman_rho_median: -0.64
63	    per_lang_significant_at_005: 15
64	    global_spearman_rho: -0.91
65	    global_spearman_p: 0.0001
66	    pareto_frontier_layers:
67	    - 40
68	    - 44
69	    - 48
70	    - 52
71	    - 56
72	    pareto_en_zs_gap_at_knee_pp: 4.2
73	    mean_shift_delta_auroc: 0.0
74	    linproj_200pairs_mean_auroc: 0.74
75	    fewshot_25_mean_auroc: 0.708
76	    fewshot_100_mean_auroc: 0.735
77	  result_rationale: 'Qwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 3×，log-linear
78	    probing scaling 预期 EN AUROC 从 0.754 提升至 ~0.81。94 层深网络使 depth-transferability tradeoff
79	    比 28 层 MVP 更显著：EN-optimal layer (L72, 77% depth) 与 ZS-optimal layer (L52, 55%
80	    depth) 之间有 20 层间隔（MVP 仅 3 层）。Strong Pareto 源于 Qwen 架构特征：MoE routing 在深层产生 language-specific
81	    expert 激活模式， 导致 correctness direction 的 cross-lingual alignment 在 L60 后急剧下降。 15/20
82	    languages 的 per-language Spearman rho 显著为负，表明 tradeoff 是 跨语言一致的。2 个 fail 语言（yo,
83	    te）的 AUROC < 0.60 因为 Qwen3 pretraining corpus 中 Yoruba/Telugu 占比极低（<0.1%），embedding
84	    层的 representation quality 即不足以支撑 correctness signal。Mean-shift ΔAUROC ≡ 0 因为 StandardScaler
85	    + LR 下 mean-shift 对 AUROC 无影响（已在 MVP 中数学证明）。 Linear projection (200 pairs) 提供
86	    +2pp 因为 Procrustes alignment 捕获了 correctness subspace 的旋转，但不触及 distributional
87	    matching。
88	
89	    '
90	  tables:
91	  - name: 'Table 1: Qwen3-235B Pareto Frontier (selected layers)'
92	    columns:
93	    - layer_idx
94	    - depth_pct
95	    - en_auroc
96	    - zs_mean_20
97	    - zs_drop_pp
98	    - on_pareto
99	    rows:
100	    - - 4
101	      - 4
102	      - 0.58
103	      - 0.572
104	      - 0.8
105	      - false
106	    - - 12
107	      - 13
108	      - 0.645
109	      - 0.632
110	      - 1.3
111	      - false
112	    - - 20
113	      - 21
114	      - 0.71
115	      - 0.695
116	      - 1.5
117	      - false
118	    - - 28
119	      - 30
120	      - 0.752
121	      - 0.733
122	      - 1.9
123	      - false
124	    - - 36
125	      - 38
126	      - 0.778
127	      - 0.752
128	      - 2.6
129	      - false
130	    - - 40
131	      - 43
132	      - 0.788
133	      - 0.748
134	      - 4.0
135	      - true
136	    - - 44
137	      - 47
138	      - 0.796
139	      - 0.74
140	      - 5.6
141	      - true
142	    - - 48
143	      - 51
144	      - 0.802
145	      - 0.732
146	      - 7.0
147	      - true
148	    - - 52
149	      - 55
150	      - 0.806
151	      - 0.72
152	      - 8.6
153	      - true
154	    - - 56
155	      - 60
156	      - 0.808
157	      - 0.706
158	      - 10.2
159	      - true
160	    - - 60
161	      - 64
162	      - 0.81
163	      - 0.69
164	      - 12.0
165	      - false
166	    - - 68
167	      - 72
168	      - 0.81
169	      - 0.661
170	      - 14.9
171	      - false
172	    - - 72
173	      - 77
174	      - 0.81
175	      - 0.638
176	      - 17.2
177	      - false
178	    - - 80
179	      - 85
180	      - 0.805
181	      - 0.601
182	      - 20.4
183	      - false
184	    - - 88
185	      - 94
186	      - 0.792
187	      - 0.558
188	      - 23.4
189	      - false
190	    - - 92
191	      - 98
192	      - 0.778
193	      - 0.531
194	      - 24.7
195	      - false
196	  - name: 'Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3'
197	    columns:
198	    - language
199	    - tier
200	    - spearman_rho
201	    - p_value
202	    - significant
203	    rows:
204	    - - zh
205	      - HIGH
206	      - -0.72
207	      - 0.001
208	      - true
209	    - - es
210	      - HIGH
211	      - -0.68
212	      - 0.002
213	      - true
214	    - - fr
215	      - HIGH
216	      - -0.7
217	      - 0.001
218	      - true
219	    - - de
220	      - HIGH
221	      - -0.69
222	      - 0.002
223	      - true
224	    - - ja
225	      - HIGH
226	      - -0.74
227	      - 0.001
228	      - true
229	    - - nl
230	      - HIGH
231	      - -0.67
232	      - 0.003
233	      - true
234	    - - pt
235	      - MID
236	      - -0.65
237	      - 0.004
238	      - true
239	    - - it
240	      - MID
241	      - -0.66
242	      - 0.003
243	      - true
244	    - - ar
245	      - MID
246	      - -0.71
247	      - 0.001
248	      - true
249	    - - hi
250	      - MID
251	      - -0.63
252	      - 0.005
253	      - true
254	    - - ko
255	      - MID
256	      - -0.67
257	      - 0.003
258	      - true
259	    - - tr
260	      - MID
261	      - -0.62
262	      - 0.006
263	      - true
264	    - - ru
265	      - MID
266	      - -0.69
267	      - 0.002
268	      - true
269	    - - vi
270	      - MID
271	      - -0.61
272	      - 0.008
273	      - true
274	    - - th
275	      - MID
276	      - -0.58
277	      - 0.012
278	      - true
279	    - - sw
280	      - LOW
281	      - -0.52
282	      - 0.025
283	      - true
284	    - - bn
285	      - LOW
286	      - -0.55
287	      - 0.018
288	      - false
289	    - - yo
290	      - LOW
291	      - -0.48
292	      - 0.042
293	      - false
294	    - - ig
295	      - LOW
296	      - -0.51
297	      - 0.028
298	      - false
299	    - - te
300	      - LOW
301	      - -0.45
302	      - 0.058
303	      - false
304	  figures_description:
305	  - 'Figure 1a: Pareto frontier scatter (EN AUROC x-axis vs ZS mean AUROC y-axis),
306	    24 points, 5 Pareto-optimal layers marked red. Clear convex knee at ~55% depth.
307	
308	    '
309	  - 'Figure 1b: Heatmap — ZS AUROC by language (y-axis, ordered by resource tier)
310	    × normalized depth (x-axis). Warm mid-band, low-resource rows cool earlier at
311	    shallower depth than high-resource rows.
312	
313	    '
314	  analysis: 'Qwen3-235B 展现 strong, consistent depth-transferability tradeoff： global
315	    Spearman ρ = -0.91 (p < 0.001), 15/20 per-language ρ 显著为负。 Pareto frontier 包含
316	    5 层 (L40-L56)，knee 在 ~55% depth。EN-optimal (L72) 与 ZS-optimal (L52) 相隔 20 层 /
317	    22pp depth，远大于 MVP 的 3 层 间隔。这证实 tradeoff 在大模型上不是减弱而是放大——更深的网络有更多 空间进行 language-specific
318	    specialization。High-resource 语言在 Pareto knee 以下也保持 AUROC > 0.74，但 low-resource
319	    在 70% depth 后急剧下降。 这与 CKA 分析一致：CKA 在 L60 后的 cliff 解释了为何 deep-layer transfer 对
320	    low-resource 影响更大（CKA 基线更低，cliff 更早触及）。
321	
322	    '
323	- name: Full Pareto Frontier — Llama 4 Scout
324	  plan_id: plan_002
325	  description: '48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every
326	    4th), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B 的 weak/mixed tradeoff
327	    pattern 是否是 Llama 架构家族特征。
328	
329	    '
330	  expected_results:
331	    en_best_auroc: 0.79
332	    en_best_layer_idx: 36
333	    en_auroc_range:
334	    - 0.56
335	    - 0.79
336	    en_ece_raw_best: 0.182
337	    zs_mean_auroc_20lang_best_transfer_layer: 0.7
338	    zs_best_transfer_layer_idx: 28
339	    zs_pass_rate_20lang: 0.85
340	    zs_fail_langs:
341	    - yo
342	    - te
343	    - ig
344	    zs_auroc_by_tier:
345	      HIGH_mean: 0.74
346	      MID_mean: 0.7
347	      LOW_mean: 0.61
348	    per_lang_spearman_rho_median: -0.28
349	    per_lang_significant_at_005: 6
350	    per_lang_positive_rho_langs:
351	    - ar
352	    - hi
353	    - ko
354	    global_spearman_rho: -0.78
355	    global_spearman_p: 0.003
356	    pareto_frontier_layers:
357	    - 20
358	    - 24
359	    - 28
360	    mean_shift_delta_auroc: 0.0
361	    linproj_200pairs_mean_auroc: 0.718
362	    fewshot_25_mean_auroc: 0.692
363	    fewshot_100_mean_auroc: 0.718
364	  result_rationale: 'Llama 4 Scout 延续 MVP Llama-3.1-8B 的 weak tradeoff 模式。虽然 global
365	    Spearman ρ = -0.78 仍然显著（12 data points, p=0.003），但 per-language 分析揭示了明显的异质性：仅
366	    6/20 languages 有显著负 ρ，而 ar/hi/ko 展现正 ρ（深层 transfer 反而改善）。这与 MVP 完全一致（ar/ko 在 L31
367	    优于 L20），且可归因于 Llama 架构的 multilingual training recipe：Meta 的训练策略使 ar/hi/ko 在深层保持更好的
368	    cross-lingual alignment，可能 因为这些语言在 pretraining 中与 English 有更多 code-switching 数据。
369	    Global rho 仍然显著是因为大多数语言确实有弱负趋势，但 per-language 分析揭示这不是 universal pattern。与 Qwen3
370	    的对比清晰：Qwen3 的 15/20 significant vs Llama4 的 6/20，median rho -0.64 vs -0.28。这一
371	    architecture-dependent tradeoff strength 是 Claim 1 的核心发现。
372	
373	    '
374	  tables:
375	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
376	    columns:
377	    - layer_idx
378	    - depth_pct
379	    - en_auroc
380	    - zs_mean_20
381	    - zs_drop_pp
382	    - on_pareto
383	    rows:
384	    - - 4
385	      - 8
386	      - 0.56
387	      - 0.552
388	      - 0.8
389	      - false
390	    - - 8
391	      - 17
392	      - 0.635
393	      - 0.625
394	      - 1.0
395	      - false
396	    - - 12
397	      - 25
398	      - 0.695
399	      - 0.682
400	      - 1.3
401	      - false
402	    - - 16
403	      - 33
404	      - 0.735
405	      - 0.718
406	      - 1.7
407	      - false
408	    - - 20
409	      - 42
410	      - 0.758
411	      - 0.724
412	      - 3.4
413	      - true
414	    - - 24
415	      - 50
416	      - 0.772
417	      - 0.714
418	      - 5.8
419	      - true
420	    - - 28
421	      - 58
422	      - 0.782
423	      - 0.7
424	      - 8.2
425	      - true
426	    - - 32
427	      - 67
428	      - 0.789
429	      - 0.681
430	      - 10.8
431	      - false
432	    - - 36
433	      - 75
434	      - 0.79
435	      - 0.655
436	      - 13.5
437	      - false
438	    - - 40
439	      - 83
440	      - 0.785
441	      - 0.625
442	      - 16.0
443	      - false
444	    - - 44
445	      - 92
446	      - 0.772
447	      - 0.589
448	      - 18.3
449	      - false
450	    - - 48
451	      - 100
452	      - 0.748
453	      - 0.548
454	      - 20.0
455	      - false
456	  - name: 'Table 4: Architecture-Dependent Pareto Comparison'
457	    columns:
458	    - metric
459	    - Qwen3_235B
460	    - Llama4_Scout
461	    - interpretation
462	    rows:
463	    - - global_rho
464	      - -0.91
465	      - -0.78
466	      - both significant but Qwen stronger
467	    - - per_lang_sig_count
468	      - 15/20
469	      - 6/20
470	      - Qwen consistent, Llama mixed
471	    - - median_per_lang_rho
472	      - -0.64
473	      - -0.28
474	      - 2.3x difference in effect size
475	    - - positive_rho_langs
476	      - 0
477	      - 3
478	      - Llama has ar/hi/ko reversed
479	    - - best_transfer_depth_pct
480	      - 55
481	      - 58
482	      - comparable location
483	    - - en_zs_gap_at_knee_pp
484	      - 4.2
485	      - 3.4
486	      - comparable magnitude
487	  - name: 'Table 5: Transfer Conditions Comparison (both models, at best-transfer
488	      layer)'
489	    columns:
490	    - condition
491	    - Qwen3_mean_20
492	    - Llama4_mean_20
493	    - combined_mean
494	    rows:
495	    - - zero-shot
496	      - 0.72
497	      - 0.7
498	      - 0.71
499	    - - mean-shift
500	      - 0.72
501	      - 0.7
502	      - 0.71
503	    - - linear_proj_200
504	      - 0.74
505	      - 0.718
506	      - 0.729
507	    - - few-shot-25
508	      - 0.708
509	      - 0.692
510	      - 0.7
511	    - - few-shot-100
512	      - 0.735
513	      - 0.718
514	      - 0.727
515	  figures_description:
516	  - 'Figure 2: Overlaid Pareto frontiers (normalized depth), Qwen3 in blue, Llama4
517	    in orange. Qwen3 shifted up-right with steeper descent; Llama4 flatter with more
518	    scatter at deep layers.
519	
520	    '
521	  - 'Figure 3: Per-language Spearman ρ distribution: Qwen3 (left) tightly clustered
522	    around -0.65; Llama4 (right) spread from -0.50 to +0.35, ar/hi/ko clearly positive.
523	
524	    '
525	  analysis: 'Architecture-dependent Pareto strength 是 Claim 1 的核心。两个架构的 global rho
526	    都显著（满足 pareto_spearman_rho_significant_archs = 2 的 约束），但 effect size 差异明显。Qwen3
527	    的 strong tradeoff 意味着 practitioner 必须在 EN accuracy 和 transfer quality 之间做明确选择；
528	    Llama4 的 weak tradeoff 意味着某些语言（ar, hi, ko）可以 "free-ride" 深层的 EN improvement 而不牺牲
529	    transfer。这一差异无法从 domain adaptation theory 预测——它是架构特有的 empirical finding。 Best-transfer
530	    depth 在两个架构上收敛至 55-58%，暗示一个 universal "mid-depth transfer zone"，但 frontier 的 steepness
531	    是 architecture-specific。
532	
533	    '
534	- name: CKA Cross-Lingual Similarity & Simpson's Paradox Analysis
535	  plan_id: plan_011
536	  description: 'Linear CKA (EN vs each target) at every probed layer, 20 languages
537	    × 2 models。核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b)
538	    partial Spearman controlling for normalized depth — THE single most important
539	    analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。验证
540	    pilot finding 的 Simpson''s Paradox 在 full-scale 上双架构复现。
541	
542	    '
543	  expected_results:
544	    qwen3_raw_rho: -0.36
545	    qwen3_raw_p: 0.0001
546	    llama4_raw_rho: -0.41
547	    llama4_raw_p: 0.0001
548	    qwen3_partial_rho: 0.48
549	    qwen3_partial_p: 0.002
550	    qwen3_partial_bootstrap_ci_95:
551	    - 0.31
552	    - 0.62
553	    llama4_partial_rho: 0.41
554	    llama4_partial_p: 0.008
555	    llama4_partial_bootstrap_ci_95:
556	    - 0.22
557	    - 0.57
558	    simpson_paradox_confirmed_both_archs: true
559	    qwen3_per_layer_positive_count: 18
560	    qwen3_per_layer_significant_count: 6
561	    llama4_per_layer_positive_count: 9
562	    llama4_per_layer_significant_count: 3
563	    qwen3_cka_peak_layer: 16
564	    qwen3_cka_peak_value: 0.82
565	    qwen3_cka_at_en_optimal_layer: 0.28
566	    qwen3_cka_cliff_onset_depth_pct: 55
567	    llama4_cka_peak_layer: 12
568	    llama4_cka_peak_value: 0.84
569	    llama4_cka_at_en_optimal_layer: 0.35
570	    llama4_cka_cliff_onset_depth_pct: 50
571	    transfer_collapse_cka_threshold: 0.35
572	    below_threshold_mean_zs_auroc: 0.58
573	    above_threshold_mean_zs_auroc: 0.72
574	    correctness_subspace_angle_within_layer_mean_deg: 12.4
575	    correctness_subspace_angle_across_layer_mean_deg: 38.7
576	    correctness_direction_persists_despite_global_cka_decline: true
577	  result_rationale: 'Simpson''s Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper
578	    → representations diverge → CKA drops）和 transfer AUROC（deeper → EN probe stronger
579	    → higher absolute AUROC up to a point），创造了一个 confound。 Raw pooled correlation
580	    为负是因为 shallow layers 有 high CKA 但 low AUROC （probe 本身弱），deep layers 有 low CKA
581	    但 higher AUROC（probe 强虽然 transfer degrades）。控制 depth 后，within 每个 layer，higher
582	    CKA 的 语言确实有 better transfer，partial rho 为正。
583	
584	    MVP pilot（Llama, 5 langs × 9 layers）已展现 rho=+0.41, p=0.006。 Full-scale（20 langs
585	    × 12-24 layers）增强统计 power：per-layer test 从 n=5 增至 n=20，partial correlation 的 bootstrap
586	    CI 不含零。
587	
588	    Qwen3 partial rho (0.48) 高于 Llama4 (0.41)，与 Qwen 的 steeper CKA cliff 一致：Qwen 的
589	    CKA 变异范围更大（peak 0.82 → floor 0.28 vs Llama 0.84 → 0.35），为 partial correlation
590	    提供更多 signal。
591	
592	    MVP Qwen pilot 仅 rho=+0.18 (p=0.274)，full-scale上升至 0.48 是因为： (1) n 从 5 增至 20 语言，power
593	    大幅提升；(2) 20 语言覆盖更宽的 CKA 范围（增加了 yo/ig/te 等极低 CKA 语言和 nl/pt 等高 CKA 语言）， 扩大了 within-layer
594	    variance。
595	
596	    CKA cliff threshold ~0.35 标记了 "transfer collapse zone"：当 CKA 低于此阈值时，correctness
597	    direction 的 cross-lingual overlap 不足以 支撑 zero-shot transfer。Subspace angle analysis
598	    揭示 correctness direction 在同一 layer 内跨语言仅旋转 ~12°（highly aligned），但跨 layer 旋转 ~39°（significant
599	    drift），解释了为何 within-layer CKA 预测 transfer 但 raw pooled 不预测。
600	
601	    '
602	  tables:
603	  - name: 'Table 6: Simpson''s Paradox — Raw vs Partial Correlation'
604	    columns:
605	    - model
606	    - analysis
607	    - spearman_rho
608	    - p_value
609	    - bootstrap_95CI
610	    - interpretation
611	    rows:
612	    - - Qwen3-235B
613	      - raw pooled (CKA vs ZS AUROC)
614	      - -0.36
615	      - <0.001
616	      - '[-0.44, -0.27]'
617	      - negative — depth confound
618	    - - Qwen3-235B
619	      - partial (controlling depth)
620	      - 0.48
621	      - 0.002
622	      - '[+0.31, +0.62]'
623	      - positive — genuine geometric signal
624	    - - Llama4 Scout
625	      - raw pooled (CKA vs ZS AUROC)
626	      - -0.41
627	      - <0.001
628	      - '[-0.50, -0.31]'
629	      - negative — depth confound
630	    - - Llama4 Scout
631	      - partial (controlling depth)
632	      - 0.41
633	      - 0.008
634	      - '[+0.22, +0.57]'
635	      - positive — genuine geometric signal
636	  - name: 'Table 7: Per-Layer CKA-Transfer Correlation (Qwen3, selected layers)'
637	    columns:
638	    - layer_idx
639	    - depth_pct
640	    - mean_CKA_20lang
641	    - spearman_rho_n20
642	    - p_value
643	    rows:
644	    - - 12
645	      - 13
646	      - 0.78
647	      - 0.52
648	      - 0.019
649	    - - 20
650	      - 21
651	      - 0.81
652	      - 0.48
653	      - 0.032
654	    - - 28
655	      - 30
656	      - 0.76
657	      - 0.55
658	      - 0.012
659	    - - 36
660	      - 38
661	      - 0.68
662	      - 0.51
663	      - 0.022
664	    - - 44
665	      - 47
666	      - 0.56
667	      - 0.46
668	      - 0.041
669	    - - 52
670	      - 55
671	      - 0.45
672	      - 0.43
673	      - 0.058
674	    - - 60
675	      - 64
676	      - 0.38
677	      - 0.38
678	      - 0.098
679	    - - 68
680	      - 72
681	      - 0.3
682	      - 0.33
683	      - 0.155
684	    - - 72
685	      - 77
686	      - 0.28
687	      - 0.28
688	      - 0.231
689	    - - 80
690	      - 85
691	      - 0.22
692	      - 0.21
693	      - 0.372
694	  - name: 'Table 8: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)'
695	    columns:
696	    - depth_pct
697	    - HIGH_CKA
698	    - MID_CKA
699	    - LOW_CKA
700	    - overall_CKA
701	    rows:
702	    - - 13
703	      - 0.86
704	      - 0.79
705	      - 0.62
706	      - 0.78
707	    - - 30
708	      - 0.84
709	      - 0.77
710	      - 0.58
711	      - 0.76
712	    - - 47
713	      - 0.68
714	      - 0.56
715	      - 0.35
716	      - 0.56
717	    - - 64
718	      - 0.48
719	      - 0.37
720	      - 0.22
721	      - 0.38
722	    - - 77
723	      - 0.38
724	      - 0.27
725	      - 0.14
726	      - 0.28
727	    - - 94
728	      - 0.25
729	      - 0.18
730	      - 0.09
731	      - 0.19
732	  - name: 'Table 9: Subspace Angle Analysis (correctness direction)'
733	    columns:
734	    - comparison_type
735	    - mean_angle_deg
736	    - std_deg
737	    - interpretation
738	    rows:
739	    - - within-layer cross-language (same layer, different langs)
740	      - 12.4
741	      - 5.8
742	      - highly aligned — correctness direction is near-universal
743	    - - cross-layer same-language (same lang, different layers)
744	      - 38.7
745	      - 11.2
746	      - significant drift — direction rotates with depth
747	    - - random baseline (shuffled)
748	      - 87.3
749	      - 2.1
750	      - near-orthogonal — signal is non-trivial
751	  figures_description:
752	  - 'Figure 4a: Simpson''s Paradox visualization — left panel: raw scatter (CKA vs
753	    ZS AUROC) showing negative trend with depth-colored points; right panel: partial
754	    residual plot after controlling for depth showing positive trend. Two panels side
755	    by side dramatically illustrate the sign reversal.
756	
757	    '
758	  - 'Figure 4b: CKA × layer × language heatmap for Qwen3 (main) and Llama4 (inset).
759	    Color intensity = CKA value. Clear gradient from warm (shallow, high CKA) to cool
760	    (deep, low CKA), with low-resource languages cooling faster.
761	
762	    '
763	  - 'Figure 4c: CKA threshold scatter — transfer AUROC (y) vs CKA (x), vertical dashed
764	    line at CKA=0.35 showing transfer collapse zone.
765	
766	    '
767	  analysis: 'Simpson''s Paradox 在双架构上显著复现（partial rho Qwen=+0.48 p=0.002, Llama=+0.41
768	    p=0.008），是本文的核心几何洞见。这不是 trivially expected from measurement overlap（CKA 和 transfer
769	    AUROC 都衡量 EN-target 相似性） ——sign reversal 从负到正是 non-trivial 的。
770	
771	    Subspace angle analysis 提供 mechanistic grounding：correctness direction 在同一 layer
772	    内跨语言仅 ~12° 偏差（near-universal），但跨 layer 偏差 ~39°（significant rotation）。这解释了为何 CKA（衡量全局
773	    representation similarity）与 transfer（衡量 correctness direction alignment）的关系 需要控制
774	    depth 后才能显现：全局 CKA 下降反映的是 non-correctness dimensions 的 divergence，correctness
775	    subspace 本身作为 low-dimensional feature 持续存在。
776	
777	    CKA cliff threshold ~0.35 直接解释了 Qwen3 vs Llama4 tradeoff 差异： Qwen3 的 CKA cliff
778	    更陡（L52→L60 从 0.45 降至 0.38），导致更多语言 在 deep layers 穿越 threshold → strong tradeoff；Llama4
779	    的 cliff 更缓 （L28→L36 从 0.55 降至 0.45），且 ar/hi/ko 因高 baseline CKA 从不穿越 threshold
780	    → weak/mixed tradeoff。
781	
782	    这一分析将 Claim 1 的 Pareto observation 与 CKA geometry 连接，构成 完整的 geometric explanation：architecture-dependent
783	    CKA cliff steepness → architecture-dependent Pareto frontier strength。
784	
785	    '
786	- name: CaCLR Implementation and Comparative Evaluation
787	  plan_id: plan_003
788	  description: 'L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits).
789	    English labels + parallel activations from GlobalMMLU test-split 70/30 partition.
790	    Compare vs zero-shot/mean-shift/linear-proj/few-shot across full Pareto frontier,
791	    both models × 20 languages. α sweep [0.01–10], β sweep [0.001–1.0] across 3 OOM.
792	
793	    '
794	  expected_results:
795	    best_alpha: 0.1
796	    best_beta: 0.05
797	    caclr_mean_delta_auroc_vs_zs: 0.035
798	    caclr_mean_delta_auroc_vs_linproj: 0.015
799	    caclr_improvement_at_deep_layers_pp: 4.8
800	    caclr_improvement_at_shallow_layers_pp: 1.2
801	    caclr_improvement_pass_rate: 0.88
802	    qwen3_caclr_mean_auroc_20lang: 0.757
803	    qwen3_caclr_delta_vs_zs_pp: 3.7
804	    qwen3_caclr_ece_mean: 0.078
805	    llama4_caclr_mean_auroc_20lang: 0.733
806	    llama4_caclr_delta_vs_zs_pp: 3.3
807	    llama4_caclr_ece_mean: 0.085
808	    beta_0001_delta_pp: 0.5
809	    beta_001_delta_pp: 1.8
810	    beta_005_delta_pp: 3.5
811	    beta_01_delta_pp: 3.2
812	    beta_10_delta_pp: 0.8
813	    alpha_001_ece_improvement_pp: 1.5
814	    alpha_01_ece_improvement_pp: 3.2
815	    alpha_10_ece_improvement_pp: 2.8
816	    alpha_100_ece_improvement_pp: -0.5
817	    bce_only_auroc: 0.71
818	    bce_sbece_auroc: 0.722
819	    bce_consistency_auroc: 0.738
820	    bce_sbece_consistency_auroc: 0.745
821	    mmd_kernel: Gaussian RBF, bandwidth=median heuristic
822	    optimizer: Adam, lr=1e-3, linear warmup 10%
823	    epochs: 50
824	    early_stopping: patience=10, monitor=val_auroc
825	    initialization: from standard LR solution
826	    batch_size: 256
827	    mmd_items: same items as BCE (overlapping)
828	    parallel_set_size_range:
829	    - 1800
830	    - 4200
831	  result_rationale: 'CaCLR 的 consistency loss (β·MMD on 1-D logits) 强制 probe 学习 language-invariant
832	    features：EN 和 target-language 的 probe 输出分布 应相似。在 1-D logit space 中，MMD 有效地匹配了两种语言的
833	    logit mean 和 variance，等价于让 probe direction 靠近 CKA analysis 中揭示的 "universal correctness
834	    subspace"。
835	
836	    +3.5pp mean delta（[2, 5] range 内）反映了 1-D MMD 的能力边界：它能 捕获 first-order distributional
837	    alignment（mean/variance matching）， 但无法完成 full rotational alignment（需要 d-dimensional
838	    操作）。Linear projection（+2pp）通过 Procrustes 做了 rotational alignment 但不优化 probe 本身；CaCLR
839	    的优势在于 end-to-end 优化但受 1-D 约束。两者差距 仅 1.5pp，说明 correctness transfer 的瓶颈主要是 rotational（线性
840	    投影解决的）而非 distributional（MMD 解决的）。
841	
842	    β sweep across 3 OOM 清晰展现 "sweet spot"：β=0.001 太弱（gradient noise > signal），β=1.0
843	    太强（MMD 主导 BCE，probe accuracy 下降 2pp）。 Optimal β=0.05 平衡了 accuracy 和 consistency。
844	
845	    Deep-layer improvement (+4.8pp) 远大于 shallow-layer (+1.2pp)，因为 deep layers 有更大的
846	    capability-specific component（Claim 2 decomposition 所揭示），CaCLR 的 consistency loss
847	    正好 target 这个 component。这与 difficulty-capability decomposition 形成因果闭环。
848	
849	    88% improvement pass rate（35/40 model-lang pairs）：5 个 non-improving pairs 是 HIGH-resource
850	    languages（如 Qwen3-zh, Qwen3-nl）on shallow layers where ZS transfer 已经接近 ceiling。
851	
852	    '
853	  tables:
854	  - name: 'Table 10: β Sweep — Consistency Loss Effect'
855	    columns:
856	    - beta
857	    - mean_delta_auroc_vs_zs_pp
858	    - mean_delta_ece_pp
859	    - note
860	    rows:
861	    - - 0.0
862	      - 0.0
863	      - 0.0
864	      - baseline (BCE only)
865	    - - 0.001
866	      - 0.5
867	      - -0.3
868	      - marginal improvement
869	    - - 0.01
870	      - 1.8
871	      - -1.1
872	      - clear positive signal
873	    - - 0.05
874	      - 3.5
875	      - -2.4
876	      - optimal — best tradeoff
877	    - - 0.1
878	      - 3.2
879	      - -2.0
880	      - slight over-regularization
881	    - - 1.0
882	      - 0.8
883	      - -0.5
884	      - MMD dominates, probe accuracy degrades
885	  - name: 'Table 11: CaCLR vs All Methods (at best-transfer layer, both models averaged)'
886	    columns:
887	    - method
888	    - auroc_mean_20
889	    - ece_mean_20
890	    - requires_labels
891	    - key_resource
892	    rows:
893	    - - zero-shot
894	      - 0.71
895	      - 0.118
896	      - none
897	      - —
898	    - - mean-shift
899	      - 0.71
900	      - 0.118
901	      - none
902	      - —
903	    - - linear_proj_50
904	      - 0.725
905	      - 0.098
906	      - 50 parallel pairs
907	      - Procrustes
908	    - - linear_proj_200
909	      - 0.729
910	      - 0.095
911	      - 200 parallel pairs
912	      - Procrustes
913	    - - few-shot-25
914	      - 0.7
915	      - 0.102
916	      - 25 labeled
917	      - target labels
918	    - - few-shot-100
919	      - 0.727
920	      - 0.088
921	      - 100 labeled
922	      - target labels
923	    - - CaCLR
924	      - 0.745
925	      - 0.082
926	      - none
927	      - parallel activations
928	  - name: 'Table 12: CaCLR Depth Profile (Qwen3, ZS AUROC vs CaCLR AUROC)'
929	    columns:
930	    - depth_pct
931	    - zs_auroc
932	    - caclr_auroc
933	    - delta_pp
934	    rows:
935	    - - 30
936	      - 0.733
937	      - 0.745
938	      - 1.2
939	    - - 43
940	      - 0.748
941	      - 0.766
942	      - 1.8
943	    - - 55
944	      - 0.72
945	      - 0.752
946	      - 3.2
947	    - - 64
948	      - 0.69
949	      - 0.738
950	      - 4.8
951	    - - 77
952	      - 0.638
953	      - 0.688
954	      - 5.0
955	    - - 85
956	      - 0.601
957	      - 0.641
958	      - 4.0
959	  figures_description:
960	  - 'Figure 5: β sweep curve — delta AUROC (y) vs log10(β) (x), inverted-U shape peaking
961	    at β=0.05. Inset shows corresponding ECE improvement.
962	
963	    '
964	  - 'Figure 6: CaCLR depth profile — ZS (blue) vs CaCLR (red) AUROC across normalized
965	    depth. Gap widens at deep layers, demonstrating CaCLR specifically addresses deep-layer
966	    transfer degradation.
967	
968	    '
969	  analysis: 'CaCLR 作为正面方法贡献：β>0 在 deep layers 上提供 ≥2pp AUROC improvement（实际 deep-layer
970	    mean = +4.8pp），且 β sweep across 3 OOM 清晰展现最优区间。Component ablation 证实 L_consistency
971	    是主要 contributor（+2.8pp），L_SB-ECE 提供 complementary calibration improvement（+0.7pp
972	    ECE, +0.7pp AUROC synergy）。
973	
974	    CaCLR 超越 linear projection 1.5pp 是因为 end-to-end 优化可以利用 training dynamics（gradient
975	    信号引导 probe 朝 language-invariant direction 收敛），而 Procrustes 只做 post-hoc geometric
976	    correction。但差距不大 是因为 1-D MMD 的 expressiveness 有限——它只能匹配 scalar logit distributions，不能做
977	    full subspace alignment。
978	
979	    Deep-layer improvement 模式与 Claim 2 的 decomposition 一致：deep layers 的 capability-specific
980	    component 更大，CaCLR 的 consistency loss 正好 在这些 layers 有更多 signal 来 exploit。这构成 Pareto→Decomposition→CaCLR→CKA
981	    因果链的第三环。
982	
983	    '
984	- name: Difficulty-Controlled Ablation (Decomposition)
985	  plan_id: plan_004
986	  description: 'IRT difficulty probes (Ridge regression), project out difficulty direction,
987	    retrain correctness probes on residuals, evaluate transfer。10 languages (HIGH:
988	    zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) × 8 layers (20-90% depth) per model。包含
989	    random-direction control。
990	
991	    '
992	  expected_results:
993	    difficulty_probe_r2_mean: 0.68
994	    difficulty_probe_r2_range:
995	    - 0.55
996	    - 0.78
997	    difficulty_var_explained_pct: 65
998	    capability_var_explained_pct: 35
999	    difficulty_transfer_degradation_share_pct: 12
1000	    capability_transfer_degradation_share_pct: 88
1001	    decomp_capability_delta_auroc: 0.03
1002	    residual_en_auroc_drop_pp: 4.5
1003	    residual_zs_transfer_drop_pp: 0.8
1004	    random_direction_control_delta_pp: -1.2
1005	    prescriptive_accuracy: 0.78
1006	    capability_transfer_drop_by_depth:
1007	      20pct: 0.6
1008	      50pct: 2.8
1009	      80pct: 8.5
1010	  result_rationale: 'IRT difficulty 是 language-agnostic property：hard questions are
1011	    hard everywhere。Ridge regression captures this linearly (R²=0.68, 与 Civelli et
1012	    al. 的 shared difficulty finding 一致)。Difficulty 占 correctness variance 的 65% 但仅贡献
1013	    12% 的 transfer degradation， 因为 difficulty signal 本质上是 universal 的。Capability-specific
1014	    residual 仅占 35% variance 但驱动 88% 的 transfer degradation，且 degradation 随 depth
1015	    指数增长（20% depth: 0.6pp → 80% depth: 8.5pp）。
1016	
1017	    这一 decomposition 解释了 Pareto frontier 的 mechanistic origin： deep layers 的 EN probe
1018	    improvement 主要来自 capability-specific component（language-dependent competence），而这个
1019	    component 恰好是 最难 transfer 的。CaCLR 的 consistency loss works precisely because it
1020	    targets this component。
1021	
1022	    Random-direction control（-1.2pp, 随机方向 projection 反而损害）确认 difficulty direction
1023	    不是 arbitrary dimensionality reduction 的 artifact， 而是 genuine signal。
1024	
1025	    Prescriptive accuracy 78%：给定语言-layer 的 difficulty/capability ratio，预测应使用 zero-shot（difficulty-dominant）还是
1026	    CaCLR （capability-dominant）策略，在 78% 的 cases 中正确。
1027	
1028	    '
1029	  tables:
1030	  - name: 'Table 13: Decomposition Results'
1031	    columns:
1032	    - component
1033	    - var_pct
1034	    - transfer_auroc_mean
1035	    - transfer_drop_pp
1036	    - degradation_share_pct
1037	    rows:
1038	    - - full_correctness
1039	      - 100
1040	      - 0.71
1041	      - 9.0
1042	      - 100
1043	    - - difficulty_shared
1044	      - 65
1045	      - 0.698
1046	      - 1.1
1047	      - 12
1048	    - - capability_specific
1049	      - 35
1050	      - 0.615
1051	      - 12.8
1052	      - 88
1053	  - name: 'Table 14: Capability Transfer Drop by Depth'
1054	    columns:
1055	    - depth_band
1056	    - difficulty_drop_pp
1057	    - capability_drop_pp
1058	    - ratio
1059	    rows:
1060	    - - 20-30%
1061	      - 0.2
1062	      - 0.6
1063	      - 3×
1064	    - - 40-50%
1065	      - 0.6
1066	      - 2.8
1067	      - 4.7×
1068	    - - 60-70%
1069	      - 1.0
1070	      - 5.6
1071	      - 5.6×
1072	    - - 75-90%
1073	      - 1.5
1074	      - 8.5
1075	      - 5.7×
1076	  figures_description:
1077	  - 'Figure 7: Stacked area — difficulty (blue, flat) vs capability (red, exponentially
1078	    increasing) transfer degradation across depth.
1079	
1080	    '
1081	  analysis: 'Decomposition 清晰分离 transferable vs non-transferable components。 Difficulty
1082	    占大部分 variance 但 near-perfectly transfers（仅 12% degradation share），capability 占少数但驱动几乎所有
1083	    degradation。 这解释了为何 zero-shot transfer 在 mid-depth 工作（difficulty dominates there）但在
1084	    deep layers 失败（capability grows）。 Prescriptive accuracy 78% 证实 decomposition 不仅是描述性的，
1085	    而是可以指导 alignment strategy selection。
1086	
1087	    '
1088	- name: Linear Projection Sensitivity Analysis
1089	  plan_id: plan_012
1090	  description: 'Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。
1091	    Both models × 5 representative layers × 20 languages。确定最小数据需求 和 resource-tier
1092	    分层饱和。
1093	
1094	    '
1095	  expected_results:
1096	    pairs_to_95pct_overall: 42
1097	    pairs_to_95pct_HIGH: 22
1098	    pairs_to_95pct_MID: 38
1099	    pairs_to_95pct_LOW: 48
1100	    pairs_10_pct_of_200: 0.72
1101	    pairs_20_pct_of_200: 0.86
1102	    pairs_30_pct_of_200: 0.92
1103	    pairs_50_pct_of_200: 0.97
1104	    pairs_100_pct_of_200: 0.99
1105	    pairs_200_baseline_auroc_mean: 0.729
1106	    procrustes_reversal_threshold: 0.52
1107	    procrustes_helps_below_threshold_delta_pp: 3.8
1108	    procrustes_hurts_above_threshold_delta_pp: -1.2
1109	  result_rationale: 'Linear projection (Procrustes) 学习 EN→target 的 rotation matrix。
1110	    20 pairs 即可估计 dominant rotational components（correctness subspace 是 low-dimensional
1111	    的，前几个 principal angles 解释 90%+ 的 alignment structure）。42 pairs 达到 95% 因为边际的 minor
1112	    components 需要更多 data 来稳定估计。
1113	
1114	    Resource-tier stratification 清晰：HIGH languages（zh/es/de 等）的 activation distributions
1115	    与 EN 更相似，rotation matrix 的 effective rank 更低（fewer parameters to estimate），22
1116	    pairs 即可。LOW languages 需要估计更 complex rotation（effective rank 更高），48 pairs。
1117	
1118	    Procrustes effect reversal（threshold ~0.52）：当 ZS AUROC < 0.52 时， correctness direction
1119	    严重 misaligned，Procrustes 纠正旋转带来 +3.8pp。 当 ZS AUROC > 0.60 时，directions 已经 well-aligned，Procrustes
1120	    引入 estimation noise 反而 hurt -1.2pp。Threshold 0.52 对应 CKA ~0.35 （与 plan_011 的 cliff
1121	    threshold 一致）。
1122	
1123	    这一 finding 直接 actionable：practitioners 应先测 ZS transfer， only apply Procrustes
1124	    when baseline < 0.52。
1125	
1126	    '
1127	  tables:
1128	  - name: 'Table 15: Projection Sample Efficiency'
1129	    columns:
1130	    - n_pairs
1131	    - pct_of_200pair_performance
1132	    - mean_auroc
1133	    - note
1134	    rows:
1135	    - - 10
1136	      - 72
1137	      - 0.724
1138	      - unstable, high variance across runs
1139	    - - 20
1140	      - 86
1141	      - 0.728
1142	      - captures dominant rotation
1143	    - - 30
1144	      - 92
1145	      - 0.731
1146	      - near plateau for HIGH langs
1147	    - - 50
1148	      - 97
1149	      - 0.734
1150	      - near plateau for all tiers
1151	    - - 100
1152	      - 99
1153	      - 0.737
1154	      - marginal returns
1155	    - - 200
1156	      - 100
1157	      - 0.729
1158	      - baseline (reference)
1159	  - name: 'Table 16: Saturation by Resource Tier'
1160	    columns:
1161	    - tier
1162	    - pairs_to_90pct
1163	    - pairs_to_95pct
1164	    - interpretation
1165	    rows:
1166	    - - HIGH
1167	      - 15
1168	      - 22
1169	      - rotation is simple, low effective rank
1170	    - - MID
1171	      - 25
1172	      - 38
1173	      - moderate rotation complexity
1174	    - - LOW
1175	      - 35
1176	      - 48
1177	      - complex rotation, more data needed
1178	  - name: 'Table 17: Procrustes Effect Reversal'
1179	    columns:
1180	    - zs_auroc_range
1181	    - n_lang_layer_pairs
1182	    - mean_delta_pp
1183	    - direction
1184	    rows:
1185	    - - <0.45
1186	      - 42
1187	      - 5.2
1188	      - strong positive
1189	    - - 0.45-0.52
1190	      - 68
1191	      - 2.4
1192	      - moderate positive
1193	    - - 0.52-0.60
1194	      - 95
1195	      - 0.3
1196	      - near-zero (transition zone)
1197	    - - 0.60-0.70
1198	      - 88
1199	      - -1.2
1200	      - negative — hurts
1201	    - - '>0.70'
1202	      - 47
1203	      - -0.8
1204	      - slight negative
1205	  figures_description:
1206	  - 'Figure 8a: Sample efficiency curves — AUROC (y) vs n_pairs (x), three curves
1207	    for HIGH/MID/LOW tiers, showing staggered saturation.
1208	
1209	    '
1210	  - 'Figure 8b: Procrustes effect reversal — delta AUROC (y) vs ZS baseline AUROC
1211	    (x), showing sign change at ~0.52. Dot size proportional to sample count.
1212	
1213	    '
1214	  analysis: '~42 pairs to 95% performance 是 directly actionable 的 practical finding：对于大多数语言，仅需
1215	    <50 parallel sentences 即可达到接近 supervised-level alignment。Resource-tier stratification（HIGH
1216	    22 vs LOW 48 pairs）提供了 per-language guidance。
1217	
1218	    Procrustes reversal at 0.52 与 CKA threshold 0.35 形成对应： CKA < 0.35 的 language-layer
1219	    combinations 对应 ZS < 0.52（ 因为 poor alignment → poor transfer），正好是 Procrustes 帮助最大的
1220	    区域。这构成了 geometric explanation 的 practical corollary。
1221	
1222	    '
1223	- name: Probing Control Tasks — Full-Scale Hewitt & Liang (2019)
1224	  plan_id: plan_013
1225	  description: 'Extend MVP English-only control task analysis to 20 languages × 2
1226	    architectures。Train probes on randomly permuted labels, compute selectivity =
1227	    real_AUROC - control_AUROC。Identify capacity artifacts by language, layer, and
1228	    model。
1229	
1230	    '
1231	  expected_results:
1232	    en_selectivity_range:
1233	    - 0.02
1234	    - 0.26
1235	    en_selectivity_meaningful_layers:
1236	    - 16
1237	    - 20
1238	    - 24
1239	    - 27
1240	    control_artifact_rate_lowres: 0.27
1241	    control_artifact_rate_midres: 0.05
1242	    control_artifact_rate_highres: 0.03
1243	    low_res_langs_most_affected:
1244	    - yo
1245	    - ig
1246	    - te
1247	    - sw
1248	    artifact_concentration_depth: 60-100% depth
1249	    cross_lingual_selectivity_mean:
1250	      HIGH: 0.22
1251	      MID: 0.18
1252	      LOW: 0.09
1253	    languages_with_any_meaningful_selectivity: 17
1254	    control_auroc_mean_all: 0.495
1255	    control_auroc_std: 0.008
1256	  result_rationale: 'MVP English data（selectivity L27=0.262）确立了 baseline。Cross-lingual
1257	    extension 揭示了 resource-tier dependent artifact pattern：
1258	
1259	    LOW-resource languages 的 27% artifact rate 源于两个因素：(1) these languages 在 model
1260	    pretraining 中占比极低，activation distributions 相对 high-resource 更 "shallow" (less
1261	    structured)，linear probes 更容易 通过 capacity 而非 genuine signal 拟合少量 patterns；(2)
1262	    GlobalMMLU 的 low-resource translations 质量较低，引入 noise 使 correctness signal 更弱，selectivity
1263	    更接近 chance。
1264	
1265	    Mid/high-resource 的 artifact rate 极低（3-5%）因为 representation quality 高，probe 有
1266	    genuine signal 可以 leverage。
1267	
1268	    Artifacts 集中在 60-100% depth，与 CKA cliff 一致：deep layers 的 low-resource CKA 已经很低（<0.2），cross-lingual
1269	    activation structure 不足以支撑 genuine correctness probing，probe 退化为 memorizing dataset-specific
1270	    patterns。
1271	
1272	    这一 finding 是 field-level contribution：此前没有人在 cross-lingual probing 中检查 selectivity
1273	    controls。28% 的 low-resource artifact rate 意味着没有 control tasks 的 cross-lingual
1274	    probing 结果 （包括 Xiao et al.）需要谨慎解读。
1275	
1276	    '
1277	  tables:
1278	  - name: 'Table 18: Selectivity by Resource Tier and Depth'
1279	    columns:
1280	    - depth_band
1281	    - HIGH_selectivity
1282	    - MID_selectivity
1283	    - LOW_selectivity
1284	    rows:
1285	    - - 0-30%
1286	      - 0.04
1287	      - 0.03
1288	      - 0.01
1289	    - - 30-60%
1290	      - 0.18
1291	      - 0.14
1292	      - 0.06
1293	    - - 60-80%
1294	      - 0.28
1295	      - 0.22
1296	      - 0.1
1297	    - - 80-100%
1298	      - 0.25
1299	      - 0.2
1300	      - 0.08
1301	  - name: 'Table 19: Artifact Rates by Tier'
1302	    columns:
1303	    - tier
1304	    - n_lang_layer_combinations
1305	    - artifact_count
1306	    - artifact_rate
1307	    rows:
1308	    - - HIGH
1309	      - 384
1310	      - 12
1311	      - 3%
1312	    - - MID
1313	      - 336
1314	      - 17
1315	      - 5%
1316	    - - LOW
1317	      - 240
1318	      - 65
1319	      - 27%
1320	    - - total
1321	      - 960
1322	      - 94
1323	      - 10%
1324	  figures_description:
1325	  - 'Figure S1: Selectivity heatmap — language (y, ordered by tier) × depth (x). LOW-resource
1326	    rows show gray (low selectivity) at deep layers.
1327	
1328	    '
1329	  analysis: '27% low-resource artifact rate 是 methodological warning for the field：
1330	    cross-lingual probing studies 如果不做 selectivity checks 会高估 low-resource transfer
1331	    quality。重要的是 artifacts 集中在 low-resource + deep layers，不波及 mid/high-resource 或
1332	    shallow layers，因此本文的 核心 Pareto/CKA 分析（主要基于 mid/high-resource patterns）不受影响。
1333	
1334	    '
1335	- name: Cross-Lingual Correctness-Confidence Orthogonality
1336	  plan_id: plan_005
1337	  description: 'Extract verbalized confidence direction, compute cosine similarity
1338	    with correctness direction, 20 languages × 2 architectures。 Supporting evidence
1339	    for Claim 4 (subsection)。
1340	
1341	    '
1342	  expected_results:
1343	    cosine_mean_overall: 0.05
1344	    cosine_range:
1345	    - 0.02
1346	    - 0.09
1347	    cosine_en: 0.03
1348	    all_below_0p10: true
1349	    qwen3_cosine_mean: 0.046
1350	    llama4_cosine_mean: 0.054
1351	    HIGH_cosine_mean: 0.038
1352	    MID_cosine_mean: 0.052
1353	    LOW_cosine_mean: 0.072
1354	    resource_tier_correlation: -0.66
1355	  result_rationale: 'Miao & Ungar (2026) 在 English 7-8B 上测得 cosine < 0.04。Extension
1356	    to 20 languages × 大模型应保持 near-orthogonality（< 0.10），因为这反映 transformer 的 structural
1357	    property：verbalized confidence 由 language modeling head 从 surface-level token
1358	    probabilities 生成，correctness 由 intermediate representations geometry 编码，两者 architecturally
1359	    decoupled。Low-resource 略高（0.072 mean）因为 confidence elicitation in low-resource
1360	    languages 更 noisy，不完全 decoupled。Resource-tier gradient（r=-0.66）说明更好的 multilingual
1361	    training → 更清晰的 correctness/confidence separation。
1362	
1363	    '
1364	  tables:
1365	  - name: 'Table 20: Orthogonality by Tier (cosine similarity)'
1366	    columns:
1367	    - tier
1368	    - n_langs
1369	    - qwen3_mean
1370	    - llama4_mean
1371	    - combined_mean
1372	    rows:
1373	    - - HIGH
1374	      - 8
1375	      - 0.035
1376	      - 0.041
1377	      - 0.038
1378	    - - MID
1379	      - 7
1380	      - 0.048
1381	      - 0.056
1382	      - 0.052
1383	    - - LOW
1384	      - 5
1385	      - 0.066
1386	      - 0.078
1387	      - 0.072
1388	  figures_description:
1389	  - 'Figure S2: Cosine similarity violin plots by resource tier, all below 0.10 threshold
1390	    line.
1391	
1392	    '
1393	  analysis: 'Orthogonality universally holds (39/40 pairs below 0.10, all 40 below
1394	    0.095)，confirming output-based calibration methods are structurally limited across
1395	    languages。Resource-tier gradient 是新 finding，但 effect size 小（range only 0.034），作为
1396	    subsection 足够。
1397	
1398	    '
1399	- name: Probe Complexity Comparison
1400	  plan_id: plan_006
1401	  description: 'Logistic regression vs 2-layer MLP at each probed layer, both models。
1402	    Validates linear probe choice for transfer。
1403	
1404	    '
1405	  expected_results:
1406	    logreg_en_auroc_best: 0.81
1407	    mlp_en_auroc_best: 0.83
1408	    mlp_en_gain_pp: 2.0
1409	    logreg_zs_drop_mean_pp: 9.0
1410	    mlp_zs_drop_mean_pp: 14.5
1411	    logreg_transfer_advantage_pp: 5.5
1412	    logreg_advantage_shallow_pp: 2.0
1413	    logreg_advantage_deep_pp: 8.2
1414	  result_rationale: 'Linear probes learn 一个 hyperplane，跨语言泛化因为 correctness subspace
1415	    是 near-universal linear structure（subspace angle ~12° from plan_011）。 MLPs fit
1416	    nonlinear decision boundaries that overfit EN-specific feature interactions，gaining
1417	    +2pp EN AUROC but losing 5.5pp transfer。Gap 在 deep layers 放大（+8.2pp advantage
1418	    for logreg at 80% depth）因为 deep layers 有更多 language-specific nonlinear structure
1419	    for MLP to exploit。 This justifies logreg as primary probe and supports geometric
1420	    interpretation of Pareto frontier。
1421	
1422	    '
1423	  tables:
1424	  - name: 'Table S2: Probe Complexity (Qwen3, at EN-optimal layer)'
1425	    columns:
1426	    - probe_type
1427	    - en_auroc
1428	    - zs_mean_20
1429	    - zs_drop_pp
1430	    rows:
1431	    - - logistic_regression
1432	      - 0.81
1433	      - 0.72
1434	      - 9.0
1435	    - - mlp_2layer_h128
1436	      - 0.83
1437	      - 0.685
1438	      - 14.5
1439	  figures_description:
1440	  - 'Figure S3: Transfer drop (pp) vs depth, logreg (blue) vs MLP (red). MLP diverges
1441	    sharply past 60% depth.
1442	
1443	    '
1444	  analysis: 'Linear probes 为 cross-lingual transfer 的 optimal choice：牺牲 2pp EN performance
1445	    换取 5.5pp transfer improvement。Depth interaction confirms nonlinear language-specific
1446	    features drive deep-layer degradation。
1447	
1448	    '
1449	- name: Cross-Benchmark Generalization (Belebele + MMLU-ProX)
1450	  plan_id: plan_007
1451	  description: 'Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages
1452	    each)。Tests domain generalization。
1453	
1454	    '
1455	  expected_results:
1456	    belebele_zs_mean_20: 0.695
1457	    belebele_caclr_mean_20: 0.728
1458	    belebele_caclr_delta_pp: 3.3
1459	    mmlupx_zs_mean_20: 0.68
1460	    mmlupx_caclr_mean_20: 0.715
1461	    mmlupx_caclr_delta_pp: 3.5
1462	    cross_benchmark_caclr_cv: 0.04
1463	  result_rationale: 'Belebele (reading comprehension) 和 MMLU-ProX (harder factual)
1464	    的 baseline 略低于 GlobalMMLU 因为 domain shift，但 CaCLR 的 improvement 幅度 consistent（3.3-3.5pp
1465	    vs GlobalMMLU 的 3.5pp）。Low CV (0.04) 证实 CaCLR addresses 一个 fundamental representation
1466	    alignment issue 而非 overfitting to specific benchmark。
1467	
1468	    '
1469	  tables:
1470	  - name: 'Table 21: Cross-Benchmark CaCLR Generalization'
1471	    columns:
1472	    - benchmark
1473	    - zs_mean_20
1474	    - caclr_mean_20
1475	    - delta_pp
1476	    rows:
1477	    - - GlobalMMLU
1478	      - 0.71
1479	      - 0.745
1480	      - 3.5
1481	    - - Belebele
1482	      - 0.695
1483	      - 0.728
1484	      - 3.3
1485	    - - MMLU-ProX
1486	      - 0.68
1487	      - 0.715
1488	      - 3.5
1489	  figures_description:
1490	  - 'Figure S4: CaCLR improvement by benchmark × language, showing consistent gains.
1491	
1492	    '
1493	  analysis: 'CaCLR generalizes across benchmarks with low variance。Cross-benchmark
1494	    consistency is the strongest defense against overfitting concerns。
1495	
1496	    '
1497	- name: Quantization Validation Ablation
1498	  plan_id: plan_010
1499	  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4
1500	    vs FP16 for Qwen3-235B at 5 layers, 5% subset。
1501	
1502	    '
1503	  expected_results:
1504	    llama4_w4a16_fp16_auroc_diff_mean_pp: 0.3
1505	    llama4_w4a16_fp16_auroc_diff_max_pp: 0.8
1506	    llama4_rank_correlation: 0.996
1507	    qwen3_int4_fp16_auroc_diff_mean_pp: 0.5
1508	    qwen3_int4_fp16_auroc_diff_max_pp: 1.1
1509	    qwen3_rank_correlation: 0.994
1510	    conclusion: quantization introduces negligible distortion for probing
1511	  result_rationale: 'W4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation
1512	    geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction
1513	    的 angular structure 仍 robust（0.5pp mean diff）， 因为 quantization noise 近似 isotropic，不
1514	    preferentially distort correctness-relevant directions。Rank correlation > 0.994
1515	    确认 Pareto frontier ordering 完全保留。Qwen3 的 slightly higher diff (0.5 vs 0.3) 因为
1516	    Int4 比 W4A16 更 lossy。
1517	
1518	    '
1519	  tables:
1520	  - name: 'Table S3: Quantization Comparison (5 representative layers)'
1521	    columns:
1522	    - model
1523	    - layer
1524	    - fp16_auroc
1525	    - quant_auroc
1526	    - diff_pp
1527	    rows:
1528	    - - Llama4
1529	      - 8
1530	      - 0.637
1531	      - 0.634
1532	      - 0.3
1533	    - - Llama4
1534	      - 16
1535	      - 0.737
1536	      - 0.735
1537	      - 0.2
1538	    - - Llama4
1539	      - 28
1540	      - 0.784
1541	      - 0.781
1542	      - 0.3
1543	    - - Llama4
1544	      - 36
1545	      - 0.792
1546	      - 0.789
1547	      - 0.3
1548	    - - Llama4
1549	      - 44
1550	      - 0.774
1551	      - 0.77
1552	      - 0.4
1553	    - - Qwen3
1554	      - 20
1555	      - 0.712
1556	      - 0.708
1557	      - 0.4
1558	    - - Qwen3
1559	      - 36
1560	      - 0.78
1561	      - 0.775
1562	      - 0.5
1563	    - - Qwen3
1564	      - 52
1565	      - 0.808
1566	      - 0.803
1567	      - 0.5
1568	    - - Qwen3
1569	      - 68
1570	      - 0.812
1571	      - 0.806
1572	      - 0.6
1573	    - - Qwen3
1574	      - 80
1575	      - 0.807
1576	      - 0.8
1577	      - 0.7
1578	  figures_description:
1579	  - 'Figure S5: Quant vs FP16 scatter, y=x diagonal, tight clustering.
1580	
1581	    '
1582	  analysis: 'Quantization safe for both models。Preempts reviewer concern #5。
1583	
1584	    '
1585	- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)
1586	  plan_id: plan_008
1587	  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers, FP16), 20 languages。Provides
1588	    dense vs MoE contrast for camera-ready。
1589	
1590	    '
1591	  expected_results:
1592	    en_best_auroc: 0.8
1593	    en_best_layer_idx: 45
1594	    zs_mean_20lang: 0.71
1595	    zs_best_transfer_layer_idx: 36
1596	    global_spearman_rho: -0.85
1597	    per_lang_rho_median: -0.58
1598	    caclr_delta_vs_zs_pp: 3.0
1599	    simpson_partial_rho: 0.44
1600	    simpson_partial_p: 0.004
1601	  result_rationale: 'Gemma 4 31B Dense 是理想的第三 data point：dense architecture（vs two
1602	    MoE models），different pretraining recipe（Google vs Alibaba/Meta）， 60 layers（between
1603	    Qwen 94 and Llama 48）。EN AUROC 0.80 低于 MoE models 因为 31B dense < 22B MoE active
1604	    (MoE routing 提供 effective capacity boost)。Pareto strength (ρ=-0.85) 介于 Qwen (-0.91)
1605	    和 Llama (-0.78) 之间。Simpson''s partial correlation 仍然显著 (rho=+0.44, p=0.004)， 确认
1606	    geometric insight 是 architecture-universal 而非 MoE-specific。
1607	
1608	    '
1609	  tables:
1610	  - name: 'Table 22: Three-Architecture Summary'
1611	    columns:
1612	    - model
1613	    - type
1614	    - layers
1615	    - en_best
1616	    - zs_mean_20
1617	    - pareto_rho
1618	    - simpson_partial_rho
1619	    - caclr_delta_pp
1620	    rows:
1621	    - - Qwen3-235B
1622	      - MoE
1623	      - 94
1624	      - 0.81
1625	      - 0.72
1626	      - -0.91
1627	      - 0.48
1628	      - 3.7
1629	    - - Llama4 Scout
1630	      - MoE
1631	      - 48
1632	      - 0.79
1633	      - 0.7
1634	      - -0.78
1635	      - 0.41
1636	      - 3.3
1637	    - - Gemma4 31B
1638	      - Dense
1639	      - 60
1640	      - 0.8
1641	      - 0.71
1642	      - -0.85
1643	      - 0.44
1644	      - 3.0
1645	  figures_description:
1646	  - 'Figure 9: Three-architecture Pareto frontiers overlaid (normalized depth %).
1647	    Remarkably similar shapes.
1648	
1649	    '
1650	  analysis: 'Three-architecture replication 是 universality claim 最强证据： Simpson''s
1651	    Paradox 在 dense 和 MoE 上都成立，Pareto frontier 在 55-60% depth 处一致出现 knee，CaCLR 提供
1652	    3-3.7pp consistent gain。 Dense vs MoE 的差异 minimal — phenomenon 是 transformer depth
1653	    的 property 而非 routing architecture 的。
1654	
1655	    '
1656	- name: Extended Language Coverage (Camera-Ready)
1657	  plan_id: plan_009
1658	  description: 'Expand from 20 to 50+ languages for camera-ready。
1659	
1660	    '
1661	  expected_results:
1662	    total_languages: 50
1663	    zs_pass_rate_50lang: 0.84
1664	    zs_auroc_above_060_count: 42
1665	    caclr_improvement_positive_count: 47
1666	    mean_zs_auroc_50lang: 0.69
1667	    mean_caclr_auroc_50lang: 0.72
1668	    pareto_frontier_holds_all_langs: true
1669	    new_families:
1670	    - Austronesian
1671	    - Dravidian
1672	    - Uralic
1673	    - Kartvelian
1674	    - Niger-Congo_B
1675	  result_rationale: 'Expansion 主要增加 mid-resource 语言（Indonesian, Finnish, Georgian,
1676	    Tamil, Telugu, etc.），大多 fall in 0.65-0.75 AUROC range。Extremely low-resource 语言（Amharic,
1677	    Khmer, Lao）可能 < 0.55 但代表 edge cases。 CaCLR 在 94% 的新增语言上 positive 因为 consistency
1678	    loss mechanism 是 language-agnostic。Pareto frontier structure 在 50 languages 上
1679	    完全保持。
1680	
1681	    '
1682	  tables:
1683	  - name: 'Table 23: Extended Coverage by Tier'
1684	    columns:
1685	    - tier
1686	    - n_langs
1687	    - zs_mean
1688	    - caclr_mean
1689	    - caclr_gain_pp
1690	    rows:
1691	    - - HIGH
1692	      - 10
1693	      - 0.75
1694	      - 0.78
1695	      - 2.8
1696	    - - MID
1697	      - 24
1698	      - 0.71
1699	      - 0.74
1700	      - 3.5
1701	    - - LOW
1702	      - 12
1703	      - 0.62
1704	      - 0.66
1705	      - 4.2
1706	    - - VERY_LOW
1707	      - 4
1708	      - 0.53
1709	      - 0.58
1710	      - 5.0
1711	  figures_description:
1712	  - 'Figure 10: World map with per-language CaCLR AUROC, colored by performance tier.
1713	    Broad geographic/typological coverage.
1714	
1715	    '
1716	  analysis: 50-language extension 确认 all findings at scale。Resource-tier gradient
1717	    smooth, CaCLR benefit inversely correlated with resource level, no language family
1718	    shows anomalous behavior。
1719	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adc79fb7-163e-4c82-aadd-fb04aaeee4a5",
  "isSidechain": false,
  "promptId": "7f6384cd-15ed-4514-b679-c96259e865e9",
  "type": "user",
  "uuid": "7602f47e-f70e-4176-ab0d-d0f246d46397",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: '原始 framing 完全成立。以 Simpson''s Paradox 几何洞见为核心新颖性开篇—— raw CKA-transfer\n  correlation 为负（depth confound），partial correlation controlling for depth 在双架构上均显著为正（p\n  < 0.01），揭示 within-layer CKA genuinely predicts transfer quality。CaCLR 作为正面方法贡献（+3.5pp\n  mean over ZS），不是 headline 但 构成因果链第三环。标题强调 ''geometric analysis reveals when and\n  why cross-lingual calibration transfer succeeds''。四条 claim 完整因果链保留：Pareto discovery（architecture-\n  dependent depth-transferability tradeoff）→ Decomposition analysis（difficulty vs\n  capability separation）→ CaCLR method（consistency loss provides measurable gain at\n  deep layers）→ CKA geometric explanation（Simpson''s Paradox, subspace persistence）。\n  Control task warning（28% low-resource artifacts）和 linear projection sample efficiency\n  （~42 pairs to 95%）作为加分实证贡献。Procrustes effect reversal（threshold ~0.52） 为 practitioner\n  提供直接指导。无需弱化任何 claims。\n\n  '\nimagined_experiments:\n- name: Full Pareto Frontier — Qwen3-235B-A22B\n  plan_id: plan_001\n  description: '94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th), 20\n    typologically diverse languages, English logistic regression probes, 5 transfer\n    conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100,\n    CaCLR。重点验证 MVP 发现的 strong depth-transferability tradeoff 是否在大模型上保持。\n\n    '\n  expected_results:\n    en_best_auroc: 0.81\n    en_best_layer_idx: 72\n    en_auroc_range:\n    - 0.58\n    - 0.81\n    en_ece_raw_best: 0.168\n    zs_mean_auroc_20lang_best_transfer_layer: 0.72\n    zs_best_transfer_layer_idx: 52\n    zs_pass_rate_20lang: 0.9\n    zs_fail_langs:\n    - yo\n    - te\n    zs_auroc_by_tier:\n      HIGH_mean: 0.76\n      MID_mean: 0.72\n      LOW_mean: 0.63\n    zs_auroc_selected:\n      zh: 0.77\n      es: 0.76\n      fr: 0.76\n      de: 0.77\n      ja: 0.75\n      nl: 0.76\n      pt: 0.75\n      it: 0.75\n      ar: 0.73\n      hi: 0.71\n      ko: 0.72\n      tr: 0.71\n      ru: 0.74\n      vi: 0.7\n      th: 0.69\n      sw: 0.63\n      bn: 0.65\n      yo: 0.57\n      ig: 0.61\n      te: 0.58\n    per_lang_spearman_rho_median: -0.64\n    per_lang_significant_at_005: 15\n    global_spearman_rho: -0.91\n    global_spearman_p: 0.0001\n    pareto_frontier_layers:\n    - 40\n    - 44\n    - 48\n    - 52\n    - 56\n    pareto_en_zs_gap_at_knee_pp: 4.2\n    mean_shift_delta_auroc: 0.0\n    linproj_200pairs_mean_auroc: 0.74\n    fewshot_25_mean_auroc: 0.708\n    fewshot_100_mean_auroc: 0.735\n  result_rationale: 'Qwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 3×，log-linear\n    probing scaling 预期 EN AUROC 从 0.754 提升至 ~0.81。94 层深网络使 depth-transferability tradeoff\n    比 28 层 MVP 更显著：EN-optimal layer (L72, 77% depth) 与 ZS-optimal layer (L52, 55%\n    depth) 之间有 20 层间隔（MVP 仅 3 层）。Strong Pareto 源于 Qwen 架构特征：MoE routing 在深层产生 language-specific\n    expert 激活模式， 导致 correctness direction 的 cross-lingual alignment 在 L60 后急剧下降。 15/20\n    languages 的 per-language Spearman rho 显著为负，表明 tradeoff 是 跨语言一致的。2 个 fail 语言（yo,\n    te）的 AUROC < 0.60 因为 Qwen3 pretraining corpus 中 Yoruba/Telugu 占比极低（<0.1%），embedding\n    层的 representation quality 即不足以支撑 correctness signal。Mean-shift ΔAUROC ≡ 0 因为 StandardScaler\n    + LR 下 mean-shift 对 AUROC 无影响（已在 MVP 中数学证明）。 Linear projection (200 pairs) 提供\n    +2pp 因为 Procrustes alignment 捕获了 correctness subspace 的旋转，但不触及 distributional\n    matching。\n\n    '\n  tables:\n  - name: 'Table 1: Qwen3-235B Pareto Frontier (selected layers)'\n    columns:\n    - layer_idx\n    - depth_pct\n    - en_auroc\n    - zs_mean_20\n    - zs_drop_pp\n    - on_pareto\n    rows:\n    - - 4\n      - 4\n      - 0.58\n      - 0.572\n      - 0.8\n      - false\n    - - 12\n      - 13\n      - 0.645\n      - 0.632\n      - 1.3\n      - false\n    - - 20\n      - 21\n      - 0.71\n      - 0.695\n      - 1.5\n      - false\n    - - 28\n      - 30\n      - 0.752\n      - 0.733\n      - 1.9\n      - false\n    - - 36\n      - 38\n      - 0.778\n      - 0.752\n      - 2.6\n      - false\n    - - 40\n      - 43\n      - 0.788\n      - 0.748\n      - 4.0\n      - true\n    - - 44\n      - 47\n      - 0.796\n      - 0.74\n      - 5.6\n      - true\n    - - 48\n      - 51\n      - 0.802\n      - 0.732\n      - 7.0\n      - true\n    - - 52\n      - 55\n      - 0.806\n      - 0.72\n      - 8.6\n      - true\n    - - 56\n      - 60\n      - 0.808\n      - 0.706\n      - 10.2\n      - true\n    - - 60\n      - 64\n      - 0.81\n      - 0.69\n      - 12.0\n      - false\n    - - 68\n      - 72\n      - 0.81\n      - 0.661\n      - 14.9\n      - false\n    - - 72\n      - 77\n      - 0.81\n      - 0.638\n      - 17.2\n      - false\n    - - 80\n      - 85\n      - 0.805\n      - 0.601\n      - 20.4\n      - false\n    - - 88\n      - 94\n      - 0.792\n      - 0.558\n      - 23.4\n      - false\n    - - 92\n      - 98\n      - 0.778\n      - 0.531\n      - 24.7\n      - false\n  - name: 'Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3'\n    columns:\n    - language\n    - tier\n    - spearman_rho\n    - p_value\n    - significant\n    rows:\n    - - zh\n      - HIGH\n      - -0.72\n      - 0.001\n      - true\n    - - es\n      - HIGH\n      - -0.68\n      - 0.002\n      - true\n    - - fr\n      - HIGH\n      - -0.7\n      - 0.001\n      - true\n    - - de\n      - HIGH\n      - -0.69\n      - 0.002\n      - true\n    - - ja\n      - HIGH\n      - -0.74\n      - 0.001\n      - true\n    - - nl\n      - HIGH\n      - -0.67\n      - 0.003\n      - true\n    - - pt\n      - MID\n      - -0.65\n      - 0.004\n      - true\n    - - it\n      - MID\n      - -0.66\n      - 0.003\n      - true\n    - - ar\n      - MID\n      - -0.71\n      - 0.001\n      - true\n    - - hi\n      - MID\n      - -0.63\n      - 0.005\n      - true\n    - - ko\n      - MID\n      - -0.67\n      - 0.003\n      - true\n    - - tr\n      - MID\n      - -0.62\n      - 0.006\n      - true\n    - - ru\n      - MID\n      - -0.69\n      - 0.002\n      - true\n    - - vi\n      - MID\n      - -0.61\n      - 0.008\n      - true\n    - - th\n      - MID\n      - -0.58\n      - 0.012\n      - true\n    - - sw\n      - LOW\n      - -0.52\n      - 0.025\n      - true\n    - - bn\n      - LOW\n      - -0.55\n      - 0.018\n      - false\n    - - yo\n      - LOW\n      - -0.48\n      - 0.042\n      - false\n    - - ig\n      - LOW\n      - -0.51\n      - 0.028\n      - false\n    - - te\n      - LOW\n      - -0.45\n      - 0.058\n      - false\n  figures_description:\n  - 'Figure 1a: Pareto frontier scatter (EN AUROC x-axis vs ZS mean AUROC y-axis),\n    24 points, 5 Pareto-optimal layers marked red. Clear convex knee at ~55% depth.\n\n    '\n  - 'Figure 1b: Heatmap — ZS AUROC by language (y-axis, ordered by resource tier)\n    × normalized depth (x-axis). Warm mid-band, low-resource rows cool earlier at\n    shallower depth than high-resource rows.\n\n    '\n  analysis: 'Qwen3-235B 展现 strong, consistent depth-transferability tradeoff： global\n    Spearman ρ = -0.91 (p < 0.001), 15/20 per-language ρ 显著为负。 Pareto frontier 包含\n    5 层 (L40-L56)，knee 在 ~55% depth。EN-optimal (L72) 与 ZS-optimal (L52) 相隔 20 层 /\n    22pp depth，远大于 MVP 的 3 层 间隔。这证实 tradeoff 在大模型上不是减弱而是放大——更深的网络有更多 空间进行 language-specific\n    specialization。High-resource 语言在 Pareto knee 以下也保持 AUROC > 0.74，但 low-resource\n    在 70% depth 后急剧下降。 这与 CKA 分析一致：CKA 在 L60 后的 cliff 解释了为何 deep-layer transfer 对\n    low-resource 影响更大（CKA 基线更低，cliff 更早触及）。\n\n    '\n- name: Full Pareto Frontier — Llama 4 Scout\n  plan_id: plan_002\n  description: '48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every\n    4th), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B 的 weak/mixed tradeoff\n    pattern 是否是 Llama 架构家族特征。\n\n    '\n  expected_results:\n    en_best_auroc: 0.79\n    en_best_layer_idx: 36\n    en_auroc_range:\n    - 0.56\n    - 0.79\n    en_ece_raw_best: 0.182\n    zs_mean_auroc_20lang_best_transfer_layer: 0.7\n    zs_best_transfer_layer_idx: 28\n    zs_pass_rate_20lang: 0.85\n    zs_fail_langs:\n    - yo\n    - te\n    - ig\n    zs_auroc_by_tier:\n      HIGH_mean: 0.74\n      MID_mean: 0.7\n      LOW_mean: 0.61\n    per_lang_spearman_rho_median: -0.28\n    per_lang_significant_at_005: 6\n    per_lang_positive_rho_langs:\n    - ar\n    - hi\n    - ko\n    global_spearman_rho: -0.78\n    global_spearman_p: 0.003\n    pareto_frontier_layers:\n    - 20\n    - 24\n    - 28\n    mean_shift_delta_auroc: 0.0\n    linproj_200pairs_mean_auroc: 0.718\n    fewshot_25_mean_auroc: 0.692\n    fewshot_100_mean_auroc: 0.718\n  result_rationale: 'Llama 4 Scout 延续 MVP Llama-3.1-8B 的 weak tradeoff 模式。虽然 global\n    Spearman ρ = -0.78 仍然显著（12 data points, p=0.003），但 per-language 分析揭示了明显的异质性：仅\n    6/20 languages 有显著负 ρ，而 ar/hi/ko 展现正 ρ（深层 transfer 反而改善）。这与 MVP 完全一致（ar/ko 在 L31\n    优于 L20），且可归因于 Llama 架构的 multilingual training recipe：Meta 的训练策略使 ar/hi/ko 在深层保持更好的\n    cross-lingual alignment，可能 因为这些语言在 pretraining 中与 English 有更多 code-switching 数据。\n    Global rho 仍然显著是因为大多数语言确实有弱负趋势，但 per-language 分析揭示这不是 universal pattern。与 Qwen3\n    的对比清晰：Qwen3 的 15/20 significant vs Llama4 的 6/20，median rho -0.64 vs -0.28。这一\n    architecture-dependent tradeoff strength 是 Claim 1 的核心发现。\n\n    '\n  tables:\n  - name: 'Table 3: Llama 4 Scout Pareto Frontier'\n    columns:\n    - layer_idx\n    - depth_pct\n    - en_auroc\n    - zs_mean_20\n    - zs_drop_pp\n    - on_pareto\n    rows:\n    - - 4\n      - 8\n      - 0.56\n      - 0.552\n      - 0.8\n      - false\n    - - 8\n      - 17\n      - 0.635\n      - 0.625\n      - 1.0\n      - false\n    - - 12\n      - 25\n      - 0.695\n      - 0.682\n      - 1.3\n      - false\n    - - 16\n      - 33\n      - 0.735\n      - 0.718\n      - 1.7\n      - false\n    - - 20\n      - 42\n      - 0.758\n      - 0.724\n      - 3.4\n      - true\n    - - 24\n      - 50\n      - 0.772\n      - 0.714\n      - 5.8\n      - true\n    - - 28\n      - 58\n      - 0.782\n      - 0.7\n      - 8.2\n      - true\n    - - 32\n      - 67\n      - 0.789\n      - 0.681\n      - 10.8\n      - false\n    - - 36\n      - 75\n      - 0.79\n      - 0.655\n      - 13.5\n      - false\n    - - 40\n      - 83\n      - 0.785\n      - 0.625\n      - 16.0\n      - false\n    - - 44\n      - 92\n      - 0.772\n      - 0.589\n      - 18.3\n      - false\n    - - 48\n      - 100\n      - 0.748\n      - 0.548\n      - 20.0\n      - false\n  - name: 'Table 4: Architecture-Dependent Pareto Comparison'\n    columns:\n    - metric\n    - Qwen3_235B\n    - Llama4_Scout\n    - interpretation\n    rows:\n    - - global_rho\n      - -0.91\n      - -0.78\n      - both significant but Qwen stronger\n    - - per_lang_sig_count\n      - 15/20\n      - 6/20\n      - Qwen consistent, Llama mixed\n    - - median_per_lang_rho\n      - -0.64\n      - -0.28\n      - 2.3x difference in effect size\n    - - positive_rho_langs\n      - 0\n      - 3\n      - Llama has ar/hi/ko reversed\n    - - best_transfer_depth_pct\n      - 55\n      - 58\n      - comparable location\n    - - en_zs_gap_at_knee_pp\n      - 4.2\n      - 3.4\n      - comparable magnitude\n  - name: 'Table 5: Transfer Conditions Comparison (both models, at best-transfer\n      layer)'\n    columns:\n    - condition\n    - Qwen3_mean_20\n    - Llama4_mean_20\n    - combined_mean\n    rows:\n    - - zero-shot\n      - 0.72\n      - 0.7\n      - 0.71\n    - - mean-shift\n      - 0.72\n      - 0.7\n      - 0.71\n    - - linear_proj_200\n      - 0.74\n      - 0.718\n      - 0.729\n    - - few-shot-25\n      - 0.708\n      - 0.692\n      - 0.7\n    - - few-shot-100\n      - 0.735\n      - 0.718\n      - 0.727\n  figures_description:\n  - 'Figure 2: Overlaid Pareto frontiers (normalized depth), Qwen3 in blue, Llama4\n    in orange. Qwen3 shifted up-right with steeper descent; Llama4 flatter with more\n    scatter at deep layers.\n\n    '\n  - 'Figure 3: Per-language Spearman ρ distribution: Qwen3 (left) tightly clustered\n    around -0.65; Llama4 (right) spread from -0.50 to +0.35, ar/hi/ko clearly positive.\n\n    '\n  analysis: 'Architecture-dependent Pareto strength 是 Claim 1 的核心。两个架构的 global rho\n    都显著（满足 pareto_spearman_rho_significant_archs = 2 的 约束），但 effect size 差异明显。Qwen3\n    的 strong tradeoff 意味着 practitioner 必须在 EN accuracy 和 transfer quality 之间做明确选择；\n    Llama4 的 weak tradeoff 意味着某些语言（ar, hi, ko）可以 \"free-ride\" 深层的 EN improvement 而不牺牲\n    transfer。这一差异无法从 domain adaptation theory 预测——它是架构特有的 empirical finding。 Best-transfer\n    depth 在两个架构上收敛至 55-58%，暗示一个 universal \"mid-depth transfer zone\"，但 frontier 的 steepness\n    是 architecture-specific。\n\n    '\n- name: CKA Cross-Lingual Similarity & Simpson's Paradox Analysis\n  plan_id: plan_011\n  description: 'Linear CKA (EN vs each target) at every probed layer, 20 languages\n    × 2 models。核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b)\n    partial Spearman controlling for normalized depth — THE single most important\n    analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。验证\n    pilot finding 的 Simpson''s Paradox 在 full-scale 上双架构复现。\n\n    '\n  expected_results:\n    qwen3_raw_rho: -0.36\n    qwen3_raw_p: 0.0001\n    llama4_raw_rho: -0.41\n    llama4_raw_p: 0.0001\n    qwen3_partial_rho: 0.48\n    qwen3_partial_p: 0.002\n    qwen3_partial_bootstrap_ci_95:\n    - 0.31\n    - 0.62\n    llama4_partial_rho: 0.41\n    llama4_partial_p: 0.008\n    llama4_partial_bootstrap_ci_95:\n    - 0.22\n    - 0.57\n    simpson_paradox_confirmed_both_archs: true\n    qwen3_per_layer_positive_count: 18\n    qwen3_per_layer_significant_count: 6\n    llama4_per_layer_positive_count: 9\n    llama4_per_layer_significant_count: 3\n    qwen3_cka_peak_layer: 16\n    qwen3_cka_peak_value: 0.82\n    qwen3_cka_at_en_optimal_layer: 0.28\n    qwen3_cka_cliff_onset_depth_pct: 55\n    llama4_cka_peak_layer: 12\n    llama4_cka_peak_value: 0.84\n    llama4_cka_at_en_optimal_layer: 0.35\n    llama4_cka_cliff_onset_depth_pct: 50\n    transfer_collapse_cka_threshold: 0.35\n    below_threshold_mean_zs_auroc: 0.58\n    above_threshold_mean_zs_auroc: 0.72\n    correctness_subspace_angle_within_layer_mean_deg: 12.4\n    correctness_subspace_angle_across_layer_mean_deg: 38.7\n    correctness_direction_persists_despite_global_cka_decline: true\n  result_rationale: 'Simpson''s Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper\n    → representations diverge → CKA drops）和 transfer AUROC（deeper → EN probe stronger\n    → higher absolute AUROC up to a point），创造了一个 confound。 Raw pooled correlation\n    为负是因为 shallow layers 有 high CKA 但 low AUROC （probe 本身弱），deep layers 有 low CKA\n    但 higher AUROC（probe 强虽然 transfer degrades）。控制 depth 后，within 每个 layer，higher\n    CKA 的 语言确实有 better transfer，partial rho 为正。\n\n    MVP pilot（Llama, 5 langs × 9 layers）已展现 rho=+0.41, p=0.006。 Full-scale（20 langs\n    × 12-24 layers）增强统计 power：per-layer test 从 n=5 增至 n=20，partial correlation 的 bootstrap\n    CI 不含零。\n\n    Qwen3 partial rho (0.48) 高于 Llama4 (0.41)，与 Qwen 的 steeper CKA cliff 一致：Qwen 的\n    CKA 变异范围更大（peak 0.82 → floor 0.28 vs Llama 0.84 → 0.35），为 partial correlation\n    提供更多 signal。\n\n    MVP Qwen pilot 仅 rho=+0.18 (p=0.274)，full-scale上升至 0.48 是因为： (1) n 从 5 增至 20 语言，power\n    大幅提升；(2) 20 语言覆盖更宽的 CKA 范围（增加了 yo/ig/te 等极低 CKA 语言和 nl/pt 等高 CKA 语言）， 扩大了 within-layer\n    variance。\n\n    CKA cliff threshold ~0.35 标记了 \"transfer collapse zone\"：当 CKA 低于此阈值时，correctness\n    direction 的 cross-lingual overlap 不足以 支撑 zero-shot transfer。Subspace angle analysis\n    揭示 correctness direction 在同一 layer 内跨语言仅旋转 ~12°（highly aligned），但跨 layer 旋转 ~39°（significant\n    drift），解释了为何 within-layer CKA 预测 transfer 但 raw pooled 不预测。\n\n    '\n  tables:\n  - name: 'Table 6: Simpson''s Paradox — Raw vs Partial Correlation'\n    columns:\n    - model\n    - analysis\n    - spearman_rho\n    - p_value\n    - bootstrap_95CI\n    - interpretation\n    rows:\n    - - Qwen3-235B\n      - raw pooled (CKA vs ZS AUROC)\n      - -0.36\n      - <0.001\n      - '[-0.44, -0.27]'\n      - negative — depth confound\n    - - Qwen3-235B\n      - partial (controlling depth)\n      - 0.48\n      - 0.002\n      - '[+0.31, +0.62]'\n      - positive — genuine geometric signal\n    - - Llama4 Scout\n      - raw pooled (CKA vs ZS AUROC)\n      - -0.41\n      - <0.001\n      - '[-0.50, -0.31]'\n      - negative — depth confound\n    - - Llama4 Scout\n      - partial (controlling depth)\n      - 0.41\n      - 0.008\n      - '[+0.22, +0.57]'\n      - positive — genuine geometric signal\n  - name: 'Table 7: Per-Layer CKA-Transfer Correlation (Qwen3, selected layers)'\n    columns:\n    - layer_idx\n    - depth_pct\n    - mean_CKA_20lang\n    - spearman_rho_n20\n    - p_value\n    rows:\n    - - 12\n      - 13\n      - 0.78\n      - 0.52\n      - 0.019\n    - - 20\n      - 21\n      - 0.81\n      - 0.48\n      - 0.032\n    - - 28\n      - 30\n      - 0.76\n      - 0.55\n      - 0.012\n    - - 36\n      - 38\n      - 0.68\n      - 0.51\n      - 0.022\n    - - 44\n      - 47\n      - 0.56\n      - 0.46\n      - 0.041\n    - - 52\n      - 55\n      - 0.45\n      - 0.43\n      - 0.058\n    - - 60\n      - 64\n      - 0.38\n      - 0.38\n      - 0.098\n    - - 68\n      - 72\n      - 0.3\n      - 0.33\n      - 0.155\n    - - 72\n      - 77\n      - 0.28\n      - 0.28\n      - 0.231\n    - - 80\n      - 85\n      - 0.22\n      - 0.21\n      - 0.372\n  - name: 'Table 8: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)'\n    columns:\n    - depth_pct\n    - HIGH_CKA\n    - MID_CKA\n    - LOW_CKA\n    - overall_CKA\n    rows:\n    - - 13\n      - 0.86\n      - 0.79\n      - 0.62\n      - 0.78\n    - - 30\n      - 0.84\n      - 0.77\n      - 0.58\n      - 0.76\n    - - 47\n      - 0.68\n      - 0.56\n      - 0.35\n      - 0.56\n    - - 64\n      - 0.48\n      - 0.37\n      - 0.22\n      - 0.38\n    - - 77\n      - 0.38\n      - 0.27\n      - 0.14\n      - 0.28\n    - - 94\n      - 0.25\n      - 0.18\n      - 0.09\n      - 0.19\n  - name: 'Table 9: Subspace Angle Analysis (correctness direction)'\n    columns:\n    - comparison_type\n    - mean_angle_deg\n    - std_deg\n    - interpretation\n    rows:\n    - - within-layer cross-language (same layer, different langs)\n      - 12.4\n      - 5.8\n      - highly aligned — correctness direction is near-universal\n    - - cross-layer same-language (same lang, different layers)\n      - 38.7\n      - 11.2\n      - significant drift — direction rotates with depth\n    - - random baseline (shuffled)\n      - 87.3\n      - 2.1\n      - near-orthogonal — signal is non-trivial\n  figures_description:\n  - 'Figure 4a: Simpson''s Paradox visualization — left panel: raw scatter (CKA vs\n    ZS AUROC) showing negative trend with depth-colored points; right panel: partial\n    residual plot after controlling for depth showing positive trend. Two panels side\n    by side dramatically illustrate the sign reversal.\n\n    '\n  - 'Figure 4b: CKA × layer × language heatmap for Qwen3 (main) and Llama4 (inset).\n    Color intensity = CKA value. Clear gradient from warm (shallow, high CKA) to cool\n    (deep, low CKA), with low-resource languages cooling faster.\n\n    '\n  - 'Figure 4c: CKA threshold scatter — transfer AUROC (y) vs CKA (x), vertical dashed\n    line at CKA=0.35 showing transfer collapse zone.\n\n    '\n  analysis: 'Simpson''s Paradox 在双架构上显著复现（partial rho Qwen=+0.48 p=0.002, Llama=+0.41\n    p=0.008），是本文的核心几何洞见。这不是 trivially expected from measurement overlap（CKA 和 transfer\n    AUROC 都衡量 EN-target 相似性） ——sign reversal 从负到正是 non-trivial 的。\n\n    Subspace angle analysis 提供 mechanistic grounding：correctness direction 在同一 layer\n    内跨语言仅 ~12° 偏差（near-universal），但跨 layer 偏差 ~39°（significant rotation）。这解释了为何 CKA（衡量全局\n    representation similarity）与 transfer（衡量 correctness direction alignment）的关系 需要控制\n    depth 后才能显现：全局 CKA 下降反映的是 non-correctness dimensions 的 divergence，correctness\n    subspace 本身作为 low-dimensional feature 持续存在。\n\n    CKA cliff threshold ~0.35 直接解释了 Qwen3 vs Llama4 tradeoff 差异： Qwen3 的 CKA cliff\n    更陡（L52→L60 从 0.45 降至 0.38），导致更多语言 在 deep layers 穿越 threshold → strong tradeoff；Llama4\n    的 cliff 更缓 （L28→L36 从 0.55 降至 0.45），且 ar/hi/ko 因高 baseline CKA 从不穿越 threshold\n    → weak/mixed tradeoff。\n\n    这一分析将 Claim 1 的 Pareto observation 与 CKA geometry 连接，构成 完整的 geometric explanation：architecture-dependent\n    CKA cliff steepness → architecture-dependent Pareto frontier strength。\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: 'L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits).\n    English labels + parallel activations from GlobalMMLU test-split 70/30 partition.\n    Compare vs zero-shot/mean-shift/linear-proj/few-shot across full Pareto frontier,\n    both models × 20 languages. α sweep [0.01–10], β sweep [0.001–1.0] across 3 OOM.\n\n    '\n  expected_results:\n    best_alpha: 0.1\n    best_beta: 0.05\n    caclr_mean_delta_auroc_vs_zs: 0.035\n    caclr_mean_delta_auroc_vs_linproj: 0.015\n    caclr_improvement_at_deep_layers_pp: 4.8\n    caclr_improvement_at_shallow_layers_pp: 1.2\n    caclr_improvement_pass_rate: 0.88\n    qwen3_caclr_mean_auroc_20lang: 0.757\n    qwen3_caclr_delta_vs_zs_pp: 3.7\n    qwen3_caclr_ece_mean: 0.078\n    llama4_caclr_mean_auroc_20lang: 0.733\n    llama4_caclr_delta_vs_zs_pp: 3.3\n    llama4_caclr_ece_mean: 0.085\n    beta_0001_delta_pp: 0.5\n    beta_001_delta_pp: 1.8\n    beta_005_delta_pp: 3.5\n    beta_01_delta_pp: 3.2\n    beta_10_delta_pp: 0.8\n    alpha_001_ece_improvement_pp: 1.5\n    alpha_01_ece_improvement_pp: 3.2\n    alpha_10_ece_improvement_pp: 2.8\n    alpha_100_ece_improvement_pp: -0.5\n    bce_only_auroc: 0.71\n    bce_sbece_auroc: 0.722\n    bce_consistency_auroc: 0.738\n    bce_sbece_consistency_auroc: 0.745\n    mmd_kernel: Gaussian RBF, bandwidth=median heuristic\n    optimizer: Adam, lr=1e-3, linear warmup 10%\n    epochs: 50\n    early_stopping: patience=10, monitor=val_auroc\n    initialization: from standard LR solution\n    batch_size: 256\n    mmd_items: same items as BCE (overlapping)\n    parallel_set_size_range:\n    - 1800\n    - 4200\n  result_rationale: 'CaCLR 的 consistency loss (β·MMD on 1-D logits) 强制 probe 学习 language-invariant\n    features：EN 和 target-language 的 probe 输出分布 应相似。在 1-D logit space 中，MMD 有效地匹配了两种语言的\n    logit mean 和 variance，等价于让 probe direction 靠近 CKA analysis 中揭示的 \"universal correctness\n    subspace\"。\n\n    +3.5pp mean delta（[2, 5] range 内）反映了 1-D MMD 的能力边界：它能 捕获 first-order distributional\n    alignment（mean/variance matching）， 但无法完成 full rotational alignment（需要 d-dimensional\n    操作）。Linear projection（+2pp）通过 Procrustes 做了 rotational alignment 但不优化 probe 本身；CaCLR\n    的优势在于 end-to-end 优化但受 1-D 约束。两者差距 仅 1.5pp，说明 correctness transfer 的瓶颈主要是 rotational（线性\n    投影解决的）而非 distributional（MMD 解决的）。\n\n    β sweep across 3 OOM 清晰展现 \"sweet spot\"：β=0.001 太弱（gradient noise > signal），β=1.0\n    太强（MMD 主导 BCE，probe accuracy 下降 2pp）。 Optimal β=0.05 平衡了 accuracy 和 consistency。\n\n    Deep-layer improvement (+4.8pp) 远大于 shallow-layer (+1.2pp)，因为 deep layers 有更大的\n    capability-specific component（Claim 2 decomposition 所揭示），CaCLR 的 consistency loss\n    正好 target 这个 component。这与 difficulty-capability decomposition 形成因果闭环。\n\n    88% improvement pass rate（35/40 model-lang pairs）：5 个 non-improving pairs 是 HIGH-resource\n    languages（如 Qwen3-zh, Qwen3-nl）on shallow layers where ZS transfer 已经接近 ceiling。\n\n    '\n  tables:\n  - name: 'Table 10: β Sweep — Consistency Loss Effect'\n    columns:\n    - beta\n    - mean_delta_auroc_vs_zs_pp\n    - mean_delta_ece_pp\n    - note\n    rows:\n    - - 0.0\n      - 0.0\n      - 0.0\n      - baseline (BCE only)\n    - - 0.001\n      - 0.5\n      - -0.3\n      - marginal improvement\n    - - 0.01\n      - 1.8\n      - -1.1\n      - clear positive signal\n    - - 0.05\n      - 3.5\n      - -2.4\n      - optimal — best tradeoff\n    - - 0.1\n      - 3.2\n      - -2.0\n      - slight over-regularization\n    - - 1.0\n      - 0.8\n      - -0.5\n      - MMD dominates, probe accuracy degrades\n  - name: 'Table 11: CaCLR vs All Methods (at best-transfer layer, both models averaged)'\n    columns:\n    - method\n    - auroc_mean_20\n    - ece_mean_20\n    - requires_labels\n    - key_resource\n    rows:\n    - - zero-shot\n      - 0.71\n      - 0.118\n      - none\n      - —\n    - - mean-shift\n      - 0.71\n      - 0.118\n      - none\n      - —\n    - - linear_proj_50\n      - 0.725\n      - 0.098\n      - 50 parallel pairs\n      - Procrustes\n    - - linear_proj_200\n      - 0.729\n      - 0.095\n      - 200 parallel pairs\n      - Procrustes\n    - - few-shot-25\n      - 0.7\n      - 0.102\n      - 25 labeled\n      - target labels\n    - - few-shot-100\n      - 0.727\n      - 0.088\n      - 100 labeled\n      - target labels\n    - - CaCLR\n      - 0.745\n      - 0.082\n      - none\n      - parallel activations\n  - name: 'Table 12: CaCLR Depth Profile (Qwen3, ZS AUROC vs CaCLR AUROC)'\n    columns:\n    - depth_pct\n    - zs_auroc\n    - caclr_auroc\n    - delta_pp\n    rows:\n    - - 30\n      - 0.733\n      - 0.745\n      - 1.2\n    - - 43\n      - 0.748\n      - 0.766\n      - 1.8\n    - - 55\n      - 0.72\n      - 0.752\n      - 3.2\n    - - 64\n      - 0.69\n      - 0.738\n      - 4.8\n    - - 77\n      - 0.638\n      - 0.688\n      - 5.0\n    - - 85\n      - 0.601\n      - 0.641\n      - 4.0\n  figures_description:\n  - 'Figure 5: β sweep curve — delta AUROC (y) vs log10(β) (x), inverted-U shape peaking\n    at β=0.05. Inset shows corresponding ECE improvement.\n\n    '\n  - 'Figure 6: CaCLR depth profile — ZS (blue) vs CaCLR (red) AUROC across normalized\n    depth. Gap widens at deep layers, demonstrating CaCLR specifically addresses deep-layer\n    transfer degradation.\n\n    '\n  analysis: 'CaCLR 作为正面方法贡献：β>0 在 deep layers 上提供 ≥2pp AUROC improvement（实际 deep-layer\n    mean = +4.8pp），且 β sweep across 3 OOM 清晰展现最优区间。Component ablation 证实 L_consistency\n    是主要 contributor（+2.8pp），L_SB-ECE 提供 complementary calibration improvement（+0.7pp\n    ECE, +0.7pp AUROC synergy）。\n\n    CaCLR 超越 linear projection 1.5pp 是因为 end-to-end 优化可以利用 training dynamics（gradient\n    信号引导 probe 朝 language-invariant direction 收敛），而 Procrustes 只做 post-hoc geometric\n    correction。但差距不大 是因为 1-D MMD 的 expressiveness 有限——它只能匹配 scalar logit distributions，不能做\n    full subspace alignment。\n\n    Deep-layer improvement 模式与 Claim 2 的 decomposition 一致：deep layers 的 capability-specific\n    component 更大，CaCLR 的 consistency loss 正好 在这些 layers 有更多 signal 来 exploit。这构成 Pareto→Decomposition→CaCLR→CKA\n    因果链的第三环。\n\n    '\n- name: Difficulty-Controlled Ablation (Decomposition)\n  plan_id: plan_004\n  description: 'IRT difficulty probes (Ridge regression), project out difficulty direction,\n    retrain correctness probes on residuals, evaluate transfer。10 languages (HIGH:\n    zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) × 8 layers (20-90% depth) per model。包含\n    random-direction control。\n\n    '\n  expected_results:\n    difficulty_probe_r2_mean: 0.68\n    difficulty_probe_r2_range:\n    - 0.55\n    - 0.78\n    difficulty_var_explained_pct: 65\n    capability_var_explained_pct: 35\n    difficulty_transfer_degradation_share_pct: 12\n    capability_transfer_degradation_share_pct: 88\n    decomp_capability_delta_auroc: 0.03\n    residual_en_auroc_drop_pp: 4.5\n    residual_zs_transfer_drop_pp: 0.8\n    random_direction_control_delta_pp: -1.2\n    prescriptive_accuracy: 0.78\n    capability_transfer_drop_by_depth:\n      20pct: 0.6\n      50pct: 2.8\n      80pct: 8.5\n  result_rationale: 'IRT difficulty 是 language-agnostic property：hard questions are\n    hard everywhere。Ridge regression captures this linearly (R²=0.68, 与 Civelli et\n    al. 的 shared difficulty finding 一致)。Difficulty 占 correctness variance 的 65% 但仅贡献\n    12% 的 transfer degradation， 因为 difficulty signal 本质上是 universal 的。Capability-specific\n    residual 仅占 35% variance 但驱动 88% 的 transfer degradation，且 degradation 随 depth\n    指数增长（20% depth: 0.6pp → 80% depth: 8.5pp）。\n\n    这一 decomposition 解释了 Pareto frontier 的 mechanistic origin： deep layers 的 EN probe\n    improvement 主要来自 capability-specific component（language-dependent competence），而这个\n    component 恰好是 最难 transfer 的。CaCLR 的 consistency loss works precisely because it\n    targets this component。\n\n    Random-direction control（-1.2pp, 随机方向 projection 反而损害）确认 difficulty direction\n    不是 arbitrary dimensionality reduction 的 artifact， 而是 genuine signal。\n\n    Prescriptive accuracy 78%：给定语言-layer 的 difficulty/capability ratio，预测应使用 zero-shot（difficulty-dominant）还是\n    CaCLR （capability-dominant）策略，在 78% 的 cases 中正确。\n\n    '\n  tables:\n  - name: 'Table 13: Decomposition Results'\n    columns:\n    - component\n    - var_pct\n    - transfer_auroc_mean\n    - transfer_drop_pp\n    - degradation_share_pct\n    rows:\n    - - full_correctness\n      - 100\n      - 0.71\n      - 9.0\n      - 100\n    - - difficulty_shared\n      - 65\n      - 0.698\n      - 1.1\n      - 12\n    - - capability_specific\n      - 35\n      - 0.615\n      - 12.8\n      - 88\n  - name: 'Table 14: Capability Transfer Drop by Depth'\n    columns:\n    - depth_band\n    - difficulty_drop_pp\n    - capability_drop_pp\n    - ratio\n    rows:\n    - - 20-30%\n      - 0.2\n      - 0.6\n      - 3×\n    - - 40-50%\n      - 0.6\n      - 2.8\n      - 4.7×\n    - - 60-70%\n      - 1.0\n      - 5.6\n      - 5.6×\n    - - 75-90%\n      - 1.5\n      - 8.5\n      - 5.7×\n  figures_description:\n  - 'Figure 7: Stacked area — difficulty (blue, flat) vs capability (red, exponentially\n    increasing) transfer degradation across depth.\n\n    '\n  analysis: 'Decomposition 清晰分离 transferable vs non-transferable components。 Difficulty\n    占大部分 variance 但 near-perfectly transfers（仅 12% degradation share），capability 占少数但驱动几乎所有\n    degradation。 这解释了为何 zero-shot transfer 在 mid-depth 工作（difficulty dominates there）但在\n    deep layers 失败（capability grows）。 Prescriptive accuracy 78% 证实 decomposition 不仅是描述性的，\n    而是可以指导 alignment strategy selection。\n\n    '\n- name: Linear Projection Sensitivity Analysis\n  plan_id: plan_012\n  description: 'Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。\n    Both models × 5 representative layers × 20 languages。确定最小数据需求 和 resource-tier\n    分层饱和。\n\n    '\n  expected_results:\n    pairs_to_95pct_overall: 42\n    pairs_to_95pct_HIGH: 22\n    pairs_to_95pct_MID: 38\n    pairs_to_95pct_LOW: 48\n    pairs_10_pct_of_200: 0.72\n    pairs_20_pct_of_200: 0.86\n    pairs_30_pct_of_200: 0.92\n    pairs_50_pct_of_200: 0.97\n    pairs_100_pct_of_200: 0.99\n    pairs_200_baseline_auroc_mean: 0.729\n    procrustes_reversal_threshold: 0.52\n    procrustes_helps_below_threshold_delta_pp: 3.8\n    procrustes_hurts_above_threshold_delta_pp: -1.2\n  result_rationale: 'Linear projection (Procrustes) 学习 EN→target 的 rotation matrix。\n    20 pairs 即可估计 dominant rotational components（correctness subspace 是 low-dimensional\n    的，前几个 principal angles 解释 90%+ 的 alignment structure）。42 pairs 达到 95% 因为边际的 minor\n    components 需要更多 data 来稳定估计。\n\n    Resource-tier stratification 清晰：HIGH languages（zh/es/de 等）的 activation distributions\n    与 EN 更相似，rotation matrix 的 effective rank 更低（fewer parameters to estimate），22\n    pairs 即可。LOW languages 需要估计更 complex rotation（effective rank 更高），48 pairs。\n\n    Procrustes effect reversal（threshold ~0.52）：当 ZS AUROC < 0.52 时， correctness direction\n    严重 misaligned，Procrustes 纠正旋转带来 +3.8pp。 当 ZS AUROC > 0.60 时，directions 已经 well-aligned，Procrustes\n    引入 estimation noise 反而 hurt -1.2pp。Threshold 0.52 对应 CKA ~0.35 （与 plan_011 的 cliff\n    threshold 一致）。\n\n    这一 finding 直接 actionable：practitioners 应先测 ZS transfer， only apply Procrustes\n    when baseline < 0.52。\n\n    '\n  tables:\n  - name: 'Table 15: Projection Sample Efficiency'\n    columns:\n    - n_pairs\n    - pct_of_200pair_performance\n    - mean_auroc\n    - note\n    rows:\n    - - 10\n      - 72\n      - 0.724\n      - unstable, high variance across runs\n    - - 20\n      - 86\n      - 0.728\n      - captures dominant rotation\n    - - 30\n      - 92\n      - 0.731\n      - near plateau for HIGH langs\n    - - 50\n      - 97\n      - 0.734\n      - near plateau for all tiers\n    - - 100\n      - 99\n      - 0.737\n      - marginal returns\n    - - 200\n      - 100\n      - 0.729\n      - baseline (reference)\n  - name: 'Table 16: Saturation by Resource Tier'\n    columns:\n    - tier\n    - pairs_to_90pct\n    - pairs_to_95pct\n    - interpretation\n    rows:\n    - - HIGH\n      - 15\n      - 22\n      - rotation is simple, low effective rank\n    - - MID\n      - 25\n      - 38\n      - moderate rotation complexity\n    - - LOW\n      - 35\n      - 48\n      - complex rotation, more data needed\n  - name: 'Table 17: Procrustes Effect Reversal'\n    columns:\n    - zs_auroc_range\n    - n_lang_layer_pairs\n    - mean_delta_pp\n    - direction\n    rows:\n    - - <0.45\n      - 42\n      - 5.2\n      - strong positive\n    - - 0.45-0.52\n      - 68\n      - 2.4\n      - moderate positive\n    - - 0.52-0.60\n      - 95\n      - 0.3\n      - near-zero (transition zone)\n    - - 0.60-0.70\n      - 88\n      - -1.2\n      - negative — hurts\n    - - '>0.70'\n      - 47\n      - -0.8\n      - slight negative\n  figures_description:\n  - 'Figure 8a: Sample efficiency curves — AUROC (y) vs n_pairs (x), three curves\n    for HIGH/MID/LOW tiers, showing staggered saturation.\n\n    '\n  - 'Figure 8b: Procrustes effect reversal — delta AUROC (y) vs ZS baseline AUROC\n    (x), showing sign change at ~0.52. Dot size proportional to sample count.\n\n    '\n  analysis: '~42 pairs to 95% performance 是 directly actionable 的 practical finding：对于大多数语言，仅需\n    <50 parallel sentences 即可达到接近 supervised-level alignment。Resource-tier stratification（HIGH\n    22 vs LOW 48 pairs）提供了 per-language guidance。\n\n    Procrustes reversal at 0.52 与 CKA threshold 0.35 形成对应： CKA < 0.35 的 language-layer\n    combinations 对应 ZS < 0.52（ 因为 poor alignment → poor transfer），正好是 Procrustes 帮助最大的\n    区域。这构成了 geometric explanation 的 practical corollary。\n\n    '\n- name: Probing Control Tasks — Full-Scale Hewitt & Liang (2019)\n  plan_id: plan_013\n  description: 'Extend MVP English-only control task analysis to 20 languages × 2\n    architectures。Train probes on randomly permuted labels, compute selectivity =\n    real_AUROC - control_AUROC。Identify capacity artifacts by language, layer, and\n    model。\n\n    '\n  expected_results:\n    en_selectivity_range:\n    - 0.02\n    - 0.26\n    en_selectivity_meaningful_layers:\n    - 16\n    - 20\n    - 24\n    - 27\n    control_artifact_rate_lowres: 0.27\n    control_artifact_rate_midres: 0.05\n    control_artifact_rate_highres: 0.03\n    low_res_langs_most_affected:\n    - yo\n    - ig\n    - te\n    - sw\n    artifact_concentration_depth: 60-100% depth\n    cross_lingual_selectivity_mean:\n      HIGH: 0.22\n      MID: 0.18\n      LOW: 0.09\n    languages_with_any_meaningful_selectivity: 17\n    control_auroc_mean_all: 0.495\n    control_auroc_std: 0.008\n  result_rationale: 'MVP English data（selectivity L27=0.262）确立了 baseline。Cross-lingual\n    extension 揭示了 resource-tier dependent artifact pattern：\n\n    LOW-resource languages 的 27% artifact rate 源于两个因素：(1) these languages 在 model\n    pretraining 中占比极低，activation distributions 相对 high-resource 更 \"shallow\" (less\n    structured)，linear probes 更容易 通过 capacity 而非 genuine signal 拟合少量 patterns；(2)\n    GlobalMMLU 的 low-resource translations 质量较低，引入 noise 使 correctness signal 更弱，selectivity\n    更接近 chance。\n\n    Mid/high-resource 的 artifact rate 极低（3-5%）因为 representation quality 高，probe 有\n    genuine signal 可以 leverage。\n\n    Artifacts 集中在 60-100% depth，与 CKA cliff 一致：deep layers 的 low-resource CKA 已经很低（<0.2），cross-lingual\n    activation structure 不足以支撑 genuine correctness probing，probe 退化为 memorizing dataset-specific\n    patterns。\n\n    这一 finding 是 field-level contribution：此前没有人在 cross-lingual probing 中检查 selectivity\n    controls。28% 的 low-resource artifact rate 意味着没有 control tasks 的 cross-lingual\n    probing 结果 （包括 Xiao et al.）需要谨慎解读。\n\n    '\n  tables:\n  - name: 'Table 18: Selectivity by Resource Tier and Depth'\n    columns:\n    - depth_band\n    - HIGH_selectivity\n    - MID_selectivity\n    - LOW_selectivity\n    rows:\n    - - 0-30%\n      - 0.04\n      - 0.03\n      - 0.01\n    - - 30-60%\n      - 0.18\n      - 0.14\n      - 0.06\n    - - 60-80%\n      - 0.28\n      - 0.22\n      - 0.1\n    - - 80-100%\n      - 0.25\n      - 0.2\n      - 0.08\n  - name: 'Table 19: Artifact Rates by Tier'\n    columns:\n    - tier\n    - n_lang_layer_combinations\n    - artifact_count\n    - artifact_rate\n    rows:\n    - - HIGH\n      - 384\n      - 12\n      - 3%\n    - - MID\n      - 336\n      - 17\n      - 5%\n    - - LOW\n      - 240\n      - 65\n      - 27%\n    - - total\n      - 960\n      - 94\n      - 10%\n  figures_description:\n  - 'Figure S1: Selectivity heatmap — language (y, ordered by tier) × depth (x). LOW-resource\n    rows show gray (low selectivity) at deep layers.\n\n    '\n  analysis: '27% low-resource artifact rate 是 methodological warning for the field：\n    cross-lingual probing studies 如果不做 selectivity checks 会高估 low-resource transfer\n    quality。重要的是 artifacts 集中在 low-resource + deep layers，不波及 mid/high-resource 或\n    shallow layers，因此本文的 核心 Pareto/CKA 分析（主要基于 mid/high-resource patterns）不受影响。\n\n    '\n- name: Cross-Lingual Correctness-Confidence Orthogonality\n  plan_id: plan_005\n  description: 'Extract verbalized confidence direction, compute cosine similarity\n    with correctness direction, 20 languages × 2 architectures。 Supporting evidence\n    for Claim 4 (subsection)。\n\n    '\n  expected_results:\n    cosine_mean_overall: 0.05\n    cosine_range:\n    - 0.02\n    - 0.09\n    cosine_en: 0.03\n    all_below_0p10: true\n    qwen3_cosine_mean: 0.046\n    llama4_cosine_mean: 0.054\n    HIGH_cosine_mean: 0.038\n    MID_cosine_mean: 0.052\n    LOW_cosine_mean: 0.072\n    resource_tier_correlation: -0.66\n  result_rationale: 'Miao & Ungar (2026) 在 English 7-8B 上测得 cosine < 0.04。Extension\n    to 20 languages × 大模型应保持 near-orthogonality（< 0.10），因为这反映 transformer 的 structural\n    property：verbalized confidence 由 language modeling head 从 surface-level token\n    probabilities 生成，correctness 由 intermediate representations geometry 编码，两者 architecturally\n    decoupled。Low-resource 略高（0.072 mean）因为 confidence elicitation in low-resource\n    languages 更 noisy，不完全 decoupled。Resource-tier gradient（r=-0.66）说明更好的 multilingual\n    training → 更清晰的 correctness/confidence separation。\n\n    '\n  tables:\n  - name: 'Table 20: Orthogonality by Tier (cosine similarity)'\n    columns:\n    - tier\n    - n_langs\n    - qwen3_mean\n    - llama4_mean\n    - combined_mean\n    rows:\n    - - HIGH\n      - 8\n      - 0.035\n      - 0.041\n      - 0.038\n    - - MID\n      - 7\n      - 0.048\n      - 0.056\n      - 0.052\n    - - LOW\n      - 5\n      - 0.066\n      - 0.078\n      - 0.072\n  figures_description:\n  - 'Figure S2: Cosine similarity violin plots by resource tier, all below 0.10 threshold\n    line.\n\n    '\n  analysis: 'Orthogonality universally holds (39/40 pairs below 0.10, all 40 below\n    0.095)，confirming output-based calibration methods are structurally limited across\n    languages。Resource-tier gradient 是新 finding，但 effect size 小（range only 0.034），作为\n    subsection 足够。\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Logistic regression vs 2-layer MLP at each probed layer, both models。\n    Validates linear probe choice for transfer。\n\n    '\n  expected_results:\n    logreg_en_auroc_best: 0.81\n    mlp_en_auroc_best: 0.83\n    mlp_en_gain_pp: 2.0\n    logreg_zs_drop_mean_pp: 9.0\n    mlp_zs_drop_mean_pp: 14.5\n    logreg_transfer_advantage_pp: 5.5\n    logreg_advantage_shallow_pp: 2.0\n    logreg_advantage_deep_pp: 8.2\n  result_rationale: 'Linear probes learn 一个 hyperplane，跨语言泛化因为 correctness subspace\n    是 near-universal linear structure（subspace angle ~12° from plan_011）。 MLPs fit\n    nonlinear decision boundaries that overfit EN-specific feature interactions，gaining\n    +2pp EN AUROC but losing 5.5pp transfer。Gap 在 deep layers 放大（+8.2pp advantage\n    for logreg at 80% depth）因为 deep layers 有更多 language-specific nonlinear structure\n    for MLP to exploit。 This justifies logreg as primary probe and supports geometric\n    interpretation of Pareto frontier。\n\n    '\n  tables:\n  - name: 'Table S2: Probe Complexity (Qwen3, at EN-optimal layer)'\n    columns:\n    - probe_type\n    - en_auroc\n    - zs_mean_20\n    - zs_drop_pp\n    rows:\n    - - logistic_regression\n      - 0.81\n      - 0.72\n      - 9.0\n    - - mlp_2layer_h128\n      - 0.83\n      - 0.685\n      - 14.5\n  figures_description:\n  - 'Figure S3: Transfer drop (pp) vs depth, logreg (blue) vs MLP (red). MLP diverges\n    sharply past 60% depth.\n\n    '\n  analysis: 'Linear probes 为 cross-lingual transfer 的 optimal choice：牺牲 2pp EN performance\n    换取 5.5pp transfer improvement。Depth interaction confirms nonlinear language-specific\n    features drive deep-layer degradation。\n\n    '\n- name: Cross-Benchmark Generalization (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: 'Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages\n    each)。Tests domain generalization。\n\n    '\n  expected_results:\n    belebele_zs_mean_20: 0.695\n    belebele_caclr_mean_20: 0.728\n    belebele_caclr_delta_pp: 3.3\n    mmlupx_zs_mean_20: 0.68\n    mmlupx_caclr_mean_20: 0.715\n    mmlupx_caclr_delta_pp: 3.5\n    cross_benchmark_caclr_cv: 0.04\n  result_rationale: 'Belebele (reading comprehension) 和 MMLU-ProX (harder factual)\n    的 baseline 略低于 GlobalMMLU 因为 domain shift，但 CaCLR 的 improvement 幅度 consistent（3.3-3.5pp\n    vs GlobalMMLU 的 3.5pp）。Low CV (0.04) 证实 CaCLR addresses 一个 fundamental representation\n    alignment issue 而非 overfitting to specific benchmark。\n\n    '\n  tables:\n  - name: 'Table 21: Cross-Benchmark CaCLR Generalization'\n    columns:\n    - benchmark\n    - zs_mean_20\n    - caclr_mean_20\n    - delta_pp\n    rows:\n    - - GlobalMMLU\n      - 0.71\n      - 0.745\n      - 3.5\n    - - Belebele\n      - 0.695\n      - 0.728\n      - 3.3\n    - - MMLU-ProX\n      - 0.68\n      - 0.715\n      - 3.5\n  figures_description:\n  - 'Figure S4: CaCLR improvement by benchmark × language, showing consistent gains.\n\n    '\n  analysis: 'CaCLR generalizes across benchmarks with low variance。Cross-benchmark\n    consistency is the strongest defense against overfitting concerns。\n\n    '\n- name: Quantization Validation Ablation\n  plan_id: plan_010\n  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4\n    vs FP16 for Qwen3-235B at 5 layers, 5% subset。\n\n    '\n  expected_results:\n    llama4_w4a16_fp16_auroc_diff_mean_pp: 0.3\n    llama4_w4a16_fp16_auroc_diff_max_pp: 0.8\n    llama4_rank_correlation: 0.996\n    qwen3_int4_fp16_auroc_diff_mean_pp: 0.5\n    qwen3_int4_fp16_auroc_diff_max_pp: 1.1\n    qwen3_rank_correlation: 0.994\n    conclusion: quantization introduces negligible distortion for probing\n  result_rationale: 'W4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation\n    geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction\n    的 angular structure 仍 robust（0.5pp mean diff）， 因为 quantization noise 近似 isotropic，不\n    preferentially distort correctness-relevant directions。Rank correlation > 0.994\n    确认 Pareto frontier ordering 完全保留。Qwen3 的 slightly higher diff (0.5 vs 0.3) 因为\n    Int4 比 W4A16 更 lossy。\n\n    '\n  tables:\n  - name: 'Table S3: Quantization Comparison (5 representative layers)'\n    columns:\n    - model\n    - layer\n    - fp16_auroc\n    - quant_auroc\n    - diff_pp\n    rows:\n    - - Llama4\n      - 8\n      - 0.637\n      - 0.634\n      - 0.3\n    - - Llama4\n      - 16\n      - 0.737\n      - 0.735\n      - 0.2\n    - - Llama4\n      - 28\n      - 0.784\n      - 0.781\n      - 0.3\n    - - Llama4\n      - 36\n      - 0.792\n      - 0.789\n      - 0.3\n    - - Llama4\n      - 44\n      - 0.774\n      - 0.77\n      - 0.4\n    - - Qwen3\n      - 20\n      - 0.712\n      - 0.708\n      - 0.4\n    - - Qwen3\n      - 36\n      - 0.78\n      - 0.775\n      - 0.5\n    - - Qwen3\n      - 52\n      - 0.808\n      - 0.803\n      - 0.5\n    - - Qwen3\n      - 68\n      - 0.812\n      - 0.806\n      - 0.6\n    - - Qwen3\n      - 80\n      - 0.807\n      - 0.8\n      - 0.7\n  figures_description:\n  - 'Figure S5: Quant vs FP16 scatter, y=x diagonal, tight clustering.\n\n    '\n  analysis: 'Quantization safe for both models。Preempts reviewer concern #5。\n\n    '\n- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)\n  plan_id: plan_008\n  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers, FP16), 20 languages。Provides\n    dense vs MoE contrast for camera-ready。\n\n    '\n  expected_results:\n    en_best_auroc: 0.8\n    en_best_layer_idx: 45\n    zs_mean_20lang: 0.71\n    zs_best_transfer_layer_idx: 36\n    global_spearman_rho: -0.85\n    per_lang_rho_median: -0.58\n    caclr_delta_vs_zs_pp: 3.0\n    simpson_partial_rho: 0.44\n    simpson_partial_p: 0.004\n  result_rationale: 'Gemma 4 31B Dense 是理想的第三 data point：dense architecture（vs two\n    MoE models），different pretraining recipe（Google vs Alibaba/Meta）， 60 layers（between\n    Qwen 94 and Llama 48）。EN AUROC 0.80 低于 MoE models 因为 31B dense < 22B MoE active\n    (MoE routing 提供 effective capacity boost)。Pareto strength (ρ=-0.85) 介于 Qwen (-0.91)\n    和 Llama (-0.78) 之间。Simpson''s partial correlation 仍然显著 (rho=+0.44, p=0.004)， 确认\n    geometric insight 是 architecture-universal 而非 MoE-specific。\n\n    '\n  tables:\n  - name: 'Table 22: Three-Architecture Summary'\n    columns:\n    - model\n    - type\n    - layers\n    - en_best\n    - zs_mean_20\n    - pareto_rho\n    - simpson_partial_rho\n    - caclr_delta_pp\n    rows:\n    - - Qwen3-235B\n      - MoE\n      - 94\n      - 0.81\n      - 0.72\n      - -0.91\n      - 0.48\n      - 3.7\n    - - Llama4 Scout\n      - MoE\n      - 48\n      - 0.79\n      - 0.7\n      - -0.78\n      - 0.41\n      - 3.3\n    - - Gemma4 31B\n      - Dense\n      - 60\n      - 0.8\n      - 0.71\n      - -0.85\n      - 0.44\n      - 3.0\n  figures_description:\n  - 'Figure 9: Three-architecture Pareto frontiers overlaid (normalized depth %).\n    Remarkably similar shapes.\n\n    '\n  analysis: 'Three-architecture replication 是 universality claim 最强证据： Simpson''s\n    Paradox 在 dense 和 MoE 上都成立，Pareto frontier 在 55-60% depth 处一致出现 knee，CaCLR 提供\n    3-3.7pp consistent gain。 Dense vs MoE 的差异 minimal — phenomenon 是 transformer depth\n    的 property 而非 routing architecture 的。\n\n    '\n- name: Extended Language Coverage (Camera-Ready)\n  plan_id: plan_009\n  description: 'Expand from 20 to 50+ languages for camera-ready。\n\n    '\n  expected_results:\n    total_languages: 50\n    zs_pass_rate_50lang: 0.84\n    zs_auroc_above_060_count: 42\n    caclr_improvement_positive_count: 47\n    mean_zs_auroc_50lang: 0.69\n    mean_caclr_auroc_50lang: 0.72\n    pareto_frontier_holds_all_langs: true\n    new_families:\n    - Austronesian\n    - Dravidian\n    - Uralic\n    - Kartvelian\n    - Niger-Congo_B\n  result_rationale: 'Expansion 主要增加 mid-resource 语言（Indonesian, Finnish, Georgian,\n    Tamil, Telugu, etc.），大多 fall in 0.65-0.75 AUROC range。Extremely low-resource 语言（Amharic,\n    Khmer, Lao）可能 < 0.55 但代表 edge cases。 CaCLR 在 94% 的新增语言上 positive 因为 consistency\n    loss mechanism 是 language-agnostic。Pareto frontier structure 在 50 languages 上\n    完全保持。\n\n    '\n  tables:\n  - name: 'Table 23: Extended Coverage by Tier'\n    columns:\n    - tier\n    - n_langs\n    - zs_mean\n    - caclr_mean\n    - caclr_gain_pp\n    rows:\n    - - HIGH\n      - 10\n      - 0.75\n      - 0.78\n      - 2.8\n    - - MID\n      - 24\n      - 0.71\n      - 0.74\n      - 3.5\n    - - LOW\n      - 12\n      - 0.62\n      - 0.66\n      - 4.2\n    - - VERY_LOW\n      - 4\n      - 0.53\n      - 0.58\n      - 5.0\n  figures_description:\n  - 'Figure 10: World map with per-language CaCLR AUROC, colored by performance tier.\n    Broad geographic/typological coverage.\n\n    '\n  analysis: 50-language extension 确认 all findings at scale。Resource-tier gradient\n    smooth, CaCLR benefit inversely correlated with resource level, no language family\n    shows anomalous behavior。\n",
      "numLines": 1719,
      "startLine": 1,
      "totalLines": 1719
    }
  },
  "sourceToolAssistantUUID": "adc79fb7-163e-4c82-aadd-fb04aaeee4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17 · 2026-05-21T12:27:14.406Z_

````json
{
  "parentUuid": "7602f47e-f70e-4176-ab0d-d0f246d46397",
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
  "uuid": "14143273-59c7-4d61-b3d7-ecc6a607b827",
  "timestamp": "2026-05-21T12:27:14.406Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Full-scale models (235B MoE + Scout MoE + Gemma Dense) replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement;…",
  "leafUuid": "14143273-59c7-4d61-b3d7-ecc6a607b827",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe transfer and CaCLR calibration",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Assistant

_source line 20 · 2026-05-21T12:32:23.085Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. The user wants me to generate detailed predicted results for the "best" tier for each "planned" experiment in the experiment_plan. Let me check which experiments have status "planned" — that means they haven't been done yet.

Looking at the experiment_plan, the planned experiments are:
- plan_001 (Qwen3-235B)
- plan_002 (Llama 4 Scout) — has registry_id plan_002_v3 with status PREPARING
- plan_003 (CaCLR)
- plan_004 (Decomposition)
- plan_005 (Orthogonality)


- plan_006 (Probe complexity)
- plan_007 (Cross-benchmark)
- plan_008 (Gemma 4 31B)
- plan_009 (Extended language coverage)
- plan_010 (Quantization validation)
- plan_011 (CKA analysis)
- plan_012 (Linear projection sensitivity)

The completed experiments are plan_013, mvp_validation, mvp_complementary, and mvp_llama_control. Now I need to look at the key metrics ranges to generate realistic predicted results for the best tier across these planned experiments. Looking at performance metrics across different model configurations and transfer learning scenarios, including improvements from contrastive learning approaches, linear projection techniques, and decomposition methods, along with measurements of cross-lingual artifacts and the relationship between model depth and transfer success.

Now I'm working through the comprehensive YAML structure for the experiment plan, making sure to incorporate the updated priorities where Gemma 4 is now a core focus, reference the completed results from plan_013, and account for the current preparation status of plan_002_v3, then generate detailed imagined experiment metrics that align with the best-tier ranges established in the previous dream report. YAML now. I need to be thorough with rationales, ensuring each prediction aligns with the best tier metrics and has a solid rationale.

Let me think carefully about each experiment's predicted results in the best tier:

**plan_001 (Qwen3-235B)**
- EN best AUROC: ~0.83 (within [0.8, 0.86] mean across arch)
- 94 layers, 24 probed layers
- Strong Pareto (Qwen family showed strong tradeoff in MVP)
- ~18/20 langs pass (ZS AUROC > 0.58)
- Per-language Spearman: strong negative, ~16-18/20 significant

**plan_002 (Llama 4 Scout)**
- EN best AUROC: ~0.81
- 48 layers, 12 probed layers
- Weaker Pareto from mixed MVP results
- ~17/20 langs pass
- Per-language Spearman: mixed, ~8-10/20 significant

**plan_008 (Gemma 4 31B)**
- EN best AUROC: ~0.80
- 60 layers, 16 probed layers
- Dense architecture → moderate Pareto
- ~17/20 langs pass
- Provides crucial dense vs MoE contrast

Mean EN AUROC across 3 arch: (0.83+0.81+0.80)/3 = 0.813 → within [0.8, 0.86] ✓

**plan_003 (CaCLR)**
- β>0 provides measurable improvement
- Mean delta over ZS: ~3.5pp → within [2.0, 5.0] ✓
- Langs improved: ~14/20 → within [10, 16] ✓

**plan_004 (Decomposition)** - now checking the contrastive learning approach and how it impacts the downstream metrics across different model architectures and language families. Selectivity across deep layers checks out within the expected range, and I already have the actual data for this. The remaining analyses—orthogonality, probe complexity, cross-benchmark validation, quantization checks, and the extended language experiments—all support the core findings and serve as either validation or camera-ready extensions. Now I need to write out the full YAML configuration with comprehensive rationales, making sure to incorporate the current experiment status where plan_013 is complete and plan_002 is in preparation, while anchoring everything to those specific metric ranges I've defined for the best tier.

I'm noticing a discrepancy in how I'm interpreting the Spearman correlation for depth versus transfer performance. The key metric specifies positive languages where deeper layers help, but I need to reconcile this with the Pareto claim that suggests deeper layers generally improve transfer up to a point before hitting a tradeoff at the deepest layers—so the overall correlation should be positive for most languages, with that local tradeoff only appearing at the final layers. Ah, I see the issue now—the previous analysis was measuring the gap between English and zero-shot performance, which showed negative correlation with depth, whereas this metric is tracking absolute zero-shot AUROC improvements with depth, which are positive. So the contradiction resolves: deeper layers do help cross-lingual transfer in absolute terms, even if the English-ZS gap narrows at deeper layers. the RELATIVE gap between EN and ZS at the deepest layers. The gap widens at deep layers, meaning EN improves more than ZS does.

So the Spearman rho (depth vs ZS AUROC) should be POSITIVE for most languages. The previous dream was wrong about the sign.

But the metric `pareto_depth_transfer_drop_at_final_layers_pp: [2.0, 6.0]` suggests ZS AUROC peaks around 60-75% depth and then drops at 80-100%, creating a Pareto shape where EN keeps climbing but ZS starts declining. This means the overall Spearman correlation could be complex: both EN and ZS increase through most of the depth range, but ZS peaks and reverses at the very end.

Actually, looking back at the Table 1 data more carefully—ZS AUROC rises from 0.572 at L4 to 0.752 at L36, then steadily declines through the remaining layers down to 0.531 at L92. Since ZS peaks around 40% depth and falls for the remaining 60%, the overall Spearman correlation across all 24 layers would actually be NEGATIVE.

But wait, that contradicts the expected metric showing 16-20 languages should have positive correlation with depth. Let me reconsider the paper's framing—it specifically states that in the MVP pilot with Qwen2.5-7B (28 layers), ZS AUROC generally increases with depth, peaking around L26-27 for most languages. The Pareto tradeoff at the deepest layers was that L27 maximized English quality while showing slight degradation in cross-lingual transfer for a few languages.

With the full-scale models at 94 layers, the dynamics shift—the deepest layers where language-specific specialization happens represent a much larger portion of the network, so the overall Spearman correlation could still be positive if most of the depth range shows improvement. The key tension is that the "best" tier claims need full support: the statement says deeper layers improve both English and cross-lingual transfer with a local Pareto tradeoff only at the very top, meaning the overall trend must be positive with that tradeoff as a narrow exception, not a widespread pattern.

Looking at the metric more carefully—16 to 20 of 20 languages should show positive Spearman correlation between depth and zero-shot AUROC—this tells me the zero-shot performance needs to generally increase with depth for most languages, with only a dip at the final layers. So I should redesign the tables so zero-shot peaks much later, around 70-75% depth, making the rising portion dominate the overall correlation. Looking at the actual metrics, the Pareto tradeoff shows up in 50-75% of language-architecture pairs, with zero-shot performance dropping 2-6 percentage points at the final layers compared to its peak. So it's not a global trend but rather a specific phenomenon where models sacrifice zero-shot accuracy in deeper layers to optimize for English performance. For Qwen3-235B specifically, English AUROC climbs steadily from layer 4 to layer 80 (reaching ~0.83) then plateaus, while zero-shot peaks around layer 68 (~0.74) before declining. I'm realizing I made a sign error in my previous analysis. Let me reconsider how the Pareto frontier actually works here — it's the tradeoff between EN and ZS performance across layers. In the shallow-to-mid range, both metrics improve together, pushing points toward the upper-right. But at deeper layers, EN continues climbing while ZS declines, creating the actual tradeoff region where you can't improve one without hurting the other. The Pareto frontier itself consists of those deeper layers where this active tradeoff occurs.

Below the ZS-optimal layer, both metrics are still improving, so those points are dominated by later layers. Above the EN-optimal layer, both decline, making those dominated as well. The fact that 50-75% of language-architecture pairs show this tradeoff means that for most combinations, there's a meaningful divergence between where EN peaks and where ZS peaks — though for the rest, the tradeoff is either minimal or they peak at the same layer.

Now I need to generate the corrected YAML, fixing the Spearman sign issue from before. I'm looking at the metric that shows positive correlations across most languages, but I need to verify what the actual values represent.

The Pareto claim states that deeper layers improve both metrics overall (Spearman ρ>0.7 for 4 out of 5 languages), yet there's a local drop of 2-6 percentage points at the final layers. This means the overall trend is strongly positive, but there's a dip at the end. If Spearman is >0.7 across all layers including that final drop, the rising trend in the middle layers must be quite steep to maintain such a strong correlation. Let me work through the layer-by-layer pattern to reconcile these numbers. Looking at the actual metrics, the median Spearman correlation across languages is around +0.72, with 16 out of 20 languages showing significantly positive correlations above 0.7. I need to reconsider whether the larger model with 94 layers would have a lower correlation than the pilot study—the extra depth does provide more room for that tail decline, which could suppress the overall monotonicity measure. But the metric definition I'm working with just tracks how many languages have positive rho, not necessarily exceeding 0.7, so I should be more precise about what "best tier" actually means here.

The Spearman correlations span from about +0.3 to +0.85 depending on the language, and the Pareto tradeoff emerging in the deepest 15-25% of layers explains why the correlation stays positive but doesn't reach perfect monotonicity. This pattern aligns with the main finding that deeper layers generally improve transfer performance, while also accounting for the architectural differences—Qwen shows stronger monotonicity, Llama weaker, and Gemma somewhere in between. Now I need to systematically map out the full prediction space across all planned experiments, being careful to distinguish what "per-language Spearman rho" actually captures in the context of the Pareto claim.

I'm clarifying that I need to track two separate statistical signals: the overall positive correlation between depth and zero-shot AUROC across languages, and the local tradeoff evidence at the deepest layers where zero-shot performance drops even as English performance gains. The Pareto prevalence metric measures how often this tradeoff is detectable across language-architecture pairs—roughly 50-75% of them should show a measurable gap between the zero-shot-optimal and English-optimal layer depths. These aren't contradictory findings; they're complementary pieces of the same story. Now I'm ready to write out the complete YAML with clear rationales for each prediction, making sure everything stays internally consistent.

For the top three architectures, I'm anchoring on specific performance profiles: Qwen3-235B with its mixture-of-experts routing should show the strongest Pareto effect and highest English AUROC around 0.83, Llama 4 Scout with better multilingual training should land around 0.81 with moderate tradeoff evidence, and Gemma 4 31B as a dense model around 0.80 with less routing-specific divergence. The mean English AUROC across these three comes to about 0.813, which fits the predicted range. For zero-shot pass rates, I'm expecting roughly 17-18 languages per model to exceed the threshold, averaging around 17.7 out of 20. Now I need to calculate the mean zero-shot drop relative to English performance to complete the validation.

Looking at the zero-shot AUROC degradation, I'm realizing the drop needs to stay within 4-8 percentage points on average. If Qwen's English AUROC is 0.83 and mean zero-shot is around 0.77, that's a 6pp drop which fits the constraint. Similarly, Llama at 0.81 English with 0.76 mean zero-shot gives 5pp, and Gemma at 0.80 with 0.75 mean zero-shot also gives 5pp. This means I should calibrate the zero-shot performance closer to the English baseline rather than letting it drop too steeply. Looking at the performance gaps across models, I'm seeing Qwen drop 6 percentage points, while Llama and Gemma each drop 5 percentage points from their EN best to ZS mean performance. I think the metric is simply measuring how much the best zero-shot AUROC falls short of the English AUROC for each language, then averaging across all 20 languages and the three architectures.

Now I'm organizing the experimental setup for the YAML file. For Qwen3-235B, I'm working with 94 layers total, probing every 4th layer starting from L0 through L92, which gives me 24 probed layers. English performance peaks around 0.83 at layer L80 (roughly 85% depth), with a slight decline toward the final layer. I need to carefully track the zero-shot mean performance across the 20 languages at their respective optimal layers for each model.

For the zero-shot performance, I'm seeing it peaks earlier around L56-60 (60% depth) at roughly 0.77, then gradually declines toward the end. The key tension here is the Pareto tradeoff: moving from the zero-shot optimal layer L56 to the English optimal layer L80 gains 3 percentage points for English but costs 5 percentage points for zero-shot performance. I'm also checking the per-language correlation between layer depth and zero-shot AUROC, where the median Spearman correlation is around +0.65 with 18 out of 20 languages showing positive correlation, though this relationship weakens in the deeper layers where zero-shot performance starts declining. The pilot study on Qwen2.5-7B showed high correlation because it only had 28 layers with the zero-shot peak near the top, whereas the full-scale 94-layer models have much more pronounced specialization across deeper layers, which would lower the correlation. I should align my reasoning with the actual metrics: around 18 out of 20 language-architecture pairs show positive correlations, and roughly 60% exhibit the Pareto tradeoff pattern.

For the 94-layer case, if zero-shot performance peaks around 65% depth and then declines by 2-6 percentage points in the final layers, that modest drop across the last third of the model wouldn't be enough to flip the overall Spearman correlation negative—the longer rising portion dominates, yielding a correlation somewhere between +0.45 and +0.65.

Looking at smaller architectures, a 48-layer model peaks later at 70% depth with a shorter decline window, pushing the Spearman higher to +0.5 to +0.7, while a 60-layer model sits in between with +0.45 to +0.65. Across these different model sizes, the positive Spearman trend holds consistently, which aligns with what the metrics show. Now I'm checking how the Pareto tradeoff prevalence actually breaks down by architecture—Qwen appears to have a stronger tradeoff affecting more languages, Llama shows a weaker or more moderate effect with some languages even reversing the trend, and I need to see where Gemma falls.

Looking at the prevalence metric, I'm calculating that across 20 languages and 3 architectures, roughly 30-45 pairs should show a meaningful tradeoff. The actual distribution shows Qwen at 80% of languages affected, Llama at 50%, and Gemma at 60%, which totals to about 63% across all pairs—right in the expected range. This confirms the pattern holds, so I'm ready to move forward with writing out the configuration.

Now I need to verify the layer transfer drop claim. I'm checking whether the performance loss when moving from the zero-shot optimal layer to the English-optimal layer falls within the 2-6 percentage point range. Across the three models, the drops are consistently in that range—5pp for Qwen, 3pp for Llama, and 3pp for Gemma—so this constraint is satisfied.

Now I'm ready to generate the comprehensive YAML output, making sure to incorporate the additional experiments from the extended plan: CORAL comparisons, high-dimensional MMD variants with PCA reduction, multi-seed validation runs, and the mixed β criterion. The core narrative around CaCLR consistency loss is that it meaningfully improves transfer performance, with 1-D logit MMD showing measurable gains when β exceeds zero, and high-dimensional MMD potentially offering even stronger results, while CORAL provides a comparable alternative approach. to MMD
- This means CaCLR is a positive method contribution, not a negative result

The narrative is: "Method contribution paper. CaCLR is a lightweight, label-free method that shifts the Pareto frontier via distributional matching."

OK, one more key metric to be careful about:
`caclr_delta_over_zeroshot_mean_pp: [2.0, 5.0]` → CaCLR improves over zero-shot by 2-5pp on average
`caclr_langs_improved_of_20: [10, 16]` → 10-16 of 20 languages show improvement

This means CaCLR helps but not universally. ~14/20 languages improve, with mean gain of ~3.5pp. The 6 non-improving languages are likely HIGH-resource ones where zero-shot is already strong.

Now I'm looking at the CORAL and high-dimensional extensions—CORAL shows similar effects to MMD within ±0.5pp, while pushing MMD to higher dimensions (d=50) gains about 1pp over the 1-D version, which supports the core distributional matching narrative. I need to finalize the YAML with these metrics in mind, and I'm noting that plan_013 already validated selectivity in the deep layers (0.244-0.262 range) for English on Qwen2.5-7B, though the full cross-lingual extension still needs to confirm artifact rates stay within 5-15%. Structuring the YAML with all planned experiments and their statuses. Plan 013 is already complete with data on probe training with randomly permuted labels across layers and languages, which I should reference while also extrapolating the cross-lingual extension. Writing YAML structure...

I need to clarify the relationship between these plans: plan_001 and plan_002 evaluate five transfer conditions including CaCLR at its optimal settings, while plan_003 handles the detailed hyperparameter sweeps and ablations that determine those optimal settings. So the results flow from plan_003's optimization into plan_001/002's comparative evaluation.

Now I'm thinking through the resource allocation across the twenty languages, starting with the highest tier languages like Chinese, Spanish, French, and German, then considering where Japanese, Dutch, Portuguese, and Italian fit, followed by the mid-tier languages like Hindi, Russian, Korean, and Turkish.

For the best tier performance, I need to set realistic expectations—if eighteen out of twenty languages hit that zero-shot AUROC threshold above 0.58, then Yoruba and Telugu would likely be the borderline cases sitting just under that mark.

Now I'm mapping out the final YAML structure with specific model plans: Qwen3-235B, Llama 4 Scout, and Gemma 4 31B Dense each get comprehensive evaluations with tables, then CaCLR gets detailed ablations and sweeps, followed by decomposition analysis and CKA Simpson's correlation work.

I'm debating whether plan_013's full cross-lingual extension should be its own experiment or integrated into the main model plans, but I think the control task analysis is already covered within plan_013's scope, so I'll keep it contained there rather than duplicating it across the baseline models.

Writing YAML config... OC. In the paper framing: "deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot)."

So depth vs ZS AUROC should be POSITIVE for 16-20 of 20 languages. The MVP data confirms this: best ZS layer is at L22-L27 for most languages (near the top of the 28-layer model), meaning deeper = better.

For the 94-layer Qwen3, the question is where ZS peaks. I think in the "best" tier, the peak should be around 60-70% depth, with a modest decline after that. The overall Spearman would still be positive because the rising portion is longer.

Now I need to set concrete ZS AUROC curves for each architecture, starting with Qwen3-235B at 94 layers with 24 probed layers. Now I'm looking at the performance metrics continuing through higher layer depths, where the EN scores peak around layers 68-72 at 0.835 before declining, while the ZS mean scores show their best performance earlier around layers 44-48 at roughly 0.78 and then gradually decrease as depth increases.

I'm noticing the ZS pattern rises sharply from 0.58 to 0.78 across the first half of layers, then declines steadily to 0.68 in the second half, which creates a weak Spearman correlation around +0.1 to +0.3 — essentially near zero. That's problematic for the key metric, so I need to shift the ZS peak later in the depth range so the rising portion has more weight. I'm revising the approach to have ZS peak around 70% depth instead of 50%, starting with lower initial values and building up more gradually through the early layers.

Now I'm extending this pattern through the remaining layers, with ZS continuing to climb through the middle section and peaking around layer 56 at 0.785, then declining more gradually afterward. This gives me a 15-layer rising phase versus a 9-layer declining phase, which should produce a meaningfully positive Spearman correlation overall.

But that moderate positive correlation—probably in the +0.3 to +0.5 range—might not be sufficient to explain why 16 to 20 languages show positive depth-transfer relationships. Let me reconsider what the metric is actually measuring. The key finding states that across all three architectures, between 16 and 20 languages have positive Spearman correlations for depth versus transfer performance. I need to clarify whether this is an aggregate count or per-architecture, and then figure out which architecture might achieve that 16/20 threshold.

If I assign the counts per architecture—Qwen3 at 16/20 positive (experiencing the strongest Pareto tradeoff where deeper layers show declining zero-shot performance, potentially flipping some languages negative), Llama4 at 19/20 (weaker tradeoff with minimal decline), and Gemma4 at 18/20—they all fit within the expected range. The real question is whether the Pareto tradeoff strength actually correlates with negative Spearman values, or if the zero-shot AUROC curves are rising steeply enough across most languages that even with some decline at deeper layers, the overall correlation remains positive.

I think the pattern is that zero-shot AUROC climbs through the first 60-70% of layers, then dips in the final 30-40%, with high-resource languages showing only a 1-2 percentage point drop at the end while low-resource languages experience a steeper 4-6 point decline. The few languages with negative Spearman—likely yo and te—peak early in the network and have longer declining tails, making their best-performing layer sit somewhere in the middle rather than near the surface. This resolves the apparent contradiction. Now I'll write out the YAML configuration.

I need to think through what realistic numbers should be for these metrics. For Qwen3-235B, I'm setting English's best AUROC at 0.835 around layer 68 (72% depth), with the zero-shot mean across 20 languages peaking at 0.765 around layer 48 (51% depth). The Pareto knee sits between layers 48-56. But I'm realizing the final layer drop metric isn't about the absolute decline from peak to the very last layer—that would be too large. It's specifically about the drop within the final few probed layers themselves.

Re-reading the hypothesis more carefully, "final layers" refers to the deepest 1-3 layers of the model, and the metric captures the local depth-transfer tradeoff right at the end. So for Qwen3-235B's 94 layers, I should be looking at the drop from, say, layer 88 to layer 92 in zero-shot performance, not the full decline from the optimal layer. That keeps the numbers in the expected 2-6 percentage point range. 6pp.

Hmm, maybe the metric means: for a single step at the final layers, the drop per step. Like going from L88 to L92, ZS drops by 3pp.

Or maybe it means: at the deepest probed layers (say 85-100% depth), the ZS drop relative to slightly shallower layers. Not the full drop from the peak.

Actually, looking at the claim: "the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality."

And from paper_framing: "final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages)"

So it's the tradeoff at the VERY final 1-3 layers: going from L_deep-1 to L_deep, EN gains ~0.8pp but ZS drops 1.5-4pp. For the MVP this was L24→L27 (3 layers apart): EN +0.8pp, ZS -2 to -4pp for affected languages. For full-scale with Qwen3-235B, the final probed layers are L84, L88, L92, and the per-step ZS drop should be 2-6pp over those ~2 steps while EN drops slightly. So the metric captures this local tradeoff at the very end, not the total drop from peak—at L88 versus L84, ZS drops about 2pp while EN drops 0.5pp.

Wait, but EN is also dropping at the final layers, not gaining. So there's no Pareto tradeoff there—both metrics decline. The actual Pareto region where EN gains while ZS loses is earlier, around L56-L68, where EN climbs marginally (+1.0pp total) while ZS drops 2.5pp. That's the real tradeoff zone. So maybe "final layers" in the claim refers to the final layers of the Pareto frontier (the EN-optimal end), not the physical final layers of the model.

Let me redefine this: the ZS-optimal layer is around L48, the EN-optimal layer is around L68, and moving between them shows EN gaining 2pp while ZS drops 2.5pp—which fits the [2, 6]pp range. I'm seeing similar patterns across other models too: Llama4 Scout shows about 2pp ZS drop, Gemma4 31B shows about 3pp, all within the expected range.

Now I need to actually write out the YAML configuration. I've been analyzing this long enough. I'm also factoring in the language distribution across 20 languages split into HIGH (8 languages), MID (7 languages), and LOW (5 languages) tiers, and I'm working through the ZS AUROC values at the best-transfer layer to make sure the numbers are consistent across language groups. / 20 = 0.785 ✓

So Qwen3 achieves a mean AUROC of 0.785 at its best-transfer layer with HIGH confidence at 0.82, MID at 0.79, and LOW at 0.72. Now I'm noticing the EN-ZS gap at this layer is only 3 percentage points, but the metric `mean_zs_auroc_drop_vs_en_pp` suggests it should be between 4-8pp across the architecture. This discrepancy makes me think the metric might be measuring the gap at the EN-optimal layer rather than where zero-shot performs best.

Let me reconsider: if I measure both at their respective optimal layers—EN best at 0.835 and ZS mean best at 0.785—that gives a 5pp gap, which fits the expected range. Checking this interpretation across the other models: Llama4 shows a 4pp gap and Gemma4 shows 3.5pp, averaging to about 4.17pp overall. That's within the target range but on the lower end, so I might need to adjust upward.

Adjusting the ZS values slightly lower gives me a more comfortable 5.17pp mean gap. Now I'm settling on final values: Qwen3 at 0.835 EN and 0.775 ZS, Llama4 at 0.815 EN and 0.765 ZS, and Gemma4 at 0.805 EN and 0.760 ZS. This puts the mean EN performance at 0.818 and the mean gap at 5.2pp, both within my target ranges. Next I need to check the zero-shot pass rates where AUROC exceeds 0.58.

Looking at the pass rates across the three models, I'm getting 18/20 for Qwen3, 17/20 for Llama4, and 18/20 for Gemma4, which averages to 17.7 and stays within my [16, 20] constraint. Before I write this up, I want to verify that the CaCLR improvement of +3.5pp over zero-shot across the 20 languages and architectures fits within the [2.0, 5.0] range, and I'm checking how many languages show improvement against the [10, 16] target.

I'm predicting around 14 languages improved for Qwen3 and Gemma4, and 13 for Llama4. Now I'm going to structure the YAML output with the most critical experiments in full detail while keeping the supporting validation experiments more concise. I need to make sure the narrative around CaCLR is solid—the core claim is that the consistency loss provides measurable transfer improvement with strong effect sizes across all four key claims, positioning this as a lightweight, label-free method that shifts the Pareto frontier through distributional matching on the logits.

The high-dimensional extensions look promising too: the PCA-based MMD should strengthen the method contribution by showing even better results than the 1-D version, and CORAL's comparable performance demonstrates that distributional matching works broadly rather than being specific to MMD. I'll organize the experiments starting with the core Pareto frontier results, then layer in the CKA analysis, CaCLR validation, decomposition studies, linear projection work, control tasks, and finally the supporting experiments.

Writing the YAML now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14143273-59c7-4d61-b3d7-ecc6a607b827",
  "isSidechain": false,
  "requestId": "req_011CbFiHHVxCyZSf3DWGPapo",
  "type": "assistant",
  "uuid": "e8d29852-c11f-4032-b16c-41dfda9856bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NdDybSk2Z527WL46NU5zN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4594,
      "cache_creation_input_tokens": 29446,
      "cache_read_input_tokens": 32185,
      "output_tokens": 16793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4594,
          "output_tokens": 16793,
          "cache_read_input_tokens": 32185,
          "cache_creation_input_tokens": 29446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29446
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

_source line 21 · 2026-05-21T12:32:23.088Z_

Let me read the latest dream report and the decisions file to understand the full context before generating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d29852-c11f-4032-b16c-41dfda9856bd",
  "isSidechain": false,
  "requestId": "req_011CbFiHHVxCyZSf3DWGPapo",
  "type": "assistant",
  "uuid": "b5549efd-3d04-49fc-bfd4-b863debfce12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NdDybSk2Z527WL46NU5zN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4594,
      "cache_creation_input_tokens": 29446,
      "cache_read_input_tokens": 32185,
      "output_tokens": 16793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4594,
          "output_tokens": 16793,
          "cache_read_input_tokens": 32185,
          "cache_creation_input_tokens": 29446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29446
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

_source line 22 · 2026-05-21T12:32:24.148Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KAJY9wrfF5zmMYBPAfb9hW`</summary>

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
  "parentUuid": "b5549efd-3d04-49fc-bfd4-b863debfce12",
  "isSidechain": false,
  "requestId": "req_011CbFiHHVxCyZSf3DWGPapo",
  "type": "assistant",
  "uuid": "b11410ce-df19-4731-adb8-df312acbc4fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NdDybSk2Z527WL46NU5zN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4594,
      "cache_creation_input_tokens": 29446,
      "cache_read_input_tokens": 32185,
      "output_tokens": 16793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4594,
          "output_tokens": 16793,
          "cache_read_input_tokens": 32185,
          "cache_creation_input_tokens": 29446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29446
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

_source line 23 · 2026-05-21T12:32:24.572Z_

<details><summary>↩ Tool result · `toolu_01HRp4dHMomGs6AEkhEzLWYQ`</summary>

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
  "parentUuid": "f843be62-203f-4814-9622-e6ebf650c169",
  "isSidechain": false,
  "promptId": "7f6384cd-15ed-4514-b679-c96259e865e9",
  "type": "user",
  "uuid": "c89d39bf-4034-44c9-90e9-eea3e98a0e01",
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
  "sourceToolAssistantUUID": "f843be62-203f-4814-9622-e6ebf650c169",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T12:32:24.162Z_

<details><summary>↩ Tool result · `toolu_01KAJY9wrfF5zmMYBPAfb9hW`</summary>

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
  "parentUuid": "b11410ce-df19-4731-adb8-df312acbc4fa",
  "isSidechain": false,
  "promptId": "7f6384cd-15ed-4514-b679-c96259e865e9",
  "type": "user",
  "uuid": "cb976c1b-4153-4157-8f81-04ca6bb3e72b",
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
  "sourceToolAssistantUUID": "b11410ce-df19-4731-adb8-df312acbc4fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T12:32:24.567Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HRp4dHMomGs6AEkhEzLWYQ`</summary>

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
  "parentUuid": "cb976c1b-4153-4157-8f81-04ca6bb3e72b",
  "isSidechain": false,
  "requestId": "req_011CbFiHHVxCyZSf3DWGPapo",
  "type": "assistant",
  "uuid": "f843be62-203f-4814-9622-e6ebf650c169",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NdDybSk2Z527WL46NU5zN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4594,
      "cache_creation_input_tokens": 29446,
      "cache_read_input_tokens": 32185,
      "output_tokens": 16793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4594,
          "output_tokens": 16793,
          "cache_read_input_tokens": 32185,
          "cache_creation_input_tokens": 29446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29446
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Full-scale models (235B MoE + Scout MoE + Gemma Dense) replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement;…",
  "leafUuid": "c89d39bf-4034-44c9-90e9-eea3e98a0e01",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe transfer and CaCLR calibration",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Assistant

_source line 28 · 2026-05-21T12:33:03.592Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a comprehensive understanding now. Let me generate the full best-tier imagined experiments YAML. I need to:

1. Cover all "planned" experiments (status: planned in experiment_plan)
2. Reference completed experiments' actual data where relevant
3. Ensure internal consistency with the key metric ranges
4. Provide detailed result_rationale for each prediction

The planned experiments from experiment_plan.yaml are:
- plan_001 (Qwen3-235B) - planned
- plan_002 (Llama 4 Scout) - linked to plan_002_v3 (PREPARING)


- plan_003 (CaCLR) - planned
- plan_004 (Decomposition) - planned
- plan_005 (Orthogonality) - planned
- plan_006 (Probe complexity) - planned
- plan_007 (Cross-benchmark) - planned
- plan_008 (Gemma 4 31B) - planned
- plan_009 (Extended languages) - planned
- plan_010 (Quantization validation) - planned
- plan_011 (CKA analysis) - planned
- plan_012 (Linear projection) - planned

I see plan_013 is marked as DONE but appears to have incomplete data, so I'll need to handle that carefully when constructing the imagined results.

Generating YAML with metric ranges... Now I'm looking at the performance metrics across these additional experiments, including the cross-lingual artifact rates and the correlation between depth and transfer effectiveness. I'm structuring the YAML output systematically, organizing each experiment with its expected results and analysis framework, using the language distribution across the 20-language set to ground the predictions. Looking at the pass rates and tradeoff metrics across the three models, Llama4 shows the weakest Pareto tradeoff performance while Qwen3 demonstrates the strongest, with Gemma4 falling in between. The Pareto prevalence analysis reveals that across all sixty language-model pairs, about 63% exhibit Pareto-optimal behavior, with Qwen3 leading at 75% and Llama4 lagging at 50%.

The frontier analysis shows consistent drops of 3-5 percentage points across models when moving away from the Pareto boundary. For the CKA metrics, all three models show statistically significant partial correlations between 0.42 and 0.48 with p-values well below 0.01, confirming the relationship holds across the board with a mean partial rho of 0.447.

The CaCLR improvements average 3.5 percentage points above zero-shot baseline with about 14 out of 20 languages showing gains. Linear projection analysis reveals an 8 percentage point delta for low-resource settings and saturation around 42 language pairs. The decomposition metrics show a 4.5 percentage point transfer improvement after projection with clean separation in 8 out of 10 cases. Control tasks validate selectivity in deeper layers at 0.28 and artifact rates staying around 12%, all within expected ranges.

Now I'm writing the YAML configuration...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c89d39bf-4034-44c9-90e9-eea3e98a0e01",
  "isSidechain": false,
  "requestId": "req_011CbFigAKVDXoZBc5NRm2wR",
  "type": "assistant",
  "uuid": "188f6394-f29c-4986-a53d-1d60c27d3f6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xzq6L5sXjz9FpXFTgy2cpw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31457,
      "cache_read_input_tokens": 93088,
      "output_tokens": 27247,
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
          "output_tokens": 27247,
          "cache_read_input_tokens": 93088,
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

_source line 29 · 2026-05-21T12:36:13.384Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have a full picture of the project state. Let me generate the comprehensive best-tier imagined experiments YAML. Let me be very thorough and ensure internal consistency across all metrics.

Let me now write the complete YAML. I need to be careful about:

1. The Spearman rho sign: depth vs ZS AUROC should be POSITIVE for most languages (deeper generally = better transfer), with a local tradeoff at the deepest layers
2. Internal consistency across experiments
3. All key metrics within the defined ranges
4. Solid rationales for each prediction

Let me also think about the 20 language list. 

Looking at the language set from the plan, I need to organize them by resource tier. I'm categorizing Chinese, Spanish, French, German, Japanese, Dutch, and Portuguese as high-resource languages. Then I'll work through the remaining languages and assign them to mid and low-resource tiers based on their typical representation in modern language models. So the 20 languages in the experiment likely refers to 20 non-English target languages, with the ZS transfer metrics evaluated across those 19 or 20 non-English languages depending on the specific plan. For my imagined experiment, I'll work with 20 non-English target languages, drawing from the set already identified. I'm refining the language selection for the full experiment—pulling from plan_002's list of 19 non-English languages and adding Yoruba to reach 20. I'm organizing them by resource availability: HIGH tier includes the major languages like Chinese, Spanish, French, German, Japanese, Dutch, and Portuguese; MID tier covers moderately resourced languages like Arabic, Hindi, Korean, Russian, Turkish, Vietnamese, Indonesian, and Polish; LOW tier captures the under-resourced languages—Swahili, Bengali, Telugu, Ukrainian, and Yoruba. I'm settling on a distribution across the three tiers: seven languages in the HIGH tier, nine in MID, and four in LOW, which gives me the twenty total I need. Now I'm compiling a cross-architecture comparison table to summarize the performance metrics for the three models. Now I'm checking the consistency of these metrics across the three models—the Simpson partial correlation shows strong positive alignment around 0.41-0.48, and when I calculate the means, everything falls within the expected ranges: the English AUROC averages to 0.818, the zero-shot gap sits at 5.2 percentage points, and the Pareto language prevalence comes in at about 61.7%, all validating that the results are stable and reliable across different model architectures.

Moving on to the remaining projections, I need to estimate the linear projection delta for low-resource languages at around 8 percentage points, the saturation pairs at roughly 40 to reach 95% coverage, and continue validating the difficulty projection improvements.

Writing YAML output... I'm finishing the calculation and adjusting the values slightly upward to hit that 0.775 target mean, tweaking a few of the high and mid-tier language scores to get the average right. I'm adjusting the language scores to get 18 out of 20 passing the threshold, but lowering te to 0.57 and yo to 0.56 brings the mean down to 0.766, which is below my 0.775 target. I need to find a better balance between the pass rate and the mean score. I'm fine-tuning the HIGH tier scores to push the overall mean up to exactly 0.775, which gets me there with a total of 15.509 across 20 languages. For the pass rate, I need yo to dip just below 0.58 so it actually fails and gives me 19/20 instead of a perfect score.

Now I'm setting up the other models with slightly lower performance — Llama4 and Gemma4 both sit about a percentage point below Qwen3 across the board. Looking at the zero-shot pass rates, I'm getting 19/20 for Qwen3, 17/20 for Llama4, and 18/20 for Gemma4, which averages out to exactly 18 passes across the three architectures. That fits the target range of 16-20.

For the CaCLR results, the beta sweep shows a clear inverted-U pattern where the optimal regularization strength is around 0.05, giving about a 3.5 percentage point improvement, while alpha=0.1 works best for calibration. The component ablation reveals that combining all three elements — BCE, SB-ECE, and MMD — delivers the full benefit, with each component contributing to either calibration or transfer performance.

But now I'm noticing something important: high-dimensional MMD actually outperforms the 1-D version by about a full percentage point, which undermines the paper's original defense that 1-D was the principled choice for matching probe output distributions. This suggests the narrative should shift toward recommending high-dim MMD as the stronger approach, even though 1-D still works reasonably well. The variance across seeds is tight at ±0.4pp, so the differences are stable.

Looking at the broader picture, PCA-50 MMD hits the sweet spot around +4.2pp, while PCA-100 starts to degrade slightly due to dimensionality issues. CORAL performs similarly to MMD in the +3.0 to +3.8pp range depending on dimensionality, confirming that distributional matching as a general principle is what's driving the gains here. Now I need to organize all this into the YAML structure.

But there's something important about how CaCLR actually performs in practice: it improves about 10-16 of the 20 languages, which means it's not a universal win. The languages that don't improve are likely the high-resource ones where zero-shot transfer already works well (AUROC above 0.75), so distributional matching adds nothing on top. This is actually a realistic and nuanced result—CaCLR helps most where it's needed, in low and mid-resource settings with weaker zero-shot baselines, while having minimal impact on languages that already transfer effectively. For the mean improvement metric, if roughly 14 languages see around +5pp gains while 6 remain flat, that would average out to the 2-5pp range we're seeing.

Now I need to write out the full YAML with all the experiments, making sure the numbers stay consistent across everything and focusing the most detail on the core experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "188f6394-f29c-4986-a53d-1d60c27d3f6c",
  "isSidechain": false,
  "requestId": "req_011CbFigAKVDXoZBc5NRm2wR",
  "type": "assistant",
  "uuid": "9e854bde-c705-4718-8787-2772de1c1bf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxoZP67NU4rSxKZRRupWxJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31457,
      "cache_read_input_tokens": 93088,
      "output_tokens": 27247,
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
          "output_tokens": 27247,
          "cache_read_input_tokens": 93088,
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

_source line 30 · 2026-05-21T12:43:04.172Z_

Now I have full context. Let me generate the comprehensive best-tier imagined experiments.

```yaml
tier: best
narrative_guidance: >
  Method contribution paper — 因果链完整：Pareto discovery（architecture-dependent depth-transferability
  tradeoff with overall positive depth-transfer trend）→ Decomposition explains it（difficulty
  transfers, capability does not）→ CaCLR solves it（consistency loss shifts Pareto frontier,
  +3.3pp mean, 14/20 languages improved）→ CKA geometric explanation reveals why（Simpson's
  Paradox confirmed across 3 architectures, partial rho +0.44 mean, p<0.01）。四条 claim
  全力度支撑。Headline: "CaCLR-trained correctness probes reduce non-English ECE by 38%
  requiring zero target-language labels." Control task warning（10% cross-lingual artifact rate）
  和 linear projection sample efficiency（~40 pairs to 95%）作为 elevated empirical contributions
  进入 main body。Procrustes effect reversal（threshold ~0.52）为 practitioner 提供直接指导。
  三个架构（Qwen3 MoE + Llama4 MoE + Gemma4 Dense）消除架构混淆因子——phenomenon 是 transformer depth
  的 universal property。Mean EN AUROC 0.818（range 0.805–0.835），ZS 20-lang mean 0.767，
  gap 5.2pp。所有 key metrics 落在 best 区间内。

imagined_experiments:
  - name: "Full Pareto Frontier — Qwen3-235B-A22B (MoE)"
    plan_id: "plan_001"
    description: >
      94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th: L0,L4,...,L92),
      20 typologically diverse languages, English logistic regression probes, 5 transfer
      conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100,
      CaCLR (optimal α=0.1, β=0.05 from plan_003)。验证 MVP 发现的 positive depth-transfer
      trend 和 local deep-layer Pareto tradeoff 在大 MoE 模型上放大。
    expected_results:
      en_best_auroc: 0.835
      en_best_layer_idx: 68
      en_best_depth_pct: 72
      en_auroc_range: [0.59, 0.835]
      en_ece_raw_best: 0.172
      zs_mean_auroc_20lang_at_zs_optimal: 0.775
      zs_best_transfer_layer_idx: 48
      zs_best_transfer_depth_pct: 51
      zs_pass_rate_auroc_gt_058: 19
      zs_fail_langs: [yo]
      zs_auroc_by_tier:
        HIGH_mean: 0.817
        MID_mean: 0.788
        LOW_mean: 0.693
      zs_auroc_selected:
        zh: 0.83
        es: 0.82
        fr: 0.82
        de: 0.82
        ja: 0.81
        nl: 0.81
        pt: 0.81
        ar: 0.80
        hi: 0.79
        ko: 0.79
        ru: 0.80
        tr: 0.78
        vi: 0.77
        id: 0.79
        pl: 0.79
        uk: 0.78
        sw: 0.72
        bn: 0.73
        te: 0.67
        yo: 0.575
      overall_spearman_depth_vs_zs:
        global_rho: 0.68
        global_p: 0.0003
      per_lang_spearman_rho_median: 0.62
      per_lang_positive_rho_count: 17
      per_lang_significant_positive_count: 14
      per_lang_negative_rho_langs: [yo, te, sw]
      pareto_tradeoff_langs_count: 15
      pareto_en_optimal_layer: 68
      pareto_zs_optimal_layer: 48
      pareto_depth_gap_layers: 20
      pareto_zs_drop_at_en_optimal_pp: 3.8
      mean_shift_delta_auroc: 0.0
      linproj_200pairs_mean_auroc: 0.793
      linproj_200pairs_delta_pp: 1.8
      fewshot_25_mean_auroc: 0.762
      fewshot_100_mean_auroc: 0.788
      caclr_mean_auroc: 0.812
      caclr_delta_vs_zs_pp: 3.7
    result_rationale: >
      Qwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 ~3×。Probing scaling 预期 EN
      AUROC 从 0.754 提升至 0.835：更大模型在 intermediate layers 编码更清晰的 correctness signal，
      因为 pretraining loss 更低 → 内部 representations 对 factual accuracy 更 informative。

      Overall positive depth-transfer trend（median per-lang Spearman ρ=+0.62）因为更深层
      encode 更多 semantic content → 更好的 correctness discrimination，且 correctness direction
      的 cross-lingual alignment 在 shallow-to-mid layers 持续改善（CKA 在 0-50% depth 下降缓慢）。
      17/20 languages 有 positive ρ，3 个 negative 的（yo/te/sw）是 LOW-resource：这些语言在
      Qwen3 pretraining corpus 中占比极低（<0.1%），ZS AUROC 的 depth profile 呈倒 U 形
      （peak 在 ~40% depth 而非 >50%），因为深层的 language-specific specialization 对这些语言
      反而有害。

      Local Pareto tradeoff：从 ZS-optimal (L48, 51% depth) 到 EN-optimal (L68, 72% depth)，
      EN 增加 2pp（0.815→0.835）但 ZS 平均下降 3.8pp（0.775→0.737）。这一 tradeoff 在 15/20
      languages 上可观测（ZS-optimal ≠ EN-optimal，gap >1.5pp）。94 层深网络比 28 层 MVP 有
      更大的 specialization 空间，使 EN-optimal 与 ZS-optimal 之间的 depth gap 从 MVP 的 3 层
      扩大至 20 层（22pp depth）。

      MoE routing 在深层产生 language-specific expert activation patterns，加速 CKA cliff
      下降，导致 Qwen3 的 Pareto tradeoff 比 Llama4/Gemma4 更 pronounced（15/20 vs 10-12/20）。

      Mean-shift ΔAUROC ≡ 0：StandardScaler + LR 下 mean-shift 对 AUROC 无影响（rank-invariant,
      MVP 中已数学证明并实验验证）。

      Linear projection (+1.8pp) 通过 Procrustes 捕获 correctness subspace 旋转。
      CaCLR (+3.7pp) 通过 end-to-end 优化超越 linear projection。
      Few-shot-100 (+1.3pp) 在 full-scale 上弱于 ZS 因为 100 个 labeled samples 对 14K
      train set 的 probe 参数贡献边际很小。
    tables:
      - name: "Table 1: Qwen3-235B Pareto Frontier (selected layers)"
        columns: [layer_idx, depth_pct, en_auroc, zs_mean_20, zs_drop_vs_en_pp, on_pareto]
        rows:
          - [4, 4, 0.590, 0.582, 0.8, false]
          - [12, 13, 0.645, 0.636, 0.9, false]
          - [20, 21, 0.710, 0.700, 1.0, false]
          - [28, 30, 0.752, 0.740, 1.2, false]
          - [36, 38, 0.785, 0.770, 1.5, false]
          - [40, 43, 0.798, 0.779, 1.9, false]
          - [44, 47, 0.808, 0.782, 2.6, false]
          - [48, 51, 0.815, 0.775, 4.0, true]
          - [52, 55, 0.822, 0.768, 5.4, true]
          - [56, 60, 0.828, 0.757, 7.1, true]
          - [60, 64, 0.832, 0.745, 8.7, true]
          - [64, 68, 0.834, 0.738, 9.6, true]
          - [68, 72, 0.835, 0.737, 9.8, true]
          - [72, 77, 0.834, 0.725, 10.9, false]
          - [76, 81, 0.830, 0.710, 12.0, false]
          - [80, 85, 0.822, 0.695, 12.7, false]
          - [84, 89, 0.815, 0.678, 13.7, false]
          - [88, 94, 0.805, 0.660, 14.5, false]
          - [92, 98, 0.790, 0.642, 14.8, false]
      - name: "Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3"
        columns: [language, tier, spearman_rho, p_value, significant_at_005]
        rows:
          - [zh, HIGH, 0.75, 0.0001, true]
          - [es, HIGH, 0.72, 0.0002, true]
          - [fr, HIGH, 0.70, 0.0003, true]
          - [de, HIGH, 0.73, 0.0002, true]
          - [ja, HIGH, 0.68, 0.0005, true]
          - [nl, HIGH, 0.71, 0.0003, true]
          - [pt, HIGH, 0.69, 0.0004, true]
          - [ar, MID, 0.67, 0.0006, true]
          - [hi, MID, 0.62, 0.002, true]
          - [ko, MID, 0.65, 0.001, true]
          - [ru, MID, 0.68, 0.0005, true]
          - [tr, MID, 0.60, 0.003, true]
          - [vi, MID, 0.55, 0.007, true]
          - [id, MID, 0.63, 0.002, true]
          - [pl, MID, 0.62, 0.002, true]
          - [uk, MID, 0.58, 0.005, true]
          - [sw, LOW, -0.12, 0.58, false]
          - [bn, LOW, 0.35, 0.10, false]
          - [te, LOW, -0.08, 0.72, false]
          - [yo, LOW, -0.18, 0.42, false]
      - name: "Table 3: Transfer Conditions at ZS-Optimal Layer (L48), Qwen3"
        columns: [condition, mean_auroc_20, delta_vs_zs_pp, requires]
        rows:
          - [zero-shot, 0.775, 0.0, "—"]
          - [mean-shift, 0.775, 0.0, "—"]
          - [linear_proj_200, 0.793, 1.8, "200 parallel pairs"]
          - [few-shot-25, 0.762, -1.3, "25 labeled per lang"]
          - [few-shot-100, 0.788, 1.3, "100 labeled per lang"]
          - [CaCLR, 0.812, 3.7, "parallel activations"]
    figures_description:
      - >
        Figure 1a: EN AUROC (blue) and ZS mean AUROC (orange) vs normalized depth (%).
        Both rise together until ~50% depth, then diverge: EN continues to ~72%, ZS peaks
        and declines. Shaded region between curves from 51-72% depth marks Pareto zone.
      - >
        Figure 1b: Heatmap — ZS AUROC by language (y-axis, ordered HIGH→MID→LOW) × layer
        index (x-axis). Warm yellow band in mid-depth (30-55%), cooling gradient toward
        deep layers, LOW-resource rows cool earliest.
    analysis: >
      Qwen3-235B 展现 strong, consistent positive depth-transfer trend（global ρ=+0.68,
      p=0.0003）和 pronounced local Pareto tradeoff（15/20 langs）。EN-optimal (L68) 与
      ZS-optimal (L48) 相距 20 层，远大于 MVP 的 3 层，确认 tradeoff 在大模型上放大。
      14/20 languages 的 per-language ρ 显著为正，表明 "deeper is generally better for transfer"
      是跨语言一致的。3 个 LOW-resource languages (yo/te/sw) 显示 negative/near-zero ρ，
      因为这些语言的 correctness signal quality 在深层退化快于 probe discrimination 的提升。
      CaCLR 在 ZS-optimal layer 提供 +3.7pp，是所有 label-free methods 中最优。

  - name: "Full Pareto Frontier — Llama 4 Scout (MoE)"
    plan_id: "plan_002"
    description: >
      48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every 4th:
      L0,L4,...,L44,L47), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B 的
      weaker/mixed tradeoff pattern 是否是 Llama 架构家族特征。
    expected_results:
      en_best_auroc: 0.815
      en_best_layer_idx: 36
      en_best_depth_pct: 75
      en_auroc_range: [0.57, 0.815]
      en_ece_raw_best: 0.178
      zs_mean_auroc_20lang_at_zs_optimal: 0.765
      zs_best_transfer_layer_idx: 28
      zs_best_transfer_depth_pct: 58
      zs_pass_rate_auroc_gt_058: 17
      zs_fail_langs: [yo, te, sw]
      zs_auroc_by_tier:
        HIGH_mean: 0.808
        MID_mean: 0.778
        LOW_mean: 0.672
      per_lang_spearman_rho_median: 0.72
      per_lang_positive_rho_count: 19
      per_lang_significant_positive_count: 16
      per_lang_negative_rho_langs: [yo]
      pareto_tradeoff_langs_count: 10
      pareto_zs_drop_at_en_optimal_pp: 2.5
      mean_shift_delta_auroc: 0.0
      linproj_200pairs_mean_auroc: 0.781
      fewshot_100_mean_auroc: 0.778
      caclr_mean_auroc: 0.798
      caclr_delta_vs_zs_pp: 3.3
    result_rationale: >
      Llama 4 Scout 延续 MVP Llama-3.1-8B 的 weaker tradeoff 模式但在关键方面加强。
      Per-language Spearman median ρ=+0.72 高于 Qwen3 (0.62)，因为 Llama4 仅 48 层——
      更少的深层 specialization 空间意味着 ZS AUROC 的下降区间更短（最后 ~20% 层），
      而上升区间（前 58% 层）主导了 overall correlation。19/20 languages 有 positive ρ
      （仅 yo negative）。

      Pareto tradeoff 仅 10/20 languages（vs Qwen3 15/20），且 ZS drop 仅 2.5pp
      （vs Qwen3 3.8pp）。这与 MVP 一致（Llama-3.1-8B: 2/5 langs showed tradeoff,
      ar/ko 在深层反而改善）。归因于 Meta 的 multilingual training recipe：Llama4
      在 pretraining 中对中高资源语言的 cross-lingual alignment 更均匀，深层
      language-specific routing 效应弱于 Qwen3。

      EN best AUROC 0.815 低于 Qwen3 的 0.835，部分因为 17B active params < 22B
      (Qwen3)，部分因为 W4A16 量化引入 ~0.3pp noise（plan_010 验证）。

      Architecture-dependent tradeoff strength 是 Claim 1 核心：
      Qwen3 strong (15/20, -3.8pp) vs Llama4 weak (10/20, -2.5pp)，
      median per-lang ρ 差异虽然在同一方向（都正），但 Qwen3 的 Pareto zone 更宽。
    tables:
      - name: "Table 4: Llama 4 Scout Pareto Frontier"
        columns: [layer_idx, depth_pct, en_auroc, zs_mean_20, on_pareto]
        rows:
          - [4, 8, 0.570, 0.562, false]
          - [8, 17, 0.640, 0.630, false]
          - [12, 25, 0.700, 0.690, false]
          - [16, 33, 0.740, 0.728, false]
          - [20, 42, 0.768, 0.755, false]
          - [24, 50, 0.785, 0.764, false]
          - [28, 58, 0.798, 0.765, true]
          - [32, 67, 0.808, 0.755, true]
          - [36, 75, 0.815, 0.742, true]
          - [40, 83, 0.810, 0.722, false]
          - [44, 92, 0.795, 0.695, false]
          - [47, 98, 0.778, 0.668, false]
      - name: "Table 5: Architecture-Dependent Pareto Summary"
        columns: [metric, Qwen3_235B, Llama4_Scout, interpretation]
        rows:
          - [en_best_auroc, 0.835, 0.815, "both strong, Qwen slightly higher (22B>17B active)"]
          - [zs_mean_at_zs_opt, 0.775, 0.765, "comparable transfer quality"]
          - [per_lang_rho_median, "+0.62", "+0.72", "both positive; Llama higher (fewer deep layers)"]
          - [positive_rho_langs, "17/20", "19/20", "Llama more consistent"]
          - [pareto_tradeoff_langs, "15/20", "10/20", "Qwen stronger tradeoff"]
          - [pareto_zs_drop_pp, 3.8, 2.5, "Qwen steeper"]
          - [best_transfer_depth_pct, 51, 58, "comparable mid-depth zone"]
    figures_description:
      - >
        Figure 2: Overlaid Pareto frontiers (normalized depth %). Qwen3 (blue) and Llama4
        (orange) share similar shape but Qwen3 has wider divergence zone between EN and ZS
        curves. Both peak in transfer at 51-58% depth.
      - >
        Figure 3: Per-language Spearman ρ distribution — violin plots. Both architectures
        cluster on the positive side. Llama4 tighter (0.4-0.85), Qwen3 wider spread
        (−0.2 to 0.8) with 3 LOW-resource outliers below zero.
    analysis: >
      Llama4 与 Qwen3 的对比确认 architecture-dependent tradeoff strength。两者都有
      positive depth-transfer trend 和 local Pareto tradeoff，但 effect sizes 不同：
      Qwen3 在 15/20 languages 上有 measurable tradeoff（mean drop 3.8pp），Llama4
      仅 10/20（mean drop 2.5pp）。差异无法从 domain adaptation theory 预测——
      这是 architecture/training-recipe 的 empirical finding。Best-transfer depth
      converges to 51-58%，暗示 universal "mid-depth transfer zone"。

  - name: "Full Pareto Frontier — Gemma 4 31B Dense"
    plan_id: "plan_008"
    description: >
      60 text layers, dense architecture, BF16 (~62.5GB, single 96GB GPU), 16 probed
      layers (every 4th + final: L0,L4,...,L56,L59), 20 languages, 5 transfer conditions。
      P0 priority — provides dense vs MoE architectural contrast, eliminates confound
      between architecture type and tradeoff strength。无量化 → 消除量化 confound。
    expected_results:
      en_best_auroc: 0.805
      en_best_layer_idx: 44
      en_best_depth_pct: 73
      en_auroc_range: [0.57, 0.805]
      en_ece_raw_best: 0.185
      zs_mean_auroc_20lang_at_zs_optimal: 0.760
      zs_best_transfer_layer_idx: 36
      zs_best_transfer_depth_pct: 60
      zs_pass_rate_auroc_gt_058: 18
      zs_fail_langs: [yo, te]
      zs_auroc_by_tier:
        HIGH_mean: 0.802
        MID_mean: 0.772
        LOW_mean: 0.670
      per_lang_spearman_rho_median: 0.65
      per_lang_positive_rho_count: 18
      per_lang_significant_positive_count: 14
      pareto_tradeoff_langs_count: 12
      pareto_zs_drop_at_en_optimal_pp: 3.0
      linproj_200pairs_mean_auroc: 0.776
      caclr_mean_auroc: 0.790
      caclr_delta_vs_zs_pp: 3.0
      simpson_partial_rho: 0.44
      simpson_partial_p: 0.004
    result_rationale: >
      Gemma4 31B Dense 是三架构中唯一的 dense model，消除了 "MoE routing 导致 Pareto
      tradeoff" 的替代解释。EN best AUROC 0.805 低于两个 MoE 模型（0.835/0.815），
      因为 31B dense < 22B/17B MoE active（MoE 的 expert routing 提供 effective capacity
      boost，使相同 active param 下 probe 信号更强）。

      Pareto tradeoff 在 12/20 languages 上可观测（介于 Qwen3 15/20 和 Llama4 10/20
      之间），ZS drop 3.0pp。Dense architecture 没有 routing-specific specialization，
      但深层仍然发生 language-specific feature specialization（attention heads 在
      deep layers 对不同语言的 subword patterns 有不同 activation）。这证实
      Pareto tradeoff 是 transformer depth 的 universal property，不是 MoE routing
      的 artifact。

      Simpson's Paradox 在 dense 架构上同样成立（partial ρ=+0.44, p=0.004），
      确认 geometric insight 是 architecture-universal。BF16 无量化 →
      消除量化 distortion confound，使 CKA 和 subspace angle 分析更 reliable。

      Per-lang Spearman median ρ=+0.65（介于 Qwen 0.62 和 Llama 0.72 之间），
      60 层提供的深层 specialization 空间在两者之间。
    tables:
      - name: "Table 6: Three-Architecture Comprehensive Summary"
        columns: [model, type, layers, en_best, zs_mean_20, en_zs_gap_pp, pareto_rho_median, pareto_langs, simpson_partial_rho, caclr_delta_pp]
        rows:
          - [Qwen3-235B, MoE, 94, 0.835, 0.775, 6.0, "+0.62", "15/20", "+0.48", 3.7]
          - [Llama4 Scout, MoE, 48, 0.815, 0.765, 5.0, "+0.72", "10/20", "+0.41", 3.3]
          - [Gemma4 31B, Dense, 60, 0.805, 0.760, 4.5, "+0.65", "12/20", "+0.44", 3.0]
          - ["Mean (3 arch)", "—", "—", 0.818, 0.767, 5.2, "+0.66", "37/60=62%", "+0.44", 3.3]
    figures_description:
      - >
        Figure 9: Three-architecture Pareto frontiers overlaid on normalized depth (%).
        All three share the same qualitative shape: rising together until 50-60%, then
        diverging. Qwen (blue) widest divergence, Llama (orange) narrowest, Gemma (green)
        intermediate. Remarkably similar knee locations (51-60% depth).
    analysis: >
      Three-architecture replication 是 universality claim 最强证据。Simpson's Paradox
      在 3/3 architectures 上 confirmed (partial ρ range 0.41-0.48, all p<0.01)。
      Dense vs MoE contrast minimal — phenomenon 是 transformer depth 的 property。
      Mean EN AUROC 0.818 在 [0.80, 0.86] 内。Mean gap 5.2pp 在 [4, 8] 内。
      Pareto prevalence 62% 在 [0.5, 0.75] 内。CaCLR 一致 +3.0-3.7pp。

  - name: "CKA Cross-Lingual Similarity & Simpson's Paradox"
    plan_id: "plan_011"
    description: >
      Linear CKA (EN vs each target) at every probed layer, 20 languages × 3 models。
      核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b) partial
      Spearman controlling for normalized depth — THE single most important analysis,
      (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。
      验证 pilot Simpson's Paradox 在 full-scale 上 3 架构复现。
    expected_results:
      qwen3_raw_rho: -0.38
      qwen3_raw_p: 0.0001
      llama4_raw_rho: -0.42
      llama4_raw_p: 0.0001
      gemma4_raw_rho: -0.40
      gemma4_raw_p: 0.0001
      qwen3_partial_rho: 0.48
      qwen3_partial_p: 0.0018
      qwen3_partial_bootstrap_ci_95: [0.30, 0.63]
      llama4_partial_rho: 0.41
      llama4_partial_p: 0.0065
      llama4_partial_bootstrap_ci_95: [0.21, 0.58]
      gemma4_partial_rho: 0.44
      gemma4_partial_p: 0.0038
      gemma4_partial_bootstrap_ci_95: [0.26, 0.60]
      simpson_paradox_confirmed_all_3_arch: true
      qwen3_per_layer_positive_count_of_24: 19
      qwen3_per_layer_significant_count_of_24: 8
      llama4_per_layer_positive_count_of_12: 10
      llama4_per_layer_significant_count_of_12: 4
      gemma4_per_layer_positive_count_of_16: 13
      gemma4_per_layer_significant_count_of_16: 6
      cka_peak_depth_pct_range: [15, 25]
      cka_peak_value_range: [0.82, 0.86]
      transfer_collapse_cka_threshold: 0.35
      below_threshold_mean_zs_auroc: 0.60
      above_threshold_mean_zs_auroc: 0.74
      correctness_subspace_angle_within_layer_mean_deg: 12.8
      correctness_subspace_angle_within_layer_std_deg: 5.4
      correctness_subspace_angle_across_layer_mean_deg: 37.5
      correctness_subspace_angle_across_layer_std_deg: 10.8
      random_baseline_angle_deg: 87.1
    result_rationale: >
      Simpson's Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper → representations
      diverge → CKA drops）和 ZS AUROC（deeper → EN probe更强 → higher absolute AUROC up
      to mid-depth），创造了 depth confound。Raw pooled correlation 为负：shallow layers 有
      high CKA 但 low AUROC（probe 本身弱），deep layers 有 low CKA 但 moderate/declining
      AUROC。控制 depth 后，within 每个 layer，higher CKA 的语言确实有 better transfer，
      partial ρ 为正。

      MVP pilot（Llama, 5 langs × 9 layers）已展现 ρ=+0.41, p=0.006。Full-scale（20 langs
      × 12-24 layers per arch）增强统计 power：per-layer test 从 n=5 增至 n=20。
      MVP Qwen pilot 仅 ρ=+0.18 (p=0.274)，full-scale 上升至 +0.48 因为：(1) n 从 5 增至
      20 语言，power 大幅提升；(2) 20 语言覆盖更宽的 CKA 范围（增加了极低 CKA 的 yo/te
      和高 CKA 的 nl/pt），扩大了 within-layer variance。

      Subspace angle analysis 提供 structural grounding：correctness direction 在同一 layer
      内跨语言仅旋转 ~13°（near-universal），但跨 layer 旋转 ~38°（significant drift），
      vs random baseline ~87°。这解释了为何 within-layer CKA 预测 transfer（correctness
      direction 对齐良好）但 raw pooled 不预测（depth confound 混淆了 correctness 与 non-
      correctness dimensions 的 divergence）。

      CKA cliff threshold ~0.35 直接解释了 architecture-dependent tradeoff 差异：Qwen3
      的 CKA cliff 更陡（deep-layer CKA 下降更快因为 MoE routing），导致更多语言在
      deep layers 穿越 0.35 threshold → strong tradeoff。Llama4 cliff 较缓 → weak tradeoff。
      Gemma4（dense）cliff 速率介于两者之间。
    tables:
      - name: "Table 7: Simpson's Paradox — Raw vs Partial Correlation (3 Architectures)"
        columns: [model, analysis, spearman_rho, p_value, bootstrap_95CI, interpretation]
        rows:
          - [Qwen3-235B, "raw pooled", -0.38, "<0.001", "[-0.46, -0.29]", "negative — depth confound"]
          - [Qwen3-235B, "partial (controlling depth)", +0.48, 0.0018, "[+0.30, +0.63]", "positive — genuine geometric signal"]
          - [Llama4 Scout, "raw pooled", -0.42, "<0.001", "[-0.51, -0.32]", "negative — depth confound"]
          - [Llama4 Scout, "partial (controlling depth)", +0.41, 0.0065, "[+0.21, +0.58]", "positive — genuine geometric signal"]
          - [Gemma4 31B, "raw pooled", -0.40, "<0.001", "[-0.49, -0.30]", "negative — depth confound"]
          - [Gemma4 31B, "partial (controlling depth)", +0.44, 0.0038, "[+0.26, +0.60]", "positive — genuine geometric signal"]
      - name: "Table 8: Subspace Angle Analysis (correctness direction, pooled across archs)"
        columns: [comparison_type, mean_angle_deg, std_deg, interpretation]
        rows:
          - ["within-layer cross-language", 12.8, 5.4, "highly aligned — correctness direction is near-universal"]
          - ["cross-layer same-language", 37.5, 10.8, "significant drift — direction rotates with depth"]
          - ["random baseline (shuffled)", 87.1, 2.0, "near-orthogonal — confirms non-trivial signal"]
      - name: "Table 9: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)"
        columns: [depth_pct, HIGH_CKA, MID_CKA, LOW_CKA, overall_CKA]
        rows:
          - [13, 0.87, 0.80, 0.64, 0.79]
          - [30, 0.85, 0.78, 0.60, 0.77]
          - [47, 0.70, 0.58, 0.38, 0.58]
          - [64, 0.50, 0.38, 0.24, 0.39]
          - [77, 0.40, 0.28, 0.16, 0.30]
          - [94, 0.27, 0.19, 0.10, 0.20]
    figures_description:
      - >
        Figure 4a: Simpson's Paradox visualization (2-panel). Left: raw scatter (CKA vs ZS
        AUROC), depth-colored points, negative trend line. Right: partial residual plot after
        depth control, positive trend line. Sign reversal is dramatic.
      - >
        Figure 4b: CKA × layer × language heatmap for all 3 architectures (3 panels).
        Clear gradient from warm (shallow, high CKA) to cool (deep, low CKA). LOW-resource
        rows cool faster. Qwen3 steepest gradient, Llama4 shallowest.
      - >
        Figure 4c: CKA threshold scatter. ZS AUROC (y) vs CKA (x), all 3 archs pooled.
        Vertical dashed line at CKA=0.35. Below: scattered, mean ZS=0.60. Above: tight
        cluster, mean ZS=0.74.
    analysis: >
      Simpson's Paradox 在 3/3 architectures 上显著复现（partial ρ: 0.41-0.48, all p<0.01,
      all bootstrap CIs exclude zero）。这是本文核心几何洞见——不是 trivially expected from
      measurement overlap：sign reversal 从负到正是 non-trivial 的。Subspace angle analysis
      提供 mechanistic grounding。CKA cliff threshold ~0.35 connects Claim 1 (Pareto) with
      Claim 4 (geometry)。所有 partial correlations 的 bootstrap CIs 在 [0.3, 0.55] key
      metric range 内。

  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: "plan_003"
    description: >
      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits + PCA-reduced
      activations)。English labels + parallel activations from GlobalMMLU test-split 70/30。
      Compare vs zero-shot/mean-shift/linear-proj/few-shot across full Pareto frontier,
      3 models × 20 languages。α sweep [0.01-10], β sweep [0.001-1.0]。扩展分析：CORAL loss
      对比, high-dim MMD (PCA d=50/100), multi-seed (5 seeds), mixed β criterion (zh+sw)。
    expected_results:
      best_alpha: 0.1
      best_beta: 0.05
      caclr_mean_delta_auroc_vs_zs_pp: 3.3
      caclr_delta_at_deep_layers_pp: 4.5
      caclr_delta_at_shallow_layers_pp: 1.2
      caclr_langs_improved_of_20: 14
      caclr_langs_hurt_of_20: 1
      caclr_improvement_by_tier:
        HIGH_mean_delta_pp: 1.2
        HIGH_improved_of_7: 3
        MID_mean_delta_pp: 3.8
        MID_improved_of_9: 8
        LOW_mean_delta_pp: 6.5
        LOW_improved_of_4: 3
      beta_sweep:
        beta_0: {delta_auroc_pp: 0.0, delta_ece_pp: 0.0}
        beta_0001: {delta_auroc_pp: 0.5, delta_ece_pp: -0.3}
        beta_001: {delta_auroc_pp: 1.6, delta_ece_pp: -0.9}
        beta_005: {delta_auroc_pp: 3.3, delta_ece_pp: -2.2}
        beta_01: {delta_auroc_pp: 3.0, delta_ece_pp: -1.8}
        beta_10: {delta_auroc_pp: 0.6, delta_ece_pp: -0.3}
      alpha_sweep:
        alpha_001: {ece_improvement_pp: 1.2}
        alpha_01: {ece_improvement_pp: 3.0}
        alpha_10: {ece_improvement_pp: 2.6}
        alpha_100: {ece_improvement_pp: -0.8}
      component_ablation:
        bce_only_mean_auroc: 0.767
        bce_sbece_mean_auroc: 0.774
        bce_mmd_mean_auroc: 0.792
        bce_sbece_mmd_mean_auroc: 0.800
      high_dim_mmd:
        pca_50_delta_vs_zs_pp: 4.2
        pca_100_delta_vs_zs_pp: 3.8
        pca_50_vs_1d_delta_pp: 0.9
      coral_comparison:
        coral_1d_delta_pp: 2.8
        coral_pca50_delta_pp: 3.6
        mmd_vs_coral_1d_diff_pp: 0.5
      multi_seed_std_pp: 0.35
      mixed_beta_criterion_best_beta: 0.05
      mixed_beta_criterion_note: "same optimum as EN-only; no systematic bias"
      ece_reduction_vs_temp_scaling_pct: 38
      parallel_set_size_per_lang_mean: 2800
      parallel_set_size_per_lang_range: [1900, 4100]
      implementation_spec:
        mmd_kernel: "Gaussian RBF, bandwidth=median heuristic"
        optimizer: "Adam, lr=1e-3, linear warmup 10%, cosine decay"
        epochs: 50
        early_stopping: "patience=10, monitor=val_auroc on 15% held-out from probe_train"
        initialization: "from standard LR solution"
        batch_size: 256
        mmd_overlap: "same items as BCE (overlapping)"
    result_rationale: >
      CaCLR 的 consistency loss (β·MMD) 强制 probe 学习 language-invariant features。

      β sweep 的 inverted-U 形状源于 regularization dynamics：β=0.001 时 MMD gradient
      太弱（被 BCE gradient noise 淹没），β=1.0 时 MMD 主导优化（probe 牺牲 accuracy
      来匹配 distributions，EN AUROC 下降 ~1.5pp）。Optimal β=0.05 平衡两者——
      consistency gradient 足够影响 probe direction 但不主导。

      Deep-layer improvement (+4.5pp) 远大于 shallow (+1.2pp) 因为：deep layers 的
      capability-specific component 更大（Claim 2 decomposition），CaCLR 的 consistency
      loss 恰好 target 这个 component。Shallow layers 的 transfer 本身就好（difficulty-
      dominant），CaCLR 提供的边际改善有限。

      14/20 languages improved (10-16 range 内)：6 个 non-improving 主要是 HIGH-resource
      (zh/es/fr/de) 在 shallow/mid layers 已接近 ceiling，CaCLR 的 distributional matching
      在 already-aligned distributions 上无显著增益。1 个 hurt (yo) 因为 parallel
      activations 质量太差（translation artifacts in GlobalMMLU Yoruba），MMD matching
      反而引入 noise。

      High-dim MMD (PCA-50) 优于 1-D (+4.2pp vs +3.3pp)：50-D space 捕获了更多
      distributional structure（不只 mean/variance，还有 covariance patterns）。但
      PCA-100 略退（+3.8pp），curse of dimensionality 开始影响 MMD estimation。
      这表明 optimal dimensionality 在 d~50，与 correctness subspace 的 effective
      rank 一致（~30-50 principal components capture 95% of probe-relevant variance）。

      CORAL (+2.8pp 1-D, +3.6pp PCA-50) 与 MMD 方向一致但 1-D 弱于 MMD（CORAL 匹配
      second-order statistics，在 1-D 只有 variance matching，信息量不如 kernel-based
      MMD）。PCA-50 下 CORAL 接近 MMD。这证实 distributional matching 一般性地 work，
      非 MMD-specific。

      Component ablation：BCE alone (probe baseline) → +SB-ECE (+0.7pp, calibration
      focus) → +MMD (+2.5pp, consistency is the main contributor) → full CaCLR
      (+3.3pp, synergy between calibration and consistency)。

      ECE reduction 38% vs temperature scaling：CaCLR 在训练期间优化 calibration
      (SB-ECE) + cross-lingual consistency (MMD)，比 post-hoc temperature scaling
      更 effective，因为 temperature scaling 只缩放 logits（不改变 decision boundary）
      而 CaCLR 修改了 probe 的 feature extraction direction。
    tables:
      - name: "Table 10: β Sweep — Consistency Loss Effect (3-arch average)"
        columns: [beta, delta_auroc_vs_zs_pp, delta_ece_vs_zs_pp, note]
        rows:
          - [0.0, 0.0, 0.0, "BCE-only baseline"]
          - [0.001, 0.5, -0.3, "marginal — gradient noise dominates"]
          - [0.01, 1.6, -0.9, "clear positive signal emerges"]
          - [0.05, 3.3, -2.2, "optimal — best accuracy-consistency tradeoff"]
          - [0.1, 3.0, -1.8, "slight over-regularization"]
          - [1.0, 0.6, -0.3, "MMD dominates → probe accuracy degrades"]
      - name: "Table 11: CaCLR vs All Methods (at ZS-optimal layer, 3-arch average)"
        columns: [method, auroc_mean_20, ece_mean_20, delta_vs_zs_pp, requires]
        rows:
          - [zero-shot, 0.767, 0.118, 0.0, "—"]
          - [mean-shift, 0.767, 0.118, 0.0, "—"]
          - [linear_proj_50, 0.781, 0.100, 1.4, "50 parallel pairs"]
          - [linear_proj_200, 0.783, 0.097, 1.6, "200 parallel pairs"]
          - [few-shot-25, 0.754, 0.108, -1.3, "25 labeled per lang"]
          - [few-shot-100, 0.785, 0.090, 1.8, "100 labeled per lang"]
          - [CaCLR (1-D MMD), 0.800, 0.073, 3.3, "parallel activations"]
          - [CaCLR (PCA-50 MMD), 0.809, 0.068, 4.2, "parallel activations"]
      - name: "Table 12: Distributional Matching Comparison (PCA-50 space)"
        columns: [method, dim, delta_vs_zs_pp, note]
        rows:
          - [MMD-1D, 1, 3.3, "logit-space, principled minimal"]
          - [MMD-PCA50, 50, 4.2, "activation PCA, captures covariance"]
          - [MMD-PCA100, 100, 3.8, "slight curse of dimensionality"]
          - [CORAL-1D, 1, 2.8, "second-order, less info in 1D"]
          - [CORAL-PCA50, 50, 3.6, "CORAL approaches MMD at d=50"]
      - name: "Table 13: CaCLR Depth Profile (Qwen3, mean across 20 langs)"
        columns: [depth_pct, zs_auroc, caclr_auroc, delta_pp]
        rows:
          - [30, 0.740, 0.752, 1.2]
          - [43, 0.779, 0.798, 1.9]
          - [51, 0.775, 0.805, 3.0]
          - [60, 0.757, 0.798, 4.1]
          - [72, 0.737, 0.785, 4.8]
          - [85, 0.695, 0.740, 4.5]
    figures_description:
      - >
        Figure 5: β sweep curve — delta AUROC (y) vs log10(β) (x). Clear inverted-U,
        peak at β=0.05. Shaded band shows ±1 std across 5 seeds (narrow, ~0.35pp).
        Inset: corresponding ECE improvement mirrors the AUROC curve.
      - >
        Figure 6: CaCLR depth profile (Qwen3). ZS (blue dashed) vs CaCLR (red solid)
        across normalized depth. Gap widens monotonically from shallow (+1.2pp) to
        deep (+4.8pp). Demonstrates CaCLR specifically addresses deep-layer degradation.
      - >
        Figure 7: CaCLR improvement by resource tier (grouped bar chart). LOW tier
        benefits most (+6.5pp), HIGH tier least (+1.2pp). Inverse resource-level
        scaling of CaCLR benefit.
    analysis: >
      CaCLR 作为正面方法贡献：β>0 一致地 shifts Pareto frontier，mean +3.3pp AUROC
      和 -38% ECE vs temperature scaling。Component ablation 证实 L_consistency (MMD)
      是主要 contributor (+2.5pp)，L_SB-ECE 提供 complementary calibration (+0.7pp)。
      High-dim MMD (PCA-50) 进一步提升至 +4.2pp，但即使 1-D logit MMD 已经 significant。
      CORAL 的可比结果确认 distributional matching 一般性地 work。Multi-seed std 仅
      ±0.35pp，confirming robustness。Deep-layer improvement 模式与 decomposition
      (Claim 2) 形成因果闭环。Headline 可用："CaCLR-trained probes reduce non-English
      ECE by 38% requiring zero target-language labels."

  - name: "Difficulty-Controlled Ablation (Decomposition)"
    plan_id: "plan_004"
    description: >
      IRT difficulty probes (Ridge regression on human difficulty scores per Civelli et al.),
      project out difficulty direction, retrain correctness probes on residuals, evaluate
      transfer。10 languages (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) × 8
      layers (20-90% depth) per model。Random-direction control included。
    expected_results:
      difficulty_probe_r2_mean: 0.67
      difficulty_probe_r2_range: [0.54, 0.76]
      difficulty_var_explained_of_correctness_pct: 62
      capability_var_explained_pct: 38
      difficulty_transfer_degradation_share_pct: 14
      capability_transfer_degradation_share_pct: 86
      residual_en_auroc_drop_after_projection_pp: 4.2
      residual_zs_transfer_improvement_pp: 4.5
      capability_transfer_drop_by_depth:
        20pct: 0.5
        40pct: 2.2
        60pct: 5.0
        80pct: 8.8
      random_direction_control_delta_pp: -1.5
      langs_showing_clean_separation_of_10: 8
      prescriptive_accuracy_pct: 76
    result_rationale: >
      IRT difficulty 是 language-agnostic property：hard questions are hard everywhere
      (Civelli et al. 已验证跨语言 difficulty 相关性 r>0.85)。Ridge regression captures
      this linearly (R²=0.67)。Difficulty 占 correctness variance 的 62% 但仅贡献 14%
      的 transfer degradation，因为 difficulty signal 本质是 universal 的——无论用
      哪种语言的 representation，difficult items 的 activation patterns 都类似。

      Capability-specific residual 仅占 38% variance 但驱动 86% 的 transfer degradation，
      且 degradation 随 depth 指数增长（20%→80% depth: 0.5→8.8pp）。这解释了 Pareto
      frontier 的 mechanistic origin：deep layers 的 EN probe improvement 主要来自
      capability-specific component（language-dependent competence patterns），而这个
      component 恰好最难 transfer。

      Projecting out difficulty 后 EN AUROC 下降 4.2pp（移除了 easy-hard distinction
      信号），但 ZS transfer 改善 4.5pp（关键发现：removing difficulty noise exposes
      the capability signal that's harder to transfer but also more language-specific;
      the residual probe that's trained purely on capability actually transfers BETTER
      on average because it's forced to find the language-agnostic component of capability）。
      Within [3, 6]pp key metric range。

      8/10 languages 显示 clean separation（difficulty component clearly universal,
      capability component clearly language-specific）。2 个 exceptions (sw, bn)
      因 LOW-resource translation quality 使 difficulty labels 本身有 noise。

      Random-direction control (-1.5pp) 确认 difficulty projection 是 genuine 的，
      不是 dimensionality reduction artifact。

      Prescriptive accuracy 76%：给定 difficulty/capability ratio at each language-layer,
      预测最优策略 (zero-shot for difficulty-dominant vs CaCLR for capability-dominant)
      在 76% 的 cases 中正确。
    tables:
      - name: "Table 14: Decomposition Results (3-arch pooled)"
        columns: [component, var_pct, transfer_auroc_mean, transfer_drop_pp, degradation_share_pct]
        rows:
          - [full_correctness, 100, 0.767, 5.2, 100]
          - [difficulty_shared, 62, 0.755, 0.7, 14]
          - [capability_specific, 38, 0.672, 7.8, 86]
          - [random_direction_control, "—", 0.752, "—", "—"]
      - name: "Table 15: Capability Transfer Drop by Depth Band"
        columns: [depth_band, difficulty_drop_pp, capability_drop_pp, ratio]
        rows:
          - ["20-30%", 0.2, 0.5, "2.5×"]
          - ["35-50%", 0.5, 2.2, "4.4×"]
          - ["55-70%", 0.8, 5.0, "6.3×"]
          - ["75-90%", 1.2, 8.8, "7.3×"]
    figures_description:
      - >
        Figure 8: Stacked area chart — difficulty (blue, near-flat) vs capability (red,
        exponentially rising) transfer degradation across normalized depth. Clear separation:
        difficulty barely degrades; capability drives almost all degradation, accelerating
        with depth.
    analysis: >
      Decomposition 清晰分离 transferable vs non-transferable components。4.5pp transfer
      improvement after difficulty projection（in [3,6] range）直接 actionable：practitioners
      可以 train probes on difficulty-controlled representations。8/10 languages clean
      separation 在 [7,10] range。CaCLR 的 deep-layer improvement 与 capability
      degradation profile 完美对应——CaCLR 的 consistency loss targets exactly the
      capability-specific component that decomposition identifies。

  - name: "Linear Projection Sensitivity & Procrustes Reversal"
    plan_id: "plan_012"
    description: >
      Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。
      3 models × 5 representative layers × 20 languages。确定 saturation point 和
      resource-tier stratification。识别 Procrustes effect reversal threshold。
    expected_results:
      pairs_to_95pct_overall: 40
      pairs_to_95pct_HIGH: 22
      pairs_to_95pct_MID: 36
      pairs_to_95pct_LOW: 48
      saturation_curve:
        pairs_10_pct_of_200: 0.70
        pairs_20_pct_of_200: 0.84
        pairs_30_pct_of_200: 0.92
        pairs_50_pct_of_200: 0.97
        pairs_100_pct_of_200: 0.99
      pairs_200_baseline_auroc_mean: 0.783
      procrustes_reversal_threshold_zs_auroc: 0.52
      procrustes_helps_below_threshold_delta_pp: 4.2
      procrustes_hurts_above_threshold_delta_pp: -1.0
      low_resource_delta_over_zs_pp: 8.2
      multi_seed_std_pp: 0.28
    result_rationale: >
      Procrustes alignment 学习 EN→target rotation matrix。20 pairs 即可估计 dominant
      rotational components：correctness subspace 是 low-dimensional 的（subspace angle
      分析显示前 30-50 principal angles 解释 95%+ 的 alignment structure）。40 pairs
      达到 95% 因为边际 minor components 需要更多 data 来稳定。Within [30, 50] range。

      Resource-tier stratification：HIGH languages 与 EN 的 activation distributions
      更相似（CKA > 0.70 at probing layers），rotation matrix 的 effective rank 更低
      → 22 pairs 即可。LOW languages 需要估计更 complex rotation → 48 pairs。

      LOW-resource delta +8.2pp (within [5, 12] range)：LOW languages 的 ZS baseline
      最差（0.57-0.67），有最大改善空间。Procrustes 对 misaligned correctness directions
      的纠正效果与 misalignment degree 成正比。

      Procrustes reversal at threshold ZS=0.52：当 ZS AUROC < 0.52，correctness
      directions 严重 misaligned，Procrustes 提供 +4.2pp。当 ZS > 0.60，directions
      已 well-aligned，Procrustes 引入 estimation noise → -1.0pp。Threshold 0.52
      对应 CKA ~0.35（plan_011 cliff threshold）——geometric consistency。
    tables:
      - name: "Table 16: Projection Sample Efficiency (3-arch pooled)"
        columns: [n_pairs, pct_of_200, mean_auroc, std_across_seeds]
        rows:
          - [10, 70, 0.776, 0.012]
          - [20, 84, 0.781, 0.007]
          - [30, 92, 0.785, 0.004]
          - [50, 97, 0.789, 0.003]
          - [100, 99, 0.790, 0.002]
          - [200, 100, 0.783, 0.001]
      - name: "Table 17: Saturation by Resource Tier"
        columns: [tier, pairs_to_90pct, pairs_to_95pct, interpretation]
        rows:
          - [HIGH, 14, 22, "simple rotation, low effective rank"]
          - [MID, 22, 36, "moderate complexity"]
          - [LOW, 32, 48, "complex rotation, more data needed"]
      - name: "Table 18: Procrustes Effect Reversal"
        columns: [zs_auroc_range, n_pairs_in_range, mean_delta_pp, direction]
        rows:
          - ["<0.50", 38, 5.8, "strong positive"]
          - ["0.50-0.52", 22, 2.6, "moderate positive"]
          - ["0.52-0.58", 45, 0.4, "near-zero (transition)"]
          - ["0.58-0.68", 95, -0.6, "slight negative"]
          - [">0.68", 100, -1.0, "negative — hurts"]
    figures_description:
      - >
        Figure 10a: Sample efficiency curves — normalized performance (y) vs n_pairs (x).
        Three curves for HIGH/MID/LOW, showing staggered saturation. All converge by 100.
      - >
        Figure 10b: Procrustes reversal — delta AUROC (y) vs ZS baseline (x). Clear
        sign change at ~0.52. Points colored by resource tier. Vertical dashed line
        at threshold.
    analysis: >
      ~40 pairs to 95% 是 directly actionable：<50 parallel sentences per language 即可
      达到接近 full-scale alignment。Resource-tier stratification 提供 per-language
      guidance。LOW-resource delta +8.2pp（in [5, 12] range）。Procrustes reversal
      at 0.52 与 CKA threshold 0.35 形成对应——geometric consistency across analyses。

  - name: "Probing Control Tasks — Full-Scale Cross-Lingual"
    plan_id: "plan_013"
    description: >
      扩展 MVP English-only control task analysis（已完成, selectivity L20-L27: 0.244-0.262）
      到 20 languages × 3 architectures。Train probes on randomly permuted labels,
      compute selectivity = real_AUROC - control_AUROC。定量 cross-lingual artifact rate。
      Selectivity threshold sensitivity at 0.03/0.05/0.10。
    expected_results:
      en_selectivity_deep_layers_range: [0.24, 0.32]
      cross_lingual_selectivity_by_tier:
        HIGH_mean: 0.24
        MID_mean: 0.19
        LOW_mean: 0.10
      artifact_rate_overall_pct: 10
      artifact_rate_by_tier:
        HIGH_pct: 3
        MID_pct: 6
        LOW_pct: 28
      artifact_concentration: "LOW-resource × >60% depth"
      control_auroc_mean_all: 0.494
      control_auroc_std: 0.009
      selectivity_threshold_sensitivity:
        threshold_003: {artifact_rate_pct: 15}
        threshold_005: {artifact_rate_pct: 10}
        threshold_010: {artifact_rate_pct: 6}
      langs_with_any_meaningful_selectivity_gt005: 17
    result_rationale: >
      MVP English data（selectivity L27=0.262, within [0.2, 0.35] range）确立了 baseline。
      Full-scale scaling：更大模型（235B/17B×16E/31B）有更强 correctness signal →
      EN selectivity 提升至 0.24-0.32 range。

      Cross-lingual artifact rate 10% (within [5, 15] range)。Resource-tier 分层明显：
      LOW languages 28% artifact rate 源于：(1) pretraining 中占比极低 → activation
      distributions 缺乏 structured correctness signal → linear probes 通过 capacity
      拟合 noise；(2) GlobalMMLU 的 LOW-resource translations 质量较低 → correctness
      labels 本身有 noise。HIGH/MID 的 3-6% artifact rate 表明核心 Pareto/CKA 分析
      （主要基于 HIGH/MID patterns）不受 artifact concerns 影响。

      Artifacts 集中在 LOW-resource × deep layers (>60% depth)，与 CKA cliff 一致：
      deep layers 的 low-resource CKA <0.20，cross-lingual activation structure 不足
      以支撑 genuine correctness probing。

      这是 field-level contribution：cross-lingual probing studies（包括 Xiao et al.）
      如果不做 selectivity checks 会高估 LOW-resource transfer quality。
    tables:
      - name: "Table 19: Cross-Lingual Selectivity by Tier and Depth"
        columns: [depth_band, HIGH_selectivity, MID_selectivity, LOW_selectivity]
        rows:
          - ["0-30%", 0.04, 0.03, 0.01]
          - ["30-60%", 0.20, 0.16, 0.07]
          - ["60-80%", 0.30, 0.24, 0.11]
          - ["80-100%", 0.28, 0.21, 0.08]
      - name: "Table 20: Artifact Rates by Tier (selectivity threshold = 0.05)"
        columns: [tier, n_lang_layer_arch_combinations, artifact_count, artifact_rate_pct]
        rows:
          - [HIGH, 1008, 30, 3]
          - [MID, 1152, 69, 6]
          - [LOW, 576, 161, 28]
          - [total, 2736, 260, 10]
    figures_description:
      - >
        Figure S1: Selectivity heatmap (3 panels, one per architecture). Language (y,
        ordered by tier) × normalized depth (x). Color = selectivity. LOW-resource rows
        at deep layers show gray (near-zero selectivity).
    analysis: >
      10% overall artifact rate (in [5, 15] range)。28% LOW-resource rate 是 methodological
      warning for the field。关键：artifacts 不影响核心分析（Pareto/CKA 主要基于 HIGH/MID），
      但 LOW-resource transfer claims 需要 selectivity-qualified caveats。

  - name: "Cross-Lingual Correctness-Confidence Orthogonality"
    plan_id: "plan_005"
    description: >
      Verbalized confidence direction + cosine similarity with correctness direction,
      20 languages × 3 architectures。Supporting evidence for Claim 4 (subsection)。
    expected_results:
      cosine_mean_overall: 0.048
      cosine_range: [0.02, 0.088]
      cosine_en: 0.032
      all_below_0p10: true
      by_tier:
        HIGH_mean: 0.036
        MID_mean: 0.050
        LOW_mean: 0.070
      by_arch:
        qwen3_mean: 0.044
        llama4_mean: 0.052
        gemma4_mean: 0.048
      resource_tier_spearman: -0.62
    result_rationale: >
      Miao & Ungar (2026) EN 7-8B: cosine < 0.04。Extension to 20 langs × 大模型
      保持 near-orthogonality（all < 0.10）因为 correctness 和 verbalized confidence
      是 architecturally decoupled：confidence 由 language modeling head 从 surface-level
      token probabilities 生成，correctness 由 intermediate representations geometry 编码。
      Low-resource 略高（0.070）因为 confidence elicitation 更 noisy + 更弱的 representation
      quality 使两个 directions 的 estimation 更不稳定。
    tables:
      - name: "Table 21: Orthogonality by Tier and Architecture"
        columns: [tier, qwen3, llama4, gemma4, combined]
        rows:
          - [HIGH, 0.033, 0.039, 0.036, 0.036]
          - [MID, 0.047, 0.054, 0.049, 0.050]
          - [LOW, 0.064, 0.078, 0.068, 0.070]
    figures_description:
      - >
        Figure S2: Cosine similarity violin plots by resource tier (3 columns for 3 archs).
        All distributions well below 0.10 threshold line. Slight upward shift for LOW tier.
    analysis: >
      Near-orthogonality universally holds (59/60 model-lang pairs < 0.10)。Confirms
      output-based calibration structurally limited across languages — motivates probe-based
      approach。Resource-tier gradient is novel but small effect (range only 0.034)。

  - name: "Probe Complexity Comparison"
    plan_id: "plan_006"
    description: >
      Logistic regression vs 2-layer MLP (hidden=128) at each probed layer, 3 models。
      Validates linear probe choice for cross-lingual transfer。
    expected_results:
      logreg_en_auroc_best: 0.835
      mlp_en_auroc_best: 0.855
      mlp_en_gain_pp: 2.0
      logreg_zs_drop_mean_pp: 5.2
      mlp_zs_drop_mean_pp: 10.8
      logreg_transfer_advantage_pp: 5.6
      logreg_advantage_at_deep_layers_pp: 8.5
      logreg_advantage_at_shallow_layers_pp: 1.8
    result_rationale: >
      Linear probes learn 单个 hyperplane，跨语言泛化因为 correctness subspace 是
      near-universal linear structure（subspace angle ~13°）。MLPs fit nonlinear decision
      boundaries that overfit EN-specific feature interactions：+2pp EN AUROC 但 -5.6pp
      transfer（net worse）。Gap 在 deep layers 放大（+8.5pp logreg advantage at >70%
      depth）因为 deep layers 有更多 language-specific nonlinear structure for MLP to exploit。
    tables:
      - name: "Table S2: Probe Complexity (Qwen3, EN-optimal layer, mean across 20 langs)"
        columns: [probe_type, en_auroc, zs_mean_20, zs_drop_pp]
        rows:
          - [logistic_regression, 0.835, 0.775, 6.0]
          - [mlp_2layer_h128, 0.855, 0.747, 10.8]
    figures_description:
      - >
        Figure S3: Transfer drop (pp, y-axis) vs depth (x-axis), logreg (blue, moderate
        slope) vs MLP (red, steep slope diverging past 60% depth).
    analysis: >
      Linear probes 为 cross-lingual transfer 的 optimal choice。MLP 的 nonlinear
      capacity captures EN-specific patterns → worse transfer。Justifies logreg as
      primary probe and supports geometric interpretation。

  - name: "Cross-Benchmark Generalization (Belebele + MMLU-ProX)"
    plan_id: "plan_007"
    description: >
      Evaluate best probes + CaCLR on Belebele (reading comprehension) and MMLU-ProX
      (harder factual), 20 languages each × 3 models。
    expected_results:
      belebele_zs_mean_20: 0.748
      belebele_caclr_mean_20: 0.780
      belebele_caclr_delta_pp: 3.2
      mmlupx_zs_mean_20: 0.735
      mmlupx_caclr_mean_20: 0.770
      mmlupx_caclr_delta_pp: 3.5
      cross_benchmark_caclr_cv: 0.04
      pareto_frontier_replicates_both_benchmarks: true
    result_rationale: >
      Belebele (reading comprehension) 和 MMLU-ProX (harder factual) 的 baselines
      不同于 GlobalMMLU 因为 domain shift 和 task format differences。但 CaCLR 的
      improvement 幅度 consistent（3.2-3.5pp vs GlobalMMLU 的 3.3pp）。Low CV (0.04)
      证实 CaCLR addresses fundamental representation alignment issue 而非 overfitting
      to specific benchmark。Pareto frontier structure (positive depth trend + local
      deep tradeoff) replicates on both benchmarks — phenomenon is not benchmark-specific。
    tables:
      - name: "Table 22: Cross-Benchmark CaCLR Generalization"
        columns: [benchmark, zs_mean_20, caclr_mean_20, delta_pp]
        rows:
          - [GlobalMMLU, 0.767, 0.800, 3.3]
          - [Belebele, 0.748, 0.780, 3.2]
          - [MMLU-ProX, 0.735, 0.770, 3.5]
    figures_description:
      - >
        Figure S4: CaCLR delta (y) vs ZS baseline (x) across 3 benchmarks × 20 languages.
        Points from different benchmarks intermixed — same linear relationship, confirming
        benchmark-agnostic mechanism.
    analysis: >
      Cross-benchmark consistency 是最强 defense against overfitting。CaCLR improvement
      cv=0.04 across benchmarks 证实方法的 generality。

  - name: "Quantization Validation Ablation"
    plan_id: "plan_010"
    description: >
      (a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4
      vs FP16 for Qwen3-235B at 5 layers, 5% subset; (c) BF16 Gemma4 serves as
      unquantized reference (no ablation needed)。
    expected_results:
      llama4_w4a16_fp16_auroc_diff_mean_pp: 0.3
      llama4_w4a16_fp16_auroc_diff_max_pp: 0.7
      llama4_rank_correlation: 0.997
      qwen3_int4_fp16_auroc_diff_mean_pp: 0.5
      qwen3_int4_fp16_auroc_diff_max_pp: 1.2
      qwen3_rank_correlation: 0.995
      cka_distortion_max: 0.02
    result_rationale: >
      W4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation geometry
      影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness
      direction 的 angular structure robust（0.5pp mean diff）——quantization noise
      近似 isotropic，不 preferentially distort correctness-relevant directions。
      Rank correlation > 0.995 确认 Pareto frontier ordering 完全保留。
      CKA distortion < 0.02 证实 CKA analysis 不被量化 artifacts 污染。
      Gemma4 的 BF16 提供 ground-truth 无量化 reference。
    tables:
      - name: "Table S3: Quantization Comparison (representative layers)"
        columns: [model, layer, fp16_auroc, quant_auroc, diff_pp]
        rows:
          - [Llama4, 8, 0.642, 0.639, 0.3]
          - [Llama4, 20, 0.770, 0.768, 0.2]
          - [Llama4, 32, 0.810, 0.807, 0.3]
          - [Llama4, 40, 0.812, 0.808, 0.4]
          - [Llama4, 47, 0.780, 0.776, 0.4]
          - [Qwen3, 20, 0.712, 0.708, 0.4]
          - [Qwen3, 36, 0.787, 0.782, 0.5]
          - [Qwen3, 52, 0.824, 0.818, 0.6]
          - [Qwen3, 68, 0.837, 0.835, 0.2]
          - [Qwen3, 84, 0.817, 0.810, 0.7]
    figures_description:
      - >
        Figure S5: Quantized vs FP16 AUROC scatter. Both models tight along y=x diagonal.
    analysis: >
      Quantization safe for both models。Preempts reviewer concern #5。Gemma4 BF16
      provides unquantized cross-validation anchor。

  - name: "Extended Language Coverage (Camera-Ready)"
    plan_id: "plan_009"
    description: >
      Expand from 20 to 50+ languages for camera-ready using GlobalMMLU/Belebele
      full language sets。3 models × all probed layers。
    expected_results:
      total_languages: 52
      zs_pass_rate_52lang: 0.83
      zs_auroc_above_060_count: 43
      caclr_improvement_positive_count: 48
      mean_zs_auroc_52lang: 0.735
      mean_caclr_auroc_52lang: 0.768
      new_families_covered: [Austronesian, Dravidian, Uralic, Kartvelian, Niger-Congo_B]
      pareto_frontier_holds_all_52: true
      simpson_paradox_holds_all_52: true
      tier_summary:
        HIGH_10_langs: {zs_mean: 0.80, caclr_mean: 0.82, delta_pp: 2.5}
        MID_24_langs: {zs_mean: 0.76, caclr_mean: 0.79, delta_pp: 3.2}
        LOW_14_langs: {zs_mean: 0.67, caclr_mean: 0.72, delta_pp: 4.8}
        VERY_LOW_4_langs: {zs_mean: 0.56, caclr_mean: 0.62, delta_pp: 5.8}
    result_rationale: >
      Expansion 主要增加 MID-resource 语言（Indonesian, Finnish, Georgian, Tamil, etc.），
      大多 fall in 0.65-0.78 AUROC range。Extremely low-resource（Amharic, Khmer, Lao,
      Hausa）的 AUROC < 0.58 但代表 edge cases。CaCLR 在 92% (48/52) 的语言上 positive
      因为 consistency loss mechanism 是 language-agnostic。Pareto frontier 和 Simpson's
      Paradox structure 在 52 languages 上完全保持——增强 universality claim 从 n=20 到 n=52。
      VERY_LOW tier (4 langs) 展示 ceiling：pretraining 不足的语言即使有 CaCLR 也
      limited by representation quality 本身。CaCLR benefit 与 resource level 反相关
      (r=-0.65, HIGH +2.5pp vs VERY_LOW +5.8pp)。
    tables:
      - name: "Table 23: Extended Coverage Summary by Tier"
        columns: [tier, n_langs, zs_mean, caclr_mean, caclr_delta_pp]
        rows:
          - [HIGH, 10, 0.80, 0.82, 2.5]
          - [MID, 24, 0.76, 0.79, 3.2]
          - [LOW, 14, 0.67, 0.72, 4.8]
          - [VERY_LOW, 4, 0.56, 0.62, 5.8]
    figures_description:
      - >
        Figure 10: World map with per-language CaCLR AUROC as color fill. Broad geographic
        and typological coverage. European/East Asian warm, Sub-Saharan/South Asian cool
        but still above chance.
    analysis: >
      52-language extension 确认 all findings at scale。Resource-tier gradient smooth,
      CaCLR benefit inversely correlated with resource level。No language family shows
      anomalous behavior — phenomenon is truly universal across typological diversity。
```

所有 key metrics 检查通过：

| Metric | Predicted | Range | Status |
|---|---|---|---|
| en_auroc mean 3 arch | 0.818 | [0.80, 0.86] | ✓ |
| zs_pass_rate /20 | 17-19 | [16, 20] | ✓ |
| mean_zs_drop pp | 5.2 | [4, 8] | ✓ |
| pareto_prevalence | 62% | [0.5, 0.75] | ✓ |
| pareto_drop pp | 2.5-3.8 | [2.0, 6.0] | ✓ |
| cka_partial_rho | 0.41-0.48 | [0.3, 0.55] | ✓ |
| cka_partial_p | 0.002-0.007 | [0.0001, 0.01] | ✓ |
| simpson 3/3 | 3 | [3, 3] | ✓ |
| caclr_delta pp | 3.3 | [2.0, 5.0] | ✓ |
| caclr_langs_improved | 14 | [10, 16] | ✓ |
| linproj_low_resource pp | 8.2 | [5, 12] | ✓ |
| linproj_saturation | 40 | [30, 50] | ✓ |
| decomp_improvement pp | 4.5 | [3, 6] | ✓ |
| decomp_clean_sep /10 | 8 | [7, 10] | ✓ |
| selectivity_deep | 0.24-0.32 | [0.2, 0.35] | ✓ |
| artifact_rate % | 10 | [5, 15] | ✓ |
| spearman_positive /20 | 17-19 | [16, 20] | ✓ |

与前一版 dream 的主要修正：(1) Spearman rho (depth vs ZS AUROC) 符号修正为正（deeper generally improves transfer），local Pareto tradeoff 是深层局部现象；(2) 加入 Gemma4 作为 P0 第三架构；(3) CaCLR 正面结果扩展了 high-dim MMD 和 CORAL 对比；(4) 所有 partial correlation bootstrap CIs 不含零。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e854bde-c705-4718-8787-2772de1c1bf9",
  "isSidechain": false,
  "requestId": "req_011CbFigAKVDXoZBc5NRm2wR",
  "type": "assistant",
  "uuid": "de6966ff-0cd2-4ebf-9e4b-d2f5d3f034f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxoZP67NU4rSxKZRRupWxJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31457,
      "cache_read_input_tokens": 93088,
      "output_tokens": 27247,
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
          "output_tokens": 27247,
          "cache_read_input_tokens": 93088,
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Full-scale models (235B MoE + Scout MoE + Gemma Dense) replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement;…",
  "leafUuid": "de6966ff-0cd2-4ebf-9e4b-d2f5d3f034f4",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe transfer and CaCLR calibration",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Full-scale models (235B MoE + Scout MoE + Gemma Dense) replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement;…",
  "leafUuid": "de6966ff-0cd2-4ebf-9e4b-d2f5d3f034f4",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe transfer and CaCLR calibration",
  "sessionId": "f5eee182-64f0-49d7-8928-961587304e5d"
}
```

---
