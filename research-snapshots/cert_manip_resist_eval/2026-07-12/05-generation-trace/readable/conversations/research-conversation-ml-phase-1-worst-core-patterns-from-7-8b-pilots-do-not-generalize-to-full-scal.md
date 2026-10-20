# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Core patterns from 7-8B pilots do not generalize to full-scale models; Pare

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/62ec8314-8921-4b1d-97d5-5290795266c5.jsonl`
- **Structured JSON:** [`49272decaca84fdb8262.json`](../../sessions/49/49272decaca84fdb8262.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T13:18:32.853Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T13:18:32.853Z",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Core patterns from 7-8B pilots do not generalize to full-scale models; Pareto frontier is absent or trivial; CKA adds no explanatory power beyond depth; CaCLR fails; must reframe around surviving findings\n核心假设：['Larger models have different internal geometry: either zero-shot transfer is already strong enough (>0.70 for most langs → no problem to solve) OR representations diverge so much that probing fails broadly', 'Pareto frontier disappears at scale — deeper layers help transfer monotonically (no tradeoff) or transfer is uniformly poor regardless of depth', \"CKA partial correlation controlling for depth is non-significant for ≥2/3 architectures → CKA provides no explanatory power beyond 'deeper = more specialized'\", \"Simpson's Paradox does not replicate at 20-language scale (driven by between-language variance at n=5, not a real structural effect)\", 'CaCLR fails; linear projection helps inconsistently (architecture-dependent, no clear threshold for when to apply)', 'Decomposition shows no clean separation — difficulty and capability are entangled at all layers']\n关键指标范围：{'en_auroc_best_layer_mean_across_arch': [0.72, 0.78], 'zs_transfer_pass_rate_auroc_gt_058_of_20': [8, 13], 'mean_zs_auroc_drop_vs_en_pp': [12, 20], 'pareto_tradeoff_prevalence_frac_lang_arch_pairs': [0.05, 0.25], 'pareto_depth_transfer_drop_at_final_layers_pp': [0.0, 1.5], 'cka_partial_corr_rho_controlling_depth': [-0.05, 0.18], 'cka_partial_corr_p_value': [0.05, 0.5], 'simpson_paradox_confirmed_of_3_arch': [0, 1], 'caclr_delta_over_zeroshot_mean_pp': [-1.5, 0.5], 'caclr_langs_improved_of_20': [2, 7], 'linear_proj_delta_over_zs_low_resource_pp': [1, 4], 'linear_proj_saturation_pairs': [80, 200], 'decomposition_transfer_improvement_after_difficulty_projection_pp': [-1, 1.5], 'decomposition_langs_showing_clean_separation_of_10': [1, 4], 'control_task_selectivity_deep_layers': [0.1, 0.2], 'cross_lingual_artifact_rate_pct': [25, 45], 'spearman_depth_vs_transfer_rho_positive_langs_of_20': [8, 13]}\n叙事方向：Reframe as large-scale field-level viability test with strong negative conclusions. Drop Claim 2 (decomposition) and Claim 3 (CaCLR method) as standalone claims. New angle: 'We conducted the first large-scale study testing whether English-trained correctness probes transfer cross-lingually across 3 architectures × 20 languages. Core finding: probe transfer is fundamentally limited by architecture-specific representation geometry that existing alignment methods (mean-shift, MMD, CORAL, linear projection) cannot reliably overcome. Control task analysis reveals that a substantial fraction of apparent shallow-layer transfer is capacity artifact, not genuine correctness signal.' Elevate the control task warning to a primary contribution (field-level methodological finding: all cross-lingual probing studies must include selectivity checks). Elevate the mean-shift impossibility proof (rank-invariance under StandardScaler + LR) as a clean theoretical contribution that clarifies confusion in the literature (Xiao et al.). Resource-tier analysis survives as descriptive empirical contribution. Linear projection's inconsistency itself is a finding — 'geometric alignment helps iff baseline representations are moderately aligned (0.50-0.60 AUROC), but the prediction of when this holds requires language-specific validation, undermining the zero-label promise.' Still targets EACL: negative results with scale (3 architectures × 20 langs), methodological contributions (control tasks, mean-shift proof), and constructive path-forward (few-shot 25-100 labels is the minimum viable approach).\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions\n- Camera-ready extension: 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as \"principled scope\" not \"design limitation.\"\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method.\" Note: linear projection is \"the only label-free method that consistently improves over zero-shot across resource tiers\" — NOT \"only viable path.\" Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive. CORAL COMPARISON\n    (D015, re-dream 2-tier consensus): Add CORAL loss (second-order alignment, Sun\n    & Saenko 2016) as alternative to MMD. Tests whether distributional matching failure\n    is MMD-specific or general. Trivial to implement on cached activations. Report\n    CORAL alongside MMD in Table 7 ablation. Strengthens negative result scope. HIGH-DIM\n    MMD (D016, dream #4 cross-tier consensus): All 3 tiers flagged \"1-D logit MMD\"\n    as overclaimed scope. Test MMD on PCA-reduced activations (d=50, d=100) instead\n    of 1-D probe logits. If high-dim also fails → broadens \"distributional matching\n    fails\" claim. If high-dim works → method contribution jumps significantly. Trivial:\n    PCA on cached activations, then MMD in reduced space. Also test with CORAL in\n    high-dim. MULTI-SEED (D016): Run 3-5 seeds for CaCLR, few-shot (25/100), and Procrustes\n    at representative layers. Report std across seeds. Addresses single-seed concern.\n    MIXED β CRITERION (D016): Add 1-2 validation languages (zh, sw) to β selection\n    criterion alongside English, to rule out systematic bias against cross-lingual\n    benefit.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  registry_id: plan_013\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique. SELECTIVITY THRESHOLD\n    SENSITIVITY (D015): Test at 0.03, 0.05, 0.10 thresholds (Hewitt & Liang used 0.05\n    for English syntactic probing; may not be appropriate for multilingual correctness).\n    Report artifact rate at each threshold. Trivial to compute from existing data\n    (plan_013 v2 already running).\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 32.7B Dense (60 text layers, dense, BF16): third architecture\n    for core submission. Full Pareto frontier at every 4th layer + final (16 probed\n    layers), 20 languages, 5 transfer conditions. BF16 (~62.5GB, fits single 96GB\n    GPU). Provides dense vs MoE architectural contrast — addresses #1 reviewer concern\n    across ALL dream tiers (\"architecture comparison confounded\").\n\n    '\n  priority: P0\n  gpu_budget_hours: 30\n  deps: []\n  notes: 'Upgraded P2→P0 (D016). User providing 4× RTX 6000 96G on second server.\n    Model: google/gemma-4-31B (HF) / ModelScope. Apache 2.0, no gating. MULTIMODAL:\n    has vision encoder (27 extra layers) — extract_activations.py must hook ONLY text\n    decoder layers (60 layers), skip vision. Code may need adjustment. BF16 ~62.5GB\n    (2 shards: 49.8 + 12.8GB), single 96GB GPU sufficient. No quantization needed\n    — eliminates quantization confound for this model.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- exp_id: plan_013_probing_controls_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002_4gpu\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan_002_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T13:18:32.857Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T13:18:32.857Z",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-21T13:18:32.876Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Core patterns from 7-8B pilots do not generalize to full-scale models; Pareto frontier is absent or trivial; CKA adds no explanatory power beyond depth; CaCLR fails; must reframe around surviving findings
核心假设：['Larger models have different internal geometry: either zero-shot transfer is already strong enough (>0.70 for most langs → no problem to solve) OR representations diverge so much that probing fails broadly', 'Pareto frontier disappears at scale — deeper layers help transfer monotonically (no tradeoff) or transfer is uniformly poor regardless of depth', "CKA partial correlation controlling for depth is non-significant for ≥2/3 architectures → CKA provides no explanatory power beyond 'deeper = more specialized'", "Simpson's Paradox does not replicate at 20-language scale (driven by between-language variance at n=5, not a real structural effect)", 'CaCLR fails; linear projection helps inconsistently (architecture-dependent, no clear threshold for when to apply)', 'Decomposition shows no clean separation — difficulty and capability are entangled at all layers']
关键指标范围：{'en_auroc_best_layer_mean_across_arch': [0.72, 0.78], 'zs_transfer_pass_rate_auroc_gt_058_of_20': [8, 13], 'mean_zs_auroc_drop_vs_en_pp': [12, 20], 'pareto_tradeoff_prevalence_frac_lang_arch_pairs': [0.05, 0.25], 'pareto_depth_transfer_drop_at_final_layers_pp': [0.0, 1.5], 'cka_partial_corr_rho_controlling_depth': [-0.05, 0.18], 'cka_partial_corr_p_value': [0.05, 0.5], 'simpson_paradox_confirmed_of_3_arch': [0, 1], 'caclr_delta_over_zeroshot_mean_pp': [-1.5, 0.5], 'caclr_langs_improved_of_20': [2, 7], 'linear_proj_delta_over_zs_low_resource_pp': [1, 4], 'linear_proj_saturation_pairs': [80, 200], 'decomposition_transfer_improvement_after_difficulty_projection_pp': [-1, 1.5], 'decomposition_langs_showing_clean_separation_of_10': [1, 4], 'control_task_selectivity_deep_layers': [0.1, 0.2], 'cross_lingual_artifact_rate_pct': [25, 45], 'spearman_depth_vs_transfer_rho_positive_langs_of_20': [8, 13]}
叙事方向：Reframe as large-scale field-level viability test with strong negative conclusions. Drop Claim 2 (decomposition) and Claim 3 (CaCLR method) as standalone claims. New angle: 'We conducted the first large-scale study testing whether English-trained correctness probes transfer cross-lingually across 3 architectures × 20 languages. Core finding: probe transfer is fundamentally limited by architecture-specific representation geometry that existing alignment methods (mean-shift, MMD, CORAL, linear projection) cannot reliably overcome. Control task analysis reveals that a substantial fraction of apparent shallow-layer transfer is capacity artifact, not genuine correctness signal.' Elevate the control task warning to a primary contribution (field-level methodological finding: all cross-lingual probing studies must include selectivity checks). Elevate the mean-shift impossibility proof (rank-invariance under StandardScaler + LR) as a clean theoretical contribution that clarifies confusion in the literature (Xiao et al.). Resource-tier analysis survives as descriptive empirical contribution. Linear projection's inconsistency itself is a finding — 'geometric alignment helps iff baseline representations are moderately aligned (0.50-0.60 AUROC), but the prediction of when this holds requires language-specific validation, undermining the zero-label promise.' Still targets EACL: negative results with scale (3 architectures × 20 langs), methodological contributions (control tasks, mean-shift proof), and constructive path-forward (few-shot 25-100 labels is the minimum viable approach).

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
  "promptId": "b640863f-263b-4e66-ad8a-d5dc1b38729c",
  "type": "user",
  "uuid": "9953e443-ac0f-47a5-a983-091b88a1eadd",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T13:18:32.875Z_

```json
{
  "parentUuid": "9953e443-ac0f-47a5-a983-091b88a1eadd",
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
  "uuid": "857d318c-b893-4319-8d5a-76f9e2beb963",
  "timestamp": "2026-05-21T13:18:32.875Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T13:18:32.875Z_

```json
{
  "parentUuid": "857d318c-b893-4319-8d5a-76f9e2beb963",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f309bc1f-7fba-4729-a905-fc23c5d05c21",
  "timestamp": "2026-05-21T13:18:32.875Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core patterns from 7-8B pilots do not generalize to full-scale models; Pareto frontier is absent or trivial; CKA adds no explanatory power beyond depth; C…",
  "leafUuid": "f309bc1f-7fba-4729-a905-fc23c5d05c21",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Large-scale cross-lingual correctness probe transfer: worst-case scenario analysis",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5"
}
```

---

### Assistant

_source line 8 · 2026-05-21T13:18:58.545Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for the "worst" tier scenario for each planned experiment in the experiment_plan. I need to carefully go through each planned experiment and generate expected results consistent with the worst-tier definition.

Let me review the worst tier definition:
- Core patterns from 7-8B pilots do NOT generalize to full-scale models
- Pareto frontier is absent or trivial
- CKA adds no explanatory power beyond depth
- CaCLR fails
- Must reframe around surviving findings

Key metric ranges for worst:
- en_auroc_best_layer_mean_across_arch: [0.72, 0.78]


- zs_transfer_pass_rate_auroc_gt_058_of_20: [8, 13]
- mean_zs_auroc_drop_vs_en_pp: [12, 20]
- pareto_tradeoff_prevalence_frac_lang_arch_pairs: [0.05, 0.25]
- pareto_depth_transfer_drop_at_final_layers_pp: [0.0, 1.5]
- cka_partial_corr_rho_controlling_depth: [-0.05, 0.18]

Now I'm looking at the remaining metric ranges to complete the worst-case scenario specification, including the p-value thresholds for CKA partial correlations and any other statistical measures that would indicate weak or insignificant relationships. Looking at the performance ranges for these metrics, then I'm mapping out the experimental plan across twelve key studies—starting with the full Pareto frontier evaluations for Qwen3 and Llama 4, moving through the CaCLR implementation and difficulty-controlled ablations, and continuing with cross-lingual analysis, probe comparisons, and validation across different model architectures and quantization approaches.

Now I need to review the existing results to understand what context I'm working with before constructing the predictions for each experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f309bc1f-7fba-4729-a905-fc23c5d05c21",
  "isSidechain": false,
  "requestId": "req_011CbFnCDPikyiX2ABigMGkY",
  "type": "assistant",
  "uuid": "d9be43b9-851b-4bfb-9db4-1326392d1598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEoPhaGyaPk8j5CEvNMGHQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19031,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1013,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1013,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19031
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

_source line 9 · 2026-05-21T13:18:58.763Z_

Let我先检查项目目录结构，确认是否有已有的 tier 数据文件可以参考格式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9be43b9-851b-4bfb-9db4-1326392d1598",
  "isSidechain": false,
  "requestId": "req_011CbFnCDPikyiX2ABigMGkY",
  "type": "assistant",
  "uuid": "6d6fcafd-8a74-496a-a987-22f53047d9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEoPhaGyaPk8j5CEvNMGHQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19031,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1013,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1013,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19031
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

_source line 10 · 2026-05-21T13:19:00.356Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011FCstuUoksfPXNSnmhhpGC`</summary>

```json
{
  "pattern": "**/*tier*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d6fcafd-8a74-496a-a987-22f53047d9cd",
  "isSidechain": false,
  "requestId": "req_011CbFnCDPikyiX2ABigMGkY",
  "type": "assistant",
  "uuid": "59ab6417-521e-44af-929d-1d4e1f2a411e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEoPhaGyaPk8j5CEvNMGHQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19031,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1013,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1013,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19031
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

_source line 11 · 2026-05-21T13:19:00.577Z_

<details><summary>↩ Tool result · `toolu_01Faz8MGbDZUHkqgTcd2vohL`</summary>

```text
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ff3971d-a5fb-4fc4-a2bf-3b3e47a99523",
  "isSidechain": false,
  "promptId": "b640863f-263b-4e66-ad8a-d5dc1b38729c",
  "type": "user",
  "uuid": "0c6bd8b3-020b-4366-9e50-37c605bed6c3",
  "toolUseResult": {
    "filenames": [
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/imagined_experiments.yaml"
    ],
    "durationMs": 12,
    "numFiles": 12,
    "truncated": false
  },
  "sourceToolAssistantUUID": "1ff3971d-a5fb-4fc4-a2bf-3b3e47a99523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T13:19:00.381Z_

<details><summary>↩ Tool result · `toolu_011FCstuUoksfPXNSnmhhpGC`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59ab6417-521e-44af-929d-1d4e1f2a411e",
  "isSidechain": false,
  "promptId": "b640863f-263b-4e66-ad8a-d5dc1b38729c",
  "type": "user",
  "uuid": "b3a9919f-808b-45be-b86b-b73aa16f4adc",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 16,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "59ab6417-521e-44af-929d-1d4e1f2a411e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T13:19:00.561Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Faz8MGbDZUHkqgTcd2vohL`</summary>

```json
{
  "pattern": "**/*imagined*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3a9919f-808b-45be-b86b-b73aa16f4adc",
  "isSidechain": false,
  "requestId": "req_011CbFnCDPikyiX2ABigMGkY",
  "type": "assistant",
  "uuid": "1ff3971d-a5fb-4fc4-a2bf-3b3e47a99523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEoPhaGyaPk8j5CEvNMGHQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19031,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1013,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1013,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19031
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

_source line 14 · 2026-05-21T13:19:03.390Z_

<details open><summary>🔧 Tool call — Read · `toolu_011M2GCyPAjozkEsjLZjpeML`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c6bd8b3-020b-4366-9e50-37c605bed6c3",
  "isSidechain": false,
  "requestId": "req_011CbFnEG51XAcSMfRL2CvTq",
  "type": "assistant",
  "uuid": "b39e96fb-c558-4442-95fc-4637614c5094",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3yKjHz4T9ZnsPpmpV1rK8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1483,
      "cache_read_input_tokens": 30872,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1483,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 30872,
          "cache_creation_input_tokens": 1483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1483
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

_source line 15 · 2026-05-21T13:19:03.695Z_

<details><summary>↩ Tool result · `toolu_011M2GCyPAjozkEsjLZjpeML`</summary>

```text
1	tier: worst
2	narrative_guidance: '原始几何洞见 framing 全面崩塌。Simpson''s Paradox 在 20 语言全量验证中双架构均不显著（Qwen
3	  partial rho=+0.11, p=0.31; Llama partial rho=+0.08, p=0.42）， CKA 在 depth 之外无额外解释力——5
4	  语言 pilot 结果被确认为 small-sample artifact。CaCLR 三个 OOM 的 β sweep 证实 consistency loss
5	  完全 inert，且几何子空间解释也不成立：correctness direction 的跨语言 persistence 远弱于预期，非 robust low-dimensional
6	  subspace。 Pareto frontier 噪声极大，20 语言中仅 2-3 个达到 per-language 显著性，non-monotonic 模式普遍存在。控制任务分析揭示问题远超预期——
7	  不仅低资源语言 artifact rate 达 42%，中资源语言也有 37% 层级组合出现 capacity artifacts，这对整个跨语言 probing
8	  文献构成方法论挑战。 Difficulty decomposition 完全无效，random-direction control 产生同量级效果。Linear
9	  projection 需要 120-180 pairs（非 50）， 且 Procrustes 效果反转阈值在语言间高度不一致，无法给出可靠的单一阈值。 新 framing
10	  路线：''The limits of cross-lingual calibration probe transfer — a large-scale negative
11	  result with methodological implications''。 三层贡献重构：(1) 控制任务发现是最强贡献——首次在 cross-lingual
12	  probing 场景系统性应用 selectivity 检验，>35% artifact rate 对整个领域有直接 implication；(2) 综合 negative
13	  result 同时关闭 distributional matching 和 geometric alignment 两条路径， 附完整 ablation 和 sweep
14	  数据；(3) 条件性实用指导——linear projection 作为唯一可行方案但需 100+ pairs， 按 resource-tier 和 baseline
15	  ZS quality 分层推荐。仍可发 EACL 作为 rigorous negative result + methodology paper。
16	
17	  '
18	imagined_experiments:
19	- name: Qwen3-235B Full Pareto Frontier
20	  plan_id: plan_001
21	  description: Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th),
22	    20 languages, 5 transfer conditions
23	  expected_results:
24	    en_best_auroc: 0.738
25	    en_best_layer: 72
26	    en_auroc_range:
27	    - 0.598
28	    - 0.738
29	    en_best_ece_raw: 0.203
30	    zs_pass_count: 12
31	    zs_pass_rate: 0.6
32	    zs_pass_langs:
33	    - zh
34	    - es
35	    - fr
36	    - de
37	    - ja
38	    - pt
39	    - it
40	    - ar
41	    - hi
42	    - ru
43	    - ko
44	    - vi
45	    zs_fail_langs:
46	    - tr
47	    - th
48	    - sw
49	    - bn
50	    - am
51	    - yo
52	    - te
53	    - my
54	    best_zs_auroc:
55	      zh: 0.672
56	      es: 0.681
57	      fr: 0.663
58	      de: 0.654
59	      ja: 0.582
60	      pt: 0.668
61	      it: 0.651
62	      ar: 0.603
63	      hi: 0.561
64	      ru: 0.624
65	      ko: 0.585
66	      tr: 0.541
67	      vi: 0.558
68	      th: 0.523
69	      sw: 0.512
70	      bn: 0.519
71	      am: 0.482
72	      yo: 0.471
73	      te: 0.498
74	      my: 0.463
75	    global_spearman_rho: -0.15
76	    global_spearman_p: 0.062
77	    per_lang_significant_negative_rho_count: 2
78	    per_lang_significant_positive_rho_count: 0
79	    per_lang_nonmonotonic_count: 14
80	    mean_shift_delta_auroc_all: 0.0
81	    linear_proj_200pair_mean_delta: 0.038
82	    fewshot_25_mean_delta: 0.022
83	    fewshot_100_mean_delta: 0.051
84	  result_rationale: 'EN best AUROC 落在 worst 范围 [0.7, 0.76] 内。MoE routing 导致层间 representation
85	    变异度增大， 每第 4 层采样可能跳过 expert routing 的关键切换点，引入额外噪声。INT4 量化对 correctness signal 有轻微衰减（plan_010
86	    将确认）。 ZS 60% pass rate 因为：(1) 235B 参数量提升了高/中资源语言的 representation quality，但 INT4
87	    折损部分增益； (2) MoE 的 expert specialization 可能导致不同语言路由到不同 expert 子集，correctness direction
88	    的跨语言一致性被 expert 分化削弱； (3) 低资源语言在预训练中 token 占比不足，加之 MoE 可能给它们分配较少 expert capacity。
89	    Global Pareto rho=-0.15 仅 marginally significant (p=0.062)：depth-transfer tradeoff
90	    在多数语言不显著， 因为 MoE 中 depth 不单调地映射到 representation specialization——expert routing
91	    在不同深度可以"重置"语言特异性。 14/20 语言呈现 non-monotonic 模式（U 形、倒 U 形、锯齿形），这是 MoE 特有的现象。 Mean-shift
92	    ΔAUROC ≡ 0 符合已证明的数学不变性。Linear projection 和 few-shot 有正增益但方差大。
93	
94	    '
95	  tables:
96	  - name: 'Table 1a: Qwen3-235B Per-Language Pareto Spearman ρ (Depth vs ZS-AUROC)'
97	    columns:
98	    - lang
99	    - resource_tier
100	    - best_zs_auroc
101	    - best_zs_layer
102	    - spearman_rho
103	    - p_value
104	    - pattern
105	    rows:
106	    - - zh
107	      - HIGH
108	      - 0.672
109	      - 60
110	      - -0.35
111	      - 0.093
112	      - weak negative
113	    - - es
114	      - HIGH
115	      - 0.681
116	      - 56
117	      - -0.28
118	      - 0.184
119	      - n.s.
120	    - - fr
121	      - HIGH
122	      - 0.663
123	      - 60
124	      - -0.31
125	      - 0.141
126	      - n.s.
127	    - - de
128	      - HIGH
129	      - 0.654
130	      - 56
131	      - -0.22
132	      - 0.3
133	      - n.s.
134	    - - ja
135	      - HIGH
136	      - 0.582
137	      - 48
138	      - 0.15
139	      - 0.483
140	      - non-monotonic U-shape
141	    - - pt
142	      - HIGH
143	      - 0.668
144	      - 60
145	      - -0.25
146	      - 0.238
147	      - n.s.
148	    - - it
149	      - HIGH
150	      - 0.651
151	      - 56
152	      - -0.19
153	      - 0.375
154	      - n.s.
155	    - - ar
156	      - MID
157	      - 0.603
158	      - 52
159	      - 0.08
160	      - 0.71
161	      - flat
162	    - - hi
163	      - MID
164	      - 0.561
165	      - 48
166	      - -0.42
167	      - 0.041
168	      - significant negative
169	    - - ru
170	      - MID
171	      - 0.624
172	      - 56
173	      - -0.18
174	      - 0.398
175	      - n.s.
176	    - - ko
177	      - MID
178	      - 0.585
179	      - 44
180	      - 0.22
181	      - 0.301
182	      - inverted — deeper helps
183	    - - tr
184	      - MID
185	      - 0.541
186	      - 44
187	      - -0.12
188	      - 0.576
189	      - n.s.
190	    - - vi
191	      - MID
192	      - 0.558
193	      - 48
194	      - 0.05
195	      - 0.815
196	      - flat
197	    - - th
198	      - MID
199	      - 0.523
200	      - 40
201	      - -0.08
202	      - 0.71
203	      - n.s.
204	    - - sw
205	      - LOW
206	      - 0.512
207	      - 36
208	      - -0.38
209	      - 0.067
210	      - marginal negative
211	    - - bn
212	      - LOW
213	      - 0.519
214	      - 40
215	      - -0.15
216	      - 0.485
217	      - n.s.
218	    - - am
219	      - LOW
220	      - 0.482
221	      - 32
222	      - 0.1
223	      - 0.641
224	      - non-monotonic
225	    - - yo
226	      - LOW
227	      - 0.471
228	      - 28
229	      - -0.05
230	      - 0.815
231	      - noisy flat
232	    - - te
233	      - LOW
234	      - 0.498
235	      - 36
236	      - -0.2
237	      - 0.348
238	      - n.s.
239	    - - my
240	      - LOW
241	      - 0.463
242	      - 28
243	      - 0.12
244	      - 0.576
245	      - non-monotonic
246	  - name: 'Table 1b: Qwen3-235B 5 Transfer Conditions Summary (mean across 20 langs)'
247	    columns:
248	    - condition
249	    - mean_auroc
250	    - std
251	    - delta_vs_zs
252	    - significant_improvement_count
253	    rows:
254	    - - zero-shot
255	      - 0.572
256	      - 0.072
257	      - 0.0
258	      - —
259	    - - mean-shift
260	      - 0.572
261	      - 0.072
262	      - 0.0
263	      - 0/20
264	    - - linear_proj_200
265	      - 0.61
266	      - 0.058
267	      - 0.038
268	      - 11/20
269	    - - fewshot_25
270	      - 0.594
271	      - 0.065
272	      - 0.022
273	      - 7/20
274	    - - fewshot_100
275	      - 0.623
276	      - 0.054
277	      - 0.051
278	      - 13/20
279	  figures_description:
280	  - 'Figure 1a: Scatter plot of EN AUROC vs best ZS AUROC per language across 24 layers
281	    for Qwen3-235B. Points colored by resource tier. Shows diffuse cloud rather than
282	    clean Pareto frontier. Non-monotonic trajectories for ja, ko, am, my highlighted
283	    with dashed lines. Annotation shows global rho=-0.15 (p=0.062).'
284	  - 'Figure 1b: Heatmap of ZS AUROC per language (y-axis) × probed layer (x-axis).
285	    Shows irregular patterns with MoE-specific layer-to-layer variance. No smooth
286	    gradient along depth axis.'
287	  analysis: 'Qwen3-235B 的 Pareto frontier 远不如 MVP (Qwen2.5-7B) 清晰。MoE 架构的 expert routing
288	    打破了 dense model 中 depth = specialization 的单调映射，导致 14/20 语言呈现 non-monotonic 模式。
289	    仅 hi 和 sw 达到 per-language 显著性，但方向相反的 ko (+0.22, n.s.) 和 ja (+0.15, n.s.) 表明 depth-transfer
290	    tradeoff 不是普遍现象。Global rho=-0.15 被 between-language 差异驱动而非 within-language depth
291	    效应。MVP 的 clear Pareto 可能是 dense 7B model 的特殊现象，不推广到大规模 MoE。 5 transfer conditions
292	    中 linear projection 和 few-shot 100 有中等改善，但 significant improvement 仅覆盖 55-65%
293	    的语言，且主要集中在高资源语言。
294	
295	    '
296	- name: Llama 4 Scout Full Pareto Frontier
297	  plan_id: plan_002
298	  description: Llama 4 Scout (48 layers, MoE, W4A16), 12 probed layers, 20 languages,
299	    5 transfer conditions
300	  expected_results:
301	    en_best_auroc: 0.715
302	    en_best_layer: 40
303	    en_auroc_range:
304	    - 0.612
305	    - 0.715
306	    en_best_ece_raw: 0.218
307	    zs_pass_count: 11
308	    zs_pass_rate: 0.55
309	    zs_pass_langs:
310	    - zh
311	    - es
312	    - fr
313	    - de
314	    - pt
315	    - it
316	    - ar
317	    - ru
318	    - ko
319	    - vi
320	    - ja
321	    zs_fail_langs:
322	    - hi
323	    - tr
324	    - th
325	    - sw
326	    - bn
327	    - am
328	    - yo
329	    - te
330	    - my
331	    best_zs_auroc:
332	      zh: 0.643
333	      es: 0.658
334	      fr: 0.641
335	      de: 0.632
336	      ja: 0.556
337	      pt: 0.645
338	      it: 0.628
339	      ar: 0.581
340	      hi: 0.542
341	      ru: 0.602
342	      ko: 0.571
343	      tr: 0.523
344	      vi: 0.555
345	      th: 0.508
346	      sw: 0.496
347	      bn: 0.505
348	      am: 0.468
349	      yo: 0.455
350	      te: 0.487
351	      my: 0.448
352	    global_spearman_rho: -0.08
353	    global_spearman_p: 0.218
354	    per_lang_significant_negative_rho_count: 0
355	    per_lang_significant_positive_rho_count: 0
356	    per_lang_nonmonotonic_count: 11
357	  result_rationale: 'Llama 4 Scout 的 EN AUROC 低于 Qwen3 因为模型有效参数量更小（17B active vs 22B
358	    active）。 W4A16 量化对 correctness signal 有轻微额外损耗。ZS pass rate 55% 处于 worst 范围低端。
359	    仅 12 probed layers 使 per-language Spearman 检验功效极低（n=12），无语言达到显著性。 MVP (Llama-3.1-8B)
360	    中观察到的 architecture-specific 弱 Pareto 在 Scout 上进一步恶化： Scout 是 MoE (16 experts)，与
361	    3.1-8B 的 dense 架构根本不同，expert routing 引入同样的 non-monotonic 行为。Global rho=-0.08 完全不显著——Llama
362	    架构系列的 depth-transfer tradeoff 不稳定。
363	
364	    '
365	  tables:
366	  - name: 'Table 2: Llama 4 Scout Per-Language Pareto Spearman ρ'
367	    columns:
368	    - lang
369	    - resource_tier
370	    - best_zs_auroc
371	    - spearman_rho
372	    - p_value
373	    rows:
374	    - - zh
375	      - HIGH
376	      - 0.643
377	      - -0.2
378	      - 0.533
379	    - - es
380	      - HIGH
381	      - 0.658
382	      - -0.15
383	      - 0.641
384	    - - fr
385	      - HIGH
386	      - 0.641
387	      - -0.25
388	      - 0.432
389	    - - de
390	      - HIGH
391	      - 0.632
392	      - -0.1
393	      - 0.758
394	    - - ja
395	      - HIGH
396	      - 0.556
397	      - 0.3
398	      - 0.343
399	    - - pt
400	      - HIGH
401	      - 0.645
402	      - -0.18
403	      - 0.576
404	    - - it
405	      - HIGH
406	      - 0.628
407	      - -0.08
408	      - 0.805
409	    - - ar
410	      - MID
411	      - 0.581
412	      - 0.25
413	      - 0.432
414	    - - hi
415	      - MID
416	      - 0.542
417	      - -0.35
418	      - 0.264
419	    - - ru
420	      - MID
421	      - 0.602
422	      - -0.05
423	      - 0.878
424	    - - ko
425	      - MID
426	      - 0.571
427	      - 0.4
428	      - 0.198
429	    - - tr
430	      - MID
431	      - 0.523
432	      - 0.1
433	      - 0.758
434	    - - vi
435	      - MID
436	      - 0.555
437	      - 0.15
438	      - 0.641
439	    - - th
440	      - MID
441	      - 0.508
442	      - -0.2
443	      - 0.533
444	    - - sw
445	      - LOW
446	      - 0.496
447	      - -0.28
448	      - 0.379
449	    - - bn
450	      - LOW
451	      - 0.505
452	      - -0.1
453	      - 0.758
454	    - - am
455	      - LOW
456	      - 0.468
457	      - 0.05
458	      - 0.878
459	    - - yo
460	      - LOW
461	      - 0.455
462	      - -0.15
463	      - 0.641
464	    - - te
465	      - LOW
466	      - 0.487
467	      - -0.08
468	      - 0.805
469	    - - my
470	      - LOW
471	      - 0.448
472	      - 0.18
473	      - 0.576
474	  figures_description:
475	  - 'Figure 2: Llama 4 Scout Pareto scatter, same format as Figure 1a. Cloud更加散乱，global
476	    rho=-0.08 (p=0.218)。Ko (+0.40) 和 ja (+0.30) 方向相反于预期。'
477	  analysis: 'Llama 4 Scout 确认 worst tier 预期：depth-transfer tradeoff 在 MoE 架构上完全不显著。
478	    与 Qwen3-235B 合并看，0 个架构在 p<0.05 水平展现清晰的 Pareto——pareto_spearman_rho_significant_archs=0。
479	    MVP 中 Qwen2.5-7B dense model 的 clear Pareto 是 dense architecture + small scale
480	    的特殊现象， 不推广到大规模 MoE。这对 Claim 1 是毁灭性的：无法声称存在普遍的 depth-transferability tradeoff。
481	
482	    '
483	- name: CaCLR Implementation and Comparative Evaluation
484	  plan_id: plan_003
485	  description: CaCLR (BCE + α·SB-ECE + β·MMD), β sweep 3 OOM, α sweep, component ablation,
486	    vs 4 baselines, 2 models × 20 langs
487	  expected_results:
488	    caclr_mean_delta_auroc_vs_zs_qwen: -0.008
489	    caclr_mean_delta_auroc_vs_zs_llama: -0.012
490	    caclr_mean_delta_auroc_combined: -0.01
491	    caclr_best_beta: none — all β values inert or harmful
492	    caclr_best_alpha: 0.1
493	    beta_sweep_results:
494	      beta_0.001:
495	        mean_delta_auroc: -0.003
496	        std: 0.018
497	      beta_0.01:
498	        mean_delta_auroc: -0.006
499	        std: 0.021
500	      beta_0.1:
501	        mean_delta_auroc: -0.011
502	        std: 0.025
503	      beta_1.0:
504	        mean_delta_auroc: -0.019
505	        std: 0.031
506	    alpha_sweep_results:
507	      alpha_0.01:
508	        mean_delta_auroc: -0.002
509	        mean_delta_ece: 0.008
510	      alpha_0.1:
511	        mean_delta_auroc: -0.005
512	        mean_delta_ece: 0.003
513	      alpha_1.0:
514	        mean_delta_auroc: -0.012
515	        mean_delta_ece: -0.002
516	      alpha_10.0:
517	        mean_delta_auroc: -0.028
518	        mean_delta_ece: -0.005
519	    component_ablation:
520	      bce_only:
521	        delta_vs_zs: -0.001
522	        note: retraining from scratch ~= standard LR
523	      bce_plus_sbece:
524	        delta_vs_zs: -0.007
525	        note: SB-ECE regularization hurts discrimination
526	      bce_plus_mmd:
527	        delta_vs_zs: -0.005
528	        note: MMD inert to slightly harmful
529	      full_caclr:
530	        delta_vs_zs: -0.01
531	        note: combined losses compound harm
532	    linear_proj_vs_caclr_delta: 0.048
533	    fewshot100_vs_caclr_delta: 0.061
534	    implementation_spec:
535	      mmd_kernel: Gaussian RBF, bandwidth=median heuristic
536	      optimizer: Adam, lr=1e-3, cosine schedule
537	      epochs: 50
538	      early_stopping: patience=10 on held-out BCE loss
539	      initialization: from standard LR solution
540	      batch_size: 256
541	      mmd_items: same items as BCE (probe_train split)
542	      parallel_set_size_range:
543	      - 612
544	      - 2847
545	  result_rationale: 'CaCLR 失败的根本原因：MMD 在 probe logits 空间操作，而 logits 是 1-D（线性 probe
546	    的单一输出）。 1-D MMD 只能 match 两个标量分布的 marginal，无法对齐 correctness direction 的方向性结构。 即使
547	    marginal logit 分布被 match，EN 和 target 的 conditional distributions P(logit|correct)
548	    vs P(logit|incorrect) 可能仍然不同——Zhao et al. (2019) 的理论预测得到验证。β 越大，MMD 约束越强， logits
549	    被拉向无区分性的 marginal match，discrimination 下降。α 高值时 SB-ECE 正则化 进一步牺牲 AUROC 以换取 calibration
550	    改善，但改善微小且不稳定。Component ablation 证实 每个额外 loss component 都是净负面的——base BCE（从 LR solution
551	    初始化再微调）已经接近 ZS 性能， 额外优化无正贡献。Linear projection 和 few-shot 都显著优于 CaCLR，因为它们直接利用
552	    target-language 信息（parallel pairs 或 labels）而非试图间接 match distributions。 CKA subspace
553	    解释（correctness direction 是 low-dimensional language-agnostic subspace） 不成立——如果该
554	    subspace 真的存在且 robust，MMD 应该至少能做到无害，但实际上有害， 说明 correctness signal 的跨语言结构比预期更 language-specific。
555	
556	    '
557	  tables:
558	  - name: 'Table 3a: CaCLR β Sweep (Qwen3-235B, fixed layer 50% depth, 20 langs mean)'
559	    columns:
560	    - beta
561	    - mean_auroc
562	    - delta_vs_zs
563	    - pct_langs_improved
564	    - pct_langs_harmed
565	    rows:
566	    - - 0.001
567	      - 0.57
568	      - -0.003
569	      - 30%
570	      - 45%
571	    - - 0.01
572	      - 0.567
573	      - -0.006
574	      - 25%
575	      - 55%
576	    - - 0.1
577	      - 0.562
578	      - -0.011
579	      - 15%
580	      - 65%
581	    - - 1.0
582	      - 0.554
583	      - -0.019
584	      - 10%
585	      - 80%
586	  - name: 'Table 3b: 5-Way Transfer Condition Comparison (both models × 20 langs,
587	      EN-optimal layer)'
588	    columns:
589	    - condition
590	    - mean_auroc
591	    - mean_ece
592	    - delta_auroc_vs_zs
593	    - win_rate_vs_zs
594	    rows:
595	    - - zero-shot
596	      - 0.568
597	      - 0.285
598	      - —
599	      - —
600	    - - mean-shift
601	      - 0.568
602	      - 0.291
603	      - 0.0
604	      - 0%
605	    - - CaCLR_best
606	      - 0.558
607	      - 0.278
608	      - -0.01
609	      - 18%
610	    - - linear_proj_200
611	      - 0.606
612	      - 0.248
613	      - 0.038
614	      - 72%
615	    - - fewshot_25
616	      - 0.59
617	      - 0.262
618	      - 0.022
619	      - 55%
620	    - - fewshot_100
621	      - 0.619
622	      - 0.235
623	      - 0.051
624	      - 78%
625	  - name: 'Table 3c: CaCLR Component Ablation'
626	    columns:
627	    - configuration
628	    - mean_auroc
629	    - delta_vs_zs
630	    - note
631	    rows:
632	    - - BCE only (re-init)
633	      - 0.567
634	      - -0.001
635	      - ≈ ZS baseline
636	    - - BCE + SB-ECE (α=0.1)
637	      - 0.561
638	      - -0.007
639	      - ECE gains tiny, AUROC drops
640	    - - BCE + MMD (β=0.01)
641	      - 0.563
642	      - -0.005
643	      - MMD inert/harmful
644	    - - Full CaCLR (α=0.1, β=0.01)
645	      - 0.558
646	      - -0.01
647	      - compound degradation
648	  figures_description:
649	  - 'Figure 3a: β sweep curve showing monotonic decrease in mean AUROC as β increases
650	    from 0.001 to 1.0. Shaded region = bootstrap 95% CI. All CIs include or fall below
651	    zero-shot baseline.'
652	  - 'Figure 3b: Per-language ΔAUROC (CaCLR vs ZS) bar chart at best β=0.001. Most
653	    bars negative; only 3-4 high-resource languages show marginal positive ΔAUROC
654	    within noise margin.'
655	  analysis: 'CaCLR 的 negative result 是 worst tier 的核心。β sweep 证实 consistency loss
656	    在所有 3 OOM 均为 inert 或 harmful—— 这不是超参选择问题而是方法论层面的失败。1-D MMD 的结构性限制（probe logit
657	    空间太低维）加上 conditional distribution mismatch（Zhao et al. 2019）导致 distributional
658	    matching 路径被彻底关闭。 与此同时，CKA subspace 解释也不成立（plan_011 将确认），所以"MMD 失败是因为它只 match
659	    marginal 而不 match subspace direction"这个 elegant 的解释也变成了 post-hoc rationalization——
660	    实际上 subspace 本身就不 robust。这是 worst tier 最痛苦的部分：不仅方法失败，解释也失败。 但作为 negative result，reproducibility
661	    标准高：完整的 implementation spec、β/α sweep、 component ablation 使社区可以独立验证，避免重复尝试 distributional
662	    matching 路径。
663	
664	    '
665	- name: Difficulty-Controlled Decomposition Ablation
666	  plan_id: plan_004
667	  description: IRT difficulty probes → project out → retrain correctness probes, 10
668	    langs × 8 layers × 2 models
669	  expected_results:
670	    decomp_capability_delta_auroc_mean: -0.003
671	    decomp_capability_delta_auroc_range:
672	    - -0.015
673	    - 0.008
674	    random_direction_control_delta_mean: -0.005
675	    random_direction_control_delta_range:
676	    - -0.018
677	    - 0.006
678	    difficulty_probe_r2: 0.31
679	    decomp_vs_random_paired_test_p: 0.42
680	    per_tier_delta:
681	      HIGH:
682	        mean_delta: -0.002
683	        significant_count: 0/4
684	      MID:
685	        mean_delta: -0.004
686	        significant_count: 0/3
687	      LOW:
688	        mean_delta: -0.003
689	        significant_count: 0/3
690	  result_rationale: 'Difficulty decomposition 在 worst tier 无实质效果。两个原因：(1) difficulty
691	    和 capability 信号在 representation 空间中高度纠缠——IRT difficulty direction 不是一个干净的、可投影去除的独立子空间，
692	    而是与 correctness signal 共享大量方差。投影去除 difficulty 后 correctness signal 也被部分损坏， 导致
693	    retrained probe 的 transfer 性能与原始相当甚至略差。(2) Random-direction control 产生 同量级的效果（mean
694	    delta -0.005 vs -0.003，paired test p=0.42），这意味着观察到的微小变化 主要来自 dimensionality reduction
695	    效应而非 difficulty-specific 投影。Difficulty probe 本身 R²=0.31（低于理想值），表明 IRT difficulty
696	    在 LLM representation 中的编码不够线性/集中， 使得 linear projection 无法有效捕获它。整个 decomposition
697	    framing 在经验层面被否定： transfer 的降解不能归因于 capability-specific component，或者说两个 component
698	    不可分。
699	
700	    '
701	  tables:
702	  - name: 'Table 4: Difficulty Decomposition Ablation (mean across 2 models)'
703	    columns:
704	    - lang
705	    - resource_tier
706	    - original_zs_auroc
707	    - after_projection_auroc
708	    - delta
709	    - random_control_delta
710	    - decomp_vs_random_p
711	    rows:
712	    - - zh
713	      - HIGH
714	      - 0.658
715	      - 0.655
716	      - -0.003
717	      - -0.006
718	      - 0.61
719	    - - es
720	      - HIGH
721	      - 0.67
722	      - 0.669
723	      - -0.001
724	      - -0.004
725	      - 0.52
726	    - - fr
727	      - HIGH
728	      - 0.652
729	      - 0.649
730	      - -0.003
731	      - -0.007
732	      - 0.38
733	    - - de
734	      - HIGH
735	      - 0.643
736	      - 0.642
737	      - -0.001
738	      - -0.003
739	      - 0.71
740	    - - hi
741	      - MID
742	      - 0.552
743	      - 0.547
744	      - -0.005
745	      - -0.008
746	      - 0.55
747	    - - ru
748	      - MID
749	      - 0.613
750	      - 0.61
751	      - -0.003
752	      - -0.005
753	      - 0.64
754	    - - ko
755	      - MID
756	      - 0.578
757	      - 0.572
758	      - -0.006
759	      - -0.004
760	      - 0.48
761	    - - tr
762	      - MID
763	      - 0.532
764	      - 0.53
765	      - -0.002
766	      - -0.006
767	      - 0.33
768	    - - sw
769	      - LOW
770	      - 0.504
771	      - 0.501
772	      - -0.003
773	      - -0.005
774	      - 0.58
775	    - - bn
776	      - LOW
777	      - 0.512
778	      - 0.504
779	      - -0.008
780	      - -0.007
781	      - 0.82
782	  figures_description:
783	  - 'Figure 4: Paired bar chart comparing delta AUROC after difficulty projection
784	    (blue) vs random-direction projection (gray) for each language. Error bars = bootstrap
785	    95% CI. All CIs overlap; no language shows meaningful separation between decomposition
786	    and random control.'
787	  analysis: 'Decomposition 的 null result 与 random-direction control 不可区分（p=0.42），表明投影效应来自
788	    dimensionality reduction 而非 difficulty-specific 信号去除。这从根本上否定了 Claim 2 的因果叙述——
789	    transfer degradation 不能分解为 difficulty-shared 和 capability-specific 两个可操作的 component。
790	    在 worst tier framing 中，这成为 negative result 的一部分：decomposition 是另一条被关闭的路径。
791	
792	    '
793	- name: Cross-Lingual Orthogonality Analysis
794	  plan_id: plan_005
795	  description: Correctness-confidence cosine similarity, 20 langs × 2 architectures,
796	    resource-tier 和 language family 分析
797	  expected_results:
798	    mean_cosine_high_resource: 0.038
799	    mean_cosine_mid_resource: 0.065
800	    mean_cosine_low_resource: 0.112
801	    std_cosine_low_resource: 0.082
802	    cosine_range_all:
803	    - 0.008
804	    - 0.198
805	    architecture_agreement_rate: 0.65
806	    outlier_langs:
807	    - am
808	    - yo
809	    - my
810	  result_rationale: 'Orthogonality 在高资源语言基本成立（cosine < 0.05），复现 Miao & Ungar (2026)
811	    的英文发现。 但低资源语言的 cosine similarity 显著升高且方差极大（mean=0.112, std=0.082），部分语言 （am=0.198,
812	    yo=0.165, my=0.142）接近打破 orthogonality 假设。这可能是因为低资源语言 的 correctness 和 confidence
813	    directions 都更 noisy（probe 本身 selectivity 低——见 plan_013）， 而非真正的非正交结构。Architecture
814	    一致性仅 65%：两个架构在 7/20 语言上对 orthogonality 程度 给出矛盾信号，削弱了"orthogonality is a universal
815	    property"的叙述。 作为 subsection（已从 standalone claim 降级），这些结果增加了复杂性但没有清晰的 takeaway。
816	
817	    '
818	  tables:
819	  - name: 'Table 5: Cross-Lingual Orthogonality (Cosine Similarity)'
820	    columns:
821	    - lang
822	    - tier
823	    - qwen3_cosine
824	    - llama4_cosine
825	    - agreement
826	    - note
827	    rows:
828	    - - zh
829	      - HIGH
830	      - 0.031
831	      - 0.028
832	      - ✓
833	      - ''
834	    - - es
835	      - HIGH
836	      - 0.025
837	      - 0.033
838	      - ✓
839	      - ''
840	    - - fr
841	      - HIGH
842	      - 0.029
843	      - 0.041
844	      - ✓
845	      - ''
846	    - - de
847	      - HIGH
848	      - 0.035
849	      - 0.038
850	      - ✓
851	      - ''
852	    - - ja
853	      - HIGH
854	      - 0.048
855	      - 0.052
856	      - ✓
857	      - ''
858	    - - pt
859	      - HIGH
860	      - 0.027
861	      - 0.035
862	      - ✓
863	      - ''
864	    - - it
865	      - HIGH
866	      - 0.033
867	      - 0.039
868	      - ✓
869	      - ''
870	    - - ar
871	      - MID
872	      - 0.042
873	      - 0.058
874	      - ✓
875	      - ''
876	    - - hi
877	      - MID
878	      - 0.055
879	      - 0.072
880	      - ✓
881	      - ''
882	    - - ru
883	      - MID
884	      - 0.038
885	      - 0.045
886	      - ✓
887	      - ''
888	    - - ko
889	      - MID
890	      - 0.061
891	      - 0.048
892	      - ✗
893	      - direction reversed
894	    - - tr
895	      - MID
896	      - 0.075
897	      - 0.068
898	      - ✓
899	      - ''
900	    - - vi
901	      - MID
902	      - 0.052
903	      - 0.082
904	      - ✗
905	      - magnitude mismatch
906	    - - th
907	      - MID
908	      - 0.088
909	      - 0.065
910	      - ✗
911	      - magnitude mismatch
912	    - - sw
913	      - LOW
914	      - 0.095
915	      - 0.108
916	      - ✓
917	      - elevated
918	    - - bn
919	      - LOW
920	      - 0.082
921	      - 0.118
922	      - ✗
923	      - ''
924	    - - am
925	      - LOW
926	      - 0.198
927	      - 0.152
928	      - ✓
929	      - near non-orthogonal
930	    - - yo
931	      - LOW
932	      - 0.165
933	      - 0.128
934	      - ✗
935	      - ''
936	    - - te
937	      - LOW
938	      - 0.105
939	      - 0.092
940	      - ✓
941	      - ''
942	    - - my
943	      - LOW
944	      - 0.142
945	      - 0.118
946	      - ✓
947	      - elevated
948	  figures_description:
949	  - 'Figure 5: Box plot of correctness-confidence cosine similarity by resource tier,
950	    faceted by architecture. LOW tier shows significantly higher median and wider
951	    spread than HIGH/MID. Dashed line at cosine=0.10 marks ''practical orthogonality
952	    threshold''.'
953	  analysis: 'Orthogonality 作为 subsection 贡献了一个 nuanced finding：该性质是 resource-tier
954	    dependent， 低资源语言中不可靠。但在 worst tier 下这个 finding 被 plan_013 的高 artifact rate 进一步削弱——
955	    低资源语言的高 cosine 可能反映 probe 本身的 capacity artifact 而非真正的非正交 representation 结构。 Section
956	    简化为："orthogonality generally holds but becomes unreliable for low-resource languages，
957	    where probe validity itself is questionable (Section X)." 贡献有限。
958	
959	    '
960	- name: Probe Complexity Comparison
961	  plan_id: plan_006
962	  description: Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer
963	    + calibration, 2 models × 20 langs
964	  expected_results:
965	    en_auroc_lr_mean: 0.726
966	    en_auroc_mlp_mean: 0.741
967	    mlp_en_advantage: 0.015
968	    zs_transfer_lr_mean_degradation: 0.152
969	    zs_transfer_mlp_mean_degradation: 0.191
970	    mlp_transfer_disadvantage: -0.039
971	    lr_better_for_transfer_pct: 0.7
972	    ece_lr_mean: 0.242
973	    ece_mlp_mean: 0.258
974	    selectivity_lr_mean: 0.218
975	    selectivity_mlp_mean: 0.235
976	  result_rationale: 'MLP 在 EN 上因更高 capacity 而有 +1.5pp AUROC 优势，但跨语言 transfer 时 degradation
977	    更大 （-19.1% vs -15.2%），符合"linear probes transfer better"假设。然而在 worst tier 下， 这个差异虽然方向正确但
978	    effect size 不大（Cohen''s d ≈ 0.3），且 70% 而非 90%+ 的语言 支持 LR > MLP for transfer，因为部分高资源语言中
979	    MLP 的额外 capacity 弥补了 transfer 损失。 此外 MLP 的 selectivity 仅比 LR 高 0.017，表明额外 capacity
980	    带来的 artifact 风险有限—— 这与 plan_013 的高 artifact rate 形成有趣对比（artifacts 主要来自语言本身而非 probe
981	    复杂度）。
982	
983	    '
984	  tables:
985	  - name: 'Table 6: Probe Complexity Comparison Summary'
986	    columns:
987	    - metric
988	    - logistic_regression
989	    - mlp_2layer
990	    - delta
991	    - p_value
992	    rows:
993	    - - EN AUROC (mean)
994	      - 0.726
995	      - 0.741
996	      - 0.015
997	      - 0.008
998	    - - ZS degradation (mean)
999	      - 15.2%
1000	      - 19.1%
1001	      - +3.9pp
1002	      - 0.023
1003	    - - ZS AUROC (mean)
1004	      - 0.616
1005	      - 0.6
1006	      - -0.016
1007	      - 0.041
1008	    - - EN ECE (mean)
1009	      - 0.242
1010	      - 0.258
1011	      - 0.016
1012	      - 0.065
1013	    - - Selectivity (mean)
1014	      - 0.218
1015	      - 0.235
1016	      - 0.017
1017	      - 0.112
1018	    - - LR better for transfer
1019	      - 70%
1020	      - 30%
1021	      - —
1022	      - —
1023	  figures_description:
1024	  - 'Figure S1 (appendix): Layer-wise EN AUROC for LR vs MLP showing MLP advantage
1025	    increases with depth. Paired with ZS AUROC showing LR advantage for transfer grows
1026	    at deep layers.'
1027	  analysis: 'LR vs MLP 比较方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下，
1028	    probe complexity 不是主要问题——语言-层级 capacity artifacts 才是。 结论：保持 LR 作为默认，MLP 结果放 appendix。
1029	
1030	    '
1031	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
1032	  plan_id: plan_007
1033	  description: Best probes + CaCLR on Belebele 和 MMLU-ProX, 20 languages each, generalization
1034	    test
1035	  expected_results:
1036	    belebele_zs_pass_rate: 0.5
1037	    belebele_mean_zs_auroc: 0.548
1038	    belebele_vs_globalmmlu_spearman_rho: 0.72
1039	    belebele_vs_globalmmlu_mean_auroc_delta: -0.024
1040	    mmlupx_zs_pass_rate: 0.55
1041	    mmlupx_mean_zs_auroc: 0.562
1042	    mmlupx_vs_globalmmlu_spearman_rho: 0.78
1043	    caclr_belebele_delta_vs_zs: -0.013
1044	    caclr_mmlupx_delta_vs_zs: -0.008
1045	    linear_proj_belebele_delta: 0.031
1046	    linear_proj_mmlupx_delta: 0.035
1047	  result_rationale: 'Belebele 的 reading comprehension 格式与 MCQA correctness probing
1048	    的 mismatch 导致更低的 pass rate。 MMLU-ProX 与 GlobalMMLU 更接近（同为知识 MCQA）所以 correlation
1049	    更高。CaCLR 在两个 benchmark 上 同样失败甚至更差——distribution mismatch 在 out-of-distribution
1050	    数据上放大。 Linear projection 仍有正增益但幅度小于 GlobalMMLU——cross-benchmark generalization
1051	    有衰减。 整体 pattern：在 worst tier 下 generalization 弱化了已经微弱的 positive findings， reinforcing
1052	    negative result narrative。Belebele 的低 pass rate 尤其令人担忧—— correctness probe 的概念可能不
1053	    generalize beyond MCQA knowledge questions。
1054	
1055	    '
1056	  tables:
1057	  - name: 'Table 7: Cross-Benchmark Generalization'
1058	    columns:
1059	    - benchmark
1060	    - zs_pass_rate
1061	    - mean_zs_auroc
1062	    - caclr_delta
1063	    - linproj_delta
1064	    - correlation_with_globalmmlu
1065	    rows:
1066	    - - GlobalMMLU
1067	      - 0.575
1068	      - 0.572
1069	      - -0.01
1070	      - 0.038
1071	      - —
1072	    - - Belebele
1073	      - 0.5
1074	      - 0.548
1075	      - -0.013
1076	      - 0.031
1077	      - 0.72
1078	    - - MMLU-ProX
1079	      - 0.55
1080	      - 0.562
1081	      - -0.008
1082	      - 0.035
1083	      - 0.78
1084	  figures_description:
1085	  - 'Figure S2 (appendix): Scatter plot of per-language ZS AUROC on GlobalMMLU vs
1086	    Belebele/MMLU-ProX. Moderate positive correlation but visible deviations, especially
1087	    for low-resource languages.'
1088	  analysis: 'Cross-benchmark generalization moderate but not strong。Belebele 的低 performance
1089	    暗示 correctness probing 可能对任务格式敏感。在 worst-tier paper 中这增加了一层 caveat： findings 可能
1090	    MCQA-specific，generalization to other formats uncertain。
1091	
1092	    '
1093	- name: Quantization Validation Ablation
1094	  plan_id: plan_010
1095	  description: W4A16 vs FP16 (Llama), INT4 vs FP16 (Qwen), 5 representative layers,
1096	    5% data subset
1097	  expected_results:
1098	    llama_w4a16_vs_fp16_max_delta_auroc: 0.018
1099	    llama_w4a16_vs_fp16_mean_delta_auroc: 0.009
1100	    llama_w4a16_vs_fp16_spearman_rank_preservation: 0.91
1101	    qwen_int4_vs_fp16_max_delta_auroc: 0.022
1102	    qwen_int4_vs_fp16_mean_delta_auroc: 0.012
1103	    qwen_int4_vs_fp16_spearman_rank_preservation: 0.88
1104	    problematic_layers_count: 2
1105	  result_rationale: 'Worst tier 下量化 artifacts 不是灾难性的但 non-negligible。W4A16 mean delta
1106	    0.9pp 和 INT4 mean delta 1.2pp 在多数层可接受，但在 2/5 测试层出现 >1.5pp 偏差—— 特别是在最深层（correctness
1107	    signal 最集中的地方），quantization 对高频/低方差的 correctness direction 影响更大。Rank preservation
1108	    88-91% 意味着 per-language ranking 大体保持但不完美。在 worst tier 下这创造了一个 uncomfortable caveat：
1109	    所有关于深层 probe 的结论都 potentially 受量化影响，但无法做完整的 FP16 实验来确认。 需要在 limitations 中明确讨论。INT4
1110	    比 W4A16 worse 因为 4-bit weight-only 比 4-bit weight + 16-bit activation 更 aggressive。
1111	
1112	    '
1113	  tables:
1114	  - name: 'Table 8: Quantization Validation'
1115	    columns:
1116	    - model
1117	    - quant
1118	    - layer_pct
1119	    - fp16_auroc
1120	    - quant_auroc
1121	    - delta
1122	    - rank_preserved
1123	    rows:
1124	    - - Llama4
1125	      - W4A16
1126	      - 20%
1127	      - 0.648
1128	      - 0.645
1129	      - -0.003
1130	      - ✓
1131	    - - Llama4
1132	      - W4A16
1133	      - 40%
1134	      - 0.672
1135	      - 0.665
1136	      - -0.007
1137	      - ✓
1138	    - - Llama4
1139	      - W4A16
1140	      - 60%
1141	      - 0.695
1142	      - 0.683
1143	      - -0.012
1144	      - ✓
1145	    - - Llama4
1146	      - W4A16
1147	      - 80%
1148	      - 0.708
1149	      - 0.692
1150	      - -0.016
1151	      - ✗ (2 langs swap)
1152	    - - Llama4
1153	      - W4A16
1154	      - 95%
1155	      - 0.712
1156	      - 0.694
1157	      - -0.018
1158	      - ✗ (3 langs swap)
1159	    - - Qwen3
1160	      - INT4
1161	      - 20%
1162	      - 0.625
1163	      - 0.62
1164	      - -0.005
1165	      - ✓
1166	    - - Qwen3
1167	      - INT4
1168	      - 40%
1169	      - 0.668
1170	      - 0.658
1171	      - -0.01
1172	      - ✓
1173	    - - Qwen3
1174	      - INT4
1175	      - 60%
1176	      - 0.702
1177	      - 0.688
1178	      - -0.014
1179	      - ✗ (1 lang swap)
1180	    - - Qwen3
1181	      - INT4
1182	      - 80%
1183	      - 0.728
1184	      - 0.71
1185	      - -0.018
1186	      - ✗ (3 langs swap)
1187	    - - Qwen3
1188	      - INT4
1189	      - 95%
1190	      - 0.738
1191	      - 0.716
1192	      - -0.022
1193	      - ✗ (4 langs swap)
1194	  figures_description:
1195	  - 'Figure S3 (appendix): Layer-wise quantization delta plot showing increasing divergence
1196	    with depth for both models.'
1197	  analysis: 'Quantization 在深层引入 1-2pp 的系统性偏差。在 worst tier 下这不改变主要结论（negative results
1198	    不依赖于精确数值），但增加了 limitations section 的内容。Deep layer probe results（包括 EN-optimal
1199	    layer 的 AUROC）可能被 overestimate 了 ~1pp by quantization loss。
1200	
1201	    '
1202	- name: CKA Cross-Lingual Representation Similarity Analysis
1203	  plan_id: plan_011
1204	  description: CKA (linear kernel) EN vs target, all probed layers, 20 langs × 2 models.
1205	    Simpson's Paradox 验证。
1206	  expected_results:
1207	    simpson_partial_rho_qwen: 0.11
1208	    simpson_partial_p_qwen: 0.31
1209	    simpson_partial_rho_llama: 0.08
1210	    simpson_partial_p_llama: 0.42
1211	    raw_correlation_rho_qwen: -0.28
1212	    raw_correlation_rho_llama: -0.35
1213	    raw_correlation_p_qwen: 0.001
1214	    raw_correlation_p_llama: <0.001
1215	    same_layer_cross_lang_rho_median: 0.15
1216	    same_layer_cross_lang_significant_layers: 2/24 (Qwen), 0/12 (Llama)
1217	    cka_threshold_identifiable: false
1218	    subspace_angle_consistency: low — angles vary 15-65° across languages at same
1219	      layer
1220	    pilot_replication_5lang: partial — Llama rho drops from +0.41 to +0.08 with 20
1221	      langs
1222	  result_rationale: '这是 worst tier 最关键的 falsification。5 语言 pilot 中的 Simpson''s Paradox
1223	    (Llama partial rho=+0.41, p=0.006) 被确认为 small-sample artifact。当 20 语言数据进入分析后：(1)
1224	    新增的 15 种语言中多数与 CKA-transfer 关系不一致，部分语言（特别是 MID/LOW tier）的 CKA 模式与 pilot 的 5 种语言截然不同——
1225	    pilot 恰好选中了 CKA 与 transfer 最相关的语言子集（zh, ar 高 CKA + 低 degradation 拉高了相关性）。 (2)
1226	    Partial correlation controlling for depth 大幅缩水：Qwen rho 从 pilot 的 +0.18 降至 +0.11
1227	    (仍 n.s.)， Llama rho 从 +0.41 骤降至 +0.08。原因是新增语言打破了"within-layer CKA predicts transfer"的模式——
1228	    同一层内不同语言的 CKA 值差异巨大但 transfer 性能差异不 track CKA。 (3) Same-layer cross-language analysis
1229	    (n=20 per layer) 是最强检验：median rho=0.15， 仅 2/24 Qwen layers 和 0/12 Llama layers
1230	    达到显著——CKA 在 within-layer 水平几乎无解释力。 (4) Subspace angle analysis 显示 correctness
1231	    direction 的跨语言一致性远低于预期—— angles 在 15-65° 范围波动，不支持"robust low-dimensional language-agnostic
1232	    subspace"的说法。 结论：CKA 不提供超越 depth 的解释力，必须从"geometric analysis"降级为"suggestive correlation"。
1233	
1234	    '
1235	  tables:
1236	  - name: 'Table 9a: Simpson''s Paradox Full-Scale Validation'
1237	    columns:
1238	    - model
1239	    - raw_rho
1240	    - raw_p
1241	    - partial_rho_depth
1242	    - partial_p
1243	    - pilot_partial_rho
1244	    - pilot_partial_p
1245	    - verdict
1246	    rows:
1247	    - - Qwen3-235B
1248	      - -0.28
1249	      - 0.001
1250	      - 0.11
1251	      - 0.31
1252	      - +0.18 (n.s.)
1253	      - 0.274
1254	      - n.s. → no Simpson's Paradox
1255	    - - Llama4-Scout
1256	      - -0.35
1257	      - <0.001
1258	      - 0.08
1259	      - 0.42
1260	      - +0.41 (sig.)
1261	      - 0.006
1262	      - pilot artifact confirmed
1263	  - name: 'Table 9b: Same-Layer Cross-Language CKA-Transfer Correlation (top 5 layers)'
1264	    columns:
1265	    - model
1266	    - layer
1267	    - layer_pct
1268	    - cka_transfer_rho
1269	    - p_value
1270	    - n_langs
1271	    rows:
1272	    - - Qwen3
1273	      - 36
1274	      - 38%
1275	      - 0.22
1276	      - 0.35
1277	      - 20
1278	    - - Qwen3
1279	      - 48
1280	      - 51%
1281	      - 0.31
1282	      - 0.18
1283	      - 20
1284	    - - Qwen3
1285	      - 56
1286	      - 60%
1287	      - 0.18
1288	      - 0.45
1289	      - 20
1290	    - - Qwen3
1291	      - 64
1292	      - 68%
1293	      - 0.42
1294	      - 0.065
1295	      - 20
1296	    - - Qwen3
1297	      - 72
1298	      - 77%
1299	      - 0.38
1300	      - 0.098
1301	      - 20
1302	    - - Llama4
1303	      - 16
1304	      - 33%
1305	      - 0.12
1306	      - 0.61
1307	      - 20
1308	    - - Llama4
1309	      - 24
1310	      - 50%
1311	      - 0.08
1312	      - 0.74
1313	      - 20
1314	    - - Llama4
1315	      - 32
1316	      - 67%
1317	      - 0.25
1318	      - 0.29
1319	      - 20
1320	    - - Llama4
1321	      - 40
1322	      - 83%
1323	      - 0.15
1324	      - 0.53
1325	      - 20
1326	    - - Llama4
1327	      - 44
1328	      - 92%
1329	      - 0.05
1330	      - 0.83
1331	      - 20
1332	  - name: 'Table 9c: Subspace Angle Analysis (Correctness Direction, EN vs Target)'
1333	    columns:
1334	    - lang
1335	    - tier
1336	    - qwen3_angle_deg_L56
1337	    - llama4_angle_deg_L32
1338	    - note
1339	    rows:
1340	    - - zh
1341	      - HIGH
1342	      - 18
1343	      - 22
1344	      - relatively aligned
1345	    - - es
1346	      - HIGH
1347	      - 15
1348	      - 19
1349	      - relatively aligned
1350	    - - fr
1351	      - HIGH
1352	      - 20
1353	      - 25
1354	      - ''
1355	    - - de
1356	      - HIGH
1357	      - 22
1358	      - 28
1359	      - ''
1360	    - - ja
1361	      - HIGH
1362	      - 35
1363	      - 41
1364	      - large angle despite HIGH resource
1365	    - - ar
1366	      - MID
1367	      - 32
1368	      - 38
1369	      - ''
1370	    - - hi
1371	      - MID
1372	      - 38
1373	      - 45
1374	      - ''
1375	    - - ko
1376	      - MID
1377	      - 28
1378	      - 35
1379	      - ''
1380	    - - tr
1381	      - MID
1382	      - 42
1383	      - 48
1384	      - ''
1385	    - - sw
1386	      - LOW
1387	      - 52
1388	      - 58
1389	      - near orthogonal
1390	    - - bn
1391	      - LOW
1392	      - 48
1393	      - 55
1394	      - ''
1395	    - - am
1396	      - LOW
1397	      - 62
1398	      - 65
1399	      - correctness direction nearly unrelated
1400	  figures_description:
1401	  - 'Figure 6a: CKA heatmap (language × layer) for both models. Shows CKA decline
1402	    with depth but no clear correspondence to transfer AUROC patterns.'
1403	  - 'Figure 6b: Scatter plot of partial residuals (CKA residualized on depth vs transfer
1404	    AUROC residualized on depth) for both models. Diffuse cloud with no visible trend.
1405	    Annotations show partial rho and p-values.'
1406	  - 'Figure 6c: Subspace angle distribution (violin plot by resource tier). Clear
1407	    tier gradient but HIGH tier also shows 15-35° range, undermining ''language-agnostic
1408	    subspace'' claim.'
1409	  analysis: 'CKA analysis 的全面失败是 worst tier 的 defining feature。Pilot 的 Simpson''s
1410	    Paradox 从 Llama rho=+0.41 (p=0.006) 崩溃到 rho=+0.08 (p=0.42)——这是教科书式的 small-sample
1411	    inflation。 5 语言 pilot 恰好 overrepresented CKA-transfer 关系最强的语言（zh, ar），排除了关系最弱的语言。
1412	    Subspace angle analysis 进一步否定了"correctness direction is a robust low-dimensional
1413	    language-agnostic subspace"的前提假设：即使 HIGH resource 语言的 angle 也有 15-35° 的 spread，
1414	    LOW resource 达到 48-65°（近乎不相关）。这意味着 Miao & Ungar (2026) 的 EN-only correctness direction
1415	    在跨语言场景下不是 language-agnostic 的——这本身是一个重要的 negative finding，值得在 paper 中强调。 CKA 框架从
1416	    geometric analysis 降级为 descriptive visualization（仅展示 CKA 随 depth 的下降趋势）， 不再承载解释性角色。
1417	
1418	    '
1419	- name: Linear Projection Sensitivity Analysis
1420	  plan_id: plan_012
1421	  description: Procrustes alignment with 10/20/50/100/200 parallel pairs, 2 models
1422	    × 5 layers × 20 langs
1423	  expected_results:
1424	    pairs_to_95pct_mean: 142
1425	    pairs_to_95pct_range:
1426	    - 85
1427	    - 198
1428	    pairs_to_95pct_high_tier: 68
1429	    pairs_to_95pct_mid_tier: 125
1430	    pairs_to_95pct_low_tier: 182
1431	    saturation_curve_r2: 0.82
1432	    pair_10_mean_auroc: 0.548
1433	    pair_20_mean_auroc: 0.568
1434	    pair_50_mean_auroc: 0.588
1435	    pair_100_mean_auroc: 0.601
1436	    pair_200_mean_auroc: 0.61
1437	    procrustes_reversal_threshold: inconsistent — varies by language
1438	    helps_when_zs_below: ranges from 0.48 to 0.58 across languages
1439	    hurts_when_zs_above: ranges from 0.55 to 0.68 across languages
1440	    reversal_overlap_zone:
1441	    - 0.48
1442	    - 0.68
1443	  result_rationale: 'Worst tier 下 linear projection 需要 100-200 pairs（非 50）达到 95% 性能：
1444	    (1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需要更多数据点来 稳定估计 rotation
1445	    matrix——50 pairs 在高维空间中 rank-deficient，低资源语言的 parallel pairs 质量更差（翻译质量低→activation
1446	    噪声→需要更多 pairs 来 average out noise）。 (2) Resource-tier 分层仍然存在（HIGH 68 pairs vs
1447	    LOW 182 pairs）但 tier 内方差大—— 同一 tier 内语言间差异可达 2-3×（如 zh 需 45 pairs 但 ja 需 95 pairs，都是
1448	    HIGH）。 (3) Procrustes 效果反转的阈值高度 language-specific：帮助的 ZS AUROC 范围和伤害的范围 有 [0.48,
1449	    0.68] 的 overlap zone，意味着对同一 ZS AUROC 值，不同语言可能被帮助或伤害。 无法给出单一可操作的阈值——这使得"practitioners
1450	    should use linear projection when ZS < X" 的建议变得不可靠。
1451	
1452	    '
1453	  tables:
1454	  - name: 'Table 10a: Linear Projection Sample Efficiency (mean across 2 models ×
1455	      20 langs)'
1456	    columns:
1457	    - n_pairs
1458	    - mean_auroc
1459	    - pct_of_200pair
1460	    - std_across_langs
1461	    - significant_improvement_pct
1462	    rows:
1463	    - - 10
1464	      - 0.548
1465	      - 68%
1466	      - 0.065
1467	      - 25%
1468	    - - 20
1469	      - 0.568
1470	      - 79%
1471	      - 0.058
1472	      - 40%
1473	    - - 50
1474	      - 0.588
1475	      - 89%
1476	      - 0.052
1477	      - 55%
1478	    - - 100
1479	      - 0.601
1480	      - 95%
1481	      - 0.048
1482	      - 65%
1483	    - - 200
1484	      - 0.61
1485	      - 100%
1486	      - 0.045
1487	      - 72%
1488	  - name: 'Table 10b: Pairs to 95% Performance by Resource Tier'
1489	    columns:
1490	    - tier
1491	    - mean_pairs_95pct
1492	    - min
1493	    - max
1494	    - std
1495	    rows:
1496	    - - HIGH
1497	      - 68
1498	      - 42
1499	      - 98
1500	      - 22
1501	    - - MID
1502	      - 125
1503	      - 78
1504	      - 165
1505	      - 35
1506	    - - LOW
1507	      - 182
1508	      - 145
1509	      - 198
1510	      - 28
1511	  - name: 'Table 10c: Procrustes Effect Reversal — Inconsistent Thresholds'
1512	    columns:
1513	    - lang
1514	    - tier
1515	    - zs_auroc
1516	    - linproj_200_auroc
1517	    - delta
1518	    - effect
1519	    rows:
1520	    - - am
1521	      - LOW
1522	      - 0.475
1523	      - 0.498
1524	      - 0.023
1525	      - helps
1526	    - - yo
1527	      - LOW
1528	      - 0.463
1529	      - 0.49
1530	      - 0.027
1531	      - helps
1532	    - - sw
1533	      - LOW
1534	      - 0.504
1535	      - 0.518
1536	      - 0.014
1537	      - helps
1538	    - - bn
1539	      - LOW
1540	      - 0.512
1541	      - 0.528
1542	      - 0.016
1543	      - helps
1544	    - - tr
1545	      - MID
1546	      - 0.532
1547	      - 0.548
1548	      - 0.016
1549	      - helps
1550	    - - hi
1551	      - MID
1552	      - 0.552
1553	      - 0.561
1554	      - 0.009
1555	      - helps (marginal)
1556	    - - vi
1557	      - MID
1558	      - 0.558
1559	      - 0.558
1560	      - 0.0
1561	      - neutral
1562	    - - ko
1563	      - MID
1564	      - 0.578
1565	      - 0.575
1566	      - -0.003
1567	      - neutral/hurts
1568	    - - ar
1569	      - MID
1570	      - 0.603
1571	      - 0.598
1572	      - -0.005
1573	      - hurts
1574	    - - ru
1575	      - MID
1576	      - 0.624
1577	      - 0.612
1578	      - -0.012
1579	      - hurts
1580	    - - zh
1581	      - HIGH
1582	      - 0.658
1583	      - 0.641
1584	      - -0.017
1585	      - hurts
1586	    - - es
1587	      - HIGH
1588	      - 0.67
1589	      - 0.65
1590	      - -0.02
1591	      - hurts
1592	    - - ja
1593	      - HIGH
1594	      - 0.582
1595	      - 0.59
1596	      - 0.008
1597	      - helps (despite HIGH tier)
1598	  figures_description:
1599	  - 'Figure 7a: Saturation curves (n_pairs vs AUROC) faceted by resource tier, with
1600	    95% threshold marked. HIGH saturates early, LOW saturates late. Per-language thin
1601	    lines show within-tier variance.'
1602	  - 'Figure 7b: Scatter plot of ZS AUROC (x) vs linear projection ΔAUROC (y). Shows
1603	    rough negative trend but wide scatter band. Vertical zone [0.48-0.68] highlighted
1604	    as ''inconsistent reversal zone'' where both positive and negative deltas occur.'
1605	  analysis: 'Linear projection 仍是唯一可行方案但实用性大打折扣：(1) 需 100+ pairs 而非 50， 对低资源语言来说 parallel
1606	    data 本身就是稀缺资源；(2) 效果反转阈值 inconsistent， practitioner 无法事先知道某语言是否会被帮助或伤害。Paper 中只能给出条件性
1607	    recommendation： "当 ZS AUROC < 0.50 时大概率有益，> 0.65 时大概率有害，0.50-0.65 区间需要 held-out
1608	    validation" ——这比预期的 clean threshold (0.50/0.60) 弱得多。
1609	
1610	    '
1611	- name: Probing Control Tasks (Cross-Lingual Extension)
1612	  plan_id: plan_013
1613	  description: Hewitt & Liang control tasks for 20 languages × all probed layers ×
1614	    2 models, selectivity analysis
1615	  expected_results:
1616	    control_artifact_rate_low_resource: 0.42
1617	    control_artifact_rate_mid_resource: 0.37
1618	    control_artifact_rate_high_resource: 0.18
1619	    control_artifact_rate_overall: 0.31
1620	    selectivity_below_0.05_pct_low: 42%
1621	    selectivity_below_0.05_pct_mid: 37%
1622	    selectivity_below_0.05_pct_high: 18%
1623	    mean_selectivity_en: 0.245
1624	    mean_selectivity_high: 0.198
1625	    mean_selectivity_mid: 0.142
1626	    mean_selectivity_low: 0.085
1627	    selectivity_vs_zs_auroc_rho: 0.68
1628	    layers_most_affected: shallow layers (0-30% depth)
1629	    worst_lang_layer_combos:
1630	    - am-L0
1631	    - yo-L4
1632	    - my-L0
1633	    - am-L4
1634	    - yo-L0
1635	    - te-L8
1636	  result_rationale: '这是 worst tier 的最强贡献。Control task artifact rate 在低资源语言达 42%，中资源
1637	    37%， 远超 MVP pilot 的 28%。原因：(1) MVP 的 5 语言中低资源仅 sw 一种，现在 6-7 种低资源语言 暴露了更系统性的问题——am,
1638	    yo, my 等在 LLM 预训练中极度不足，对应的 representation 缺乏区分性结构，probe 学到的主要是 capacity artifacts
1639	    而非 correctness signals。 (2) 中资源语言出现 37% artifact rate 是 worst tier 的 signature
1640	    finding： 这不仅仅是"低资源语言有问题"——tr, th, vi 等中资源语言在浅层也有大量 artifacts， 说明 probing methodology
1641	    在 cross-lingual 场景的可靠性比预期差得多。 (3) Selectivity 与 ZS AUROC 高度相关（rho=0.68），暗示许多看似成功的
1642	    cross-lingual transfer 结果其实是 capacity artifacts 在目标语言中的 shadow。 这对整个跨语言 probing
1643	    文献有 field-level implication：任何不包含 control task 检验的 跨语言 probing 研究的结论都值得质疑。这是首次在
1644	    cross-lingual transfer 场景系统性 应用 selectivity 检验——贡献的 novelty 和 impact 在 worst tier
1645	    下反而最强。
1646	
1647	    '
1648	  tables:
1649	  - name: 'Table 11a: Control Task Artifact Rate by Resource Tier and Model'
1650	    columns:
1651	    - tier
1652	    - n_langs
1653	    - qwen3_artifact_rate
1654	    - llama4_artifact_rate
1655	    - combined
1656	    - selectivity_mean
1657	    rows:
1658	    - - HIGH
1659	      - 7
1660	      - 16%
1661	      - 20%
1662	      - 18%
1663	      - 0.198
1664	    - - MID
1665	      - 7
1666	      - 35%
1667	      - 39%
1668	      - 37%
1669	      - 0.142
1670	    - - LOW
1671	      - 6
1672	      - 40%
1673	      - 44%
1674	      - 42%
1675	      - 0.085
1676	    - - ALL
1677	      - 20
1678	      - 29%
1679	      - 33%
1680	      - 31%
1681	      - 0.145
1682	  - name: 'Table 11b: Per-Language Selectivity at EN-Optimal Layer'
1683	    columns:
1684	    - lang
1685	    - tier
1686	    - real_auroc
1687	    - permuted_auroc
1688	    - selectivity
1689	    - artifact_flag
1690	    rows:
1691	    - - en
1692	      - —
1693	      - 0.738
1694	      - 0.49
1695	      - 0.248
1696	      - ''
1697	    - - zh
1698	      - HIGH
1699	      - 0.672
1700	      - 0.498
1701	      - 0.174
1702	      - ''
1703	    - - es
1704	      - HIGH
1705	      - 0.681
1706	      - 0.495
1707	      - 0.186
1708	      - ''
1709	    - - fr
1710	      - HIGH
1711	      - 0.663
1712	      - 0.492
1713	      - 0.171
1714	      - ''
1715	    - - de
1716	      - HIGH
1717	      - 0.654
1718	      - 0.488
1719	      - 0.166
1720	      - ''
1721	    - - ja
1722	      - HIGH
1723	      - 0.582
1724	      - 0.502
1725	      - 0.08
1726	      - ''
1727	    - - pt
1728	      - HIGH
1729	      - 0.668
1730	      - 0.491
1731	      - 0.177
1732	      - ''
1733	    - - it
1734	      - HIGH
1735	      - 0.651
1736	      - 0.494
1737	      - 0.157
1738	      - ''
1739	    - - ar
1740	      - MID
1741	      - 0.603
1742	      - 0.498
1743	      - 0.105
1744	      - ''
1745	    - - hi
1746	      - MID
1747	      - 0.561
1748	      - 0.505
1749	      - 0.056
1750	      - ⚠
1751	    - - ru
1752	      - MID
1753	      - 0.624
1754	      - 0.495
1755	      - 0.129
1756	      - ''
1757	    - - ko
1758	      - MID
1759	      - 0.585
1760	      - 0.501
1761	      - 0.084
1762	      - ''
1763	    - - tr
1764	      - MID
1765	      - 0.541
1766	      - 0.508
1767	      - 0.033
1768	      - ⚠
1769	    - - vi
1770	      - MID
1771	      - 0.558
1772	      - 0.512
1773	      - 0.046
1774	      - ⚠
1775	    - - th
1776	      - MID
1777	      - 0.523
1778	      - 0.498
1779	      - 0.025
1780	      - ⚠
1781	    - - sw
1782	      - LOW
1783	      - 0.512
1784	      - 0.505
1785	      - 0.007
1786	      - ⚠⚠
1787	    - - bn
1788	      - LOW
1789	      - 0.519
1790	      - 0.502
1791	      - 0.017
1792	      - ⚠⚠
1793	    - - am
1794	      - LOW
1795	      - 0.482
1796	      - 0.478
1797	      - 0.004
1798	      - ⚠⚠
1799	    - - yo
1800	      - LOW
1801	      - 0.471
1802	      - 0.465
1803	      - 0.006
1804	      - ⚠⚠
1805	    - - te
1806	      - LOW
1807	      - 0.498
1808	      - 0.488
1809	      - 0.01
1810	      - ⚠⚠
1811	    - - my
1812	      - LOW
1813	      - 0.463
1814	      - 0.458
1815	      - 0.005
1816	      - ⚠⚠
1817	  - name: 'Table 11c: Layers with Artifact Rate > 40%'
1818	    columns:
1819	    - model
1820	    - layer_range
1821	    - high_artifact_pct
1822	    - mid_artifact_pct
1823	    - low_artifact_pct
1824	    rows:
1825	    - - Qwen3
1826	      - L0-L20 (0-21%)
1827	      - 8%
1828	      - 48%
1829	      - 65%
1830	    - - Qwen3
1831	      - L24-L48 (26-51%)
1832	      - 12%
1833	      - 35%
1834	      - 52%
1835	    - - Qwen3
1836	      - L52-L72 (55-77%)
1837	      - 18%
1838	      - 28%
1839	      - 35%
1840	    - - Qwen3
1841	      - L76-L92 (81-98%)
1842	      - 25%
1843	      - 32%
1844	      - 38%
1845	    - - Llama4
1846	      - L0-L12 (0-25%)
1847	      - 12%
1848	      - 52%
1849	      - 68%
1850	    - - Llama4
1851	      - L16-L28 (33-58%)
1852	      - 18%
1853	      - 38%
1854	      - 48%
1855	    - - Llama4
1856	      - L32-L44 (67-92%)
1857	      - 22%
1858	      - 30%
1859	      - 35%
1860	    - - Llama4
1861	      - L48 (100%)
1862	      - 28%
1863	      - 35%
1864	      - 40%
1865	  figures_description:
1866	  - 'Figure 8a: Heatmap of selectivity (language × layer) for Qwen3-235B. Color scale:
1867	    red (< 0.05 artifact) to green (> 0.20 genuine). Large red region in bottom-left
1868	    (low-resource × shallow layers). Mid-resource languages show surprising red patches
1869	    even at moderate depths.'
1870	  - 'Figure 8b: Bar chart of artifact rate by resource tier with 95% CI. Error bars
1871	    computed via bootstrap over languages within each tier. The CI for MID tier overlaps
1872	    substantially with LOW tier — the artifact problem is not confined to low-resource.'
1873	  - 'Figure 8c: Scatter plot of selectivity vs ZS AUROC across all language-layer-model
1874	    combinations. Strong positive correlation (rho=0.68) suggests many ''successful''
1875	    ZS transfer results are artifacts.'
1876	  analysis: 'Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact
1877	    rate 波及中资源语言是 field-level 发现：不是"低资源语言有问题，审稿人可以忽略"，而是 "所有跨语言 probing 研究——包括那些只看中/高资源语言的——都需要
1878	    selectivity 检验"。 Selectivity 与 ZS AUROC 的高相关性 (rho=0.68) 尤其尖锐：它暗示 cross-lingual
1879	    probing 文献中的许多 positive results 可能是 capacity artifacts。这个 finding 独立于 本文的其他所有
1880	    claims——即使 Pareto, CaCLR, decomposition 全部失败，这个方法论贡献 仍然足以支撑一篇 findings paper。首次在
1881	    cross-lingual transfer 场景应用 Hewitt & Liang selectivity 框架，发现 artifact 问题远比 monolingual
1882	    probing 严重——这是 reframe 后 paper 叙事的 structural foundation。
1883	
1884	    '
1885	- name: Gemma 4 31B Dense Pareto Frontier
1886	  plan_id: plan_008
1887	  description: Gemma 4 31B Dense (60 layers, FP16), 15 probed layers, 20 langs, camera-ready
1888	    第三架构
1889	  expected_results:
1890	    en_best_auroc: 0.742
1891	    en_best_layer: 48
1892	    zs_pass_rate: 0.6
1893	    global_spearman_rho: -0.22
1894	    global_spearman_p: 0.045
1895	    per_lang_significant_count: 4
1896	    dense_vs_moe_pareto_clarity: moderately clearer but still noisy
1897	    control_artifact_rate_low: 0.38
1898	  result_rationale: 'Dense 架构避免了 MoE routing 的 non-monotonic 噪声，global rho marginally
1899	    significant (p=0.045)——pareto_spearman_rho_significant_archs 从 0 变为 1。但这反而增加了叙述复杂性：
1900	    Pareto 是 architecture-dependent 的，dense 模型有 moderate tradeoff，MoE 没有。 无法声称 depth-transfer
1901	    tradeoff 是普遍现象。EN AUROC 0.742 在 worst 范围内。 Control artifact rate 对低资源语言 38%，确认这不是
1902	    MoE-specific 的问题。 作为 camera-ready 扩展，Gemma 增加了 architecture coverage 但不改变核心叙事。
1903	
1904	    '
1905	  tables:
1906	  - name: 'Table S1: Gemma 4 31B Dense Pareto Summary'
1907	    columns:
1908	    - metric
1909	    - value
1910	    rows:
1911	    - - en_best_auroc
1912	      - 0.742
1913	    - - zs_pass_rate
1914	      - 60% (12/20)
1915	    - - global_pareto_rho
1916	      - -0.22 (p=0.045)
1917	    - - per_lang_significant_rho
1918	      - 4/20
1919	    - - control_artifact_rate_low
1920	      - 38%
1921	    - - simpson_partial_rho
1922	      - +0.14 (p=0.22)
1923	  figures_description:
1924	  - 'Figure S4 (camera-ready): Gemma 4 Pareto scatter showing cleaner but still noisy
1925	    frontier vs Qwen3/Llama4.'
1926	  analysis: 'Gemma dense 提供了 MoE vs dense 的对比：dense 架构的 Pareto 更清晰但仍远非 universal。
1927	    4/20 语言 per-language significance 比 Qwen3 的 2/20 好但仍是少数。 Simpson''s Paradox 在
1928	    Gemma 上也不显著 (partial rho=+0.14, p=0.22)。 三架构综合：0-1 个有 significant Pareto，0 个有
1929	    significant Simpson''s Paradox—— worst tier 叙事的 architecture coverage 从 2 扩展到
1930	    3 但结论不变。
1931	
1932	    '
1933	- name: Extended Language Coverage (50+ Languages)
1934	  plan_id: plan_009
1935	  description: 从 20 扩展到 50+ 语言, camera-ready extension
1936	  expected_results:
1937	    total_languages: 52
1938	    zs_pass_rate_52lang: 0.52
1939	    control_artifact_rate_low_expanded: 0.45
1940	    new_langs_with_significant_pareto: 1
1941	    additional_artifact_langs: 15
1942	    linear_proj_pairs_to_95pct_expanded_mean: 158
1943	  result_rationale: '扩展到 50+ 语言后，新增的大部分是 MID/LOW resource 语言。ZS pass rate 从 60% (20
1944	    langs) 降至 52% (52 langs) 因为新增语言 skew toward lower resource。Control artifact rate
1945	    在扩展后的低资源组升至 45%——更多极低资源语言被纳入。这进一步强化了 control task finding 的 field-level 意义：近半数低资源跨语言
1946	    probing 结果是 artifacts。 但扩展语言数不改变核心 negative results——主要增加 statistical power 和
1947	    coverage。 Linear projection 需要的 pairs 数在扩展后 mean 升至 158 因为更多 hard languages。
1948	
1949	    '
1950	  tables:
1951	  - name: 'Table S2: 52-Language Summary vs 20-Language Core'
1952	    columns:
1953	    - metric
1954	    - 20_lang
1955	    - 52_lang
1956	    - delta
1957	    rows:
1958	    - - zs_pass_rate
1959	      - 60%
1960	      - 52%
1961	      - -8pp
1962	    - - control_artifact_low
1963	      - 42%
1964	      - 45%
1965	      - +3pp
1966	    - - control_artifact_mid
1967	      - 37%
1968	      - 39%
1969	      - +2pp
1970	    - - linear_proj_mean_pairs
1971	      - 142
1972	      - 158
1973	      - '+16'
1974	    - - simpson_partial_rho_max
1975	      - 0.11
1976	      - 0.09
1977	      - '-0.02'
1978	  figures_description:
1979	  - 'Figure S5 (camera-ready): World map of ZS AUROC at EN-optimal layer with artifact-flagged
1980	    languages marked. Large regions (Sub-Saharan Africa, Southeast Asia) dominated
1981	    by artifact flags.'
1982	  analysis: 52 语言扩展主要服务于 coverage 和 robustness 声称。 核心结论不变但 control task finding 更加
1983	    impactful：近半数低资源结果是 artifacts 在 50+ 语言规模下是对跨语言 probing 文献的强警告。
1984	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b39e96fb-c558-4442-95fc-4637614c5094",
  "isSidechain": false,
  "promptId": "b640863f-263b-4e66-ad8a-d5dc1b38729c",
  "type": "user",
  "uuid": "fc2c39f7-2a8d-4574-a69e-5565dfa2a025",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/imagined_experiments.yaml",
      "content": "tier: worst\nnarrative_guidance: '原始几何洞见 framing 全面崩塌。Simpson''s Paradox 在 20 语言全量验证中双架构均不显著（Qwen\n  partial rho=+0.11, p=0.31; Llama partial rho=+0.08, p=0.42）， CKA 在 depth 之外无额外解释力——5\n  语言 pilot 结果被确认为 small-sample artifact。CaCLR 三个 OOM 的 β sweep 证实 consistency loss\n  完全 inert，且几何子空间解释也不成立：correctness direction 的跨语言 persistence 远弱于预期，非 robust low-dimensional\n  subspace。 Pareto frontier 噪声极大，20 语言中仅 2-3 个达到 per-language 显著性，non-monotonic 模式普遍存在。控制任务分析揭示问题远超预期——\n  不仅低资源语言 artifact rate 达 42%，中资源语言也有 37% 层级组合出现 capacity artifacts，这对整个跨语言 probing\n  文献构成方法论挑战。 Difficulty decomposition 完全无效，random-direction control 产生同量级效果。Linear\n  projection 需要 120-180 pairs（非 50）， 且 Procrustes 效果反转阈值在语言间高度不一致，无法给出可靠的单一阈值。 新 framing\n  路线：''The limits of cross-lingual calibration probe transfer — a large-scale negative\n  result with methodological implications''。 三层贡献重构：(1) 控制任务发现是最强贡献——首次在 cross-lingual\n  probing 场景系统性应用 selectivity 检验，>35% artifact rate 对整个领域有直接 implication；(2) 综合 negative\n  result 同时关闭 distributional matching 和 geometric alignment 两条路径， 附完整 ablation 和 sweep\n  数据；(3) 条件性实用指导——linear projection 作为唯一可行方案但需 100+ pairs， 按 resource-tier 和 baseline\n  ZS quality 分层推荐。仍可发 EACL 作为 rigorous negative result + methodology paper。\n\n  '\nimagined_experiments:\n- name: Qwen3-235B Full Pareto Frontier\n  plan_id: plan_001\n  description: Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th),\n    20 languages, 5 transfer conditions\n  expected_results:\n    en_best_auroc: 0.738\n    en_best_layer: 72\n    en_auroc_range:\n    - 0.598\n    - 0.738\n    en_best_ece_raw: 0.203\n    zs_pass_count: 12\n    zs_pass_rate: 0.6\n    zs_pass_langs:\n    - zh\n    - es\n    - fr\n    - de\n    - ja\n    - pt\n    - it\n    - ar\n    - hi\n    - ru\n    - ko\n    - vi\n    zs_fail_langs:\n    - tr\n    - th\n    - sw\n    - bn\n    - am\n    - yo\n    - te\n    - my\n    best_zs_auroc:\n      zh: 0.672\n      es: 0.681\n      fr: 0.663\n      de: 0.654\n      ja: 0.582\n      pt: 0.668\n      it: 0.651\n      ar: 0.603\n      hi: 0.561\n      ru: 0.624\n      ko: 0.585\n      tr: 0.541\n      vi: 0.558\n      th: 0.523\n      sw: 0.512\n      bn: 0.519\n      am: 0.482\n      yo: 0.471\n      te: 0.498\n      my: 0.463\n    global_spearman_rho: -0.15\n    global_spearman_p: 0.062\n    per_lang_significant_negative_rho_count: 2\n    per_lang_significant_positive_rho_count: 0\n    per_lang_nonmonotonic_count: 14\n    mean_shift_delta_auroc_all: 0.0\n    linear_proj_200pair_mean_delta: 0.038\n    fewshot_25_mean_delta: 0.022\n    fewshot_100_mean_delta: 0.051\n  result_rationale: 'EN best AUROC 落在 worst 范围 [0.7, 0.76] 内。MoE routing 导致层间 representation\n    变异度增大， 每第 4 层采样可能跳过 expert routing 的关键切换点，引入额外噪声。INT4 量化对 correctness signal 有轻微衰减（plan_010\n    将确认）。 ZS 60% pass rate 因为：(1) 235B 参数量提升了高/中资源语言的 representation quality，但 INT4\n    折损部分增益； (2) MoE 的 expert specialization 可能导致不同语言路由到不同 expert 子集，correctness direction\n    的跨语言一致性被 expert 分化削弱； (3) 低资源语言在预训练中 token 占比不足，加之 MoE 可能给它们分配较少 expert capacity。\n    Global Pareto rho=-0.15 仅 marginally significant (p=0.062)：depth-transfer tradeoff\n    在多数语言不显著， 因为 MoE 中 depth 不单调地映射到 representation specialization——expert routing\n    在不同深度可以\"重置\"语言特异性。 14/20 语言呈现 non-monotonic 模式（U 形、倒 U 形、锯齿形），这是 MoE 特有的现象。 Mean-shift\n    ΔAUROC ≡ 0 符合已证明的数学不变性。Linear projection 和 few-shot 有正增益但方差大。\n\n    '\n  tables:\n  - name: 'Table 1a: Qwen3-235B Per-Language Pareto Spearman ρ (Depth vs ZS-AUROC)'\n    columns:\n    - lang\n    - resource_tier\n    - best_zs_auroc\n    - best_zs_layer\n    - spearman_rho\n    - p_value\n    - pattern\n    rows:\n    - - zh\n      - HIGH\n      - 0.672\n      - 60\n      - -0.35\n      - 0.093\n      - weak negative\n    - - es\n      - HIGH\n      - 0.681\n      - 56\n      - -0.28\n      - 0.184\n      - n.s.\n    - - fr\n      - HIGH\n      - 0.663\n      - 60\n      - -0.31\n      - 0.141\n      - n.s.\n    - - de\n      - HIGH\n      - 0.654\n      - 56\n      - -0.22\n      - 0.3\n      - n.s.\n    - - ja\n      - HIGH\n      - 0.582\n      - 48\n      - 0.15\n      - 0.483\n      - non-monotonic U-shape\n    - - pt\n      - HIGH\n      - 0.668\n      - 60\n      - -0.25\n      - 0.238\n      - n.s.\n    - - it\n      - HIGH\n      - 0.651\n      - 56\n      - -0.19\n      - 0.375\n      - n.s.\n    - - ar\n      - MID\n      - 0.603\n      - 52\n      - 0.08\n      - 0.71\n      - flat\n    - - hi\n      - MID\n      - 0.561\n      - 48\n      - -0.42\n      - 0.041\n      - significant negative\n    - - ru\n      - MID\n      - 0.624\n      - 56\n      - -0.18\n      - 0.398\n      - n.s.\n    - - ko\n      - MID\n      - 0.585\n      - 44\n      - 0.22\n      - 0.301\n      - inverted — deeper helps\n    - - tr\n      - MID\n      - 0.541\n      - 44\n      - -0.12\n      - 0.576\n      - n.s.\n    - - vi\n      - MID\n      - 0.558\n      - 48\n      - 0.05\n      - 0.815\n      - flat\n    - - th\n      - MID\n      - 0.523\n      - 40\n      - -0.08\n      - 0.71\n      - n.s.\n    - - sw\n      - LOW\n      - 0.512\n      - 36\n      - -0.38\n      - 0.067\n      - marginal negative\n    - - bn\n      - LOW\n      - 0.519\n      - 40\n      - -0.15\n      - 0.485\n      - n.s.\n    - - am\n      - LOW\n      - 0.482\n      - 32\n      - 0.1\n      - 0.641\n      - non-monotonic\n    - - yo\n      - LOW\n      - 0.471\n      - 28\n      - -0.05\n      - 0.815\n      - noisy flat\n    - - te\n      - LOW\n      - 0.498\n      - 36\n      - -0.2\n      - 0.348\n      - n.s.\n    - - my\n      - LOW\n      - 0.463\n      - 28\n      - 0.12\n      - 0.576\n      - non-monotonic\n  - name: 'Table 1b: Qwen3-235B 5 Transfer Conditions Summary (mean across 20 langs)'\n    columns:\n    - condition\n    - mean_auroc\n    - std\n    - delta_vs_zs\n    - significant_improvement_count\n    rows:\n    - - zero-shot\n      - 0.572\n      - 0.072\n      - 0.0\n      - —\n    - - mean-shift\n      - 0.572\n      - 0.072\n      - 0.0\n      - 0/20\n    - - linear_proj_200\n      - 0.61\n      - 0.058\n      - 0.038\n      - 11/20\n    - - fewshot_25\n      - 0.594\n      - 0.065\n      - 0.022\n      - 7/20\n    - - fewshot_100\n      - 0.623\n      - 0.054\n      - 0.051\n      - 13/20\n  figures_description:\n  - 'Figure 1a: Scatter plot of EN AUROC vs best ZS AUROC per language across 24 layers\n    for Qwen3-235B. Points colored by resource tier. Shows diffuse cloud rather than\n    clean Pareto frontier. Non-monotonic trajectories for ja, ko, am, my highlighted\n    with dashed lines. Annotation shows global rho=-0.15 (p=0.062).'\n  - 'Figure 1b: Heatmap of ZS AUROC per language (y-axis) × probed layer (x-axis).\n    Shows irregular patterns with MoE-specific layer-to-layer variance. No smooth\n    gradient along depth axis.'\n  analysis: 'Qwen3-235B 的 Pareto frontier 远不如 MVP (Qwen2.5-7B) 清晰。MoE 架构的 expert routing\n    打破了 dense model 中 depth = specialization 的单调映射，导致 14/20 语言呈现 non-monotonic 模式。\n    仅 hi 和 sw 达到 per-language 显著性，但方向相反的 ko (+0.22, n.s.) 和 ja (+0.15, n.s.) 表明 depth-transfer\n    tradeoff 不是普遍现象。Global rho=-0.15 被 between-language 差异驱动而非 within-language depth\n    效应。MVP 的 clear Pareto 可能是 dense 7B model 的特殊现象，不推广到大规模 MoE。 5 transfer conditions\n    中 linear projection 和 few-shot 100 有中等改善，但 significant improvement 仅覆盖 55-65%\n    的语言，且主要集中在高资源语言。\n\n    '\n- name: Llama 4 Scout Full Pareto Frontier\n  plan_id: plan_002\n  description: Llama 4 Scout (48 layers, MoE, W4A16), 12 probed layers, 20 languages,\n    5 transfer conditions\n  expected_results:\n    en_best_auroc: 0.715\n    en_best_layer: 40\n    en_auroc_range:\n    - 0.612\n    - 0.715\n    en_best_ece_raw: 0.218\n    zs_pass_count: 11\n    zs_pass_rate: 0.55\n    zs_pass_langs:\n    - zh\n    - es\n    - fr\n    - de\n    - pt\n    - it\n    - ar\n    - ru\n    - ko\n    - vi\n    - ja\n    zs_fail_langs:\n    - hi\n    - tr\n    - th\n    - sw\n    - bn\n    - am\n    - yo\n    - te\n    - my\n    best_zs_auroc:\n      zh: 0.643\n      es: 0.658\n      fr: 0.641\n      de: 0.632\n      ja: 0.556\n      pt: 0.645\n      it: 0.628\n      ar: 0.581\n      hi: 0.542\n      ru: 0.602\n      ko: 0.571\n      tr: 0.523\n      vi: 0.555\n      th: 0.508\n      sw: 0.496\n      bn: 0.505\n      am: 0.468\n      yo: 0.455\n      te: 0.487\n      my: 0.448\n    global_spearman_rho: -0.08\n    global_spearman_p: 0.218\n    per_lang_significant_negative_rho_count: 0\n    per_lang_significant_positive_rho_count: 0\n    per_lang_nonmonotonic_count: 11\n  result_rationale: 'Llama 4 Scout 的 EN AUROC 低于 Qwen3 因为模型有效参数量更小（17B active vs 22B\n    active）。 W4A16 量化对 correctness signal 有轻微额外损耗。ZS pass rate 55% 处于 worst 范围低端。\n    仅 12 probed layers 使 per-language Spearman 检验功效极低（n=12），无语言达到显著性。 MVP (Llama-3.1-8B)\n    中观察到的 architecture-specific 弱 Pareto 在 Scout 上进一步恶化： Scout 是 MoE (16 experts)，与\n    3.1-8B 的 dense 架构根本不同，expert routing 引入同样的 non-monotonic 行为。Global rho=-0.08 完全不显著——Llama\n    架构系列的 depth-transfer tradeoff 不稳定。\n\n    '\n  tables:\n  - name: 'Table 2: Llama 4 Scout Per-Language Pareto Spearman ρ'\n    columns:\n    - lang\n    - resource_tier\n    - best_zs_auroc\n    - spearman_rho\n    - p_value\n    rows:\n    - - zh\n      - HIGH\n      - 0.643\n      - -0.2\n      - 0.533\n    - - es\n      - HIGH\n      - 0.658\n      - -0.15\n      - 0.641\n    - - fr\n      - HIGH\n      - 0.641\n      - -0.25\n      - 0.432\n    - - de\n      - HIGH\n      - 0.632\n      - -0.1\n      - 0.758\n    - - ja\n      - HIGH\n      - 0.556\n      - 0.3\n      - 0.343\n    - - pt\n      - HIGH\n      - 0.645\n      - -0.18\n      - 0.576\n    - - it\n      - HIGH\n      - 0.628\n      - -0.08\n      - 0.805\n    - - ar\n      - MID\n      - 0.581\n      - 0.25\n      - 0.432\n    - - hi\n      - MID\n      - 0.542\n      - -0.35\n      - 0.264\n    - - ru\n      - MID\n      - 0.602\n      - -0.05\n      - 0.878\n    - - ko\n      - MID\n      - 0.571\n      - 0.4\n      - 0.198\n    - - tr\n      - MID\n      - 0.523\n      - 0.1\n      - 0.758\n    - - vi\n      - MID\n      - 0.555\n      - 0.15\n      - 0.641\n    - - th\n      - MID\n      - 0.508\n      - -0.2\n      - 0.533\n    - - sw\n      - LOW\n      - 0.496\n      - -0.28\n      - 0.379\n    - - bn\n      - LOW\n      - 0.505\n      - -0.1\n      - 0.758\n    - - am\n      - LOW\n      - 0.468\n      - 0.05\n      - 0.878\n    - - yo\n      - LOW\n      - 0.455\n      - -0.15\n      - 0.641\n    - - te\n      - LOW\n      - 0.487\n      - -0.08\n      - 0.805\n    - - my\n      - LOW\n      - 0.448\n      - 0.18\n      - 0.576\n  figures_description:\n  - 'Figure 2: Llama 4 Scout Pareto scatter, same format as Figure 1a. Cloud更加散乱，global\n    rho=-0.08 (p=0.218)。Ko (+0.40) 和 ja (+0.30) 方向相反于预期。'\n  analysis: 'Llama 4 Scout 确认 worst tier 预期：depth-transfer tradeoff 在 MoE 架构上完全不显著。\n    与 Qwen3-235B 合并看，0 个架构在 p<0.05 水平展现清晰的 Pareto——pareto_spearman_rho_significant_archs=0。\n    MVP 中 Qwen2.5-7B dense model 的 clear Pareto 是 dense architecture + small scale\n    的特殊现象， 不推广到大规模 MoE。这对 Claim 1 是毁灭性的：无法声称存在普遍的 depth-transferability tradeoff。\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: CaCLR (BCE + α·SB-ECE + β·MMD), β sweep 3 OOM, α sweep, component ablation,\n    vs 4 baselines, 2 models × 20 langs\n  expected_results:\n    caclr_mean_delta_auroc_vs_zs_qwen: -0.008\n    caclr_mean_delta_auroc_vs_zs_llama: -0.012\n    caclr_mean_delta_auroc_combined: -0.01\n    caclr_best_beta: none — all β values inert or harmful\n    caclr_best_alpha: 0.1\n    beta_sweep_results:\n      beta_0.001:\n        mean_delta_auroc: -0.003\n        std: 0.018\n      beta_0.01:\n        mean_delta_auroc: -0.006\n        std: 0.021\n      beta_0.1:\n        mean_delta_auroc: -0.011\n        std: 0.025\n      beta_1.0:\n        mean_delta_auroc: -0.019\n        std: 0.031\n    alpha_sweep_results:\n      alpha_0.01:\n        mean_delta_auroc: -0.002\n        mean_delta_ece: 0.008\n      alpha_0.1:\n        mean_delta_auroc: -0.005\n        mean_delta_ece: 0.003\n      alpha_1.0:\n        mean_delta_auroc: -0.012\n        mean_delta_ece: -0.002\n      alpha_10.0:\n        mean_delta_auroc: -0.028\n        mean_delta_ece: -0.005\n    component_ablation:\n      bce_only:\n        delta_vs_zs: -0.001\n        note: retraining from scratch ~= standard LR\n      bce_plus_sbece:\n        delta_vs_zs: -0.007\n        note: SB-ECE regularization hurts discrimination\n      bce_plus_mmd:\n        delta_vs_zs: -0.005\n        note: MMD inert to slightly harmful\n      full_caclr:\n        delta_vs_zs: -0.01\n        note: combined losses compound harm\n    linear_proj_vs_caclr_delta: 0.048\n    fewshot100_vs_caclr_delta: 0.061\n    implementation_spec:\n      mmd_kernel: Gaussian RBF, bandwidth=median heuristic\n      optimizer: Adam, lr=1e-3, cosine schedule\n      epochs: 50\n      early_stopping: patience=10 on held-out BCE loss\n      initialization: from standard LR solution\n      batch_size: 256\n      mmd_items: same items as BCE (probe_train split)\n      parallel_set_size_range:\n      - 612\n      - 2847\n  result_rationale: 'CaCLR 失败的根本原因：MMD 在 probe logits 空间操作，而 logits 是 1-D（线性 probe\n    的单一输出）。 1-D MMD 只能 match 两个标量分布的 marginal，无法对齐 correctness direction 的方向性结构。 即使\n    marginal logit 分布被 match，EN 和 target 的 conditional distributions P(logit|correct)\n    vs P(logit|incorrect) 可能仍然不同——Zhao et al. (2019) 的理论预测得到验证。β 越大，MMD 约束越强， logits\n    被拉向无区分性的 marginal match，discrimination 下降。α 高值时 SB-ECE 正则化 进一步牺牲 AUROC 以换取 calibration\n    改善，但改善微小且不稳定。Component ablation 证实 每个额外 loss component 都是净负面的——base BCE（从 LR solution\n    初始化再微调）已经接近 ZS 性能， 额外优化无正贡献。Linear projection 和 few-shot 都显著优于 CaCLR，因为它们直接利用\n    target-language 信息（parallel pairs 或 labels）而非试图间接 match distributions。 CKA subspace\n    解释（correctness direction 是 low-dimensional language-agnostic subspace） 不成立——如果该\n    subspace 真的存在且 robust，MMD 应该至少能做到无害，但实际上有害， 说明 correctness signal 的跨语言结构比预期更 language-specific。\n\n    '\n  tables:\n  - name: 'Table 3a: CaCLR β Sweep (Qwen3-235B, fixed layer 50% depth, 20 langs mean)'\n    columns:\n    - beta\n    - mean_auroc\n    - delta_vs_zs\n    - pct_langs_improved\n    - pct_langs_harmed\n    rows:\n    - - 0.001\n      - 0.57\n      - -0.003\n      - 30%\n      - 45%\n    - - 0.01\n      - 0.567\n      - -0.006\n      - 25%\n      - 55%\n    - - 0.1\n      - 0.562\n      - -0.011\n      - 15%\n      - 65%\n    - - 1.0\n      - 0.554\n      - -0.019\n      - 10%\n      - 80%\n  - name: 'Table 3b: 5-Way Transfer Condition Comparison (both models × 20 langs,\n      EN-optimal layer)'\n    columns:\n    - condition\n    - mean_auroc\n    - mean_ece\n    - delta_auroc_vs_zs\n    - win_rate_vs_zs\n    rows:\n    - - zero-shot\n      - 0.568\n      - 0.285\n      - —\n      - —\n    - - mean-shift\n      - 0.568\n      - 0.291\n      - 0.0\n      - 0%\n    - - CaCLR_best\n      - 0.558\n      - 0.278\n      - -0.01\n      - 18%\n    - - linear_proj_200\n      - 0.606\n      - 0.248\n      - 0.038\n      - 72%\n    - - fewshot_25\n      - 0.59\n      - 0.262\n      - 0.022\n      - 55%\n    - - fewshot_100\n      - 0.619\n      - 0.235\n      - 0.051\n      - 78%\n  - name: 'Table 3c: CaCLR Component Ablation'\n    columns:\n    - configuration\n    - mean_auroc\n    - delta_vs_zs\n    - note\n    rows:\n    - - BCE only (re-init)\n      - 0.567\n      - -0.001\n      - ≈ ZS baseline\n    - - BCE + SB-ECE (α=0.1)\n      - 0.561\n      - -0.007\n      - ECE gains tiny, AUROC drops\n    - - BCE + MMD (β=0.01)\n      - 0.563\n      - -0.005\n      - MMD inert/harmful\n    - - Full CaCLR (α=0.1, β=0.01)\n      - 0.558\n      - -0.01\n      - compound degradation\n  figures_description:\n  - 'Figure 3a: β sweep curve showing monotonic decrease in mean AUROC as β increases\n    from 0.001 to 1.0. Shaded region = bootstrap 95% CI. All CIs include or fall below\n    zero-shot baseline.'\n  - 'Figure 3b: Per-language ΔAUROC (CaCLR vs ZS) bar chart at best β=0.001. Most\n    bars negative; only 3-4 high-resource languages show marginal positive ΔAUROC\n    within noise margin.'\n  analysis: 'CaCLR 的 negative result 是 worst tier 的核心。β sweep 证实 consistency loss\n    在所有 3 OOM 均为 inert 或 harmful—— 这不是超参选择问题而是方法论层面的失败。1-D MMD 的结构性限制（probe logit\n    空间太低维）加上 conditional distribution mismatch（Zhao et al. 2019）导致 distributional\n    matching 路径被彻底关闭。 与此同时，CKA subspace 解释也不成立（plan_011 将确认），所以\"MMD 失败是因为它只 match\n    marginal 而不 match subspace direction\"这个 elegant 的解释也变成了 post-hoc rationalization——\n    实际上 subspace 本身就不 robust。这是 worst tier 最痛苦的部分：不仅方法失败，解释也失败。 但作为 negative result，reproducibility\n    标准高：完整的 implementation spec、β/α sweep、 component ablation 使社区可以独立验证，避免重复尝试 distributional\n    matching 路径。\n\n    '\n- name: Difficulty-Controlled Decomposition Ablation\n  plan_id: plan_004\n  description: IRT difficulty probes → project out → retrain correctness probes, 10\n    langs × 8 layers × 2 models\n  expected_results:\n    decomp_capability_delta_auroc_mean: -0.003\n    decomp_capability_delta_auroc_range:\n    - -0.015\n    - 0.008\n    random_direction_control_delta_mean: -0.005\n    random_direction_control_delta_range:\n    - -0.018\n    - 0.006\n    difficulty_probe_r2: 0.31\n    decomp_vs_random_paired_test_p: 0.42\n    per_tier_delta:\n      HIGH:\n        mean_delta: -0.002\n        significant_count: 0/4\n      MID:\n        mean_delta: -0.004\n        significant_count: 0/3\n      LOW:\n        mean_delta: -0.003\n        significant_count: 0/3\n  result_rationale: 'Difficulty decomposition 在 worst tier 无实质效果。两个原因：(1) difficulty\n    和 capability 信号在 representation 空间中高度纠缠——IRT difficulty direction 不是一个干净的、可投影去除的独立子空间，\n    而是与 correctness signal 共享大量方差。投影去除 difficulty 后 correctness signal 也被部分损坏， 导致\n    retrained probe 的 transfer 性能与原始相当甚至略差。(2) Random-direction control 产生 同量级的效果（mean\n    delta -0.005 vs -0.003，paired test p=0.42），这意味着观察到的微小变化 主要来自 dimensionality reduction\n    效应而非 difficulty-specific 投影。Difficulty probe 本身 R²=0.31（低于理想值），表明 IRT difficulty\n    在 LLM representation 中的编码不够线性/集中， 使得 linear projection 无法有效捕获它。整个 decomposition\n    framing 在经验层面被否定： transfer 的降解不能归因于 capability-specific component，或者说两个 component\n    不可分。\n\n    '\n  tables:\n  - name: 'Table 4: Difficulty Decomposition Ablation (mean across 2 models)'\n    columns:\n    - lang\n    - resource_tier\n    - original_zs_auroc\n    - after_projection_auroc\n    - delta\n    - random_control_delta\n    - decomp_vs_random_p\n    rows:\n    - - zh\n      - HIGH\n      - 0.658\n      - 0.655\n      - -0.003\n      - -0.006\n      - 0.61\n    - - es\n      - HIGH\n      - 0.67\n      - 0.669\n      - -0.001\n      - -0.004\n      - 0.52\n    - - fr\n      - HIGH\n      - 0.652\n      - 0.649\n      - -0.003\n      - -0.007\n      - 0.38\n    - - de\n      - HIGH\n      - 0.643\n      - 0.642\n      - -0.001\n      - -0.003\n      - 0.71\n    - - hi\n      - MID\n      - 0.552\n      - 0.547\n      - -0.005\n      - -0.008\n      - 0.55\n    - - ru\n      - MID\n      - 0.613\n      - 0.61\n      - -0.003\n      - -0.005\n      - 0.64\n    - - ko\n      - MID\n      - 0.578\n      - 0.572\n      - -0.006\n      - -0.004\n      - 0.48\n    - - tr\n      - MID\n      - 0.532\n      - 0.53\n      - -0.002\n      - -0.006\n      - 0.33\n    - - sw\n      - LOW\n      - 0.504\n      - 0.501\n      - -0.003\n      - -0.005\n      - 0.58\n    - - bn\n      - LOW\n      - 0.512\n      - 0.504\n      - -0.008\n      - -0.007\n      - 0.82\n  figures_description:\n  - 'Figure 4: Paired bar chart comparing delta AUROC after difficulty projection\n    (blue) vs random-direction projection (gray) for each language. Error bars = bootstrap\n    95% CI. All CIs overlap; no language shows meaningful separation between decomposition\n    and random control.'\n  analysis: 'Decomposition 的 null result 与 random-direction control 不可区分（p=0.42），表明投影效应来自\n    dimensionality reduction 而非 difficulty-specific 信号去除。这从根本上否定了 Claim 2 的因果叙述——\n    transfer degradation 不能分解为 difficulty-shared 和 capability-specific 两个可操作的 component。\n    在 worst tier framing 中，这成为 negative result 的一部分：decomposition 是另一条被关闭的路径。\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: Correctness-confidence cosine similarity, 20 langs × 2 architectures,\n    resource-tier 和 language family 分析\n  expected_results:\n    mean_cosine_high_resource: 0.038\n    mean_cosine_mid_resource: 0.065\n    mean_cosine_low_resource: 0.112\n    std_cosine_low_resource: 0.082\n    cosine_range_all:\n    - 0.008\n    - 0.198\n    architecture_agreement_rate: 0.65\n    outlier_langs:\n    - am\n    - yo\n    - my\n  result_rationale: 'Orthogonality 在高资源语言基本成立（cosine < 0.05），复现 Miao & Ungar (2026)\n    的英文发现。 但低资源语言的 cosine similarity 显著升高且方差极大（mean=0.112, std=0.082），部分语言 （am=0.198,\n    yo=0.165, my=0.142）接近打破 orthogonality 假设。这可能是因为低资源语言 的 correctness 和 confidence\n    directions 都更 noisy（probe 本身 selectivity 低——见 plan_013）， 而非真正的非正交结构。Architecture\n    一致性仅 65%：两个架构在 7/20 语言上对 orthogonality 程度 给出矛盾信号，削弱了\"orthogonality is a universal\n    property\"的叙述。 作为 subsection（已从 standalone claim 降级），这些结果增加了复杂性但没有清晰的 takeaway。\n\n    '\n  tables:\n  - name: 'Table 5: Cross-Lingual Orthogonality (Cosine Similarity)'\n    columns:\n    - lang\n    - tier\n    - qwen3_cosine\n    - llama4_cosine\n    - agreement\n    - note\n    rows:\n    - - zh\n      - HIGH\n      - 0.031\n      - 0.028\n      - ✓\n      - ''\n    - - es\n      - HIGH\n      - 0.025\n      - 0.033\n      - ✓\n      - ''\n    - - fr\n      - HIGH\n      - 0.029\n      - 0.041\n      - ✓\n      - ''\n    - - de\n      - HIGH\n      - 0.035\n      - 0.038\n      - ✓\n      - ''\n    - - ja\n      - HIGH\n      - 0.048\n      - 0.052\n      - ✓\n      - ''\n    - - pt\n      - HIGH\n      - 0.027\n      - 0.035\n      - ✓\n      - ''\n    - - it\n      - HIGH\n      - 0.033\n      - 0.039\n      - ✓\n      - ''\n    - - ar\n      - MID\n      - 0.042\n      - 0.058\n      - ✓\n      - ''\n    - - hi\n      - MID\n      - 0.055\n      - 0.072\n      - ✓\n      - ''\n    - - ru\n      - MID\n      - 0.038\n      - 0.045\n      - ✓\n      - ''\n    - - ko\n      - MID\n      - 0.061\n      - 0.048\n      - ✗\n      - direction reversed\n    - - tr\n      - MID\n      - 0.075\n      - 0.068\n      - ✓\n      - ''\n    - - vi\n      - MID\n      - 0.052\n      - 0.082\n      - ✗\n      - magnitude mismatch\n    - - th\n      - MID\n      - 0.088\n      - 0.065\n      - ✗\n      - magnitude mismatch\n    - - sw\n      - LOW\n      - 0.095\n      - 0.108\n      - ✓\n      - elevated\n    - - bn\n      - LOW\n      - 0.082\n      - 0.118\n      - ✗\n      - ''\n    - - am\n      - LOW\n      - 0.198\n      - 0.152\n      - ✓\n      - near non-orthogonal\n    - - yo\n      - LOW\n      - 0.165\n      - 0.128\n      - ✗\n      - ''\n    - - te\n      - LOW\n      - 0.105\n      - 0.092\n      - ✓\n      - ''\n    - - my\n      - LOW\n      - 0.142\n      - 0.118\n      - ✓\n      - elevated\n  figures_description:\n  - 'Figure 5: Box plot of correctness-confidence cosine similarity by resource tier,\n    faceted by architecture. LOW tier shows significantly higher median and wider\n    spread than HIGH/MID. Dashed line at cosine=0.10 marks ''practical orthogonality\n    threshold''.'\n  analysis: 'Orthogonality 作为 subsection 贡献了一个 nuanced finding：该性质是 resource-tier\n    dependent， 低资源语言中不可靠。但在 worst tier 下这个 finding 被 plan_013 的高 artifact rate 进一步削弱——\n    低资源语言的高 cosine 可能反映 probe 本身的 capacity artifact 而非真正的非正交 representation 结构。 Section\n    简化为：\"orthogonality generally holds but becomes unreliable for low-resource languages，\n    where probe validity itself is questionable (Section X).\" 贡献有限。\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer\n    + calibration, 2 models × 20 langs\n  expected_results:\n    en_auroc_lr_mean: 0.726\n    en_auroc_mlp_mean: 0.741\n    mlp_en_advantage: 0.015\n    zs_transfer_lr_mean_degradation: 0.152\n    zs_transfer_mlp_mean_degradation: 0.191\n    mlp_transfer_disadvantage: -0.039\n    lr_better_for_transfer_pct: 0.7\n    ece_lr_mean: 0.242\n    ece_mlp_mean: 0.258\n    selectivity_lr_mean: 0.218\n    selectivity_mlp_mean: 0.235\n  result_rationale: 'MLP 在 EN 上因更高 capacity 而有 +1.5pp AUROC 优势，但跨语言 transfer 时 degradation\n    更大 （-19.1% vs -15.2%），符合\"linear probes transfer better\"假设。然而在 worst tier 下， 这个差异虽然方向正确但\n    effect size 不大（Cohen''s d ≈ 0.3），且 70% 而非 90%+ 的语言 支持 LR > MLP for transfer，因为部分高资源语言中\n    MLP 的额外 capacity 弥补了 transfer 损失。 此外 MLP 的 selectivity 仅比 LR 高 0.017，表明额外 capacity\n    带来的 artifact 风险有限—— 这与 plan_013 的高 artifact rate 形成有趣对比（artifacts 主要来自语言本身而非 probe\n    复杂度）。\n\n    '\n  tables:\n  - name: 'Table 6: Probe Complexity Comparison Summary'\n    columns:\n    - metric\n    - logistic_regression\n    - mlp_2layer\n    - delta\n    - p_value\n    rows:\n    - - EN AUROC (mean)\n      - 0.726\n      - 0.741\n      - 0.015\n      - 0.008\n    - - ZS degradation (mean)\n      - 15.2%\n      - 19.1%\n      - +3.9pp\n      - 0.023\n    - - ZS AUROC (mean)\n      - 0.616\n      - 0.6\n      - -0.016\n      - 0.041\n    - - EN ECE (mean)\n      - 0.242\n      - 0.258\n      - 0.016\n      - 0.065\n    - - Selectivity (mean)\n      - 0.218\n      - 0.235\n      - 0.017\n      - 0.112\n    - - LR better for transfer\n      - 70%\n      - 30%\n      - —\n      - —\n  figures_description:\n  - 'Figure S1 (appendix): Layer-wise EN AUROC for LR vs MLP showing MLP advantage\n    increases with depth. Paired with ZS AUROC showing LR advantage for transfer grows\n    at deep layers.'\n  analysis: 'LR vs MLP 比较方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下，\n    probe complexity 不是主要问题——语言-层级 capacity artifacts 才是。 结论：保持 LR 作为默认，MLP 结果放 appendix。\n\n    '\n- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: Best probes + CaCLR on Belebele 和 MMLU-ProX, 20 languages each, generalization\n    test\n  expected_results:\n    belebele_zs_pass_rate: 0.5\n    belebele_mean_zs_auroc: 0.548\n    belebele_vs_globalmmlu_spearman_rho: 0.72\n    belebele_vs_globalmmlu_mean_auroc_delta: -0.024\n    mmlupx_zs_pass_rate: 0.55\n    mmlupx_mean_zs_auroc: 0.562\n    mmlupx_vs_globalmmlu_spearman_rho: 0.78\n    caclr_belebele_delta_vs_zs: -0.013\n    caclr_mmlupx_delta_vs_zs: -0.008\n    linear_proj_belebele_delta: 0.031\n    linear_proj_mmlupx_delta: 0.035\n  result_rationale: 'Belebele 的 reading comprehension 格式与 MCQA correctness probing\n    的 mismatch 导致更低的 pass rate。 MMLU-ProX 与 GlobalMMLU 更接近（同为知识 MCQA）所以 correlation\n    更高。CaCLR 在两个 benchmark 上 同样失败甚至更差——distribution mismatch 在 out-of-distribution\n    数据上放大。 Linear projection 仍有正增益但幅度小于 GlobalMMLU——cross-benchmark generalization\n    有衰减。 整体 pattern：在 worst tier 下 generalization 弱化了已经微弱的 positive findings， reinforcing\n    negative result narrative。Belebele 的低 pass rate 尤其令人担忧—— correctness probe 的概念可能不\n    generalize beyond MCQA knowledge questions。\n\n    '\n  tables:\n  - name: 'Table 7: Cross-Benchmark Generalization'\n    columns:\n    - benchmark\n    - zs_pass_rate\n    - mean_zs_auroc\n    - caclr_delta\n    - linproj_delta\n    - correlation_with_globalmmlu\n    rows:\n    - - GlobalMMLU\n      - 0.575\n      - 0.572\n      - -0.01\n      - 0.038\n      - —\n    - - Belebele\n      - 0.5\n      - 0.548\n      - -0.013\n      - 0.031\n      - 0.72\n    - - MMLU-ProX\n      - 0.55\n      - 0.562\n      - -0.008\n      - 0.035\n      - 0.78\n  figures_description:\n  - 'Figure S2 (appendix): Scatter plot of per-language ZS AUROC on GlobalMMLU vs\n    Belebele/MMLU-ProX. Moderate positive correlation but visible deviations, especially\n    for low-resource languages.'\n  analysis: 'Cross-benchmark generalization moderate but not strong。Belebele 的低 performance\n    暗示 correctness probing 可能对任务格式敏感。在 worst-tier paper 中这增加了一层 caveat： findings 可能\n    MCQA-specific，generalization to other formats uncertain。\n\n    '\n- name: Quantization Validation Ablation\n  plan_id: plan_010\n  description: W4A16 vs FP16 (Llama), INT4 vs FP16 (Qwen), 5 representative layers,\n    5% data subset\n  expected_results:\n    llama_w4a16_vs_fp16_max_delta_auroc: 0.018\n    llama_w4a16_vs_fp16_mean_delta_auroc: 0.009\n    llama_w4a16_vs_fp16_spearman_rank_preservation: 0.91\n    qwen_int4_vs_fp16_max_delta_auroc: 0.022\n    qwen_int4_vs_fp16_mean_delta_auroc: 0.012\n    qwen_int4_vs_fp16_spearman_rank_preservation: 0.88\n    problematic_layers_count: 2\n  result_rationale: 'Worst tier 下量化 artifacts 不是灾难性的但 non-negligible。W4A16 mean delta\n    0.9pp 和 INT4 mean delta 1.2pp 在多数层可接受，但在 2/5 测试层出现 >1.5pp 偏差—— 特别是在最深层（correctness\n    signal 最集中的地方），quantization 对高频/低方差的 correctness direction 影响更大。Rank preservation\n    88-91% 意味着 per-language ranking 大体保持但不完美。在 worst tier 下这创造了一个 uncomfortable caveat：\n    所有关于深层 probe 的结论都 potentially 受量化影响，但无法做完整的 FP16 实验来确认。 需要在 limitations 中明确讨论。INT4\n    比 W4A16 worse 因为 4-bit weight-only 比 4-bit weight + 16-bit activation 更 aggressive。\n\n    '\n  tables:\n  - name: 'Table 8: Quantization Validation'\n    columns:\n    - model\n    - quant\n    - layer_pct\n    - fp16_auroc\n    - quant_auroc\n    - delta\n    - rank_preserved\n    rows:\n    - - Llama4\n      - W4A16\n      - 20%\n      - 0.648\n      - 0.645\n      - -0.003\n      - ✓\n    - - Llama4\n      - W4A16\n      - 40%\n      - 0.672\n      - 0.665\n      - -0.007\n      - ✓\n    - - Llama4\n      - W4A16\n      - 60%\n      - 0.695\n      - 0.683\n      - -0.012\n      - ✓\n    - - Llama4\n      - W4A16\n      - 80%\n      - 0.708\n      - 0.692\n      - -0.016\n      - ✗ (2 langs swap)\n    - - Llama4\n      - W4A16\n      - 95%\n      - 0.712\n      - 0.694\n      - -0.018\n      - ✗ (3 langs swap)\n    - - Qwen3\n      - INT4\n      - 20%\n      - 0.625\n      - 0.62\n      - -0.005\n      - ✓\n    - - Qwen3\n      - INT4\n      - 40%\n      - 0.668\n      - 0.658\n      - -0.01\n      - ✓\n    - - Qwen3\n      - INT4\n      - 60%\n      - 0.702\n      - 0.688\n      - -0.014\n      - ✗ (1 lang swap)\n    - - Qwen3\n      - INT4\n      - 80%\n      - 0.728\n      - 0.71\n      - -0.018\n      - ✗ (3 langs swap)\n    - - Qwen3\n      - INT4\n      - 95%\n      - 0.738\n      - 0.716\n      - -0.022\n      - ✗ (4 langs swap)\n  figures_description:\n  - 'Figure S3 (appendix): Layer-wise quantization delta plot showing increasing divergence\n    with depth for both models.'\n  analysis: 'Quantization 在深层引入 1-2pp 的系统性偏差。在 worst tier 下这不改变主要结论（negative results\n    不依赖于精确数值），但增加了 limitations section 的内容。Deep layer probe results（包括 EN-optimal\n    layer 的 AUROC）可能被 overestimate 了 ~1pp by quantization loss。\n\n    '\n- name: CKA Cross-Lingual Representation Similarity Analysis\n  plan_id: plan_011\n  description: CKA (linear kernel) EN vs target, all probed layers, 20 langs × 2 models.\n    Simpson's Paradox 验证。\n  expected_results:\n    simpson_partial_rho_qwen: 0.11\n    simpson_partial_p_qwen: 0.31\n    simpson_partial_rho_llama: 0.08\n    simpson_partial_p_llama: 0.42\n    raw_correlation_rho_qwen: -0.28\n    raw_correlation_rho_llama: -0.35\n    raw_correlation_p_qwen: 0.001\n    raw_correlation_p_llama: <0.001\n    same_layer_cross_lang_rho_median: 0.15\n    same_layer_cross_lang_significant_layers: 2/24 (Qwen), 0/12 (Llama)\n    cka_threshold_identifiable: false\n    subspace_angle_consistency: low — angles vary 15-65° across languages at same\n      layer\n    pilot_replication_5lang: partial — Llama rho drops from +0.41 to +0.08 with 20\n      langs\n  result_rationale: '这是 worst tier 最关键的 falsification。5 语言 pilot 中的 Simpson''s Paradox\n    (Llama partial rho=+0.41, p=0.006) 被确认为 small-sample artifact。当 20 语言数据进入分析后：(1)\n    新增的 15 种语言中多数与 CKA-transfer 关系不一致，部分语言（特别是 MID/LOW tier）的 CKA 模式与 pilot 的 5 种语言截然不同——\n    pilot 恰好选中了 CKA 与 transfer 最相关的语言子集（zh, ar 高 CKA + 低 degradation 拉高了相关性）。 (2)\n    Partial correlation controlling for depth 大幅缩水：Qwen rho 从 pilot 的 +0.18 降至 +0.11\n    (仍 n.s.)， Llama rho 从 +0.41 骤降至 +0.08。原因是新增语言打破了\"within-layer CKA predicts transfer\"的模式——\n    同一层内不同语言的 CKA 值差异巨大但 transfer 性能差异不 track CKA。 (3) Same-layer cross-language analysis\n    (n=20 per layer) 是最强检验：median rho=0.15， 仅 2/24 Qwen layers 和 0/12 Llama layers\n    达到显著——CKA 在 within-layer 水平几乎无解释力。 (4) Subspace angle analysis 显示 correctness\n    direction 的跨语言一致性远低于预期—— angles 在 15-65° 范围波动，不支持\"robust low-dimensional language-agnostic\n    subspace\"的说法。 结论：CKA 不提供超越 depth 的解释力，必须从\"geometric analysis\"降级为\"suggestive correlation\"。\n\n    '\n  tables:\n  - name: 'Table 9a: Simpson''s Paradox Full-Scale Validation'\n    columns:\n    - model\n    - raw_rho\n    - raw_p\n    - partial_rho_depth\n    - partial_p\n    - pilot_partial_rho\n    - pilot_partial_p\n    - verdict\n    rows:\n    - - Qwen3-235B\n      - -0.28\n      - 0.001\n      - 0.11\n      - 0.31\n      - +0.18 (n.s.)\n      - 0.274\n      - n.s. → no Simpson's Paradox\n    - - Llama4-Scout\n      - -0.35\n      - <0.001\n      - 0.08\n      - 0.42\n      - +0.41 (sig.)\n      - 0.006\n      - pilot artifact confirmed\n  - name: 'Table 9b: Same-Layer Cross-Language CKA-Transfer Correlation (top 5 layers)'\n    columns:\n    - model\n    - layer\n    - layer_pct\n    - cka_transfer_rho\n    - p_value\n    - n_langs\n    rows:\n    - - Qwen3\n      - 36\n      - 38%\n      - 0.22\n      - 0.35\n      - 20\n    - - Qwen3\n      - 48\n      - 51%\n      - 0.31\n      - 0.18\n      - 20\n    - - Qwen3\n      - 56\n      - 60%\n      - 0.18\n      - 0.45\n      - 20\n    - - Qwen3\n      - 64\n      - 68%\n      - 0.42\n      - 0.065\n      - 20\n    - - Qwen3\n      - 72\n      - 77%\n      - 0.38\n      - 0.098\n      - 20\n    - - Llama4\n      - 16\n      - 33%\n      - 0.12\n      - 0.61\n      - 20\n    - - Llama4\n      - 24\n      - 50%\n      - 0.08\n      - 0.74\n      - 20\n    - - Llama4\n      - 32\n      - 67%\n      - 0.25\n      - 0.29\n      - 20\n    - - Llama4\n      - 40\n      - 83%\n      - 0.15\n      - 0.53\n      - 20\n    - - Llama4\n      - 44\n      - 92%\n      - 0.05\n      - 0.83\n      - 20\n  - name: 'Table 9c: Subspace Angle Analysis (Correctness Direction, EN vs Target)'\n    columns:\n    - lang\n    - tier\n    - qwen3_angle_deg_L56\n    - llama4_angle_deg_L32\n    - note\n    rows:\n    - - zh\n      - HIGH\n      - 18\n      - 22\n      - relatively aligned\n    - - es\n      - HIGH\n      - 15\n      - 19\n      - relatively aligned\n    - - fr\n      - HIGH\n      - 20\n      - 25\n      - ''\n    - - de\n      - HIGH\n      - 22\n      - 28\n      - ''\n    - - ja\n      - HIGH\n      - 35\n      - 41\n      - large angle despite HIGH resource\n    - - ar\n      - MID\n      - 32\n      - 38\n      - ''\n    - - hi\n      - MID\n      - 38\n      - 45\n      - ''\n    - - ko\n      - MID\n      - 28\n      - 35\n      - ''\n    - - tr\n      - MID\n      - 42\n      - 48\n      - ''\n    - - sw\n      - LOW\n      - 52\n      - 58\n      - near orthogonal\n    - - bn\n      - LOW\n      - 48\n      - 55\n      - ''\n    - - am\n      - LOW\n      - 62\n      - 65\n      - correctness direction nearly unrelated\n  figures_description:\n  - 'Figure 6a: CKA heatmap (language × layer) for both models. Shows CKA decline\n    with depth but no clear correspondence to transfer AUROC patterns.'\n  - 'Figure 6b: Scatter plot of partial residuals (CKA residualized on depth vs transfer\n    AUROC residualized on depth) for both models. Diffuse cloud with no visible trend.\n    Annotations show partial rho and p-values.'\n  - 'Figure 6c: Subspace angle distribution (violin plot by resource tier). Clear\n    tier gradient but HIGH tier also shows 15-35° range, undermining ''language-agnostic\n    subspace'' claim.'\n  analysis: 'CKA analysis 的全面失败是 worst tier 的 defining feature。Pilot 的 Simpson''s\n    Paradox 从 Llama rho=+0.41 (p=0.006) 崩溃到 rho=+0.08 (p=0.42)——这是教科书式的 small-sample\n    inflation。 5 语言 pilot 恰好 overrepresented CKA-transfer 关系最强的语言（zh, ar），排除了关系最弱的语言。\n    Subspace angle analysis 进一步否定了\"correctness direction is a robust low-dimensional\n    language-agnostic subspace\"的前提假设：即使 HIGH resource 语言的 angle 也有 15-35° 的 spread，\n    LOW resource 达到 48-65°（近乎不相关）。这意味着 Miao & Ungar (2026) 的 EN-only correctness direction\n    在跨语言场景下不是 language-agnostic 的——这本身是一个重要的 negative finding，值得在 paper 中强调。 CKA 框架从\n    geometric analysis 降级为 descriptive visualization（仅展示 CKA 随 depth 的下降趋势）， 不再承载解释性角色。\n\n    '\n- name: Linear Projection Sensitivity Analysis\n  plan_id: plan_012\n  description: Procrustes alignment with 10/20/50/100/200 parallel pairs, 2 models\n    × 5 layers × 20 langs\n  expected_results:\n    pairs_to_95pct_mean: 142\n    pairs_to_95pct_range:\n    - 85\n    - 198\n    pairs_to_95pct_high_tier: 68\n    pairs_to_95pct_mid_tier: 125\n    pairs_to_95pct_low_tier: 182\n    saturation_curve_r2: 0.82\n    pair_10_mean_auroc: 0.548\n    pair_20_mean_auroc: 0.568\n    pair_50_mean_auroc: 0.588\n    pair_100_mean_auroc: 0.601\n    pair_200_mean_auroc: 0.61\n    procrustes_reversal_threshold: inconsistent — varies by language\n    helps_when_zs_below: ranges from 0.48 to 0.58 across languages\n    hurts_when_zs_above: ranges from 0.55 to 0.68 across languages\n    reversal_overlap_zone:\n    - 0.48\n    - 0.68\n  result_rationale: 'Worst tier 下 linear projection 需要 100-200 pairs（非 50）达到 95% 性能：\n    (1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需要更多数据点来 稳定估计 rotation\n    matrix——50 pairs 在高维空间中 rank-deficient，低资源语言的 parallel pairs 质量更差（翻译质量低→activation\n    噪声→需要更多 pairs 来 average out noise）。 (2) Resource-tier 分层仍然存在（HIGH 68 pairs vs\n    LOW 182 pairs）但 tier 内方差大—— 同一 tier 内语言间差异可达 2-3×（如 zh 需 45 pairs 但 ja 需 95 pairs，都是\n    HIGH）。 (3) Procrustes 效果反转的阈值高度 language-specific：帮助的 ZS AUROC 范围和伤害的范围 有 [0.48,\n    0.68] 的 overlap zone，意味着对同一 ZS AUROC 值，不同语言可能被帮助或伤害。 无法给出单一可操作的阈值——这使得\"practitioners\n    should use linear projection when ZS < X\" 的建议变得不可靠。\n\n    '\n  tables:\n  - name: 'Table 10a: Linear Projection Sample Efficiency (mean across 2 models ×\n      20 langs)'\n    columns:\n    - n_pairs\n    - mean_auroc\n    - pct_of_200pair\n    - std_across_langs\n    - significant_improvement_pct\n    rows:\n    - - 10\n      - 0.548\n      - 68%\n      - 0.065\n      - 25%\n    - - 20\n      - 0.568\n      - 79%\n      - 0.058\n      - 40%\n    - - 50\n      - 0.588\n      - 89%\n      - 0.052\n      - 55%\n    - - 100\n      - 0.601\n      - 95%\n      - 0.048\n      - 65%\n    - - 200\n      - 0.61\n      - 100%\n      - 0.045\n      - 72%\n  - name: 'Table 10b: Pairs to 95% Performance by Resource Tier'\n    columns:\n    - tier\n    - mean_pairs_95pct\n    - min\n    - max\n    - std\n    rows:\n    - - HIGH\n      - 68\n      - 42\n      - 98\n      - 22\n    - - MID\n      - 125\n      - 78\n      - 165\n      - 35\n    - - LOW\n      - 182\n      - 145\n      - 198\n      - 28\n  - name: 'Table 10c: Procrustes Effect Reversal — Inconsistent Thresholds'\n    columns:\n    - lang\n    - tier\n    - zs_auroc\n    - linproj_200_auroc\n    - delta\n    - effect\n    rows:\n    - - am\n      - LOW\n      - 0.475\n      - 0.498\n      - 0.023\n      - helps\n    - - yo\n      - LOW\n      - 0.463\n      - 0.49\n      - 0.027\n      - helps\n    - - sw\n      - LOW\n      - 0.504\n      - 0.518\n      - 0.014\n      - helps\n    - - bn\n      - LOW\n      - 0.512\n      - 0.528\n      - 0.016\n      - helps\n    - - tr\n      - MID\n      - 0.532\n      - 0.548\n      - 0.016\n      - helps\n    - - hi\n      - MID\n      - 0.552\n      - 0.561\n      - 0.009\n      - helps (marginal)\n    - - vi\n      - MID\n      - 0.558\n      - 0.558\n      - 0.0\n      - neutral\n    - - ko\n      - MID\n      - 0.578\n      - 0.575\n      - -0.003\n      - neutral/hurts\n    - - ar\n      - MID\n      - 0.603\n      - 0.598\n      - -0.005\n      - hurts\n    - - ru\n      - MID\n      - 0.624\n      - 0.612\n      - -0.012\n      - hurts\n    - - zh\n      - HIGH\n      - 0.658\n      - 0.641\n      - -0.017\n      - hurts\n    - - es\n      - HIGH\n      - 0.67\n      - 0.65\n      - -0.02\n      - hurts\n    - - ja\n      - HIGH\n      - 0.582\n      - 0.59\n      - 0.008\n      - helps (despite HIGH tier)\n  figures_description:\n  - 'Figure 7a: Saturation curves (n_pairs vs AUROC) faceted by resource tier, with\n    95% threshold marked. HIGH saturates early, LOW saturates late. Per-language thin\n    lines show within-tier variance.'\n  - 'Figure 7b: Scatter plot of ZS AUROC (x) vs linear projection ΔAUROC (y). Shows\n    rough negative trend but wide scatter band. Vertical zone [0.48-0.68] highlighted\n    as ''inconsistent reversal zone'' where both positive and negative deltas occur.'\n  analysis: 'Linear projection 仍是唯一可行方案但实用性大打折扣：(1) 需 100+ pairs 而非 50， 对低资源语言来说 parallel\n    data 本身就是稀缺资源；(2) 效果反转阈值 inconsistent， practitioner 无法事先知道某语言是否会被帮助或伤害。Paper 中只能给出条件性\n    recommendation： \"当 ZS AUROC < 0.50 时大概率有益，> 0.65 时大概率有害，0.50-0.65 区间需要 held-out\n    validation\" ——这比预期的 clean threshold (0.50/0.60) 弱得多。\n\n    '\n- name: Probing Control Tasks (Cross-Lingual Extension)\n  plan_id: plan_013\n  description: Hewitt & Liang control tasks for 20 languages × all probed layers ×\n    2 models, selectivity analysis\n  expected_results:\n    control_artifact_rate_low_resource: 0.42\n    control_artifact_rate_mid_resource: 0.37\n    control_artifact_rate_high_resource: 0.18\n    control_artifact_rate_overall: 0.31\n    selectivity_below_0.05_pct_low: 42%\n    selectivity_below_0.05_pct_mid: 37%\n    selectivity_below_0.05_pct_high: 18%\n    mean_selectivity_en: 0.245\n    mean_selectivity_high: 0.198\n    mean_selectivity_mid: 0.142\n    mean_selectivity_low: 0.085\n    selectivity_vs_zs_auroc_rho: 0.68\n    layers_most_affected: shallow layers (0-30% depth)\n    worst_lang_layer_combos:\n    - am-L0\n    - yo-L4\n    - my-L0\n    - am-L4\n    - yo-L0\n    - te-L8\n  result_rationale: '这是 worst tier 的最强贡献。Control task artifact rate 在低资源语言达 42%，中资源\n    37%， 远超 MVP pilot 的 28%。原因：(1) MVP 的 5 语言中低资源仅 sw 一种，现在 6-7 种低资源语言 暴露了更系统性的问题——am,\n    yo, my 等在 LLM 预训练中极度不足，对应的 representation 缺乏区分性结构，probe 学到的主要是 capacity artifacts\n    而非 correctness signals。 (2) 中资源语言出现 37% artifact rate 是 worst tier 的 signature\n    finding： 这不仅仅是\"低资源语言有问题\"——tr, th, vi 等中资源语言在浅层也有大量 artifacts， 说明 probing methodology\n    在 cross-lingual 场景的可靠性比预期差得多。 (3) Selectivity 与 ZS AUROC 高度相关（rho=0.68），暗示许多看似成功的\n    cross-lingual transfer 结果其实是 capacity artifacts 在目标语言中的 shadow。 这对整个跨语言 probing\n    文献有 field-level implication：任何不包含 control task 检验的 跨语言 probing 研究的结论都值得质疑。这是首次在\n    cross-lingual transfer 场景系统性 应用 selectivity 检验——贡献的 novelty 和 impact 在 worst tier\n    下反而最强。\n\n    '\n  tables:\n  - name: 'Table 11a: Control Task Artifact Rate by Resource Tier and Model'\n    columns:\n    - tier\n    - n_langs\n    - qwen3_artifact_rate\n    - llama4_artifact_rate\n    - combined\n    - selectivity_mean\n    rows:\n    - - HIGH\n      - 7\n      - 16%\n      - 20%\n      - 18%\n      - 0.198\n    - - MID\n      - 7\n      - 35%\n      - 39%\n      - 37%\n      - 0.142\n    - - LOW\n      - 6\n      - 40%\n      - 44%\n      - 42%\n      - 0.085\n    - - ALL\n      - 20\n      - 29%\n      - 33%\n      - 31%\n      - 0.145\n  - name: 'Table 11b: Per-Language Selectivity at EN-Optimal Layer'\n    columns:\n    - lang\n    - tier\n    - real_auroc\n    - permuted_auroc\n    - selectivity\n    - artifact_flag\n    rows:\n    - - en\n      - —\n      - 0.738\n      - 0.49\n      - 0.248\n      - ''\n    - - zh\n      - HIGH\n      - 0.672\n      - 0.498\n      - 0.174\n      - ''\n    - - es\n      - HIGH\n      - 0.681\n      - 0.495\n      - 0.186\n      - ''\n    - - fr\n      - HIGH\n      - 0.663\n      - 0.492\n      - 0.171\n      - ''\n    - - de\n      - HIGH\n      - 0.654\n      - 0.488\n      - 0.166\n      - ''\n    - - ja\n      - HIGH\n      - 0.582\n      - 0.502\n      - 0.08\n      - ''\n    - - pt\n      - HIGH\n      - 0.668\n      - 0.491\n      - 0.177\n      - ''\n    - - it\n      - HIGH\n      - 0.651\n      - 0.494\n      - 0.157\n      - ''\n    - - ar\n      - MID\n      - 0.603\n      - 0.498\n      - 0.105\n      - ''\n    - - hi\n      - MID\n      - 0.561\n      - 0.505\n      - 0.056\n      - ⚠\n    - - ru\n      - MID\n      - 0.624\n      - 0.495\n      - 0.129\n      - ''\n    - - ko\n      - MID\n      - 0.585\n      - 0.501\n      - 0.084\n      - ''\n    - - tr\n      - MID\n      - 0.541\n      - 0.508\n      - 0.033\n      - ⚠\n    - - vi\n      - MID\n      - 0.558\n      - 0.512\n      - 0.046\n      - ⚠\n    - - th\n      - MID\n      - 0.523\n      - 0.498\n      - 0.025\n      - ⚠\n    - - sw\n      - LOW\n      - 0.512\n      - 0.505\n      - 0.007\n      - ⚠⚠\n    - - bn\n      - LOW\n      - 0.519\n      - 0.502\n      - 0.017\n      - ⚠⚠\n    - - am\n      - LOW\n      - 0.482\n      - 0.478\n      - 0.004\n      - ⚠⚠\n    - - yo\n      - LOW\n      - 0.471\n      - 0.465\n      - 0.006\n      - ⚠⚠\n    - - te\n      - LOW\n      - 0.498\n      - 0.488\n      - 0.01\n      - ⚠⚠\n    - - my\n      - LOW\n      - 0.463\n      - 0.458\n      - 0.005\n      - ⚠⚠\n  - name: 'Table 11c: Layers with Artifact Rate > 40%'\n    columns:\n    - model\n    - layer_range\n    - high_artifact_pct\n    - mid_artifact_pct\n    - low_artifact_pct\n    rows:\n    - - Qwen3\n      - L0-L20 (0-21%)\n      - 8%\n      - 48%\n      - 65%\n    - - Qwen3\n      - L24-L48 (26-51%)\n      - 12%\n      - 35%\n      - 52%\n    - - Qwen3\n      - L52-L72 (55-77%)\n      - 18%\n      - 28%\n      - 35%\n    - - Qwen3\n      - L76-L92 (81-98%)\n      - 25%\n      - 32%\n      - 38%\n    - - Llama4\n      - L0-L12 (0-25%)\n      - 12%\n      - 52%\n      - 68%\n    - - Llama4\n      - L16-L28 (33-58%)\n      - 18%\n      - 38%\n      - 48%\n    - - Llama4\n      - L32-L44 (67-92%)\n      - 22%\n      - 30%\n      - 35%\n    - - Llama4\n      - L48 (100%)\n      - 28%\n      - 35%\n      - 40%\n  figures_description:\n  - 'Figure 8a: Heatmap of selectivity (language × layer) for Qwen3-235B. Color scale:\n    red (< 0.05 artifact) to green (> 0.20 genuine). Large red region in bottom-left\n    (low-resource × shallow layers). Mid-resource languages show surprising red patches\n    even at moderate depths.'\n  - 'Figure 8b: Bar chart of artifact rate by resource tier with 95% CI. Error bars\n    computed via bootstrap over languages within each tier. The CI for MID tier overlaps\n    substantially with LOW tier — the artifact problem is not confined to low-resource.'\n  - 'Figure 8c: Scatter plot of selectivity vs ZS AUROC across all language-layer-model\n    combinations. Strong positive correlation (rho=0.68) suggests many ''successful''\n    ZS transfer results are artifacts.'\n  analysis: 'Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact\n    rate 波及中资源语言是 field-level 发现：不是\"低资源语言有问题，审稿人可以忽略\"，而是 \"所有跨语言 probing 研究——包括那些只看中/高资源语言的——都需要\n    selectivity 检验\"。 Selectivity 与 ZS AUROC 的高相关性 (rho=0.68) 尤其尖锐：它暗示 cross-lingual\n    probing 文献中的许多 positive results 可能是 capacity artifacts。这个 finding 独立于 本文的其他所有\n    claims——即使 Pareto, CaCLR, decomposition 全部失败，这个方法论贡献 仍然足以支撑一篇 findings paper。首次在\n    cross-lingual transfer 场景应用 Hewitt & Liang selectivity 框架，发现 artifact 问题远比 monolingual\n    probing 严重——这是 reframe 后 paper 叙事的 structural foundation。\n\n    '\n- name: Gemma 4 31B Dense Pareto Frontier\n  plan_id: plan_008\n  description: Gemma 4 31B Dense (60 layers, FP16), 15 probed layers, 20 langs, camera-ready\n    第三架构\n  expected_results:\n    en_best_auroc: 0.742\n    en_best_layer: 48\n    zs_pass_rate: 0.6\n    global_spearman_rho: -0.22\n    global_spearman_p: 0.045\n    per_lang_significant_count: 4\n    dense_vs_moe_pareto_clarity: moderately clearer but still noisy\n    control_artifact_rate_low: 0.38\n  result_rationale: 'Dense 架构避免了 MoE routing 的 non-monotonic 噪声，global rho marginally\n    significant (p=0.045)——pareto_spearman_rho_significant_archs 从 0 变为 1。但这反而增加了叙述复杂性：\n    Pareto 是 architecture-dependent 的，dense 模型有 moderate tradeoff，MoE 没有。 无法声称 depth-transfer\n    tradeoff 是普遍现象。EN AUROC 0.742 在 worst 范围内。 Control artifact rate 对低资源语言 38%，确认这不是\n    MoE-specific 的问题。 作为 camera-ready 扩展，Gemma 增加了 architecture coverage 但不改变核心叙事。\n\n    '\n  tables:\n  - name: 'Table S1: Gemma 4 31B Dense Pareto Summary'\n    columns:\n    - metric\n    - value\n    rows:\n    - - en_best_auroc\n      - 0.742\n    - - zs_pass_rate\n      - 60% (12/20)\n    - - global_pareto_rho\n      - -0.22 (p=0.045)\n    - - per_lang_significant_rho\n      - 4/20\n    - - control_artifact_rate_low\n      - 38%\n    - - simpson_partial_rho\n      - +0.14 (p=0.22)\n  figures_description:\n  - 'Figure S4 (camera-ready): Gemma 4 Pareto scatter showing cleaner but still noisy\n    frontier vs Qwen3/Llama4.'\n  analysis: 'Gemma dense 提供了 MoE vs dense 的对比：dense 架构的 Pareto 更清晰但仍远非 universal。\n    4/20 语言 per-language significance 比 Qwen3 的 2/20 好但仍是少数。 Simpson''s Paradox 在\n    Gemma 上也不显著 (partial rho=+0.14, p=0.22)。 三架构综合：0-1 个有 significant Pareto，0 个有\n    significant Simpson''s Paradox—— worst tier 叙事的 architecture coverage 从 2 扩展到\n    3 但结论不变。\n\n    '\n- name: Extended Language Coverage (50+ Languages)\n  plan_id: plan_009\n  description: 从 20 扩展到 50+ 语言, camera-ready extension\n  expected_results:\n    total_languages: 52\n    zs_pass_rate_52lang: 0.52\n    control_artifact_rate_low_expanded: 0.45\n    new_langs_with_significant_pareto: 1\n    additional_artifact_langs: 15\n    linear_proj_pairs_to_95pct_expanded_mean: 158\n  result_rationale: '扩展到 50+ 语言后，新增的大部分是 MID/LOW resource 语言。ZS pass rate 从 60% (20\n    langs) 降至 52% (52 langs) 因为新增语言 skew toward lower resource。Control artifact rate\n    在扩展后的低资源组升至 45%——更多极低资源语言被纳入。这进一步强化了 control task finding 的 field-level 意义：近半数低资源跨语言\n    probing 结果是 artifacts。 但扩展语言数不改变核心 negative results——主要增加 statistical power 和\n    coverage。 Linear projection 需要的 pairs 数在扩展后 mean 升至 158 因为更多 hard languages。\n\n    '\n  tables:\n  - name: 'Table S2: 52-Language Summary vs 20-Language Core'\n    columns:\n    - metric\n    - 20_lang\n    - 52_lang\n    - delta\n    rows:\n    - - zs_pass_rate\n      - 60%\n      - 52%\n      - -8pp\n    - - control_artifact_low\n      - 42%\n      - 45%\n      - +3pp\n    - - control_artifact_mid\n      - 37%\n      - 39%\n      - +2pp\n    - - linear_proj_mean_pairs\n      - 142\n      - 158\n      - '+16'\n    - - simpson_partial_rho_max\n      - 0.11\n      - 0.09\n      - '-0.02'\n  figures_description:\n  - 'Figure S5 (camera-ready): World map of ZS AUROC at EN-optimal layer with artifact-flagged\n    languages marked. Large regions (Sub-Saharan Africa, Southeast Asia) dominated\n    by artifact flags.'\n  analysis: 52 语言扩展主要服务于 coverage 和 robustness 声称。 核心结论不变但 control task finding 更加\n    impactful：近半数低资源结果是 artifacts 在 50+ 语言规模下是对跨语言 probing 文献的强警告。\n",
      "numLines": 1984,
      "startLine": 1,
      "totalLines": 1984
    }
  },
  "sourceToolAssistantUUID": "b39e96fb-c558-4442-95fc-4637614c5094",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16 · 2026-05-21T13:19:03.733Z_

````json
{
  "parentUuid": "fc2c39f7-2a8d-4574-a69e-5565dfa2a025",
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
  "uuid": "9a6d1cc8-312f-4a7f-ba98-3ba720c0aa37",
  "timestamp": "2026-05-21T13:19:03.733Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core patterns from 7-8B pilots do not generalize to full-scale models; Pareto frontier is absent or trivial; CKA adds no explanatory power beyond depth; C…",
  "leafUuid": "9a6d1cc8-312f-4a7f-ba98-3ba720c0aa37",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Large-scale cross-lingual correctness probe transfer: worst-case scenario analysis",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5"
}
```

---

### Assistant

_source line 19 · 2026-05-21T13:20:05.371Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for the "worst" tier for each planned experiment. I see there's already a previous version in the dream reports. Let me check the latest one more carefully, and also check what the current experiment plan looks like more carefully.

The user says "对 experiment_plan 中每个 planned 实验展开详细数据" - so I need to cover all experiments with status "planned" in the experiment plan. Let me list them:

1. plan_001 - Qwen3-235B Full Pareto Frontier (planned)
2. plan_002 - Llama 4 Scout Full Pareto Frontier (status shows some attempts but latest is PREPARING, so still planned)


3. plan_003 - CaCLR (planned)
4. plan_004 - Difficulty decomposition (planned)
5. plan_005 - Cross-lingual orthogonality (planned)
6. plan_006 - Probe complexity comparison (planned)
7. plan_007 - Additional benchmark eval (planned)
8. plan_008 - Gemma 4 31B Dense (planned)
9. plan_009 - Extended language coverage (planned, P2)
10. plan_010 - Quantization validation (planned)
11. plan_011 - CKA analysis (planned)
12. plan_012 - Linear projection sensitivity (planned)

So I have 12 planned experiments to generate worst-case scenario data for.

Looking at the previous report, it's quite thorough, but the user wants a fresh version. I should create a comprehensive YAML output with the worst-tier characteristics in mind—thinking through the key metrics like AUROC ranges across architectures, zero-shot transfer performance, Pareto tradeoff prevalence, and CKA correlations to establish realistic worst-case bounds.

Now I need to make sure each experiment includes a result_rationale that explains the underlying mechanisms driving these worst-tier outcomes, and craft a coherent narrative that ties everything together.

The story should position this as a large-scale viability assessment with strong negative findings: CaCLR fundamentally fails to generalize, CKA provides no explanatory power beyond what depth already tells us, the Pareto frontier is either absent or trivial, and decomposition methods don't actually isolate meaningful components.

I should generate predicted data for plan_002 v3 since it's still in preparation, and reference the actual results from plan_013 while extending predictions for its cross-lingual variant. Let me construct the full YAML output with all planned experiments and their detailed metrics.

I need to be precise about which experiments have "planned" status—going through the registry, that's plan_001 through plan_012, while plan_013 is already done so I'll skip it. Each entry needs a name, plan_id, description, expected results with detailed metrics, a rationale explaining why these results fit the worst-tier narrative, data tables, figure descriptions, and analysis sections. This will be a substantial output, so I'm building a coherent worst-tier prediction where the paper gets reframed as demonstrating fundamental limitations rather than positive findings.

Generating YAML output with internally consistent numbers... ~10-11 of 20 (within 8-13 range for combined)
- Pareto: nearly absent, only ~2-4 languages show any tradeoff

For plan_002 (Llama 4 Scout):
- EN best AUROC: ~0.72 
- 48 layers, every 4th = 12 probed layers
- Also MoE
- ZS pass: ~9-10 of 20

For plan_008 (Gemma 4 31B Dense):
- EN best AUROC: ~0.76
- 60 layers, every 4th + final = ~16 probed layers
- Dense architecture - slightly cleaner patterns
- ZS pass: ~11-12 of 20

Mean across 3 architectures for en_auroc: (0.74 + 0.72 + 0.76)/3 = 0.74 ✓ (within 0.72-0.78)

Combined ZS pass rate averages around 10-11 per architecture, which fits the 8-13 target. The mean ZS AUROC drop from English to cross-language is roughly 15 percentage points, sitting comfortably in the 12-20pp range. Pareto tradeoffs remain sparse across language-architecture pairs, appearing in only about 5-15% of cases. Now I'm ready to write this out as a structured YAML document with detailed mechanistic rationales for each finding. improvement I can bring compared to the existing dream report. The previous version was already very detailed. I should:

1. Make the numbers more precisely consistent with the key metric ranges
2. Ensure cross-experiment consistency (e.g., CKA numbers in plan_011 match what plan_001/002/008 imply)
3. More detailed per-experiment tables
4. Better rationales that connect to the specific architectural properties

Let me also think about which experiments have data available from the MVP that I should reference for extrapolation.

MVP data:
- Qwen2.5-7B: EN best 0.7541, ZS pass 4/5, mean-shift ΔAUROC=0
- Llama-3.1-8B: EN best 0.7284, ZS pass 5/5
- plan_013 (Qwen): selectivity concentrated in L20-L27

Now I'm looking at the performance degradation patterns at scale—the 7-8B model behaviors don't necessarily carry over, and I need to account for how zero-shot transfer and English AUROC might shift differently as model size increases. I should also make sure to incorporate the existing comparisons like CORAL and high-dimensional MMD that were already in the previous version, plus account for multi-seed robustness in my CaCLR predictions. Before I write out the full YAML, let me verify the language groupings from the existing version: HIGH tier has 7 languages (zh, es, fr, de, ja, pt, it), MID tier has 5 (ar, hi, ru, ko, tr).

Writing comprehensive YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a6d1cc8-312f-4a7f-ba98-3ba720c0aa37",
  "isSidechain": false,
  "requestId": "req_011CbFnEVF2766isirYo6Va4",
  "type": "assistant",
  "uuid": "968f4e76-3703-488e-b5f5-05e284909e1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdvpqGBc1gaCTKbYYE6Zfd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32447,
      "cache_read_input_tokens": 32355,
      "output_tokens": 26102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26102,
          "cache_read_input_tokens": 32355,
          "cache_creation_input_tokens": 32447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32447
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

_source line 20 · 2026-05-21T13:27:06.240Z_

已读取上一版 worst tier imagined experiments，现在生成更新版，确保与最新 experiment_plan 中所有 planned 实验对齐、指标范围与 worst 定义一致、跨实验数值内部自洽。

```yaml
tier: worst
narrative_guidance: >
  7-8B pilot 的核心模式不推广到全量模型。两个 MoE 架构（Qwen3-235B, Llama 4 Scout）完全没有清晰的
  Pareto frontier——MoE expert routing 打破了 dense model 中 depth→specialization 的单调映射，
  depth-transfer 关系在绝大多数语言为 non-monotonic 或 flat。唯一的 dense 架构（Gemma 4 31B）展现出
  marginal Pareto（global rho=-0.24, p=0.038），但仅 4/20 语言 per-language 显著，且 final-layer
  transfer drop 微不足道（0.8pp），远不及 pilot 的 2-4pp。三架构平均 EN AUROC 0.74，处于 worst 范围中段。
  
  Simpson's Paradox 在 20 语言全量验证中全面崩塌：3 架构的 CKA partial correlation controlling for
  depth 均不显著（max rho=+0.16, min p=0.09），Llama pilot 的 rho=+0.41 被确认为 5 语言 small-sample
  artifact。CKA 提供不了超越 depth 的解释力。Subspace angle analysis 否定了 "correctness direction
  is a robust language-agnostic subspace"——HIGH tier 语言 angle 15-38°，LOW tier 45-65°。
  
  CaCLR 全面失败：β sweep 3 OOM 证实 consistency loss inert 或 harmful；CORAL 和 high-dim MMD (PCA
  d=50/100) 同样失败，将 negative result 从 "MMD-specific" 扩展为 "distributional matching 路径全面
  关闭"。Component ablation 每加一项 loss 都 net negative。
  
  Decomposition 无实质效果，random-direction control 产生同量级 delta（paired test p=0.38），
  difficulty 和 capability 不可分。
  
  Control task analysis 是最强贡献：cross-lingual artifact rate 达 35%（LOW 42%，MID 31%，HIGH 15%），
  首次在跨语言 probing 场景系统性应用 selectivity 检验。Selectivity 与 ZS AUROC 强相关（rho=0.65），
  暗示文献中许多 positive transfer 结果可能是 capacity artifacts。
  
  Linear projection 作为唯一可行方案但需 100+ pairs（非 50），且效果反转阈值 language-specific，
  无法给出单一可操作的 cutoff。
  
  重构为 EACL negative results + methodology paper：(1) control task 方法论警告（field-level 贡献），
  (2) mean-shift 不可能性证明（理论贡献），(3) distributional matching 路径全面关闭（CaCLR + CORAL +
  high-dim MMD 系统性 negative result），(4) linear projection 条件性实用指导（descriptive empirical
  贡献）。Drop Claim 2（decomposition）和 Claim 3（CaCLR method）作为 standalone claims。

imagined_experiments:
  - name: "Qwen3-235B Full Pareto Frontier"
    plan_id: "plan_001"
    description: >
      Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th),
      20 typologically diverse languages, EN correctness probes (LR + MLP),
      5 transfer conditions (zero-shot, mean-shift, linear projection 200 pairs,
      few-shot 25/100, CaCLR).
    expected_results:
      en_best_auroc: 0.741
      en_best_layer: 72
      en_auroc_range: [0.601, 0.741]
      en_best_ece_raw: 0.198
      zs_pass_count_auroc_gt_058: 11
      zs_pass_rate: 0.55
      zs_fail_count: 9
      mean_zs_auroc_all_20: 0.576
      mean_zs_auroc_drop_vs_en_pp: 16.5
      best_zs_auroc:
        zh: 0.668
        es: 0.675
        fr: 0.658
        de: 0.649
        ja: 0.588
        pt: 0.662
        it: 0.645
        ar: 0.608
        hi: 0.567
        ru: 0.621
        ko: 0.591
        tr: 0.548
        vi: 0.562
        th: 0.528
        sw: 0.518
        bn: 0.524
        am: 0.486
        yo: 0.475
        te: 0.502
        my: 0.468
      best_zs_layer:
        zh: 60
        es: 56
        fr: 60
        de: 52
        ja: 48
        pt: 56
        it: 56
        ar: 52
        hi: 44
        ru: 56
        ko: 48
        tr: 40
        vi: 44
        th: 36
        sw: 36
        bn: 40
        am: 32
        yo: 28
        te: 36
        my: 32
      global_spearman_rho_depth_vs_transfer: -0.12
      global_spearman_p: 0.078
      per_lang_spearman:
        zh: { rho: -0.31, p: 0.14 }
        es: { rho: -0.25, p: 0.24 }
        fr: { rho: -0.28, p: 0.18 }
        de: { rho: -0.19, p: 0.38 }
        ja: { rho: 0.18, p: 0.40 }
        pt: { rho: -0.22, p: 0.30 }
        it: { rho: -0.16, p: 0.46 }
        ar: { rho: 0.05, p: 0.82 }
        hi: { rho: -0.41, p: 0.046 }
        ru: { rho: -0.14, p: 0.52 }
        ko: { rho: 0.25, p: 0.24 }
        tr: { rho: -0.08, p: 0.71 }
        vi: { rho: 0.09, p: 0.68 }
        th: { rho: -0.11, p: 0.61 }
        sw: { rho: -0.35, p: 0.09 }
        bn: { rho: -0.12, p: 0.58 }
        am: { rho: 0.14, p: 0.52 }
        yo: { rho: -0.02, p: 0.93 }
        te: { rho: -0.18, p: 0.40 }
        my: { rho: 0.10, p: 0.64 }
      per_lang_significant_negative_rho_count: 1  # hi only
      per_lang_significant_positive_rho_count: 0
      per_lang_nonmonotonic_count: 13
      pareto_tradeoff_prevalence: 0.08  # ~3 lang-arch pairs of ~40 show clear tradeoff
      pareto_depth_transfer_drop_final_layers_pp: 0.6
      mean_shift_delta_auroc_all: 0.0
      transfer_conditions_summary:
        zero_shot: { mean_auroc: 0.576, std: 0.068, delta_vs_zs: 0.0 }
        mean_shift: { mean_auroc: 0.576, std: 0.068, delta_vs_zs: 0.0 }
        linear_proj_200: { mean_auroc: 0.612, std: 0.055, delta_vs_zs: 0.036 }
        fewshot_25: { mean_auroc: 0.598, std: 0.061, delta_vs_zs: 0.022 }
        fewshot_100: { mean_auroc: 0.625, std: 0.049, delta_vs_zs: 0.049 }
    result_rationale: >
      EN best AUROC 0.741 在 worst 范围 [0.72, 0.78] 内——Qwen3-235B 的 22B active parameters
      对 correctness signal 的编码不显著优于 7B pilot（0.754），因为 correctness direction 的信号
      强度主要由 pretraining data 质量和 MCQA 格式暴露量决定，而非模型 scale。INT4 量化引入
      ~1pp 额外损耗。

      ZS pass 11/20 (55%) 处于 worst 范围 [8, 13] 中段。MoE routing 导致不同语言被路由到
      不同 expert 子集，correctness direction 的跨语言一致性被 expert 分化削弱：pilot 中 Qwen2.5-7B
      dense 架构的 4/5 pass 不能外推，因为 dense model 的 shared representation 天然更有利于
      cross-lingual alignment。低资源语言（am, yo, my）的 best ZS AUROC < 0.50，接近 random。

      Global Pareto rho=-0.12 (p=0.078) 仅 marginally significant：depth-transfer tradeoff 在
      MoE 中不成立，因为 expert routing 在不同深度可以 "重置" 语言特异性——L48 的 expert allocation
      可能与 L72 完全不同，打破了 "deeper = more specialized" 的 dense-model 假设。13/20 语言呈现
      non-monotonic 模式（U形、锯齿形、plateau），这是 MoE 的结构性特征而非噪声。仅 hi 达到
      per-language significant negative rho（p=0.046），ko 和 ja 方向反转（deeper helps transfer）。

      Final-layer transfer drop 仅 0.6pp（worst 范围 [0.0, 1.5]），远低于 pilot 的 2-4pp——
      235B MoE 的最深层 expert routing 已经足够 specialized，EN probe 在这些层的 AUROC
      提升本身就很小（L88 vs L72 仅 +0.3pp EN AUROC），所以 transfer drop 也被压缩。

      Mean-shift ΔAUROC ≡ 0 符合已证明的 rank-invariance。Linear projection +3.6pp 和
      few-shot 100 +4.9pp 有中等改善，但 significant improvement 仅覆盖 55-65% 的语言。
    tables:
      - name: "Table 1a: Qwen3-235B Per-Language Pareto (Depth vs ZS-AUROC Spearman ρ)"
        columns: [lang, tier, best_zs_auroc, best_zs_layer, spearman_rho, p_value, pattern]
        rows:
          - [zh, HIGH, 0.668, 60, -0.31, 0.14, "weak negative"]
          - [es, HIGH, 0.675, 56, -0.25, 0.24, "n.s."]
          - [fr, HIGH, 0.658, 60, -0.28, 0.18, "n.s."]
          - [de, HIGH, 0.649, 52, -0.19, 0.38, "n.s."]
          - [ja, HIGH, 0.588, 48, 0.18, 0.40, "non-monotonic U-shape"]
          - [pt, HIGH, 0.662, 56, -0.22, 0.30, "n.s."]
          - [it, HIGH, 0.645, 56, -0.16, 0.46, "n.s."]
          - [ar, MID, 0.608, 52, 0.05, 0.82, "flat"]
          - [hi, MID, 0.567, 44, -0.41, 0.046, "significant negative"]
          - [ru, MID, 0.621, 56, -0.14, 0.52, "n.s."]
          - [ko, MID, 0.591, 48, 0.25, 0.24, "inverted—deeper helps"]
          - [tr, MID, 0.548, 40, -0.08, 0.71, "n.s."]
          - [vi, MID, 0.562, 44, 0.09, 0.68, "flat"]
          - [th, MID, 0.528, 36, -0.11, 0.61, "n.s."]
          - [sw, LOW, 0.518, 36, -0.35, 0.09, "marginal negative"]
          - [bn, LOW, 0.524, 40, -0.12, 0.58, "n.s."]
          - [am, LOW, 0.486, 32, 0.14, 0.52, "non-monotonic"]
          - [yo, LOW, 0.475, 28, -0.02, 0.93, "noisy flat"]
          - [te, LOW, 0.502, 36, -0.18, 0.40, "n.s."]
          - [my, LOW, 0.468, 32, 0.10, 0.64, "non-monotonic"]
      - name: "Table 1b: Qwen3-235B Transfer Conditions Summary (20 langs, EN-optimal layer)"
        columns: [condition, mean_auroc, std, delta_vs_zs, significant_improvement_count]
        rows:
          - [zero-shot, 0.576, 0.068, "—", "—"]
          - [mean-shift, 0.576, 0.068, 0.000, "0/20"]
          - [linear_proj_200, 0.612, 0.055, +0.036, "11/20"]
          - [fewshot_25, 0.598, 0.061, +0.022, "7/20"]
          - [fewshot_100, 0.625, 0.049, +0.049, "13/20"]
    figures_description:
      - >
        Figure 1a: EN AUROC vs best ZS AUROC scatter across 24 layers for Qwen3-235B,
        colored by resource tier. Diffuse cloud without clean Pareto frontier. Non-monotonic
        language trajectories (ja, ko, am, my) highlighted. Annotation: global ρ=-0.12 (p=0.078).
      - >
        Figure 1b: ZS AUROC heatmap (language × probed layer). Irregular MoE-specific
        layer-to-layer variance, no smooth depth gradient. Expert routing artifacts visible
        as 4-layer-period oscillations.
    analysis: >
      Qwen3-235B 的 Pareto frontier 远不如 Qwen2.5-7B pilot 清晰。MoE expert routing 打破了
      dense model 中 depth = specialization 的单调映射。Pilot 的 clear Pareto（L27 EN best 但
      transfer drops 2-4pp vs L24）是 dense 7B model 的特殊现象。仅 1/20 语言达到 per-language
      显著性（hi），且部分语言方向反转——depth-transfer tradeoff 不是普遍现象。对 Claim 1 构成
      严重挑战：不能声称 Qwen 系列存在 consistent Pareto。

  - name: "Llama 4 Scout Full Pareto Frontier"
    plan_id: "plan_002"
    description: >
      Llama 4 Scout (48 layers, 17B-16E MoE, W4A16), 12 probed layers (every 4th),
      20 languages, 5 transfer conditions.
    expected_results:
      en_best_auroc: 0.718
      en_best_layer: 40
      en_auroc_range: [0.615, 0.718]
      en_best_ece_raw: 0.215
      zs_pass_count_auroc_gt_058: 9
      zs_pass_rate: 0.45
      mean_zs_auroc_all_20: 0.562
      mean_zs_auroc_drop_vs_en_pp: 15.6
      best_zs_auroc:
        zh: 0.648
        es: 0.655
        fr: 0.642
        de: 0.635
        ja: 0.562
        pt: 0.648
        it: 0.631
        ar: 0.588
        hi: 0.548
        ru: 0.608
        ko: 0.575
        tr: 0.531
        vi: 0.558
        th: 0.515
        sw: 0.501
        bn: 0.508
        am: 0.472
        yo: 0.458
        te: 0.491
        my: 0.452
      global_spearman_rho_depth_vs_transfer: -0.06
      global_spearman_p: 0.31
      per_lang_significant_negative_rho_count: 0
      per_lang_significant_positive_rho_count: 0
      per_lang_nonmonotonic_count: 8
      pareto_tradeoff_prevalence: 0.05
      pareto_depth_transfer_drop_final_layers_pp: 0.3
      mean_shift_delta_auroc_all: 0.0
      transfer_conditions_summary:
        zero_shot: { mean_auroc: 0.562, std: 0.065, delta_vs_zs: 0.0 }
        mean_shift: { mean_auroc: 0.562, std: 0.065, delta_vs_zs: 0.0 }
        linear_proj_200: { mean_auroc: 0.598, std: 0.052, delta_vs_zs: 0.036 }
        fewshot_25: { mean_auroc: 0.584, std: 0.058, delta_vs_zs: 0.022 }
        fewshot_100: { mean_auroc: 0.611, std: 0.048, delta_vs_zs: 0.049 }
    result_rationale: >
      Llama 4 Scout EN best AUROC 0.718 在 worst 范围低端——active parameters 17B 但 16 experts
      的稀疏激活使得每个 token 实际使用的参数量有限，correctness signal 在 expert 间被稀释。W4A16
      量化额外损耗 ~0.5-1pp。

      ZS pass 9/20 (45%)，比 Qwen3 低因为：(1) Llama 4 Scout 的 multilingual pretraining
      比例可能低于 Qwen3（Qwen 系列历来强调多语言）；(2) 16-expert MoE 的 expert specialization
      程度更高，语言间 representation divergence 更大。MVP 中 Llama-3.1-8B dense 的 5/5 pass
      不推广——8B dense → Scout MoE 的架构变化比 scale change 更根本。

      Global Pareto rho=-0.06 (p=0.31) 完全不显著，0/20 语言 per-language 显著。仅 12 probed
      layers 使 per-language Spearman 功效极低（n=12），但即使考虑 power 问题，effect sizes 也很小
      （max |rho| = 0.38）。Scout 的 expert routing 比 Qwen3 更激进（16 experts vs Qwen3 的
      设计），导致 depth-transfer 关系更加 noisy。

      Final-layer drop 仅 0.3pp——transfer 在 L40-L48 区间几乎 flat，没有 tradeoff 可言。
    tables:
      - name: "Table 2a: Llama 4 Scout Per-Language Pareto Spearman ρ"
        columns: [lang, tier, best_zs_auroc, spearman_rho, p_value]
        rows:
          - [zh, HIGH, 0.648, -0.18, 0.58]
          - [es, HIGH, 0.655, -0.12, 0.71]
          - [fr, HIGH, 0.642, -0.22, 0.49]
          - [de, HIGH, 0.635, -0.08, 0.81]
          - [ja, HIGH, 0.562, 0.32, 0.31]
          - [pt, HIGH, 0.648, -0.15, 0.64]
          - [it, HIGH, 0.631, -0.05, 0.88]
          - [ar, MID, 0.588, 0.22, 0.49]
          - [hi, MID, 0.548, -0.38, 0.22]
          - [ru, MID, 0.608, -0.02, 0.95]
          - [ko, MID, 0.575, 0.35, 0.26]
          - [tr, MID, 0.531, 0.08, 0.81]
          - [vi, MID, 0.558, 0.12, 0.71]
          - [th, MID, 0.515, -0.18, 0.58]
          - [sw, LOW, 0.501, -0.25, 0.43]
          - [bn, LOW, 0.508, -0.08, 0.81]
          - [am, LOW, 0.472, 0.02, 0.95]
          - [yo, LOW, 0.458, -0.12, 0.71]
          - [te, LOW, 0.491, -0.05, 0.88]
          - [my, LOW, 0.452, 0.15, 0.64]
      - name: "Table 2b: Llama 4 Scout Transfer Conditions Summary"
        columns: [condition, mean_auroc, delta_vs_zs, significant_count]
        rows:
          - [zero-shot, 0.562, "—", "—"]
          - [mean-shift, 0.562, 0.000, "0/20"]
          - [linear_proj_200, 0.598, +0.036, "10/20"]
          - [fewshot_25, 0.584, +0.022, "6/20"]
          - [fewshot_100, 0.611, +0.049, "12/20"]
    figures_description:
      - >
        Figure 2: Llama 4 Scout Pareto scatter, same format as Figure 1a. Cloud 更散乱，
        global ρ=-0.06 (p=0.31)。ko (+0.35) 和 ja (+0.32) 方向反转于预期。
    analysis: >
      Llama 4 Scout 确认 MoE 架构的 Pareto 缺失。与 Qwen3 合并看：0 个 MoE 架构在 p<0.05
      展现 Pareto。MVP 中 Llama-3.1-8B 的弱 Pareto 是 dense 架构特有的。两个 MoE 结合表明
      expert routing 是 Pareto 缺失的结构性原因，而非偶然。

  - name: "Gemma 4 31B Dense Pareto Frontier"
    plan_id: "plan_008"
    description: >
      Gemma 4 31B Dense (60 text layers, BF16 无量化), 16 probed layers (every 4th + final),
      20 languages, 5 transfer conditions. Dense vs MoE 对照。
    expected_results:
      en_best_auroc: 0.755
      en_best_layer: 52
      en_auroc_range: [0.618, 0.755]
      en_best_ece_raw: 0.188
      zs_pass_count_auroc_gt_058: 12
      zs_pass_rate: 0.60
      mean_zs_auroc_all_20: 0.585
      mean_zs_auroc_drop_vs_en_pp: 17.0
      best_zs_auroc:
        zh: 0.682
        es: 0.691
        fr: 0.672
        de: 0.665
        ja: 0.598
        pt: 0.678
        it: 0.658
        ar: 0.618
        hi: 0.575
        ru: 0.635
        ko: 0.602
        tr: 0.558
        vi: 0.572
        th: 0.538
        sw: 0.525
        bn: 0.531
        am: 0.492
        yo: 0.481
        te: 0.508
        my: 0.475
      global_spearman_rho_depth_vs_transfer: -0.24
      global_spearman_p: 0.038
      per_lang_significant_negative_rho_count: 4  # zh, fr, hi, sw
      per_lang_significant_positive_rho_count: 0
      per_lang_nonmonotonic_count: 5
      pareto_tradeoff_prevalence: 0.22  # ~9 lang-arch pairs of ~40 total across 3 arch
      pareto_depth_transfer_drop_final_layers_pp: 0.8
      spearman_depth_vs_transfer_rho_positive_langs: 10  # cross-arch combined
      transfer_conditions_summary:
        zero_shot: { mean_auroc: 0.585, std: 0.063, delta_vs_zs: 0.0 }
        mean_shift: { mean_auroc: 0.585, std: 0.063, delta_vs_zs: 0.0 }
        linear_proj_200: { mean_auroc: 0.621, std: 0.051, delta_vs_zs: 0.036 }
        fewshot_25: { mean_auroc: 0.607, std: 0.057, delta_vs_zs: 0.022 }
        fewshot_100: { mean_auroc: 0.634, std: 0.045, delta_vs_zs: 0.049 }
    result_rationale: >
      Gemma 4 31B Dense 是唯一有 marginal Pareto 的架构。Dense 架构没有 expert routing，
      depth→specialization 映射更单调，因此 global rho=-0.24 (p=0.038) 达到 significance。
      4/20 语言 per-language 显著（zh, fr, hi, sw）——全部是负 rho（deeper layers = worse transfer），
      符合 specialization 叙述。
      
      但这反而增加了叙述复杂性：Pareto 是 architecture-dependent 的（dense 有，MoE 没有），
      无法声称是普遍现象。且 final-layer drop 仅 0.8pp——远低于 pilot 的 2-4pp，因为 31B dense
      model 的最深层已经足够 expressive，EN probe 的边际 AUROC 提升很小（L56→L60 仅 +0.4pp），
      相应 transfer 损失也被压缩。
      
      EN AUROC 0.755 略高于两个 MoE（因无量化损耗 + BF16 保留更多信号精度），三架构均值
      (0.741 + 0.718 + 0.755)/3 = 0.738，在 worst 范围 [0.72, 0.78] 内。
      
      ZS pass 12/20 (60%)——三架构最高，因为 Gemma 4 的 multilingual pretraining 可能
      更均衡（Apache 2.0 开源模型通常 training data 更 curated），且无量化损耗。
    tables:
      - name: "Table 3: Gemma 4 31B Dense Pareto Summary"
        columns: [metric, value]
        rows:
          - [en_best_auroc, 0.755]
          - [en_best_layer, "L52 (87% depth)"]
          - [zs_pass_rate, "60% (12/20)"]
          - [global_pareto_rho, "-0.24 (p=0.038)"]
          - [per_lang_significant_rho, "4/20 (zh, fr, hi, sw)"]
          - [final_layer_transfer_drop_pp, 0.8]
          - [control_artifact_rate_LOW, "38%"]
          - [no_quantization_confound, "BF16 — no quantization artifact"]
      - name: "Table 3b: Dense vs MoE Architecture Comparison"
        columns: [metric, "Qwen3 (MoE)", "Llama4 (MoE)", "Gemma4 (Dense)"]
        rows:
          - [en_best_auroc, 0.741, 0.718, 0.755]
          - [global_pareto_rho, "-0.12 (n.s.)", "-0.06 (n.s.)", "-0.24 (p=0.038)"]
          - [per_lang_sig_count, "1/20", "0/20", "4/20"]
          - [non_monotonic_langs, "13/20", "8/20", "5/20"]
          - [final_layer_drop_pp, 0.6, 0.3, 0.8]
          - [zs_pass_rate, "55%", "45%", "60%"]
    figures_description:
      - >
        Figure 3a: Gemma 4 Pareto scatter vs Qwen3/Llama4 (3-panel). Gemma shows
        cleaner negative trend but still substantial scatter. MoE panels show diffuse
        clouds. Visual comparison highlights dense vs MoE structural difference.
      - >
        Figure 3b: Per-language Spearman ρ bar chart across 3 architectures. Gemma
        bars lean negative but most still n.s. MoE bars scattered around zero.
    analysis: >
      Dense vs MoE 对比是 Gemma 最大的贡献：dense 架构确实有 cleaner depth-transfer 关系，
      但 effect size 远小于 pilot 预期。三架构综合 pareto_tradeoff_prevalence ≈ 0.12
      (12% of lang-arch pairs)，在 worst 范围 [0.05, 0.25] 内。
      结论：Pareto 是 architecture-conditional 的，不是 universal finding——这使得
      Claim 1 从 "discovery" 降级为 "architecture-dependent observational note"。

  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: "plan_003"
    description: >
      CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD), β sweep 3 OOM, α sweep,
      component ablation, CORAL comparison, high-dim MMD (PCA d=50/100),
      multi-seed (5 seeds), mixed β criterion. vs 4 baselines,
      3 models × 20 langs.
    expected_results:
      caclr_mean_delta_auroc_vs_zs: -0.008
      caclr_langs_improved_of_20: 4
      caclr_best_beta: "none — all β inert or harmful"
      beta_sweep:
        beta_0.001: { mean_delta_auroc: -0.002, std: 0.016 }
        beta_0.01: { mean_delta_auroc: -0.005, std: 0.019 }
        beta_0.1: { mean_delta_auroc: -0.009, std: 0.023 }
        beta_1.0: { mean_delta_auroc: -0.016, std: 0.028 }
      alpha_sweep:
        alpha_0.01: { delta_auroc: -0.001, delta_ece: +0.006 }
        alpha_0.1: { delta_auroc: -0.004, delta_ece: +0.002 }
        alpha_1.0: { delta_auroc: -0.010, delta_ece: -0.001 }
        alpha_10.0: { delta_auroc: -0.025, delta_ece: -0.004 }
      component_ablation:
        bce_only: { delta_vs_zs: -0.001, note: "≈ ZS baseline" }
        bce_plus_sbece: { delta_vs_zs: -0.005, note: "SB-ECE hurts discrimination" }
        bce_plus_mmd_1d: { delta_vs_zs: -0.004, note: "1-D MMD inert/harmful" }
        bce_plus_mmd_pca50: { delta_vs_zs: -0.006, note: "50-D MMD also fails" }
        bce_plus_mmd_pca100: { delta_vs_zs: -0.008, note: "100-D MMD worse — curse of dimensionality" }
        bce_plus_coral: { delta_vs_zs: -0.005, note: "CORAL fails — second-order alignment insufficient" }
        bce_plus_coral_pca50: { delta_vs_zs: -0.007, note: "high-dim CORAL also fails" }
        full_caclr: { delta_vs_zs: -0.008, note: "compound degradation" }
      multi_seed_std:
        caclr: 0.003
        fewshot_25: 0.008
        fewshot_100: 0.005
        procrustes: 0.002
      mixed_beta_criterion_result: >
        β selected on zh+sw validation matches English-only selection (β=0.001).
        No evidence of systematic bias against cross-lingual benefit.
      five_way_comparison:
        zero_shot: { mean_auroc: 0.574, mean_ece: 0.282 }
        mean_shift: { mean_auroc: 0.574, mean_ece: 0.288 }
        caclr_best: { mean_auroc: 0.566, mean_ece: 0.275 }
        linear_proj_200: { mean_auroc: 0.610, mean_ece: 0.245 }
        fewshot_25: { mean_auroc: 0.596, mean_ece: 0.258 }
        fewshot_100: { mean_auroc: 0.623, mean_ece: 0.232 }
      implementation_spec:
        mmd_kernel: "Gaussian RBF, bandwidth=median heuristic"
        optimizer: "Adam, lr=1e-3, cosine schedule to 1e-5"
        epochs: 50
        early_stopping: "patience=10 on held-out English BCE loss"
        initialization: "from standard LR solution"
        batch_size: 256
        mmd_items: "same items as BCE (probe_train 70% split)"
        parallel_set_size_range: [618, 2852]
    result_rationale: >
      CaCLR 失败的根本原因链：
      
      (1) 1-D MMD 结构性限制：probe logit 是标量，MMD 只能 match 两个 1-D 分布的 marginal。
      即使 marginal 被 match，EN 和 target 的 conditional distributions P(logit|correct) vs
      P(logit|incorrect) 仍然不同——Zhao et al. (2019) 的理论预测在此得到验证。β 越大，logits
      被拉向无区分性的 marginal match，discrimination 下降。
      
      (2) High-dim MMD (PCA d=50/100) 同样失败：curse of dimensionality 使得 Gaussian RBF kernel
      在 50-100 维空间的 MMD estimate 方差极大，有效样本量不足（probe_train ~2000 samples 对
      100 维 MMD 来说 severely underpowered）。d=100 比 d=50 更差，证实这一解释。
      
      (3) CORAL 也失败：second-order alignment（match mean + covariance）比 MMD 更受 conditional
      distribution mismatch 的影响——对齐 marginal moments 不能修复 correctness signal 的
      conditional structure 差异。CORAL 在 domain adaptation 中成功的条件是 covariate shift
      （P(X) changes, P(Y|X) stable），但 cross-lingual correctness probing 违反这一条件
      （P(correct|representation) 在不同语言中不同）。
      
      (4) Component ablation 证实每个额外 loss 都是 net negative：BCE-only retrain ≈ ZS
      baseline（LR solution 初始化后 Adam 微调不改变 optimum），每加一项都引入额外 noise 而
      无 signal。CaCLR 不是超参选择问题而是方法论层面的失败。
      
      (5) Multi-seed 结果稳定（std=0.003），排除了 single-seed 偶然性。Mixed β criterion
      排除了 β selection 对 cross-lingual benefit 的系统性偏见。
      
      综合：distributional matching 路径（MMD + CORAL，low-dim + high-dim）被全面关闭。
      Linear projection 和 few-shot 显著优于 CaCLR，因为它们直接利用 target-language 结构
      信息而非试图间接 match distributions。
    tables:
      - name: "Table 4a: CaCLR β Sweep (3 architectures × 20 langs, EN-optimal layer)"
        columns: [beta, mean_auroc, delta_vs_zs, pct_improved, pct_harmed]
        rows:
          - [0.001, 0.572, -0.002, "30%", "42%"]
          - [0.01, 0.569, -0.005, "25%", "52%"]
          - [0.1, 0.565, -0.009, "18%", "62%"]
          - [1.0, 0.558, -0.016, "12%", "75%"]
      - name: "Table 4b: Distributional Matching Comprehensive Ablation"
        columns: [method, dimensionality, mean_delta_auroc, note]
        rows:
          - ["MMD (logit)", "1-D", -0.004, "marginal match, no conditional alignment"]
          - ["MMD (PCA-50)", "50-D", -0.006, "underpowered MMD in 50-D"]
          - ["MMD (PCA-100)", "100-D", -0.008, "curse of dimensionality"]
          - ["CORAL (logit)", "1-D", -0.005, "second-order alignment insufficient"]
          - ["CORAL (PCA-50)", "50-D", -0.007, "covariance match fails"]
          - ["Linear projection", "full-D Procrustes", +0.036, "learns subspace rotation directly"]
      - name: "Table 4c: 5-Way Transfer Comparison (3 arch × 20 langs)"
        columns: [condition, mean_auroc, mean_ece, delta_auroc_vs_zs, win_rate_vs_zs]
        rows:
          - [zero-shot, 0.574, 0.282, "—", "—"]
          - [mean-shift, 0.574, 0.288, 0.000, "0%"]
          - [CaCLR (best), 0.566, 0.275, -0.008, "20%"]
          - [linear_proj_200, 0.610, 0.245, +0.036, "70%"]
          - [fewshot_25, 0.596, 0.258, +0.022, "52%"]
          - [fewshot_100, 0.623, 0.232, +0.049, "75%"]
    figures_description:
      - >
        Figure 4a: β sweep curve showing monotonic decrease in mean AUROC. Shaded
        95% CI all below or crossing zero-shot baseline. Separate lines for MMD-1D,
        MMD-50D, MMD-100D, CORAL showing all fail.
      - >
        Figure 4b: Per-language ΔAUROC bars at best β=0.001. Most bars negative.
        Only 4 HIGH-resource languages show marginal positive Δ within noise margin.
      - >
        Figure 4c: Distributional matching ablation (MMD vs CORAL × dimensionality).
        All configurations below zero-shot. Linear projection (rightmost) is the only
        positive method. Clean visual separation between distribution-matching
        (all negative) and structure-learning (linear projection, positive).
    analysis: >
      CaCLR 的全面 negative result 是 worst tier 的核心贡献之一。关键升级：CORAL + high-dim MMD
      将 scope 从 "MMD fails" 扩展为 "distributional matching path is closed"。这比仅报告
      1-D MMD 失败有力得多——reviewer 无法反驳说 "换个 kernel/提高维度就行"。
      Distributional matching ablation table (Table 4b) 是该 claim 的 anchor evidence。
      CKA subspace 解释也不成立（plan_011），所以 geometric rationalization 也失败——
      不仅方法失败，elegant 解释也失败。但完整的 implementation spec + sweep + ablation
      确保 reproducibility，使 negative result 可信。

  - name: "Difficulty-Controlled Decomposition Ablation"
    plan_id: "plan_004"
    description: >
      IRT difficulty probes → project out difficulty direction → retrain correctness
      probes on residuals → evaluate transfer. 10 representative languages × 8
      representative layers × 3 models. Random-direction control.
    expected_results:
      decomp_transfer_improvement_pp: 0.2
      decomp_transfer_improvement_range: [-0.8, 1.2]
      random_direction_control_delta_pp: -0.1
      random_direction_control_range: [-1.0, 0.8]
      decomp_vs_random_paired_test_p: 0.38
      difficulty_probe_r2: 0.28
      decomp_langs_showing_clean_separation: 2  # of 10
      per_tier_results:
        HIGH: { mean_delta_pp: 0.3, significant: "0/4", clean_separation: 1 }
        MID: { mean_delta_pp: 0.1, significant: "0/3", clean_separation: 1 }
        LOW: { mean_delta_pp: -0.2, significant: "0/3", clean_separation: 0 }
    result_rationale: >
      Decomposition 在 worst tier 无实质效果，两个层面的失败：
      
      (1) Difficulty direction 在 LLM representation 中编码不够 linear/集中——IRT difficulty
      probe R²=0.28（低），意味着 linear projection 只捕获了 difficulty variance 的 28%。
      剩余 72% 的 difficulty 信息分布在 correctness direction 也占据的子空间中——两者高度
      纠缠，projecting out 28% 的 difficulty 同时损坏了部分 correctness signal。
      
      (2) Random-direction control 产生同量级效果（paired test p=0.38），这是 worst tier
      的 killer finding：观察到的微小 delta 主要来自 dimensionality reduction 效应
      （投影去除任意方向都会改变 probe 性能 ≈ 同量级），而非 difficulty-specific 信号去除。
      
      2/10 语言 "clean separation"（zh, ko）可能是 type-I error 在 10 次检验中的自然出现率。
      LOW tier 3 语言全部 negative delta——它们的 difficulty 和 capability 信号本身就很弱，
      投影去除任何方向只会损失信息。
      
      结论：transfer degradation 不能分解为 difficulty-shared + capability-specific
      两个可操作的 component——Claim 2 被否定，decomposition 从 standalone claim 降级。
    tables:
      - name: "Table 5: Difficulty Decomposition Ablation (3 models mean)"
        columns: [lang, tier, original_zs, after_proj, delta_pp, random_ctrl_delta_pp, paired_p]
        rows:
          - [zh, HIGH, 0.666, 0.670, +0.4, +0.1, 0.45]
          - [es, HIGH, 0.674, 0.676, +0.2, -0.1, 0.58]
          - [fr, HIGH, 0.657, 0.660, +0.3, +0.2, 0.82]
          - [de, HIGH, 0.650, 0.652, +0.2, -0.2, 0.41]
          - [hi, MID, 0.563, 0.565, +0.2, +0.3, 0.91]
          - [ru, MID, 0.621, 0.622, +0.1, -0.2, 0.52]
          - [ko, MID, 0.589, 0.598, +0.9, +0.2, 0.08]
          - [tr, MID, 0.546, 0.540, -0.6, -0.4, 0.65]
          - [sw, LOW, 0.515, 0.510, -0.5, -0.3, 0.71]
          - [bn, LOW, 0.521, 0.519, -0.2, 0.0, 0.68]
    figures_description:
      - >
        Figure 5: Paired bar chart of ΔAUROC after difficulty projection (blue) vs
        random-direction projection (gray). Error bars = bootstrap 95% CI. All CIs
        overlap; no language shows meaningful separation. Vertical dashed line at 0.
    analysis: >
      Decomposition null result 与 random control 不可区分。Claim 2 被否定。
      在 worst tier paper 中这成为另一条被关闭的路径，但不需要大篇幅——
      1 table + 1 figure 在 Section 5.2 用 1 paragraph 报告即可。

  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: "plan_005"
    description: >
      Correctness-confidence cosine similarity, 20 languages × 2 architectures
      (Qwen3 + Llama4), resource-tier 和 language family 分析.
    expected_results:
      mean_cosine_high: 0.035
      mean_cosine_mid: 0.062
      mean_cosine_low: 0.108
      std_cosine_low: 0.078
      cosine_range_all: [0.012, 0.192]
      architecture_agreement_rate: 0.65
      outlier_langs: [am, yo, my]
    result_rationale: >
      Orthogonality 在 HIGH resource 语言成立（cosine < 0.05），复现 Miao & Ungar (2026)。
      但 LOW resource 的 cosine 显著升高且方差大（mean 0.108, std 0.078）——原因不是真正的
      非正交结构，而是两个 probe 都更 noisy：correctness probe selectivity 低（plan_013 控制
      任务发现），confidence probe 同样缺乏区分性信号，两个 noisy direction 的 cosine 自然
      偏离 0。Architecture 一致性仅 65%：7/20 语言两架构给出矛盾信号——可能反映不同 MoE
      routing 对 confidence 编码方式的影响。
      
      作为已降级的 subsection，这些结果增加复杂性但无 clean takeaway。
    tables:
      - name: "Table 6: Correctness-Confidence Orthogonality by Resource Tier"
        columns: [tier, n_langs, mean_cosine, std, min, max, arch_agreement]
        rows:
          - [HIGH, 7, 0.035, 0.012, 0.012, 0.052, "6/7"]
          - [MID, 7, 0.062, 0.025, 0.035, 0.095, "5/7"]
          - [LOW, 6, 0.108, 0.078, 0.042, 0.192, "2/6"]
          - [ALL, 20, 0.065, 0.055, 0.012, 0.192, "13/20"]
    figures_description:
      - >
        Figure S1 (appendix): Box plot of cosine similarity by resource tier, faceted
        by architecture. LOW tier shows higher median and wider spread. Dashed line
        at cosine=0.10.
    analysis: >
      Orthogonality 作为 subsection 贡献有限。LOW tier 的高 cosine 可能是 probe noise
      而非真 non-orthogonality（control task artifact rate 42% in LOW tier）。
      简化为 1 paragraph + 1 table 在 supporting evidence 小节。

  - name: "Probe Complexity Comparison"
    plan_id: "plan_006"
    description: >
      Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer
      degradation + calibration, 3 models × 20 languages.
    expected_results:
      en_auroc_lr_mean: 0.738
      en_auroc_mlp_mean: 0.752
      mlp_en_advantage_pp: 1.4
      zs_transfer_degradation_lr_pp: 15.8
      zs_transfer_degradation_mlp_pp: 19.4
      mlp_transfer_disadvantage_pp: 3.6
      lr_better_for_transfer_pct: 0.72
      ece_lr_mean: 0.238
      ece_mlp_mean: 0.252
    result_rationale: >
      MLP 更高 capacity → EN +1.4pp，但跨语言 transfer degradation 更大（-19.4% vs -15.8%），
      符合 "linear probes transfer better" 假设。在 worst tier 下 effect size 中等
      （Cohen's d ≈ 0.35），72% 语言支持 LR。部分 HIGH resource 语言中 MLP 额外 capacity
      弥补了 transfer loss。结论方向正确但不 dramatic——LR 作为默认 choice 被 confirm，
      MLP 结果放 appendix。
    tables:
      - name: "Table S2: Probe Complexity Comparison"
        columns: [metric, logistic_regression, mlp_2layer, delta, p_value]
        rows:
          - ["EN AUROC", 0.738, 0.752, +0.014, 0.006]
          - ["ZS degradation", "15.8%", "19.4%", "+3.6pp", 0.018]
          - ["ZS AUROC", 0.621, 0.608, -0.013, 0.032]
          - ["EN ECE", 0.238, 0.252, +0.014, 0.058]
          - ["LR better for transfer", "72%", "28%", "—", "—"]
    figures_description:
      - >
        Figure S2 (appendix): Layer-wise EN AUROC for LR vs MLP (upper panel) paired
        with ZS AUROC (lower panel). MLP advantage grows with EN depth; LR advantage
        grows with transfer depth.
    analysis: >
      方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下，probe complexity
      不是主要问题。保持 LR 默认，appendix 报告 MLP 对比。

  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: "plan_007"
    description: >
      Best probes + all transfer conditions on Belebele (20 langs) and MMLU-ProX
      (20 langs). Cross-benchmark generalization test.
    expected_results:
      belebele_zs_pass_rate: 0.45
      belebele_mean_zs_auroc: 0.545
      belebele_vs_globalmmlu_spearman: 0.71
      belebele_mean_delta_vs_globalmmlu: -0.029
      mmlupx_zs_pass_rate: 0.55
      mmlupx_mean_zs_auroc: 0.565
      mmlupx_vs_globalmmlu_spearman: 0.79
      caclr_belebele_delta: -0.015
      caclr_mmlupx_delta: -0.009
      linear_proj_belebele_delta: +0.028
      linear_proj_mmlupx_delta: +0.033
    result_rationale: >
      Belebele (reading comprehension) 与 MCQA correctness probing 的 task mismatch
      导致更低 pass rate。Correctness probe 在 GlobalMMLU 上学到的 "correct answer" signal
      部分依赖于 MCQA-specific format cues（如选项长度、academic domain structure），这些
      在 Belebele 的 reading comprehension 中缺失。MMLU-ProX 与 GlobalMMLU 更接近（同为
      知识 MCQA），correlation 更高。
      
      CaCLR 在 out-of-distribution data 上更差——distribution mismatch 被放大。
      Linear projection 仍正但幅度缩小。
      
      Worst tier 意味着 generalization 弱化了已经微弱的 positive findings，
      暗示 correctness probing 可能 MCQA-specific。
    tables:
      - name: "Table S3: Cross-Benchmark Generalization"
        columns: [benchmark, zs_pass_rate, mean_zs_auroc, caclr_Δ, linproj_Δ, corr_vs_globalmmlu]
        rows:
          - [GlobalMMLU, "57%", 0.574, -0.008, +0.036, "—"]
          - [Belebele, "45%", 0.545, -0.015, +0.028, 0.71]
          - [MMLU-ProX, "55%", 0.565, -0.009, +0.033, 0.79]
    figures_description:
      - >
        Figure S3 (appendix): Per-language ZS AUROC scatter: GlobalMMLU vs Belebele
        and GlobalMMLU vs MMLU-ProX. Moderate positive correlation with visible
        deviations for low-resource languages.
    analysis: >
      Cross-benchmark generalization moderate。Belebele 低 performance 暗示 correctness
      probing 对 task format 敏感——在 worst tier paper 中增加一层 caveat。
      放 appendix 作为 generalization check。

  - name: "Quantization Validation Ablation"
    plan_id: "plan_010"
    description: >
      (a) W4A16 vs FP16 for Llama 4 Scout, 5 representative layers, 5% data subset;
      (b) INT4 vs FP16 for Qwen3-235B, 5 representative layers, 5% data subset.
    expected_results:
      llama_w4a16_vs_fp16:
        mean_delta_auroc: 0.008
        max_delta_auroc: 0.016
        rank_preservation: 0.92
      qwen_int4_vs_fp16:
        mean_delta_auroc: 0.011
        max_delta_auroc: 0.021
        rank_preservation: 0.89
      problematic_layers: 2  # deep layers with >1.5pp deviation
      gemma_note: "BF16, no quantization — serves as quantization-free control"
    result_rationale: >
      Quantization artifacts 不灾难性但 non-negligible。深层（80-95% depth）受影响最大，
      因为 correctness signal 在这些层最集中，而高频/低方差的 correctness direction 对
      quantization noise 更敏感。INT4 (Qwen) 比 W4A16 (Llama) 更aggressive，所以
      delta 更大。Rank preservation 88-92% 意味着 per-language ranking 大体保持但不完美。
      
      Worst tier 下这创造一个 caveat：深层 probe 结论 potentially 受量化影响。
      Gemma 4 BF16 无量化，提供了 quantization-free 的 architecture 数据点。
    tables:
      - name: "Table S4: Quantization Validation"
        columns: [model, quant, layer_pct, fp16_auroc, quant_auroc, delta, rank_ok]
        rows:
          - [Llama4, W4A16, "20%", 0.650, 0.647, -0.003, "✓"]
          - [Llama4, W4A16, "40%", 0.675, 0.668, -0.007, "✓"]
          - [Llama4, W4A16, "60%", 0.698, 0.688, -0.010, "✓"]
          - [Llama4, W4A16, "80%", 0.710, 0.696, -0.014, "✗ (2 swaps)"]
          - [Llama4, W4A16, "95%", 0.715, 0.699, -0.016, "✗ (3 swaps)"]
          - [Qwen3, INT4, "20%", 0.628, 0.623, -0.005, "✓"]
          - [Qwen3, INT4, "40%", 0.672, 0.662, -0.010, "✓"]
          - [Qwen3, INT4, "60%", 0.705, 0.692, -0.013, "✗ (1 swap)"]
          - [Qwen3, INT4, "80%", 0.730, 0.714, -0.016, "✗ (3 swaps)"]
          - [Qwen3, INT4, "95%", 0.741, 0.720, -0.021, "✗ (4 swaps)"]
    figures_description:
      - >
        Figure S4 (appendix): Layer-wise quantization delta for both models. Monotonic
        increase in delta with depth. Horizontal dashed line at 1.5pp threshold.
    analysis: >
      Quantization 在深层引入 1-2pp 偏差，不改变主要 negative result 结论
      （negative results 不依赖精确数值），但增加 limitations 内容。
      Gemma BF16 作为 quantization-free control 点使得 Gemma 的结果最可信。

  - name: "CKA Cross-Lingual Representation Similarity Analysis"
    plan_id: "plan_011"
    description: >
      CKA (linear kernel) EN vs target, all probed layers, 20 langs × 3 models.
      Simpson's Paradox full-scale validation. Partial correlation controlling
      for depth. Same-layer cross-language analysis. Subspace angle analysis.
    expected_results:
      simpson_paradox_confirmed_of_3_arch: 0
      partial_correlations:
        qwen3: { rho: 0.11, p: 0.28, bootstrap_ci: [-0.08, 0.29] }
        llama4: { rho: 0.06, p: 0.45, bootstrap_ci: [-0.12, 0.24] }
        gemma4: { rho: 0.16, p: 0.09, bootstrap_ci: [-0.02, 0.33] }
      raw_correlations:
        qwen3: { rho: -0.32, p: "<0.001" }
        llama4: { rho: -0.38, p: "<0.001" }
        gemma4: { rho: -0.29, p: "<0.001" }
      same_layer_cross_lang_analysis:
        qwen3_significant_layers: "2/24"
        llama4_significant_layers: "0/12"
        gemma4_significant_layers: "1/16"
        median_rho: 0.14
      subspace_angle:
        high_tier_range_deg: [15, 38]
        mid_tier_range_deg: [28, 52]
        low_tier_range_deg: [42, 65]
        consistency_across_layers: "low — within-language angle std 8-15° across layers"
      pilot_replication:
        llama_pilot_rho: 0.41
        llama_fullscale_rho: 0.06
        verdict: "pilot artifact confirmed"
    result_rationale: >
      这是 worst tier 的 defining falsification。
      
      5 语言 pilot 的 Simpson's Paradox 被 20 语言全量数据否定：
      
      (1) Llama partial rho 从 +0.41 (p=0.006) 骤降至 +0.06 (p=0.45)。原因：pilot 的 5 语言
      恰好 overrepresented CKA-transfer 相关性最强的语言（zh, ar 有高 CKA + 低 degradation），
      排除了关系最弱的语言。15 种新增语言中 MID/LOW tier 的 CKA 模式与 pilot 语言截然不同——
      这些语言的 CKA 虽然也随 depth 下降，但下降斜率和 transfer degradation 之间没有一致的
      within-layer 关系。
      
      (2) Qwen3 rho=+0.11 (p=0.28) 在 pilot 就不显著（+0.18, p=0.274），全量数据只是确认。
      Gemma4 rho=+0.16 (p=0.09) 是最接近显著的，但 bootstrap CI 跨零（[-0.02, 0.33]），
      不能依赖。
      
      (3) Same-layer cross-language analysis（n=20 per layer，最强检验）：median rho=0.14，
      仅 3/52 层 significant——CKA 在 within-layer 水平几乎无预测力。在同一层中，不同语言
      的 CKA 差异巨大但 transfer AUROC 差异不 track CKA。
      
      (4) Subspace angle analysis 否定 "correctness direction is a robust language-agnostic
      subspace"：HIGH tier 15-38°（不是近乎平行），LOW tier 42-65°（近乎 orthogonal）。
      Angle 在同一语言的不同层之间也有 8-15° 的标准差——correctness direction 不仅跨语言
      不一致，在同一语言内也随 depth 漂移。
      
      结论：CKA 不提供超越 depth 的解释力。从 "geometric analysis" 降级为
      "suggestive correlation"——仅保留 CKA heatmap 作为 descriptive visualization。
    tables:
      - name: "Table 7a: Simpson's Paradox Full-Scale Validation"
        columns: [model, raw_rho, raw_p, partial_rho, partial_p, pilot_rho, pilot_p, verdict]
        rows:
          - [Qwen3-235B, -0.32, "<0.001", +0.11, 0.28, "+0.18 (n.s.)", 0.274, "n.s. confirmed"]
          - [Llama4-Scout, -0.38, "<0.001", +0.06, 0.45, "+0.41 (sig.)", 0.006, "pilot artifact"]
          - [Gemma4-31B, -0.29, "<0.001", +0.16, 0.09, "N/A", "N/A", "marginal, CI spans 0"]
      - name: "Table 7b: Same-Layer Cross-Language CKA-Transfer Correlation"
        columns: [model, total_layers, significant_layers, median_rho, best_layer_rho, best_p]
        rows:
          - [Qwen3, 24, "2/24", 0.15, 0.40, 0.078]
          - [Llama4, 12, "0/12", 0.08, 0.28, 0.23]
          - [Gemma4, 16, "1/16", 0.18, 0.44, 0.052]
      - name: "Table 7c: Subspace Angle (Correctness Direction, EN vs Target, at ~60% depth)"
        columns: [lang, tier, qwen3_angle, llama4_angle, gemma4_angle]
        rows:
          - [zh, HIGH, "18°", "24°", "16°"]
          - [es, HIGH, "15°", "20°", "14°"]
          - [ja, HIGH, "35°", "42°", "32°"]
          - [ar, MID, "32°", "40°", "30°"]
          - [hi, MID, "38°", "46°", "35°"]
          - [ko, MID, "28°", "36°", "26°"]
          - [tr, MID, "45°", "52°", "42°"]
          - [sw, LOW, "52°", "58°", "48°"]
          - [bn, LOW, "48°", "55°", "45°"]
          - [am, LOW, "62°", "65°", "58°"]
    figures_description:
      - >
        Figure 6a: CKA heatmap (language × layer) for 3 models. Shows CKA decline with
        depth but no clear correspondence to transfer patterns. Color-coded annotations
        marking same-layer significant correlations (rare).
      - >
        Figure 6b: Partial residual scatter (CKA residualized on depth vs transfer AUROC
        residualized on depth) for 3 models. Diffuse clouds with no visible trend.
      - >
        Figure 6c: Subspace angle violin plot by resource tier across 3 architectures.
        Clear tier gradient but HIGH tier also 15-38° range, undermining "language-agnostic
        subspace" claim. LOW tier near orthogonal.
    analysis: >
      CKA 的全面失败从 pilot 的 Simpson's Paradox 标杆发现降级为 "depth confound 在
      raw correlation 中占主导，controlling 后无 signal"。Subspace angle 否定了论文的
      前提假设："correctness direction 是 robust language-agnostic subspace" 不成立。
      CKA 框架从解释性分析降级为描述性可视化——保留 heatmap 但不承载因果叙述。
      3 架构 0/3 Simpson's Paradox confirmed，在 worst 范围 [0, 1] 内。

  - name: "Linear Projection Sensitivity Analysis"
    plan_id: "plan_012"
    description: >
      Procrustes alignment with 10/20/50/100/200 parallel pairs.
      3 models × 5 representative layers × 20 languages.
    expected_results:
      linear_proj_delta_over_zs_low_resource_pp: 2.8
      linear_proj_saturation_pairs_mean: 135
      saturation_by_tier:
        HIGH: { pairs_95pct: 62, range: [38, 92] }
        MID: { pairs_95pct: 118, range: [72, 158] }
        LOW: { pairs_95pct: 175, range: [140, 198] }
      sample_efficiency_curve:
        10_pairs: { mean_auroc: 0.552, pct_of_200: "66%" }
        20_pairs: { mean_auroc: 0.571, pct_of_200: "78%" }
        50_pairs: { mean_auroc: 0.592, pct_of_200: "89%" }
        100_pairs: { mean_auroc: 0.605, pct_of_200: "96%" }
        200_pairs: { mean_auroc: 0.610, pct_of_200: "100%" }
      procrustes_reversal:
        helps_below_zs: "< 0.53 (mostly helps)"
        hurts_above_zs: "> 0.62 (mostly hurts)"
        inconsistent_zone: [0.53, 0.62]
        note: "threshold varies ±0.08 across languages — no single reliable cutoff"
    result_rationale: >
      Worst tier 下 linear projection 需 100-135 pairs 达到 95% performance（非 50）：
      
      (1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需更多数据
      稳定 rotation matrix 估计——50 pairs 在高维空间 rank-deficient。
      
      (2) LOW resource 语言的 parallel pairs 翻译质量低 → activation noise → 需更多
      pairs average out noise。HIGH tier 62 pairs（翻译精确，subspace angle 小）vs
      LOW tier 175 pairs（翻译 noisy，subspace angle 大）。
      
      (3) Effect reversal threshold language-specific：inconsistent zone [0.53, 0.62]
      意味着同一 ZS AUROC 值下不同语言可能被帮助或伤害。例如 ja (HIGH, ZS=0.588) 被
      帮助但 ko (MID, ZS=0.589) 被伤害——差异来自 subspace angle 和翻译质量的交互作用。
      无法给出单一可操作阈值——practitioner recommendation 弱化为 "ZS < 0.50 大概率有益，
      > 0.65 大概率有害，中间区间需 held-out validation"。
      
      低资源语言 delta +2.8pp（worst 范围 [1, 4] 内），仍是唯一可行的 label-free 方案。
    tables:
      - name: "Table 8a: Linear Projection Sample Efficiency (3 arch × 20 langs)"
        columns: [n_pairs, mean_auroc, pct_of_200, std, significant_pct]
        rows:
          - [10, 0.552, "66%", 0.062, "22%"]
          - [20, 0.571, "78%", 0.055, "38%"]
          - [50, 0.592, "89%", 0.049, "52%"]
          - [100, 0.605, "96%", 0.044, "65%"]
          - [200, 0.610, "100%", 0.042, "70%"]
      - name: "Table 8b: Pairs to 95% by Resource Tier"
        columns: [tier, mean, min, max, std]
        rows:
          - [HIGH, 62, 38, 92, 20]
          - [MID, 118, 72, 158, 32]
          - [LOW, 175, 140, 198, 25]
      - name: "Table 8c: Procrustes Effect Direction (200 pairs, selected languages)"
        columns: [lang, tier, zs_auroc, linproj_auroc, delta, effect]
        rows:
          - [am, LOW, 0.483, 0.508, +0.025, helps]
          - [yo, LOW, 0.468, 0.494, +0.026, helps]
          - [sw, LOW, 0.511, 0.528, +0.017, helps]
          - [tr, MID, 0.544, 0.560, +0.016, helps]
          - [hi, MID, 0.560, 0.568, +0.008, marginal]
          - [vi, MID, 0.563, 0.562, -0.001, neutral]
          - [ko, MID, 0.589, 0.582, -0.007, hurts]
          - [ar, MID, 0.606, 0.598, -0.008, hurts]
          - [ru, MID, 0.622, 0.610, -0.012, hurts]
          - [es, HIGH, 0.674, 0.654, -0.020, hurts]
          - [ja, HIGH, 0.588, 0.596, +0.008, helps (despite HIGH)]
    figures_description:
      - >
        Figure 7a: Saturation curves faceted by resource tier, 95% threshold marked.
        Per-language thin lines show within-tier variance. HIGH saturates early, LOW late.
      - >
        Figure 7b: ZS AUROC (x) vs ΔAUROC (y) scatter. Rough negative trend but wide
        scatter band. Shaded inconsistent zone [0.53, 0.62] where both ± deltas occur.
    analysis: >
      Linear projection 是唯一可行 label-free 方案但实用性弱化：需 100+ pairs（非 50），
      effect reversal threshold inconsistent。Paper 给出条件性 recommendation：
      "ZS < 0.50 大概率有益, > 0.65 大概率有害, 中间需 validation"——
      比预期的 clean threshold 弱得多，但对 practitioners 仍有指导价值。

  - name: "Probing Control Tasks — Cross-Lingual Extension"
    plan_id: "plan_013"
    description: >
      Hewitt & Liang control tasks extended to 20 languages × all probed layers × 3 models.
      Selectivity analysis. Multiple selectivity thresholds (0.03, 0.05, 0.10).
      (builds on completed plan_013 EN-only results)
    expected_results:
      cross_lingual_artifact_rate_pct: 35
      artifact_by_tier:
        HIGH: { rate: "15%", selectivity_mean: 0.195 }
        MID: { rate: "31%", selectivity_mean: 0.138 }
        LOW: { rate: "42%", selectivity_mean: 0.082 }
      control_task_selectivity_deep_layers: 0.16
      selectivity_vs_zs_auroc_rho: 0.65
      threshold_sensitivity:
        threshold_003: { artifact_rate: "42%" }
        threshold_005: { artifact_rate: "35%" }
        threshold_010: { artifact_rate: "24%" }
      worst_combos:
        - "am: selectivity 0.004 at EN-opt layer"
        - "yo: selectivity 0.005 at EN-opt layer"
        - "my: selectivity 0.006 at EN-opt layer"
        - "sw: selectivity 0.008 at EN-opt layer"
      mid_resource_surprise:
        tr: { selectivity_at_enopt: 0.031 }
        th: { selectivity_at_enopt: 0.028 }
        vi: { selectivity_at_enopt: 0.042 }
    result_rationale: >
      Cross-lingual artifact rate 35% (overall) 是 worst tier 最强贡献。

      LOW tier 42% artifact rate 的原因：am, yo, my, te 等语言在 LLM pretraining 中
      极度不足（估计 < 0.1% token share），这些语言的 representation 缺乏区分性结构——
      probe 学到的主要是 capacity artifacts（随机 label 也能达到类似 AUROC）。
      Selectivity = real_AUROC - permuted_AUROC 对这些语言仅 0.004-0.008，
      几乎等于 zero information content。

      MID tier 31% artifact rate 是 worst tier 的 signature finding：不仅低资源有问题——
      tr (0.031), th (0.028), vi (0.042) 等中资源语言在 shallow/mid layers 也有大量
      artifacts。原因：这些语言虽然 pretraining 充足，但 correctness-specific signal
      （区分 "模型答对/答错"）在 representation 中的编码弱于语言 identity signal，
      probe 部分地拟合了 language-specific capacity pattern 而非 correctness。

      HIGH tier 15% artifact rate 主要出现在 shallow layers（0-30% depth），
      与 plan_013 completed results 一致（L0-L16 selectivity < 0.12）。

      Selectivity 与 ZS AUROC 的 rho=0.65 是最尖锐的发现：暗示 cross-lingual probing
      文献中许多 "positive transfer" 结果可能是 artifacts——高 ZS AUROC 可能部分反映
      capacity artifacts 而非 genuine correctness signal transfer。

      首次在 cross-lingual transfer 场景系统性应用 Hewitt & Liang selectivity——
      发现 artifact 问题远比 monolingual probing 严重。Field-level implication。
    tables:
      - name: "Table 9a: Cross-Lingual Artifact Rate by Resource Tier (3 models)"
        columns: [tier, n_langs, artifact_rate_thresh_005, selectivity_mean, selectivity_std]
        rows:
          - [HIGH, 7, "15%", 0.195, 0.042]
          - [MID, 7, "31%", 0.138, 0.038]
          - [LOW, 6, "42%", 0.082, 0.035]
          - [ALL, 20, "35%", 0.142, 0.058]
      - name: "Table 9b: Per-Language Selectivity at EN-Optimal Layer (Qwen3)"
        columns: [lang, tier, real_auroc, permuted_auroc, selectivity, flag]
        rows:
          - [en, "—", 0.741, 0.488, 0.253, ""]
          - [zh, HIGH, 0.668, 0.495, 0.173, ""]
          - [es, HIGH, 0.675, 0.492, 0.183, ""]
          - [fr, HIGH, 0.658, 0.490, 0.168, ""]
          - [de, HIGH, 0.649, 0.486, 0.163, ""]
          - [ja, HIGH, 0.588, 0.501, 0.087, ""]
          - [pt, HIGH, 0.662, 0.489, 0.173, ""]
          - [it, HIGH, 0.645, 0.492, 0.153, ""]
          - [ar, MID, 0.608, 0.496, 0.112, ""]
          - [hi, MID, 0.567, 0.503, 0.064, "⚠"]
          - [ru, MID, 0.621, 0.493, 0.128, ""]
          - [ko, MID, 0.591, 0.499, 0.092, ""]
          - [tr, MID, 0.548, 0.517, 0.031, "⚠"]
          - [vi, MID, 0.562, 0.520, 0.042, "⚠"]
          - [th, MID, 0.528, 0.500, 0.028, "⚠"]
          - [sw, LOW, 0.518, 0.510, 0.008, "⚠⚠"]
          - [bn, LOW, 0.524, 0.505, 0.019, "⚠⚠"]
          - [am, LOW, 0.486, 0.482, 0.004, "⚠⚠"]
          - [yo, LOW, 0.475, 0.470, 0.005, "⚠⚠"]
          - [te, LOW, 0.502, 0.492, 0.010, "⚠⚠"]
          - [my, LOW, 0.468, 0.462, 0.006, "⚠⚠"]
      - name: "Table 9c: Selectivity Threshold Sensitivity"
        columns: [threshold, overall_artifact_rate, LOW_rate, MID_rate, HIGH_rate]
        rows:
          - [0.03, "42%", "52%", "40%", "22%"]
          - [0.05, "35%", "42%", "31%", "15%"]
          - [0.10, "24%", "35%", "22%", "8%"]
    figures_description:
      - >
        Figure 8a: Selectivity heatmap (language × layer) for Qwen3-235B. Color scale:
        red (<0.05) → yellow (0.05-0.10) → green (>0.20). Large red region in
        LOW × shallow layers. MID-resource red patches at moderate depths are the
        surprise finding.
      - >
        Figure 8b: Selectivity vs ZS AUROC scatter across all language-layer-model
        combinations. Strong positive correlation (ρ=0.65). Annotation: "Many
        'successful' transfer results fall in the low-selectivity region."
      - >
        Figure 8c: Artifact rate by resource tier with bootstrap 95% CI. MID tier CI
        overlaps substantially with LOW tier — the problem is not confined to
        low-resource languages.
    analysis: >
      Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact rate
      波及中资源语言是 field-level 发现：所有跨语言 probing 研究——包括只看中/高资源的——
      都需要 selectivity 检验。Selectivity-AUROC correlation (ρ=0.65) 暗示文献中许多
      positive results 可能是 artifacts。首次系统性应用 Hewitt & Liang 到 cross-lingual
      场景——这个贡献独立于本文其他所有 claims，即使其他全部失败仍足以支撑 EACL findings paper。

  - name: "Extended Language Coverage (50+ Languages)"
    plan_id: "plan_009"
    description: >
      从 20 扩展到 50+ 语言 (camera-ready extension)。Leverages GlobalMMLU/Belebele
      full language sets。P2 priority。
    expected_results:
      total_languages: 52
      zs_pass_rate_52lang: 0.50
      artifact_rate_low_expanded: 0.45
      artifact_rate_mid_expanded: 0.34
      new_significant_pareto_langs: 2
      linear_proj_saturation_mean_expanded: 155
    result_rationale: >
      扩展到 52 语言后新增大部分是 MID/LOW resource，ZS pass rate 从 57% → 50%
      因为新语言 skew lower resource。Control artifact rate 在扩展 LOW tier 升至 45%
      因为更多极低资源语言纳入。新增语言不改变核心 negative results，主要增加 statistical
      power 和 coverage credibility。Linear projection saturation mean 升至 155 因为
      更多 hard languages。
      
      扩展语言数的主要价值：(1) control task finding 的 scope 更大——"近半数低资源跨语言
      probing 结果是 artifacts" 在 50+ 语言规模下更有说服力；(2) EACL reviewer 可能要求
      更多语言的 coverage；(3) 无量化 Gemma 在 52 语言上的数据最可信。
    tables:
      - name: "Table S5: 52-Language vs 20-Language Summary"
        columns: [metric, 20_lang, 52_lang, delta]
        rows:
          - [zs_pass_rate, "57%", "50%", "-7pp"]
          - [artifact_rate_LOW, "42%", "45%", "+3pp"]
          - [artifact_rate_MID, "31%", "34%", "+3pp"]
          - [linear_proj_mean_pairs, 135, 155, "+20"]
          - [max_partial_rho, 0.16, 0.14, "-0.02"]
    figures_description:
      - >
        Figure S5 (camera-ready): World map of ZS AUROC at EN-optimal layer with
        artifact flags. Sub-Saharan Africa and Southeast Asia dominated by artifact
        flags. Latin-script European cluster relatively clean.
    analysis: >
      52 语言扩展服务于 coverage 和 robustness。核心结论不变但 control task finding
      更 impactful，linear projection guidance 更 granular（更多语言的 tier classification）。

# Cross-experiment consistency checks
cross_experiment_summary:
  en_auroc_best_layer_mean_across_3_arch: 0.738  # (0.741+0.718+0.755)/3, in [0.72,0.78] ✓
  zs_transfer_pass_rate_mean: 10.7  # (11+9+12)/3, in [8,13] ✓
  mean_zs_auroc_drop_vs_en_pp: 16.4  # (16.5+15.6+17.0)/3, in [12,20] ✓
  pareto_tradeoff_prevalence: 0.12  # 1 arch marginal, 2 arch null; ~12% of pairs, in [0.05,0.25] ✓
  pareto_depth_transfer_drop_final_pp: 0.57  # (0.6+0.3+0.8)/3, in [0.0,1.5] ✓
  cka_partial_corr_rho_max: 0.16  # Gemma, in [-0.05,0.18] ✓
  cka_partial_corr_p_min: 0.09  # Gemma, in [0.05,0.5] ✓
  simpson_paradox_confirmed: 0  # of 3, in [0,1] ✓
  caclr_delta_over_zs_mean_pp: -0.8  # in [-1.5,0.5] ✓
  caclr_langs_improved: 4  # of 20, in [2,7] ✓
  linear_proj_delta_low_resource_pp: 2.8  # in [1,4] ✓
  linear_proj_saturation_pairs: 135  # in [80,200] ✓
  decomposition_improvement_pp: 0.2  # in [-1,1.5] ✓
  decomposition_clean_separation: 2  # of 10, in [1,4] ✓
  control_task_selectivity_deep: 0.16  # in [0.1,0.2] ✓
  cross_lingual_artifact_rate: 35  # %, in [25,45] ✓
  spearman_positive_langs: 10  # of 20 across 3 arch, in [8,13] ✓
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "968f4e76-3703-488e-b5f5-05e284909e1e",
  "isSidechain": false,
  "requestId": "req_011CbFnEVF2766isirYo6Va4",
  "type": "assistant",
  "uuid": "593b507e-9877-438d-b053-49edf0d36379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdvpqGBc1gaCTKbYYE6Zfd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32447,
      "cache_read_input_tokens": 32355,
      "output_tokens": 26102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26102,
          "cache_read_input_tokens": 32355,
          "cache_creation_input_tokens": 32447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32447
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core patterns from 7-8B pilots do not generalize to full-scale models; Pareto frontier is absent or trivial; CKA adds no explanatory power beyond depth; C…",
  "leafUuid": "593b507e-9877-438d-b053-49edf0d36379",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Large-scale cross-lingual correctness probe transfer: worst-case scenario analysis",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core patterns from 7-8B pilots do not generalize to full-scale models; Pareto frontier is absent or trivial; CKA adds no explanatory power beyond depth; C…",
  "leafUuid": "593b507e-9877-438d-b053-49edf0d36379",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Large-scale cross-lingual correctness probe transfer: worst-case scenario analysis",
  "sessionId": "62ec8314-8921-4b1d-97d5-5290795266c5"
}
```

---
