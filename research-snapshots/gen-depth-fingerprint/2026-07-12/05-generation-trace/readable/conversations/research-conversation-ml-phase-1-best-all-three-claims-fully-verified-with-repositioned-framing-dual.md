# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：All three claims fully verified with repositioned framing — dual dynamics ge

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/4fc48029-56d5-4e7d-b665-816eb1ee8426.jsonl`
- **Structured JSON:** [`e61034e34f7c748920db.json`](../../sessions/e6/e61034e34f7c748920db.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T22:17:02.790Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T22:17:02.790Z",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：All three claims fully verified with repositioned framing — dual dynamics generalizes across generators, reference models, and scales; downstream utility significant with proper controls\n核心假设：['Cross-generator leave-one-out macro-F1 remains competitive (≥0.70), confirming depth signal is generator-agnostic', 'Entropy_mean H2 drift persists with non-Pythia reference models (plan_003), confirming dual dynamics is generation-intrinsic not reference-model artifact', 'Length-controlled surface features retain most discriminability (F1 drop <0.03), ruling out length confound as primary driver', '7B+ generator (plan_014) shows comparable depth signal to ≤2.8B, establishing scale generalization', 'Downstream depth-aware filtering significantly outperforms binary baselines with CIs non-overlapping (plan_004, OLMo-1B, ≥3 seeds)', 'Full > surface-only > reference-only ablation gap holds under cross-generator setting, not just single-generator MVP']\n关键指标范围：{'cross_gen_logo_macro_f1': [0.7, 0.78], 'cross_family_ref_entropy_mean_rho': [-0.75, -0.55], 'length_controlled_f1_delta': [-0.03, 0.0], 'full_vs_surface_f1_gap': [0.04, 0.08], 'full_vs_reference_f1_gap': [0.08, 0.12], 'downstream_depth_quality_spearman': [0.65, 0.85], 'depth_filtering_perplexity_improvement_pct': [8, 20], 'generator_7bplus_macro_f1': [0.65, 0.78], 'finer_5class_macro_f1': [0.5, 0.65]}\n叙事方向：Original framing fully intact. Empirical contribution positioned as: (1) new task formulation (ordinal depth estimation), (2) dual dynamics discovery that cross-cuts surface/reference boundary — validated across generator families, reference models, and scales, (3) practical depth-aware curation with significant downstream gains. Paper reads as clean empirical science paper with surprising finding + immediate utility. Dual dynamics is the headline — 'what features measure matters more than where they come from' holds as a general principle. 30+ references anchor the work in OOD detection + model collapse + data quality literatures. AAAI/EMNLP accept as strong empirical contribution.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nfocus: D006 re-dream after framing repositioning. Key changes: (1) contribution explicitly positioned as empirical/conceptual not methodological — features are standard NLL stats, novelty is in problem formulation + dual dynamics finding + application; (2) OOD detection connection acknowledged (RC8); (3) text length confound controlled (plan_013); (4) downstream utility uses OLMo-1B not Pythia-410M to avoid reference model circularity, multiple seeds + CIs required (RC11); (5) 7B+ generator added as P1 (plan_014, RC9); (6) related work must be 30+ references. Verify whether these changes address the structural issues that caused Best=5/Median=5/Worst=4 in previous dream.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that \"reference-model features = robust, surface features = fragile.\" The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are \"better\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: \"fingerprint\" in the paper refers to the full feature vector's combination, not just reference-model features.\n\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\n\n**RC9 — \"Only ≤2.8B generators — does this transfer to frontier scale?\"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.\n\n**RC10 — \"Text length confound\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\n\n**RC11 — \"Downstream utility — single run, no CIs\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\n\n## Contribution Positioning (Dream D006 insight)\nThe contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection\n2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary\n3. **Practical application**: Risk-stratified data curation outperforming binary filtering\n\nDo NOT overclaim \"distributional fingerprinting\" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.\n\nRelated work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).\n\n## Venue Fit\n- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T22:17:02.797Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T22:17:02.797Z",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-14T22:17:02.831Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：All three claims fully verified with repositioned framing — dual dynamics generalizes across generators, reference models, and scales; downstream utility significant with proper controls
核心假设：['Cross-generator leave-one-out macro-F1 remains competitive (≥0.70), confirming depth signal is generator-agnostic', 'Entropy_mean H2 drift persists with non-Pythia reference models (plan_003), confirming dual dynamics is generation-intrinsic not reference-model artifact', 'Length-controlled surface features retain most discriminability (F1 drop <0.03), ruling out length confound as primary driver', '7B+ generator (plan_014) shows comparable depth signal to ≤2.8B, establishing scale generalization', 'Downstream depth-aware filtering significantly outperforms binary baselines with CIs non-overlapping (plan_004, OLMo-1B, ≥3 seeds)', 'Full > surface-only > reference-only ablation gap holds under cross-generator setting, not just single-generator MVP']
关键指标范围：{'cross_gen_logo_macro_f1': [0.7, 0.78], 'cross_family_ref_entropy_mean_rho': [-0.75, -0.55], 'length_controlled_f1_delta': [-0.03, 0.0], 'full_vs_surface_f1_gap': [0.04, 0.08], 'full_vs_reference_f1_gap': [0.08, 0.12], 'downstream_depth_quality_spearman': [0.65, 0.85], 'depth_filtering_perplexity_improvement_pct': [8, 20], 'generator_7bplus_macro_f1': [0.65, 0.78], 'finer_5class_macro_f1': [0.5, 0.65]}
叙事方向：Original framing fully intact. Empirical contribution positioned as: (1) new task formulation (ordinal depth estimation), (2) dual dynamics discovery that cross-cuts surface/reference boundary — validated across generator families, reference models, and scales, (3) practical depth-aware curation with significant downstream gains. Paper reads as clean empirical science paper with surprising finding + immediate utility. Dual dynamics is the headline — 'what features measure matters more than where they come from' holds as a general principle. 30+ references anchor the work in OOD detection + model collapse + data quality literatures. AAAI/EMNLP accept as strong empirical contribution.

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
  "promptId": "b31cb076-ce0a-49c6-b272-c8ffd64b2269",
  "type": "user",
  "uuid": "04678fb6-9eaf-466f-940b-9667b9f92791",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T22:17:02.827Z_

```json
{
  "parentUuid": "04678fb6-9eaf-466f-940b-9667b9f92791",
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
  "uuid": "96176ec2-176d-4177-b6f2-1062ee485bd3",
  "timestamp": "2026-05-14T22:17:02.827Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T22:17:02.827Z_

```json
{
  "parentUuid": "96176ec2-176d-4177-b6f2-1062ee485bd3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "90e9f21f-22be-445f-8ae3-05d8ebe1876f",
  "timestamp": "2026-05-14T22:17:02.827Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All three claims fully verified with repositioned framing — dual dynamics generalizes across generators, reference models, and scales; downstream utility s…",
  "leafUuid": "90e9f21f-22be-445f-8ae3-05d8ebe1876f",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "ML depth fingerprint multi-generator empirical validation",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

### Assistant

_source line 8 · 2026-05-14T22:17:22.380Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for the "best" tier across all planned experiments in the experiment_plan. Let me carefully go through each planned experiment and generate realistic predictions based on the best-tier definition.

Let me first understand the best tier:
- All three claims fully verified with repositioned framing
- Dual dynamics generalizes across generators, reference models, and scales
- Downstream utility significant with proper controls

Key metric ranges for best tier:
- cross_gen_logo_macro_f1: [0.70, 0.78]
- cross_family_ref_entropy_mean_rho: [-0.75, -0.55]


- length_controlled_f1_delta: [-0.03, 0.0]
- full_vs_surface_f1_gap: [0.04, 0.08]
- full_vs_reference_f1_gap: [0.08, 0.12]
- downstream_depth_quality_spearman: [0.65, 0.85]
- depth_filtering_perplexity_improvement_pct: [8, 20]
- generator_7bplus_macro_f1: [0.65, 0.78]
- finer_5class_macro_f1: [0.50, 0.65]

Now I'm working through each planned experiment to construct realistic best-tier results.

I've got the completed work so far: mvp-001 hit 0.8408 macro F1, plan-001 finished with full/surface/reference scores of 0.8204/0.7628/0.7187, and plan-002 is currently running with Pythia-1B and OLMo-2 shards done but Qwen generation hitting issues. The remaining experiments span cross-generator evaluation, reference model families, downstream utility, prompt variations, paraphrastic comparisons, and cross-model chains.

Now I need to generate realistic expected results for all the planned experiments through plan-014, making sure the numbers fall within best-tier ranges and are grounded in what we've already achieved.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90e9f21f-22be-445f-8ae3-05d8ebe1876f",
  "isSidechain": false,
  "requestId": "req_011Cb3EbWdBL1vpVcUBhTwo1",
  "type": "assistant",
  "uuid": "e7595468-ed5d-4f4e-a275-a6221b937d73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014kwttBi4CyPca1o15TRfzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12948,
      "cache_read_input_tokens": 11841,
      "output_tokens": 995,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 995,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12948
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

_source line 9 · 2026-05-14T22:17:22.384Z_

Let me review the existing experiment data and registry to ground the predictions properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7595468-ed5d-4f4e-a275-a6221b937d73",
  "isSidechain": false,
  "requestId": "req_011Cb3EbWdBL1vpVcUBhTwo1",
  "type": "assistant",
  "uuid": "734810f5-2023-466c-860a-ce2e436fda49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014kwttBi4CyPca1o15TRfzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12948,
      "cache_read_input_tokens": 11841,
      "output_tokens": 995,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 995,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12948
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

_source line 10 · 2026-05-14T22:17:28.348Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MhrzG5RUr1sFUJixMR3euN`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore project structure and data",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_3, I need to understand the current state of experiments. Find and read:\n1. Any existing results files (look for CSVs, JSONs, or analysis outputs in results/, data/, outputs/ directories or similar)\n2. The registry file (registry.yaml or similar)\n3. The experiment_plan file\n4. paper_framing.md\n5. Any analysis scripts that show feature names, metric calculations, or evaluation logic\n\nReport: (a) exact file paths found, (b) key metric values from completed experiments (mvp-001, plan-001-fix), (c) the feature names used (surface vs reference), (d) any existing analysis outputs that show trend/ablation results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "734810f5-2023-466c-860a-ce2e436fda49",
  "isSidechain": false,
  "requestId": "req_011Cb3EbWdBL1vpVcUBhTwo1",
  "type": "assistant",
  "uuid": "aa264e10-d3c4-462f-a58a-95655624a8a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014kwttBi4CyPca1o15TRfzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12948,
      "cache_read_input_tokens": 11841,
      "output_tokens": 995,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 995,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12948
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

_source line 11 · 2026-05-14T22:18:22.266Z_

<details><summary>↩ Tool result · `toolu_01MhrzG5RUr1sFUJixMR3euN`</summary>

```text
Excellent! Now let me compile the final report with all the information I've gathered:

## Final Report: Current Experiment State

### (a) Exact File Paths Found

**Registry & Configuration:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml` (26.5 KB) — Complete experiment registry with 23 experiments tracked
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/dream_registry.yaml` (2.2 KB) — Dream review tracking
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml` (7.98 KB) — Experiment plan with P0/P1/P2 priorities

**Framing & Planning:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md` (10.1 KB) — Paper framing with 3 core claims, anticipated reviewer concerns (RC1-RC11), and contribution positioning
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md` (3.3 KB) — Key findings, model paths, and lessons learned
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md` (5.0 KB) — Active status tracking
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/report.md` (3.2 KB) — Auto-generated status report

**Analysis Scripts:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ablation_analysis.py` (15.9 KB) — Feature ablation, trend analysis, perplexity pre-validation
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ablation_analysis_fixed.py` (17.6 KB) — Fixed version

**Dream Reports & Analysis Output:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json` (44 KB) — Best-case analysis with dream tier scores
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/experiment_data.json` (37 KB)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/experiment_data.json` (35 KB)

---

### (b) Key Metric Values from Completed Experiments

#### **MVP-001 (DONE)**
Status: COMPLETED 2026-05-14T18:08:20
- **Hypothesis**: Pythia-410M reference model's distributional features can distinguish Pythia-2.8B continuation chains at gen-0/gen-1/gen-2+ with 3-class macro-F1 ≥ 0.45
- **Data**: 4609 records from 995 seeds (1000 initial, 173 skipped)
- **Key Metrics**:
  - `macro_f1: 0.8408` (PASS threshold 0.45)
  - `binary_f1_gen0_vs_gen2plus: 0.8653` (PASS threshold 0.65)
  - `cv_macro_f1: 0.806` ± 0.013 (std)
  - Per-class F1: `gen0_f1: 0.9517`, `gen1_f1: 0.7759`, `gen2plus_f1: 0.7947`

#### **Plan-001-Fix (DONE)**
Status: COMPLETED 2026-05-14T19:34:25
Key Finding: **Dual Dynamics** confirmed (level/diversity drift vs shape stationarity)
- **Feature Ablation Results**:
  - `full_macro_f1: 0.8204` (5-feature set: entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay, ttr, hapax_ratio)
  - `reference_only_f1: 0.7187` (5 reference features: entropy stats + tail_decay)
  - `surface_only_f1: 0.7628` (2 surface features: ttr + hapax_ratio)
  - Bootstrap CI for comparison: `ref_vs_surf_bootstrap_ci: [0.706, 0.733] vs [0.747, 0.774]`
- **Feature Categories by Behavior**:
  - **H2 Features (Drift)**: entropy_mean, ttr, hapax_ratio — monotonic drift with depth
  - **H1 Features (Stationary)**: tail_decay, entropy_std, entropy_max, entropy_min — near-stationary shape
- **Perplexity by Depth** (Pythia-410M reference model):
  - `median_ppl_by_depth: [13.50, 4.96, 3.00, 2.07, 1.72]` (gen-0 through gen-4)

---

### (c) Feature Names Used

**Reference Model Features** (Pythia-410M, NLL-based):
1. `entropy_mean` — Mean negative log likelihood (drift feature, H2)
2. `entropy_std` — Std of NLL (shape feature, H1)
3. `entropy_min` — Minimum NLL observed (shape feature, H1)
4. `entropy_max` — Maximum NLL observed (shape feature, H1)
5. `tail_decay` — Tail probability decay coefficient (shape feature, H1)

**Surface Features** (text statistics):
6. `ttr` — Type-Token Ratio, lexical diversity (drift feature, H2)
7. `hapax_ratio` — Hapax legomena ratio, singleton ratio (drift feature, H2)

**Feature Characterization**:
- **Drift Features (H2)**: Monotonically drift with depth → vocabulary impoverishment + entropy compression
- **Shape Features (H1)**: Remain near-stationary across depths → distributional shape robust to recursive generation
- **Key Insight**: The H1/H2 split is about **what the feature measures** (central tendency vs shape), NOT where it comes from (surface vs reference). `entropy_mean` is reference-derived but drifts (H2), contradicting naive expectations.

---

### (d) Existing Analysis Outputs & Trend/Ablation Results

#### **Ablation Analysis (Plan-001-Fix)**
From the dream report (`experiment_data.json`), the complete ablation shows:

**Table 1: Feature Ablation Results (3-class depth classification)**
| Feature Set | Features | Macro-F1 | gen-0 F1 | gen-1 F1 | gen-2+ F1 | CV std |
|---|---|---|---|---|---|---|
| Reference-only | entropy_{mean,std,min,max}, tail_decay | 0.79 | 0.91 | 0.71 | 0.74 | 0.018 |
| Surface-only | ttr, hapax_ratio | 0.63 | 0.82 | 0.52 | 0.55 | 0.022 |
| Full | All 7 features | 0.87 | 0.96 | 0.81 | 0.83 | 0.012 |
| Δ (ref − surface) | — | +0.16 | +0.09 | +0.19 | +0.19 | — |

**Table 2: Feature Importance (Permutation, Full Model)**
| Feature | Permutation Importance | XGBoost Gain (MVP) |
|---|---|---|
| entropy_mean | 0.28 | 0.22 |
| entropy_std | 0.19 | 0.13 |
| hapax_ratio | 0.14 | 0.30 |
| tail_decay | 0.13 | 0.06 |
| ttr | 0.09 | 0.17 |
| entropy_max | 0.09 | 0.07 |
| entropy_min | 0.08 | 0.06 |

**Key Findings**:
1. Reference features provide **independent signal** beyond surface features (Δ=+0.16 macro-F1, p<0.001)
2. Reference features strongest on gen-1/gen-2+ discrimination (Δ=+0.19 each), weak on gen-0 (Δ=+0.09)
3. Surface features alone achieve F1=0.63 (only vocabulary impoverishment) — not sufficient
4. Full model achieves F1=0.87 (MVP was 0.84) — complementarity confirmed
5. **Permutation importance reranking**: entropy_mean rises to 0.28 (top), hapax_ratio drops to 0.14 — refutes RC1 ("Is this just vocabulary impoverishment?")
6. **Perplexity single-monotonic**: Pythia-410M median PPL = [13.50, 4.96, 3.00, 2.07, 1.72] across depths, no reversal

#### **Cross-Generator Evaluation (Plan-002 Status)**
From dream report (projected results):
- **Leave-One-Generator-Out CV**: Mean macro-F1 = 0.78 ± 0.03
  - Pythia-2.8B held-out: 0.81
  - Pythia-1B held-out: 0.82
  - OLMo-2-1B held-out: 0.77
  - Qwen3.5-2B held-out: 0.76
  - Qwen3.5-0.8B held-out: 0.74 (hardest case)
- **Per-Generator In-Distribution**: 0.85–0.86 macro-F1 (all generators)
- **Data Generated**: 4 generators completed (Pythia-1B, OLMo-2-1B), Qwen models failed with SIGHUP issues

#### **Completed Experiments Summary**
| Exp ID | Status | Data (records/seeds) | Key Finding |
|---|---|---|---|
| mvp-001 | DONE | 4609 / 995 | macro-F1 0.8408, confirms basic hypothesis |
| plan-001 | DONE | 4609 | Dual Dynamics identified (H1/H2 split) |
| plan-001-fix | DONE | 4609 | Full=0.82 > Ref=0.72 vs Surf=0.76 (complementary) |
| plan-002-pythia1b-s0 | DONE | 2286 / 497 | Single-shard generation successful |
| plan-002-pythia1b-s1 | DONE | 2269 / 498 | Single-shard generation successful |
| plan-002-olmo2-s0 | DONE | 2379 / 497 | OLMo-2-1B shard 0 complete |
| plan-002-olmo2-s1 | DONE | 2334 / 498 | OLMo-2-1B shard 1 complete |

#### **Failed Experiments (SIGHUP/tmux Issues)**
Qwen3 models (1.7B, 0.6B) all failed with SIGHUP after ~20-30% completion:
- plan-002-qwen3-1_7b-s0: ~104/498 seeds (21%) — SIGHUP
- plan-002-qwen3-1_7b-s1: ~95/498 seeds (19%) — SIGHUP
- plan-002-qwen17b-retry-s0: ~144/498 seeds (29%) — SIGHUP
- plan-002-qwen17b-retry-s1: ~144/498 seeds (29%) — SIGHUP
- plan-002-qwen06b-s0: ~226/498 seeds (45%) — Process terminated
- plan-002-qwen06b-s1: ~218/498 seeds (44%) — Process terminated

**Root Cause**: Systematic tmux session death (not Python/CUDA errors), likely due to duplicate job submissions or server infra issues on autodl-5090.

---

### Summary of Paper Framing & Claims

**Core Insight**: Non-paraphrastic LLM generation chains exhibit **dual depth dynamics** crossing surface/reference boundary:
- **Level/diversity features** (entropy_mean, ttr, hapax) drift monotonically with depth (H₂)
- **Distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁)
- This split is about **what features measure**, not where they come from — entropy_mean is reference-derived but drifts

**3 Core Claims** (Claim 2 most validated by data):
1. **Claim 1 (Depth Discriminability)**: Distributional features classify text generation depth with macro-F1 significantly above chance, generalizing across generators
2. **Claim 2 (Dual Dynamics)**: Level vs Shape features split independent of surface/reference origin; complementary for classification (0.82 > 0.76/0.72)
3. **Claim 3 (Downstream Utility)**: Predicted depth correlates with fine-tuning quality; depth-aware filtering outperforms binary detection
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa264e10-d3c4-462f-a58a-95655624a8a9",
  "isSidechain": false,
  "promptId": "b31cb076-ce0a-49c6-b272-c8ffd64b2269",
  "type": "user",
  "uuid": "83deeb6c-d8d3-49aa-8082-3f4518cd1fcc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_3, I need to understand the current state of experiments. Find and read:\n1. Any existing results files (look for CSVs, JSONs, or analysis outputs in results/, data/, outputs/ directories or similar)\n2. The registry file (registry.yaml or similar)\n3. The experiment_plan file\n4. paper_framing.md\n5. Any analysis scripts that show feature names, metric calculations, or evaluation logic\n\nReport: (a) exact file paths found, (b) key metric values from completed experiments (mvp-001, plan-001-fix), (c) the feature names used (surface vs reference), (d) any existing analysis outputs that show trend/ablation results.",
    "agentId": "a1cd6f101abedab30",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now let me compile the final report with all the information I've gathered:\n\n## Final Report: Current Experiment State\n\n### (a) Exact File Paths Found\n\n**Registry & Configuration:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml` (26.5 KB) — Complete experiment registry with 23 experiments tracked\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/dream_registry.yaml` (2.2 KB) — Dream review tracking\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml` (7.98 KB) — Experiment plan with P0/P1/P2 priorities\n\n**Framing & Planning:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md` (10.1 KB) — Paper framing with 3 core claims, anticipated reviewer concerns (RC1-RC11), and contribution positioning\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md` (3.3 KB) — Key findings, model paths, and lessons learned\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md` (5.0 KB) — Active status tracking\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/report.md` (3.2 KB) — Auto-generated status report\n\n**Analysis Scripts:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ablation_analysis.py` (15.9 KB) — Feature ablation, trend analysis, perplexity pre-validation\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ablation_analysis_fixed.py` (17.6 KB) — Fixed version\n\n**Dream Reports & Analysis Output:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json` (44 KB) — Best-case analysis with dream tier scores\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/experiment_data.json` (37 KB)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/experiment_data.json` (35 KB)\n\n---\n\n### (b) Key Metric Values from Completed Experiments\n\n#### **MVP-001 (DONE)**\nStatus: COMPLETED 2026-05-14T18:08:20\n- **Hypothesis**: Pythia-410M reference model's distributional features can distinguish Pythia-2.8B continuation chains at gen-0/gen-1/gen-2+ with 3-class macro-F1 ≥ 0.45\n- **Data**: 4609 records from 995 seeds (1000 initial, 173 skipped)\n- **Key Metrics**:\n  - `macro_f1: 0.8408` (PASS threshold 0.45)\n  - `binary_f1_gen0_vs_gen2plus: 0.8653` (PASS threshold 0.65)\n  - `cv_macro_f1: 0.806` ± 0.013 (std)\n  - Per-class F1: `gen0_f1: 0.9517`, `gen1_f1: 0.7759`, `gen2plus_f1: 0.7947`\n\n#### **Plan-001-Fix (DONE)**\nStatus: COMPLETED 2026-05-14T19:34:25\nKey Finding: **Dual Dynamics** confirmed (level/diversity drift vs shape stationarity)\n- **Feature Ablation Results**:\n  - `full_macro_f1: 0.8204` (5-feature set: entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay, ttr, hapax_ratio)\n  - `reference_only_f1: 0.7187` (5 reference features: entropy stats + tail_decay)\n  - `surface_only_f1: 0.7628` (2 surface features: ttr + hapax_ratio)\n  - Bootstrap CI for comparison: `ref_vs_surf_bootstrap_ci: [0.706, 0.733] vs [0.747, 0.774]`\n- **Feature Categories by Behavior**:\n  - **H2 Features (Drift)**: entropy_mean, ttr, hapax_ratio — monotonic drift with depth\n  - **H1 Features (Stationary)**: tail_decay, entropy_std, entropy_max, entropy_min — near-stationary shape\n- **Perplexity by Depth** (Pythia-410M reference model):\n  - `median_ppl_by_depth: [13.50, 4.96, 3.00, 2.07, 1.72]` (gen-0 through gen-4)\n\n---\n\n### (c) Feature Names Used\n\n**Reference Model Features** (Pythia-410M, NLL-based):\n1. `entropy_mean` — Mean negative log likelihood (drift feature, H2)\n2. `entropy_std` — Std of NLL (shape feature, H1)\n3. `entropy_min` — Minimum NLL observed (shape feature, H1)\n4. `entropy_max` — Maximum NLL observed (shape feature, H1)\n5. `tail_decay` — Tail probability decay coefficient (shape feature, H1)\n\n**Surface Features** (text statistics):\n6. `ttr` — Type-Token Ratio, lexical diversity (drift feature, H2)\n7. `hapax_ratio` — Hapax legomena ratio, singleton ratio (drift feature, H2)\n\n**Feature Characterization**:\n- **Drift Features (H2)**: Monotonically drift with depth → vocabulary impoverishment + entropy compression\n- **Shape Features (H1)**: Remain near-stationary across depths → distributional shape robust to recursive generation\n- **Key Insight**: The H1/H2 split is about **what the feature measures** (central tendency vs shape), NOT where it comes from (surface vs reference). `entropy_mean` is reference-derived but drifts (H2), contradicting naive expectations.\n\n---\n\n### (d) Existing Analysis Outputs & Trend/Ablation Results\n\n#### **Ablation Analysis (Plan-001-Fix)**\nFrom the dream report (`experiment_data.json`), the complete ablation shows:\n\n**Table 1: Feature Ablation Results (3-class depth classification)**\n| Feature Set | Features | Macro-F1 | gen-0 F1 | gen-1 F1 | gen-2+ F1 | CV std |\n|---|---|---|---|---|---|---|\n| Reference-only | entropy_{mean,std,min,max}, tail_decay | 0.79 | 0.91 | 0.71 | 0.74 | 0.018 |\n| Surface-only | ttr, hapax_ratio | 0.63 | 0.82 | 0.52 | 0.55 | 0.022 |\n| Full | All 7 features | 0.87 | 0.96 | 0.81 | 0.83 | 0.012 |\n| Δ (ref − surface) | — | +0.16 | +0.09 | +0.19 | +0.19 | — |\n\n**Table 2: Feature Importance (Permutation, Full Model)**\n| Feature | Permutation Importance | XGBoost Gain (MVP) |\n|---|---|---|\n| entropy_mean | 0.28 | 0.22 |\n| entropy_std | 0.19 | 0.13 |\n| hapax_ratio | 0.14 | 0.30 |\n| tail_decay | 0.13 | 0.06 |\n| ttr | 0.09 | 0.17 |\n| entropy_max | 0.09 | 0.07 |\n| entropy_min | 0.08 | 0.06 |\n\n**Key Findings**:\n1. Reference features provide **independent signal** beyond surface features (Δ=+0.16 macro-F1, p<0.001)\n2. Reference features strongest on gen-1/gen-2+ discrimination (Δ=+0.19 each), weak on gen-0 (Δ=+0.09)\n3. Surface features alone achieve F1=0.63 (only vocabulary impoverishment) — not sufficient\n4. Full model achieves F1=0.87 (MVP was 0.84) — complementarity confirmed\n5. **Permutation importance reranking**: entropy_mean rises to 0.28 (top), hapax_ratio drops to 0.14 — refutes RC1 (\"Is this just vocabulary impoverishment?\")\n6. **Perplexity single-monotonic**: Pythia-410M median PPL = [13.50, 4.96, 3.00, 2.07, 1.72] across depths, no reversal\n\n#### **Cross-Generator Evaluation (Plan-002 Status)**\nFrom dream report (projected results):\n- **Leave-One-Generator-Out CV**: Mean macro-F1 = 0.78 ± 0.03\n  - Pythia-2.8B held-out: 0.81\n  - Pythia-1B held-out: 0.82\n  - OLMo-2-1B held-out: 0.77\n  - Qwen3.5-2B held-out: 0.76\n  - Qwen3.5-0.8B held-out: 0.74 (hardest case)\n- **Per-Generator In-Distribution**: 0.85–0.86 macro-F1 (all generators)\n- **Data Generated**: 4 generators completed (Pythia-1B, OLMo-2-1B), Qwen models failed with SIGHUP issues\n\n#### **Completed Experiments Summary**\n| Exp ID | Status | Data (records/seeds) | Key Finding |\n|---|---|---|---|\n| mvp-001 | DONE | 4609 / 995 | macro-F1 0.8408, confirms basic hypothesis |\n| plan-001 | DONE | 4609 | Dual Dynamics identified (H1/H2 split) |\n| plan-001-fix | DONE | 4609 | Full=0.82 > Ref=0.72 vs Surf=0.76 (complementary) |\n| plan-002-pythia1b-s0 | DONE | 2286 / 497 | Single-shard generation successful |\n| plan-002-pythia1b-s1 | DONE | 2269 / 498 | Single-shard generation successful |\n| plan-002-olmo2-s0 | DONE | 2379 / 497 | OLMo-2-1B shard 0 complete |\n| plan-002-olmo2-s1 | DONE | 2334 / 498 | OLMo-2-1B shard 1 complete |\n\n#### **Failed Experiments (SIGHUP/tmux Issues)**\nQwen3 models (1.7B, 0.6B) all failed with SIGHUP after ~20-30% completion:\n- plan-002-qwen3-1_7b-s0: ~104/498 seeds (21%) — SIGHUP\n- plan-002-qwen3-1_7b-s1: ~95/498 seeds (19%) — SIGHUP\n- plan-002-qwen17b-retry-s0: ~144/498 seeds (29%) — SIGHUP\n- plan-002-qwen17b-retry-s1: ~144/498 seeds (29%) — SIGHUP\n- plan-002-qwen06b-s0: ~226/498 seeds (45%) — Process terminated\n- plan-002-qwen06b-s1: ~218/498 seeds (44%) — Process terminated\n\n**Root Cause**: Systematic tmux session death (not Python/CUDA errors), likely due to duplicate job submissions or server infra issues on autodl-5090.\n\n---\n\n### Summary of Paper Framing & Claims\n\n**Core Insight**: Non-paraphrastic LLM generation chains exhibit **dual depth dynamics** crossing surface/reference boundary:\n- **Level/diversity features** (entropy_mean, ttr, hapax) drift monotonically with depth (H₂)\n- **Distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁)\n- This split is about **what features measure**, not where they come from — entropy_mean is reference-derived but drifts\n\n**3 Core Claims** (Claim 2 most validated by data):\n1. **Claim 1 (Depth Discriminability)**: Distributional features classify text generation depth with macro-F1 significantly above chance, generalizing across generators\n2. **Claim 2 (Dual Dynamics)**: Level vs Shape features split independent of surface/reference origin; complementary for classification (0.82 > 0.76/0.72)\n3. **Claim 3 (Downstream Utility)**: Predicted depth correlates with fine-tuning quality; depth-aware filtering outperforms binary detection"
      }
    ],
    "totalDurationMs": 53912,
    "totalTokens": 60413,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2727,
      "cache_read_input_tokens": 54238,
      "output_tokens": 3443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2727
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 3443,
          "cache_read_input_tokens": 54238,
          "cache_creation_input_tokens": 2727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2727,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 0,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "aa264e10-d3c4-462f-a58a-95655624a8a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T22:18:26.627Z_

<details open><summary>🔧 Tool call — Read · `toolu_014z4WzTT6VpTHhPnpeoghQ3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83deeb6c-d8d3-49aa-8082-3f4518cd1fcc",
  "isSidechain": false,
  "requestId": "req_011Cb3EhN5eFG94DRpU2BoFe",
  "type": "assistant",
  "uuid": "ceeade48-e8aa-43e8-a8aa-79e1dab259c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015hfzBKmUo6sDKsuyLegkUD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4435,
      "cache_read_input_tokens": 24789,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4435,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 24789,
          "cache_creation_input_tokens": 4435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4435
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

_source line 13 · 2026-05-14T22:18:26.632Z_

<details><summary>↩ Tool result · `toolu_014z4WzTT6VpTHhPnpeoghQ3`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation",
4	    "description": "Ablation on existing MVP data (4609 records, Pythia-2.8B generator, Pythia-410M reference, Wikipedia seeds). Three conditions: (A) reference-only features (entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay), (B) surface-only features (ttr, hapax_ratio), (C) full 7-feature set. Same XGBoost classifier, 5-fold stratified CV, 3-class (gen-0/gen-1/gen-2+).\n",
5	    "results": {
6	      "ref_only_macro_f1": 0.79,
7	      "ref_only_cv_std": 0.018,
8	      "ref_only_gen0_f1": 0.91,
9	      "ref_only_gen1_f1": 0.71,
10	      "ref_only_gen2plus_f1": 0.74,
11	      "surface_only_macro_f1": 0.63,
12	      "surface_only_cv_std": 0.022,
13	      "surface_only_gen0_f1": 0.82,
14	      "surface_only_gen1_f1": 0.52,
15	      "surface_only_gen2plus_f1": 0.55,
16	      "full_macro_f1": 0.87,
17	      "full_cv_std": 0.012,
18	      "full_gen0_f1": 0.96,
19	      "full_gen1_f1": 0.81,
20	      "full_gen2plus_f1": 0.83,
21	      "ref_minus_surface_delta": 0.16,
22	      "mcnemar_p_ref_vs_surface": 3e-05,
23	      "permutation_importance_entropy_mean": 0.28,
24	      "permutation_importance_entropy_std": 0.19,
25	      "permutation_importance_hapax_ratio": 0.14,
26	      "permutation_importance_ttr": 0.09
27	    },
28	    "tables": [
29	      {
30	        "name": "Table 1: Feature Ablation Results (3-class depth classification)",
31	        "columns": [
32	          "Feature Set",
33	          "Features",
34	          "Macro-F1",
35	          "gen-0 F1",
36	          "gen-1 F1",
37	          "gen-2+ F1",
38	          "CV std"
39	        ],
40	        "rows": [
41	          [
42	            "Reference-only",
43	            "entropy_{mean,std,min,max}, tail_decay",
44	            0.79,
45	            0.91,
46	            0.71,
47	            0.74,
48	            0.018
49	          ],
50	          [
51	            "Surface-only",
52	            "ttr, hapax_ratio",
53	            0.63,
54	            0.82,
55	            0.52,
56	            0.55,
57	            0.022
58	          ],
59	          [
60	            "Full",
61	            "All 7 features",
62	            0.87,
63	            0.96,
64	            0.81,
65	            0.83,
66	            0.012
67	          ],
68	          [
69	            "Δ (ref − surface)",
70	            "—",
71	            "+0.16",
72	            "+0.09",
73	            "+0.19",
74	            "+0.19",
75	            "—"
76	          ]
77	        ]
78	      },
79	      {
80	        "name": "Table 2: Permutation Importance (Full model, 5-fold mean)",
81	        "columns": [
82	          "Feature",
83	          "Permutation Importance",
84	          "XGBoost Gain (MVP)"
85	        ],
86	        "rows": [
87	          [
88	            "entropy_mean",
89	            0.28,
90	            0.22
91	          ],
92	          [
93	            "entropy_std",
94	            0.19,
95	            0.13
96	          ],
97	          [
98	            "hapax_ratio",
99	            0.14,
100	            0.3
101	          ],
102	          [
103	            "tail_decay",
104	            0.13,
105	            0.06
106	          ],
107	          [
108	            "ttr",
109	            0.09,
110	            0.17
111	          ],
112	          [
113	            "entropy_max",
114	            0.09,
115	            0.07
116	          ],
117	          [
118	            "entropy_min",
119	            0.08,
120	            0.06
121	          ]
122	        ]
123	      }
124	    ],
125	    "figures": [],
126	    "analysis": "The ablation cleanly validates Claim 2. The ref-only advantage is strongest on gen-1 (Δ=+0.19) and gen-2+ (Δ=+0.19), the classes where surface features struggle most — TTR/hapax can separate human text from any synthetic text but cannot distinguish depth levels within synthetic text, because vocabulary impoverishment saturates quickly (mostly between gen-0→gen-1). Reference-model entropy features, by contrast, capture cumulative distributional drift that continues to grow between gen-1 and gen-2+. The reranking of feature importance under permutation (entropy_mean rises to 0.28, hapax_ratio drops to 0.14) directly addresses RC1 (\"Is this just vocabulary impoverishment?\") — it is not. The full model's improvement to 0.87 suggests the two feature families capture partially orthogonal information: surface features provide a cheap gen-0 vs rest shortcut, while reference features provide the finer gen-1 vs gen-2+ signal.\n\n\nMVP feature importance (hapax_ratio=0.30) was inflated by XGBoost's split-gain metric, which overweights high-cardinality continuous features with many useful split points. When surface features are ablated, the 5 reference-model features retain macro-F1=0.79 because they directly measure the generator's deviation from the reference model's next-token distribution — a signal that accumulates monotonically with depth as the generator's output drifts further from human text. Entropy_mean captures the average surprise under the reference model (increases with depth as generated text occupies lower-probability regions), while entropy_std captures the increasing variance of surprise (deeper text alternates between familiar patterns and novel drift). Surface features alone (F1=0.63) capture only vocabulary impoverishment — TTR and hapax_ratio decline with depth as generators recycle high-frequency tokens — but this is a weaker, noisier proxy. The 0.16 delta and significant McNemar test confirm reference features carry independent, dominant signal. The full set achieves F1=0.87 (up from MVP's 0.84) because retuned hyperparameters on the same data with proper ablation awareness extract slightly more complementary value. Permutation importance (which avoids split-gain bias) reranks entropy_mean as the top feature.\n"
127	  },
128	  {
129	    "name": "cross_generator_evaluation",
130	    "description": "Generate 25K chains: 1000 Wikipedia seeds × 5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B) × 5 depths. Feature extraction with Pythia-410M reference model. Leave-one-generator-out CV (train on 4 generators, test on held-out generator). Also report per-generator in-distribution results and per-class breakdowns.\n",
131	    "results": {
132	      "leave_one_out_macro_f1_mean": 0.78,
133	      "leave_one_out_macro_f1_std": 0.03,
134	      "leave_one_out_gen1_f1_mean": 0.73,
135	      "leave_one_out_gen2plus_f1_mean": 0.75,
136	      "leave_one_out_gen0_f1_mean": 0.88,
137	      "in_distribution_5fold_macro_f1": 0.86,
138	      "per_generator_held_out": {
139	        "pythia_2_8b": 0.81,
140	        "olmo_2_1b": 0.77,
141	        "qwen3_5_2b": 0.76,
142	        "qwen3_5_0_8b": 0.74,
143	        "pythia_1b": 0.82
144	      },
145	      "total_chains_generated": 24200,
146	      "attrition_rate_pct": 3.2,
147	      "generation_gpu_hours": 18.5
148	    },
149	    "tables": [
150	      {
151	        "name": "Table 3: Leave-One-Generator-Out Cross-Validation",
152	        "columns": [
153	          "Held-out Generator",
154	          "Macro-F1",
155	          "gen-0 F1",
156	          "gen-1 F1",
157	          "gen-2+ F1"
158	        ],
159	        "rows": [
160	          [
161	            "Pythia-2.8B",
162	            0.81,
163	            0.91,
164	            0.75,
165	            0.77
166	          ],
167	          [
168	            "OLMo-2-1B",
169	            0.77,
170	            0.87,
171	            0.72,
172	            0.73
173	          ],
174	          [
175	            "Qwen3.5-2B",
176	            0.76,
177	            0.86,
178	            0.71,
179	            0.72
180	          ],
181	          [
182	            "Qwen3.5-0.8B",
183	            0.74,
184	            0.84,
185	            0.68,
186	            0.7
187	          ],
188	          [
189	            "Pythia-1B",
190	            0.82,
191	            0.92,
192	            0.76,
193	            0.78
194	          ],
195	          [
196	            "Mean ± std",
197	            "0.78 ± 0.03",
198	            "0.88 ± 0.03",
199	            "0.73 ± 0.03",
200	            "0.75 ± 0.03"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceeade48-e8aa-43e8-a8aa-79e1dab259c1",
  "isSidechain": false,
  "promptId": "b31cb076-ce0a-49c6-b272-c8ffd64b2269",
  "type": "user",
  "uuid": "d92fb610-c2dd-4171-85b3-d5e0571e1d3e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation\",\n    \"description\": \"Ablation on existing MVP data (4609 records, Pythia-2.8B generator, Pythia-410M reference, Wikipedia seeds). Three conditions: (A) reference-only features (entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay), (B) surface-only features (ttr, hapax_ratio), (C) full 7-feature set. Same XGBoost classifier, 5-fold stratified CV, 3-class (gen-0/gen-1/gen-2+).\\n\",\n    \"results\": {\n      \"ref_only_macro_f1\": 0.79,\n      \"ref_only_cv_std\": 0.018,\n      \"ref_only_gen0_f1\": 0.91,\n      \"ref_only_gen1_f1\": 0.71,\n      \"ref_only_gen2plus_f1\": 0.74,\n      \"surface_only_macro_f1\": 0.63,\n      \"surface_only_cv_std\": 0.022,\n      \"surface_only_gen0_f1\": 0.82,\n      \"surface_only_gen1_f1\": 0.52,\n      \"surface_only_gen2plus_f1\": 0.55,\n      \"full_macro_f1\": 0.87,\n      \"full_cv_std\": 0.012,\n      \"full_gen0_f1\": 0.96,\n      \"full_gen1_f1\": 0.81,\n      \"full_gen2plus_f1\": 0.83,\n      \"ref_minus_surface_delta\": 0.16,\n      \"mcnemar_p_ref_vs_surface\": 3e-05,\n      \"permutation_importance_entropy_mean\": 0.28,\n      \"permutation_importance_entropy_std\": 0.19,\n      \"permutation_importance_hapax_ratio\": 0.14,\n      \"permutation_importance_ttr\": 0.09\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Feature Ablation Results (3-class depth classification)\",\n        \"columns\": [\n          \"Feature Set\",\n          \"Features\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\",\n          \"CV std\"\n        ],\n        \"rows\": [\n          [\n            \"Reference-only\",\n            \"entropy_{mean,std,min,max}, tail_decay\",\n            0.79,\n            0.91,\n            0.71,\n            0.74,\n            0.018\n          ],\n          [\n            \"Surface-only\",\n            \"ttr, hapax_ratio\",\n            0.63,\n            0.82,\n            0.52,\n            0.55,\n            0.022\n          ],\n          [\n            \"Full\",\n            \"All 7 features\",\n            0.87,\n            0.96,\n            0.81,\n            0.83,\n            0.012\n          ],\n          [\n            \"Δ (ref − surface)\",\n            \"—\",\n            \"+0.16\",\n            \"+0.09\",\n            \"+0.19\",\n            \"+0.19\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Permutation Importance (Full model, 5-fold mean)\",\n        \"columns\": [\n          \"Feature\",\n          \"Permutation Importance\",\n          \"XGBoost Gain (MVP)\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            0.28,\n            0.22\n          ],\n          [\n            \"entropy_std\",\n            0.19,\n            0.13\n          ],\n          [\n            \"hapax_ratio\",\n            0.14,\n            0.3\n          ],\n          [\n            \"tail_decay\",\n            0.13,\n            0.06\n          ],\n          [\n            \"ttr\",\n            0.09,\n            0.17\n          ],\n          [\n            \"entropy_max\",\n            0.09,\n            0.07\n          ],\n          [\n            \"entropy_min\",\n            0.08,\n            0.06\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The ablation cleanly validates Claim 2. The ref-only advantage is strongest on gen-1 (Δ=+0.19) and gen-2+ (Δ=+0.19), the classes where surface features struggle most — TTR/hapax can separate human text from any synthetic text but cannot distinguish depth levels within synthetic text, because vocabulary impoverishment saturates quickly (mostly between gen-0→gen-1). Reference-model entropy features, by contrast, capture cumulative distributional drift that continues to grow between gen-1 and gen-2+. The reranking of feature importance under permutation (entropy_mean rises to 0.28, hapax_ratio drops to 0.14) directly addresses RC1 (\\\"Is this just vocabulary impoverishment?\\\") — it is not. The full model's improvement to 0.87 suggests the two feature families capture partially orthogonal information: surface features provide a cheap gen-0 vs rest shortcut, while reference features provide the finer gen-1 vs gen-2+ signal.\\n\\n\\nMVP feature importance (hapax_ratio=0.30) was inflated by XGBoost's split-gain metric, which overweights high-cardinality continuous features with many useful split points. When surface features are ablated, the 5 reference-model features retain macro-F1=0.79 because they directly measure the generator's deviation from the reference model's next-token distribution — a signal that accumulates monotonically with depth as the generator's output drifts further from human text. Entropy_mean captures the average surprise under the reference model (increases with depth as generated text occupies lower-probability regions), while entropy_std captures the increasing variance of surprise (deeper text alternates between familiar patterns and novel drift). Surface features alone (F1=0.63) capture only vocabulary impoverishment — TTR and hapax_ratio decline with depth as generators recycle high-frequency tokens — but this is a weaker, noisier proxy. The 0.16 delta and significant McNemar test confirm reference features carry independent, dominant signal. The full set achieves F1=0.87 (up from MVP's 0.84) because retuned hyperparameters on the same data with proper ablation awareness extract slightly more complementary value. Permutation importance (which avoids split-gain bias) reranks entropy_mean as the top feature.\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"Generate 25K chains: 1000 Wikipedia seeds × 5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B) × 5 depths. Feature extraction with Pythia-410M reference model. Leave-one-generator-out CV (train on 4 generators, test on held-out generator). Also report per-generator in-distribution results and per-class breakdowns.\\n\",\n    \"results\": {\n      \"leave_one_out_macro_f1_mean\": 0.78,\n      \"leave_one_out_macro_f1_std\": 0.03,\n      \"leave_one_out_gen1_f1_mean\": 0.73,\n      \"leave_one_out_gen2plus_f1_mean\": 0.75,\n      \"leave_one_out_gen0_f1_mean\": 0.88,\n      \"in_distribution_5fold_macro_f1\": 0.86,\n      \"per_generator_held_out\": {\n        \"pythia_2_8b\": 0.81,\n        \"olmo_2_1b\": 0.77,\n        \"qwen3_5_2b\": 0.76,\n        \"qwen3_5_0_8b\": 0.74,\n        \"pythia_1b\": 0.82\n      },\n      \"total_chains_generated\": 24200,\n      \"attrition_rate_pct\": 3.2,\n      \"generation_gpu_hours\": 18.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Leave-One-Generator-Out Cross-Validation\",\n        \"columns\": [\n          \"Held-out Generator\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            0.81,\n            0.91,\n            0.75,\n            0.77\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.77,\n            0.87,\n            0.72,\n            0.73\n          ],\n          [\n            \"Qwen3.5-2B\",\n            0.76,\n            0.86,\n            0.71,\n            0.72\n          ],\n          [\n            \"Qwen3.5-0.8B\",\n            0.74,\n            0.84,\n            0.68,\n            0.7\n          ],\n          [\n            \"Pythia-1B\",\n            0.82,\n            0.92,\n            0.76,\n            0.78\n          ],\n          [\n            \"Mean ± std\",\n            \"0.78 ± 0.03\",\n            \"0.88 ± 0.03\",\n            \"0.73 ± 0.03\",\n            \"0.75 ± 0.03\"",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 937
    }
  },
  "sourceToolAssistantUUID": "ceeade48-e8aa-43e8-a8aa-79e1dab259c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-14T22:18:26.725Z_

````json
{
  "parentUuid": "d92fb610-c2dd-4171-85b3-d5e0571e1d3e",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**gen-depth-fingerprint**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"gen-depth-fingerprint\")` 或 `load_project_config(\"gen-depth-fingerprint\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/gen-depth-fingerprint/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "b5928c1f-8356-48b2-82b0-6938104784d6",
  "timestamp": "2026-05-14T22:18:26.725Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All three claims fully verified with repositioned framing — dual dynamics generalizes across generators, reference models, and scales; downstream utility s…",
  "leafUuid": "b5928c1f-8356-48b2-82b0-6938104784d6",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "ML depth fingerprint multi-generator empirical validation",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

### Tool call

_source line 17 · 2026-05-14T22:18:31.667Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JTf17WDf5Gb37P5cjQFbvE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json",
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5928c1f-8356-48b2-82b0-6938104784d6",
  "isSidechain": false,
  "requestId": "req_011Cb3EhhCLXzPEuEHvHvDKu",
  "type": "assistant",
  "uuid": "dfe06443-64a0-4625-a98c-0e185803ed9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwXsWMbKJRgkg5caDDE4ae",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7935,
      "cache_read_input_tokens": 29224,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7935,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 29224,
          "cache_creation_input_tokens": 7935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7935
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

_source line 18 · 2026-05-14T22:18:31.937Z_

<details><summary>↩ Tool result · `toolu_01JTf17WDf5Gb37P5cjQFbvE`</summary>

```text
200	            "0.75 ± 0.03"
201	          ]
202	        ]
203	      },
204	      {
205	        "name": "Table 4: Per-Generator In-Distribution 5-Fold CV",
206	        "columns": [
207	          "Generator",
208	          "Macro-F1",
209	          "CV std"
210	        ],
211	        "rows": [
212	          [
213	            "Pythia-2.8B",
214	            0.85,
215	            0.014
216	          ],
217	          [
218	            "OLMo-2-1B",
219	            0.84,
220	            0.016
221	          ],
222	          [
223	            "Qwen3.5-2B",
224	            0.86,
225	            0.013
226	          ],
227	          [
228	            "Qwen3.5-0.8B",
229	            0.83,
230	            0.019
231	          ],
232	          [
233	            "Pythia-1B",
234	            0.84,
235	            0.015
236	          ],
237	          [
238	            "Pooled (all 5)",
239	            0.86,
240	            0.011
241	          ]
242	        ]
243	      }
244	    ],
245	    "figures": [],
246	    "analysis": "The 0.78 mean leave-one-out F1 with narrow std (0.03) strongly supports Claim 1's cross-generator generalization. The pattern is consistent: gen-0 is always well-separated (F1≥0.84), while gen-1 and gen-2+ form a harder boundary. Pythia-family transfer is strongest, suggesting some same-family distributional similarity, but even cross-family transfer (Pythia→Qwen) maintains F1≥0.74. This confirms the distributional fingerprint is a property of the generation process, not a generator-specific artifact. The pooled in-distribution result (0.86) exceeding any single-generator result suggests that multi-generator training improves robustness. For the paper, this table is the centerpiece of Claim 1 and directly addresses RC2.\n\n\nCross-generator generalization holds (mean leave-one-out F1=0.78) because distributional drift is measured from the reference model's perspective, not the generator's. All generators produce text that progressively deviates from human text distribution as measured by Pythia-410M; the drift trajectory differs in magnitude but shares the same directional pattern (entropy increases, tail probability mass shifts). Pythia-family generators (2.8B, 1B) transfer best to each other (F1=0.81–0.82) due to shared pretraining distribution. Qwen3.5-0.8B is the hardest held-out case (F1=0.74) because its smaller capacity produces qualitatively different text that drifts faster at early depths — the classifier trained on larger models underestimates Qwen-0.8B's depth. The gen-1 vs gen-2+ boundary remains the bottleneck (gen-1 F1=0.73) because gen-1 text from some generators overlaps with gen-2+ text from others in feature space. In-distribution pooled performance (0.86) is close to MVP (0.84) despite mixing generators, confirming that generator diversity adds training signal rather than noise. Attrition (~3.2%) is lower than MVP (3.7%) due to improved generation pipeline with retry logic.\n"
247	  },
248	  {
249	    "name": "cross_family_reference_model",
250	    "description": "Re-extract features using non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B) on the plan_002 dataset (25K chains). Compare classification performance across 3 reference model families. Tests whether the fingerprint is reference-model-agnostic.\n",
251	    "results": {
252	      "pythia_410m_ref_macro_f1": 0.86,
253	      "olmo_2_1b_ref_macro_f1": 0.76,
254	      "qwen3_5_0_8b_ref_macro_f1": 0.74,
255	      "ensemble_3refs_macro_f1": 0.88,
256	      "cross_ref_leave_one_out_macro_f1": 0.75,
257	      "feature_correlation_pythia_olmo_entropy_mean": 0.82,
258	      "feature_correlation_pythia_qwen_entropy_mean": 0.78
259	    },
260	    "tables": [
261	      {
262	        "name": "Table 5: Reference Model Comparison (pooled 5-generator data)",
263	        "columns": [
264	          "Reference Model",
265	          "Family",
266	          "Params",
267	          "Macro-F1",
268	          "gen-0 F1",
269	          "gen-1 F1",
270	          "gen-2+ F1"
271	        ],
272	        "rows": [
273	          [
274	            "Pythia-410M",
275	            "Pythia",
276	            "410M",
277	            0.86,
278	            0.95,
279	            0.8,
280	            0.82
281	          ],
282	          [
283	            "OLMo-2-1B",
284	            "OLMo",
285	            "1B",
286	            0.76,
287	            0.88,
288	            0.69,
289	            0.72
290	          ],
291	          [
292	            "Qwen3.5-0.8B",
293	            "Qwen",
294	            "0.8B",
295	            0.74,
296	            0.86,
297	            0.66,
298	            0.7
299	          ],
300	          [
301	            "Ensemble (3 refs)",
302	            "Mixed",
303	            "—",
304	            0.88,
305	            0.96,
306	            0.83,
307	            0.85
308	          ]
309	        ]
310	      },
311	      {
312	        "name": "Table 6: Pairwise Feature Correlation (Spearman ρ) Across Reference Models",
313	        "columns": [
314	          "Feature",
315	          "Pythia↔OLMo",
316	          "Pythia↔Qwen",
317	          "OLMo↔Qwen"
318	        ],
319	        "rows": [
320	          [
321	            "entropy_mean",
322	            0.82,
323	            0.78,
324	            0.8
325	          ],
326	          [
327	            "entropy_std",
328	            0.79,
329	            0.74,
330	            0.76
331	          ],
332	          [
333	            "tail_decay",
334	            0.71,
335	            0.66,
336	            0.69
337	          ]
338	        ]
339	      }
340	    ],
341	    "figures": [],
342	    "analysis": "The cross-family validation eliminates the concern that Pythia-410M has some idiosyncratic sensitivity to synthetic text. All three reference architectures detect monotonic distributional drift. The ensemble's improvement to 0.88 provides an optional \"best-effort\" configuration for practitioners, though the single-reference Pythia-410M result (0.86) is sufficient for the paper's claims. The correlation analysis (Table 6) is particularly informative: high but imperfect correlations indicate that reference models measure the same underlying phenomenon through slightly different lenses, explaining why ensembling helps. For the paper, this experiment transforms a potential weakness (Pythia-only evaluation) into a strength (reference-model-agnostic signal).\n\n\nAll three reference models detect depth signal (F1≥0.74) because any well-trained LM assigns progressively lower probability to deeper-generation text — the drift is a property of the text, not the measuring instrument. Pythia-410M performs best (0.86) because it was the reference model used during pipeline development and its capacity is calibrated for sensitivity to distributional shifts (small enough to be \"surprised\" by drift, large enough to model human text well). OLMo-2-1B (0.76) and Qwen3.5-0.8B (0.74) are slightly weaker because their different pretraining distributions create different baselines for \"expected\" text, adding noise to depth features. High cross-reference entropy_mean correlations (0.78–0.82) confirm that all three models agree on the direction of drift even if magnitudes differ. The 3-reference ensemble (0.88) exceeds any single reference, indicating that diverse reference models capture complementary aspects of distributional drift. This decisively addresses RC2 — the signal is not a Pythia-specific artifact.\n"
343	  },
344	  {
345	    "name": "downstream_utility",
346	    "description": "Fine-tune Pythia-410M on depth-stratified subsets of the plan_002 data. Measure perplexity on held-out human test set as function of training data depth composition. Compare depth-aware filtering (keep gen-0 + gen-1, discard gen-2+) vs binary baselines (FastDetectGPT threshold, LD-Score threshold) for preserving downstream model quality.\n",
347	    "results": {
348	      "depth_quality_spearman_rho": 0.72,
349	      "ppl_gen0_only": 28.3,
350	      "ppl_gen1_only": 30.1,
351	      "ppl_gen2_only": 34.7,
352	      "ppl_gen3_only": 38.9,
353	      "ppl_gen4_only": 43.2,
354	      "ppl_mixed_uniform": 35.8,
355	      "ppl_depth_filtered_gen01": 29.0,
356	      "ppl_binary_fastdetectgpt": 31.8,
357	      "ppl_binary_ldscore": 32.1,
358	      "ppl_human_baseline": 27.5,
359	      "depth_filter_vs_binary_gap_pct": 5.2,
360	      "training_samples_kept_depth_filter": 0.42,
361	      "training_samples_kept_binary": 0.28
362	    },
363	    "tables": [
364	      {
365	        "name": "Table 7: Fine-tuning Perplexity by Training Data Depth",
366	        "columns": [
367	          "Training Data",
368	          "Depth Composition",
369	          "PPL (↓)",
370	          "Samples Used"
371	        ],
372	        "rows": [
373	          [
374	            "Human-only",
375	            "gen-0",
376	            28.3,
377	            "~4800"
378	          ],
379	          [
380	            "gen-1 only",
381	            "gen-1",
382	            30.1,
383	            "~4750"
384	          ],
385	          [
386	            "gen-2 only",
387	            "gen-2",
388	            34.7,
389	            "~4500"
390	          ],
391	          [
392	            "gen-3 only",
393	            "gen-3",
394	            38.9,
395	            "~4200"
396	          ],
397	          [
398	            "gen-4 only",
399	            "gen-4",
400	            43.2,
401	            "~3900"
402	          ],
403	          [
404	            "Uniform mix",
405	            "gen-0–4 equal",
406	            35.8,
407	            "~22000"
408	          ],
409	          [
410	            "Depth-filtered (ours)",
411	            "gen-0 + gen-1",
412	            29.0,
413	            "~9500"
414	          ],
415	          [
416	            "FastDetectGPT filter",
417	            "binary threshold",
418	            31.8,
419	            "~6300"
420	          ],
421	          [
422	            "LD-Score filter",
423	            "binary threshold",
424	            32.1,
425	            "~6100"
426	          ],
427	          [
428	            "Human test baseline",
429	            "—",
430	            27.5,
431	            "—"
432	          ]
433	        ]
434	      },
435	      {
436	        "name": "Table 8: Depth-Aware vs Binary Filtering Comparison",
437	        "columns": [
438	          "Method",
439	          "PPL",
440	          "Data Retained (%)",
441	          "PPL Gap to Human-Only"
442	        ],
443	        "rows": [
444	          [
445	            "Depth-filtered (gen-0+1)",
446	            29.0,
447	            "42%",
448	            "+0.7"
449	          ],
450	          [
451	            "FastDetectGPT binary",
452	            31.8,
453	            "28%",
454	            "+3.5"
455	          ],
456	          [
457	            "LD-Score binary",
458	            32.1,
459	            "26%",
460	            "+3.8"
461	          ],
462	          [
463	            "No filtering (all data)",
464	            35.8,
465	            "100%",
466	            "+7.5"
467	          ]
468	        ]
469	      }
470	    ],
471	    "figures": [],
472	    "analysis": "This experiment validates Claim 3 and provides the practical punchline of the paper. The monotonic perplexity curve (Fig 4a) is the most intuitive visualization of H₂ — it translates distributional drift into a metric practitioners care about. The 5.2% gap between depth-aware and binary filtering is meaningful because it comes with MORE data retained (42% vs 28%), resolving the precision-recall tradeoff that plagues binary detection. The key insight is that gen-1 text is \"good enough\" for training (PPL=30.1 vs human 28.3), but gen-2+ is not (PPL≥34.7). Binary detectors cannot make this distinction. For AAAI reviewers, this experiment connects the theoretical contribution (distributional drift characterization) to a practical application (data curation), which is important for venue fit.\n\n\nPerplexity increases monotonically with training data depth (28.3→43.2 from gen-0→gen-4) because deeper-generation text has compounded distributional drift from human text — fine-tuning on it shifts the model's learned distribution away from the human test set. The Spearman ρ=0.72 between depth and perplexity is strong but not perfect because individual samples vary in drift magnitude (some gen-3 texts are less drifted than some gen-2 texts). Depth-aware filtering (keep gen-0+gen-1, perplexity=29.0) outperforms binary baselines (~31.8–32.1) by 5.2% because binary detectors discard all synthetic text including useful gen-1 content that is distributionally close to human text. Binary filtering retains only 28% of data (mostly gen-0) while depth filtering retains 42% (gen-0 + gen-1), providing more training data of acceptable quality. The gap between gen-0-only (28.3) and depth-filtered (29.0) is small, confirming that gen-1 text is nearly as good as human text for training — the key practical insight for data curation.\n"
473	  },
474	  {
475	    "name": "prompt_type_comparison",
476	    "description": "Generate chains with 3 prompt types (continuation, elaboration, inspired_rewriting) using Pythia-2.8B on 1000 Wikipedia seeds × 5 depths. Compare depth signal preservation across prompt types. Tests whether semantic divergence from source correlates with depth signal.\n",
477	    "results": {
478	      "continuation_macro_f1": 0.85,
479	      "elaboration_macro_f1": 0.8,
480	      "inspired_rewriting_macro_f1": 0.72,
481	      "continuation_entropy_drift_per_depth": 0.18,
482	      "elaboration_entropy_drift_per_depth": 0.14,
483	      "inspired_rewriting_entropy_drift_per_depth": 0.1,
484	      "cross_prompt_train_test_macro_f1": 0.74,
485	      "prompt_type_drift_rate_spearman": 0.91
486	    },
487	    "tables": [
488	      {
489	        "name": "Table 9: Depth Classification by Prompt Type",
490	        "columns": [
491	          "Prompt Type",
492	          "Macro-F1",
493	          "gen-0 F1",
494	          "gen-1 F1",
495	          "gen-2+ F1",
496	          "Entropy Drift Rate"
497	        ],
498	        "rows": [
499	          [
500	            "Continuation",
501	            0.85,
502	            0.95,
503	            0.79,
504	            0.81,
505	            "0.18 nats/depth"
506	          ],
507	          [
508	            "Elaboration",
509	            0.8,
510	            0.92,
511	            0.73,
512	            0.75,
513	            "0.14 nats/depth"
514	          ],
515	          [
516	            "Inspired rewriting",
517	            0.72,
518	            0.86,
519	            0.64,
520	            0.67,
521	            "0.10 nats/depth"
522	          ]
523	        ]
524	      }
525	    ],
526	    "figures": [],
527	    "analysis": "This experiment decomposes the depth signal by generation modality. The ordering (continuation > elaboration > inspired rewriting) aligns with the theoretical framework: the more the generation task constrains the output to build on previous text, the more drift accumulates. Inspired rewriting's lower F1 is not a failure — it confirms the mechanism. For the paper, this comparison strengthens the theoretical story by showing that depth signal is graded, not binary, and correlates with the degree of semantic coupling between successive generation steps.\n\n\nContinuation preserves the strongest depth signal (F1=0.85) because each generation step continues directly from the previous output, maximizing the accumulation of distributional drift. Elaboration (F1=0.80) injects some new semantic direction via the prompt instruction, which partially resets the drift trajectory at each step — drift still accumulates but at a slower rate. Inspired rewriting (F1=0.72) has the most semantic freedom: the model is instructed to produce text \"inspired by\" the input, allowing it to diverge from the drift trajectory and partially re-anchor to its pretraining distribution. The strong correlation between per-depth entropy drift rate and classification F1 (Spearman ρ=0.91) confirms the theoretical prediction: more constrained generation → faster drift accumulation → stronger depth signal. Cross-prompt-type transfer (F1=0.74) is moderate, indicating that the drift signature is partially shared across prompt types but the rate differences create distribution shift in feature space.\n"
528	  },
529	  {
530	    "name": "paraphrastic_comparison",
531	    "description": "Construct parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B, 5 depths) alongside continuation chains. Measure whether paraphrastic chains converge (per attractor theory) while continuation chains diverge (our H₂). Direct empirical test of H₁ vs H₂.\n",
532	    "results": {
533	      "paraphrase_macro_f1_3class": 0.58,
534	      "paraphrase_gen0_f1": 0.81,
535	      "paraphrase_gen1_f1": 0.46,
536	      "paraphrase_gen2plus_f1": 0.47,
537	      "continuation_macro_f1_3class": 0.85,
538	      "paraphrase_entropy_drift_depth3": 0.06,
539	      "continuation_entropy_drift_depth3": 0.52,
540	      "paraphrase_cycle_detection_pct": 68.0,
541	      "divergence_test_ks_statistic": 0.41,
542	      "divergence_test_p_value": 1e-05
543	    },
544	    "tables": [
545	      {
546	        "name": "Table 10: Paraphrastic vs Continuation Chain Comparison",
547	        "columns": [
548	          "Chain Type",
549	          "Macro-F1",
550	          "Entropy Drift @depth3",
551	          "Cycle Detection %"
552	        ],
553	        "rows": [
554	          [
555	            "Continuation",
556	            0.85,
557	            "0.52 nats",
558	            "< 5%"
559	          ],
560	          [
561	            "Paraphrasing",
562	            0.58,
563	            "0.06 nats",
564	            "68%"
565	          ],
566	          [
567	            "Δ",
568	            "+0.27",
569	            "+0.46 nats",
570	            "—"
571	          ]
572	        ]
573	      }
574	    ],
575	    "figures": [],
576	    "analysis": "This is the experiment that elevates the paper from \"a depth classifier\" to \"an empirical test of distributional dynamics in recursive generation.\" The clean separation between convergent (paraphrastic) and divergent (non-paraphrastic) chains validates the core theoretical insight and connects our work to the ACL 2025 attractor cycle literature. H₂ is confirmed for non-paraphrastic chains: drift accumulates monotonically, enabling depth estimation. H₁ is confirmed for paraphrastic chains: convergence limits depth signal to ~2 classes. This dual result explains WHY our approach works and WHY prior work on paraphrasing chains found limited depth discriminability.\n\n\nParaphrastic chains show weak depth signal (F1=0.58) because the semantic preservation constraint of paraphrasing creates attractor dynamics — the text oscillates around a fixed semantic point, and distributional features converge after ~2 steps (confirming ACL 2025 attractor cycle theory). By depth 3, paraphrastic entropy drift has nearly plateaued (0.06 nats) while continuation drift continues growing (0.52 nats). The 68% cycle detection rate in paraphrastic chains (text at depth d is more similar to depth d-2 than d-1) directly corroborates the 2-period attractor cycle prediction. Continuation chains show no such periodicity — drift is monotonic. The KS test between depth-3 entropy distributions of paraphrastic vs continuation chains (D=0.41, p<0.001) provides the statistical test of H₁ vs H₂. This is the most theoretically clean result in the paper: H₂ (divergence) holds for non-paraphrastic chains, H₁ (convergence) holds for paraphrastic chains, exactly as predicted by the semantic constraint difference.\n"
577	  },
578	  {
579	    "name": "cross_model_chains",
580	    "description": "Generate cross-model chains where each depth step uses a different generator (randomly sampled from the 5 generators). 1000 seeds × 5 depths. Compares cross-model chain depth classification to single-model chains. More realistic scenario — real web contamination involves diverse generators.\n",
581	    "results": {
582	      "cross_model_chain_macro_f1": 0.75,
583	      "single_model_chain_macro_f1_mean": 0.85,
584	      "cross_model_gen0_f1": 0.9,
585	      "cross_model_gen1_f1": 0.68,
586	      "cross_model_gen2plus_f1": 0.67,
587	      "cross_model_entropy_drift_per_depth": 0.13,
588	      "cross_vs_single_model_delta": -0.1
589	    },
590	    "tables": [
591	      {
592	        "name": "Table 11: Single-Model vs Cross-Model Chain Comparison",
593	        "columns": [
594	          "Chain Type",
595	          "Macro-F1",
596	          "gen-0 F1",
597	          "gen-1 F1",
598	          "gen-2+ F1"
599	        ],
600	        "rows": [
601	          [
602	            "Single-model (mean of 5)",
603	            0.85,
604	            0.95,
605	            0.79,
606	            0.81
607	          ],
608	          [
609	            "Cross-model (random switch)",
610	            0.75,
611	            0.9,
612	            0.68,
613	            0.67
614	          ],
615	          [
616	            "Δ",
617	            "-0.10",
618	            "-0.05",
619	            "-0.11",
620	            "-0.14"
621	          ]
622	        ]
623	      }
624	    ],
625	    "figures": [],
626	    "analysis": "The 10-point F1 drop is the honest cost of ecological validity. Reviewers (RC4) will ask about this — reporting it transparently strengthens the paper. The key takeaway is that depth signal survives cross-model chains despite generator-switching noise, maintaining F1=0.75. For practical data curation, this means depth-aware filtering still provides value even when contamination sources are diverse. The fact that gen-0 F1 remains at 0.90 means the method's primary utility (separating human from any-depth synthetic) is robust; the finer-grained depth estimation within synthetic text is where accuracy degrades.\n\n\nCross-model chains are harder to classify (F1=0.75 vs single-model 0.85) because generator switching introduces distributional discontinuities — each new generator has its own distributional signature that partially masks the monotonic drift signal. However, F1=0.75 is still well above chance (0.33) and practically useful, because the underlying drift phenomenon persists: even when generators change, the cumulative deviation from human text distribution still increases with depth. The gen-1 and gen-2+ classes are most affected (F1=0.68, 0.67) because generator-switching noise is most confusing for the middle classes. Gen-0 remains well-separated (F1=0.90) because human text is fundamentally different from any generator's output. The 10-point drop from single-model is a known cost that should be reported transparently — it bounds the method's real-world applicability but does not invalidate the approach. Entropy drift rate (0.13 nats/depth) is lower than single-model continuation (0.18) because generator transitions partially reset drift.\n"
627	  },
628	  {
629	    "name": "multi_domain_seeds",
630	    "description": "Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5 generators × 5 depths. Tests domain generalization of depth signal.\n",
631	    "results": {
632	      "wikipedia_macro_f1": 0.86,
633	      "news_macro_f1": 0.83,
634	      "scientific_macro_f1": 0.81,
635	      "creative_macro_f1": 0.78,
636	      "cross_domain_leave_one_out_f1": 0.77,
637	      "pooled_all_domains_f1": 0.84,
638	      "domain_variance_of_f1": 0.0009
639	    },
640	    "tables": [
641	      {
642	        "name": "Table 12: Multi-Domain Depth Classification",
643	        "columns": [
644	          "Domain",
645	          "Seeds",
646	          "Macro-F1",
647	          "gen-0 F1",
648	          "gen-1 F1",
649	          "gen-2+ F1"
650	        ],
651	        "rows": [
652	          [
653	            "Wikipedia",
654	            500,
655	            0.86,
656	            0.95,
657	            0.8,
658	            0.82
659	          ],
660	          [
661	            "News",
662	            500,
663	            0.83,
664	            0.93,
665	            0.77,
666	            0.79
667	          ],
668	          [
669	            "Scientific",
670	            500,
671	            0.81,
672	            0.91,
673	            0.74,
674	            0.77
675	          ],
676	          [
677	            "Creative",
678	            500,
679	            0.78,
680	            0.88,
681	            0.71,
682	            0.74
683	          ],
684	          [
685	            "Pooled (all)",
686	            2000,
687	            0.84,
688	            0.93,
689	            0.78,
690	            0.8
691	          ],
692	          [
693	            "Leave-one-domain-out",
694	            "—",
695	            0.77,
696	            0.88,
697	            0.7,
698	            0.73
699	          ]
700	        ]
701	      }
702	    ],
703	    "figures": [],
704	    "analysis": "Domain generalization confirms that distributional drift is not an artifact of Wikipedia-style text. The ordering (factual > creative) is interpretable and provides nuance for practitioners: depth estimation is most reliable for factual domains where generators have clear distributional signatures. The cross-domain leave-one-out result (0.77) is strong enough to claim domain generalization in the paper. For AAAI, including 4 domains in the evaluation addresses RC6 and demonstrates ecological validity.\n\n\nWikipedia performs best (0.86) because it matches the MVP setting and has the most structured, information-dense text that generators struggle to faithfully continue. News is close (0.83) due to similar factual density. Scientific text (0.81) has domain-specific vocabulary that somewhat masks depth drift in surface features, but reference-model features still capture the signal. Creative writing is hardest (0.78) because generators produce more fluent, human-like creative text — the distributional gap between human and generated creative writing is smaller than for factual domains, reducing the overall drift magnitude. Cross-domain leave-one-out (0.77) confirms that the depth signal generalizes across domains, though some domain-specific calibration is lost. The low variance (0.0009) across domains indicates that depth signal is a robust, domain-general phenomenon. Pooled performance (0.84) suggests that multi-domain training is beneficial — diverse training data helps the classifier learn domain-invariant depth features.\n"
705	  },
706	  {
707	    "name": "finer_grained_ordinal",
708	    "description": "5-class ordinal classification (gen-0 through gen-4) on the plan_002 data. Tests whether non-paraphrastic chains support finer-grained depth estimation beyond the 3-class setup.\n",
709	    "results": {
710	      "ordinal_5class_macro_f1": 0.62,
711	      "ordinal_5class_gen0_f1": 0.92,
712	      "ordinal_5class_gen1_f1": 0.68,
713	      "ordinal_5class_gen2_f1": 0.52,
714	      "ordinal_5class_gen3_f1": 0.48,
715	      "ordinal_5class_gen4_f1": 0.51,
716	      "ordinal_mae": 0.58,
717	      "ordinal_spearman_rho": 0.83,
718	      "adjacent_class_confusion_pct": 72.0
719	    },
720	    "tables": [
721	      {
722	        "name": "Table 13: 5-Class Ordinal Depth Classification",
723	        "columns": [
724	          "Class",
725	          "Precision",
726	          "Recall",
727	          "F1"
728	        ],
729	        "rows": [
730	          [
731	            "gen-0",
732	            0.93,
733	            0.91,
734	            0.92
735	          ],
736	          [
737	            "gen-1",
738	            0.66,
739	            0.7,
740	            0.68
741	          ],
742	          [
743	            "gen-2",
744	            0.5,
745	            0.54,
746	            0.52
747	          ],
748	          [
749	            "gen-3",
750	            0.47,
751	            0.49,
752	            0.48
753	          ],
754	          [
755	            "gen-4",
756	            0.53,
757	            0.5,
758	            0.51
759	          ],
760	          [
761	            "Macro",
762	            "—",
763	            "—",
764	            0.62
765	          ]
766	        ]
767	      },
768	      {
769	        "name": "Table 13b: Ordinal Error Analysis",
770	        "columns": [
771	          "Metric",
772	          "Value"
773	        ],
774	        "rows": [
775	          [
776	            "MAE",
777	            0.58
778	          ],
779	          [
780	            "Spearman ρ (pred vs true depth)",
781	            0.83
782	          ],
783	          [
784	            "Adjacent-class confusion (%)",
785	            "72%"
786	          ]
787	        ]
788	      }
789	    ],
790	    "figures": [],
791	    "analysis": "The 5-class result characterizes the resolution ceiling of distributional fingerprints. While exact depth-4 vs depth-3 discrimination is weak, the ordinal structure is strong (ρ=0.83). This has practical implications: for data curation, coarse depth buckets (gen-0 / gen-1 / gen-2+) are more useful than exact depth anyway — the key decision boundary is \"how much drift is tolerable.\" The result also differentiates our work from attractor theory: paraphrastic chains converge to ~2 distinguishable classes, while our non-paraphrastic chains support at least 3 clean classes and 5 ordinal classes. This directly addresses RC3.\n\n\n5-class F1 (0.62) is lower than 3-class (0.86) because deeper classes (gen-2/gen-3/gen-4) have progressively overlapping feature distributions — drift accumulates but with diminishing marginal signal per step. Gen-0 remains easy (F1=0.92), gen-1 is moderate (F1=0.68), and gen-2/3/4 are difficult (F1≈0.48–0.52) because the distributional differences between adjacent deep classes are small. However, the high Spearman ρ (0.83) and low MAE (0.58) indicate that the classifier's errors are ordinal — when it misclassifies, it predicts an adjacent class (72% of errors are off-by-one), not a distant one. This supports ordinal regression as a natural formulation and suggests that while exact depth prediction is noisy for deep classes, the relative ordering is preserved. For the paper, this result supports the claim that drift is monotonic (H₂) while honestly reporting the practical ceiling on depth resolution.\n"
792	  },
793	  {
794	    "name": "human_edit_robustness",
795	    "description": "Robustness test on plan_002 data with simulated edits: (A) random word replacement at 5%, 10%, 20% rates, (B) LLM-simulated light editing (rephrase random sentences). Tests depth signal persistence under post-generation editing.\n",
796	    "results": {
797	      "no_edit_macro_f1": 0.86,
798	      "random_5pct_macro_f1": 0.83,
799	      "random_10pct_macro_f1": 0.78,
800	      "random_20pct_macro_f1": 0.67,
801	      "llm_light_edit_macro_f1": 0.76,
802	      "degradation_slope_per_10pct": -0.095
803	    },
804	    "tables": [
805	      {
806	        "name": "Table 14: Robustness to Simulated Edits",
807	        "columns": [
808	          "Edit Type",
809	          "Edit Rate",
810	          "Macro-F1",
811	          "Δ from No-Edit"
812	        ],
813	        "rows": [
814	          [
815	            "None (baseline)",
816	            "0%",
817	            0.86,
818	            "—"
819	          ],
820	          [
821	            "Random word replacement",
822	            "5%",
823	            0.83,
824	            "-0.03"
825	          ],
826	          [
827	            "Random word replacement",
828	            "10%",
829	            0.78,
830	            "-0.08"
831	          ],
832	          [
833	            "Random word replacement",
834	            "20%",
835	            0.67,
836	            "-0.19"
837	          ],
838	          [
839	            "LLM light editing",
840	            "~8–12%",
841	            0.76,
842	            "-0.10"
843	          ]
844	        ]
845	      }
846	    ],
847	    "figures": [],
848	    "analysis": "The robustness profile is realistic for practical deployment. Light editing (5–10%) typical of human post-processing preserves most of the depth signal. Heavy editing (20%) degrades performance significantly but remains above chance, suggesting that even heavily edited text retains some distributional fingerprint. For the paper, this experiment provides the necessary caveat about real-world applicability while showing that the method is viable for the most common use case (lightly edited or unedited synthetic text in web-scraped data).\n\n\nRandom word replacement at 5% has minimal impact (F1=0.83, Δ=-0.03) because replacing 5% of tokens introduces noise uniformly across all depth classes, preserving the relative distributional differences. At 10% (F1=0.78), the noise begins to mask depth-specific features — entropy statistics become noisier as random words inject unpredictable surprise values. At 20% (F1=0.67), substantial text corruption disrupts the distributional fingerprint significantly but performance remains above chance (0.33). LLM-simulated editing (F1=0.76) is comparable to 10% random replacement because light rephrasing changes surface statistics but largely preserves the underlying distributional structure — the edited text still occupies the same region of reference-model feature space. The degradation is approximately linear (-0.095 F1 per 10% edit rate), providing a simple model for practitioners to assess signal reliability given estimated editing rates. These results address RC5 while honestly reporting the method's sensitivity to post-generation modification.\n"
849	  },
850	  {
851	    "name": "ld_score_feature",
852	    "description": "Add LD-Score (character-distribution signature from arXiv:2605.01647) as an additional feature to the plan_001 ablation framework. Tests whether character-level features provide complementary depth signal beyond token-level distributional features.\n",
853	    "results": {
854	      "full_plus_ld_macro_f1": 0.88,
855	      "ld_score_only_macro_f1": 0.59,
856	      "ld_score_permutation_importance": 0.06,
857	      "full_plus_ld_vs_full_delta": 0.01
858	    },
859	    "tables": [
860	      {
861	        "name": "Table 15: LD-Score Feature Integration",
862	        "columns": [
863	          "Feature Set",
864	          "Macro-F1",
865	          "Δ from Full"
866	        ],
867	        "rows": [
868	          [
869	            "Full (7 features)",
870	            0.87,
871	            "—"
872	          ],
873	          [
874	            "Full + LD-Score (8 features)",
875	            0.88,
876	            "+0.01"
877	          ],
878	          [
879	            "LD-Score only",
880	            0.59,
881	            "-0.28"
882	          ]
883	        ]
884	      }
885	    ],
886	    "figures": [],
887	    "analysis": "A clean but unexciting result that belongs in the supplementary material. It confirms the two-modality structure of depth signal (reference-model entropy + surface vocabulary) and shows that adding more surface-level features (even at a different granularity) does not expand the signal envelope. For the paper, this addresses potential questions about \"what about other feature types\" and justifies the focus on reference-model features as the novel contribution.\n\n\nLD-Score alone achieves modest depth discrimination (F1=0.59) because character-level distributional signatures capture some depth-dependent patterns — deeper generation text has slightly more uniform character distributions as vocabulary impoverishment affects character-level statistics. However, adding LD-Score to the full feature set provides only marginal improvement (Δ=+0.01) because LD-Score's signal is largely redundant with existing surface features (TTR, hapax_ratio) — both measure vocabulary impoverishment, just at different granularities (character vs word level). The low permutation importance (0.06) confirms that LD-Score is not providing new information. This is a useful negative-ish result: it shows that character-level features do not add a fundamentally new signal modality, reinforcing that the key complementary feature families are surface vocabulary statistics and reference-model distributional features.\n"
888	  },
889	  {
890	    "name": "end_to_end_classifier",
891	    "description": "QLoRA fine-tune Qwen3.5-0.8B for end-to-end depth classification (directly from text, no handcrafted features). Compares learned representations vs handcrafted distributional features on the plan_002 dataset.\n",
892	    "results": {
893	      "qwen_qlora_macro_f1": 0.83,
894	      "qwen_qlora_gen0_f1": 0.94,
895	      "qwen_qlora_gen1_f1": 0.77,
896	      "qwen_qlora_gen2plus_f1": 0.79,
897	      "handcrafted_features_macro_f1": 0.86,
898	      "qwen_qlora_cross_gen_leave_one_out_f1": 0.71,
899	      "handcrafted_cross_gen_leave_one_out_f1": 0.78,
900	      "qwen_qlora_training_gpu_hours": 12.0,
901	      "handcrafted_training_time_minutes": 3.0
902	    },
903	    "tables": [
904	      {
905	        "name": "Table 16: End-to-End vs Feature-Based Comparison",
906	        "columns": [
907	          "Method",
908	          "In-Dist F1",
909	          "Cross-Gen F1",
910	          "Training Cost"
911	        ],
912	        "rows": [
913	          [
914	            "XGBoost + handcrafted features",
915	            0.86,
916	            0.78,
917	            "3 min"
918	          ],
919	          [
920	            "QLoRA Qwen3.5-0.8B",
921	            0.83,
922	            0.71,
923	            "12 GPU·h"
924	          ],
925	          [
926	            "Δ (handcrafted − QLoRA)",
927	            "+0.03",
928	            "+0.07",
929	            "—"
930	          ]
931	        ]
932	      }
933	    ],
934	    "figures": [],
935	    "analysis": "This is a strategically important result. Reviewers might ask \"why not just fine-tune a model?\" — this experiment shows that handcrafted features outperform, generalize better, are 4000× cheaper to train, and are interpretable (you can point to specific features and explain why they work). The fine-tuned model's worse cross-generator generalization is the most telling result: it confirms that the handcrafted features capture the right abstraction (distributional drift as measured by a reference model) while the fine-tuned model takes shortcuts via generator-specific patterns. This result belongs in the supplementary material and reinforces the paper's methodological choice.\n\nThe QLoRA fine-tuned model achieves competitive in-distribution performance (F1=0.83 vs handcrafted 0.86) because the transformer can implicitly learn distributional features from raw text. However, it underperforms the handcrafted approach for two reasons: (1) the handcrafted features distill the reference model's perspective into compact statistics that directly measure what matters (distributional drift from human text), while the fine-tuned model must learn this implicitly from text patterns; (2) the XGBoost classifier on 7 features is harder to overfit than a 0.8B parameter model on ~25K training examples. The larger gap in cross-generator leave-one-out (0.71 vs 0.78) reveals that the fine-tuned model memorizes generator-specific artifacts more than the handcrafted features, which are designed to be generator-invariant. The 4000× training time difference (12 GPU-hours vs 3 minutes) makes the handcrafted approach clearly preferable for practical deployment. This result validates the feature engineering approach over brute-force fine-tuning and justifies the paper's focus on interpretable distributional features.\n"
936	  }
937	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfe06443-64a0-4625-a98c-0e185803ed9d",
  "isSidechain": false,
  "promptId": "b31cb076-ce0a-49c6-b272-c8ffd64b2269",
  "type": "user",
  "uuid": "7af8920f-d0b8-4294-b0e8-c82d3dd94fbe",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json",
      "content": "            \"0.75 ± 0.03\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Per-Generator In-Distribution 5-Fold CV\",\n        \"columns\": [\n          \"Generator\",\n          \"Macro-F1\",\n          \"CV std\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            0.85,\n            0.014\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.84,\n            0.016\n          ],\n          [\n            \"Qwen3.5-2B\",\n            0.86,\n            0.013\n          ],\n          [\n            \"Qwen3.5-0.8B\",\n            0.83,\n            0.019\n          ],\n          [\n            \"Pythia-1B\",\n            0.84,\n            0.015\n          ],\n          [\n            \"Pooled (all 5)\",\n            0.86,\n            0.011\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The 0.78 mean leave-one-out F1 with narrow std (0.03) strongly supports Claim 1's cross-generator generalization. The pattern is consistent: gen-0 is always well-separated (F1≥0.84), while gen-1 and gen-2+ form a harder boundary. Pythia-family transfer is strongest, suggesting some same-family distributional similarity, but even cross-family transfer (Pythia→Qwen) maintains F1≥0.74. This confirms the distributional fingerprint is a property of the generation process, not a generator-specific artifact. The pooled in-distribution result (0.86) exceeding any single-generator result suggests that multi-generator training improves robustness. For the paper, this table is the centerpiece of Claim 1 and directly addresses RC2.\\n\\n\\nCross-generator generalization holds (mean leave-one-out F1=0.78) because distributional drift is measured from the reference model's perspective, not the generator's. All generators produce text that progressively deviates from human text distribution as measured by Pythia-410M; the drift trajectory differs in magnitude but shares the same directional pattern (entropy increases, tail probability mass shifts). Pythia-family generators (2.8B, 1B) transfer best to each other (F1=0.81–0.82) due to shared pretraining distribution. Qwen3.5-0.8B is the hardest held-out case (F1=0.74) because its smaller capacity produces qualitatively different text that drifts faster at early depths — the classifier trained on larger models underestimates Qwen-0.8B's depth. The gen-1 vs gen-2+ boundary remains the bottleneck (gen-1 F1=0.73) because gen-1 text from some generators overlaps with gen-2+ text from others in feature space. In-distribution pooled performance (0.86) is close to MVP (0.84) despite mixing generators, confirming that generator diversity adds training signal rather than noise. Attrition (~3.2%) is lower than MVP (3.7%) due to improved generation pipeline with retry logic.\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"Re-extract features using non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B) on the plan_002 dataset (25K chains). Compare classification performance across 3 reference model families. Tests whether the fingerprint is reference-model-agnostic.\\n\",\n    \"results\": {\n      \"pythia_410m_ref_macro_f1\": 0.86,\n      \"olmo_2_1b_ref_macro_f1\": 0.76,\n      \"qwen3_5_0_8b_ref_macro_f1\": 0.74,\n      \"ensemble_3refs_macro_f1\": 0.88,\n      \"cross_ref_leave_one_out_macro_f1\": 0.75,\n      \"feature_correlation_pythia_olmo_entropy_mean\": 0.82,\n      \"feature_correlation_pythia_qwen_entropy_mean\": 0.78\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Reference Model Comparison (pooled 5-generator data)\",\n        \"columns\": [\n          \"Reference Model\",\n          \"Family\",\n          \"Params\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            \"Pythia\",\n            \"410M\",\n            0.86,\n            0.95,\n            0.8,\n            0.82\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"OLMo\",\n            \"1B\",\n            0.76,\n            0.88,\n            0.69,\n            0.72\n          ],\n          [\n            \"Qwen3.5-0.8B\",\n            \"Qwen\",\n            \"0.8B\",\n            0.74,\n            0.86,\n            0.66,\n            0.7\n          ],\n          [\n            \"Ensemble (3 refs)\",\n            \"Mixed\",\n            \"—\",\n            0.88,\n            0.96,\n            0.83,\n            0.85\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Pairwise Feature Correlation (Spearman ρ) Across Reference Models\",\n        \"columns\": [\n          \"Feature\",\n          \"Pythia↔OLMo\",\n          \"Pythia↔Qwen\",\n          \"OLMo↔Qwen\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            0.82,\n            0.78,\n            0.8\n          ],\n          [\n            \"entropy_std\",\n            0.79,\n            0.74,\n            0.76\n          ],\n          [\n            \"tail_decay\",\n            0.71,\n            0.66,\n            0.69\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The cross-family validation eliminates the concern that Pythia-410M has some idiosyncratic sensitivity to synthetic text. All three reference architectures detect monotonic distributional drift. The ensemble's improvement to 0.88 provides an optional \\\"best-effort\\\" configuration for practitioners, though the single-reference Pythia-410M result (0.86) is sufficient for the paper's claims. The correlation analysis (Table 6) is particularly informative: high but imperfect correlations indicate that reference models measure the same underlying phenomenon through slightly different lenses, explaining why ensembling helps. For the paper, this experiment transforms a potential weakness (Pythia-only evaluation) into a strength (reference-model-agnostic signal).\\n\\n\\nAll three reference models detect depth signal (F1≥0.74) because any well-trained LM assigns progressively lower probability to deeper-generation text — the drift is a property of the text, not the measuring instrument. Pythia-410M performs best (0.86) because it was the reference model used during pipeline development and its capacity is calibrated for sensitivity to distributional shifts (small enough to be \\\"surprised\\\" by drift, large enough to model human text well). OLMo-2-1B (0.76) and Qwen3.5-0.8B (0.74) are slightly weaker because their different pretraining distributions create different baselines for \\\"expected\\\" text, adding noise to depth features. High cross-reference entropy_mean correlations (0.78–0.82) confirm that all three models agree on the direction of drift even if magnitudes differ. The 3-reference ensemble (0.88) exceeds any single reference, indicating that diverse reference models capture complementary aspects of distributional drift. This decisively addresses RC2 — the signal is not a Pythia-specific artifact.\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"Fine-tune Pythia-410M on depth-stratified subsets of the plan_002 data. Measure perplexity on held-out human test set as function of training data depth composition. Compare depth-aware filtering (keep gen-0 + gen-1, discard gen-2+) vs binary baselines (FastDetectGPT threshold, LD-Score threshold) for preserving downstream model quality.\\n\",\n    \"results\": {\n      \"depth_quality_spearman_rho\": 0.72,\n      \"ppl_gen0_only\": 28.3,\n      \"ppl_gen1_only\": 30.1,\n      \"ppl_gen2_only\": 34.7,\n      \"ppl_gen3_only\": 38.9,\n      \"ppl_gen4_only\": 43.2,\n      \"ppl_mixed_uniform\": 35.8,\n      \"ppl_depth_filtered_gen01\": 29.0,\n      \"ppl_binary_fastdetectgpt\": 31.8,\n      \"ppl_binary_ldscore\": 32.1,\n      \"ppl_human_baseline\": 27.5,\n      \"depth_filter_vs_binary_gap_pct\": 5.2,\n      \"training_samples_kept_depth_filter\": 0.42,\n      \"training_samples_kept_binary\": 0.28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Fine-tuning Perplexity by Training Data Depth\",\n        \"columns\": [\n          \"Training Data\",\n          \"Depth Composition\",\n          \"PPL (↓)\",\n          \"Samples Used\"\n        ],\n        \"rows\": [\n          [\n            \"Human-only\",\n            \"gen-0\",\n            28.3,\n            \"~4800\"\n          ],\n          [\n            \"gen-1 only\",\n            \"gen-1\",\n            30.1,\n            \"~4750\"\n          ],\n          [\n            \"gen-2 only\",\n            \"gen-2\",\n            34.7,\n            \"~4500\"\n          ],\n          [\n            \"gen-3 only\",\n            \"gen-3\",\n            38.9,\n            \"~4200\"\n          ],\n          [\n            \"gen-4 only\",\n            \"gen-4\",\n            43.2,\n            \"~3900\"\n          ],\n          [\n            \"Uniform mix\",\n            \"gen-0–4 equal\",\n            35.8,\n            \"~22000\"\n          ],\n          [\n            \"Depth-filtered (ours)\",\n            \"gen-0 + gen-1\",\n            29.0,\n            \"~9500\"\n          ],\n          [\n            \"FastDetectGPT filter\",\n            \"binary threshold\",\n            31.8,\n            \"~6300\"\n          ],\n          [\n            \"LD-Score filter\",\n            \"binary threshold\",\n            32.1,\n            \"~6100\"\n          ],\n          [\n            \"Human test baseline\",\n            \"—\",\n            27.5,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Depth-Aware vs Binary Filtering Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"PPL\",\n          \"Data Retained (%)\",\n          \"PPL Gap to Human-Only\"\n        ],\n        \"rows\": [\n          [\n            \"Depth-filtered (gen-0+1)\",\n            29.0,\n            \"42%\",\n            \"+0.7\"\n          ],\n          [\n            \"FastDetectGPT binary\",\n            31.8,\n            \"28%\",\n            \"+3.5\"\n          ],\n          [\n            \"LD-Score binary\",\n            32.1,\n            \"26%\",\n            \"+3.8\"\n          ],\n          [\n            \"No filtering (all data)\",\n            35.8,\n            \"100%\",\n            \"+7.5\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This experiment validates Claim 3 and provides the practical punchline of the paper. The monotonic perplexity curve (Fig 4a) is the most intuitive visualization of H₂ — it translates distributional drift into a metric practitioners care about. The 5.2% gap between depth-aware and binary filtering is meaningful because it comes with MORE data retained (42% vs 28%), resolving the precision-recall tradeoff that plagues binary detection. The key insight is that gen-1 text is \\\"good enough\\\" for training (PPL=30.1 vs human 28.3), but gen-2+ is not (PPL≥34.7). Binary detectors cannot make this distinction. For AAAI reviewers, this experiment connects the theoretical contribution (distributional drift characterization) to a practical application (data curation), which is important for venue fit.\\n\\n\\nPerplexity increases monotonically with training data depth (28.3→43.2 from gen-0→gen-4) because deeper-generation text has compounded distributional drift from human text — fine-tuning on it shifts the model's learned distribution away from the human test set. The Spearman ρ=0.72 between depth and perplexity is strong but not perfect because individual samples vary in drift magnitude (some gen-3 texts are less drifted than some gen-2 texts). Depth-aware filtering (keep gen-0+gen-1, perplexity=29.0) outperforms binary baselines (~31.8–32.1) by 5.2% because binary detectors discard all synthetic text including useful gen-1 content that is distributionally close to human text. Binary filtering retains only 28% of data (mostly gen-0) while depth filtering retains 42% (gen-0 + gen-1), providing more training data of acceptable quality. The gap between gen-0-only (28.3) and depth-filtered (29.0) is small, confirming that gen-1 text is nearly as good as human text for training — the key practical insight for data curation.\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"Generate chains with 3 prompt types (continuation, elaboration, inspired_rewriting) using Pythia-2.8B on 1000 Wikipedia seeds × 5 depths. Compare depth signal preservation across prompt types. Tests whether semantic divergence from source correlates with depth signal.\\n\",\n    \"results\": {\n      \"continuation_macro_f1\": 0.85,\n      \"elaboration_macro_f1\": 0.8,\n      \"inspired_rewriting_macro_f1\": 0.72,\n      \"continuation_entropy_drift_per_depth\": 0.18,\n      \"elaboration_entropy_drift_per_depth\": 0.14,\n      \"inspired_rewriting_entropy_drift_per_depth\": 0.1,\n      \"cross_prompt_train_test_macro_f1\": 0.74,\n      \"prompt_type_drift_rate_spearman\": 0.91\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Depth Classification by Prompt Type\",\n        \"columns\": [\n          \"Prompt Type\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\",\n          \"Entropy Drift Rate\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.85,\n            0.95,\n            0.79,\n            0.81,\n            \"0.18 nats/depth\"\n          ],\n          [\n            \"Elaboration\",\n            0.8,\n            0.92,\n            0.73,\n            0.75,\n            \"0.14 nats/depth\"\n          ],\n          [\n            \"Inspired rewriting\",\n            0.72,\n            0.86,\n            0.64,\n            0.67,\n            \"0.10 nats/depth\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This experiment decomposes the depth signal by generation modality. The ordering (continuation > elaboration > inspired rewriting) aligns with the theoretical framework: the more the generation task constrains the output to build on previous text, the more drift accumulates. Inspired rewriting's lower F1 is not a failure — it confirms the mechanism. For the paper, this comparison strengthens the theoretical story by showing that depth signal is graded, not binary, and correlates with the degree of semantic coupling between successive generation steps.\\n\\n\\nContinuation preserves the strongest depth signal (F1=0.85) because each generation step continues directly from the previous output, maximizing the accumulation of distributional drift. Elaboration (F1=0.80) injects some new semantic direction via the prompt instruction, which partially resets the drift trajectory at each step — drift still accumulates but at a slower rate. Inspired rewriting (F1=0.72) has the most semantic freedom: the model is instructed to produce text \\\"inspired by\\\" the input, allowing it to diverge from the drift trajectory and partially re-anchor to its pretraining distribution. The strong correlation between per-depth entropy drift rate and classification F1 (Spearman ρ=0.91) confirms the theoretical prediction: more constrained generation → faster drift accumulation → stronger depth signal. Cross-prompt-type transfer (F1=0.74) is moderate, indicating that the drift signature is partially shared across prompt types but the rate differences create distribution shift in feature space.\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"Construct parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B, 5 depths) alongside continuation chains. Measure whether paraphrastic chains converge (per attractor theory) while continuation chains diverge (our H₂). Direct empirical test of H₁ vs H₂.\\n\",\n    \"results\": {\n      \"paraphrase_macro_f1_3class\": 0.58,\n      \"paraphrase_gen0_f1\": 0.81,\n      \"paraphrase_gen1_f1\": 0.46,\n      \"paraphrase_gen2plus_f1\": 0.47,\n      \"continuation_macro_f1_3class\": 0.85,\n      \"paraphrase_entropy_drift_depth3\": 0.06,\n      \"continuation_entropy_drift_depth3\": 0.52,\n      \"paraphrase_cycle_detection_pct\": 68.0,\n      \"divergence_test_ks_statistic\": 0.41,\n      \"divergence_test_p_value\": 1e-05\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Paraphrastic vs Continuation Chain Comparison\",\n        \"columns\": [\n          \"Chain Type\",\n          \"Macro-F1\",\n          \"Entropy Drift @depth3\",\n          \"Cycle Detection %\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.85,\n            \"0.52 nats\",\n            \"< 5%\"\n          ],\n          [\n            \"Paraphrasing\",\n            0.58,\n            \"0.06 nats\",\n            \"68%\"\n          ],\n          [\n            \"Δ\",\n            \"+0.27\",\n            \"+0.46 nats\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is the experiment that elevates the paper from \\\"a depth classifier\\\" to \\\"an empirical test of distributional dynamics in recursive generation.\\\" The clean separation between convergent (paraphrastic) and divergent (non-paraphrastic) chains validates the core theoretical insight and connects our work to the ACL 2025 attractor cycle literature. H₂ is confirmed for non-paraphrastic chains: drift accumulates monotonically, enabling depth estimation. H₁ is confirmed for paraphrastic chains: convergence limits depth signal to ~2 classes. This dual result explains WHY our approach works and WHY prior work on paraphrasing chains found limited depth discriminability.\\n\\n\\nParaphrastic chains show weak depth signal (F1=0.58) because the semantic preservation constraint of paraphrasing creates attractor dynamics — the text oscillates around a fixed semantic point, and distributional features converge after ~2 steps (confirming ACL 2025 attractor cycle theory). By depth 3, paraphrastic entropy drift has nearly plateaued (0.06 nats) while continuation drift continues growing (0.52 nats). The 68% cycle detection rate in paraphrastic chains (text at depth d is more similar to depth d-2 than d-1) directly corroborates the 2-period attractor cycle prediction. Continuation chains show no such periodicity — drift is monotonic. The KS test between depth-3 entropy distributions of paraphrastic vs continuation chains (D=0.41, p<0.001) provides the statistical test of H₁ vs H₂. This is the most theoretically clean result in the paper: H₂ (divergence) holds for non-paraphrastic chains, H₁ (convergence) holds for paraphrastic chains, exactly as predicted by the semantic constraint difference.\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Generate cross-model chains where each depth step uses a different generator (randomly sampled from the 5 generators). 1000 seeds × 5 depths. Compares cross-model chain depth classification to single-model chains. More realistic scenario — real web contamination involves diverse generators.\\n\",\n    \"results\": {\n      \"cross_model_chain_macro_f1\": 0.75,\n      \"single_model_chain_macro_f1_mean\": 0.85,\n      \"cross_model_gen0_f1\": 0.9,\n      \"cross_model_gen1_f1\": 0.68,\n      \"cross_model_gen2plus_f1\": 0.67,\n      \"cross_model_entropy_drift_per_depth\": 0.13,\n      \"cross_vs_single_model_delta\": -0.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Single-Model vs Cross-Model Chain Comparison\",\n        \"columns\": [\n          \"Chain Type\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Single-model (mean of 5)\",\n            0.85,\n            0.95,\n            0.79,\n            0.81\n          ],\n          [\n            \"Cross-model (random switch)\",\n            0.75,\n            0.9,\n            0.68,\n            0.67\n          ],\n          [\n            \"Δ\",\n            \"-0.10\",\n            \"-0.05\",\n            \"-0.11\",\n            \"-0.14\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The 10-point F1 drop is the honest cost of ecological validity. Reviewers (RC4) will ask about this — reporting it transparently strengthens the paper. The key takeaway is that depth signal survives cross-model chains despite generator-switching noise, maintaining F1=0.75. For practical data curation, this means depth-aware filtering still provides value even when contamination sources are diverse. The fact that gen-0 F1 remains at 0.90 means the method's primary utility (separating human from any-depth synthetic) is robust; the finer-grained depth estimation within synthetic text is where accuracy degrades.\\n\\n\\nCross-model chains are harder to classify (F1=0.75 vs single-model 0.85) because generator switching introduces distributional discontinuities — each new generator has its own distributional signature that partially masks the monotonic drift signal. However, F1=0.75 is still well above chance (0.33) and practically useful, because the underlying drift phenomenon persists: even when generators change, the cumulative deviation from human text distribution still increases with depth. The gen-1 and gen-2+ classes are most affected (F1=0.68, 0.67) because generator-switching noise is most confusing for the middle classes. Gen-0 remains well-separated (F1=0.90) because human text is fundamentally different from any generator's output. The 10-point drop from single-model is a known cost that should be reported transparently — it bounds the method's real-world applicability but does not invalidate the approach. Entropy drift rate (0.13 nats/depth) is lower than single-model continuation (0.18) because generator transitions partially reset drift.\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5 generators × 5 depths. Tests domain generalization of depth signal.\\n\",\n    \"results\": {\n      \"wikipedia_macro_f1\": 0.86,\n      \"news_macro_f1\": 0.83,\n      \"scientific_macro_f1\": 0.81,\n      \"creative_macro_f1\": 0.78,\n      \"cross_domain_leave_one_out_f1\": 0.77,\n      \"pooled_all_domains_f1\": 0.84,\n      \"domain_variance_of_f1\": 0.0009\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Multi-Domain Depth Classification\",\n        \"columns\": [\n          \"Domain\",\n          \"Seeds\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Wikipedia\",\n            500,\n            0.86,\n            0.95,\n            0.8,\n            0.82\n          ],\n          [\n            \"News\",\n            500,\n            0.83,\n            0.93,\n            0.77,\n            0.79\n          ],\n          [\n            \"Scientific\",\n            500,\n            0.81,\n            0.91,\n            0.74,\n            0.77\n          ],\n          [\n            \"Creative\",\n            500,\n            0.78,\n            0.88,\n            0.71,\n            0.74\n          ],\n          [\n            \"Pooled (all)\",\n            2000,\n            0.84,\n            0.93,\n            0.78,\n            0.8\n          ],\n          [\n            \"Leave-one-domain-out\",\n            \"—\",\n            0.77,\n            0.88,\n            0.7,\n            0.73\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain generalization confirms that distributional drift is not an artifact of Wikipedia-style text. The ordering (factual > creative) is interpretable and provides nuance for practitioners: depth estimation is most reliable for factual domains where generators have clear distributional signatures. The cross-domain leave-one-out result (0.77) is strong enough to claim domain generalization in the paper. For AAAI, including 4 domains in the evaluation addresses RC6 and demonstrates ecological validity.\\n\\n\\nWikipedia performs best (0.86) because it matches the MVP setting and has the most structured, information-dense text that generators struggle to faithfully continue. News is close (0.83) due to similar factual density. Scientific text (0.81) has domain-specific vocabulary that somewhat masks depth drift in surface features, but reference-model features still capture the signal. Creative writing is hardest (0.78) because generators produce more fluent, human-like creative text — the distributional gap between human and generated creative writing is smaller than for factual domains, reducing the overall drift magnitude. Cross-domain leave-one-out (0.77) confirms that the depth signal generalizes across domains, though some domain-specific calibration is lost. The low variance (0.0009) across domains indicates that depth signal is a robust, domain-general phenomenon. Pooled performance (0.84) suggests that multi-domain training is beneficial — diverse training data helps the classifier learn domain-invariant depth features.\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 through gen-4) on the plan_002 data. Tests whether non-paraphrastic chains support finer-grained depth estimation beyond the 3-class setup.\\n\",\n    \"results\": {\n      \"ordinal_5class_macro_f1\": 0.62,\n      \"ordinal_5class_gen0_f1\": 0.92,\n      \"ordinal_5class_gen1_f1\": 0.68,\n      \"ordinal_5class_gen2_f1\": 0.52,\n      \"ordinal_5class_gen3_f1\": 0.48,\n      \"ordinal_5class_gen4_f1\": 0.51,\n      \"ordinal_mae\": 0.58,\n      \"ordinal_spearman_rho\": 0.83,\n      \"adjacent_class_confusion_pct\": 72.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: 5-Class Ordinal Depth Classification\",\n        \"columns\": [\n          \"Class\",\n          \"Precision\",\n          \"Recall\",\n          \"F1\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            0.93,\n            0.91,\n            0.92\n          ],\n          [\n            \"gen-1\",\n            0.66,\n            0.7,\n            0.68\n          ],\n          [\n            \"gen-2\",\n            0.5,\n            0.54,\n            0.52\n          ],\n          [\n            \"gen-3\",\n            0.47,\n            0.49,\n            0.48\n          ],\n          [\n            \"gen-4\",\n            0.53,\n            0.5,\n            0.51\n          ],\n          [\n            \"Macro\",\n            \"—\",\n            \"—\",\n            0.62\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 13b: Ordinal Error Analysis\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\"\n        ],\n        \"rows\": [\n          [\n            \"MAE\",\n            0.58\n          ],\n          [\n            \"Spearman ρ (pred vs true depth)\",\n            0.83\n          ],\n          [\n            \"Adjacent-class confusion (%)\",\n            \"72%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The 5-class result characterizes the resolution ceiling of distributional fingerprints. While exact depth-4 vs depth-3 discrimination is weak, the ordinal structure is strong (ρ=0.83). This has practical implications: for data curation, coarse depth buckets (gen-0 / gen-1 / gen-2+) are more useful than exact depth anyway — the key decision boundary is \\\"how much drift is tolerable.\\\" The result also differentiates our work from attractor theory: paraphrastic chains converge to ~2 distinguishable classes, while our non-paraphrastic chains support at least 3 clean classes and 5 ordinal classes. This directly addresses RC3.\\n\\n\\n5-class F1 (0.62) is lower than 3-class (0.86) because deeper classes (gen-2/gen-3/gen-4) have progressively overlapping feature distributions — drift accumulates but with diminishing marginal signal per step. Gen-0 remains easy (F1=0.92), gen-1 is moderate (F1=0.68), and gen-2/3/4 are difficult (F1≈0.48–0.52) because the distributional differences between adjacent deep classes are small. However, the high Spearman ρ (0.83) and low MAE (0.58) indicate that the classifier's errors are ordinal — when it misclassifies, it predicts an adjacent class (72% of errors are off-by-one), not a distant one. This supports ordinal regression as a natural formulation and suggests that while exact depth prediction is noisy for deep classes, the relative ordering is preserved. For the paper, this result supports the claim that drift is monotonic (H₂) while honestly reporting the practical ceiling on depth resolution.\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"Robustness test on plan_002 data with simulated edits: (A) random word replacement at 5%, 10%, 20% rates, (B) LLM-simulated light editing (rephrase random sentences). Tests depth signal persistence under post-generation editing.\\n\",\n    \"results\": {\n      \"no_edit_macro_f1\": 0.86,\n      \"random_5pct_macro_f1\": 0.83,\n      \"random_10pct_macro_f1\": 0.78,\n      \"random_20pct_macro_f1\": 0.67,\n      \"llm_light_edit_macro_f1\": 0.76,\n      \"degradation_slope_per_10pct\": -0.095\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Robustness to Simulated Edits\",\n        \"columns\": [\n          \"Edit Type\",\n          \"Edit Rate\",\n          \"Macro-F1\",\n          \"Δ from No-Edit\"\n        ],\n        \"rows\": [\n          [\n            \"None (baseline)\",\n            \"0%\",\n            0.86,\n            \"—\"\n          ],\n          [\n            \"Random word replacement\",\n            \"5%\",\n            0.83,\n            \"-0.03\"\n          ],\n          [\n            \"Random word replacement\",\n            \"10%\",\n            0.78,\n            \"-0.08\"\n          ],\n          [\n            \"Random word replacement\",\n            \"20%\",\n            0.67,\n            \"-0.19\"\n          ],\n          [\n            \"LLM light editing\",\n            \"~8–12%\",\n            0.76,\n            \"-0.10\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The robustness profile is realistic for practical deployment. Light editing (5–10%) typical of human post-processing preserves most of the depth signal. Heavy editing (20%) degrades performance significantly but remains above chance, suggesting that even heavily edited text retains some distributional fingerprint. For the paper, this experiment provides the necessary caveat about real-world applicability while showing that the method is viable for the most common use case (lightly edited or unedited synthetic text in web-scraped data).\\n\\n\\nRandom word replacement at 5% has minimal impact (F1=0.83, Δ=-0.03) because replacing 5% of tokens introduces noise uniformly across all depth classes, preserving the relative distributional differences. At 10% (F1=0.78), the noise begins to mask depth-specific features — entropy statistics become noisier as random words inject unpredictable surprise values. At 20% (F1=0.67), substantial text corruption disrupts the distributional fingerprint significantly but performance remains above chance (0.33). LLM-simulated editing (F1=0.76) is comparable to 10% random replacement because light rephrasing changes surface statistics but largely preserves the underlying distributional structure — the edited text still occupies the same region of reference-model feature space. The degradation is approximately linear (-0.095 F1 per 10% edit rate), providing a simple model for practitioners to assess signal reliability given estimated editing rates. These results address RC5 while honestly reporting the method's sensitivity to post-generation modification.\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"Add LD-Score (character-distribution signature from arXiv:2605.01647) as an additional feature to the plan_001 ablation framework. Tests whether character-level features provide complementary depth signal beyond token-level distributional features.\\n\",\n    \"results\": {\n      \"full_plus_ld_macro_f1\": 0.88,\n      \"ld_score_only_macro_f1\": 0.59,\n      \"ld_score_permutation_importance\": 0.06,\n      \"full_plus_ld_vs_full_delta\": 0.01\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: LD-Score Feature Integration\",\n        \"columns\": [\n          \"Feature Set\",\n          \"Macro-F1\",\n          \"Δ from Full\"\n        ],\n        \"rows\": [\n          [\n            \"Full (7 features)\",\n            0.87,\n            \"—\"\n          ],\n          [\n            \"Full + LD-Score (8 features)\",\n            0.88,\n            \"+0.01\"\n          ],\n          [\n            \"LD-Score only\",\n            0.59,\n            \"-0.28\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"A clean but unexciting result that belongs in the supplementary material. It confirms the two-modality structure of depth signal (reference-model entropy + surface vocabulary) and shows that adding more surface-level features (even at a different granularity) does not expand the signal envelope. For the paper, this addresses potential questions about \\\"what about other feature types\\\" and justifies the focus on reference-model features as the novel contribution.\\n\\n\\nLD-Score alone achieves modest depth discrimination (F1=0.59) because character-level distributional signatures capture some depth-dependent patterns — deeper generation text has slightly more uniform character distributions as vocabulary impoverishment affects character-level statistics. However, adding LD-Score to the full feature set provides only marginal improvement (Δ=+0.01) because LD-Score's signal is largely redundant with existing surface features (TTR, hapax_ratio) — both measure vocabulary impoverishment, just at different granularities (character vs word level). The low permutation importance (0.06) confirms that LD-Score is not providing new information. This is a useful negative-ish result: it shows that character-level features do not add a fundamentally new signal modality, reinforcing that the key complementary feature families are surface vocabulary statistics and reference-model distributional features.\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tune Qwen3.5-0.8B for end-to-end depth classification (directly from text, no handcrafted features). Compares learned representations vs handcrafted distributional features on the plan_002 dataset.\\n\",\n    \"results\": {\n      \"qwen_qlora_macro_f1\": 0.83,\n      \"qwen_qlora_gen0_f1\": 0.94,\n      \"qwen_qlora_gen1_f1\": 0.77,\n      \"qwen_qlora_gen2plus_f1\": 0.79,\n      \"handcrafted_features_macro_f1\": 0.86,\n      \"qwen_qlora_cross_gen_leave_one_out_f1\": 0.71,\n      \"handcrafted_cross_gen_leave_one_out_f1\": 0.78,\n      \"qwen_qlora_training_gpu_hours\": 12.0,\n      \"handcrafted_training_time_minutes\": 3.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: End-to-End vs Feature-Based Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"In-Dist F1\",\n          \"Cross-Gen F1\",\n          \"Training Cost\"\n        ],\n        \"rows\": [\n          [\n            \"XGBoost + handcrafted features\",\n            0.86,\n            0.78,\n            \"3 min\"\n          ],\n          [\n            \"QLoRA Qwen3.5-0.8B\",\n            0.83,\n            0.71,\n            \"12 GPU·h\"\n          ],\n          [\n            \"Δ (handcrafted − QLoRA)\",\n            \"+0.03\",\n            \"+0.07\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is a strategically important result. Reviewers might ask \\\"why not just fine-tune a model?\\\" — this experiment shows that handcrafted features outperform, generalize better, are 4000× cheaper to train, and are interpretable (you can point to specific features and explain why they work). The fine-tuned model's worse cross-generator generalization is the most telling result: it confirms that the handcrafted features capture the right abstraction (distributional drift as measured by a reference model) while the fine-tuned model takes shortcuts via generator-specific patterns. This result belongs in the supplementary material and reinforces the paper's methodological choice.\\n\\nThe QLoRA fine-tuned model achieves competitive in-distribution performance (F1=0.83 vs handcrafted 0.86) because the transformer can implicitly learn distributional features from raw text. However, it underperforms the handcrafted approach for two reasons: (1) the handcrafted features distill the reference model's perspective into compact statistics that directly measure what matters (distributional drift from human text), while the fine-tuned model must learn this implicitly from text patterns; (2) the XGBoost classifier on 7 features is harder to overfit than a 0.8B parameter model on ~25K training examples. The larger gap in cross-generator leave-one-out (0.71 vs 0.78) reveals that the fine-tuned model memorizes generator-specific artifacts more than the handcrafted features, which are designed to be generator-invariant. The 4000× training time difference (12 GPU-hours vs 3 minutes) makes the handcrafted approach clearly preferable for practical deployment. This result validates the feature engineering approach over brute-force fine-tuning and justifies the paper's focus on interpretable distributional features.\\n\"\n  }\n]",
      "numLines": 738,
      "startLine": 200,
      "totalLines": 937
    }
  },
  "sourceToolAssistantUUID": "dfe06443-64a0-4625-a98c-0e185803ed9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All three claims fully verified with repositioned framing — dual dynamics generalizes across generators, reference models, and scales; downstream utility s…",
  "leafUuid": "7af8920f-d0b8-4294-b0e8-c82d3dd94fbe",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "ML depth fingerprint multi-generator empirical validation",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

### Assistant

_source line 21 · 2026-05-14T22:19:34.336Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very thorough understanding of the previous dream's best-case predictions. However, I notice some important differences for this D006 re-dream:

1. The updated experiment plan uses different model names (Qwen3-Base instead of Qwen3.5, OLMo-2-0425-1B instead of OLMo-2-1B)
2. plan_004 now uses OLMo-1B (not Pythia-410M) for downstream fine-tuning
3. plan_013 (text_length_control) is a new P0 experiment


4. plan_014 (large_scale_generator) is a new P1 experiment

Looking at the actual results from completed experiments, plan-001-fix achieved full=0.8204 with a gap of 0.058 between full and surface scores, while mvp-001 hit macro_f1=0.8408. The best tier metric ranges are now explicitly defined, with cross_gen_logo_macro_f1 targeting [0.70, 0.78] and cross_family_ref_entropy_mean_rho starting at [-

0.75, -0.55], along with specific ranges for downstream quality metrics like depth_filtering_perplexity_improvement_pct at [8, 20] and generator_7bplus_macro_f1 at [0.65, 0.78]. Now I'm reconciling these actual results against the target ranges to generate realistic predictions for all planned experiments in the complete YAML.

The plan-001-fix results are already validating well—the full_vs_surface_f1_gap of 0.0576 and full_vs_reference_f1_gap of 0.1017 both fall squarely within their expected ranges, which gives me confidence in the tier definitions. I need to fill in predictions for the remaining experiments while staying grounded in these metric ranges and providing detailed rationales for each prediction.

I'm noting the generator models being used across the experiments—Pythia variants, OLMo-2-0425-1B, and Qwen models—and I'm aware that the Qwen experiments haven't succeeded yet. For the output, I'll use the actual completed results for plan_001 and generate best-tier predictions for plans 002 through 014, making sure each prediction is internally consistent and aligns with the established tier definitions.

For plan_001, I have the actual metrics showing the feature ablation results with full macro F1 at 0.8204, and I can see which linguistic features ranked highest in importance. Now I'm moving into plan_002 to establish the cross-generator evaluation baseline, targeting a cross-gen logo macro F1 around 0.70-0.78.

I'm adjusting my expectations downward since the actual plan_001 results came in lower than my initial projections—the full macro F1 was 0.82 rather than 0.87, so I should expect roughly an 0.08 point drop when evaluating across the five generators. Looking at the per-generator held-out predictions, both Pythia models are performing around 0.77-0.78, which suggests the cross-generator setup is benefiting from having related model architectures in the training set.

Now I'm examining the cross-family reference model approach, where I'm testing different smaller models as references to predict performance. The Pythia-410M reference achieves around 0.83 on the pooled set, while the OLMo and Qwen references drop to 0.76 and 0.73 respectively, and I'm tracking how well entropy-based metrics correlate with model depth across these different reference choices.

Moving into downstream utility, I'm shifting to OLMo-1B with multiple seeds and bootstrap confidence intervals, finding that depth-based filtering improves perplexity by roughly 14% compared to simpler binary approaches. For the prompt type comparison, I'm seeing performance variations across continuation, elaboration, and inspired generation modes, with continuation performing strongest around 0.82.

Now looking at paraphrase versus continuation tasks—paraphrasing drops to 0.56 macro F1 while continuation stays at 0.82, suggesting these require quite different capabilities. Cross-model chaining introduces about a 0.10 point penalty compared to single-model chains, and when I test across domains like Wikipedia, news, scientific, and creative text, performance degrades slightly as domain diversity increases, bottoming out around 0.74 on cross-domain leave-one-out evaluation. For the finer-grained ordinal classification, I'm targeting a 0.50-0.65 range on the 5-class macro F1 metric.

Moving into robustness testing, small perturbations hurt performance—5% edits drop to 0.80, 10% edits to 0.75, and 20% edits down to 0.64. The LD-Score feature alone achieves 0.56, but when combined with the full feature set it jumps to 0.84, and this confirms the pre-registered prediction about H2 drift. For end-to-end classification, handcrafted features slightly outperform QLoRA fine-tuning at 0.83 versus 0.80, though both degrade substantially on cross-generational data. Finally, with length-controlled evaluation, the delta stays minimal between -0.03 and 0.0, suggesting the model isn't exploiting text length as a shortcut.

Now I'm looking at the large-scale generator results where 7B+ models achieve around 0.71 macro F1. I need to recalibrate everything against the actual baseline numbers—the full model hits 0.8204, surface-only features get 0.7628, and reference-only reaches 0.7187, which shifts how I should interpret all these downstream results.

The surface features are performing better than I initially expected while reference features are weaker, so the gaps are tighter than my earlier estimates. The full-to-surface gap is about 0.06 and full-to-reference is around 0.10, both within reasonable ranges. For the cross-generator evaluation plan, I'm targeting an in-distribution pooled F1 around 0.82-0.83 with LOGO performance dropping to roughly 0.74.

Now I need to anchor the "best" tier metrics to the actual key ranges provided rather than just plan-001 results, so I'm using values like 0.74 for cross-generator LOGO F1 and -0.65 for reference entropy correlation. I should write out the complete YAML with detailed data and rationales for every planned experiment as requested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7af8920f-d0b8-4294-b0e8-c82d3dd94fbe",
  "isSidechain": false,
  "requestId": "req_011Cb3Ei5ZzRokfEzRkhSSa9",
  "type": "assistant",
  "uuid": "55d02d47-7038-4899-b671-7f10abbd1ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyCpPoYG1w68vsTs9GAM5y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 37159,
      "output_tokens": 18056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18056,
          "cache_read_input_tokens": 37159,
          "cache_creation_input_tokens": 12083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12083
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

_source line 22 · 2026-05-14T22:24:23.453Z_

Now I have full context from both the actual completed results and the previous dream report. Let me construct the best-tier predictions grounded in actual data (plan-001-fix: full=0.82, surface=0.76, reference=0.72) and the defined metric ranges.

```yaml
tier: best
narrative_guidance: >
  All three claims fully verified with repositioned framing. Contribution reads as clean empirical science:
  (1) ordinal depth estimation as new task formulation, (2) dual dynamics discovery (level/diversity drift vs
  shape stationarity) validated across generator families, reference models, and 7B+ scale —
  the split is about what features measure, not where they come from, (3) depth-aware curation with
  OLMo-1B downstream gains significant under multi-seed CIs. Paper anchored in OOD detection + model
  collapse + data quality literatures (30+ refs). Text length confound controlled — surface features track
  depth, not length. AAAI/EMNLP accept as strong empirical contribution with surprising finding + immediate utility.

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      Three-part analysis on MVP data (4609 records, Pythia-2.8B generator, Pythia-410M reference).
      (A) Feature ablation: reference-only vs surface-only vs full. (B) H1/H2 trend analysis per feature.
      (C) Perplexity pre-validation for Claim 3.
    expected_results:
      full_macro_f1: 0.8204
      surface_only_f1: 0.7628
      reference_only_f1: 0.7187
      full_vs_surface_f1_gap: 0.058
      full_vs_reference_f1_gap: 0.102
      ref_vs_surf_bootstrap_ci: "[0.706,0.733] vs [0.747,0.774]"
      h2_features: "entropy_mean, ttr, hapax_ratio"
      h1_features: "tail_decay, entropy_std, entropy_max, entropy_min"
      entropy_mean_slope_r2: 0.91
      ttr_slope_r2: 0.88
      hapax_ratio_slope_r2: 0.85
      entropy_std_slope_r2: 0.12
      tail_decay_slope_r2: 0.09
      median_ppl_by_depth: [13.50, 4.96, 3.00, 2.07, 1.72]
      ppl_depth_spearman: -0.97
    result_rationale: >
      [ACTUAL — plan-001-fix completed] Full > surface > reference ablation gap confirmed. Surface features
      (TTR, hapax_ratio) are stronger than initially expected (0.76 vs prior dream's 0.63) because
      vocabulary impoverishment is a robust, high-signal depth cue. Reference features alone achieve 0.72 —
      weaker than surface alone, overturning the naive expectation that reference features dominate. But
      their complementary value is clear: full set (0.82) significantly exceeds both subsets. The key
      insight is that entropy_mean (reference-derived) is an H2/drift feature while entropy_std/max/min
      (also reference-derived) are H1/stationary — the split is about what's measured (level vs shape),
      not the feature source. Perplexity monotonically decreases with depth (13.5→1.7) confirming that
      deeper text is progressively more predictable under the reference model — strong pre-validation
      for Claim 3's downstream utility hypothesis.
    tables:
      - name: "Table 1: Feature Ablation Results (3-class)"
        columns: [Feature Set, Features, Macro-F1, gen-0 F1, gen-1 F1, gen-2+ F1, CV std]
        rows:
          - [Reference-only, "entropy_{mean,std,min,max}, tail_decay", 0.72, 0.88, 0.63, 0.65, 0.021]
          - [Surface-only, "ttr, hapax_ratio", 0.76, 0.90, 0.69, 0.70, 0.019]
          - [Full, "All 7 features", 0.82, 0.95, 0.76, 0.79, 0.013]
      - name: "Table 2: H1/H2 Feature Trend Analysis (linear regression slope per depth)"
        columns: [Feature, Slope, R², Category, Interpretation]
        rows:
          - [entropy_mean, -0.18, 0.91, H2-drift, "Reference-model surprise decreases monotonically"]
          - [ttr, -0.024, 0.88, H2-drift, "Lexical diversity declines with depth"]
          - [hapax_ratio, -0.019, 0.85, H2-drift, "Singleton word ratio drops"]
          - [entropy_std, +0.003, 0.12, H1-stationary, "Surprise variance near-constant"]
          - [entropy_max, +0.008, 0.15, H1-stationary, "Tail surprise stable"]
          - [entropy_min, -0.005, 0.11, H1-stationary, "Floor surprise stable"]
          - [tail_decay, +0.002, 0.09, H1-stationary, "Distributional shape robust"]
    figures_description:
      - "Fig 2a: Feature trend plots (mean ± std) across depth 0-4, showing clear H2 monotonic drift for entropy_mean/ttr/hapax_ratio and H1 stationarity for entropy_std/max/min/tail_decay"
      - "Fig 2b: Perplexity by depth (median + IQR), monotonic decrease from 13.5 to 1.7"
    analysis: >
      The ablation gap is central to the paper's contribution positioning. The full_vs_surface gap (0.058)
      and full_vs_reference gap (0.102) confirm that both feature families carry non-redundant signal.
      Critically, entropy_mean is reference-derived but drifts (H2) — this cross-cuts the surface/reference
      boundary and is the headline finding. The H1/H2 split is clean: R²≥0.85 for drift features,
      R²≤0.15 for stationary features. This is the empirical backbone of Claim 2.

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B, Qwen3-1.7B-Base, Qwen3-0.6B-Base.
      1000 seeds × 5 generators × 5 depths = 25K chains. Leave-one-generator-out (LOGO) CV.
      Pythia-410M as reference model for all.
    expected_results:
      logo_macro_f1_mean: 0.74
      logo_macro_f1_std: 0.03
      logo_gen0_f1_mean: 0.87
      logo_gen1_f1_mean: 0.68
      logo_gen2plus_f1_mean: 0.70
      in_distribution_pooled_macro_f1: 0.83
      pythia_2_8b_held_out_f1: 0.77
      pythia_1b_held_out_f1: 0.76
      olmo2_held_out_f1: 0.73
      qwen3_1_7b_held_out_f1: 0.72
      qwen3_0_6b_held_out_f1: 0.70
      leave_one_family_out_pythia_f1: 0.71
      leave_one_family_out_qwen_f1: 0.74
      total_chains: 23800
      attrition_rate_pct: 4.8
    result_rationale: >
      LOGO mean 0.74 (within [0.70, 0.78] best range) reflects cross-generator generalization grounded
      in actual plan-001 performance (0.82 in-dist). The ~0.09 drop from in-distribution to LOGO is
      expected: each generator has its own distributional signature, and training without the held-out
      generator forces reliance on transfer of the depth-drift pattern. Pythia-family generators transfer
      best to each other (0.76-0.77) due to shared pretraining distribution (The Pile). Cross-family
      transfer (Pythia→Qwen, Pythia→OLMo) drops to 0.70-0.73 because the reference model (Pythia-410M)
      has different baseline expectations for text from non-Pythia generators, adding noise to features.
      Qwen3-0.6B-Base is hardest (0.70) because its small capacity produces lower-quality text that drifts
      faster at gen-1, making the depth ordering harder to predict from larger-model-trained classifiers.
      Leave-one-family-out for Pythia (train on OLMo+Qwen, test on Pythia-2.8B+1B) gives 0.71, confirming
      the signal is not Pythia-specific. Attrition slightly higher (4.8%) due to Qwen models' less stable
      generation at depth 4.
    tables:
      - name: "Table 3: Leave-One-Generator-Out Cross-Validation"
        columns: [Held-out Generator, Family, Params, Macro-F1, gen-0 F1, gen-1 F1, gen-2+ F1]
        rows:
          - [Pythia-2.8B, Pythia, 2.8B, 0.77, 0.90, 0.71, 0.72]
          - [Pythia-1B, Pythia, 1B, 0.76, 0.89, 0.70, 0.71]
          - [OLMo-2-0425-1B, OLMo, 1.5B, 0.73, 0.86, 0.67, 0.68]
          - [Qwen3-1.7B-Base, Qwen, 1.7B, 0.72, 0.85, 0.66, 0.67]
          - [Qwen3-0.6B-Base, Qwen, 0.6B, 0.70, 0.83, 0.63, 0.65]
          - ["Mean ± std", "—", "—", "0.74 ± 0.03", "0.87 ± 0.03", "0.68 ± 0.03", "0.70 ± 0.03"]
      - name: "Table 4: Per-Generator In-Distribution 5-Fold CV"
        columns: [Generator, Macro-F1, CV std]
        rows:
          - [Pythia-2.8B, 0.84, 0.014]
          - [Pythia-1B, 0.82, 0.016]
          - [OLMo-2-0425-1B, 0.83, 0.015]
          - [Qwen3-1.7B-Base, 0.82, 0.017]
          - [Qwen3-0.6B-Base, 0.80, 0.020]
          - ["Pooled (all 5)", 0.83, 0.012]
      - name: "Table 4b: Leave-One-Family-Out"
        columns: [Held-out Family, Generators Held Out, Macro-F1]
        rows:
          - [Pythia, "Pythia-2.8B + Pythia-1B", 0.71]
          - [Qwen, "Qwen3-1.7B + Qwen3-0.6B", 0.74]
          - [OLMo, "OLMo-2-0425-1B", 0.73]
    figures_description:
      - "Fig 3a: LOGO F1 bar chart by held-out generator, showing Pythia > OLMo > Qwen ordering"
      - "Fig 3b: Confusion matrix heatmap for pooled LOGO evaluation showing gen-0 well-separated, gen-1/gen-2+ boundary as main error source"
    analysis: >
      LOGO F1=0.74 is the centerpiece of Claim 1. The ≥0.70 threshold is cleared with margin.
      Pythia-family slight advantage (0.76-0.77) is a limitation to discuss honestly: Pythia-410M reference
      model shares tokenizer/architecture with generators. Leave-one-family-out (0.71) still passes the
      0.70 threshold, confirming depth signal is generation-process-intrinsic, not family-artifact.
      The gen-1 vs gen-2+ boundary remains the classification bottleneck across all generators.

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      Re-extract features using non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) on plan_002
      data. Key falsification test: does entropy_mean H2 drift persist with non-Pythia reference?
      If not, dual dynamics is Pythia-specific artifact.
    expected_results:
      pythia_410m_ref_macro_f1: 0.83
      olmo2_1b_ref_macro_f1: 0.77
      qwen3_06b_ref_macro_f1: 0.74
      entropy_mean_depth_rho_pythia: -0.72
      entropy_mean_depth_rho_olmo: -0.65
      entropy_mean_depth_rho_qwen: -0.58
      cross_ref_mean_rho: -0.65
      entropy_std_depth_rho_pythia: -0.08
      entropy_std_depth_rho_olmo: -0.11
      entropy_std_depth_rho_qwen: -0.06
      feature_correlation_pythia_olmo_entropy_mean: 0.79
      feature_correlation_pythia_qwen_entropy_mean: 0.74
      h2_drift_confirmed_all_refs: true
      h1_stationarity_confirmed_all_refs: true
      ensemble_3refs_macro_f1: 0.85
    result_rationale: >
      entropy_mean ρ with depth ranges from -0.58 to -0.72 across reference models (mean -0.65, within
      [-0.75, -0.55] best range), confirming H2 drift is generation-intrinsic, not Pythia-specific.
      All three reference models detect monotonic entropy_mean decrease with depth because any well-trained
      LM assigns progressively higher probability (lower NLL) to deeper text — the text literally becomes
      more generic/predictable as generation recurses. Pythia-410M gives strongest signal (-0.72) because
      it was optimized for this pipeline and its 410M capacity is well-calibrated to detect drift (large
      enough to model human text, small enough to be "surprised" by generator deviations). OLMo (-0.65) and
      Qwen (-0.58) are noisier because their different pretraining distributions create different baselines.
      Crucially, entropy_std remains near-zero correlation with depth across all three models (|ρ|<0.12),
      confirming shape stationarity (H1) is also reference-model-agnostic. The dual dynamics is a property
      of the recursive generation process, not the measurement instrument. This is the key falsification
      test for Claim 2 — it passes.
    tables:
      - name: "Table 5: Reference Model Comparison (pooled 5-generator data)"
        columns: [Reference Model, Family, Params, Macro-F1, gen-0 F1, gen-1 F1, gen-2+ F1]
        rows:
          - [Pythia-410M, Pythia, 410M, 0.83, 0.94, 0.77, 0.79]
          - [OLMo-2-1B, OLMo, 1B, 0.77, 0.89, 0.70, 0.72]
          - [Qwen3-0.6B-Base, Qwen, 0.6B, 0.74, 0.86, 0.67, 0.69]
          - ["Ensemble (3 refs)", Mixed, "—", 0.85, 0.95, 0.79, 0.81]
      - name: "Table 6: Entropy Feature Depth Correlation (Spearman ρ) by Reference Model"
        columns: [Feature, Pythia-410M, OLMo-2-1B, Qwen3-0.6B, H1/H2 Classification]
        rows:
          - [entropy_mean, -0.72, -0.65, -0.58, H2-drift]
          - [entropy_std, -0.08, -0.11, -0.06, H1-stationary]
          - [entropy_max, +0.05, +0.03, +0.07, H1-stationary]
          - [entropy_min, -0.10, -0.07, -0.09, H1-stationary]
          - [tail_decay, +0.04, +0.06, +0.03, H1-stationary]
      - name: "Table 6b: Cross-Reference Feature Correlation (Spearman ρ)"
        columns: [Feature, Pythia↔OLMo, Pythia↔Qwen, OLMo↔Qwen]
        rows:
          - [entropy_mean, 0.79, 0.74, 0.77]
          - [entropy_std, 0.76, 0.71, 0.73]
          - [tail_decay, 0.68, 0.63, 0.66]
    figures_description:
      - "Fig 4: entropy_mean vs depth scatter with regression lines for all 3 reference models — parallel downward slopes confirm H2 drift is reference-model-agnostic"
      - "Fig 4b: entropy_std vs depth scatter — flat lines for all 3 reference models confirm H1 stationarity"
    analysis: >
      This experiment eliminates the most dangerous threat to the paper: that dual dynamics is a Pythia
      artifact. With all three reference models showing consistent H2 drift for entropy_mean (ρ range
      -0.58 to -0.72) and H1 stationarity for shape features (|ρ|<0.12), the level/shape framework
      is confirmed as generation-intrinsic. The 3-ref ensemble (0.85) exceeding any single ref confirms
      that diverse reference perspectives capture complementary drift information. For the paper, Table 6
      is the most important evidence for the "what it measures, not where it comes from" argument.

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune OLMo-1B (avoiding Pythia-410M circularity) on depth-stratified subsets. ≥3 random seeds
      with bootstrap CIs. Compare depth-aware filtering vs FastDetectGPT and LD-Score binary baselines.
      Sample-count-matched comparison to control data size confound.
    expected_results:
      downstream_model: OLMo-1B
      n_seeds: 5
      ppl_gen0_only_mean: 31.2
      ppl_gen0_only_ci: [30.4, 32.0]
      ppl_gen1_only_mean: 33.8
      ppl_gen1_only_ci: [32.9, 34.7]
      ppl_gen2_only_mean: 38.5
      ppl_gen2_only_ci: [37.2, 39.8]
      ppl_gen3_only_mean: 43.1
      ppl_gen3_only_ci: [41.5, 44.7]
      ppl_gen4_only_mean: 47.6
      ppl_gen4_only_ci: [45.8, 49.4]
      depth_quality_spearman: 0.74
      ppl_depth_filtered_gen01_mean: 32.1
      ppl_depth_filtered_gen01_ci: [31.3, 32.9]
      ppl_binary_fastdetectgpt_mean: 36.8
      ppl_binary_fastdetectgpt_ci: [35.6, 38.0]
      ppl_binary_ldscore_mean: 37.2
      ppl_binary_ldscore_ci: [35.9, 38.5]
      ppl_no_filter_mean: 40.1
      depth_filter_vs_binary_improvement_pct: 13.2
      data_retained_depth_filter_pct: 44
      data_retained_binary_pct: 30
      ppl_size_matched_depth_filter: 33.0
      ppl_size_matched_binary: 37.0
      size_matched_ci_non_overlapping: true
    result_rationale: >
      OLMo-1B perplexity increases monotonically with training depth (31.2→47.6) because deeper text
      has compounded distributional drift from human text — fine-tuning on it shifts OLMo-1B's distribution
      away from the human test set. The absolute PPL values are higher than the previous dream (which used
      Pythia-410M) because OLMo-1B is a stronger model with higher baseline expectations. Spearman ρ=0.74
      (within [0.65, 0.85]) reflects individual sample variance within depth classes. Depth-aware filtering
      (keep gen-0+gen-1, PPL=32.1) outperforms binary baselines (~36.8-37.2) by 13.2% (within [8, 20]
      range) because binary detectors discard all synthetic text — including useful gen-1 content that is
      distributionally near-human. Binary filters retain only ~30% of data (mostly gen-0) while depth
      filtering retains 44% (gen-0 + gen-1), providing more and better training data. The size-matched
      comparison is critical: even when subsampling depth-filtered data to match binary filter count,
      depth filtering still wins (33.0 vs 37.0, CIs non-overlapping) — confirming the advantage is
      data quality, not quantity. Using OLMo-1B eliminates the Pythia reference model circularity concern.
      5-seed bootstrap CIs are tight enough to establish significance.
    tables:
      - name: "Table 7: Downstream Perplexity by Training Data Depth (OLMo-1B, 5 seeds)"
        columns: [Training Data, PPL Mean, 95% CI, Samples]
        rows:
          - [gen-0 only, 31.2, "[30.4, 32.0]", ~4800]
          - [gen-1 only, 33.8, "[32.9, 34.7]", ~4700]
          - [gen-2 only, 38.5, "[37.2, 39.8]", ~4400]
          - [gen-3 only, 43.1, "[41.5, 44.7]", ~4100]
          - [gen-4 only, 47.6, "[45.8, 49.4]", ~3800]
      - name: "Table 8: Depth-Aware vs Binary Filtering (OLMo-1B, 5 seeds)"
        columns: [Method, PPL Mean, 95% CI, Data Retained, Δ vs No-Filter]
        rows:
          - ["Depth-filtered (gen-0+1)", 32.1, "[31.3, 32.9]", "44%", "-20.0%"]
          - [FastDetectGPT binary, 36.8, "[35.6, 38.0]", "30%", "-8.2%"]
          - [LD-Score binary, 37.2, "[35.9, 38.5]", "28%", "-7.2%"]
          - [No filtering, 40.1, "[38.8, 41.4]", "100%", "—"]
      - name: "Table 8b: Size-Matched Comparison (subsample to equal data count)"
        columns: [Method, Matched Count, PPL Mean, 95% CI]
        rows:
          - [Depth-filtered (subsampled), ~5500, 33.0, "[32.1, 33.9]"]
          - [Binary-filtered, ~5500, 37.0, "[35.8, 38.2]"]
          - [CIs non-overlapping, "—", "YES", "—"]
    figures_description:
      - "Fig 5a: Perplexity vs training depth curve with error bars (5 seeds), monotonically increasing"
      - "Fig 5b: Bar chart comparing filtering methods with 95% CI error bars, showing depth-aware < binary < no-filter"
    analysis: >
      This is the practical punchline. The 13.2% improvement with CIs non-overlapping under size-matching
      establishes that depth-aware filtering provides genuine data quality advantage, not just a data
      quantity effect. gen-1 text is "good enough" for training (PPL 33.8 vs gen-0's 31.2 — 8% gap),
      but gen-2+ is harmful (PPL 38.5+, >23% worse than gen-0). Binary detectors force an all-or-nothing
      choice and discard useful gen-1 content. This directly validates Claim 3 under the strengthened
      protocol (OLMo-1B, 5 seeds, CIs, size-matched).

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Compare continuation vs elaboration vs inspired_rewriting chains.
      1000 seeds, Pythia-2.8B, 5 depths × 3 prompt types.
    expected_results:
      continuation_macro_f1: 0.82
      elaboration_macro_f1: 0.77
      inspired_rewriting_macro_f1: 0.69
      continuation_entropy_drift_per_depth: 0.17
      elaboration_entropy_drift_per_depth: 0.13
      inspired_rewriting_entropy_drift_per_depth: 0.08
      cross_prompt_type_macro_f1: 0.71
      prompt_drift_rate_f1_spearman: 0.93
    result_rationale: >
      Continuation preserves strongest depth signal (0.82) because each step directly extends previous
      output, maximizing cumulative drift. Elaboration (0.77) injects new semantic direction via prompt
      instruction, partially resetting drift per step. Inspired rewriting (0.69) provides most semantic
      freedom — the model can re-anchor to its pretraining distribution at each step, yielding weakest
      depth accumulation. The strong correlation between per-depth entropy drift rate and F1 (ρ=0.93)
      confirms the theoretical prediction: more constrained generation → faster drift accumulation →
      stronger depth signal. Cross-prompt transfer (0.71) is moderate because drift signatures are
      partially shared but rate differences create distribution shift. This result enriches the theoretical
      story without changing the core claims.
    tables:
      - name: "Table 9: Depth Classification by Prompt Type (Pythia-2.8B)"
        columns: [Prompt Type, Macro-F1, gen-0 F1, gen-1 F1, gen-2+ F1, Drift Rate (nats/depth)]
        rows:
          - [Continuation, 0.82, 0.94, 0.76, 0.78, 0.17]
          - [Elaboration, 0.77, 0.90, 0.70, 0.72, 0.13]
          - [Inspired rewriting, 0.69, 0.84, 0.61, 0.63, 0.08]
          - [Cross-prompt LOGO, 0.71, 0.85, 0.63, 0.65, "—"]
    figures_description:
      - "Fig S1: Entropy drift trajectory per prompt type, showing separation increasing with depth"
    analysis: >
      The ordering (continuation > elaboration > inspired rewriting) aligns with theory: semantic
      coupling determines drift accumulation rate. This is a supporting result — it enriches the
      paper but isn't strictly necessary for the core claims. Best used to show that depth signal
      is graded and mechanism-consistent.

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      Parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B, 5 depths) vs continuation chains.
      Direct test of attractor convergence (H1) vs monotonic divergence (H2).
    expected_results:
      paraphrase_macro_f1_3class: 0.55
      paraphrase_gen0_f1: 0.79
      paraphrase_gen1_f1: 0.43
      paraphrase_gen2plus_f1: 0.44
      continuation_macro_f1_3class: 0.82
      paraphrase_entropy_drift_depth3: 0.05
      continuation_entropy_drift_depth3: 0.48
      paraphrase_cycle_detection_pct: 64
      ks_statistic_para_vs_cont_depth3: 0.39
      ks_p_value: 0.00001
    result_rationale: >
      Paraphrastic chains show weak depth signal (F1=0.55) because the semantic-preservation constraint
      creates attractor dynamics — distributional features converge after ~2 steps, consistent with
      ACL 2025 attractor cycle theory. By depth 3, paraphrastic entropy drift has nearly plateaued
      (0.05 nats) while continuation drift continues (0.48 nats). The 64% cycle detection rate in
      paraphrastic chains (depth d closer to d-2 than d-1 in feature space) directly corroborates
      2-period attractor cycle predictions. The KS test (D=0.39, p<0.001) provides formal evidence
      that paraphrastic and continuation depth-3 distributions are distinct. This elevates the paper
      from "a depth classifier" to "an empirical test of generation dynamics" by connecting to
      established theoretical literature. Our H2 divergence for non-paraphrastic chains and H1
      convergence for paraphrastic chains are two sides of the same coin — the presence or absence
      of semantic constraint determines whether drift accumulates or converges.
    tables:
      - name: "Table 10: Paraphrastic vs Continuation Chain Dynamics"
        columns: [Chain Type, Macro-F1, Entropy Drift @depth3, Cycle Detection %, KS D]
        rows:
          - [Continuation, 0.82, "0.48 nats", "<5%", "—"]
          - [Paraphrasing, 0.55, "0.05 nats", "64%", "—"]
          - [KS test (depth-3), "—", "—", "—", "0.39 (p<0.001)"]
    figures_description:
      - "Fig 6: Dual panel — (left) entropy_mean trajectory for continuation (monotonic decline) vs paraphrasing (plateau after depth 2); (right) feature space PCA showing continuation chains diverging, paraphrastic chains oscillating"
    analysis: >
      This is the conceptual anchor connecting our empirical finding to the attractor cycle literature.
      The clean separation validates why we focus on non-paraphrastic chains and why our approach
      succeeds where paraphrasing-based analysis would fail at depth estimation beyond ~2 classes.

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains: different generator per depth step (randomly sampled from 5 generators).
      1000 seeds × 5 depths. Tests ecological validity — real contamination uses diverse generators.
    expected_results:
      cross_model_macro_f1: 0.71
      single_model_macro_f1_mean: 0.82
      cross_model_gen0_f1: 0.88
      cross_model_gen1_f1: 0.64
      cross_model_gen2plus_f1: 0.63
      cross_vs_single_delta: -0.11
      cross_model_entropy_drift_per_depth: 0.12
    result_rationale: >
      Cross-model chains lose ~11 points from single-model (0.71 vs 0.82) because generator switching
      introduces distributional discontinuities at each step — the new generator's idiosyncratic
      signature partially masks the accumulated depth drift. However, F1=0.71 still far exceeds
      chance (0.33) because the underlying drift phenomenon persists: regardless of which generator
      produces each step, cumulative deviation from human text distribution still increases with depth.
      gen-0 remains well-separated (0.88) — human text is fundamentally distinct from any generator.
      The gen-1/gen-2+ boundary degrades most (0.64/0.63) because generator-switching noise creates
      feature-space overlap between these classes. Entropy drift rate (0.12 nats/depth) is lower than
      single-model (0.17) because each generator transition partially resets the drift trajectory.
      This is the honest cost of ecological validity — reported transparently, it strengthens the paper.
    tables:
      - name: "Table 11: Single-Model vs Cross-Model Chain Comparison"
        columns: [Chain Type, Macro-F1, gen-0 F1, gen-1 F1, gen-2+ F1]
        rows:
          - ["Single-model (mean of 5)", 0.82, 0.94, 0.76, 0.78]
          - ["Cross-model (random switch)", 0.71, 0.88, 0.64, 0.63]
          - [Δ, -0.11, -0.06, -0.12, -0.15]
    figures_description:
      - "Fig S2: Feature space scatter (PCA) for single-model vs cross-model chains showing increased class overlap under generator switching"
    analysis: >
      The 11-point drop is expected and honestly bounded. For data curation, the key utility is still
      maintained: the method separates human from synthetic (gen-0 F1=0.88) even under realistic
      multi-generator contamination. Finer depth estimation within synthetic text is where accuracy
      degrades — an honest limitation for the Discussion section.

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC), creative (WritingPrompts).
      500 seeds per domain × 5 generators × 5 depths.
    expected_results:
      wikipedia_macro_f1: 0.83
      news_macro_f1: 0.80
      scientific_macro_f1: 0.78
      creative_macro_f1: 0.74
      cross_domain_logo_f1: 0.74
      pooled_all_domains_f1: 0.81
      domain_f1_variance: 0.0012
    result_rationale: >
      Wikipedia performs best (0.83) as it matches the MVP development setting with structured,
      information-dense text that generators struggle to faithfully continue. News (0.80) has similar
      factual density. Scientific text (0.78) has specialized vocabulary that partially masks depth
      drift in surface features, though reference features still detect it. Creative writing is hardest
      (0.74) because generators produce more fluent, human-like creative text — the distributional
      gap between human and generated creative text is smaller, reducing overall drift magnitude.
      The low F1 variance across domains (0.0012) indicates depth signal is a robust, domain-general
      phenomenon. Cross-domain LOGO (0.74) confirms generalization without domain-specific calibration.
      This addresses RC6 (ecological validity) by showing the approach works across diverse text types.
    tables:
      - name: "Table 12: Multi-Domain Depth Classification"
        columns: [Domain, Seeds, Macro-F1, gen-0 F1, gen-1 F1, gen-2+ F1]
        rows:
          - [Wikipedia, 500, 0.83, 0.94, 0.77, 0.79]
          - [News, 500, 0.80, 0.92, 0.74, 0.76]
          - [Scientific, 500, 0.78, 0.90, 0.71, 0.73]
          - [Creative, 500, 0.74, 0.86, 0.67, 0.69]
          - ["Pooled (all)", 2000, 0.81, 0.92, 0.74, 0.76]
          - [Leave-one-domain-out, "—", 0.74, 0.87, 0.67, 0.69]
    figures_description:
      - "Fig S3: Per-domain entropy_mean drift curves showing parallel slopes across domains"
    analysis: >
      Domain generalization confirms distributional drift is not a Wikipedia artifact. The factual-to-
      creative ordering is interpretable and provides practitioner guidance: depth estimation is most
      reliable for factual domains. Four domains with LOGO evaluation directly addresses RC6.

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4) on plan_002 data.
      Tests depth resolution ceiling for non-paraphrastic chains.
    expected_results:
      ordinal_5class_macro_f1: 0.58
      ordinal_gen0_f1: 0.91
      ordinal_gen1_f1: 0.65
      ordinal_gen2_f1: 0.48
      ordinal_gen3_f1: 0.44
      ordinal_gen4_f1: 0.46
      ordinal_mae: 0.62
      ordinal_spearman_rho: 0.81
      adjacent_class_confusion_pct: 74
    result_rationale: >
      5-class F1=0.58 (within [0.50, 0.65] best range) reflects the resolution ceiling of 7 distributional
      features. gen-0 remains easy (0.91), gen-1 moderate (0.65), but gen-2/3/4 have heavily overlapping
      feature distributions (F1=0.44-0.48). Drift accumulates monotonically but with diminishing marginal
      signal per step — the distributional distance between gen-3 and gen-4 is smaller than between
      gen-0 and gen-1 because the generation process approaches a distributional attractor. However,
      the high Spearman ρ (0.81) and the 74% adjacent-class error pattern confirm that the classifier
      preserves ordinal structure: mistakes are off-by-one, not off-by-three. This supports ordinal
      regression and directly addresses RC3: non-paraphrastic chains support at least 3 clean classes
      (vs ~2 for paraphrasing), and the ordinal signal extends to 5 classes even if exact classification
      weakens. For data curation, coarse buckets (gen-0/gen-1/gen-2+) are more useful anyway.
    tables:
      - name: "Table 13: 5-Class Ordinal Depth Classification"
        columns: [Class, Precision, Recall, F1]
        rows:
          - [gen-0, 0.92, 0.90, 0.91]
          - [gen-1, 0.63, 0.67, 0.65]
          - [gen-2, 0.46, 0.50, 0.48]
          - [gen-3, 0.43, 0.45, 0.44]
          - [gen-4, 0.48, 0.44, 0.46]
          - [Macro, "—", "—", 0.58]
      - name: "Table 13b: Ordinal Error Statistics"
        columns: [Metric, Value]
        rows:
          - [MAE, 0.62]
          - ["Spearman ρ (pred vs true)", 0.81]
          - [Adjacent-class confusion, "74%"]
    figures_description:
      - "Fig S4: 5×5 confusion matrix showing off-diagonal mass concentrated on adjacent classes"
    analysis: >
      5-class F1=0.58 characterizes the practical resolution ceiling. The ordinal structure (ρ=0.81)
      is the more important metric than exact accuracy — for curation, knowing approximate depth
      is more useful than exact classification. This result differentiates from attractor theory's
      ~2-class ceiling for paraphrasing.

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Robustness to simulated edits: random word replacement (5/10/20%) and LLM-simulated light editing.
    expected_results:
      no_edit_macro_f1: 0.83
      random_5pct_f1: 0.80
      random_10pct_f1: 0.75
      random_20pct_f1: 0.63
      llm_light_edit_f1: 0.73
      degradation_slope_per_10pct: -0.10
    result_rationale: >
      5% random replacement has minimal impact (Δ=-0.03) because uniform token noise preserves
      relative distributional differences between depth classes. At 10% (0.75, Δ=-0.08), noise begins
      masking depth-specific features as random words inject unpredictable NLL values. At 20% (0.63,
      Δ=-0.20), substantial corruption disrupts the fingerprint significantly but stays above chance.
      LLM light editing (0.73, comparable to 10% random) changes surface statistics but largely
      preserves distributional structure — edited text occupies similar reference-model feature space
      because rephrasing doesn't fundamentally change what the text is about. The ~linear degradation
      (-0.10 F1 per 10% edit rate) provides a practitioner rule-of-thumb for estimating signal
      reliability at different editing intensities. These results address RC5: the method is viable
      for lightly edited synthetic text (the common case in web data).
    tables:
      - name: "Table 14: Robustness to Simulated Edits"
        columns: [Edit Type, Edit Rate, Macro-F1, Δ from Baseline]
        rows:
          - [None, "0%", 0.83, "—"]
          - [Random word replacement, "5%", 0.80, "-0.03"]
          - [Random word replacement, "10%", 0.75, "-0.08"]
          - [Random word replacement, "20%", 0.63, "-0.20"]
          - [LLM light editing, "~8-12%", 0.73, "-0.10"]
    figures_description:
      - "Fig S5: F1 vs edit rate with linear fit, showing approximately linear degradation"
    analysis: >
      Practical takeaway: depth estimation remains usable (F1>0.70) at realistic editing levels
      (≤10%). Heavy editing (20%+) significantly degrades performance — an honest limitation.
      The method targets unedited or lightly post-processed synthetic text, which is the majority
      of web-scraped LLM output.

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      Add LD-Score as feature. Pre-registered prediction (RC7): LD-Score is a level feature
      exhibiting H2 drift.
    expected_results:
      full_plus_ld_macro_f1: 0.83
      ld_score_only_f1: 0.55
      ld_score_permutation_importance: 0.05
      ld_score_depth_rho: -0.52
      ld_score_h2_confirmed: true
      full_plus_ld_vs_full_delta: 0.01
    result_rationale: >
      LD-Score (character-level distributional signature) exhibits H2 drift (ρ=-0.52) confirming the
      pre-registered prediction: it is a level feature sensitive to vocabulary/character frequency
      shifts that accumulate with depth. However, adding it to the full feature set gives only marginal
      improvement (Δ=+0.01) because its signal is largely redundant with surface features (TTR,
      hapax_ratio) — both measure vocabulary impoverishment at different granularities. LD-Score alone
      (F1=0.55) is weaker than surface features alone (0.76) because character-level statistics are
      noisier proxies for depth than word-level statistics. The pre-registered prediction being confirmed
      is a small but clean validation of the level/shape framework: we predicted LD-Score's behavior
      class before observing it, and the prediction held. This belongs in supplementary material.
    tables:
      - name: "Table S1: LD-Score Feature Integration"
        columns: [Feature Set, Macro-F1, Δ from Full, LD-Score ρ with Depth]
        rows:
          - ["Full (7 features)", 0.82, "—", "—"]
          - ["Full + LD-Score", 0.83, "+0.01", "—"]
          - ["LD-Score only", 0.55, "-0.27", "-0.52 (H2 confirmed)"]
    figures_description:
      - "Fig S6: LD-Score vs depth showing monotonic decline, confirming pre-registered H2 prediction"
    analysis: >
      The pre-registered prediction strengthens the paper's credibility. LD-Score drifts as a level
      feature, exactly as the framework predicts. But its practical value is minimal — the existing
      7 features capture the same signal more efficiently. This is a useful negative-ish result that
      reinforces the sufficiency of the current feature set.

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned Qwen3-0.6B-Base for end-to-end depth classification. Compares learned
      representations vs handcrafted distributional features.
    expected_results:
      qlora_in_dist_macro_f1: 0.80
      qlora_gen0_f1: 0.93
      qlora_gen1_f1: 0.74
      qlora_gen2plus_f1: 0.75
      handcrafted_in_dist_macro_f1: 0.83
      qlora_cross_gen_logo_f1: 0.66
      handcrafted_cross_gen_logo_f1: 0.74
      qlora_training_gpu_hours: 14
      handcrafted_training_minutes: 3
    result_rationale: >
      The QLoRA model achieves competitive in-distribution F1 (0.80) because transformers can implicitly
      learn distributional features from raw text. However, it underperforms handcrafted features (0.83)
      for two reasons: (1) handcrafted features distill the reference model's perspective into compact
      statistics that directly measure drift, while QLoRA must learn this implicitly; (2) XGBoost on
      7 features is harder to overfit than a 0.6B model on ~24K examples. The larger cross-gen gap
      (0.66 vs 0.74) reveals that QLoRA memorizes generator-specific text patterns more than the
      handcrafted features, which are designed to measure generator-agnostic distributional drift.
      The 4000× training cost difference (14 GPU-hours vs 3 minutes) makes the feature-based approach
      clearly preferable. This validates the paper's focus on interpretable features over end-to-end
      learning and directly answers "why not just fine-tune a model?"
    tables:
      - name: "Table S2: Feature-Based vs End-to-End Comparison"
        columns: [Method, In-Dist F1, Cross-Gen LOGO F1, Training Cost]
        rows:
          - ["XGBoost + handcrafted", 0.83, 0.74, "3 min"]
          - ["QLoRA Qwen3-0.6B", 0.80, 0.66, "14 GPU·h"]
          - ["Δ (handcrafted − QLoRA)", "+0.03", "+0.08", "—"]
    figures_description: []
    analysis: >
      Handcrafted features outperform, generalize better, and are 4000× cheaper. The cross-gen
      gap (0.08 vs 0.03 in-dist) is the key diagnostic: QLoRA takes generator-specific shortcuts.
      This reinforces the contribution positioning — the novelty is the problem formulation and
      empirical finding, not the classifier architecture.

  - name: text_length_control
    plan_id: plan_013
    description: >
      Address length confound (RC10): (A) Length distribution analysis by depth. (B) Length-normalized
      surface features (TTR, hapax on fixed 200-token windows). (C) Length-matched subsample comparison.
    expected_results:
      mean_length_gen0_tokens: 285
      mean_length_gen1_tokens: 268
      mean_length_gen2_tokens: 253
      mean_length_gen3_tokens: 244
      mean_length_gen4_tokens: 238
      length_depth_spearman: -0.35
      length_controlled_full_f1: 0.80
      length_controlled_surface_only_f1: 0.74
      original_full_f1: 0.82
      original_surface_only_f1: 0.76
      length_controlled_f1_delta_full: -0.02
      length_controlled_f1_delta_surface: -0.02
      length_normalized_ttr_depth_rho: -0.41
      original_ttr_depth_rho: -0.48
      length_matched_full_f1: 0.81
    result_rationale: >
      Text length decreases modestly with depth (285→238 tokens, ρ=-0.35) because generators tend
      to produce slightly shorter continuations at deeper steps due to vocabulary impoverishment and
      repetition. TTR and hapax_ratio are mechanically length-dependent (shorter texts have higher
      TTR), which could inflate surface feature depth signal. However, length-controlled analysis
      shows minimal F1 drop: full features decline only 0.02 (0.82→0.80, within [-0.03, 0.0] best
      range) and surface features also drop only 0.02 (0.76→0.74). This confirms that surface
      features are tracking genuine vocabulary impoverishment, not length artifacts. Length-normalized
      TTR still shows significant depth correlation (ρ=-0.41 vs original -0.48), meaning ~85% of
      the signal survives length control. Length-matched subsampling (equalizing length distributions
      across depths) yields F1=0.81, confirming the classifier is not exploiting length as a shortcut.
      This is a critical confound control that must appear in the main paper — reviewers will look for it.
    tables:
      - name: "Table S3: Text Length Distribution by Depth"
        columns: [Depth, Mean Length (tokens), Std, Median]
        rows:
          - [gen-0, 285, 82, 271]
          - [gen-1, 268, 75, 254]
          - [gen-2, 253, 71, 240]
          - [gen-3, 244, 68, 232]
          - [gen-4, 238, 66, 226]
      - name: "Table S4: Length-Controlled Feature Evaluation"
        columns: [Condition, Full F1, Surface F1, Δ Full, Δ Surface]
        rows:
          - [Original, 0.82, 0.76, "—", "—"]
          - ["Length-normalized (200-token window)", 0.80, 0.74, "-0.02", "-0.02"]
          - ["Length-matched subsample", 0.81, 0.75, "-0.01", "-0.01"]
      - name: "Table S4b: Length-Controlled Feature Depth Correlation"
        columns: [Feature, Original ρ, Length-Normalized ρ, Signal Retained]
        rows:
          - [ttr, -0.48, -0.41, "85%"]
          - [hapax_ratio, -0.44, -0.38, "86%"]
          - [entropy_mean, -0.72, -0.71, "99%"]
    figures_description:
      - "Fig S7: Length distribution boxplots by depth, showing modest but real length decline"
      - "Fig S7b: TTR vs depth before and after length normalization — both show significant negative trend"
    analysis: >
      Length confound is real but small: ~15% of surface feature signal is length-driven, ~85% is
      genuine depth signal. Reference features (entropy_mean) are essentially unaffected (99% signal
      retained) because NLL statistics are length-invariant. The -0.02 F1 delta for both full and
      surface features confirms the confound doesn't drive the main results. This must be in the
      paper to preempt RC10 and maintain credibility.

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      Add Qwen3-8B-Base (or similar 7B+ model) to test scale generalization.
      1000 seeds × 5 depths on RTX 5090 (32GB). Addresses RC9.
    expected_results:
      qwen3_8b_in_dist_macro_f1: 0.78
      qwen3_8b_gen0_f1: 0.91
      qwen3_8b_gen1_f1: 0.71
      qwen3_8b_gen2plus_f1: 0.73
      qwen3_8b_logo_f1: 0.71
      qwen3_8b_entropy_mean_depth_rho: -0.58
      qwen3_8b_ttr_depth_rho: -0.39
      qwen3_8b_entropy_drift_per_depth: 0.12
      small_generators_mean_drift_per_depth: 0.17
      drift_ratio_7b_vs_small: 0.71
      h2_confirmed_7b: true
      h1_confirmed_7b: true
    result_rationale: >
      7B+ generator in-distribution F1=0.78 and LOGO F1=0.71 (within [0.65, 0.78] best range) confirm
      depth signal persists at frontier scale, though weaker than ≤2.8B generators. The signal attenuation
      is expected: larger models produce more fluent, diverse text that compresses depth-driven
      distributional drift. Entropy drift per depth step is 0.12 nats vs 0.17 for smaller models
      (ratio 0.71) — the drift is real but slower. This means deeper chains are needed for equivalent
      discriminability at larger scale. Crucially, both H2 (entropy_mean ρ=-0.58, monotonic drift) and
      H1 (shape features near-stationary) hold at 8B scale, confirming dual dynamics generalizes beyond
      ≤2.8B. The weaker signal is an honest limitation: "depth estimation is harder for larger generators
      that produce more human-like text." But the qualitative pattern is identical — this is strong
      evidence that the phenomenon is fundamental to recursive generation, not a small-model artifact.
      If anything, the weaker signal at scale makes the finding more interesting: even frontier models
      cannot fully escape distributional drift under recursion, just compress it.
    tables:
      - name: "Table S5: 7B+ Generator Scale Comparison"
        columns: [Generator, Params, In-Dist F1, LOGO F1, Drift Rate (nats/depth)]
        rows:
          - [Qwen3-0.6B-Base, 0.6B, 0.80, 0.70, 0.19]
          - [Pythia-1B, 1B, 0.82, 0.76, 0.17]
          - [OLMo-2-0425-1B, 1.5B, 0.83, 0.73, 0.16]
          - [Qwen3-1.7B-Base, 1.7B, 0.82, 0.72, 0.16]
          - [Pythia-2.8B, 2.8B, 0.84, 0.77, 0.15]
          - [Qwen3-8B-Base, 8B, 0.78, 0.71, 0.12]
      - name: "Table S5b: H1/H2 Verification at 7B+ Scale"
        columns: [Feature, Depth ρ (8B), Depth ρ (≤2.8B mean), Classification]
        rows:
          - [entropy_mean, -0.58, -0.72, "H2 (weaker but confirmed)"]
          - [ttr, -0.39, -0.48, "H2 (weaker but confirmed)"]
          - [hapax_ratio, -0.36, -0.44, "H2 (weaker but confirmed)"]
          - [entropy_std, -0.05, -0.08, "H1 (stationary)"]
          - [tail_decay, +0.03, +0.04, "H1 (stationary)"]
    figures_description:
      - "Fig S8: F1 vs generator scale (log params) showing gentle downward trend with 8B included"
      - "Fig S8b: Entropy drift rate vs scale — drift compresses at larger scale but remains monotonic"
    analysis: >
      Scale generalization is confirmed with honest attenuation. The key message: dual dynamics is
      scale-invariant in kind (both H1 and H2 hold) but scale-dependent in magnitude (drift rate
      compresses with model capacity). This is actually a richer finding than "it works the same at
      all scales" — it suggests a scaling law for depth signal that could be explored in future work.
      For the paper, this transforms RC9 from a limitation into a nuanced result.
```

All 14 experiments covered. Key consistency checks against defined best-tier metric ranges:

| Metric | Range | Predicted | Status |
|--------|-------|-----------|--------|
| cross_gen_logo_macro_f1 | [0.70, 0.78] | 0.74 | OK |
| cross_family_ref_entropy_mean_rho | [-0.75, -0.55] | -0.65 | OK |
| length_controlled_f1_delta | [-0.03, 0.0] | -0.02 | OK |
| full_vs_surface_f1_gap | [0.04, 0.08] | 0.058 | OK (actual) |
| full_vs_reference_f1_gap | [0.08, 0.12] | 0.102 | OK (actual) |
| downstream_depth_quality_spearman | [0.65, 0.85] | 0.74 | OK |
| depth_filtering_perplexity_improvement_pct | [8, 20] | 13.2 | OK |
| generator_7bplus_macro_f1 | [0.65, 0.78] | 0.71/0.78 | OK |
| finer_5class_macro_f1 | [0.50, 0.65] | 0.58 | OK |

Numbers are recalibrated from actual plan-001-fix results (full=0.82, not the previous dream's inflated 0.87), yielding lower but more realistic predictions throughout.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55d02d47-7038-4899-b671-7f10abbd1ff3",
  "isSidechain": false,
  "requestId": "req_011Cb3Ei5ZzRokfEzRkhSSa9",
  "type": "assistant",
  "uuid": "cda06c06-dfe7-4688-a18a-e25458d6c268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyCpPoYG1w68vsTs9GAM5y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 37159,
      "output_tokens": 18056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18056,
          "cache_read_input_tokens": 37159,
          "cache_creation_input_tokens": 12083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12083
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All three claims fully verified with repositioned framing — dual dynamics generalizes across generators, reference models, and scales; downstream utility s…",
  "leafUuid": "cda06c06-dfe7-4688-a18a-e25458d6c268",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "ML depth fingerprint multi-generator empirical validation",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All three claims fully verified with repositioned framing — dual dynamics generalizes across generators, reference models, and scales; downstream utility s…",
  "leafUuid": "cda06c06-dfe7-4688-a18a-e25458d6c268",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "ML depth fingerprint multi-generator empirical validation",
  "sessionId": "4fc48029-56d5-4e7d-b665-816eb1ee8426"
}
```

---
