# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Depth discriminability and downstream utility hold but dual dynamics parti

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/27db3dfb-9d0a-49f3-bf36-70dd72769be4.jsonl`
- **Structured JSON:** [`ff463ae96b6f4912d7b3.json`](../../sessions/ff/ff463ae96b6f4912d7b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T22:24:26.098Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T22:24:26.098Z",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Depth discriminability and downstream utility hold but dual dynamics partially weakened — either length confound erodes surface features, cross-family reference shows weaker drift, or 7B+ signal degrades; claims need softening\n核心假设：['Cross-generator leave-one-out macro-F1 moderate (0.58-0.70), with performance drop concentrated on out-of-family generators', 'Entropy_mean drift attenuates with non-Pythia reference (|ρ| drops to 0.3-0.5) — dual dynamics exists but strength is reference-model-dependent', 'Length-controlled F1 drops 0.03-0.08 for surface features — length is a partial confound but not sole driver', '7B+ generator shows weaker but non-zero depth signal (F1 0.50-0.65), confirming signal exists but decays with fluency', 'Downstream filtering advantage exists but CI overlap with best binary baseline on some metrics; effect size modest', 'Full feature set still outperforms single-family subsets but gap narrows (0.02-0.04 over surface-only)']\n关键指标范围：{'cross_gen_logo_macro_f1': [0.58, 0.7], 'cross_family_ref_entropy_mean_rho': [-0.5, -0.3], 'length_controlled_f1_delta': [-0.08, -0.03], 'full_vs_surface_f1_gap': [0.02, 0.04], 'full_vs_reference_f1_gap': [0.04, 0.08], 'downstream_depth_quality_spearman': [0.4, 0.65], 'depth_filtering_perplexity_improvement_pct': [3, 8], 'generator_7bplus_macro_f1': [0.5, 0.65], 'finer_5class_macro_f1': [0.35, 0.5]}\n叙事方向：Claim 1 (depth discriminability) holds but generalization qualified — works best within model family, degrades cross-family. Claim 2 (dual dynamics) softened: level/shape split is real but strength varies with reference model choice, presented as 'reference-model-modulated dual dynamics' rather than universal law. Length confound acknowledged as partial contributor — paper adds length-controlled analysis as supplementary validation, notes residual signal beyond length. Claim 3 softened to 'depth-aware filtering offers complementary signal to binary detection' rather than 'significantly outperforms.' 7B+ results presented as honest scaling analysis — depth signal weakens but doesn't vanish, motivating future work on scale-robust features. Paper reframed slightly: emphasis shifts from 'dual dynamics as general principle' to 'depth estimation as feasible and useful task with initial evidence for dual dynamics.' Still viable for AAAI/EMNLP as empirical contribution with nuanced findings — reviewers often reward honesty about limitations.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nfocus: D006 re-dream after framing repositioning. Key changes: (1) contribution explicitly positioned as empirical/conceptual not methodological — features are standard NLL stats, novelty is in problem formulation + dual dynamics finding + application; (2) OOD detection connection acknowledged (RC8); (3) text length confound controlled (plan_013); (4) downstream utility uses OLMo-1B not Pythia-410M to avoid reference model circularity, multiple seeds + CIs required (RC11); (5) 7B+ generator added as P1 (plan_014, RC9); (6) related work must be 30+ references. Verify whether these changes address the structural issues that caused Best=5/Median=5/Worst=4 in previous dream.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that \"reference-model features = robust, surface features = fragile.\" The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are \"better\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: \"fingerprint\" in the paper refers to the full feature vector's combination, not just reference-model features.\n\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\n\n**RC9 — \"Only ≤2.8B generators — does this transfer to frontier scale?\"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.\n\n**RC10 — \"Text length confound\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\n\n**RC11 — \"Downstream utility — single run, no CIs\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\n\n## Contribution Positioning (Dream D006 insight)\nThe contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection\n2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary\n3. **Practical application**: Risk-stratified data curation outperforming binary filtering\n\nDo NOT overclaim \"distributional fingerprinting\" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.\n\nRelated work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).\n\n## Venue Fit\n- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T22:24:26.102Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T22:24:26.102Z",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T22:24:26.122Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Depth discriminability and downstream utility hold but dual dynamics partially weakened — either length confound erodes surface features, cross-family reference shows weaker drift, or 7B+ signal degrades; claims need softening
核心假设：['Cross-generator leave-one-out macro-F1 moderate (0.58-0.70), with performance drop concentrated on out-of-family generators', 'Entropy_mean drift attenuates with non-Pythia reference (|ρ| drops to 0.3-0.5) — dual dynamics exists but strength is reference-model-dependent', 'Length-controlled F1 drops 0.03-0.08 for surface features — length is a partial confound but not sole driver', '7B+ generator shows weaker but non-zero depth signal (F1 0.50-0.65), confirming signal exists but decays with fluency', 'Downstream filtering advantage exists but CI overlap with best binary baseline on some metrics; effect size modest', 'Full feature set still outperforms single-family subsets but gap narrows (0.02-0.04 over surface-only)']
关键指标范围：{'cross_gen_logo_macro_f1': [0.58, 0.7], 'cross_family_ref_entropy_mean_rho': [-0.5, -0.3], 'length_controlled_f1_delta': [-0.08, -0.03], 'full_vs_surface_f1_gap': [0.02, 0.04], 'full_vs_reference_f1_gap': [0.04, 0.08], 'downstream_depth_quality_spearman': [0.4, 0.65], 'depth_filtering_perplexity_improvement_pct': [3, 8], 'generator_7bplus_macro_f1': [0.5, 0.65], 'finer_5class_macro_f1': [0.35, 0.5]}
叙事方向：Claim 1 (depth discriminability) holds but generalization qualified — works best within model family, degrades cross-family. Claim 2 (dual dynamics) softened: level/shape split is real but strength varies with reference model choice, presented as 'reference-model-modulated dual dynamics' rather than universal law. Length confound acknowledged as partial contributor — paper adds length-controlled analysis as supplementary validation, notes residual signal beyond length. Claim 3 softened to 'depth-aware filtering offers complementary signal to binary detection' rather than 'significantly outperforms.' 7B+ results presented as honest scaling analysis — depth signal weakens but doesn't vanish, motivating future work on scale-robust features. Paper reframed slightly: emphasis shifts from 'dual dynamics as general principle' to 'depth estimation as feasible and useful task with initial evidence for dual dynamics.' Still viable for AAAI/EMNLP as empirical contribution with nuanced findings — reviewers often reward honesty about limitations.

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
  "promptId": "2c1e6fec-9013-4c4c-a44b-01f35719703e",
  "type": "user",
  "uuid": "9c972832-c15e-4742-9774-b96d2651a9aa",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T22:24:26.120Z_

```json
{
  "parentUuid": "9c972832-c15e-4742-9774-b96d2651a9aa",
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
  "uuid": "9b6a873a-6fe9-493e-ab25-b39305b3c291",
  "timestamp": "2026-05-14T22:24:26.120Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T22:24:26.120Z_

```json
{
  "parentUuid": "9b6a873a-6fe9-493e-ab25-b39305b3c291",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f7da42a3-8710-47ac-8ddb-49e228755cf7",
  "timestamp": "2026-05-14T22:24:26.120Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Depth discriminability and downstream utility hold but dual dynamics partially weakened — either length confound erodes surface features, cross-family re…",
  "leafUuid": "f7da42a3-8710-47ac-8ddb-49e228755cf7",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical validation of dual dynamics in LLM generation depth estimation",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4"
}
```

---

### Assistant

_source line 8 · 2026-05-14T22:27:10.017Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental results for all "planned" experiments in the experiment plan, at the "median" tier level. I need to understand the median tier definition and produce realistic predicted results with rationales.

Let me first review the experiment plan and understand what experiments are planned vs completed.

Completed experiments:
- mvp-001: DONE (macro_f1: 0.8408, cv_macro_f1: 0.806)
- plan-001/plan-001-fix: DONE (full: 0.82, surface: 0.76, reference: 0.72)


- plan-002: RUNNING with mixed results across sub-experiments

Now I'm looking at the full list of planned experiments that still need imagined results. Beyond plan-002, there are ten more experiments ranging from cross-generator evaluation through multi-domain seeds and finer-grained ordinal analysis, up to human edit robustness and feature engineering experiments. I need to generate realistic median-tier predictions for each of these.

Wait, I'm noticing something important here—the experiment_plan marks everything as "planned" status, but some like plan-001 already have completed registry entries. Since the user asked for results on each planned experiment in the plan, I should treat all of them as needing imagined data, even the ones that are technically done or in progress.

Now I'm working through the metric constraints for the median tier. I'm looking at the acceptable ranges for each key performance indicator—things like cross-generation logo classification F1 scores, reference entropy correlations, length control deltas, and various gap measurements between model variants. I'm also noting the ranges for downstream quality metrics and generator performance across different model sizes and classification granularities.

With these constraints in mind, I'm establishing the core assumptions that will guide the experiment design: moderate cross-generator performance with concentrated drops on out-of-family cases, entropy drift that attenuates when using non-Pythia references, controlled F1 degradation for surface features, weaker but measurable depth signals in larger models, filtering advantages that still overlap with baseline confidence intervals, and narrowing but persistent gaps between full feature sets and single-family subsets.

Now I'm ready to construct the full experimental configuration and provide detailed rationale for each experiment.

For the feature ablation experiment, I need to reconcile the existing MVP results with median tier constraints. The current numbers show a 0.06 gap between full and surface features, but the median tier definition expects this to narrow to 0.02-0.04 under more rigorous cross-generator testing. Since the MVP data represents within-generator performance, those numbers can stand, but I should adjust expectations for how they generalize across generators. Now I'm mapping out where the median-tier constraints would actually bite: plan_002 shows the sharpest drop in cross-generator performance down to 0.58-0.70, plan_003 sees entropy correlations weaken significantly, and the smaller model experiments in plan_014 struggle at 0.50-0.65. The length control and finer-grained analyses also degrade noticeably. So I'll anchor plan_001 to the existing results since it's on the same data, then work through each experiment with these performance drops in mind.

For plan_001, the feature importance hierarchy is clear: entropy_mean, TTR, and hapax_ratio are the strong predictors with steep negative slopes and high R² values, while entropy_std and entropy_max barely move. Perplexity shows interesting depth-dependent variation that I should note.

Moving to plan_002, the cross-generator LOGO evaluation reveals a performance gap between within-family (Pythia at 0.72) and cross-family (0.60), with the full feature set landing around 0.65 overall. The surface and reference models are converging nicely, narrowing that gap to just 0.03.

For plan_003, switching to non-Pythia reference models shows entropy_mean correlations weaken considerably—dropping from -0.68 with Pythia to -0.42 with OLMo and -0.35 with Qwen—but the classification performance still holds at 0.78 F1, suggesting the shape features are doing the heavy lifting. Plan_004 shows the downstream utility is modest but real: depth-aware filtering gives about 5.5% perplexity improvement with a Spearman correlation around 0.52 on the fine-tuning task.

Looking at prompt variations, continuation preserves the depth signal best, while elaboration and inspired rewriting degrade it progressively. The paraphrastic chains saturate quickly at generation-2, whereas non-paraphrastic chains extend the signal further. Cross-model chains underperform single-model chains but stay above baseline, and across domains, Wikipedia generalizes best while creative writing struggles most. Finally, the finer-grained 5-class classification reaches about 0.43 F1 with confusion concentrated between adjacent classes.

Now examining robustness and scaling: human edits cause performance to degrade with intensity, though 5% edits barely impact results while 20% edits drop significantly. The LD-Score feature confirms the predicted H2 drift and provides modest classifier gains. A QLoRA end-to-end model performs comparably to handcrafted features with mixed results across conditions. Length-controlled experiments show depth correlates with shorter text at higher levels, and controlling for length reduces surface feature F1 by 0.05 while reference features remain more stable. Scaling to a 7B+ generator yields around 0.57 F1—the depth signal weakens but persists.

Now I'm organizing all these findings into a comprehensive YAML structure with detailed metrics, rationales, and analysis for each experiment. Let me work through the specific numbers more carefully, starting with the feature ablation baseline where I observed full=0.82, surface=0.76, reference=0.72 on the MVP data with Pythia-2.8B as the generator and Pythia-410M as reference. The gap between full and surface is 0.06, and between full and reference is 0.10, confirming the H2/H1 split with strong perplexity gradients in pre-validation. For cross-generator evaluation, I'm testing across multiple generators including Pythia-2.8B, Pythia-1B, and others.

For the leave-one-out analysis, the macro-F1 scores show variation across generators—Pythia-2.8B held out gives 0.71, Pythia-1B gives 0.70, while the smaller models like OLMo-2-1B and Qwen variants range from 0.58 to 0.62, with an overall LOGO mean around 0.644. When I look at family-level holdout, removing the entire Pythia family drops performance to 0.58, which suggests there's meaningful family-specific signal in the training data.

The gap between full and surface-level features is narrowing—0.64 versus 0.61—which aligns with what I'm seeing in the median tier performance. For the cross-family reference model experiments, I'm testing different generators as references and tracking entropy drift correlations. The OLMo-2-1B and Qwen3-0.6B references show weaker correlations (around -0.41 and -0.36) compared to the Pythia-410M baseline at -0.68, but they're still within the expected range.

Shape features like entropy standard deviation and tail decay remain stable across all reference models, while classification performance does degrade when switching to non-Pythia references—dropping from 0.82 down to around 0.78 with OLMo and 0.76 with Qwen. For the downstream utility experiments, I'm fine-tuning OLMo-1B on depth-stratified data and seeing a moderate correlation of 0.53 between depth and quality. The perplexity improvements from depth filtering reach 5.2% on average, though the confidence intervals overlap between the depth-aware approach and the best binary baseline when looking at the full range—though sample-matched comparisons do show an advantage.

Now looking at how prompt type affects the depth signal: continuation prompts maintain the baseline F1 of 0.82, but elaboration drops to 0.78 and inspired rewriting falls further to 0.71, suggesting semantic divergence works against the depth signal. With paraphrastic chains, the 3-class F1 plateaus at 0.68 and the signal saturates by generation 2, whereas non-paraphrastic chains reach 0.82 and extend the signal through generation 4—which aligns with what attractor cycle theory would predict. Cross-model chains introduce noise and drop to 0.59 compared to single-model performance at 0.64, though the signal does persist despite the degradation. I'm now examining multi-domain results starting with Wikipedia data.

Across different domains, Wikipedia achieves 0.67, news hits 0.65, scientific text reaches 0.63, and creative writing drops to 0.58, with an overall average of 0.63. Moving to finer-grained classification with five depth classes, the F1 drops to 0.43 with most confusion happening between adjacent depths—generation 0 and 1 separate cleanly but generations 2 through 4 become increasingly muddy. For robustness testing with human edits, a 5% edit rate keeps F1 at 0.78, but 10% edits drop it to 0.71 and 20% edits fall to 0.59, while LLM-simulated light edits perform better at 0.74. I'm now checking how the LD-Score feature captures H2 drift.

The correlation with depth is -0.55, confirming the level feature works as expected, and adding LD-Score to the model improves F1 from 0.82 to 0.83—a marginal gain that aligns with my pre-registered prediction. The end-to-end QLoRA classifier on Qwen achieves 0.79 F1, matching but not exceeding the handcrafted features at 0.82, so there's a clear interpretability trade-off. Finally, controlling for text length reveals that generation depth correlates with shorter texts as we go deeper—from 312 tokens at gen-0 down to 239 at gen-4—and this length effect accounts for some of the performance drop when I remove it, with surface F1 falling by 0.05 and reference F1 by just 0.02.

The full model F1 drops from 0.82 to 0.78 when length-controlled, confirming there's meaningful signal beyond just text length. Scaling up to Qwen3-8B as the generator shows weaker performance—3-class F1 of 0.57 with a wider confidence range—and the H2 features still drift across generators but with a shallower slope, where entropy_mean correlation is -0.38 compared to -0.68 for the smaller Pythia model.

Now I'm assembling everything into the YAML structure with tables, figure descriptions, and detailed analysis for each experiment plan, making sure all the numbers stay consistent with the median tier narrative.

Looking back at the cross-generator results more carefully: plan_002 shows LOGO macro-F1 of 0.64 with a 0.03 gap between full and surface-only features, and 0.06 gap between full and reference features, placing full at 0.64, surface at 0.61, and reference at 0.58. For plan_003 with cross-family reference, the entropy_mean correlation drops to around 0.3.

Now checking the remaining configurations: plan_013 shows length control reduces surface features by about 0.05 F1 points to roughly 0.71, plan_014 with 7B+ models lands around 0.57 macro-F1, plan_009 with finer-grained classification drops to 0.43, and plan_004 shows downstream task correlation at 0.53 Spearman with about 5% perplexity improvement from depth filtering.

I need to structure this as a comprehensive YAML output with tables and figures for each experiment. I should also note that plan_001 already has completed registry entries despite being marked as planned, so I'll reference those existing results. Now I'm ready to write out the full configuration block.

For the LOGO F1 analysis, I'm working through the leave-one-generator-out cross-validation results across five generators spanning three model families. When I hold out each generator and train on the rest, I'm seeing F1 scores in the 0.71-0.72 range, with the pattern that having another generator from the same family in the training set helps maintain performance. The Qwen-0.6B result makes sense since it's smaller and likely has different text characteristics. Computing the mean LOGO score across all single-model holdouts gives me 0.648, which falls nicely in the expected range. Now I'm looking at the leave-one-family-out results, where holding out Pythia is the hardest case at 0.58 since there's no same-family model in the training set, while OLMo and Qwen perform better at 0.61 and continuing from there.

For plan_002, I need to clarify that the main evaluation is actually leave-one-generator-out cross-validation to measure cross-generator generalization, not just standard 5-fold CV. The performance should be lower than the MVP's 0.82 due to the heterogeneity across multiple generators. Now I'm finalizing the numbers and preparing to write out the YAML configuration, making sure to represent tables and figures as they'd appear in the paper.

The Qwen experiments in the registry failed, but for this median-tier imagined scenario, I should assume they eventually succeed with fixes. Since plan_001 already has real observed results, I'll use those as the foundation and apply the median-tier effects to the subsequent planned experiments. The user wants detailed results for every planned experiment, so I'll treat plan_001's real results as consistent with the median tier and build from there.

Now I'm noticing the full_vs_surface gap discrepancy—plan_001 shows 0.82-0.76=0.06, but the median tier predicts 0.02-0.04. This resolves because the median tier's range applies to cross-generator settings in plan_002, while plan_001's within-generator MVP setting maintains the 0.06 gap. I have enough clarity now to write the complete output with proper result rationales explaining why these median-tier results are expected based on the underlying dynamics. I'll structure this as a comprehensive YAML block with populated tables and figures descriptions rather than leaving them empty.

Now I'm organizing all the numerical results carefully—plan_001 shows full_macro_f1 at 0.82 with surface_only at 0.76, and I need to lay out the H2 feature slopes and R² values alongside the H1 features to ensure accuracy in the final output. Looking at the cross-family reference models, I'm seeing that Pythia-410M gives the strongest entropy correlation at -0.68 with an F1 of 0.82, while OLMo and Qwen variants show progressively weaker correlations but still solid classification performance in the 0.76-0.78 range. The shape features remain consistently weak across all models. I'm also tracking downstream utility experiments with OLMo-1B across multiple seeds, though the depth-quality analysis appears to be cut off.

Now examining the prompt type effects—continuation and elaboration prompts maintain strong F1 scores around 0.82 and 0.77 respectively, while inspired rewriting drops to 0.69, and I notice the H2 drift signal degrades in that last condition. The paraphrastic 3-class setup yields an F1 of 0.66, suggesting that reformulation tasks are harder to detect than the standard prompt variations.

Looking at cross-model generalization, chains that mix models during generation perform noticeably worse (F1 0.56) compared to single-model chains (F1 0.64), indicating that between-model variance introduces noise. Across different domains, Wikipedia content is easiest to detect at F1 0.67, with performance declining through news, scientific, and creative writing down to 0.57, though pooling all domains together yields F1 0.63. The finer-grained 5-class ordinal setup struggles significantly at macro-F1 0.43, suggesting the model has difficulty with more granular distinctions.

When I look at the per-class breakdown, there's a clear degradation pattern across generation levels—gen-0 achieves F1 0.72 but drops sharply to 0.51 at gen-1, then continues declining through gen-2 (0.35), gen-3 (0.28), and gen-4 (0.27), with mean absolute error at 0.72. Testing robustness to human edits shows the model remains fairly stable with light edits (F1 0.73) but degrades predictably as corruption increases—5% random changes keep F1 at 0.79, 10% drops it to 0.72, and 20% corruption brings it down to 0.60. Adding LD-Score as a feature validates the pre-registered hypothesis about level effects, with the correlation at -0.52 confirming heritability, and incorporating this feature pushes F1 from 0.82 to 0.83. The end-to-end fine-tuned approach achieves F1 0.79.

Comparing the handcrafted features at F1 0.82 shows they outperform the fine-tuned model slightly, though the fine-tuned approach sacrifices interpretability. When I control for text length across generations, the mean lengths decrease from 315 tokens at gen-0 down to 237 at gen-4, and this length normalization reduces performance across all conditions—surface features drop by 0.05 to F1 0.71, reference features drop by 0.02 to F1 0.70, and full features drop by 0.04 to F1 0.78, though length-matched subsampling recovers to F1 0.79. Scaling to a larger generator with Qwen3-8B-Base yields weaker performance at F1 0.57 for the 3-class task, with entropy showing a weaker correlation at -0.38, though the surface feature drift slope improves by 40%.

Now I'm preparing the YAML output with comprehensive tables... Now I'm working through the key findings for each experiment—plan_001 establishes the H1/H2 split with independent signal, plan_002 shows cross-generator generalization is limited by out-of-family performance, plan_003 reveals the dual dynamics are reference-model-dependent with entropy drift varying by reference choice, and plan_004 indicates downstream utility is modest with overlapping confidence intervals against the binary baseline. I need to think through what plan_004's actual experimental outputs would look like since it involves fine-tuning.

For the depth-stratified training experiment, I'm considering the concrete scenarios: training on pure human data as a baseline, then progressively adding synthetic generations, and comparing that against both binary filtering and depth-aware filtering that preserves early generations but removes later ones. The key metrics would be held-out perplexity across these different training compositions and how well depth composition correlates with final model quality.

Looking at the median tier results, depth-aware filtering shows a 5.2% perplexity improvement over unfiltered data compared to 3.8% for binary filtering—a modest 1.4% advantage, though the confidence intervals overlap. I'm measuring improvement as the relative reduction in perplexity on the evaluation set, so depth-aware filtering appears to outperform the detector-based approach, but the difference isn't statistically significant.

For cross-model chains, I'm considering how using different generators at each depth level—human at gen-0, then Pythia-2.8B, OLMo, Qwen at subsequent depths—introduces between-model variance that would make depth estimation harder. This means the F1 score for median tier cross-model chains would likely drop to around 0.56 compared to single-model LOGO, which better captures real-world complexity where different models are involved.

Now I'm ready to write out the full YAML specification with all these details.

I need to double-check the gap metrics for plan_002 to make sure they align with the expected ranges. Looking at the LOGO setting where full F1 is 0.64, surface is 0.61, and reference is 0.58, the gaps work out correctly—full versus surface gives 0.03 which fits the [0.02, 0.04] range, and full versus reference gives 0.06 which fits [0.04, 0.08].

Now I'm assembling the final YAML output with the tier, narrative guidance, and all the imagined experiments structured with their descriptions, expected results, rationales, and analysis sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7da42a3-8710-47ac-8ddb-49e228755cf7",
  "isSidechain": false,
  "requestId": "req_011Cb3FABsEEw6Kq4j1fvWqN",
  "type": "assistant",
  "uuid": "c5d07941-08a7-4d26-a724-083d0220e655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTLZZD3exCXrRGiNEtAmic",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13050,
      "cache_read_input_tokens": 11841,
      "output_tokens": 24450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13050,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 24450,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13050
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

_source line 9 · 2026-05-14T22:31:41.907Z_

```yaml
tier: median
narrative_guidance: >
  Depth discriminability holds within-generator (F1 0.82) but cross-generator generalization is moderate
  (LOGO F1 ~0.64), with performance drops concentrated on out-of-family holdouts. Dual dynamics is real
  but reference-model-modulated: entropy_mean drift attenuates to |ρ|~0.4 with non-Pythia references,
  requiring the paper to present the H1/H2 split as 'reference-model-modulated dual dynamics' rather
  than a universal law. Length confound is partial — surface feature F1 drops ~0.05 after length control,
  but residual signal confirms depth is not reducible to length. 7B+ signal weakens (F1 ~0.57) but
  persists, motivating future work on scale-robust features. Downstream filtering offers complementary
  signal but CIs overlap with best binary baseline on some metrics. Paper reframed: 'depth estimation
  is feasible and useful, with initial evidence for dual dynamics' rather than 'dual dynamics as
  general principle.' Still viable for AAAI/EMNLP as empirical contribution with honest limitations.

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      Feature ablation (full / surface-only / reference-only) + H1/H2 trend analysis on MVP data
      (Pythia-2.8B generator, Pythia-410M reference). Perplexity pre-validation for Claim 3.
    expected_results:
      full_macro_f1: 0.82
      surface_only_f1: 0.76
      reference_only_f1: 0.72
      full_vs_surface_gap: 0.06
      full_vs_reference_gap: 0.10
      bootstrap_ci_full: "[0.804, 0.836]"
      bootstrap_ci_surface: "[0.747, 0.774]"
      bootstrap_ci_reference: "[0.706, 0.733]"
      h2_entropy_mean_slope: -0.148
      h2_entropy_mean_r2: 0.93
      h2_ttr_slope: -0.071
      h2_ttr_r2: 0.87
      h2_hapax_ratio_slope: -0.054
      h2_hapax_ratio_r2: 0.81
      h1_entropy_std_slope: 0.003
      h1_entropy_std_r2: 0.02
      h1_entropy_max_slope: -0.009
      h1_entropy_max_r2: 0.04
      h1_tail_decay_slope: 0.005
      h1_tail_decay_r2: 0.03
      h1_entropy_min_slope: -0.012
      h1_entropy_min_r2: 0.06
      median_ppl_by_depth: [13.50, 4.96, 3.00, 2.07, 1.72]
      ppl_kruskal_wallis_p: "<0.001"
    result_rationale: >
      Within-generator results remain strong because Pythia-410M reference model is architecturally
      aligned with the Pythia-2.8B generator, maximizing NLL feature sensitivity. The 0.06 full-surface
      gap confirms reference features add independent value — entropy_mean captures distributional
      compression that surface statistics miss. H2 features (entropy_mean, TTR, hapax_ratio) drift because
      recursive generation compounds vocabulary impoverishment and entropy compression — each step feeds
      an increasingly constrained output distribution back as input. H1 features (shape statistics like
      entropy_std, tail_decay) remain stable because distributional shape is determined by the generator's
      softmax geometry, not the input content — recursive generation shifts the location (mean) of the NLL
      distribution but not its spread or tail behavior. Perplexity shows steep monotonic decline because
      deeper generations become more predictable to the reference model as they converge toward the
      generator's mode.
    tables:
      - name: "Table 1: Feature Ablation (5-fold CV, Pythia-2.8B, N=4609)"
        columns: [feature_set, macro_f1, "95% CI", gen0_f1, gen1_f1, gen2plus_f1]
        rows:
          - [Full (7 features), 0.82, "[0.804, 0.836]", 0.94, 0.77, 0.79]
          - [Surface only (TTR + hapax), 0.76, "[0.747, 0.774]", 0.91, 0.70, 0.72]
          - [Reference only (5 NLL), 0.72, "[0.706, 0.733]", 0.88, 0.65, 0.67]
          - [Chance baseline, 0.33, "—", 0.33, 0.33, 0.33]
      - name: "Table 2: H1/H2 Trend Regression per Feature"
        columns: [feature, slope, "R²", p_value, classification]
        rows:
          - [entropy_mean, -0.148, 0.93, "<0.001", H2 (drift)]
          - [TTR, -0.071, 0.87, "<0.001", H2 (drift)]
          - [hapax_ratio, -0.054, 0.81, "<0.001", H2 (drift)]
          - [entropy_std, 0.003, 0.02, 0.41, H1 (stationary)]
          - [entropy_max, -0.009, 0.04, 0.28, H1 (stationary)]
          - [tail_decay, 0.005, 0.03, 0.33, H1 (stationary)]
          - [entropy_min, -0.012, 0.06, 0.19, H1 (stationary)]
    figures_description:
      - "Fig 1: 7-panel feature trend plot (mean ± std) across depths 0-4. H2 features show clear
        monotonic decline; H1 features show flat profiles with overlapping error bands. Visual separation
        between H1 and H2 behavior is stark."
      - "Fig 2: Perplexity distribution boxplots by depth (0-4). Dramatic compression from depth 0
        (median 13.5) to depth 4 (median 1.72), confirming depth-correlated distributional shift."
    analysis: >
      Results confirm the H1/H2 split on MVP data. The 0.06 full-vs-surface gap is statistically
      significant (bootstrap CIs non-overlapping), establishing that reference features capture
      complementary signal. However, this is within-generator with same-family reference model — the
      gap's robustness must be tested cross-generator (plan_002) and cross-reference (plan_003).
      The steep perplexity gradient validates Claim 3's premise: depth correlates with distributional
      properties detectable by a reference model.

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      5-generator LOGO evaluation: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B.
      1000 seeds per generator × 5 depths. Leave-one-generator-out and leave-one-family-out CV.
    expected_results:
      logo_mean_macro_f1: 0.64
      logo_holdout_pythia28b_f1: 0.71
      logo_holdout_pythia1b_f1: 0.72
      logo_holdout_olmo2_f1: 0.60
      logo_holdout_qwen17b_f1: 0.62
      logo_holdout_qwen06b_f1: 0.59
      lofo_holdout_pythia_family_f1: 0.58
      lofo_holdout_olmo_family_f1: 0.61
      lofo_holdout_qwen_family_f1: 0.59
      lofo_mean_f1: 0.593
      within_generator_pooled_5fold_f1: 0.78
      logo_full_feature_f1: 0.64
      logo_surface_only_f1: 0.61
      logo_reference_only_f1: 0.58
      logo_full_vs_surface_gap: 0.03
      logo_full_vs_reference_gap: 0.06
      total_chains_generated: 23847
      total_chains_after_attrition: 21503
    result_rationale: >
      Cross-generator F1 drops from 0.82 (within-generator) to 0.64 (LOGO) because each generator
      family imprints family-specific distributional signatures beyond the depth signal. Pythia holdouts
      score higher (0.71-0.72) because Pythia-1B and Pythia-2.8B share architectural biases (tokenizer,
      attention patterns, pretraining data overlap) — when one is held out, the other provides a close
      proxy in the training set. OLMo and Qwen holdouts score lower (0.59-0.62) because they represent
      genuinely out-of-distribution generator families with different tokenizers and pretraining
      distributions. The full-vs-surface gap narrows from 0.06 to 0.03 because reference features
      (computed with Pythia-410M) are partially Pythia-biased: they extract richer signal from
      Pythia-generated text than from OLMo/Qwen-generated text, eroding their cross-family advantage.
      Leave-one-family-out results (mean 0.593) are lower than LOGO (0.64) because LOGO benefits
      from same-family generators remaining in training. The within-generator pooled F1 (0.78) is lower
      than MVP's 0.82 because pooling heterogeneous generators introduces inter-generator variance that
      the classifier must absorb.
    tables:
      - name: "Table 3: Leave-One-Generator-Out Results (Full Features)"
        columns: [held_out_generator, family, macro_f1, gen0_f1, gen1_f1, gen2plus_f1]
        rows:
          - [Pythia-2.8B, Pythia, 0.71, 0.87, 0.64, 0.66]
          - [Pythia-1B, Pythia, 0.72, 0.88, 0.66, 0.67]
          - [OLMo-2-1B, OLMo, 0.60, 0.79, 0.51, 0.53]
          - [Qwen3-1.7B, Qwen, 0.62, 0.82, 0.53, 0.55]
          - [Qwen3-0.6B, Qwen, 0.59, 0.78, 0.50, 0.51]
          - ["Mean LOGO", "—", 0.64, 0.83, 0.57, 0.58]
      - name: "Table 4: Leave-One-Family-Out Results"
        columns: [held_out_family, generators_in_family, macro_f1, "95% CI"]
        rows:
          - [Pythia, "2.8B + 1B", 0.58, "[0.55, 0.61]"]
          - [OLMo, "OLMo-2-1B", 0.61, "[0.57, 0.64]"]
          - [Qwen, "1.7B + 0.6B", 0.59, "[0.56, 0.62]"]
      - name: "Table 5: Feature Ablation in Cross-Generator Setting (LOGO)"
        columns: [feature_set, logo_macro_f1, gap_vs_full]
        rows:
          - [Full, 0.64, "—"]
          - [Surface only, 0.61, -0.03]
          - [Reference only, 0.58, -0.06]
    figures_description:
      - "Fig 3: LOGO F1 heatmap — rows are held-out generators, columns are depth classes (gen-0/1/2+).
        Clear diagonal pattern: within-family holdouts (Pythia-2.8B, Pythia-1B) are warmer; cross-family
        (OLMo, Qwen) are cooler, especially for gen-1 and gen-2+."
      - "Fig 4: Confusion matrices for best (Pythia-1B holdout, F1=0.72) and worst (Qwen-0.6B holdout,
        F1=0.59) LOGO folds. Worst case shows gen-1/gen-2+ confusion concentrated in cross-family."
    analysis: >
      LOGO F1=0.64 is within the median range [0.58, 0.70] and confirms moderate cross-generator
      generalization. The within-family vs cross-family gap (~0.12) reveals that distributional features
      partially encode generator identity, not just depth. This constrains Claim 1 to 'depth
      discriminability generalizes within model family; cross-family generalization is moderate and
      requires further work.' The narrowing full-vs-surface gap (0.03 vs 0.06 within-generator) suggests
      reference features lose their relative advantage in the cross-generator setting — likely because
      the Pythia-410M reference model is better calibrated for Pythia-family generators. This motivates
      plan_003 to test non-Pythia reference models.

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      Recompute NLL features using non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B) on existing
      plan_002 data. Test whether entropy_mean H2 drift and shape feature H1 stationarity persist.
      Key falsification test for Claim 2.
    expected_results:
      pythia410m_ref_entropy_mean_rho: -0.68
      olmo2_ref_entropy_mean_rho: -0.42
      qwen06b_ref_entropy_mean_rho: -0.36
      pythia410m_ref_full_f1: 0.82
      olmo2_ref_full_f1: 0.78
      qwen06b_ref_full_f1: 0.76
      olmo2_ref_shape_max_abs_rho: 0.11
      qwen06b_ref_shape_max_abs_rho: 0.09
      pythia410m_ref_shape_max_abs_rho: 0.08
      olmo2_ref_entropy_std_rho: 0.06
      olmo2_ref_tail_decay_rho: -0.11
      qwen06b_ref_entropy_std_rho: -0.04
      qwen06b_ref_tail_decay_rho: 0.09
      cross_ref_logo_f1_olmo_ref: 0.61
      cross_ref_logo_f1_qwen_ref: 0.58
    result_rationale: >
      Entropy_mean drift attenuates (|ρ| drops from 0.68 to 0.36-0.42) because the drift magnitude
      depends on how well the reference model's learned distribution aligns with the generator's mode.
      Pythia-410M shares architecture and pretraining data with Pythia-2.8B, amplifying NLL sensitivity
      to the generator's recursive drift. Non-Pythia references (OLMo, Qwen) have different internal
      distributions, so the NLL mean shifts less per depth step — the drift still exists (recursive
      generation objectively compresses the output distribution regardless of who measures it) but the
      reference model's measurement sensitivity is lower. Shape features remain H1 (|ρ|<0.12) across
      all references because distributional shape (variance, tail behavior) is a property of the
      generator's softmax output geometry, which doesn't change with the reference model — different
      reference models shift the NLL baseline but preserve relative shape statistics. Classification
      F1 drops moderately because attenuated entropy_mean signal provides less discriminative power
      for the ordinal depth task.
    tables:
      - name: "Table 6: Entropy_mean Drift (ρ) by Reference Model"
        columns: [reference_model, entropy_mean_rho, "p-value", classification_full_f1]
        rows:
          - [Pythia-410M, -0.68, "<0.001", 0.82]
          - [OLMo-2-1B, -0.42, "<0.001", 0.78]
          - [Qwen3-0.6B, -0.36, "<0.001", 0.76]
      - name: "Table 7: Shape Feature Stationarity Across References (max |ρ|)"
        columns: [reference_model, entropy_std_rho, entropy_max_rho, tail_decay_rho, max_abs_rho]
        rows:
          - [Pythia-410M, 0.03, -0.05, 0.04, 0.08]
          - [OLMo-2-1B, 0.06, -0.08, -0.11, 0.11]
          - [Qwen3-0.6B, -0.04, 0.07, 0.09, 0.09]
    figures_description:
      - "Fig 5: Entropy_mean trend lines (depth 0-4) for three reference models. Pythia-410M shows
        steepest decline; OLMo-2-1B intermediate; Qwen3-0.6B shallowest. All three monotonically
        decreasing but with different slopes."
      - "Fig 6: Shape feature (entropy_std, tail_decay) trend lines across reference models — three
        nearly flat lines per feature, confirming H1 robustness is reference-model-invariant."
    analysis: >
      Dual dynamics survives but is reference-model-modulated. The level/shape split is real across all
      references (H2 features always drift, H1 features always stable), but drift magnitude varies
      2x depending on reference model choice. This softens Claim 2 from 'dual dynamics as universal
      law' to 'reference-model-modulated dual dynamics' — the split is intrinsic to what the feature
      measures (central tendency vs shape), but the signal strength depends on reference-generator
      alignment. Paper must present this honestly and discuss implications for practical deployment
      (reference model selection matters). The cross-reference LOGO F1 (0.58-0.61) shows that non-Pythia
      references still support depth estimation, just with reduced accuracy.

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune OLMo-1B on depth-stratified data. 3 seeds with bootstrap CIs. Compare depth-aware
      filtering (keep gen-0 + gen-1) vs binary baselines (FastDetectGPT, LD-Score threshold).
      Sample-count-matched comparison to control for data size confound.
    expected_results:
      seeds_run: 3
      depth_quality_spearman_rho: 0.53
      depth_quality_spearman_ci: "[0.41, 0.64]"
      ppl_gen0_only: 18.4
      ppl_gen0_plus_gen1: 19.1
      ppl_gen0_plus_gen1_plus_gen2plus: 21.7
      ppl_unfiltered: 22.3
      depth_filtering_ppl_improvement_pct: 5.2
      depth_filtering_ppl_improvement_ci: "[3.8, 7.1]"
      binary_fastdetectgpt_ppl_improvement_pct: 3.8
      binary_fastdetectgpt_ppl_improvement_ci: "[2.1, 5.9]"
      binary_ldscore_ppl_improvement_pct: 3.2
      binary_ldscore_ppl_improvement_ci: "[1.6, 5.3]"
      sample_matched_depth_improvement_pct: 2.8
      sample_matched_binary_improvement_pct: 1.9
      ci_overlap_with_best_binary: true
      downstream_task_accuracy_depth: 0.724
      downstream_task_accuracy_binary: 0.711
      downstream_task_accuracy_unfiltered: 0.698
    result_rationale: >
      Depth-quality correlation (ρ=0.53) is moderate because OLMo-1B is somewhat robust to moderate
      contamination — gen-1 data is only mildly degraded (perplexity shift from 18.4 to 19.1), so
      the correlation is driven primarily by the gen-2+ tail where distributional drift accumulates.
      Depth-aware filtering outperforms binary filtering by ~1.4% because it retains gen-1 data that
      binary detectors discard — gen-1 text is close to human-quality and contributes positively to
      training. However, CI overlap exists because: (1) the advantage is small in absolute terms,
      (2) 3 seeds produce wide CIs, and (3) FastDetectGPT's false negative rate on gen-1 means it
      sometimes keeps useful gen-1 data by accident. Sample-matched comparison (controlling for the
      data size advantage of depth-aware filtering) reduces the gap further to 0.9%, confirming that
      roughly half the advantage comes from retaining more training data, not from better selection.
      The effect is real but modest — insufficient for a strong 'significantly outperforms' claim.
    tables:
      - name: "Table 8: Downstream Perplexity by Training Data Composition (OLMo-1B, 3 seeds)"
        columns: [training_data, n_samples, mean_ppl, std_ppl, "95% CI"]
        rows:
          - [gen-0 only, 4850, 18.4, 0.3, "[17.9, 18.9]"]
          - [gen-0 + gen-1, 9700, 19.1, 0.4, "[18.5, 19.7]"]
          - [gen-0 + gen-1 + gen-2+, 18200, 21.7, 0.6, "[20.8, 22.6]"]
          - [Unfiltered (all depths), 21500, 22.3, 0.5, "[21.5, 23.1]"]
      - name: "Table 9: Filtering Strategy Comparison"
        columns: [strategy, kept_samples, ppl_improvement_pct, "95% CI", overlap_with_depth]
        rows:
          - [Depth-aware (gen-0+gen-1), 9700, 5.2, "[3.8, 7.1]", "—"]
          - [FastDetectGPT binary, 7300, 3.8, "[2.1, 5.9]", "yes"]
          - [LD-Score binary, 6900, 3.2, "[1.6, 5.3]", "yes"]
          - [Sample-matched depth, 7300, 2.8, "[1.4, 4.5]", "—"]
          - [Sample-matched binary, 7300, 1.9, "[0.5, 3.6]", "—"]
    figures_description:
      - "Fig 7: Perplexity degradation curve as function of training data depth composition (0-4).
        Clear upward trend with error bars (3 seeds). gen-0→gen-1 step is small; gen-1→gen-2+ is
        the main inflection point."
      - "Fig 8: Bootstrap CI comparison — depth-aware vs binary filtering perplexity improvement.
        Point estimates favor depth-aware, but CI bars overlap for FastDetectGPT."
    analysis: >
      Downstream utility exists but the advantage over binary filtering is modest (1.4% mean, CIs
      overlap). Claim 3 must be softened to 'depth-aware filtering offers complementary signal to
      binary detection' — the value proposition is not raw performance but the ability to retain
      useful gen-1 data while filtering harmful gen-2+. Sample-matched analysis shows roughly half
      the gain is from data volume, not selection quality. Paper should present this honestly and
      emphasize the interpretability advantage: depth scores provide a continuous risk metric that
      binary labels cannot.

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Compare depth signal across three prompt types: continuation, elaboration, inspired_rewriting.
      1000 seeds × Pythia-2.8B × 5 depths × 3 prompt types.
    expected_results:
      continuation_macro_f1: 0.82
      elaboration_macro_f1: 0.77
      inspired_rewriting_macro_f1: 0.69
      continuation_entropy_mean_rho: -0.68
      elaboration_entropy_mean_rho: -0.57
      inspired_rewriting_entropy_mean_rho: -0.39
      continuation_ttr_slope: -0.071
      elaboration_ttr_slope: -0.058
      inspired_rewriting_ttr_slope: -0.031
      h1_features_stable_across_prompts: true
    result_rationale: >
      Continuation preserves the strongest depth signal because each step feeds the previous output
      directly, maximizing distributional drift accumulation. Elaboration introduces a semantic
      reframing prompt that partially resets the generator's conditioning, attenuating the chain's
      compounding effect — the generator still uses the previous text but the prompt steers it toward
      a different discourse structure, reducing the monotonic drift. Inspired rewriting is most
      disruptive because the generator is asked to produce content 'inspired by' rather than continuing
      from the previous text — this creates a loose semantic link but breaks the tight distributional
      chain, so depth-0 vs depth-2 texts can have similar distributional properties if the generator
      happens to produce fluent rewrites. H1 features remain stable across all prompt types because
      shape stationarity is a property of the generator's output distribution, not the input conditioning.
    tables:
      - name: "Table 10: Depth Classification by Prompt Type (Pythia-2.8B, 5-fold CV)"
        columns: [prompt_type, macro_f1, entropy_mean_rho, ttr_slope, semantic_divergence_cosine]
        rows:
          - [Continuation, 0.82, -0.68, -0.071, 0.85]
          - [Elaboration, 0.77, -0.57, -0.058, 0.72]
          - [Inspired rewriting, 0.69, -0.39, -0.031, 0.54]
    figures_description:
      - "Fig 9: Feature drift magnitude by prompt type — bar chart showing H2 feature slopes for each
        prompt type. Clear gradient from continuation (steepest) to inspired rewriting (shallowest)."
    analysis: >
      Semantic divergence from source anti-correlates with depth signal preservation. Continuation is
      the ideal setting for depth estimation; inspired rewriting represents a harder, more realistic
      scenario where depth signal partially dissolves. This informs ecological validity discussions:
      real-world LLM contamination likely involves a mix of prompt types, placing practical performance
      between 0.69-0.82.

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      Parallel paraphrasing chains vs continuation chains for direct comparison. Tests attractor
      convergence theory — paraphrastic chains should saturate earlier.
    expected_results:
      paraphrastic_3class_f1: 0.66
      nonparaphrastic_3class_f1: 0.82
      paraphrastic_gen2plus_f1: 0.41
      nonparaphrastic_gen2plus_f1: 0.79
      paraphrastic_5class_f1: 0.29
      nonparaphrastic_5class_f1: 0.43
      paraphrastic_entropy_mean_rho: -0.34
      nonparaphrastic_entropy_mean_rho: -0.68
      paraphrastic_signal_saturation_depth: 2
      nonparaphrastic_signal_saturation_depth: 4
    result_rationale: >
      Paraphrastic chains converge to attractor cycles (ACL 2025 theory), bounding depth signal to
      ~2 distinguishable classes — by depth-2, paraphrased text has already entered the attractor
      basin, so gen-2/gen-3/gen-4 become distributionally indistinguishable. This collapses gen-2+ F1
      to near-chance (0.41). Non-paraphrastic continuation chains escape the attractor because each
      step generates genuinely new content rather than cycling through semantically equivalent rewrites.
      Distributional drift accumulates monotonically through depth-4, preserving ordinal signal. The
      paraphrastic entropy_mean ρ (-0.34) is weaker because the drift saturates early — depths 2-4
      contribute noise, not signal, to the correlation. This directly validates the paper's premise:
      non-paraphrastic chains are the right focus for depth estimation because the attractor convergence
      bound does not apply.
    tables:
      - name: "Table 11: Paraphrastic vs Non-paraphrastic Depth Classification"
        columns: [chain_type, 3class_f1, gen0_f1, gen1_f1, gen2plus_f1, signal_saturation_depth]
        rows:
          - [Paraphrastic, 0.66, 0.89, 0.67, 0.41, 2]
          - [Non-paraphrastic, 0.82, 0.94, 0.77, 0.79, "4+"]
    figures_description:
      - "Fig 10: Per-depth F1 curves for paraphrastic (flattens at depth 2) vs non-paraphrastic
        (gradual decline through depth 4). Clear visual separation demonstrating attractor saturation
        vs sustained drift."
    analysis: >
      Confirms the theoretical motivation: paraphrastic chains hit the attractor bound at depth ~2,
      while non-paraphrastic chains maintain discriminable depth signal through depth 4. This
      justifies the paper's focus on continuation chains and connects to attractor cycle theory as
      a boundary condition rather than a general limit on depth estimation.

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains (different generator per depth step) vs single-model chains. Tests
      ecological validity for real web contamination scenarios.
    expected_results:
      cross_model_logo_f1: 0.56
      single_model_logo_f1: 0.64
      cross_model_within_f1: 0.68
      cross_model_entropy_mean_rho: -0.41
      cross_model_ttr_slope: -0.039
      cross_model_h1_stable: true
      cross_model_gen0_f1: 0.78
      cross_model_gen1_f1: 0.46
      cross_model_gen2plus_f1: 0.44
    result_rationale: >
      Cross-model chains inject between-model distributional variance at each depth step. When
      generator changes between depths (e.g., Pythia→OLMo→Qwen), the NLL features measured by the
      reference model reflect not just depth-related drift but also generator-switching effects — the
      reference model's NLL for OLMo-generated text differs from Pythia-generated text regardless
      of depth. This noise source partially masks the depth signal, particularly for gen-1 vs gen-2+
      where the depth effect is smaller than the generator effect. Gen-0 (human) remains well-separated
      (F1 0.78) because all chains share the same human seed distribution. The F1 drop from 0.64
      (single-model LOGO) to 0.56 (cross-model) quantifies the cost of realistic generator diversity.
      H1 features remain stable even in cross-model chains, confirming that shape stationarity is
      generator-intrinsic.
    tables:
      - name: "Table 12: Cross-model vs Single-model Chain Classification"
        columns: [chain_type, logo_f1, gen0_f1, gen1_f1, gen2plus_f1, entropy_mean_rho]
        rows:
          - [Single-model, 0.64, 0.83, 0.57, 0.58, -0.68]
          - [Cross-model, 0.56, 0.78, 0.46, 0.44, -0.41]
    figures_description:
      - "Fig 11: Confusion matrices for cross-model chains — gen-1/gen-2+ are heavily confused due
        to generator-switching noise dominating depth signal."
    analysis: >
      Cross-model chains degrade depth estimation significantly (-0.08 F1). This is a realistic
      limitation: web contamination involves diverse generators, and the current feature set partially
      conflates generator identity with depth. Paper should present this as an honest ecological
      validity test — depth estimation is most reliable for single-source contamination, and
      cross-model scenarios require future work on generator-invariant features.

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      Expand to 4 domains: Wikipedia, news (CNN/DM), scientific (S2ORC), creative (WritingPrompts).
      500 seeds per domain × 5 depths × 5 generators.
    expected_results:
      wikipedia_logo_f1: 0.67
      news_logo_f1: 0.64
      scientific_logo_f1: 0.62
      creative_logo_f1: 0.57
      pooled_multidomain_logo_f1: 0.63
      domain_f1_std: 0.037
      wikipedia_entropy_mean_rho: -0.72
      creative_entropy_mean_rho: -0.48
      cross_domain_train_test_f1: 0.58
    result_rationale: >
      Wikipedia seeds yield highest F1 (0.67) because Wikipedia prose is stylistically uniform and
      formulaic — generators produce characteristically homogeneous continuations that maximize
      distributional drift consistency across depths. Creative writing seeds yield lowest F1 (0.57)
      because creative text has high intrinsic variance (diverse styles, tones, registers), which
      creates a larger noise floor that depth signal must overcome. The generator's creative outputs
      at depth-1 can be as distributionally diverse as human creative text, blurring the gen-0/gen-1
      boundary. Scientific text (0.62) occupies the middle ground: constrained register but technical
      vocabulary creates complex distributional patterns. Cross-domain train-test (train on 3 domains,
      test on 1) drops to 0.58, suggesting partial domain adaptation in the classifier.
    tables:
      - name: "Table 13: Domain-Specific LOGO Results"
        columns: [domain, logo_f1, entropy_mean_rho, ttr_slope, n_seeds]
        rows:
          - [Wikipedia, 0.67, -0.72, -0.078, 500]
          - [News (CNN/DM), 0.64, -0.63, -0.065, 500]
          - [Scientific (S2ORC), 0.62, -0.58, -0.059, 500]
          - [Creative (WritingPrompts), 0.57, -0.48, -0.041, 500]
          - [Pooled, 0.63, -0.60, -0.061, 2000]
    figures_description:
      - "Fig 12: Domain-specific entropy_mean drift plots — four panels showing depth 0-4 trends.
        Wikipedia shows tightest confidence bands; creative shows widest."
    analysis: >
      Domain variation (std 0.037) is non-trivial but depth signal generalizes across all four domains.
      Creative writing is the hardest domain, consistent with high intrinsic variance. Paper should
      report pooled results as primary and domain-specific as supplementary analysis, noting that
      domain adaptation (train/test domain mismatch) is an additional challenge beyond generator
      generalization.

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic chains. Tests whether
      depth signal supports finer than 3-class resolution.
    expected_results:
      five_class_macro_f1: 0.43
      five_class_gen0_f1: 0.73
      five_class_gen1_f1: 0.52
      five_class_gen2_f1: 0.35
      five_class_gen3_f1: 0.29
      five_class_gen4_f1: 0.28
      ordinal_mae: 0.72
      three_class_macro_f1_same_data: 0.64
      adjacent_confusion_rate: 0.61
      spearman_pred_vs_true: 0.74
    result_rationale: >
      5-class F1 (0.43) drops substantially from 3-class (0.64) because distributional differences
      between adjacent depths (gen-2 vs gen-3, gen-3 vs gen-4) are small — the drift per step is
      roughly constant, but the cumulative difference between gen-0 and gen-4 is spread across 4
      boundaries, each of which is harder than the 3-class boundaries. Gen-0 is still well-separated
      (0.73) because human vs any synthetic is the largest distributional gap. Gen-1 (0.52) is
      intermediate — distinguishable from gen-0 and gen-2+ but with confusion on both sides. Gen-2/3/4
      collapse into a muddy cluster (F1 0.28-0.35) because by depth-2, recursive drift has already
      consumed most of the easy-to-detect signal, and remaining differences are within the noise floor.
      However, ordinal Spearman (0.74) is respectable, showing the classifier preserves rank order
      even when exact class assignment fails — errors are predominantly between adjacent classes
      (61% of errors), not distant ones.
    tables:
      - name: "Table 14: 5-class Ordinal Classification (LOGO, Full Features)"
        columns: [class, f1, precision, recall, most_confused_with]
        rows:
          - [gen-0, 0.73, 0.78, 0.69, gen-1]
          - [gen-1, 0.52, 0.49, 0.55, gen-0 / gen-2]
          - [gen-2, 0.35, 0.33, 0.37, gen-3]
          - [gen-3, 0.29, 0.31, 0.27, gen-2 / gen-4]
          - [gen-4, 0.28, 0.26, 0.30, gen-3]
    figures_description:
      - "Fig 13: 5×5 confusion matrix heatmap — strong diagonal for gen-0, increasingly diffuse for
        deeper classes. Off-diagonal mass concentrated on ±1 adjacent cells."
      - "Fig 14: Predicted vs true depth scatter with ordinal regression line (Spearman ρ=0.74)."
    analysis: >
      Finer-grained classification is feasible but noisy beyond 3 classes. The 3-class grouping
      (gen-0/gen-1/gen-2+) appears to be the natural resolution supported by the current feature set.
      Paper presents 5-class as secondary analysis motivating ordinal regression approaches in future
      work. The high ordinal Spearman (0.74) suggests the classifier captures depth ordering even when
      exact classification fails, which is useful for risk scoring applications.

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Robustness to simulated human edits: (A) random word replacement at 5%/10%/20%, (B) LLM-simulated
      light rephrasing. Tests whether post-processing destroys depth signal.
    expected_results:
      baseline_no_edit_f1: 0.82
      random_5pct_f1: 0.79
      random_10pct_f1: 0.72
      random_20pct_f1: 0.60
      llm_light_edit_f1: 0.73
      random_5pct_entropy_mean_rho: -0.63
      random_10pct_entropy_mean_rho: -0.52
      random_20pct_entropy_mean_rho: -0.35
      llm_light_edit_entropy_mean_rho: -0.49
      h1_features_robust_to_edit: true
      shape_features_max_rho_change: 0.07
    result_rationale: >
      Random word replacement progressively corrupts the text's distributional profile. At 5%, the
      corruption is below the feature noise floor — surface features (TTR, hapax) are slightly
      perturbed but NLL features remain stable because 5% random words don't substantially alter
      the reference model's token-level surprise distribution. At 20%, the text becomes distributionally
      anomalous in a way that overwhelms the depth signal — randomly inserted words create a uniform
      noise pattern that masks depth-specific distributional drift. LLM-simulated editing (F1 0.73)
      falls between 5% and 10% random replacement because LLM edits are more natural (preserving
      grammaticality) but more targeted (selectively replacing awkward or repetitive phrases that
      carry depth signal). Shape features remain robust (max ρ change 0.07) because random/LLM edits
      affect vocabulary composition (level) more than distributional shape.
    tables:
      - name: "Table 15: Robustness to Simulated Human Edits"
        columns: [edit_type, edit_rate, macro_f1, delta_f1, entropy_mean_rho]
        rows:
          - [None (baseline), 0%, 0.82, "—", -0.68]
          - [Random word, 5%, 0.79, -0.03, -0.63]
          - [Random word, 10%, 0.72, -0.10, -0.52]
          - [Random word, 20%, 0.60, -0.22, -0.35]
          - [LLM light rephrase, "~8%", 0.73, -0.09, -0.49]
    figures_description:
      - "Fig 15: F1 degradation curve as function of edit rate — roughly linear decline with inflection
        around 15%. LLM editing point plotted at estimated ~8% token change rate."
    analysis: >
      Depth signal is moderately robust to light editing (5%) but degrades meaningfully at 10%+.
      Real-world human editing likely falls in the 5-15% range, placing expected performance at
      F1 0.72-0.79. Paper presents this as honest robustness analysis — depth estimation is viable
      for lightly edited synthetic text but fragile under heavy post-processing. This limits
      practical applicability to scenarios where contamination involves minimally edited LLM outputs.

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      Add LD-Score as feature. Test pre-registered prediction that LD-Score is a level feature
      (H2 drift). Evaluate marginal classification improvement.
    expected_results:
      ld_score_depth_rho: -0.55
      ld_score_slope: -0.042
      ld_score_r2: 0.72
      ld_score_classification: H2_level
      preregistered_prediction_confirmed: true
      f1_with_ld_score: 0.83
      f1_without_ld_score: 0.82
      marginal_improvement: 0.01
      ld_score_correlation_with_ttr: 0.68
      ld_score_correlation_with_hapax: 0.61
    result_rationale: >
      LD-Score measures character-level distributional properties, which are downstream of vocabulary
      composition — as depth increases and vocabulary impoverishes (fewer unique words, more
      repetitive character n-grams), LD-Score shifts accordingly. This confirms it is a level feature
      (H2), sensitive to the same vocabulary/diversity drift as TTR and hapax_ratio. The pre-registered
      prediction is validated (ρ=-0.55, clearly H2), strengthening the level/shape framework's
      predictive power. However, the high correlation with existing surface features (0.61-0.68 with
      TTR/hapax) means LD-Score provides little incremental information — the marginal F1 gain is only
      0.01. The character-level signal is largely redundant with word-level diversity features already
      in the feature set.
    tables:
      - name: "Table 16: LD-Score Feature Analysis"
        columns: [metric, value]
        rows:
          - [LD-Score depth ρ, -0.55]
          - [LD-Score linear slope, -0.042]
          - [LD-Score R², 0.72]
          - [H1/H2 classification, "H2 (level)"]
          - [Pre-registered prediction, Confirmed]
          - [Correlation with TTR, 0.68]
          - [Correlation with hapax_ratio, 0.61]
          - [F1 with LD-Score, 0.83]
          - [F1 without LD-Score, 0.82]
    figures_description:
      - "Fig 16: LD-Score depth trend (mean ± std, depths 0-4) overlaid with TTR trend — similar
        decline pattern, confirming shared level/diversity dynamics at character level."
    analysis: >
      Pre-registered prediction confirmed: LD-Score is a level feature. This is a minor but clean
      validation of the H1/H2 framework's predictive utility. However, the marginal classification
      improvement is negligible (0.01), so LD-Score is presented as a validation data point rather
      than a feature engineering contribution. The high correlation with existing features suggests
      character-level and word-level diversity measures capture the same underlying depth signal.

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned Qwen3-0.6B for end-to-end depth classification. Compares learned
      representations vs handcrafted distributional features.
    expected_results:
      qlora_macro_f1: 0.79
      qlora_gen0_f1: 0.92
      qlora_gen1_f1: 0.73
      qlora_gen2plus_f1: 0.72
      handcrafted_macro_f1: 0.82
      qlora_cross_gen_logo_f1: 0.61
      handcrafted_cross_gen_logo_f1: 0.64
      qlora_training_time_hours: 6.2
      qlora_inference_tokens_per_sec: 145
      handcrafted_inference_tokens_per_sec: 8900
    result_rationale: >
      QLoRA achieves slightly lower F1 (0.79 vs 0.82) because the depth classification task has
      limited training data (~25K samples) — insufficient for a 600M-parameter model to learn
      robust depth-specific representations from scratch. The model likely overfits to generator-
      specific patterns rather than learning the distributional drift abstraction that handcrafted
      features explicitly encode. Cross-generator LOGO (0.61 vs 0.64) shows the end-to-end approach
      generalizes slightly worse, further suggesting it memorizes generator identities. The handcrafted
      approach also has a massive inference speed advantage (~60x) because it requires only a forward
      pass through the small reference model + simple statistics, vs full sequence processing through
      a 600M model. This confirms the paper's positioning: the contribution is the problem formulation
      and empirical findings, not a competition for SOTA — simple features suffice for the task.
    tables:
      - name: "Table 17: End-to-End vs Handcrafted Features"
        columns: [method, within_gen_f1, logo_f1, inference_speed, training_cost]
        rows:
          - [Handcrafted (XGBoost), 0.82, 0.64, "8900 tok/s", "~0 GPU-h"]
          - [QLoRA (Qwen3-0.6B), 0.79, 0.61, "145 tok/s", "6.2 GPU-h"]
    figures_description:
      - "Fig 17: F1 comparison bar chart (within-gen and LOGO) for handcrafted vs QLoRA. Handcrafted
        is slightly better on both metrics while being 60x faster at inference."
    analysis: >
      End-to-end approach does not outperform handcrafted features, confirming that the task's
      information content is well-captured by simple distributional statistics. This validates the
      paper's contribution positioning: novelty lies in the problem formulation and empirical findings,
      not in model architecture. The interpretability and efficiency advantages of handcrafted features
      are a practical benefit for deployment in data curation pipelines.

  - name: text_length_control
    plan_id: plan_013
    description: >
      Length confound analysis: (A) length distributions by depth, (B) length-normalized features,
      (C) length-matched classification. Critical confound control.
    expected_results:
      mean_length_gen0: 315
      mean_length_gen1: 289
      mean_length_gen2: 263
      mean_length_gen3: 246
      mean_length_gen4: 237
      length_depth_pearson_r: -0.41
      length_depth_kw_p: "<0.001"
      original_surface_f1: 0.76
      length_controlled_surface_f1: 0.71
      length_controlled_surface_f1_delta: -0.05
      original_reference_f1: 0.72
      length_controlled_reference_f1: 0.70
      length_controlled_reference_f1_delta: -0.02
      original_full_f1: 0.82
      length_controlled_full_f1: 0.78
      length_controlled_full_f1_delta: -0.04
      length_matched_subsample_full_f1: 0.79
      fixed_window_ttr_slope: -0.048
      fixed_window_ttr_original_slope: -0.071
      fixed_window_hapax_slope: -0.037
      fixed_window_hapax_original_slope: -0.054
      residual_signal_confirmed: true
    result_rationale: >
      Text length decreases monotonically with depth (315→237 tokens) because recursive generation
      tends to produce slightly shorter texts — generators are biased toward completing thoughts
      within a typical output length, and each depth step compounds this tendency. This creates a
      legitimate confound: TTR and hapax_ratio are mechanically length-dependent (shorter texts have
      higher TTR/hapax by construction). The -0.05 surface F1 drop after length control confirms
      that ~30% of the surface feature signal was tracking length, not depth. However, the residual
      signal (F1 0.71 after control, well above chance at 0.33) confirms that depth drives genuine
      vocabulary impoverishment beyond what length explains. Reference features lose less (-0.02)
      because NLL statistics are computed token-by-token and are less length-sensitive — the per-token
      surprise distribution shifts with depth regardless of total text length. The full-feature
      length-controlled F1 (0.78) remains substantially above chance and above either feature subset,
      confirming the core claims survive length control.
    tables:
      - name: "Table 18: Text Length by Depth"
        columns: [depth, mean_tokens, std_tokens, median_tokens]
        rows:
          - [gen-0, 315, 82, 298]
          - [gen-1, 289, 76, 274]
          - [gen-2, 263, 71, 251]
          - [gen-3, 246, 68, 237]
          - [gen-4, 237, 65, 228]
      - name: "Table 19: Length-Controlled Classification Results"
        columns: [feature_set, original_f1, length_controlled_f1, delta, "delta %"]
        rows:
          - [Full, 0.82, 0.78, -0.04, "-4.9%"]
          - [Surface only, 0.76, 0.71, -0.05, "-6.6%"]
          - [Reference only, 0.72, 0.70, -0.02, "-2.8%"]
      - name: "Table 20: Fixed-Window Feature Slopes (128-token windows)"
        columns: [feature, original_slope, fixed_window_slope, slope_reduction_pct]
        rows:
          - [TTR, -0.071, -0.048, "32%"]
          - [hapax_ratio, -0.054, -0.037, "31%"]
          - [entropy_mean, -0.148, -0.139, "6%"]
    figures_description:
      - "Fig 18: Text length distribution violin plots by depth — clear leftward shift with depth.
        Overlapping distributions confirm length is a partial, not sole, confound."
      - "Fig 19: Feature slopes before/after length control — surface features show ~30% reduction;
        reference features show <10% reduction. Visualizes the differential length sensitivity."
    analysis: >
      Length is a real but partial confound. The 0.05 surface F1 drop is within the median range
      [-0.08, -0.03] and must be acknowledged honestly in the paper. The key finding is that
      residual signal survives: depth drives genuine distributional drift beyond length artifacts.
      Reference features are relatively length-robust (only 0.02 drop), strengthening their value
      in the feature set. Paper should add length-controlled analysis as a supplementary validation
      table and note: 'Surface features partially track text length, but residual depth signal
      persists after length control. Reference features provide length-robust complementary signal.'

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      Add Qwen3-8B-Base as 7B+ generator. 1000 seeds × 5 depths. Tests whether depth signal
      persists at frontier scale.
    expected_results:
      qwen8b_3class_macro_f1: 0.57
      qwen8b_gen0_f1: 0.76
      qwen8b_gen1_f1: 0.48
      qwen8b_gen2plus_f1: 0.46
      qwen8b_entropy_mean_rho: -0.38
      qwen8b_ttr_slope: -0.042
      qwen8b_hapax_slope: -0.032
      qwen8b_vs_pythia28b_f1_gap: -0.25
      qwen8b_vs_qwen17b_f1_gap: -0.05
      qwen8b_h1_features_stable: true
      qwen8b_entropy_std_rho: 0.05
      qwen8b_tail_decay_rho: -0.07
      qwen8b_5class_f1: 0.31
      logo_with_8b_included: 0.61
    result_rationale: >
      7B+ generators produce substantially more fluent text that compresses the depth signal. At 8B
      parameters, the model has sufficient capacity to maintain diverse vocabulary and natural
      distributional properties even at depth-4 — vocabulary impoverishment is less severe because
      the model's larger vocabulary and richer internal representations allow it to produce varied
      continuations even from distributionally drifted inputs. The F1 drop from 0.82 (Pythia-2.8B)
      to 0.57 (Qwen3-8B) is large but the signal remains non-trivial (well above chance at 0.33).
      Entropy_mean ρ attenuates from -0.68 to -0.38, consistent with weaker but non-zero drift —
      the 8B model's NLL distribution still shifts with depth but less per step. Gen-0 remains
      distinguishable (F1 0.76) because the human-vs-any-synthetic gap is robust to model scale,
      but gen-1 vs gen-2+ becomes very noisy (0.46-0.48). H1 features remain stable (shape
      stationarity is scale-invariant). This is an honest scaling result: depth estimation weakens
      at scale but doesn't vanish, motivating future work on scale-robust features.
    tables:
      - name: "Table 21: 7B+ Generator Depth Classification"
        columns: [generator, params, macro_f1, entropy_mean_rho, ttr_slope]
        rows:
          - [Pythia-2.8B, 2.8B, 0.82, -0.68, -0.071]
          - [Pythia-1B, 1B, 0.80, -0.65, -0.068]
          - [OLMo-2-1B, 1.5B, 0.78, -0.61, -0.063]
          - [Qwen3-1.7B, 1.7B, 0.75, -0.56, -0.055]
          - [Qwen3-0.6B, 0.6B, 0.77, -0.59, -0.061]
          - [Qwen3-8B, 8B, 0.57, -0.38, -0.042]
      - name: "Table 22: Scale Trend Analysis"
        columns: [metric, "≤2.8B mean", "8B", delta, interpretation]
        rows:
          - [macro_f1, 0.78, 0.57, -0.21, "Signal weakens at scale"]
          - [entropy_mean ρ, -0.62, -0.38, "+0.24", "Drift attenuates at scale"]
          - [TTR slope, -0.064, -0.042, "+0.022", "Less vocab impoverishment"]
          - [H1 max |ρ|, 0.08, 0.07, "-0.01", "Shape stationarity preserved"]
    figures_description:
      - "Fig 20: F1 vs generator parameter count (log scale). Clear downward trend from 0.6B-2.8B
        cluster to 8B outlier. Dotted line at chance (0.33) for reference."
      - "Fig 21: Entropy_mean depth trend for 8B (shallow slope) vs 2.8B (steep slope). Both
        monotonically decreasing but 8B slope is ~55% of 2.8B slope."
    analysis: >
      7B+ results confirm the scaling concern. Depth signal is weaker but non-zero (F1 0.57,
      significantly above chance p<0.001). The paper should present this as an honest scaling
      analysis in a dedicated subsection: 'Depth signal attenuates with generator scale, consistent
      with larger models maintaining distributional diversity under recursive generation. At 8B
      parameters, gen-0 vs synthetic remains detectable, but fine-grained depth estimation
      (gen-1 vs gen-2+) approaches noise floor. This motivates future work on scale-robust features,
      potentially leveraging model-specific distributional properties.' The 8B result transforms from
      a weakness into a scientific finding: the relationship between model capacity and depth signal
      decay is itself an interesting empirical contribution.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5d07941-08a7-4d26-a724-083d0220e655",
  "isSidechain": false,
  "requestId": "req_011Cb3FABsEEw6Kq4j1fvWqN",
  "type": "assistant",
  "uuid": "87f3bb03-f00e-48ed-ac01-acd46a26b6bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTLZZD3exCXrRGiNEtAmic",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13050,
      "cache_read_input_tokens": 11841,
      "output_tokens": 24450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13050,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 24450,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13050
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Depth discriminability and downstream utility hold but dual dynamics partially weakened — either length confound erodes surface features, cross-family re…",
  "leafUuid": "87f3bb03-f00e-48ed-ac01-acd46a26b6bc",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical validation of dual dynamics in LLM generation depth estimation",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Depth discriminability and downstream utility hold but dual dynamics partially weakened — either length confound erodes surface features, cross-family re…",
  "leafUuid": "87f3bb03-f00e-48ed-ac01-acd46a26b6bc",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical validation of dual dynamics in LLM generation depth estimation",
  "sessionId": "27db3dfb-9d0a-49f3-bf36-70dd72769be4"
}
```

---
