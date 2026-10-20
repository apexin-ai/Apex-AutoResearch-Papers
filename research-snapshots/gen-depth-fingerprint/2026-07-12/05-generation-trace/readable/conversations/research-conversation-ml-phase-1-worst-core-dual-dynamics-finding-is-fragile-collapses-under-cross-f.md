# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Core dual dynamics finding is fragile — collapses under cross-family refere

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/d03f4dca-ffac-4ec2-93c7-f5bebc60961e.jsonl`
- **Structured JSON:** [`79331a1f83c51c296c9a.json`](../../sessions/79/79331a1f83c51c296c9a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T22:31:44.057Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T22:31:44.057Z",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Core dual dynamics finding is fragile — collapses under cross-family reference or is primarily a length/vocabulary artifact; depth signal weak at 7B+ scale; must reframe around task formulation + scaling analysis\n核心假设：['Cross-generator leave-one-out macro-F1 poor (<0.58), especially on out-of-family holdouts — model overfits to generator-specific artifacts', 'Entropy_mean drift largely disappears with non-Pythia reference (|ρ|<0.3) — H2 drift was partially a Pythia-specific artifact', 'Length-controlled F1 drops >0.08 — surface feature signal substantially driven by length confound', '7B+ generator shows minimal depth signal (F1 <0.50, near chance for gen-1 vs gen-2+) — fluent generators compress distinguishability', 'Downstream filtering advantage not significant after CI correction — depth-aware and best binary baseline statistically indistinguishable', 'Dual dynamics framing collapses: without robust cross-reference validation, H1/H2 split is a description of one experimental configuration, not a generalizable finding']\n关键指标范围：{'cross_gen_logo_macro_f1': [0.42, 0.58], 'cross_family_ref_entropy_mean_rho': [-0.3, -0.1], 'length_controlled_f1_delta': [-0.15, -0.08], 'full_vs_surface_f1_gap': [0.0, 0.02], 'full_vs_reference_f1_gap': [0.0, 0.04], 'downstream_depth_quality_spearman': [0.15, 0.4], 'depth_filtering_perplexity_improvement_pct': [0, 3], 'generator_7bplus_macro_f1': [0.35, 0.5], 'finer_5class_macro_f1': [0.2, 0.35]}\n叙事方向：Abandon dual dynamics as headline contribution. Reframe paper around two angles that survive: (1) **Task formulation paper** — 'Generation Depth Estimation: A Missing Layer in Synthetic Text Analysis.' The task itself (ordinal depth, not binary) is novel regardless of feature performance. Formalize the task, provide baselines, release benchmark dataset, discuss what makes it hard. (2) **Negative/analytical result on depth signal scaling** — depth signal is strong for small generators but degrades with scale, revealing that distributional drift from recursive generation is partially masked by model fluency. This connects to model collapse literature (larger models collapse slower) and provides empirical evidence for a scale-dependent regime. The perplexity-by-depth monotonic decrease (13.5→1.7) remains robust as a reference-model phenomenon — reposition around 'reference-model perplexity as depth proxy' rather than the full dual dynamics story. Paper becomes: new task + benchmark + scaling analysis + practical baseline. Still targets AAAI/EMNLP — empirical task-definition papers with honest negative findings are publishable, especially with strong related work contextualization (30+ refs in OOD/model-collapse/data-quality). Key: do NOT try to salvage the dual dynamics claim — pivot cleanly.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nfocus: D006 re-dream after framing repositioning. Key changes: (1) contribution explicitly positioned as empirical/conceptual not methodological — features are standard NLL stats, novelty is in problem formulation + dual dynamics finding + application; (2) OOD detection connection acknowledged (RC8); (3) text length confound controlled (plan_013); (4) downstream utility uses OLMo-1B not Pythia-410M to avoid reference model circularity, multiple seeds + CIs required (RC11); (5) 7B+ generator added as P1 (plan_014, RC9); (6) related work must be 30+ references. Verify whether these changes address the structural issues that caused Best=5/Median=5/Worst=4 in previous dream.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that \"reference-model features = robust, surface features = fragile.\" The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are \"better\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: \"fingerprint\" in the paper refers to the full feature vector's combination, not just reference-model features.\n\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\n\n**RC9 — \"Only ≤2.8B generators — does this transfer to frontier scale?\"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.\n\n**RC10 — \"Text length confound\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\n\n**RC11 — \"Downstream utility — single run, no CIs\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\n\n## Contribution Positioning (Dream D006 insight)\nThe contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection\n2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary\n3. **Practical application**: Risk-stratified data curation outperforming binary filtering\n\nDo NOT overclaim \"distributional fingerprinting\" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.\n\nRelated work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).\n\n## Venue Fit\n- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T22:31:44.059Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T22:31:44.059Z",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T22:31:44.076Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Core dual dynamics finding is fragile — collapses under cross-family reference or is primarily a length/vocabulary artifact; depth signal weak at 7B+ scale; must reframe around task formulation + scaling analysis
核心假设：['Cross-generator leave-one-out macro-F1 poor (<0.58), especially on out-of-family holdouts — model overfits to generator-specific artifacts', 'Entropy_mean drift largely disappears with non-Pythia reference (|ρ|<0.3) — H2 drift was partially a Pythia-specific artifact', 'Length-controlled F1 drops >0.08 — surface feature signal substantially driven by length confound', '7B+ generator shows minimal depth signal (F1 <0.50, near chance for gen-1 vs gen-2+) — fluent generators compress distinguishability', 'Downstream filtering advantage not significant after CI correction — depth-aware and best binary baseline statistically indistinguishable', 'Dual dynamics framing collapses: without robust cross-reference validation, H1/H2 split is a description of one experimental configuration, not a generalizable finding']
关键指标范围：{'cross_gen_logo_macro_f1': [0.42, 0.58], 'cross_family_ref_entropy_mean_rho': [-0.3, -0.1], 'length_controlled_f1_delta': [-0.15, -0.08], 'full_vs_surface_f1_gap': [0.0, 0.02], 'full_vs_reference_f1_gap': [0.0, 0.04], 'downstream_depth_quality_spearman': [0.15, 0.4], 'depth_filtering_perplexity_improvement_pct': [0, 3], 'generator_7bplus_macro_f1': [0.35, 0.5], 'finer_5class_macro_f1': [0.2, 0.35]}
叙事方向：Abandon dual dynamics as headline contribution. Reframe paper around two angles that survive: (1) **Task formulation paper** — 'Generation Depth Estimation: A Missing Layer in Synthetic Text Analysis.' The task itself (ordinal depth, not binary) is novel regardless of feature performance. Formalize the task, provide baselines, release benchmark dataset, discuss what makes it hard. (2) **Negative/analytical result on depth signal scaling** — depth signal is strong for small generators but degrades with scale, revealing that distributional drift from recursive generation is partially masked by model fluency. This connects to model collapse literature (larger models collapse slower) and provides empirical evidence for a scale-dependent regime. The perplexity-by-depth monotonic decrease (13.5→1.7) remains robust as a reference-model phenomenon — reposition around 'reference-model perplexity as depth proxy' rather than the full dual dynamics story. Paper becomes: new task + benchmark + scaling analysis + practical baseline. Still targets AAAI/EMNLP — empirical task-definition papers with honest negative findings are publishable, especially with strong related work contextualization (30+ refs in OOD/model-collapse/data-quality). Key: do NOT try to salvage the dual dynamics claim — pivot cleanly.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-fingerprint
focus: D006 re-dream after framing repositioning. Key changes: (1) contribution explicitly positioned as empirical/conceptual not methodological — features are standard NLL stats, novelty is in problem formulation + dual dynamics finding + application; (2) OOD detection connection acknowledged (RC8); (3) text length confound controlled (plan_013); (4) downstream utility uses OLMo-1B not Pythia-410M to avoid reference model circularity, multiple seeds + CIs required (RC11); (5) 7B+ generator added as P1 (plan_014, RC9); (6) related work must be 30+ references. Verify whether these changes address the structural issues that caused Best=5/Median=5/Worst=4 in previous dream.

## paper_framing.md

# Paper Framing — gen-depth-fingerprint

## Target Venue
- Primary: AAAI 2027 (deadline: August 2, 2026)
- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4
- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)

## Core Insight
Non-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).

## Core Claims (3 条，均可证伪)

**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).

**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.

**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.

## Story Spine

**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).

**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.

**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that "reference-model features = robust, surface features = fragile." The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.

**Headline result template**: "On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines."

## Anticipated Reviewer Concerns

**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are "better" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: "fingerprint" in the paper refers to the full feature vector's combination, not just reference-model features.

**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.

**RC2 — "Does this generalize beyond Pythia?"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).

**RC3 — "Is 3-class sufficient? Why not finer-grained?"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.

**RC4 — "How realistic are single-model chains?"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).

**RC5 — "What about human editing / post-processing?"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).

**RC6 — "Ecological validity — continuation vs real web content"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).

**RC8 — "Aren't these just OOD detection features?"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.

**RC9 — "Only ≤2.8B generators — does this transfer to frontier scale?"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.

**RC10 — "Text length confound"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.

**RC11 — "Downstream utility — single run, no CIs"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).

## Contribution Positioning (Dream D006 insight)
The contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:
1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection
2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary
3. **Practical application**: Risk-stratified data curation outperforming binary filtering

Do NOT overclaim "distributional fingerprinting" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.

Related work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).

## Venue Fit
- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.
- EMNLP 2026: Excellent fit — directly addresses special theme "New Missions for NLP Research" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.


## experiment_plan (with registry status)

- id: plan_001
  claim: 2
  name: feature_ablation_and_trend
  description: 'Three-part analysis on existing MVP data (zero new generation): (A)
    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)
    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold
    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across
    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit
    linear regression per feature, report slope + R². (C) Perplexity pre-validation
    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,
    just forward pass). If perplexity varies significantly with depth → Claim 3 signal
    exists.

    '
  priority: P0
  gpu_budget_hours: 1
  deps:
  - mvp-001
  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only
    ≈ full: reframe Claim 2 as "complementary signal" instead of "independent signal",
    narrative shifts to "vocabulary impoverishment as primary depth signal".

    '
  status: planned
- id: plan_002
  claim: 1
  name: cross_generator_evaluation
  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),
    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out
    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths
    = 25K chains.

    '
  priority: P0
  gpu_budget_hours: 20
  deps:
  - plan_001
  notes: 'Only proceed if plan_001 confirms reference features have independent or
    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out
    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance
    inflated by Pythia-1B in training set.

    '
  status: planned
- id: plan_003
  claim: 2
  name: cross_family_reference_model
  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for
    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean
    H2 drift persists with non-Pythia reference (if drift disappears → "dual dynamics"
    is reference-model artifact, not generation-intrinsic). Also verify shape features
    remain H1 across reference models.

    '
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_002
  notes: 'Importance elevated after D005: this is now the key falsification test for
    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the
    entire dual dynamics narrative collapses.

    '
  status: planned
- id: plan_004
  claim: 3
  name: downstream_utility
  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)
    on depth-stratified data subsets. Measure perplexity degradation on held-out test
    set as function of training data depth. Compare depth-aware filtering vs binary
    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap
    CIs. Include sample-count-matched comparison (subsample depth-filtered to match
    binary-filtered count) to control for data size confound.

    '
  priority: P0
  gpu_budget_hours: 20
  deps:
  - plan_002
  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,
    (3) data size confound. All three addressed in updated design.

    '
  status: planned
- id: plan_005
  claim: 1
  name: prompt_type_comparison
  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting
    chains. Tests whether semantic divergence from source correlates with depth signal
    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.

    '
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_001
  status: planned
- id: plan_006
  claim: 1
  name: paraphrastic_comparison
  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison
    with continuation chains. Tests attractor convergence theory — do non-paraphrastic
    chains preserve more depth signal?

    '
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_005
  status: planned
- id: plan_007
  claim: 1
  name: cross_model_chains
  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model
    chains. More realistic scenario — web contamination involves diverse generators.

    '
  priority: P1
  gpu_budget_hours: 12
  deps:
  - plan_002
  status: planned
- id: plan_008
  claim: 1
  name: multi_domain_seeds
  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific
    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5
    depths.

    '
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_002
  status: planned
- id: plan_009
  claim: 1
  name: finer_grained_ordinal
  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through
    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.

    '
  priority: P2
  gpu_budget_hours: 1
  deps:
  - plan_002
  status: planned
- id: plan_010
  claim: 1
  name: human_edit_robustness
  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement
    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of
    random sentences).

    '
  priority: P2
  gpu_budget_hours: 5
  deps:
  - plan_002
  status: planned
- id: plan_011
  claim: 2
  name: ld_score_feature
  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)
    as additional feature. Tests whether character-level features provide complementary
    depth signal.

    '
  priority: P2
  gpu_budget_hours: 2
  deps:
  - plan_001
  status: planned
- id: plan_012
  claim: 1
  name: end_to_end_classifier
  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.
    Compares learned representations vs handcrafted distributional features.

    '
  priority: P2
  gpu_budget_hours: 15
  deps:
  - plan_002
  status: planned
- id: plan_013
  claim:
  - 1
  - 2
  name: text_length_control
  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze
    text length distributions by depth across all generators. (B) Compute length-normalized
    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched
    comparison: subsample to equalize length distributions across depths, re-evaluate
    classifier. If length-controlled F1 drops significantly → surface features were
    tracking length, not depth.

    '
  priority: P0
  gpu_budget_hours: 0.5
  deps:
  - plan_002
  notes: 'Zero new generation — analysis on existing data. Critical confound control
    flagged by dream (all three tiers). Low cost, high impact on paper credibility.

    '
  status: planned
- id: plan_014
  claim: 1
  name: large_scale_generator
  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth
    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current
    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).

    '
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_002
  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth
    signal weaker at scale → honest limitation with analysis. If comparable → strong
    generalization evidence for the paper.

    '
  status: planned


## registry (completed experiments)

- exp_id: mvp-001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    macro_f1: 0.8408
    binary_f1_gen0_vs_gen2plus: 0.8653
    cv_macro_f1: 0.806
    cv_std: 0.013
    gen0_f1: 0.9517
    gen1_f1: 0.7759
    gen2plus_f1: 0.7947
    total_records: 4609
    seeds_used: 995
    skipped: 173
- exp_id: mvp-001-gen-s0
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: mvp-001-gen-s1
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: mvp-001-gen-s2
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: mvp-001-gen-s3
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: plan-001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    note: initial_run_partial_issues_fixed_in_plan-001-fix
    ablation_full_macro_f1: 0.82
    ablation_surface_only_f1: 0.76
    ablation_reference_only_f1: 0.72
- exp_id: plan-001-fix
  name: ''
  status: DONE
  conclusion: success
  metrics:
    full_macro_f1: 0.8204
    reference_only_f1: 0.7187
    surface_only_f1: 0.7628
    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'
    h2_features: entropy_mean, ttr, hapax_ratio
    h1_features: tail_decay, entropy_std, entropy_max, entropy_min
    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72
- exp_id: plan-001-restore
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan-002
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan-002-pythia1b-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    records: 2286
    seeds: 497
    skipped: 91
    wall_time_s: 2296.7
    depth_dist:
      gen0: 497
      gen1: 497
      gen2: 457
      gen3: 429
      gen4: 406
    file: data/pythia-1b/generations_shard0.jsonl
    file_size_mb: 2.5
- exp_id: plan-002-pythia1b-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    records: 2269
    seeds: 498
    skipped: 100
    wall_time_s: 2247.6
    depth_dist:
      gen0: 498
      gen1: 496
      gen2: 455
      gen3: 422
      gen4: 398
    file: data/pythia-1b/generations_shard1.jsonl
    file_size_mb: 2.44
- exp_id: plan-002-olmo2-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    records: 2379
    seeds: 497
    skipped: 47
    wall_time_s: 3885.2
    depth_dist:
      gen0: 497
      gen1: 494
      gen2: 477
      gen3: 461
      gen4: 450
    file: generations_shard0.jsonl
    file_size_mb: 2.68
- exp_id: plan-002-olmo2-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    records: 2334
    seeds: 498
    skipped: 70
    wall_time_s: 4081.2
    depth_dist:
      gen0: 498
      gen1: 494
      gen2: 470
      gen3: 444
      gen4: 428
    file: generations_shard1.jsonl
    file_size_mb: 2.57
- exp_id: plan-002-qwen3-1_7b-s0
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan-002-qwen3-1_7b-s1
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan-002-qwen17b-s0
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan-002-qwen17b-s1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan-002-qwen17b-retry-s0
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan-002-qwen17b-retry-s1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan-002-qwen06b-s0
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan-002-qwen06b-s1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan-002-qwen17b-r2-s0
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan-002-qwen17b-r2-s1
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
  "promptId": "18a191cb-0dd1-43ed-83da-388439f99451",
  "type": "user",
  "uuid": "50a776b5-2fdd-4a63-9af0-043ca0929d19",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T22:31:44.075Z_

```json
{
  "parentUuid": "50a776b5-2fdd-4a63-9af0-043ca0929d19",
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
  "uuid": "e9eda0cd-8303-42b3-a672-78d2d1e6160e",
  "timestamp": "2026-05-14T22:31:44.075Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T22:31:44.075Z_

```json
{
  "parentUuid": "e9eda0cd-8303-42b3-a672-78d2d1e6160e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "82077db1-e097-4dd2-aaf4-3a78864e31fc",
  "timestamp": "2026-05-14T22:31:44.075Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core dual dynamics finding is fragile — collapses under cross-family reference or is primarily a length/vocabulary artifact; depth signal weak at 7B+ scal…",
  "leafUuid": "82077db1-e097-4dd2-aaf4-3a78864e31fc",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation benchmark and negative scaling analysis",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e"
}
```

---

### Assistant

_source line 8 · 2026-05-14T22:32:33.748Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for the "worst" tier scenario for each "planned" experiment in the experiment plan. I need to carefully go through each planned experiment and generate realistic worst-case results with rationales.

Let me identify all planned experiments:
- plan_001: feature_ablation_and_trend (status: planned, but registry shows plan-001 and plan-001-fix as DONE - so this is actually completed, but the plan says "planned". Let me re-read... The experiment_plan shows status: planned for all entries. But the registry shows some as DONE. I think the user wants me to generate imagined results for experiments that are still "planned" in the experiment_plan. 

I'm noticing a discrepancy between the experiment_plan status (all marked "planned") and the registry entries (some marked "DONE"). Since the user specifically asked for planned experiments from the experiment_plan, I'll treat all entries in that plan as the target set, regardless of what the registry shows. The plan itself lists them all as planned, so I'll generate worst-case scenario results for each one. actual metrics. And plan-002 is RUNNING with some sub-experiments done. So for those that are already done, the "imagined" results would need to be consistent with actual results or... no, I think the user wants me to imagine what the worst case would look like for each experiment as if we're predicting forward.

Actually, re-reading more carefully: the user says "对 experiment_plan 中每个 planned 实验展开详细数据" - this means for each experiment in the experiment_plan that has status "planned". All of them show status: planned in the experiment_plan YAML. But the registry shows some are done.

I think the intent is to generate worst-tier predictions for ALL experiments in the plan. The fact that some are done in the registry doesn't change what we're doing - we're generating a complete imagined scenario.

Now I'm mapping out what the worst-case scenario would look like across all experiments. The key assumptions are that cross-generator performance drops significantly below 0.58 macro-F1, entropy correlations weaken substantially when moving away from Pythia models, length-controlled metrics degrade by more than 0.08 points, larger generators fail to capture depth signals, and the downstream filtering advantage disappears after multiple comparison corrections. I'm also setting metric ranges for each key outcome to establish the bounds of this pessimistic scenario. I'm realizing the registry already has actual results for plan_001, so I should use those as ground truth rather than predicting worst-case scenarios. Since all experiments are marked as planned, I'll focus on forecasting the remaining ones based on the existing data point. of them as needing predictions for the worst tier.

But for plan_001, the actual results exist and are quite good (full=0.82, surface=0.76, reference=0.72). Under the worst tier, the remaining experiments would show these initial results were misleading because they were on in-distribution data.

Let me think about this more carefully. The worst tier says the core finding is fragile. So plan_001's results might look okay on the MVP data (single generator, same family reference), but everything falls apart when you test cross-generator, cross-family, length control, etc.

I'll generate predictions for all planned experiments, noting where results are already known and projecting worst-case for the remaining ones.

Now I'm mapping out the worst-case scenario for each remaining experiment: plan_002 would show poor cross-generator performance especially across families, plan_003 would lose the entropy signal with different reference models, plan_004 would show no real downstream advantage after accounting for confidence intervals, plan_005 would only work for continuation chains while other prompt types fail, plan_006 would show paraphrastic and non-paraphrastic approaches performing similarly, plan_007 would see dramatic F1 drops on cross-model chains, and plan_008 would reveal high variance across domains. , some domains show no signal.

plan_009 (finer_grained_ordinal) - Worst case: 5-class F1 ~0.25, barely above chance.

plan_010 (human_edit_robustness) - Worst case: even 5% edits destroy signal.

plan_011 (ld_score_feature) - Worst case: LD-Score doesn't add much, and doesn't clearly follow H2.

plan_012 (end_to_end_classifier) - Worst case: end-to-end slightly beats handcrafted, undermining feature analysis.

plan_013 (text_length_control) - Worst case: length-controlled F1 drops >0.08, surface features were tracking length.

plan_014 (large_scale_generator) - Worst case: 7B+ shows minimal depth signal.

Now I'm structuring the full YAML output with careful attention to each experiment. The worst-case scenario points toward reframing this as a negative results paper focused on task formulation and scaling analysis rather than dual dynamics.

Generating YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82077db1-e097-4dd2-aaf4-3a78864e31fc",
  "isSidechain": false,
  "requestId": "req_011Cb3FiUH6nMrFDR6ATbPpR",
  "type": "assistant",
  "uuid": "1ac1b3d1-a272-447b-a26d-750b89fb2cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HNgLjuNMeoEznaMLarPoo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13118,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15474,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13118
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

_source line 9 · 2026-05-14T22:36:57.914Z_

```yaml
tier: worst
narrative_guidance: >
  Abandon dual dynamics as headline contribution. Reframe paper around two angles that survive:
  (1) Task formulation paper — 'Generation Depth Estimation: A Missing Layer in Synthetic Text Analysis.'
  The task itself (ordinal depth, not binary) is novel regardless of feature performance. Formalize the task,
  provide baselines, release benchmark dataset, discuss what makes it hard.
  (2) Negative/analytical result on depth signal scaling — depth signal is strong for small generators
  but degrades with scale, revealing that distributional drift from recursive generation is partially masked
  by model fluency. Connects to model collapse literature. Perplexity-by-depth monotonic decrease (13.5→1.7)
  remains robust as reference-model phenomenon — reposition around 'reference-model perplexity as depth proxy'
  rather than the full dual dynamics story. Paper becomes: new task + benchmark + scaling analysis + practical baseline.

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      Feature ablation (surface-only vs reference-only vs full) and H1/H2 trend analysis on MVP data.
      Already executed; registry results from plan-001-fix are taken as given. In worst tier, these
      in-distribution results are not wrong but are misleadingly optimistic — the 0.06 full-vs-surface gap
      and the clean H1/H2 split both depend on same-family (Pythia) reference and single-generator setting.
    expected_results:
      full_macro_f1: 0.8204
      surface_only_f1: 0.7628
      reference_only_f1: 0.7187
      full_vs_surface_gap: 0.058
      full_vs_reference_gap: 0.102
      h2_features_count: 3
      h1_features_count: 4
      entropy_mean_depth_rho: -0.68
      median_ppl_by_depth: "13.50, 4.96, 3.00, 2.07, 1.72"
    result_rationale: >
      These results are from actual execution and look encouraging. But they are entirely in-distribution:
      single generator (Pythia-2.8B), same-family reference (Pythia-410M), no length control. The 0.82
      full F1 benefits from generator-specific artifacts that the reference model can detect precisely
      because it shares the Pythia architecture. The H2 entropy_mean drift (ρ=-0.68) is strong here
      because Pythia-410M and Pythia-2.8B share tokenizer and distributional priors — the reference model's
      perplexity is calibrated to the generator's output distribution. The perplexity monotonic decrease
      (13.5→1.7) is real but partially reflects the reference model's familiarity with same-family outputs.
      In worst tier, subsequent experiments reveal these as inflated baselines.
    tables:
      - name: "Table 1: Feature Ablation (MVP In-Distribution)"
        columns: [feature_set, macro_f1, 95_ci, gen0_f1, gen1_f1, gen2plus_f1]
        rows:
          - [full, 0.8204, "[0.807, 0.834]", 0.952, 0.776, 0.795]
          - [surface_only, 0.7628, "[0.747, 0.774]", 0.920, 0.710, 0.658]
          - [reference_only, 0.7187, "[0.706, 0.733]", 0.895, 0.640, 0.621]
      - name: "Table 2: H1/H2 Feature Classification"
        columns: [feature, source, depth_slope, R2, classification]
        rows:
          - [entropy_mean, reference, -0.042, 0.91, H2_drift]
          - [ttr, surface, -0.031, 0.87, H2_drift]
          - [hapax_ratio, surface, -0.028, 0.83, H2_drift]
          - [entropy_std, reference, 0.003, 0.04, H1_stationary]
          - [entropy_max, reference, -0.005, 0.07, H1_stationary]
          - [entropy_min, reference, 0.002, 0.02, H1_stationary]
          - [tail_decay, reference, 0.004, 0.05, H1_stationary]
    figures_description:
      - "Fig 1: Feature trends across depth 0-4 with mean±std bands. Clear monotonic decrease for entropy_mean/TTR/hapax_ratio; flat for shape features. Looks clean — but this is single-generator same-family setting."
      - "Fig 2: Perplexity by depth (Pythia-410M reference). Monotonic 13.5→1.7. Strong signal — survives into worst tier as reference-model-specific phenomenon."
    analysis: >
      In-distribution results are solid. The dual dynamics split appears clean: 3 H2 features drift,
      4 H1 features are stationary. Perplexity signal is very strong. However, the worst-tier
      interpretation is that this clean separation is partly an artifact of the Pythia-Pythia
      configuration. Subsequent experiments (plan_003, plan_013) will show the H2 drift is partially
      confounded by length artifacts and reference-model specificity.

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      Leave-one-generator-out evaluation across 5 generators. Tests cross-generator generalization.
      In worst tier, LOGO F1 is poor, especially when holding out non-Pythia generators.
    expected_results:
      overall_logo_macro_f1: 0.52
      logo_holdout_pythia28b: 0.61
      logo_holdout_pythia1b: 0.64
      logo_holdout_olmo2: 0.48
      logo_holdout_qwen17b: 0.44
      logo_holdout_qwen06b: 0.43
      within_family_avg_f1: 0.625
      cross_family_avg_f1: 0.45
      leave_one_family_out_pythia_held_in: 0.58
      leave_one_family_out_pythia_held_out: 0.41
    result_rationale: >
      The classifier overfits to generator-specific artifacts rather than learning universal depth
      signatures. Within the Pythia family, generalization is passable (0.61–0.64) because Pythia-2.8B
      and Pythia-1B share tokenizer, training data (The Pile), and architectural patterns — the
      Pythia-410M reference model's NLL features are structurally similar for both. But cross-family
      holdouts (OLMo, Qwen) drop sharply to 0.43–0.48 because: (a) different tokenizers mean surface
      features (TTR, hapax) have different baseline distributions, (b) the Pythia-410M reference
      model assigns systematically different perplexity distributions to non-Pythia outputs, creating
      a domain shift in entropy features, (c) each generator family has its own repetition/diversity
      profile at each depth, so depth-correlated patterns learned from one family don't transfer.
      The leave-one-family-out result (0.41 when Pythia held out) confirms the classifier critically
      depends on Pythia-specific patterns. Overall LOGO F1 of 0.52 is below the 0.58 threshold,
      killing the cross-generator generalization claim.
    tables:
      - name: "Table 3: Leave-One-Generator-Out Macro-F1"
        columns: [held_out_generator, family, macro_f1, gen0_f1, gen1_f1, gen2plus_f1]
        rows:
          - [pythia-2.8b, pythia, 0.61, 0.82, 0.51, 0.50]
          - [pythia-1b, pythia, 0.64, 0.85, 0.54, 0.53]
          - [olmo-2-1b, olmo, 0.48, 0.72, 0.38, 0.34]
          - [qwen3-1.7b, qwen, 0.44, 0.68, 0.35, 0.29]
          - [qwen3-0.6b, qwen, 0.43, 0.67, 0.33, 0.29]
          - ["mean (all)", "-", 0.52, 0.75, 0.42, 0.39]
      - name: "Table 4: Leave-One-Family-Out"
        columns: [held_out_family, train_generators, macro_f1]
        rows:
          - [pythia, "olmo+qwen", 0.41]
          - [olmo, "pythia+qwen", 0.54]
          - [qwen, "pythia+olmo", 0.56]
    figures_description:
      - "Fig 3: Confusion matrices for each LOGO fold. Pythia holdouts show reasonable diagonal; OLMo/Qwen holdouts show heavy off-diagonal mass, especially gen1↔gen2+ confusion."
      - "Fig 4: Feature distribution shift across generators. Box plots of entropy_mean by depth for each generator — Pythia generators show clean separation, OLMo/Qwen show overlapping distributions."
    analysis: >
      Cross-generator generalization fails the 0.58 threshold. The within-family vs cross-family gap
      (0.625 vs 0.45) reveals the classifier relies on generator-specific artifacts. Gen-0 detection
      remains passable (~0.75 average) because human-written text is universally distinct, but gen-1
      vs gen-2+ discrimination (the core depth signal) collapses cross-family. This undermines Claim 1's
      generalization requirement. In the reframed paper, this becomes evidence for: "depth estimation
      requires generator-aware features or larger, more diverse training sets — the task is harder
      than binary detection because depth artifacts are generator-specific."

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B) for feature extraction. Critical
      falsification test for the dual dynamics framework.
    expected_results:
      olmo_ref_entropy_mean_rho: -0.22
      qwen_ref_entropy_mean_rho: -0.15
      pythia_ref_entropy_mean_rho: -0.68
      olmo_ref_full_f1: 0.63
      qwen_ref_full_f1: 0.58
      pythia_ref_full_f1: 0.82
      olmo_ref_h2_features_count: 1
      qwen_ref_h2_features_count: 1
      cross_family_ref_entropy_mean_rho_avg: -0.185
      shape_features_h1_stable_across_refs: true
      ttr_rho_across_refs: -0.30
      hapax_rho_across_refs: -0.27
    result_rationale: >
      Entropy_mean drift (ρ=-0.68 with Pythia reference) largely disappears with non-Pythia references
      (ρ≈-0.22 OLMo, ρ≈-0.15 Qwen). This happens because entropy_mean is driven by how well the
      reference model predicts the generated text — when the reference model shares architecture and
      training data with the generator (Pythia-Pythia), it has calibrated predictions that systematically
      shift with depth. A cross-family reference model assigns noisier, less calibrated perplexities,
      washing out the drift signal. The |ρ|<0.3 threshold is breached for both non-Pythia references.
      Shape features (entropy_std, entropy_max, tail_decay) remain H1-stationary across all references
      — this is genuinely robust because distributional shape is less sensitive to absolute calibration.
      But the H2 side of the "dual dynamics" now has only surface features (TTR, hapax_ratio) showing
      reliable drift (ρ≈-0.28 to -0.30), and these are precisely the features confounded by text
      length (plan_013). The "dual dynamics cross-cuts surface/reference boundary" claim collapses:
      the cross-cutting was an artifact of Pythia-Pythia alignment. Classification F1 with non-Pythia
      reference drops to 0.58–0.63 because the strongest H2 reference feature is now noise.
    tables:
      - name: "Table 5: Entropy_mean Depth Correlation by Reference Model"
        columns: [reference_model, family, entropy_mean_rho, p_value, h2_classification]
        rows:
          - [pythia-410m, pythia, -0.68, "<0.001", H2_confirmed]
          - [olmo-2-1b, olmo, -0.22, 0.031, "H2_weak (|ρ|<0.3)"]
          - [qwen3-0.6b, qwen, -0.15, 0.118, "H2_not_confirmed"]
      - name: "Table 6: Full Feature Set Classification by Reference Model"
        columns: [reference_model, macro_f1, surface_only_f1, ref_only_f1, full_vs_surface_gap]
        rows:
          - [pythia-410m, 0.82, 0.76, 0.72, 0.06]
          - [olmo-2-1b, 0.63, 0.61, 0.48, 0.02]
          - [qwen3-0.6b, 0.58, 0.57, 0.41, 0.01]
      - name: "Table 7: H1/H2 Stability Across Reference Models"
        columns: [feature, pythia_class, olmo_class, qwen_class, stable_across_refs]
        rows:
          - [entropy_mean, H2, "weak/NS", "NS", "NO"]
          - [entropy_std, H1, H1, H1, "YES"]
          - [entropy_max, H1, H1, H1, "YES"]
          - [tail_decay, H1, H1, H1, "YES"]
          - [ttr, H2, H2, H2, "YES"]
          - [hapax_ratio, H2, H2, "weak H2", "YES (marginal)"]
    figures_description:
      - "Fig 5: Entropy_mean by depth for 3 reference models. Pythia shows clear monotonic decrease; OLMo shows slight noisy decline; Qwen nearly flat. Devastating for the dual dynamics narrative."
      - "Fig 6: Shape features (entropy_std, tail_decay) by depth for 3 reference models. All show flat trends — H1 stationarity is genuinely reference-model-independent."
    analysis: >
      The key falsification test triggers: entropy_mean's H2 drift was substantially a Pythia-specific
      artifact. The dual dynamics narrative ("level features drift, shape features don't, and this
      cross-cuts surface/reference") collapses because the cross-cutting evidence depended on
      entropy_mean being a reference feature that drifts. Without it, H2 features are just surface
      features (TTR, hapax), and H1 features are just reference features — exactly the naive
      expectation the paper claimed to overturn. The shape feature H1 stability is real but less
      interesting: it says "distributional shape under any reference model is stable across depth,"
      which is a weaker claim. In the reframed paper, this becomes: "reference-model perplexity
      as depth proxy is reference-model-dependent — a same-family reference provides much stronger
      signal, pointing toward an alignment-based explanation of depth discriminability."

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune OLMo-1B on depth-stratified data. Compare depth-aware filtering vs binary baselines
      with 3+ seeds and bootstrap CIs. In worst tier, the advantage is not statistically significant.
    expected_results:
      depth_quality_spearman: 0.28
      depth_quality_spearman_ci: "[0.11, 0.45]"
      depth_filtering_ppl_improvement_pct: 1.8
      depth_filtering_ppl_improvement_ci: "[-0.5, 4.1]"
      binary_filtering_ppl_improvement_pct: 1.2
      binary_filtering_ppl_improvement_ci: "[-1.1, 3.5]"
      depth_vs_binary_p_value: 0.31
      sample_matched_depth_ppl: 14.2
      sample_matched_binary_ppl: 14.5
      sample_matched_p_value: 0.42
      seed_variance_cv: 0.08
      n_seeds: 5
    result_rationale: >
      With proper experimental controls (multiple seeds, CIs, sample-count matching, non-Pythia model),
      the downstream advantage of depth-aware filtering shrinks to statistical insignificance. Several
      factors contribute: (1) OLMo-1B is more robust to training data contamination than Pythia-410M
      (the original MVP model), reducing the overall signal magnitude; (2) with 5 seeds, the variance
      across runs is substantial (CV≈0.08), swamping the small depth-vs-binary difference; (3) the
      sample-count-matched comparison shows the original advantage was partly a data size confound —
      depth-aware filtering keeps more data (it retains gen-1) than binary filtering (which discards
      all synthetic), so the improvement was partially from having more training data, not from depth
      stratification per se; (4) bootstrap CIs for the depth-vs-binary comparison overlap substantially
      (p=0.31), failing significance. The Spearman ρ=0.28 between predicted depth and quality
      degradation is real but weak, falling in the [0.15, 0.4] worst-tier range. In isolation,
      this correlation is interesting but not actionable. Claim 3 (downstream utility) cannot be
      supported as "significantly outperforms binary baselines."
    tables:
      - name: "Table 8: Downstream Fine-Tuning Results (OLMo-1B, 5 seeds)"
        columns: [filtering_strategy, mean_ppl, std_ppl, 95_ci, improvement_vs_unfiltered_pct]
        rows:
          - [unfiltered, 14.8, 0.42, "[14.2, 15.4]", "-"]
          - [binary_fastdetectgpt, 14.5, 0.51, "[13.8, 15.2]", "1.2 [-1.1, 3.5]"]
          - [binary_ldscore, 14.6, 0.48, "[14.0, 15.2]", "0.9 [-1.4, 3.2]"]
          - [depth_aware_keep_gen01, 14.2, 0.39, "[13.7, 14.7]", "1.8 [-0.5, 4.1]"]
          - [depth_aware_sample_matched, 14.2, 0.44, "[13.6, 14.8]", "1.5 [-0.8, 3.8]"]
      - name: "Table 9: Depth-Quality Correlation"
        columns: [metric, value, 95_ci]
        rows:
          - [spearman_rho, 0.28, "[0.11, 0.45]"]
          - [ppl_gen0_mean, 12.1, "[11.8, 12.4]"]
          - [ppl_gen1_mean, 13.4, "[12.9, 13.9]"]
          - [ppl_gen2_mean, 14.1, "[13.5, 14.7]"]
          - [ppl_gen3_mean, 14.5, "[13.8, 15.2]"]
          - [ppl_gen4_mean, 14.9, "[14.1, 15.7]"]
    figures_description:
      - "Fig 7: Box plots of held-out perplexity across 5 seeds for each filtering strategy. Wide overlapping boxes; depth-aware slightly lower median but CIs encompass binary."
      - "Fig 8: Training data depth composition vs downstream perplexity. Weak positive trend (ρ=0.28) with substantial scatter."
    analysis: >
      Downstream utility claim fails significance after proper experimental controls. The improvement
      exists directionally (1.8% vs 1.2%) but CIs overlap. This was the most anticipated outcome
      from dream reviews: single-run results are fragile. In reframed paper, report honestly as
      "directional evidence for depth-quality correlation, insufficient for statistical significance
      at this sample size" and pivot to the correlation itself (ρ=0.28) as motivation for future
      work. The perplexity-by-depth monotonic relationship (Table 9) is real and publishable as
      a descriptive finding — it just doesn't translate into significant downstream filtering advantage.

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Compare continuation vs elaboration vs inspired_rewriting chains. In worst tier,
      depth signal varies dramatically by prompt type, undermining generalizability.
    expected_results:
      continuation_macro_f1: 0.78
      elaboration_macro_f1: 0.55
      inspired_rewriting_macro_f1: 0.47
      continuation_entropy_mean_rho: -0.65
      elaboration_entropy_mean_rho: -0.38
      rewriting_entropy_mean_rho: -0.18
      cross_prompt_train_test_f1: 0.42
    result_rationale: >
      Depth signal is strongly prompt-type dependent. Continuation chains preserve the strongest
      signal (F1=0.78) because each generation builds directly on the previous output, creating
      cumulative distributional drift. Elaboration chains weaken the signal (F1=0.55) because the
      model is asked to expand on a topic rather than continue text — this introduces more
      creative variation that partially resets the distributional state at each depth. Inspired
      rewriting shows near-chance depth discrimination (F1=0.47) because the semantic departure
      from the source is maximal — each depth step is essentially an independent generation
      conditioned on a theme, not a recursive chain. The entropy_mean drift follows the same
      pattern (ρ: -0.65/-0.38/-0.18). When training on one prompt type and testing on another,
      F1 drops to 0.42, showing the features are prompt-type-specific. This means the "depth
      signal" is partly a "continuation-chain-specific" artifact — real web contamination involves
      diverse generation patterns, not just continuation.
    tables:
      - name: "Table 10: Depth Classification by Prompt Type"
        columns: [prompt_type, macro_f1, entropy_mean_rho, ttr_rho, gen1_vs_gen2plus_f1]
        rows:
          - [continuation, 0.78, -0.65, -0.29, 0.71]
          - [elaboration, 0.55, -0.38, -0.16, 0.44]
          - [inspired_rewriting, 0.47, -0.18, -0.08, 0.36]
      - name: "Table 11: Cross-Prompt Transfer"
        columns: [train_prompt, test_prompt, macro_f1]
        rows:
          - [continuation, elaboration, 0.46]
          - [continuation, rewriting, 0.39]
          - [elaboration, continuation, 0.51]
          - [elaboration, rewriting, 0.42]
          - [rewriting, continuation, 0.44]
          - [rewriting, elaboration, 0.40]
    figures_description:
      - "Fig 9: Feature drift (entropy_mean, TTR) by depth for 3 prompt types. Continuation shows monotonic decrease; elaboration shows noisy partial decrease; rewriting shows flat/noisy trajectory."
    analysis: >
      Prompt type is a major moderator of depth signal, challenging ecological validity. In the
      reframed paper, this becomes a positive finding for the task formulation angle: "Generation
      depth estimation difficulty depends critically on the semantic coupling between generation
      steps. Continuation chains (high coupling) preserve depth signal; rewriting chains (low
      coupling) do not. This connects to attractor cycle theory — semantic-preserving chains
      converge, while semantically divergent chains don't accumulate distributional drift."

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      Compare paraphrasing vs continuation chains. In worst tier, paraphrasing chains
      converge quickly (as attractor theory predicts), but continuation chains also
      show limited depth discrimination beyond gen-2.
    expected_results:
      paraphrastic_3class_f1: 0.52
      nonparaphrastic_3class_f1: 0.78
      paraphrastic_entropy_mean_plateau_depth: 2
      nonparaphrastic_saturation_depth: 3
      paraphrastic_gen2_vs_gen3_f1: 0.34
      nonparaphrastic_gen2_vs_gen3_f1: 0.41
    result_rationale: >
      Paraphrasing chains converge by depth 2 as attractor theory predicts — gen-2, gen-3, gen-4
      are nearly indistinguishable (F1=0.34 for gen-2 vs gen-3). Continuation chains preserve more
      signal but also saturate by depth 3 — the distributional drift accumulates but with
      diminishing marginal signal at each step. The worst-tier interpretation: even non-paraphrastic
      chains have bounded depth discriminability, just with a slightly higher ceiling than
      paraphrastic ones. The difference (0.78 vs 0.52) confirms continuation chains are better
      for depth estimation but doesn't rescue the broader generalizability problem — the signal
      is still chain-type-specific and bounded.
    tables:
      - name: "Table 12: Paraphrastic vs Non-Paraphrastic Depth Discrimination"
        columns: [chain_type, 3class_f1, gen0_f1, gen1_f1, gen2plus_f1, entropy_mean_rho]
        rows:
          - [paraphrastic, 0.52, 0.78, 0.45, 0.33, -0.31]
          - [continuation, 0.78, 0.93, 0.72, 0.69, -0.65]
    figures_description:
      - "Fig 10: Feature values by depth for paraphrastic vs continuation chains. Paraphrastic shows rapid convergence (plateau by depth 2); continuation shows gradual drift with diminishing returns after depth 3."
    analysis: >
      Confirms attractor theory prediction for paraphrastic chains. Continuation chains have more
      signal but also saturate. In reframed paper: "Our empirical results are consistent with
      attractor convergence — extending the theory to non-paraphrastic chains shows the convergence
      is slower but still present, bounding practical depth estimation to ~3 useful classes."

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains (different generator per depth step). In worst tier, cross-model
      chains destroy depth signal because generator identity dominates depth identity.
    expected_results:
      cross_model_macro_f1: 0.39
      single_model_macro_f1: 0.78
      cross_model_gen0_f1: 0.65
      cross_model_gen1_f1: 0.28
      cross_model_gen2plus_f1: 0.24
      cross_vs_single_delta: -0.39
    result_rationale: >
      Cross-model chains are dramatically harder (F1=0.39, essentially near chance for gen-1 and
      gen-2+). The reason is fundamental: when generator identity changes at each depth step,
      the distributional features capture generator identity more than depth. A gen-1 text from
      Qwen looks more different from gen-1 text from Pythia than gen-1 looks from gen-2 within
      the same generator. The features (NLL statistics under a fixed reference model) are sensitive
      to the generator's output distribution, creating a confound where generator variation swamps
      depth variation. Gen-0 remains detectable (F1=0.65) because human-written text is still
      distinct from any machine-generated text, but ordinal depth discrimination collapses. This
      is perhaps the strongest negative result: in the realistic scenario of diverse web generators,
      depth estimation with these features is not viable.
    tables:
      - name: "Table 13: Single-Model vs Cross-Model Chains"
        columns: [chain_type, macro_f1, gen0_f1, gen1_f1, gen2plus_f1]
        rows:
          - [single_model, 0.78, 0.93, 0.72, 0.69]
          - [cross_model_random, 0.39, 0.65, 0.28, 0.24]
          - [cross_model_increasing_size, 0.41, 0.66, 0.30, 0.27]
          - [cross_model_decreasing_size, 0.38, 0.63, 0.27, 0.24]
    figures_description:
      - "Fig 11: t-SNE of feature space colored by depth, single-model (left) vs cross-model (right). Single-model shows depth clusters; cross-model shows generator clusters."
    analysis: >
      Cross-model chains destroy depth signal — generator identity is a much stronger signal
      than depth in the feature space. This is the ecological validity nail: real web contamination
      involves diverse generators. In reframed paper, this honestly motivates future work on
      generator-invariant depth features and positions the current features as a baseline that
      works in controlled (single-generator) settings but not in the wild.

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      Expand to 4 domains. In worst tier, significant domain variance with some domains
      showing near-chance performance.
    expected_results:
      wikipedia_macro_f1: 0.72
      news_macro_f1: 0.68
      scientific_macro_f1: 0.55
      creative_macro_f1: 0.48
      overall_macro_f1: 0.61
      cross_domain_train_test_f1: 0.49
      domain_f1_std: 0.11
    result_rationale: >
      Domain variance is substantial. Wikipedia and news seeds (factual, structured prose) show
      passable performance because LLMs generate predictable continuations with consistent
      distributional drift. Scientific abstracts show weaker signal because the specialized
      vocabulary and formulaic structure reduce the distinguishability of human vs machine text
      at each depth. Creative writing shows near-chance performance because it has the highest
      natural language variance — the within-class variation in features (e.g., TTR, hapax_ratio)
      for creative text at any depth is large enough to swamp the between-class (depth) variation.
      Cross-domain transfer is poor (0.49) because the feature baselines differ across domains.
      This adds another moderator (domain + prompt type + generator family) that limits the
      generalizability of depth estimation.
    tables:
      - name: "Table 14: Depth Classification by Domain"
        columns: [domain, n_seeds, macro_f1, gen0_f1, gen1_f1, gen2plus_f1]
        rows:
          - [wikipedia, 500, 0.72, 0.89, 0.63, 0.64]
          - [news, 500, 0.68, 0.86, 0.59, 0.59]
          - [scientific, 500, 0.55, 0.78, 0.44, 0.43]
          - [creative, 500, 0.48, 0.71, 0.37, 0.36]
          - [all_pooled, 2000, 0.61, 0.81, 0.51, 0.51]
    figures_description:
      - "Fig 12: Feature variance decomposition by domain. Box plots showing much wider feature distributions for creative/scientific than wiki/news."
    analysis: >
      Domain is a significant moderator. Factual domains have more signal; creative domains have
      less. In reframed paper: "Depth estimation difficulty depends on the entropy of the source
      domain — low-entropy domains (wiki, news) produce more predictable generations with clearer
      depth drift; high-entropy domains (creative) mask depth signal with natural variation."

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4). In worst tier, performance
      is near chance for finer classes.
    expected_results:
      five_class_macro_f1: 0.28
      three_class_macro_f1: 0.78
      gen0_f1: 0.85
      gen1_f1: 0.42
      gen2_f1: 0.18
      gen3_f1: 0.12
      gen4_f1: 0.11
      ordinal_mae: 1.4
      adjacent_confusion_pct: 0.72
    result_rationale: >
      Five-class F1 of 0.28 is barely above chance (0.20 for 5 classes). Gen-0 remains detectable
      (F1=0.85) and gen-1 is marginally separable (F1=0.42), but gen-2/3/4 collapse into an
      indistinguishable cluster (F1: 0.18/0.12/0.11). This is because distributional drift
      between adjacent deep generations is minimal — the marginal change from gen-2→gen-3 in
      any feature is smaller than the within-class variance. The ordinal MAE of 1.4 means
      predictions are off by ~1.4 depth levels on average. 72% of misclassifications are between
      adjacent classes, suggesting some ordinal structure remains but is too weak for practical
      5-class discrimination. This validates the attractor convergence prediction: beyond ~3
      classes, depth signal is negligible even for non-paraphrastic chains.
    tables:
      - name: "Table 15: Five-Class Ordinal Classification"
        columns: [class, precision, recall, f1, n_samples]
        rows:
          - [gen-0, 0.88, 0.82, 0.85, 995]
          - [gen-1, 0.39, 0.45, 0.42, 993]
          - [gen-2, 0.16, 0.20, 0.18, 912]
          - [gen-3, 0.11, 0.13, 0.12, 856]
          - [gen-4, 0.10, 0.12, 0.11, 816]
    figures_description:
      - "Fig 13: 5×5 confusion matrix. Strong diagonal for gen-0; gen-1 somewhat visible; gen-2/3/4 form a diffuse block with heavy off-diagonal mass."
    analysis: >
      Five-class is essentially unsolvable with current features. Confirms the 3-class ceiling.
      In reframed paper, this is a benchmark result: "We establish that 3-class depth estimation
      (gen-0/gen-1/gen-2+) is the practical ceiling for distributional features, consistent with
      attractor convergence theory extended to non-paraphrastic generation."

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Robustness to simulated human edits. In worst tier, even mild edits substantially
      degrade performance.
    expected_results:
      baseline_f1: 0.78
      random_replace_5pct_f1: 0.68
      random_replace_10pct_f1: 0.58
      random_replace_20pct_f1: 0.44
      llm_light_edit_f1: 0.53
      f1_drop_at_5pct: -0.10
    result_rationale: >
      Even 5% random word replacement drops F1 by 0.10, and LLM-simulated light editing drops
      F1 by 0.25. The features are brittle to post-generation modification because both surface
      features (TTR, hapax) and reference features (entropy statistics) are sensitive to token-level
      changes. A few word substitutions can significantly alter hapax ratio, TTR, and the reference
      model's NLL distribution. LLM-simulated editing is worse than random replacement because it
      systematically "cleans up" the distributional artifacts that depth estimation relies on —
      an LLM editing gen-3 text makes it look more like gen-1 by smoothing out the accumulated
      drift. This is a fundamental limitation: any real-world post-processing pipeline (human
      editing, automated cleanup, grammar correction) will degrade depth signal.
    tables:
      - name: "Table 16: Robustness to Human Edits"
        columns: [edit_type, edit_rate, macro_f1, delta_f1]
        rows:
          - [none, "0%", 0.78, "-"]
          - [random_replace, "5%", 0.68, -0.10]
          - [random_replace, "10%", 0.58, -0.20]
          - [random_replace, "20%", 0.44, -0.34]
          - [llm_light_edit, "~8%", 0.53, -0.25]
    figures_description:
      - "Fig 14: F1 degradation curve as function of edit rate. Roughly linear decline with slope ≈-1.7 F1 per percentage point of edits."
    analysis: >
      Depth features are fragile to post-generation modification. In reframed paper: "Depth
      estimation is most applicable to unedited generation chains (e.g., automated content
      farms) and degrades rapidly with human post-processing. This constrains the practical
      applicability to detection of fully automated pipelines."

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      Add LD-Score as feature. In worst tier, LD-Score shows inconsistent behavior —
      neither clearly H2 nor clearly adding value.
    expected_results:
      ldscore_depth_rho: -0.25
      ldscore_added_f1_delta: 0.005
      ldscore_h2_classification: "weak/ambiguous"
      with_ldscore_f1: 0.785
      without_ldscore_f1: 0.78
    result_rationale: >
      LD-Score shows weak depth correlation (ρ=-0.25), not clearly meeting H2 criteria (slope
      significant but R²<0.15). Character-level distribution is a noisy proxy for depth — it
      captures some vocabulary shift but is contaminated by topic and style variation. Adding
      LD-Score to the feature set provides negligible improvement (+0.005 F1), well within noise.
      The pre-registered prediction that LD-Score would be a "level feature" exhibiting H2 drift
      is partially supported (negative ρ) but weak. In worst tier, this fails to provide
      out-of-sample validation for the level/shape framework because the framework itself is
      collapsing (plan_003 shows H2 is reference-model-dependent).
    tables:
      - name: "Table 17: LD-Score as Depth Feature"
        columns: [metric, value]
        rows:
          - [ldscore_depth_rho, -0.25]
          - [ldscore_slope_R2, 0.12]
          - [feature_set_without_ldscore_f1, 0.780]
          - [feature_set_with_ldscore_f1, 0.785]
          - [ldscore_feature_importance_rank, "7/8"]
    figures_description:
      - "Fig 15: LD-Score by depth. Noisy downward trend with wide variance bands. Partial H2 behavior but unconvincing."
    analysis: >
      LD-Score pre-registered prediction is weakly supported but insufficient to validate the
      level/shape framework given that the framework is independently undermined by plan_003.
      In reframed paper: "LD-Score shows weak depth sensitivity, consistent with character-level
      features capturing some vocabulary drift, but insufficient to serve as independent validation
      of the dual dynamics hypothesis."

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification. In worst tier,
      end-to-end slightly outperforms handcrafted features, undermining the feature analysis.
    expected_results:
      e2e_macro_f1: 0.83
      handcrafted_macro_f1: 0.78
      e2e_cross_generator_f1: 0.55
      e2e_vs_handcrafted_delta: 0.05
      e2e_gen1_vs_gen2plus_f1: 0.76
    result_rationale: >
      End-to-end classification achieves F1=0.83, slightly above the handcrafted 0.78, suggesting
      that learned representations capture additional signal beyond the 7 distributional features.
      However, the improvement is modest and the end-to-end model also fails to generalize
      cross-generator (F1=0.55), indicating the additional signal is also generator-specific.
      This undercuts the feature analysis contribution: if a fine-tuned LM can slightly beat the
      handcrafted features, the dual dynamics decomposition is more of an interpretability lens
      than a competitive method. In worst tier, this result slightly undermines the feature-level
      analysis without providing a clearly superior alternative — neither approach generalizes.
    tables:
      - name: "Table 18: End-to-End vs Handcrafted Features"
        columns: [method, in_dist_f1, cross_gen_logo_f1, training_cost_gpu_h]
        rows:
          - [handcrafted_xgboost, 0.78, 0.52, 0.1]
          - [qwen_qolra_e2e, 0.83, 0.55, 15]
          - [qwen_qolra_frozen, 0.80, 0.53, 8]
    figures_description:
      - "Fig 16: Learning curves for end-to-end model showing rapid convergence on in-distribution data. Cross-generator performance plateaus early."
    analysis: >
      End-to-end slightly beats handcrafted but shares the generalization failure. In reframed
      paper: "Both handcrafted and learned features achieve similar in-distribution performance
      and similar cross-generator degradation, suggesting the depth estimation difficulty is
      fundamental to the feature space, not a limitation of our specific feature engineering."

  - name: text_length_control
    plan_id: plan_013
    description: >
      Text length confound analysis. In worst tier, length-controlled F1 drops >0.08,
      revealing that surface features substantially tracked length.
    expected_results:
      length_depth_correlation: 0.42
      original_full_f1: 0.78
      length_controlled_full_f1: 0.68
      length_controlled_f1_delta: -0.10
      length_controlled_surface_f1: 0.63
      length_controlled_reference_f1: 0.66
      length_normalized_ttr_rho: -0.12
      length_normalized_hapax_rho: -0.09
      original_ttr_rho: -0.31
      original_hapax_rho: -0.28
      length_matched_f1: 0.70
    result_rationale: >
      Text length correlates with depth (r=0.42) — deeper generations tend to be shorter as models
      produce more repetitive/compressed outputs. This correlation confounds both surface features
      and indirectly reference features. TTR and hapax_ratio are mechanically length-dependent
      (shorter texts have higher TTR, lower hapax ratio), so their depth correlation (ρ≈-0.3)
      was partially a length proxy. After length normalization (fixed-window computation), TTR
      depth correlation drops from -0.31 to -0.12 and hapax from -0.28 to -0.09 — most of the
      "H2 drift" in surface features was length artifact. Length-controlled full F1 drops by 0.10
      (from 0.78 to 0.68), breaching the >0.08 threshold. Notably, reference features also drop
      (from 0.72 to 0.66) because entropy statistics are affected by text length through the
      number of tokens evaluated. After length matching (subsampling to equalize length distributions),
      F1 is 0.70 — real depth signal exists but is substantially weaker than originally measured.
      The full-vs-surface gap shrinks (0.68 vs 0.63 = 0.05 gap → 0.02 gap after removing length
      confound from surface features).
    tables:
      - name: "Table 19: Length Confound Analysis"
        columns: [condition, full_f1, surface_f1, reference_f1, full_vs_surface_gap]
        rows:
          - [original, 0.78, 0.76, 0.72, 0.02]
          - [length_normalized_features, 0.68, 0.63, 0.66, 0.02]
          - [length_matched_subsampling, 0.70, 0.65, 0.67, 0.03]
      - name: "Table 20: Feature Depth Correlation Before/After Length Control"
        columns: [feature, original_rho, length_normalized_rho, pct_explained_by_length]
        rows:
          - [ttr, -0.31, -0.12, "61%"]
          - [hapax_ratio, -0.28, -0.09, "68%"]
          - [entropy_mean, -0.68, -0.55, "19%"]
          - [entropy_std, 0.03, 0.02, "33%"]
          - [tail_decay, 0.04, 0.03, "25%"]
    figures_description:
      - "Fig 17: Text length distributions by depth. Clear shift toward shorter texts at deeper generations."
      - "Fig 18: TTR vs depth before/after length normalization. Original shows clear decline; normalized shows near-flat with slight residual trend."
    analysis: >
      Length confound is substantial. ~60-68% of surface feature depth correlation was length
      artifact. Reference features are less affected (19% for entropy_mean) but still impacted.
      After controlling for length, the full-vs-surface gap nearly vanishes (0.02), meaning
      reference features' advantage was partially from being less length-confounded, not from
      capturing genuinely different depth signal. In reframed paper: "We identify text length as
      a major confound in depth estimation: standard surface diversity metrics (TTR, hapax ratio)
      primarily track length variation rather than genuine distributional drift. Length-controlled
      analysis reveals a weaker but real residual depth signal, predominantly carried by
      reference-model perplexity statistics."

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      Add 7B+ generator (Qwen3-8B-Base). In worst tier, depth signal is minimal at this scale —
      larger models produce more fluent text that masks distributional drift.
    expected_results:
      generator_7bplus_macro_f1: 0.43
      generator_7bplus_gen0_f1: 0.62
      generator_7bplus_gen1_f1: 0.35
      generator_7bplus_gen2plus_f1: 0.32
      generator_7bplus_entropy_mean_rho: -0.19
      small_generator_avg_f1: 0.72
      f1_vs_generator_size_correlation: -0.85
      generator_7bplus_ppl_depth0: 8.2
      generator_7bplus_ppl_depth4: 4.1
      ppl_dynamic_range_7bplus: 4.1
      ppl_dynamic_range_2_8b: 11.8
    result_rationale: >
      The 7B+ generator produces text that is much harder to depth-classify (F1=0.43, near chance
      for gen-1 and gen-2+). Several mechanisms explain this: (1) larger models have lower
      perplexity under any reference model, so the absolute perplexity at gen-0 is already closer
      to machine-generated (8.2 vs 13.5 for human text under Pythia-2.8B reference), reducing
      the dynamic range for drift detection (4.1 vs 11.8 points of perplexity range across depths);
      (2) larger models maintain more vocabulary diversity across recursive generations — TTR and
      hapax ratio drift less because the model's larger capacity preserves lexical variety; (3) the
      distributional shape of 7B+ outputs is more "human-like" at every depth, compressing the
      feature space. The F1-vs-generator-size correlation of -0.85 shows a clear scaling law:
      depth discriminability degrades roughly log-linearly with generator parameters. This connects
      directly to model collapse literature — larger models collapse slower, producing less
      distributional drift per recursive step. Gen-0 detection (human vs 7B-generated) is also
      harder (F1=0.62 vs ~0.90 for smaller generators) because 7B outputs are more human-like
      on all features.
    tables:
      - name: "Table 21: Depth Classification by Generator Scale"
        columns: [generator, params, macro_f1, gen0_f1, gen1_f1, gen2plus_f1, entropy_mean_rho]
        rows:
          - [qwen3-0.6b, 0.6B, 0.74, 0.91, 0.66, 0.65, -0.58]
          - [pythia-1b, 1B, 0.71, 0.89, 0.62, 0.62, -0.55]
          - [olmo-2-1b, 1.5B, 0.69, 0.87, 0.60, 0.60, -0.51]
          - [qwen3-1.7b, 1.7B, 0.68, 0.86, 0.58, 0.60, -0.48]
          - [pythia-2.8b, 2.8B, 0.78, 0.93, 0.72, 0.69, -0.68]
          - [qwen3-8b, 8B, 0.43, 0.62, 0.35, 0.32, -0.19]
      - name: "Table 22: Perplexity Dynamic Range by Generator Scale"
        columns: [generator, ppl_depth0, ppl_depth4, dynamic_range, ppl_ratio]
        rows:
          - [pythia-2.8b, 13.5, 1.7, 11.8, 7.9]
          - [pythia-1b, 12.8, 2.1, 10.7, 6.1]
          - [olmo-2-1b, 11.4, 2.5, 8.9, 4.6]
          - [qwen3-1.7b, 10.8, 2.8, 8.0, 3.9]
          - [qwen3-8b, 8.2, 4.1, 4.1, 2.0]
    figures_description:
      - "Fig 19: Macro-F1 vs log(generator_params). Clear negative log-linear trend with R²=0.72. Pythia-2.8B is an outlier above the trend (same-family reference advantage)."
      - "Fig 20: Perplexity-by-depth curves for all generators. Smaller generators show steeper descent; 7B+ shows shallow, nearly flat curve."
      - "Fig 21: Feature space visualization (PCA) for 7B+ generator outputs. Depth classes heavily overlap, unlike the clean separation seen with smaller generators."
    analysis: >
      Scale-dependent depth signal degradation is the strongest negative finding and the most
      publishable result in the worst tier. The log-linear F1-vs-scale relationship is novel
      empirical evidence connecting depth estimation to model collapse theory: "larger models
      collapse slower (Gerstgrasser et al.), and correspondingly, depth signal degrades with scale."
      Note Pythia-2.8B is anomalously high due to same-family reference advantage — once corrected
      (using cross-family reference, plan_003), it would likely fall closer to the trend line.
      The perplexity dynamic range analysis (Table 22) provides a mechanistic explanation:
      reference-model perplexity has less room to drift when the generator is already fluent.
      In reframed paper, this becomes the central analytical contribution: "Generation depth
      estimation exhibits a scale-dependent regime: distributional features that reliably detect
      depth for ≤3B generators fail at 7B+ scale, providing empirical evidence for scale-dependent
      convergence rates in recursive generation."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ac1b3d1-a272-447b-a26d-750b89fb2cb2",
  "isSidechain": false,
  "requestId": "req_011Cb3FiUH6nMrFDR6ATbPpR",
  "type": "assistant",
  "uuid": "44ab2775-8881-431a-a580-e04bdb468eba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HNgLjuNMeoEznaMLarPoo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13118,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15474,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13118
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core dual dynamics finding is fragile — collapses under cross-family reference or is primarily a length/vocabulary artifact; depth signal weak at 7B+ scal…",
  "leafUuid": "44ab2775-8881-431a-a580-e04bdb468eba",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation benchmark and negative scaling analysis",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core dual dynamics finding is fragile — collapses under cross-family reference or is primarily a length/vocabulary artifact; depth signal weak at 7B+ scal…",
  "leafUuid": "44ab2775-8881-431a-a580-e04bdb468eba",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation benchmark and negative scaling analysis",
  "sessionId": "d03f4dca-ffac-4ec2-93c7-f5bebc60961e"
}
```

---
