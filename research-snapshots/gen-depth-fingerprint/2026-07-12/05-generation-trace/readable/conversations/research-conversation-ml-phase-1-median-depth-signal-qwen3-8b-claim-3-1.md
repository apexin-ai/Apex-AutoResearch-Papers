# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：部分新家族 depth signal 退化（类似 Qwen3-8B 模式），泛化 claim 需收窄但核心贡献不变 核心假设：['3 个新家族中 1

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/90143ee6-16f1-4985-88d2-ed06c2b2634a.jsonl`
- **Structured JSON:** [`e8b2c24d621edbe02cac.json`](../../sessions/e8/e8b2c24d621edbe02cac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T11:04:29.679Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T11:04:29.679Z",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：部分新家族 depth signal 退化（类似 Qwen3-8B 模式），泛化 claim 需收窄但核心贡献不变\n核心假设：['3 个新家族中 1-2 个 held-out F1 < 0.60（类似 instruct 退化但不至于 chance level）', '扩展后 LOGO binary F1 下降至 0.68-0.71 区间（被低性能 generator 拉低）', '7-feature vs best baseline 优势缩窄至 +1.0-2.5pp（仍显著但 effect size 小）', 'differential response 在多数但非全部家族成立（个别家族 shape feature 也出现 drift）', '某些家族的 cross-scale/cross-architecture gap 比预期更大']\n关键指标范围：{'binary_logo_f1_expanded': [0.68, 0.72], 'per_gen_f1_std': [0.07, 0.11], 'worst_single_gen_f1': [0.5, 0.62], 'seven_feat_vs_best_baseline_pp': [1.0, 2.5], 'new_family_avg_held_out_f1': [0.55, 0.68], 'drifting_feature_spearman_range': [-0.55, -0.2], 'shape_feature_spearman_range': [-0.2, 0.2]}\n叙事方向：需要调整 claims 强度。Claim 1 从 \"generalizes across model families\" 收窄为  \"robust within tested base-model regime (≤8B), with architecture-dependent transfer gap  as honest limitation\"。Claim 2 补充 caveat：differential response 是 dominant pattern  但非 universal（某些架构 shape features 也漂移）。增加 \"conditions under which depth  signal degrades\" 的系统分析作为额外贡献。Paper 仍以 novel task + empirical  characterization 为主线，但 universality claim 变为 qualified generalization。 可能需要 Table 明确标注哪些 generators 属于 \"high-signal\" vs \"low-signal\" regime。 EMNLP 投稿强度：borderline accept，需要 rebuttal 说服 1-2 个 reviewer。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR (deadline: May 25, 2026)** — D012\n- Fallback: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response**: **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **distributional shape features** (entropy_std, tail_decay) remain near-stationary. This differential response is consistent with recursive generation inducing a **location shift** in the NLL distribution — the text becomes progressively more predictable (mean shifts) while the functional form of the distribution is preserved (shape is invariant). The genuine novelty is not the drift/stationarity split per se (which follows from location-shift properties), but: (a) the **task formulation** (ordinal depth estimation beyond binary detection), (b) **empirical validation** across 6 generators / 3 model families (including 7B+ scale) showing this pattern is robust, (c) the practical consequence that combining both feature types yields **complementary signal** for depth classification. **Primary metric (D017)**: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, excluding gen-0 due to shared-seed leakage). 3-class LOGO F1 = 0.789 reported as supplementary with gen-0 caveat. Per-generator held-out F1: 0.68–0.86 (std=0.058). Key finding: in binary evaluation (no gen-0 leakage), 7-feature (0.723) > 4-baseline ensemble (0.712) — baseline advantage in 3-class was entirely from gen-0 classification. Depth signal is scale-invariant as a phenomenon, though cross-scale classifier transfer shows a moderate gap (8B held-out F1=0.69 vs ≤2.8B 0.76-0.85).\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth with F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation). Primary metric: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, gen-0 excluded due to shared-seed overlap). 3-class (gen-0/gen-1/gen-2+) LOGO F1 = 0.789 supplementary with caveat.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Depth-dependent features exhibit differential response: central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (consistent with location shift in NLL distribution), while shape features (entropy_std, tail_decay) remain near-stationary. In binary eval, 7-feature ensemble (0.723) outperforms 4-baseline detector ensemble (0.712) by +1.1pp and all individual detectors (+1.1–19.9pp). The 4-baseline advantage in 3-class (0.796 vs 0.789) is entirely from gen-0 classification. Ordinal-specific methods (CORAL 0.771, Frank-Hall 0.793) do not outperform XGBoost (0.789) — CI overlap at 3-class granularity.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality compared to random subsampling. At equal data count, size_matched (random control, ppl=2.367) outperforms depth01 (depth-stratified, 2.387) and binary_filtered (2.389). The primary determinant is data quantity, not depth composition (all 12K samples → ppl=2.335). Depth fingerprinting is an effective **diagnostic** tool for characterizing provenance, but not a **curative** tool for data curation. This honest negative finding is reported transparently.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation. When repurposed as ordinal depth predictors, single detector scores (Avg-LogProb 0.737, LD-Score 0.655, FastDetectGPT 0.688, Binoculars 0.417 under 6-gen LOGO) show moderate signal but **high per-generator F1 variance** (e.g., AvgLogProb range 0.615–0.805, 19.0pp span), making them unreliable as standalone depth estimators.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **differential depth response**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth, while distributional shape features (entropy variance, tail decay) remain near-stationary. This split is about **what the feature measures** (central tendency vs shape), not where it comes from. The combination of drifting and stationary features yields a 7-feature ensemble that **significantly and consistently** outperforms all single-detector baselines: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, p<0.001 vs Avg-LogProb 0.712, LD-Score 0.701, FastDetectGPT 0.616, Binoculars 0.524). In the leak-free binary evaluation, 7-feature (0.723) > 4-baseline ensemble (0.712), reversing the 3-class result where baseline advantage came entirely from gen-0 classification. The practical advantage is **reliability across unknown generators** — per-generator F1 std = 0.058 for our ensemble vs higher variance for individual detectors.\n\n**Headline result template**: \"On non-paraphrastic continuation chains across 6 base-model generators from 3 model families (0.6B–8.2B), our 7-feature distributional ensemble achieves binary LOGO F1 of 0.72 for leak-free depth discrimination (gen-1 vs gen-2+), outperforming all individual detection baselines. Per-generator held-out F1 ranges from 0.68 to 0.86 (std=0.051). Depth-aware data curation does not outperform random subsampling for downstream CLM quality, establishing depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.73 macro-F1, but full 7-feature ensemble achieves 0.789 3-class / 0.723 binary (p<0.001). We don't claim reference features are \"better\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). Note: \"fingerprint\" in the paper refers to the full feature vector's combination, not just reference-model features.\n\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\n\n**RC9 — \"Only ≤2.8B generators — does this transfer to frontier scale?\"**: **Answered (plan-014, D011).** Qwen3-8B (7.6B params) added as 6th generator. Depth signal IS present at 8B scale — all feature-depth Spearman correlations significant. Cross-scale transfer gap: 8B held-out F1=0.69 vs ≤2.8B 0.76-0.85. P0-B volume-matched control: adding Qwen3-8B's +1.1pp improvement is 94% from generator diversity, not data volume. **Paper framing**: depth signal universality supported; cross-scale gap is honest limitation; scope narrowed to base models (see N3/N4 fixes).\n\n**RC10 — \"Text length confound\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\n\n**RC11 — \"Downstream utility — single run, no CIs\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\n\n## Contribution Positioning (D006+D007)\nThe contribution is **primarily empirical and conceptual**, not methodological:\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection (genuinely novel — no prior work)\n2. **Empirical characterization**: Differential depth response across 6 generators / 3 families (including 7B+ scale), with robust cross-generator generalization (binary LOGO F1=0.723, 3-class LOGO F1=0.789). Scale-invariant phenomenon with honest cross-scale transfer gap.\n3. **Negative finding**: Depth-aware data curation does NOT improve downstream CLM quality — depth fingerprinting is diagnostic, not curative (D009).\n\n**Framing discipline (D007 — re-dream consensus):**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution (means shift under distributional drift, shapes don't). Acknowledge this explicitly.\n- Do NOT use H1/H2 terminology (overloads time-series unit-root convention). Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics\" as a novel theoretical framework. Use \"differential depth response\" — more calibrated.\n- Consider renaming \"distributional fingerprinting\" → \"distributional depth profiling\" (fingerprinting implies source identification, creates confusion with LLM attribution literature).\n- Provide at least a speculative theoretical motivation for WHY shape features remain stationary (e.g., \"shape is determined by sampling mechanism and architecture, invariant to input content drift\").\n- Report **realistic performance range** (0.68–0.86 per-generator held-out F1, binary LOGO F1=0.72, 3-class LOGO F1=0.79 with gen-0 caveat) in abstract/conclusion, not just best-case. **禁止用 CI width 作为 cross-generator 一致性论据**（Round 2 C1 critical）——用 per-gen F1 std/range 替代。\n- R² on 5 aggregated depth means is statistically meaningless (3 df). Use individual-level Spearman ρ with bootstrap CIs throughout.\n\nRelated work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020), **stylometry/authorship attribution** (Stamatatos 2009, Koppel et al. 2009 — feature set is essentially stylometric), **iterative generation** (LLM as Broken Telephone ACL 2025, Markovian Generation Chains), **membership inference** (Shi et al. 2024).\n\n## Venue Fit\n- **EMNLP 2026**: Excellent fit — directly addresses \"New Missions for NLP Research\" theme (data contamination, synthetic data feedback loops, data governance). NLP-native venue. Empirical/conceptual contributions well-received. Novel task formulation + honest negative finding valued.\n\n## Open Questions (pending P1-C)\n- Instruct model depth response: if Qwen3-1.7B-Instruct shows drift → extend to 1-2 more instruct models; if not → limitation paragraph (scope narrowing already in place)\n- Rd2-W4 (no validated alternative application): diagnostic framing is current defense; no new experiment planned unless P1-C opens a new angle\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  registry_id: plan-003\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'DONE. Registry: plan-003 (parent), plan-003-olmo2ref, plan-003-qwen06bref.\n    Falsification test passed: entropy drift confirmed across all 3 reference families.\n    dual_dynamics_is_pythia_artifact: false. LOGO F1: Pythia 0.803, OLMo 0.807, Qwen\n    0.816.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  registry_id: plan-004-v2\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  registry_id: plan-005\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  registry_id: plan-007-cross-model\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: DONE\n  conclusion: success\n  metrics:\n    3class_macro_f1: 0.8089\n    3class_f1_std: 0.0166\n    binary_f1_gen1_vs_gen2plus: 0.7635\n    binary_f1_gen0_vs_gen2plus: 0.8372\n    per_class_f1:\n      gen0: 0.9285\n      gen1: 0.7367\n      gen2plus: 0.7614\n    n_samples: 2964\n    avg_generators_per_chain: 3\n    feature_importance:\n      hapax_ratio: 0.357\n      entropy_mean: 0.204\n      ttr: 0.202\n    vs_single_model:\n      pythia-1b: 0.8622\n      qwen3-0.6b: 0.8354\n      pythia-2.8b: 0.8156\n      qwen3-1.7b: 0.8106\n      olmo-2-1b: 0.7801\n      cross-model: 0.8089\n    n_samples_note: corrected from 4773 to 2964 per confusion matrix sum\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  registry_id: plan-008-multi-domain\n  description: 'Expand seeds to 3 domains: news (CNN/DailyMail), scientific (arXiv\n    abstracts via ccdv/arxiv-summarization), creative writing (WritingPrompts). 500\n    seeds per domain × 5 depths. Wikipedia used as transfer evaluation target (not\n    a seed domain). Single generator: Pythia-2.8B only (initial domain robustness\n    validation).\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  notes: 'Original plan said \"S2ORC abstracts\" but script uses ccdv/arxiv-summarization\n    (arXiv paper abstracts, more accessible on HuggingFace). Both are scientific text.\n    Wikipedia moved from seed domain to cross-domain transfer evaluation target. Single-generator\n    (Pythia-2.8B) limits claim scope — cannot directly support \"across domains AND\n    generators\" without multi-generator follow-up.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    per_domain:\n      news:\n        3class_f1: 0.5614\n        binary_f1: 0.6264\n      scientific:\n        3class_f1: 0.7049\n        binary_f1: 0.7701\n      creative:\n        3class_f1: 0.6275\n        binary_f1: 0.731\n      wikipedia:\n        3class_f1: 0.7928\n        binary_f1: 0.8224\n    cross_domain_pooled:\n      3class_f1: 0.4775\n      binary_f1: 0.6742\n    wiki_transfer:\n      news: 0.231\n      scientific: 0.3351\n      creative: 0.2319\n    n_records:\n      news: 2314\n      scientific: 2316\n      creative: 2466\n    dedup_applied: true\n    dedup_removed:\n      news: 801\n      scientific: 0\n      creative: 0\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  registry_id: plan-010-human-edit\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  notes: 'DONE/success. Graceful degradation: 5-20% random replacement -3.5 to -6.0pp\n    3-class, binary nearly unchanged. LLM rephrase: 3-class -3.4pp, binary -6.3pp.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline:\n      3class_f1: 0.7889\n      binary_f1: 0.7241\n      ci_3class:\n      - 0.787\n      - 0.798\n      ci_binary:\n      - 0.719\n      - 0.734\n    random_5pct:\n      3class_f1: 0.7538\n      binary_f1: 0.7182\n      delta_3class: -0.0351\n      delta_binary: -0.0059\n    random_10pct:\n      3class_f1: 0.7425\n      binary_f1: 0.7168\n      delta_3class: -0.0464\n      delta_binary: -0.0073\n    random_20pct:\n      3class_f1: 0.7292\n      binary_f1: 0.7165\n      delta_3class: -0.0597\n      delta_binary: -0.0076\n    llm_rephrase:\n      3class_f1: 0.7549\n      binary_f1: 0.6615\n      delta_3class: -0.034\n      delta_binary: -0.0626\n    degradation_curve: robust\n    llm_rephrase_robust: true\n    finding: 'Graceful degradation: 5-20% random replacement drops 3-class F1 by 3.5-6.0pp.\n      LLM rephrase: 3-class robust (-3.4pp) but binary degrades more (-6.3pp).'\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  registry_id: review-exp-a-baseline-ensemble\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  notes: 'Subsumed by plan-015 + review-exp-a-baseline-ensemble. LD-Score evaluated\n    as standalone baseline (3class=0.655, binary=0.701) and in multi-detector ensemble\n    (4-det+surface: 3class=0.805, binary=0.724). No separate plan_011 run needed.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    4_baseline:\n      avg_f1: 0.7964\n      ci95:\n      - 0.7921\n      - 0.8007\n    4_baseline_plus_surface:\n      avg_f1: 0.8049\n      ci95:\n      - 0.8003\n      - 0.8092\n    7_feature_unified:\n      avg_f1: 0.7887\n      ci95:\n      - 0.7839\n      - 0.793\n    7_feature_original:\n      avg_f1: 0.7887\n      ci95:\n      - 0.7839\n      - 0.793\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  registry_id: plan-013\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  registry_id: plan-014\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  registry_id: plan-015\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4_baseline:\n      avg_f1: 0.7964\n      ci95:\n      - 0.7921\n      - 0.8007\n    4_baseline_plus_surface:\n      avg_f1: 0.8049\n      ci95:\n      - 0.8003\n      - 0.8092\n    7_feature_unified:\n      avg_f1: 0.7887\n      ci95:\n      - 0.7839\n      - 0.793\n    7_feature_original:\n      avg_f1: 0.7887\n      ci95:\n      - 0.7839\n      - 0.793\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_f1_v2: 0.7878\n    overall_ci95_v2:\n    - 0.783\n    - 0.792\n    ci_width: 0.009\n    pipeline: bootstrap_ci_v2.py (class-balanced downsample)\n    per_gen_sanity_check:\n      olmo-2-1b: 0.7649\n      pythia-1b: 0.8528\n      pythia-2.8b: 0.8037\n      qwen3-0.6b: 0.8231\n      qwen3-1.7b: 0.8064\n      qwen3-8b: 0.6815\n- exp_id: review-p0a-gen0-leakage\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 21557\n    7_feature:\n      f1: 0.7233\n      ci95:\n      - 0.7174\n      - 0.7292\n    avg_logprob:\n      f1: 0.7124\n      ci95:\n      - 0.706\n      - 0.7189\n    ld_score:\n      f1: 0.7009\n      ci95:\n      - 0.6942\n      - 0.7073\n    fastdetectgpt:\n      f1: 0.6155\n      ci95:\n      - 0.6086\n      - 0.6222\n    binoculars:\n      f1: 0.524\n      ci95:\n      - 0.5167\n      - 0.5306\n    4_baseline:\n      f1: 0.7118\n      ci95:\n      - 0.7052\n      - 0.7182\n    4_baseline_surface:\n      f1: 0.7239\n      ci95:\n      - 0.7179\n      - 0.7303\n- exp_id: review-p0b-volume-matched\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    5gen_logo_original: 0.8019\n    5gen_volume_matched_avg: 0.8024\n    6gen_logo_excl_qwen8b: 0.8102\n    volume_effect_pp: 0.05\n    diversity_residual_pp: 0.78\n    diversity_pct: 94\n- exp_id: review-p1c-instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_records: 4963\n    depths: 5\n    seeds: 996\n    length_depth_spearman: -0.52\n    length_confound_dominates: true\n    depth_signal_after_control: negligible\n    length_per_depth_tokens:\n      '0': 252\n      '1': 79\n      '2': 74\n      '3': 72\n      '4': 68\n    original_rho:\n      ttr: 0.48\n      hapax: 0.477\n      entropy_mean: 0.478\n    length_matched_rho:\n      ttr: 0.19\n      hapax: 0.224\n      entropy_mean: 0.042\n    partial_rho:\n      ttr: 0.13\n      hapax: 0.166\n      entropy_mean: 0.161\n    binary_gen1_vs_gen2plus_f1: 0.506\n- exp_id: review-p1d-table3-6gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    avglogprob_100_3: 0.737\n    avglogprob_200_6: 0.737\n    fastdetectgpt_100_3: 0.688\n    fastdetectgpt_200_6: 0.688\n    ldscore_100_3: 0.655\n    ldscore_200_6: 0.654\n    binoculars_100_3: 0.416\n    binoculars_200_6: 0.417\n    max_hyperparam_delta: 0.0011\n    hyperparam_effect: negligible\n- exp_id: review-p1e-ordinal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    xgboost_3class_f1: 0.7888\n    coral_3class_f1: 0.7711\n    frankhall_3class_f1: 0.7931\n    xgboost_binary_f1: 0.7213\n    coral_binary_f1: 0.7275\n    xgboost_concordance: 0.821\n    coral_concordance: 0.81\n    frankhall_concordance: 0.825\n    ordinal_benefit: negligible\n    ci_overlap: true\n- exp_id: review-p2f-cross-ref-bias\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia1b_f1_pythia410m_ref: 0.856\n    pythia1b_f1_olmo_ref: 0.845\n    pythia1b_f1_qwen_ref: 0.848\n    same_to_cross_drop: 0.009\n    pythia1b_rank_all_refs: 1\n    same_family_bias: false\n- exp_id: review-p1c-olmo-instruct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    instruct_logo_f1: 0.338\n    base_olmo_logo_f1: 0.763\n    delta: -0.425\n    n_records: 4429\n    binary_logo_f1: 0.3506\n    length_depth_spearman: -0.3701\n    length_confound_dominates: false\n    depth_signal_after_control: partially_survives\n    original_rho:\n      entropy_mean: 0.4822\n      ttr: 0.0057\n      hapax: 0.0253\n    partial_rho:\n      entropy_mean: 0.364\n      ttr: -0.2407\n      hapax: -0.1979\n    entropy_reversal_survives_length_control: true\n    surface_reversal: false\n- exp_id: review-p1c-qwen06b-instruct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    instruct_logo_3class_f1: 0.667\n    base_logo_3class_f1: 0.816\n    delta_3class: -0.148\n    binary_gen1_vs_gen2plus_f1: 0.552\n    length_depth_spearman: -0.583\n    length_confound_dominates: true\n    depth_signal_after_control: negligible\n    length_per_depth_tokens:\n      '0': 252\n      '1': 35\n      '2': 27\n      '3': 24\n      '4': 23\n    length_matched_rho:\n      ttr: -0.007\n      hapax: -0.003\n      entropy_mean: -0.012\n- exp_id: review-rd2m7-bib-audit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    diveye:\n      year_correct: true\n      year: 2026\n      venue: TMLR\n      author_fix: Varun Basani → Advik Raj Basani, Yuntian Chen → Pin-Yu Chen\n    strong_model_collapse:\n      year_correct: true\n      year: 2025\n      venue: ICLR\n    aaronson_watermark:\n      author_fix: Chelsea → Hendrik Kirchner\n      url_added: https://scottaaronson.blog/?p=6823\n- exp_id: review-sampling-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_t05_p08:\n      3class_f1: 0.785\n      binary_f1: 0.797\n      spearman_entropy_mean: -0.694\n    default_t07_p09:\n      3class_f1: 0.788\n      binary_f1: 0.799\n      spearman_entropy_mean: -0.602\n    high_t10_p095:\n      3class_f1: 0.726\n      binary_f1: 0.733\n      spearman_entropy_mean: -0.002\n    f1_range_pp: 6.19\n    robust: false\n    finding: Low/default configs robust (<0.3pp diff). High temp (t=1.0) degrades\n      depth signal ~6pp; entropy correlation drops to ~0. Qwen3-1.7B per-gen F1 collapses\n      to 0.418 at high temp.\n- exp_id: review-p1c-instruct-logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    7gen_logo_avg_f1: 0.7498\n    7gen_binary_f1: 0.768\n    6gen_base_logo_f1: 0.789\n    6gen_base_binary_f1: 0.723\n    instruct_held_out_3class_f1: 0.5434\n    instruct_held_out_binary_f1: 0.6582\n    base_qwen17b_held_out_3class_f1: 0.8023\n    base_qwen17b_held_out_binary_f1: 0.8208\n    instruct_vs_base_delta_3class: -0.2589\n    instruct_vs_base_delta_binary: -0.1626\n- exp_id: plan-010-human-edit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline:\n      3class_f1: 0.7889\n      binary_f1: 0.7241\n      ci_3class:\n      - 0.787\n      - 0.798\n      ci_binary:\n      - 0.719\n      - 0.734\n    random_5pct:\n      3class_f1: 0.7538\n      binary_f1: 0.7182\n      delta_3class: -0.0351\n      delta_binary: -0.0059\n    random_10pct:\n      3class_f1: 0.7425\n      binary_f1: 0.7168\n      delta_3class: -0.0464\n      delta_binary: -0.0073\n    random_20pct:\n      3class_f1: 0.7292\n      binary_f1: 0.7165\n      delta_3class: -0.0597\n      delta_binary: -0.0076\n    llm_rephrase:\n      3class_f1: 0.7549\n      binary_f1: 0.6615\n      delta_3class: -0.034\n      delta_binary: -0.0626\n    degradation_curve: robust\n    llm_rephrase_robust: true\n    finding: 'Graceful degradation: 5-20% random replacement drops 3-class F1 by 3.5-6.0pp.\n      LLM rephrase: 3-class robust (-3.4pp) but binary degrades more (-6.3pp).'\n- exp_id: plan-008-multi-domain\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    per_domain:\n      news:\n        3class_f1: 0.5614\n        binary_f1: 0.6264\n      scientific:\n        3class_f1: 0.7049\n        binary_f1: 0.7701\n      creative:\n        3class_f1: 0.6275\n        binary_f1: 0.731\n      wikipedia:\n        3class_f1: 0.7928\n        binary_f1: 0.8224\n    cross_domain_pooled:\n      3class_f1: 0.4775\n      binary_f1: 0.6742\n    wiki_transfer:\n      news: 0.231\n      scientific: 0.3351\n      creative: 0.2319\n    n_records:\n      news: 2314\n      scientific: 2316\n      creative: 2466\n    dedup_applied: true\n    dedup_removed:\n      news: 801\n      scientific: 0\n      creative: 0\n- exp_id: plan-007-cross-model\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    3class_macro_f1: 0.8089\n    3class_f1_std: 0.0166\n    binary_f1_gen1_vs_gen2plus: 0.7635\n    binary_f1_gen0_vs_gen2plus: 0.8372\n    per_class_f1:\n      gen0: 0.9285\n      gen1: 0.7367\n      gen2plus: 0.7614\n    n_samples: 2964\n    avg_generators_per_chain: 3\n    feature_importance:\n      hapax_ratio: 0.357\n      entropy_mean: 0.204\n      ttr: 0.202\n    vs_single_model:\n      pythia-1b: 0.8622\n      qwen3-0.6b: 0.8354\n      pythia-2.8b: 0.8156\n      qwen3-1.7b: 0.8106\n      olmo-2-1b: 0.7801\n      cross-model: 0.8089\n    n_samples_note: corrected from 4773 to 2964 per confusion matrix sum\n- exp_id: plan-006-paraphrastic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    paraphrastic_3class_f1: 0.68\n    paraphrastic_3class_f1_std: 0.0086\n    paraphrastic_binary_f1: 0.539\n    paraphrastic_binary_f1_std: 0.017\n    continuation_3class_f1: 0.788\n    continuation_3class_f1_std: 0.0061\n    continuation_binary_f1: 0.749\n    continuation_binary_f1_std: 0.011\n    f1_3class_delta: -0.108\n    retention_para: 0.8915\n    retention_cont: 0.8261\n    retention_delta: 0.0654\n    cross_transfer_para_to_cont_f1: 0.155\n    cross_transfer_cont_to_para_f1: 0.431\n    spearman_entropy_mean_para: 0.394\n    spearman_entropy_mean_cont: -0.675\n    spearman_ttr_para: 0.567\n    spearman_ttr_cont: -0.633\n    spearman_hapax_para: 0.556\n    spearman_hapax_cont: -0.655\n    spearman_signs_reversed: true\n    n_paraphrastic: 4754\n    n_continuation: 4609\n- exp_id: plan-009-finer-ordinal\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    5class_HGBT_macro_f1: 0.5028\n    5class_HGBT_f1_95ci:\n    - 0.4974\n    - 0.5079\n    5class_HGBT_accuracy: 0.5423\n    5class_HGBT_mae: 0.6587\n    5class_RF_macro_f1: 0.4767\n    5class_LR_macro_f1: 0.4468\n    5class_FrankHall_macro_f1: 0.4513\n    3class_HGBT_macro_f1: 0.7815\n    3class_HGBT_f1_95ci:\n    - 0.7764\n    - 0.7864\n    delta_5class_vs_3class: -0.2787\n    5class_per_class_f1:\n      depth_0: 0.9129\n      depth_1: 0.6277\n      depth_2: 0.2687\n      depth_3: 0.2653\n      depth_4: 0.4393\n    gen2_gen3_inseparable: true\n- exp_id: plan-012-qwen06b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    5class_macro_f1: 0.583\n    5class_f1_std: 0.01\n    3class_macro_f1: 0.905\n    3class_f1_std: 0.003\n    per_class_f1:\n      gen0: 0.999\n      gen1: 0.796\n      gen2: 0.413\n      gen3: 0.259\n      gen4: 0.447\n    runtime_seconds: 6928\n    model: Qwen3-0.6B-Base\n    method: QLoRA\n    lora_rank: 16\n    seed: 42\n- exp_id: plan-006-confound-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_paraphrastic_clean: 4912\n    n_paraphrastic_contaminated_removed: 4754\n    paraphrastic_3class_f1: 0.742\n    paraphrastic_binary_f1: 0.671\n    continuation_3class_f1: 0.788\n    continuation_binary_f1: 0.749\n    f1_3class_delta: -0.046\n    spearman_entropy_mean_para: -0.533\n    spearman_entropy_mean_cont: -0.675\n    entropy_reversal_was_artifact: true\n    cross_transfer_para_to_cont_f1: 0.77\n    cross_transfer_cont_to_para_f1: 0.743\n    depth_retention_para: 0.97\n    vs_contaminated:\n      old_3class_f1: 0.68\n      new_3class_f1: 0.742\n      old_binary_f1: 0.539\n      new_binary_f1: 0.671\n      old_entropy_rho: 0.394\n      new_entropy_rho: -0.533\n- exp_id: plan-012-pythia410m\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    5class_macro_f1: 0.556\n    5class_f1_std: 0.016\n    3class_macro_f1: 0.87\n    3class_f1_std: 0.022\n    per_class_f1:\n      gen0: 0.991\n      gen1: 0.733\n      gen2: 0.347\n      gen3: 0.291\n      gen4: 0.42\n    runtime_seconds: 3705\n    model: Pythia-410M\n    method: QLoRA\n- exp_id: plan-012-qwen06b-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    5class_macro_f1: 0.5873\n    5class_f1_std: 0.0047\n    3class_macro_f1: 0.9054\n    3class_f1_std: 0.0037\n    per_class_5class:\n      depth_0: 0.9995\n      depth_1: 0.7959\n      depth_2: 0.4016\n      depth_3: 0.3176\n      depth_4: 0.4217\n    per_class_3class:\n      gen0: 0.9995\n      gen1: 0.7959\n      gen2plus: 0.9209\n    runtime_minutes: 116.7\n    model: Qwen3-0.6B-Base\n    method: QLoRA\n    lora_rank: 32\n    seed: 123\n    results_file: results/plan012_qwen06b_seed123_r32_results.json\n    vs_xgboost_5class_delta_pp: 8.5\n    vs_xgboost_3class_delta_pp: 12.4\n- exp_id: plan-016-llama32-3b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-016-gemma2-2b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-016-mistral-7b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-016-crossref-qwen8b\n  name: ''\n  status: QUEUED\n  conclusion: success\n  metrics:\n    logo_avg_pythia_ref: 0.7891\n    logo_avg_olmo_ref: 0.7948\n    logo_avg_qwen_ref: 0.8135\n    qwen8b_pythia_ref: 0.6854\n    qwen8b_olmo_ref: 0.6962\n    qwen8b_qwen_ref: 0.7568\n    ci95_pythia:\n    - 0.747\n    - 0.824\n    ci95_olmo:\n    - 0.757\n    - 0.828\n    ci95_qwen:\n    - 0.785\n    - 0.842\n    all_entropy_drift_negative: true\n    spread_across_refs: 0.024\n- exp_id: plan-016-llama32-3b-rp11\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T11:04:29.682Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T11:04:29.682Z",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-16T11:04:29.700Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：部分新家族 depth signal 退化（类似 Qwen3-8B 模式），泛化 claim 需收窄但核心贡献不变
核心假设：['3 个新家族中 1-2 个 held-out F1 < 0.60（类似 instruct 退化但不至于 chance level）', '扩展后 LOGO binary F1 下降至 0.68-0.71 区间（被低性能 generator 拉低）', '7-feature vs best baseline 优势缩窄至 +1.0-2.5pp（仍显著但 effect size 小）', 'differential response 在多数但非全部家族成立（个别家族 shape feature 也出现 drift）', '某些家族的 cross-scale/cross-architecture gap 比预期更大']
关键指标范围：{'binary_logo_f1_expanded': [0.68, 0.72], 'per_gen_f1_std': [0.07, 0.11], 'worst_single_gen_f1': [0.5, 0.62], 'seven_feat_vs_best_baseline_pp': [1.0, 2.5], 'new_family_avg_held_out_f1': [0.55, 0.68], 'drifting_feature_spearman_range': [-0.55, -0.2], 'shape_feature_spearman_range': [-0.2, 0.2]}
叙事方向：需要调整 claims 强度。Claim 1 从 "generalizes across model families" 收窄为  "robust within tested base-model regime (≤8B), with architecture-dependent transfer gap  as honest limitation"。Claim 2 补充 caveat：differential response 是 dominant pattern  但非 universal（某些架构 shape features 也漂移）。增加 "conditions under which depth  signal degrades" 的系统分析作为额外贡献。Paper 仍以 novel task + empirical  characterization 为主线，但 universality claim 变为 qualified generalization。 可能需要 Table 明确标注哪些 generators 属于 "high-signal" vs "low-signal" regime。 EMNLP 投稿强度：borderline accept，需要 rebuttal 说服 1-2 个 reviewer。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-fingerprint

## paper_framing.md

# Paper Framing — gen-depth-fingerprint

## Target Venue
- **Primary: EMNLP 2026 ARR (deadline: May 25, 2026)** — D012
- Fallback: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)

## Core Insight
Non-paraphrastic LLM generation chains exhibit **differential depth response**: **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **distributional shape features** (entropy_std, tail_decay) remain near-stationary. This differential response is consistent with recursive generation inducing a **location shift** in the NLL distribution — the text becomes progressively more predictable (mean shifts) while the functional form of the distribution is preserved (shape is invariant). The genuine novelty is not the drift/stationarity split per se (which follows from location-shift properties), but: (a) the **task formulation** (ordinal depth estimation beyond binary detection), (b) **empirical validation** across 6 generators / 3 model families (including 7B+ scale) showing this pattern is robust, (c) the practical consequence that combining both feature types yields **complementary signal** for depth classification. **Primary metric (D017)**: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, excluding gen-0 due to shared-seed leakage). 3-class LOGO F1 = 0.789 reported as supplementary with gen-0 caveat. Per-generator held-out F1: 0.68–0.86 (std=0.058). Key finding: in binary evaluation (no gen-0 leakage), 7-feature (0.723) > 4-baseline ensemble (0.712) — baseline advantage in 3-class was entirely from gen-0 classification. Depth signal is scale-invariant as a phenomenon, though cross-scale classifier transfer shows a moderate gap (8B held-out F1=0.69 vs ≤2.8B 0.76-0.85).

## Core Claims (3 条，均可证伪)

**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth with F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation). Primary metric: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, gen-0 excluded due to shared-seed overlap). 3-class (gen-0/gen-1/gen-2+) LOGO F1 = 0.789 supplementary with caveat.

**Claim 2 — Differential Depth Response & Feature Complementarity**: Depth-dependent features exhibit differential response: central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (consistent with location shift in NLL distribution), while shape features (entropy_std, tail_decay) remain near-stationary. In binary eval, 7-feature ensemble (0.723) outperforms 4-baseline detector ensemble (0.712) by +1.1pp and all individual detectors (+1.1–19.9pp). The 4-baseline advantage in 3-class (0.796 vs 0.789) is entirely from gen-0 classification. Ordinal-specific methods (CORAL 0.771, Frank-Hall 0.793) do not outperform XGBoost (0.789) — CI overlap at 3-class granularity.

**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality compared to random subsampling. At equal data count, size_matched (random control, ppl=2.367) outperforms depth01 (depth-stratified, 2.387) and binary_filtered (2.389). The primary determinant is data quantity, not depth composition (all 12K samples → ppl=2.335). Depth fingerprinting is an effective **diagnostic** tool for characterizing provenance, but not a **curative** tool for data curation. This honest negative finding is reported transparently.

## Story Spine

**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).

**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation. When repurposed as ordinal depth predictors, single detector scores (Avg-LogProb 0.737, LD-Score 0.655, FastDetectGPT 0.688, Binoculars 0.417 under 6-gen LOGO) show moderate signal but **high per-generator F1 variance** (e.g., AvgLogProb range 0.615–0.805, 19.0pp span), making them unreliable as standalone depth estimators.

**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **differential depth response**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth, while distributional shape features (entropy variance, tail decay) remain near-stationary. This split is about **what the feature measures** (central tendency vs shape), not where it comes from. The combination of drifting and stationary features yields a 7-feature ensemble that **significantly and consistently** outperforms all single-detector baselines: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, p<0.001 vs Avg-LogProb 0.712, LD-Score 0.701, FastDetectGPT 0.616, Binoculars 0.524). In the leak-free binary evaluation, 7-feature (0.723) > 4-baseline ensemble (0.712), reversing the 3-class result where baseline advantage came entirely from gen-0 classification. The practical advantage is **reliability across unknown generators** — per-generator F1 std = 0.058 for our ensemble vs higher variance for individual detectors.

**Headline result template**: "On non-paraphrastic continuation chains across 6 base-model generators from 3 model families (0.6B–8.2B), our 7-feature distributional ensemble achieves binary LOGO F1 of 0.72 for leak-free depth discrimination (gen-1 vs gen-2+), outperforming all individual detection baselines. Per-generator held-out F1 ranges from 0.68 to 0.86 (std=0.051). Depth-aware data curation does not outperform random subsampling for downstream CLM quality, establishing depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection."

## Anticipated Reviewer Concerns

**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.73 macro-F1, but full 7-feature ensemble achieves 0.789 3-class / 0.723 binary (p<0.001). We don't claim reference features are "better" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). Note: "fingerprint" in the paper refers to the full feature vector's combination, not just reference-model features.

**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.

**RC2 — "Does this generalize beyond Pythia?"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).

**RC3 — "Is 3-class sufficient? Why not finer-grained?"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.

**RC4 — "How realistic are single-model chains?"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).

**RC5 — "What about human editing / post-processing?"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).

**RC6 — "Ecological validity — continuation vs real web content"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).

**RC8 — "Aren't these just OOD detection features?"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.

**RC9 — "Only ≤2.8B generators — does this transfer to frontier scale?"**: **Answered (plan-014, D011).** Qwen3-8B (7.6B params) added as 6th generator. Depth signal IS present at 8B scale — all feature-depth Spearman correlations significant. Cross-scale transfer gap: 8B held-out F1=0.69 vs ≤2.8B 0.76-0.85. P0-B volume-matched control: adding Qwen3-8B's +1.1pp improvement is 94% from generator diversity, not data volume. **Paper framing**: depth signal universality supported; cross-scale gap is honest limitation; scope narrowed to base models (see N3/N4 fixes).

**RC10 — "Text length confound"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.

**RC11 — "Downstream utility — single run, no CIs"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).

## Contribution Positioning (D006+D007)
The contribution is **primarily empirical and conceptual**, not methodological:
1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection (genuinely novel — no prior work)
2. **Empirical characterization**: Differential depth response across 6 generators / 3 families (including 7B+ scale), with robust cross-generator generalization (binary LOGO F1=0.723, 3-class LOGO F1=0.789). Scale-invariant phenomenon with honest cross-scale transfer gap.
3. **Negative finding**: Depth-aware data curation does NOT improve downstream CLM quality — depth fingerprinting is diagnostic, not curative (D009).

**Framing discipline (D007 — re-dream consensus):**
- Do NOT call the drift/stationarity split a "discovery" — it follows from location-shift properties of the NLL distribution (means shift under distributional drift, shapes don't). Acknowledge this explicitly.
- Do NOT use H1/H2 terminology (overloads time-series unit-root convention). Use "drifting" vs "stationary" or "differential response."
- Do NOT overclaim "dual dynamics" as a novel theoretical framework. Use "differential depth response" — more calibrated.
- Consider renaming "distributional fingerprinting" → "distributional depth profiling" (fingerprinting implies source identification, creates confusion with LLM attribution literature).
- Provide at least a speculative theoretical motivation for WHY shape features remain stationary (e.g., "shape is determined by sampling mechanism and architecture, invariant to input content drift").
- Report **realistic performance range** (0.68–0.86 per-generator held-out F1, binary LOGO F1=0.72, 3-class LOGO F1=0.79 with gen-0 caveat) in abstract/conclusion, not just best-case. **禁止用 CI width 作为 cross-generator 一致性论据**（Round 2 C1 critical）——用 per-gen F1 std/range 替代。
- R² on 5 aggregated depth means is statistically meaningless (3 df). Use individual-level Spearman ρ with bootstrap CIs throughout.

Related work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020), **stylometry/authorship attribution** (Stamatatos 2009, Koppel et al. 2009 — feature set is essentially stylometric), **iterative generation** (LLM as Broken Telephone ACL 2025, Markovian Generation Chains), **membership inference** (Shi et al. 2024).

## Venue Fit
- **EMNLP 2026**: Excellent fit — directly addresses "New Missions for NLP Research" theme (data contamination, synthetic data feedback loops, data governance). NLP-native venue. Empirical/conceptual contributions well-received. Novel task formulation + honest negative finding valued.

## Open Questions (pending P1-C)
- Instruct model depth response: if Qwen3-1.7B-Instruct shows drift → extend to 1-2 more instruct models; if not → limitation paragraph (scope narrowing already in place)
- Rd2-W4 (no validated alternative application): diagnostic framing is current defense; no new experiment planned unless P1-C opens a new angle


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
  registry_id: plan-003
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
  notes: 'DONE. Registry: plan-003 (parent), plan-003-olmo2ref, plan-003-qwen06bref.
    Falsification test passed: entropy drift confirmed across all 3 reference families.
    dual_dynamics_is_pythia_artifact: false. LOGO F1: Pythia 0.803, OLMo 0.807, Qwen
    0.816.

    '
  status: DONE
  conclusion: success
  metrics:
    logo_f1_pythia_ref: 0.8034
    logo_f1_olmo_ref: 0.8072
    logo_f1_qwen_ref: 0.8158
    entropy_drift_all_refs_negative: true
    olmo_ref_drift_range:
    - -0.608
    - -0.9089
    qwen_ref_drift_range:
    - -0.9557
    - -1.3458
    pythia_ref_drift_range:
    - -1.1872
    - -1.4017
    dual_dynamics_is_pythia_artifact: false
- id: plan_004
  claim: 3
  name: downstream_utility
  registry_id: plan-004-v2
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
  status: DONE
  conclusion: negative
  metrics:
    total_runs: 15
    completed: 15
    variants:
      all:
        eval_loss_mean: 0.848
        perplexity_mean: 2.335
        seeds:
          '42':
            eval_loss: 0.848
            ppl: 2.335
          '123':
            eval_loss: 0.848
            ppl: 2.335
          '456':
            eval_loss: 0.8482
            ppl: 2.3354
      size_matched:
        eval_loss_mean: 0.8617
        perplexity_mean: 2.367
        seeds:
          '42':
            eval_loss: 0.8618
            ppl: 2.367
          '123':
            eval_loss: 0.8615
            ppl: 2.367
          '456':
            eval_loss: 0.8618
            ppl: 2.367
      depth01:
        eval_loss_mean: 0.8701
        perplexity_mean: 2.387
        seeds:
          '42':
            eval_loss: 0.8703
            ppl: 2.3877
          '123':
            eval_loss: 0.87
            ppl: 2.3869
          '456':
            eval_loss: 0.8699
            ppl: 2.387
      binary_filtered:
        eval_loss_mean: 0.8709
        perplexity_mean: 2.389
        seeds:
          '42':
            eval_loss: 0.8708
            ppl: 2.389
          '123':
            eval_loss: 0.871
            ppl: 2.389
          '456':
            eval_loss: 0.871
            ppl: 2.389
      depth0_only:
        eval_loss_mean: 0.9864
        perplexity_mean: 2.681
        seeds:
          '42':
            eval_loss: 0.9865
            ppl: 2.6818
          '123':
            eval_loss: 0.9863
            ppl: 2.68
          '456':
            eval_loss: 0.9865
            ppl: 2.6817
    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)
      << depth0_only(2.681)
    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）
- id: plan_005
  claim: 1
  name: prompt_type_comparison
  registry_id: plan-005
  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting
    chains. Tests whether semantic divergence from source correlates with depth signal
    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.

    '
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_001
  status: DONE
  conclusion: success
  metrics:
    cv_f1:
      continuation: 0.7806
      inspired_rewriting: 0.7368
      elaboration: 0.73
    lopto_f1:
      held_out_cont: 0.762
      held_out_elab: 0.7622
      held_out_rewrite: 0.7334
      avg: 0.7525
    depth_retention_d4_d0:
      continuation: 0.831
      inspired_rewriting: 0.939
      elaboration: 0.986
    drift_hapax_ratio:
      continuation: -0.74
      elaboration: -0.828
      rewriting: -0.8
    drift_ttr:
      continuation: -0.607
      elaboration: -0.641
      rewriting: -0.618
    drift_entropy_mean:
      continuation: -0.557
      elaboration: -0.471
      rewriting: -0.477
    spearman_ttr:
      continuation: -0.629
      elaboration: -0.666
      rewriting: -0.659
    spearman_hapax:
      continuation: -0.651
      elaboration: -0.674
      rewriting: -0.67
    spearman_entropy_mean:
      continuation: -0.665
      elaboration: -0.583
      rewriting: -0.564
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
  registry_id: plan-007-cross-model
  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model
    chains. More realistic scenario — web contamination involves diverse generators.

    '
  priority: P1
  gpu_budget_hours: 12
  deps:
  - plan_002
  status: DONE
  conclusion: success
  metrics:
    3class_macro_f1: 0.8089
    3class_f1_std: 0.0166
    binary_f1_gen1_vs_gen2plus: 0.7635
    binary_f1_gen0_vs_gen2plus: 0.8372
    per_class_f1:
      gen0: 0.9285
      gen1: 0.7367
      gen2plus: 0.7614
    n_samples: 2964
    avg_generators_per_chain: 3
    feature_importance:
      hapax_ratio: 0.357
      entropy_mean: 0.204
      ttr: 0.202
    vs_single_model:
      pythia-1b: 0.8622
      qwen3-0.6b: 0.8354
      pythia-2.8b: 0.8156
      qwen3-1.7b: 0.8106
      olmo-2-1b: 0.7801
      cross-model: 0.8089
    n_samples_note: corrected from 4773 to 2964 per confusion matrix sum
- id: plan_008
  claim: 1
  name: multi_domain_seeds
  registry_id: plan-008-multi-domain
  description: 'Expand seeds to 3 domains: news (CNN/DailyMail), scientific (arXiv
    abstracts via ccdv/arxiv-summarization), creative writing (WritingPrompts). 500
    seeds per domain × 5 depths. Wikipedia used as transfer evaluation target (not
    a seed domain). Single generator: Pythia-2.8B only (initial domain robustness
    validation).

    '
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_002
  notes: 'Original plan said "S2ORC abstracts" but script uses ccdv/arxiv-summarization
    (arXiv paper abstracts, more accessible on HuggingFace). Both are scientific text.
    Wikipedia moved from seed domain to cross-domain transfer evaluation target. Single-generator
    (Pythia-2.8B) limits claim scope — cannot directly support "across domains AND
    generators" without multi-generator follow-up.

    '
  status: DONE
  conclusion: success
  metrics:
    per_domain:
      news:
        3class_f1: 0.5614
        binary_f1: 0.6264
      scientific:
        3class_f1: 0.7049
        binary_f1: 0.7701
      creative:
        3class_f1: 0.6275
        binary_f1: 0.731
      wikipedia:
        3class_f1: 0.7928
        binary_f1: 0.8224
    cross_domain_pooled:
      3class_f1: 0.4775
      binary_f1: 0.6742
    wiki_transfer:
      news: 0.231
      scientific: 0.3351
      creative: 0.2319
    n_records:
      news: 2314
      scientific: 2316
      creative: 2466
    dedup_applied: true
    dedup_removed:
      news: 801
      scientific: 0
      creative: 0
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
  registry_id: plan-010-human-edit
  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement
    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of
    random sentences).

    '
  priority: P2
  gpu_budget_hours: 5
  deps:
  - plan_002
  notes: 'DONE/success. Graceful degradation: 5-20% random replacement -3.5 to -6.0pp
    3-class, binary nearly unchanged. LLM rephrase: 3-class -3.4pp, binary -6.3pp.

    '
  status: DONE
  conclusion: success
  metrics:
    baseline:
      3class_f1: 0.7889
      binary_f1: 0.7241
      ci_3class:
      - 0.787
      - 0.798
      ci_binary:
      - 0.719
      - 0.734
    random_5pct:
      3class_f1: 0.7538
      binary_f1: 0.7182
      delta_3class: -0.0351
      delta_binary: -0.0059
    random_10pct:
      3class_f1: 0.7425
      binary_f1: 0.7168
      delta_3class: -0.0464
      delta_binary: -0.0073
    random_20pct:
      3class_f1: 0.7292
      binary_f1: 0.7165
      delta_3class: -0.0597
      delta_binary: -0.0076
    llm_rephrase:
      3class_f1: 0.7549
      binary_f1: 0.6615
      delta_3class: -0.034
      delta_binary: -0.0626
    degradation_curve: robust
    llm_rephrase_robust: true
    finding: 'Graceful degradation: 5-20% random replacement drops 3-class F1 by 3.5-6.0pp.
      LLM rephrase: 3-class robust (-3.4pp) but binary degrades more (-6.3pp).'
- id: plan_011
  claim: 2
  name: ld_score_feature
  registry_id: review-exp-a-baseline-ensemble
  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)
    as additional feature. Tests whether character-level features provide complementary
    depth signal.

    '
  priority: P2
  gpu_budget_hours: 2
  deps:
  - plan_001
  notes: 'Subsumed by plan-015 + review-exp-a-baseline-ensemble. LD-Score evaluated
    as standalone baseline (3class=0.655, binary=0.701) and in multi-detector ensemble
    (4-det+surface: 3class=0.805, binary=0.724). No separate plan_011 run needed.

    '
  status: DONE
  conclusion: success
  metrics:
    4_baseline:
      avg_f1: 0.7964
      ci95:
      - 0.7921
      - 0.8007
    4_baseline_plus_surface:
      avg_f1: 0.8049
      ci95:
      - 0.8003
      - 0.8092
    7_feature_unified:
      avg_f1: 0.7887
      ci95:
      - 0.7839
      - 0.793
    7_feature_original:
      avg_f1: 0.7887
      ci95:
      - 0.7839
      - 0.793
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
  registry_id: plan-013
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
  status: DONE
  conclusion: success
  metrics:
    spearman_rho_range: '[-0.066, +0.134]'
    length_depth_correlation: weak (|ρ|<0.14)
    normalized_ttr_trend_preserved: true
    normalized_hapax_trend_preserved: true
    normalized_rho_stronger: true
    length_matched_f1_delta: '+0.041'
    length_is_confound: false
    dropout_short_text_bias: true
- id: plan_014
  claim: 1
  name: large_scale_generator
  registry_id: plan-014
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
  status: DONE
  conclusion: success
  metrics:
    total_records: 4497
    unique_seeds: 995
    depth_dist:
      '0': 995
      '1': 979
      '2': 937
      '3': 831
      '4': 755
    logo_6gen_avg_f1: 0.7893
    logo_per_generator:
      olmo-2-1b: 0.7635
      pythia-1b: 0.8562
      pythia-2.8b: 0.8041
      qwen3-0.6b: 0.8243
      qwen3-1.7b: 0.8046
      qwen3-8b: 0.6832
    logo_qwen3_8b_held_out_f1: 0.6832
    logo_5gen_baseline_f1: 0.8
    spearman:
      hapax_ratio: -0.5578
      ttr: -0.5419
      entropy_mean: -0.4754
      entropy_min: -0.3029
      entropy_max: 0.0946
      tail_decay: -0.0894
      entropy_std: -0.0755
    feature_importance:
      hapax_ratio: 0.269
      entropy_mean: 0.1637
      ttr: 0.159
      entropy_max: 0.0634
      entropy_std: 0.0463
      entropy_min: 0.0153
      tail_decay: 0.0123
    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)
    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness
- id: plan_015
  claim: 1
  name: ordinal_baseline_comparison
  registry_id: plan-015
  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):
    Test whether existing detector continuous scores already provide ordinal depth
    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation
    depth. Compare single-feature ordinal classifiers (each detector score as sole
    feature) vs our 7-feature model. If existing detectors yield comparable ordinal
    signal, our custom feature set contribution collapses.

    '
  priority: P0
  gpu_budget_hours: 3
  deps:
  - plan_002
  notes: 'Re-dream consensus: without this comparison, reviewers will question whether
    depth-specific features add value. Must be in the paper. FastDetectGPT needs model
    pair (source + reference), LD-Score is character-level, Binoculars needs two models.
    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution
    as "complementary to existing detectors" not "novel approach."

    '
  status: DONE
  conclusion: success
  metrics:
    seven_feature_logo_f1: 0.798
    seven_feature_ci:
    - 0.786
    - 0.799
    avg_logprob_logo_f1: 0.7653
    avg_logprob_ci:
    - 0.616
    - 0.82
    avg_logprob_spearman: 0.7876
    ld_score_logo_f1: 0.7212
    ld_score_ci:
    - 0.588
    - 0.77
    ld_score_spearman: 0.7943
    ld_score_pre_fix: 0.6854
    fast_detect_gpt_logo_f1: 0.6269
    fast_detect_gpt_ci:
    - 0.511
    - 0.762
    fast_detect_gpt_spearman: 0.4325
    binoculars_logo_f1: 0.579
    binoculars_ci:
    - 0.405
    - 0.664
    binoculars_spearman: 0.1989
    binoculars_bug_confirmed: true
    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,
      shifted_ids)
    bootstrap_n: 1000
    bootstrap_delta_7feat_vs_avglogprob:
      delta: 0.039
      p: 0
      significant: true
    bootstrap_delta_7feat_vs_fdgpt:
      delta: 0.067
      p: 0
      significant: true
    best_single_detector: Avg-LogProb (0.7653)
    seven_feature_advantage_pp: 3.3


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
  status: DONE
  conclusion: success
  metrics:
    total_records: 18423
    models: 4
    pythia_1b:
      records: 4555
      seeds: 995
      file: data/pythia-1b/generations.jsonl
    olmo_2_1b:
      records: 4713
      seeds: 995
      file: data/olmo-2-1b/generations.jsonl
    qwen3_0_6b:
      records: 4538
      seeds: 996
      depth_dist:
        gen0: 996
        gen1: 986
        gen2: 938
        gen3: 840
        gen4: 778
      file: data/qwen3-0.6b/generations.jsonl
    qwen3_1_7b:
      records: 4617
      seeds: 996
      depth_dist:
        gen0: 996
        gen1: 983
        gen2: 941
        gen3: 875
        gen4: 822
      file: data/qwen3-1.7b/generations.jsonl
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
  status: DONE
  conclusion: success
  metrics:
    records: 2291
    seeds: 498
    depth_dist:
      '0': 498
      '1': 492
      '2': 468
      '3': 435
      '4': 398
    skipped: 199
    duration_s: 4548.2
    file_size_mb: 2.5
    file: generations_shard0.jsonl
- exp_id: plan-002-qwen17b-r2-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    records: 2326
    seeds: 498
    depth_dist:
      '0': 498
      '1': 491
      '2': 473
      '3': 440
      '4': 424
    skipped: 53
    duration_s: 4228
    file: generations_shard1.jsonl
- exp_id: plan-002-qwen06b-r2-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    records: 2270
    seeds: 498
    depth_dist:
      '0': 498
      '1': 493
      '2': 468
      '3': 423
      '4': 388
    file: generations_shard0.jsonl
- exp_id: plan-002-qwen06b-r2-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    records: 2268
    seeds: 498
    depth_dist:
      '0': 498
      '1': 493
      '2': 470
      '3': 417
      '4': 390
    file: generations_shard1.jsonl
- exp_id: plan-002-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    leave_one_out_avg_macro_f1: 0.8037
    best_held_out:
      model: pythia-1b
      macro_f1: 0.8507
    worst_held_out:
      model: olmo-2-1b
      macro_f1: 0.7519
    family_out_delta: 0.0107
    ablation_full_f1: 0.8037
    ablation_reference_only_f1: 0.7543
    ablation_surface_only_f1: 0.7471
    mcnemar_p: 0
    top_features:
    - hapax_ratio_0.289
    - ttr_0.168
    - entropy_mean_0.160
    entropy_std_drop: 0.0049
    entropy_std_drift: 0.12
    entropy_mean_drift: 1.5
- exp_id: plan-013
  name: ''
  status: DONE
  conclusion: success
  metrics:
    spearman_rho_range: '[-0.066, +0.134]'
    length_depth_correlation: weak (|ρ|<0.14)
    normalized_ttr_trend_preserved: true
    normalized_hapax_trend_preserved: true
    normalized_rho_stronger: true
    length_matched_f1_delta: '+0.041'
    length_is_confound: false
    dropout_short_text_bias: true
- exp_id: plan-003
  name: ''
  status: DONE
  conclusion: success
  metrics:
    logo_f1_pythia_ref: 0.8034
    logo_f1_olmo_ref: 0.8072
    logo_f1_qwen_ref: 0.8158
    entropy_drift_all_refs_negative: true
    olmo_ref_drift_range:
    - -0.608
    - -0.9089
    qwen_ref_drift_range:
    - -0.9557
    - -1.3458
    pythia_ref_drift_range:
    - -1.1872
    - -1.4017
    dual_dynamics_is_pythia_artifact: false
- exp_id: plan-015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    seven_feature_logo_f1: 0.798
    seven_feature_ci:
    - 0.786
    - 0.799
    avg_logprob_logo_f1: 0.7653
    avg_logprob_ci:
    - 0.616
    - 0.82
    avg_logprob_spearman: 0.7876
    ld_score_logo_f1: 0.7212
    ld_score_ci:
    - 0.588
    - 0.77
    ld_score_spearman: 0.7943
    ld_score_pre_fix: 0.6854
    fast_detect_gpt_logo_f1: 0.6269
    fast_detect_gpt_ci:
    - 0.511
    - 0.762
    fast_detect_gpt_spearman: 0.4325
    binoculars_logo_f1: 0.579
    binoculars_ci:
    - 0.405
    - 0.664
    binoculars_spearman: 0.1989
    binoculars_bug_confirmed: true
    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,
      shifted_ids)
    bootstrap_n: 1000
    bootstrap_delta_7feat_vs_avglogprob:
      delta: 0.039
      p: 0
      significant: true
    bootstrap_delta_7feat_vs_fdgpt:
      delta: 0.067
      p: 0
      significant: true
    best_single_detector: Avg-LogProb (0.7653)
    seven_feature_advantage_pp: 3.3
- exp_id: plan-004-prep
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    model: OLMo-2-0425-1B (1485M)
    datasets:
      depth0_only:
        train: 797
        test: 3138
      depth01:
        train: 3951
        test: 3138
      all:
        train: 12299
        test: 3138
      size_matched:
        train: 3951
        test: 3138
      binary_filtered:
        train: 3951
        test: 3138
    dry_run_loss: 2.18
    script: finetune_downstream.py
- exp_id: plan-003-olmo2ref
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan-003-qwen06bref
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan-014
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 4497
    unique_seeds: 995
    depth_dist:
      '0': 995
      '1': 979
      '2': 937
      '3': 831
      '4': 755
    logo_6gen_avg_f1: 0.7893
    logo_per_generator:
      olmo-2-1b: 0.7635
      pythia-1b: 0.8562
      pythia-2.8b: 0.8041
      qwen3-0.6b: 0.8243
      qwen3-1.7b: 0.8046
      qwen3-8b: 0.6832
    logo_qwen3_8b_held_out_f1: 0.6832
    logo_5gen_baseline_f1: 0.8
    spearman:
      hapax_ratio: -0.5578
      ttr: -0.5419
      entropy_mean: -0.4754
      entropy_min: -0.3029
      entropy_max: 0.0946
      tail_decay: -0.0894
      entropy_std: -0.0755
    feature_importance:
      hapax_ratio: 0.269
      entropy_mean: 0.1637
      ttr: 0.159
      entropy_max: 0.0634
      entropy_std: 0.0463
      entropy_min: 0.0153
      tail_decay: 0.0123
    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)
    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness
- exp_id: plan-004
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan-004-v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    total_runs: 15
    completed: 15
    variants:
      all:
        eval_loss_mean: 0.848
        perplexity_mean: 2.335
        seeds:
          '42':
            eval_loss: 0.848
            ppl: 2.335
          '123':
            eval_loss: 0.848
            ppl: 2.335
          '456':
            eval_loss: 0.8482
            ppl: 2.3354
      size_matched:
        eval_loss_mean: 0.8617
        perplexity_mean: 2.367
        seeds:
          '42':
            eval_loss: 0.8618
            ppl: 2.367
          '123':
            eval_loss: 0.8615
            ppl: 2.367
          '456':
            eval_loss: 0.8618
            ppl: 2.367
      depth01:
        eval_loss_mean: 0.8701
        perplexity_mean: 2.387
        seeds:
          '42':
            eval_loss: 0.8703
            ppl: 2.3877
          '123':
            eval_loss: 0.87
            ppl: 2.3869
          '456':
            eval_loss: 0.8699
            ppl: 2.387
      binary_filtered:
        eval_loss_mean: 0.8709
        perplexity_mean: 2.389
        seeds:
          '42':
            eval_loss: 0.8708
            ppl: 2.389
          '123':
            eval_loss: 0.871
            ppl: 2.389
          '456':
            eval_loss: 0.871
            ppl: 2.389
      depth0_only:
        eval_loss_mean: 0.9864
        perplexity_mean: 2.681
        seeds:
          '42':
            eval_loss: 0.9865
            ppl: 2.6818
          '123':
            eval_loss: 0.9863
            ppl: 2.68
          '456':
            eval_loss: 0.9865
            ppl: 2.6817
    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)
      << depth0_only(2.681)
    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）
- exp_id: plan-015-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    seven_feature_logo_f1: 0.798
    seven_feature_ci95:
    - 0.786
    - 0.799
    avg_logprob_logo_f1: 0.7653
    avg_logprob_ci95:
    - 0.616
    - 0.82
    ld_score_logo_f1: 0.7212
    ld_score_ci95:
    - 0.588
    - 0.77
    fastdetectgpt_logo_f1: 0.6269
    fastdetectgpt_ci95:
    - 0.511
    - 0.762
    binoculars_logo_f1: 0.579
    binoculars_ci95:
    - 0.405
    - 0.664
    binoculars_bug_fixed: true
    ld_score_corrected_cv_f1: 0.7925
    bootstrap_7feat_vs_avglogprob:
      delta: 0.039
      p: 0
      significant: true
    bootstrap_7feat_vs_fastdetectgpt:
      delta: 0.067
      p: 0
      significant: true
- exp_id: plan-005
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cv_f1:
      continuation: 0.7806
      inspired_rewriting: 0.7368
      elaboration: 0.73
    lopto_f1:
      held_out_cont: 0.762
      held_out_elab: 0.7622
      held_out_rewrite: 0.7334
      avg: 0.7525
    depth_retention_d4_d0:
      continuation: 0.831
      inspired_rewriting: 0.939
      elaboration: 0.986
    drift_hapax_ratio:
      continuation: -0.74
      elaboration: -0.828
      rewriting: -0.8
    drift_ttr:
      continuation: -0.607
      elaboration: -0.641
      rewriting: -0.618
    drift_entropy_mean:
      continuation: -0.557
      elaboration: -0.471
      rewriting: -0.477
    spearman_ttr:
      continuation: -0.629
      elaboration: -0.666
      rewriting: -0.659
    spearman_hapax:
      continuation: -0.651
      elaboration: -0.674
      rewriting: -0.67
    spearman_entropy_mean:
      continuation: -0.665
      elaboration: -0.583
      rewriting: -0.564
- exp_id: plan-005-cont
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 4620
    unique_seeds: 995
    skipped: 168
    depth_distribution:
      '0': 995
      '1': 992
      '2': 932
      '3': 874
      '4': 827
    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl
    file_size_mb: 4.93
    runtime_seconds: 7760
    speed_seeds_per_sec: 0.13
- exp_id: plan-005-elab
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 4946
    unique_seeds: 995
    skipped: 14
    depth_distribution:
      '0': 995
      '1': 995
      '2': 989
      '3': 986
      '4': 981
    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl
    file_size_mb: 5.53
    runtime_seconds: 8960.2
    depth_retention_d4_d0: 0.986
    logo_cv_f1:
      mean: 0.73
      std: 0.011
    lopto_f1: 0.7622
    feature_drift_entropy_mean: -0.4705
    feature_drift_ttr: -0.6413
    feature_drift_hapax: -0.8284
    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration
      chains more stable but depth signal weaker within-type
    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,
      elaboration slightly lower
- exp_id: plan-005-rewrite
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 4827
    unique_seeds: 995
    skipped: 61
    depth_distribution:
      '0': 995
      '1': 995
      '2': 959
      '3': 944
      '4': 934
    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl
    file_size_mb: 5.41
    runtime_seconds: 8584
    speed_seeds_per_sec: 0.12
    depth_retention_d4_d0: 0.939
    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more
      stable depth chains
- exp_id: review-exp-a-baseline-ensemble
  name: ''
  status: DONE
  conclusion: success
  metrics:
    4_baseline:
      avg_f1: 0.7964
      ci95:
      - 0.7921
      - 0.8007
    4_baseline_plus_surface:
      avg_f1: 0.8049
      ci95:
      - 0.8003
      - 0.8092
    7_feature_unified:
      avg_f1: 0.7887
      ci95:
      - 0.7839
      - 0.793
    7_feature_original:
      avg_f1: 0.7887
      ci95:
      - 0.7839
      - 0.793
- exp_id: review-exp-b-topic-drift
  name: ''
  status: DONE
  conclusion: success
  metrics:
    semantic_similarity_by_transition:
      0_to_1:
        mean: 0.622
        std: 0.1647
      1_to_2:
        mean: 0.6829
        std: 0.1837
      2_to_3:
        mean: 0.801
        std: 0.2012
      3_to_4:
        mean: 0.8587
        std: 0.1895
    prompt_type_avg_sim:
      continuation: 0.7168
      elaboration: 0.8093
      inspired_rewriting: 0.808
    shape_feature_correlations:
      entropy_std_rho: -0.1639
      tail_decay_rho: 0.0675
    drifting_feature_correlations:
      hapax_ratio_rho: -0.1242
      ttr_rho: -0.1784
      entropy_mean_rho: -0.2859
- exp_id: review-exp-c-overall-ci
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_f1_v2: 0.7878
    overall_ci95_v2:
    - 0.783
    - 0.792
    ci_width: 0.009
    pipeline: bootstrap_ci_v2.py (class-balanced downsample)
    per_gen_sanity_check:
      olmo-2-1b: 0.7649
      pythia-1b: 0.8528
      pythia-2.8b: 0.8037
      qwen3-0.6b: 0.8231
      qwen3-1.7b: 0.8064
      qwen3-8b: 0.6815
- exp_id: review-p0a-gen0-leakage
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_samples: 21557
    7_feature:
      f1: 0.7233
      ci95:
      - 0.7174
      - 0.7292
    avg_logprob:
      f1: 0.7124
      ci95:
      - 0.706
      - 0.7189
    ld_score:
      f1: 0.7009
      ci95:
      - 0.6942
      - 0.7073
    fastdetectgpt:
      f1: 0.6155
      ci95:
      - 0.6086
      - 0.6222
    binoculars:
      f1: 0.524
      ci95:
      - 0.5167
      - 0.5306
    4_baseline:
      f1: 0.7118
      ci95:
      - 0.7052
      - 0.7182
    4_baseline_surface:
      f1: 0.7239
      ci95:
      - 0.7179
      - 0.7303
- exp_id: review-p0b-volume-matched
  name: ''
  status: DONE
  conclusion: success
  metrics:
    5gen_logo_original: 0.8019
    5gen_volume_matched_avg: 0.8024
    6gen_logo_excl_qwen8b: 0.8102
    volume_effect_pp: 0.05
    diversity_residual_pp: 0.78
    diversity_pct: 94
- exp_id: review-p1c-instruct
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_records: 4963
    depths: 5
    seeds: 996
    length_depth_spearman: -0.52
    length_confound_dominates: true
    depth_signal_after_control: negligible
    length_per_depth_tokens:
      '0': 252
      '1': 79
      '2': 74
      '3': 72
      '4': 68
    original_rho:
      ttr: 0.48
      hapax: 0.477
      entropy_mean: 0.478
    length_matched_rho:
      ttr: 0.19
      hapax: 0.224
      entropy_mean: 0.042
    partial_rho:
      ttr: 0.13
      hapax: 0.166
      entropy_mean: 0.161
    binary_gen1_vs_gen2plus_f1: 0.506
- exp_id: review-p1d-table3-6gen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    avglogprob_100_3: 0.737
    avglogprob_200_6: 0.737
    fastdetectgpt_100_3: 0.688
    fastdetectgpt_200_6: 0.688
    ldscore_100_3: 0.655
    ldscore_200_6: 0.654
    binoculars_100_3: 0.416
    binoculars_200_6: 0.417
    max_hyperparam_delta: 0.0011
    hyperparam_effect: negligible
- exp_id: review-p1e-ordinal
  name: ''
  status: DONE
  conclusion: success
  metrics:
    xgboost_3class_f1: 0.7888
    coral_3class_f1: 0.7711
    frankhall_3class_f1: 0.7931
    xgboost_binary_f1: 0.7213
    coral_binary_f1: 0.7275
    xgboost_concordance: 0.821
    coral_concordance: 0.81
    frankhall_concordance: 0.825
    ordinal_benefit: negligible
    ci_overlap: true
- exp_id: review-p2f-cross-ref-bias
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pythia1b_f1_pythia410m_ref: 0.856
    pythia1b_f1_olmo_ref: 0.845
    pythia1b_f1_qwen_ref: 0.848
    same_to_cross_drop: 0.009
    pythia1b_rank_all_refs: 1
    same_family_bias: false
- exp_id: review-p1c-olmo-instruct
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    instruct_logo_f1: 0.338
    base_olmo_logo_f1: 0.763
    delta: -0.425
    n_records: 4429
    binary_logo_f1: 0.3506
    length_depth_spearman: -0.3701
    length_confound_dominates: false
    depth_signal_after_control: partially_survives
    original_rho:
      entropy_mean: 0.4822
      ttr: 0.0057
      hapax: 0.0253
    partial_rho:
      entropy_mean: 0.364
      ttr: -0.2407
      hapax: -0.1979
    entropy_reversal_survives_length_control: true
    surface_reversal: false
- exp_id: review-p1c-qwen06b-instruct
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    instruct_logo_3class_f1: 0.667
    base_logo_3class_f1: 0.816
    delta_3class: -0.148
    binary_gen1_vs_gen2plus_f1: 0.552
    length_depth_spearman: -0.583
    length_confound_dominates: true
    depth_signal_after_control: negligible
    length_per_depth_tokens:
      '0': 252
      '1': 35
      '2': 27
      '3': 24
      '4': 23
    length_matched_rho:
      ttr: -0.007
      hapax: -0.003
      entropy_mean: -0.012
- exp_id: review-rd2m7-bib-audit
  name: ''
  status: DONE
  conclusion: success
  metrics:
    diveye:
      year_correct: true
      year: 2026
      venue: TMLR
      author_fix: Varun Basani → Advik Raj Basani, Yuntian Chen → Pin-Yu Chen
    strong_model_collapse:
      year_correct: true
      year: 2025
      venue: ICLR
    aaronson_watermark:
      author_fix: Chelsea → Hendrik Kirchner
      url_added: https://scottaaronson.blog/?p=6823
- exp_id: review-sampling-ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    low_t05_p08:
      3class_f1: 0.785
      binary_f1: 0.797
      spearman_entropy_mean: -0.694
    default_t07_p09:
      3class_f1: 0.788
      binary_f1: 0.799
      spearman_entropy_mean: -0.602
    high_t10_p095:
      3class_f1: 0.726
      binary_f1: 0.733
      spearman_entropy_mean: -0.002
    f1_range_pp: 6.19
    robust: false
    finding: Low/default configs robust (<0.3pp diff). High temp (t=1.0) degrades
      depth signal ~6pp; entropy correlation drops to ~0. Qwen3-1.7B per-gen F1 collapses
      to 0.418 at high temp.
- exp_id: review-p1c-instruct-logo
  name: ''
  status: DONE
  conclusion: success
  metrics:
    7gen_logo_avg_f1: 0.7498
    7gen_binary_f1: 0.768
    6gen_base_logo_f1: 0.789
    6gen_base_binary_f1: 0.723
    instruct_held_out_3class_f1: 0.5434
    instruct_held_out_binary_f1: 0.6582
    base_qwen17b_held_out_3class_f1: 0.8023
    base_qwen17b_held_out_binary_f1: 0.8208
    instruct_vs_base_delta_3class: -0.2589
    instruct_vs_base_delta_binary: -0.1626
- exp_id: plan-010-human-edit
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline:
      3class_f1: 0.7889
      binary_f1: 0.7241
      ci_3class:
      - 0.787
      - 0.798
      ci_binary:
      - 0.719
      - 0.734
    random_5pct:
      3class_f1: 0.7538
      binary_f1: 0.7182
      delta_3class: -0.0351
      delta_binary: -0.0059
    random_10pct:
      3class_f1: 0.7425
      binary_f1: 0.7168
      delta_3class: -0.0464
      delta_binary: -0.0073
    random_20pct:
      3class_f1: 0.7292
      binary_f1: 0.7165
      delta_3class: -0.0597
      delta_binary: -0.0076
    llm_rephrase:
      3class_f1: 0.7549
      binary_f1: 0.6615
      delta_3class: -0.034
      delta_binary: -0.0626
    degradation_curve: robust
    llm_rephrase_robust: true
    finding: 'Graceful degradation: 5-20% random replacement drops 3-class F1 by 3.5-6.0pp.
      LLM rephrase: 3-class robust (-3.4pp) but binary degrades more (-6.3pp).'
- exp_id: plan-008-multi-domain
  name: ''
  status: DONE
  conclusion: success
  metrics:
    per_domain:
      news:
        3class_f1: 0.5614
        binary_f1: 0.6264
      scientific:
        3class_f1: 0.7049
        binary_f1: 0.7701
      creative:
        3class_f1: 0.6275
        binary_f1: 0.731
      wikipedia:
        3class_f1: 0.7928
        binary_f1: 0.8224
    cross_domain_pooled:
      3class_f1: 0.4775
      binary_f1: 0.6742
    wiki_transfer:
      news: 0.231
      scientific: 0.3351
      creative: 0.2319
    n_records:
      news: 2314
      scientific: 2316
      creative: 2466
    dedup_applied: true
    dedup_removed:
      news: 801
      scientific: 0
      creative: 0
- exp_id: plan-007-cross-model
  name: ''
  status: DONE
  conclusion: success
  metrics:
    3class_macro_f1: 0.8089
    3class_f1_std: 0.0166
    binary_f1_gen1_vs_gen2plus: 0.7635
    binary_f1_gen0_vs_gen2plus: 0.8372
    per_class_f1:
      gen0: 0.9285
      gen1: 0.7367
      gen2plus: 0.7614
    n_samples: 2964
    avg_generators_per_chain: 3
    feature_importance:
      hapax_ratio: 0.357
      entropy_mean: 0.204
      ttr: 0.202
    vs_single_model:
      pythia-1b: 0.8622
      qwen3-0.6b: 0.8354
      pythia-2.8b: 0.8156
      qwen3-1.7b: 0.8106
      olmo-2-1b: 0.7801
      cross-model: 0.8089
    n_samples_note: corrected from 4773 to 2964 per confusion matrix sum
- exp_id: plan-006-paraphrastic
  name: ''
  status: DONE
  conclusion: success
  metrics:
    paraphrastic_3class_f1: 0.68
    paraphrastic_3class_f1_std: 0.0086
    paraphrastic_binary_f1: 0.539
    paraphrastic_binary_f1_std: 0.017
    continuation_3class_f1: 0.788
    continuation_3class_f1_std: 0.0061
    continuation_binary_f1: 0.749
    continuation_binary_f1_std: 0.011
    f1_3class_delta: -0.108
    retention_para: 0.8915
    retention_cont: 0.8261
    retention_delta: 0.0654
    cross_transfer_para_to_cont_f1: 0.155
    cross_transfer_cont_to_para_f1: 0.431
    spearman_entropy_mean_para: 0.394
    spearman_entropy_mean_cont: -0.675
    spearman_ttr_para: 0.567
    spearman_ttr_cont: -0.633
    spearman_hapax_para: 0.556
    spearman_hapax_cont: -0.655
    spearman_signs_reversed: true
    n_paraphrastic: 4754
    n_continuation: 4609
- exp_id: plan-009-finer-ordinal
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    5class_HGBT_macro_f1: 0.5028
    5class_HGBT_f1_95ci:
    - 0.4974
    - 0.5079
    5class_HGBT_accuracy: 0.5423
    5class_HGBT_mae: 0.6587
    5class_RF_macro_f1: 0.4767
    5class_LR_macro_f1: 0.4468
    5class_FrankHall_macro_f1: 0.4513
    3class_HGBT_macro_f1: 0.7815
    3class_HGBT_f1_95ci:
    - 0.7764
    - 0.7864
    delta_5class_vs_3class: -0.2787
    5class_per_class_f1:
      depth_0: 0.9129
      depth_1: 0.6277
      depth_2: 0.2687
      depth_3: 0.2653
      depth_4: 0.4393
    gen2_gen3_inseparable: true
- exp_id: plan-012-qwen06b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    5class_macro_f1: 0.583
    5class_f1_std: 0.01
    3class_macro_f1: 0.905
    3class_f1_std: 0.003
    per_class_f1:
      gen0: 0.999
      gen1: 0.796
      gen2: 0.413
      gen3: 0.259
      gen4: 0.447
    runtime_seconds: 6928
    model: Qwen3-0.6B-Base
    method: QLoRA
    lora_rank: 16
    seed: 42
- exp_id: plan-006-confound-fix
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_paraphrastic_clean: 4912
    n_paraphrastic_contaminated_removed: 4754
    paraphrastic_3class_f1: 0.742
    paraphrastic_binary_f1: 0.671
    continuation_3class_f1: 0.788
    continuation_binary_f1: 0.749
    f1_3class_delta: -0.046
    spearman_entropy_mean_para: -0.533
    spearman_entropy_mean_cont: -0.675
    entropy_reversal_was_artifact: true
    cross_transfer_para_to_cont_f1: 0.77
    cross_transfer_cont_to_para_f1: 0.743
    depth_retention_para: 0.97
    vs_contaminated:
      old_3class_f1: 0.68
      new_3class_f1: 0.742
      old_binary_f1: 0.539
      new_binary_f1: 0.671
      old_entropy_rho: 0.394
      new_entropy_rho: -0.533
- exp_id: plan-012-pythia410m
  name: ''
  status: DONE
  conclusion: success
  metrics:
    5class_macro_f1: 0.556
    5class_f1_std: 0.016
    3class_macro_f1: 0.87
    3class_f1_std: 0.022
    per_class_f1:
      gen0: 0.991
      gen1: 0.733
      gen2: 0.347
      gen3: 0.291
      gen4: 0.42
    runtime_seconds: 3705
    model: Pythia-410M
    method: QLoRA
- exp_id: plan-012-qwen06b-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    5class_macro_f1: 0.5873
    5class_f1_std: 0.0047
    3class_macro_f1: 0.9054
    3class_f1_std: 0.0037
    per_class_5class:
      depth_0: 0.9995
      depth_1: 0.7959
      depth_2: 0.4016
      depth_3: 0.3176
      depth_4: 0.4217
    per_class_3class:
      gen0: 0.9995
      gen1: 0.7959
      gen2plus: 0.9209
    runtime_minutes: 116.7
    model: Qwen3-0.6B-Base
    method: QLoRA
    lora_rank: 32
    seed: 123
    results_file: results/plan012_qwen06b_seed123_r32_results.json
    vs_xgboost_5class_delta_pp: 8.5
    vs_xgboost_3class_delta_pp: 12.4
- exp_id: plan-016-llama32-3b
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan-016-gemma2-2b
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan-016-mistral-7b
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan-016-crossref-qwen8b
  name: ''
  status: QUEUED
  conclusion: success
  metrics:
    logo_avg_pythia_ref: 0.7891
    logo_avg_olmo_ref: 0.7948
    logo_avg_qwen_ref: 0.8135
    qwen8b_pythia_ref: 0.6854
    qwen8b_olmo_ref: 0.6962
    qwen8b_qwen_ref: 0.7568
    ci95_pythia:
    - 0.747
    - 0.824
    ci95_olmo:
    - 0.757
    - 0.828
    ci95_qwen:
    - 0.785
    - 0.842
    all_entropy_drift_negative: true
    spread_across_refs: 0.024
- exp_id: plan-016-llama32-3b-rp11
  name: ''
  status: RUNNING
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
  "promptId": "dd52a47a-ed24-4ace-b099-792192098121",
  "type": "user",
  "uuid": "c17ca41c-d8ed-457f-bc04-2efd978a6880",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T11:04:29.698Z_

```json
{
  "parentUuid": "c17ca41c-d8ed-457f-bc04-2efd978a6880",
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
  "uuid": "21f98dde-ee5a-4f8a-855e-109dcb384d84",
  "timestamp": "2026-05-16T11:04:29.698Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T11:04:29.698Z_

```json
{
  "parentUuid": "21f98dde-ee5a-4f8a-855e-109dcb384d84",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "630c3869-5465-449f-b3e8-38b186f226fa",
  "timestamp": "2026-05-16T11:04:29.698Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分新家族 depth signal 退化（类似 Qwen3-8B 模式），泛化 claim 需收窄但核心贡献不变 核心假设：['3 个新家族中 1-2 个 held-out F1 < 0.60（类似 instruct 退化但不至于 chance level）', '扩展后 LOGO binary F1…",
  "leafUuid": "630c3869-5465-449f-b3e8-38b186f226fa",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median scenario paper framing for gen-depth-fingerprint",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

### Assistant

_source line 8 · 2026-05-16T11:04:36.030Z_

I'll analyze the experiment plan and project context to generate detailed median-tier predictions for each planned experiment. Let me first check the current state of which experiments are still "planned" status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "630c3869-5465-449f-b3e8-38b186f226fa",
  "isSidechain": false,
  "requestId": "req_011Cb68vjq1tY1bcEC9Mfm1G",
  "type": "assistant",
  "uuid": "a6829832-3bb3-46ff-b826-b63e3b387223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7XXSkmdsYYqpvbdtfG9p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28725,
      "cache_read_input_tokens": 11841,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 234,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28725
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

_source line 9 · 2026-05-16T11:04:39.673Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Cmy8Lg8HC5c1MHNz5PuFKp`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan details",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_3, find and read any files related to experiment plans, especially looking for experiments with status \"planned\". Check for files like experiment_plan.yaml, experiment_plan.md, or similar. Also check for any phase1 prediction files to understand the output format expected. Search broadly - check yaml, json, md files in the root and any subdirectories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6829832-3bb3-46ff-b826-b63e3b387223",
  "isSidechain": false,
  "requestId": "req_011Cb68vjq1tY1bcEC9Mfm1G",
  "type": "assistant",
  "uuid": "3908a250-75c2-4f44-b945-3f320c1f1c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7XXSkmdsYYqpvbdtfG9p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28725,
      "cache_read_input_tokens": 11841,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 234,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28725
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

_source line 10 · 2026-05-16T11:05:12.089Z_

<details><summary>↩ Tool result · `toolu_01Cmy8Lg8HC5c1MHNz5PuFKp`</summary>

```text
Excellent! Let me compile a comprehensive report based on what I've found.

## Summary of Findings

I've found and analyzed the core experiment planning and dream simulation files for the **gen-depth-fingerprint** project. Here's what I discovered:

### Primary Experiment Plan File
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`

This file contains 15 planned experiments (plan_001 through plan_015) organized by priority:
- **P0 (Critical)**: 6 experiments (~45.5 GPU hours) - plans 001, 002, 003, 004, 013, 015
- **P1 (Important)**: 5 experiments (~48 GPU hours) - plans 005, 006, 007, 008, 014
- **P2 (Nice-to-have)**: 4 experiments (~23 GPU hours) - plans 009, 010, 011, 012

Key P0 experiments related to "planned" status:
- **plan_001**: Feature ablation (reference-model vs surface features) - essential for Claim 2 validation
- **plan_002**: Cross-generator evaluation (leave-one-out CV) - tests generalization across 5 generators
- **plan_003**: Cross-family reference model testing - marked as **DONE** in comments
- **plan_004**: Downstream utility with fine-tuning - RQ4 validation
- **plan_013**: Text length confound control - zero new generation needed
- **plan_015**: Ordinal baseline comparison - critical missing baseline (both re-dreams flagged)

### Dream Report Files (Phase1 Prediction Format)

Found **2 dream reports** with complete imagined experiment specifications:

1. **dream_20260514T181213** - Initial dream review with 3 tiers
2. **dream_20260514T221538** - Re-dream after framing repositioning with refined tiers

Each dream report contains:
- `/meta.yaml` - Metadata including tier definitions with expected number ranges for key metrics
- `/best/imagined_experiments.yaml` - Detailed expected results for best-case scenario
- `/median/` and `/worst/` directories with similar structures
- `/logs/phase1_attempt0.log` - Execution logs from phase 1

### Phase1 Prediction Output Format

The **imagined_experiments.yaml** files demonstrate the expected output structure with:

**For each experiment:**
- `name`: Experiment identifier (e.g., "feature_ablation", "cross_generator_evaluation")
- `plan_id`: Reference to experiment_plan.yaml (e.g., "plan_001")
- `description`: Detailed methodology and setup
- `expected_results`: Dictionary of numeric metrics with specific predicted values
  - E.g., `ref_only_macro_f1: 0.79`, `surface_only_macro_f1: 0.63`, `full_macro_f1: 0.87`
  - Includes error metrics: `ref_only_cv_std: 0.018`
  - Statistical tests: `mcnemar_p_ref_vs_surface: 3.0e-05`
- `result_rationale`: Detailed explanation of why results should fall in this range
- `tables`: List of expected output tables with columns and rows
- `figures_description`: List of figure descriptions for visualization
- `analysis`: Narrative interpretation

### Experiments with Status "planned"

Based on the experiment_plan.yaml, the experiments with **status "planned"** (not DONE) include:

**Definitely Planned:**
- plan_001: feature_ablation_and_trend (P0)
- plan_002: cross_generator_evaluation (P0)
- plan_004: downstream_utility (P0)
- plan_005-008: Various robustness and domain tests (P1)
- plan_009-015: Supplementary analyses (P2)

**Marked as DONE:**
- plan_003: cross_family_reference_model
- plan_010: human_edit_robustness

### Key Files Referenced

**Absolute paths to relevant files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml` - Main experiment plan
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml` - Phase1 predictions (tier: best)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml` - Phase1 predictions (tier: median)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml` - Phase1 predictions (tier: worst)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/meta.yaml` - Re-dream metadata with refined tier definitions

The dream reports provide quantitative expected ranges and narrative framing for three outcome scenarios (best/median/worst), which you can use to understand the critical success factors and anticipated challenges for the experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3908a250-75c2-4f44-b945-3f320c1f1c79",
  "isSidechain": false,
  "promptId": "dd52a47a-ed24-4ace-b099-792192098121",
  "type": "user",
  "uuid": "6c1dc551-2639-4d16-8ea0-ab64ca6c71f6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_3, find and read any files related to experiment plans, especially looking for experiments with status \"planned\". Check for files like experiment_plan.yaml, experiment_plan.md, or similar. Also check for any phase1 prediction files to understand the output format expected. Search broadly - check yaml, json, md files in the root and any subdirectories.",
    "agentId": "a5677b3571a207387",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Let me compile a comprehensive report based on what I've found.\n\n## Summary of Findings\n\nI've found and analyzed the core experiment planning and dream simulation files for the **gen-depth-fingerprint** project. Here's what I discovered:\n\n### Primary Experiment Plan File\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`\n\nThis file contains 15 planned experiments (plan_001 through plan_015) organized by priority:\n- **P0 (Critical)**: 6 experiments (~45.5 GPU hours) - plans 001, 002, 003, 004, 013, 015\n- **P1 (Important)**: 5 experiments (~48 GPU hours) - plans 005, 006, 007, 008, 014\n- **P2 (Nice-to-have)**: 4 experiments (~23 GPU hours) - plans 009, 010, 011, 012\n\nKey P0 experiments related to \"planned\" status:\n- **plan_001**: Feature ablation (reference-model vs surface features) - essential for Claim 2 validation\n- **plan_002**: Cross-generator evaluation (leave-one-out CV) - tests generalization across 5 generators\n- **plan_003**: Cross-family reference model testing - marked as **DONE** in comments\n- **plan_004**: Downstream utility with fine-tuning - RQ4 validation\n- **plan_013**: Text length confound control - zero new generation needed\n- **plan_015**: Ordinal baseline comparison - critical missing baseline (both re-dreams flagged)\n\n### Dream Report Files (Phase1 Prediction Format)\n\nFound **2 dream reports** with complete imagined experiment specifications:\n\n1. **dream_20260514T181213** - Initial dream review with 3 tiers\n2. **dream_20260514T221538** - Re-dream after framing repositioning with refined tiers\n\nEach dream report contains:\n- `/meta.yaml` - Metadata including tier definitions with expected number ranges for key metrics\n- `/best/imagined_experiments.yaml` - Detailed expected results for best-case scenario\n- `/median/` and `/worst/` directories with similar structures\n- `/logs/phase1_attempt0.log` - Execution logs from phase 1\n\n### Phase1 Prediction Output Format\n\nThe **imagined_experiments.yaml** files demonstrate the expected output structure with:\n\n**For each experiment:**\n- `name`: Experiment identifier (e.g., \"feature_ablation\", \"cross_generator_evaluation\")\n- `plan_id`: Reference to experiment_plan.yaml (e.g., \"plan_001\")\n- `description`: Detailed methodology and setup\n- `expected_results`: Dictionary of numeric metrics with specific predicted values\n  - E.g., `ref_only_macro_f1: 0.79`, `surface_only_macro_f1: 0.63`, `full_macro_f1: 0.87`\n  - Includes error metrics: `ref_only_cv_std: 0.018`\n  - Statistical tests: `mcnemar_p_ref_vs_surface: 3.0e-05`\n- `result_rationale`: Detailed explanation of why results should fall in this range\n- `tables`: List of expected output tables with columns and rows\n- `figures_description`: List of figure descriptions for visualization\n- `analysis`: Narrative interpretation\n\n### Experiments with Status \"planned\"\n\nBased on the experiment_plan.yaml, the experiments with **status \"planned\"** (not DONE) include:\n\n**Definitely Planned:**\n- plan_001: feature_ablation_and_trend (P0)\n- plan_002: cross_generator_evaluation (P0)\n- plan_004: downstream_utility (P0)\n- plan_005-008: Various robustness and domain tests (P1)\n- plan_009-015: Supplementary analyses (P2)\n\n**Marked as DONE:**\n- plan_003: cross_family_reference_model\n- plan_010: human_edit_robustness\n\n### Key Files Referenced\n\n**Absolute paths to relevant files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml` - Main experiment plan\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml` - Phase1 predictions (tier: best)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml` - Phase1 predictions (tier: median)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml` - Phase1 predictions (tier: worst)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/meta.yaml` - Re-dream metadata with refined tier definitions\n\nThe dream reports provide quantitative expected ranges and narrative framing for three outcome scenarios (best/median/worst), which you can use to understand the critical success factors and anticipated challenges for the experiments."
      }
    ],
    "totalDurationMs": 32410,
    "totalTokens": 68182,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 63839,
      "output_tokens": 1321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3018
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 1321,
          "cache_read_input_tokens": 63839,
          "cache_creation_input_tokens": 3018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3018,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 6,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "3908a250-75c2-4f44-b945-3f320c1f1c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T11:05:14.531Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DhFPiUi22J6YsXppTfy9Ya`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c1dc551-2639-4d16-8ea0-ab64ca6c71f6",
  "isSidechain": false,
  "requestId": "req_011Cb68yrxy3jnmFGGS8Dz5s",
  "type": "assistant",
  "uuid": "62d74234-1ec5-4b2d-9b75-a73dd19bbc0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAxcRxexEw5wwnD4VPTi3D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1556,
      "cache_read_input_tokens": 40566,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 40566,
          "cache_creation_input_tokens": 1556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1556
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

_source line 12 · 2026-05-16T11:05:14.545Z_

<details><summary>↩ Tool result · `toolu_01DhFPiUi22J6YsXppTfy9Ya`</summary>

```text
1	experiments:
2	  # === P0: Must-run experiments (headline results) ===
3	
4	  - id: plan_001
5	    claim: 2
6	    name: feature_ablation_and_trend
7	    description: >
8	      Three-part analysis on existing MVP data (zero new generation):
9	      (A) Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)
10	      vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold CV for each.
11	      (B) H1/H2 trend analysis: plot each feature's mean ± std across depth 0-4. Monotonic trend → H2 (divergence);
12	      plateau → H1 (convergence). Fit linear regression per feature, report slope + R².
13	      (C) Perplexity pre-validation for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets
14	      (no fine-tuning, just forward pass). If perplexity varies significantly with depth → Claim 3 signal exists.
15	    priority: P0
16	    gpu_budget_hours: 1
17	    deps: [mvp-001]
18	    notes: >
19	      Uses existing MVP data + features.csv. Critical for Claim 2.
20	      Plan B if surface-only ≈ full: reframe Claim 2 as "complementary signal" instead of "independent signal",
21	      narrative shifts to "vocabulary impoverishment as primary depth signal".
22	
23	  - id: plan_002
24	    claim: 1
25	    name: cross_generator_evaluation
26	    description: >
27	      Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),
28	      Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。)
29	      Leave-one-generator-out CV to test cross-generator generalization.
30	      1000 seeds × 5 generators × 5 depths = 25K chains.
31	    priority: P0
32	    gpu_budget_hours: 20
33	    deps: [plan_001]
34	    notes: >
35	      Only proceed if plan_001 confirms reference features have independent or complementary value.
36	      Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out evaluation in analysis.
37	      Discuss limitation in paper if Pythia holdout performance inflated by Pythia-1B in training set.
38	
39	  - id: plan_003
40	    claim: 2
41	    name: cross_family_reference_model
42	    registry_id: plan-003
43	    description: >
44	      Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for feature extraction.
45	      Addresses RC2 + critical test of Claim 2: verify entropy_mean H2 drift persists
46	      with non-Pythia reference (if drift disappears → "dual dynamics" is reference-model artifact,
47	      not generation-intrinsic). Also verify shape features remain H1 across reference models.
48	    priority: P0
49	    gpu_budget_hours: 8
50	    deps: [plan_002]
51	    notes: >
52	      DONE. Registry: plan-003 (parent), plan-003-olmo2ref, plan-003-qwen06bref.
53	      Falsification test passed: entropy drift confirmed across all 3 reference families.
54	      dual_dynamics_is_pythia_artifact: false. LOGO F1: Pythia 0.803, OLMo 0.807, Qwen 0.816.
55	
56	  - id: plan_004
57	    claim: 3
58	    name: downstream_utility
59	    registry_id: plan-004-v2
60	    description: >
61	      RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)
62	      on depth-stratified data subsets. Measure perplexity degradation on held-out test
63	      set as function of training data depth. Compare depth-aware filtering vs binary
64	      baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with
65	      bootstrap CIs. Include sample-count-matched comparison (subsample depth-filtered
66	      to match binary-filtered count) to control for data size confound.
67	    priority: P0
68	    gpu_budget_hours: 20
69	    deps: [plan_002]
70	    notes: >
71	      Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,
72	      (3) data size confound. All three addressed in updated design.
73	
74	  # === P1: Important for story completeness ===
75	
76	  - id: plan_005
77	    claim: 1
78	    name: prompt_type_comparison
79	    registry_id: plan-005
80	    description: >
81	      RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting chains.
82	      Tests whether semantic divergence from source correlates with depth signal preservation.
83	      Same 1000 seeds, Pythia-2.8B, 3 prompt types.
84	    priority: P1
85	    gpu_budget_hours: 10
86	    deps: [plan_001]
87	
88	  - id: plan_006
89	    claim: 1
90	    name: paraphrastic_comparison
91	    description: >
92	      RQ2 full: Construct parallel paraphrasing chains for direct comparison with continuation chains.
93	      Tests attractor convergence theory — do non-paraphrastic chains preserve more depth signal?
94	    priority: P1
95	    gpu_budget_hours: 8
96	    deps: [plan_005]
97	
98	  - id: plan_007
99	    claim: 1
100	    name: cross_model_chains
101	    registry_id: plan-007-cross-model
102	    description: >
103	      RQ3: Cross-model chains (different generator per depth step) vs single-model chains.
104	      More realistic scenario — web contamination involves diverse generators.
105	    priority: P1
106	    gpu_budget_hours: 12
107	    deps: [plan_002]
108	
109	  - id: plan_008
110	    claim: 1
111	    name: multi_domain_seeds
112	    registry_id: plan-008-multi-domain
113	    description: >
114	      Expand seeds to 3 domains: news (CNN/DailyMail), scientific (arXiv abstracts via
115	      ccdv/arxiv-summarization), creative writing (WritingPrompts). 500 seeds per domain × 5 depths.
116	      Wikipedia used as transfer evaluation target (not a seed domain).
117	      Single generator: Pythia-2.8B only (initial domain robustness validation).
118	    priority: P1
119	    gpu_budget_hours: 10
120	    deps: [plan_002]
121	    notes: >
122	      Original plan said "S2ORC abstracts" but script uses ccdv/arxiv-summarization
123	      (arXiv paper abstracts, more accessible on HuggingFace). Both are scientific text.
124	      Wikipedia moved from seed domain to cross-domain transfer evaluation target.
125	      Single-generator (Pythia-2.8B) limits claim scope — cannot directly support
126	      "across domains AND generators" without multi-generator follow-up.
127	
128	  # === P2: Nice-to-have / strengthen claims ===
129	
130	  - id: plan_009
131	    claim: 1
132	    name: finer_grained_ordinal
133	    description: >
134	      Secondary analysis: 5-class ordinal classification (gen-0 through gen-4)
135	      on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.
136	    priority: P2
137	    gpu_budget_hours: 1
138	    deps: [plan_002]
139	
140	  - id: plan_010
141	    claim: 1
142	    name: human_edit_robustness
143	    registry_id: plan-010-human-edit
144	    description: >
145	      RC5: Robustness to simulated human edits.
146	      (A) Random word replacement (5%, 10%, 20%) as lower-bound.
147	      (B) LLM-simulated editing (light rephrasing of random sentences).
148	    priority: P2
149	    gpu_budget_hours: 5
150	    deps: [plan_002]
151	    notes: >
152	      DONE/success. Graceful degradation: 5-20% random replacement -3.5 to -6.0pp 3-class,
153	      binary nearly unchanged. LLM rephrase: 3-class -3.4pp, binary -6.3pp.
154	
155	  - id: plan_011
156	    claim: 2
157	    name: ld_score_feature
158	    registry_id: review-exp-a-baseline-ensemble
159	    description: >
160	      Add LD-Score (character-distribution signature from arXiv:2605.01647) as additional feature.
161	      Tests whether character-level features provide complementary depth signal.
162	    priority: P2
163	    gpu_budget_hours: 2
164	    deps: [plan_001]
165	    notes: >
166	      Subsumed by plan-015 + review-exp-a-baseline-ensemble. LD-Score evaluated as
167	      standalone baseline (3class=0.655, binary=0.701) and in multi-detector ensemble
168	      (4-det+surface: 3class=0.805, binary=0.724). No separate plan_011 run needed.
169	
170	  - id: plan_012
171	    claim: 1
172	    name: end_to_end_classifier
173	    description: >
174	      QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.
175	      Compares learned representations vs handcrafted distributional features.
176	    priority: P2
177	    gpu_budget_hours: 15
178	    deps: [plan_002]
179	
180	  - id: plan_013
181	    claim: [1, 2]
182	    name: text_length_control
183	    registry_id: plan-013
184	    description: >
185	      Address text length confound (RC10, dream all three tiers):
186	      (A) Analyze text length distributions by depth across all generators.
187	      (B) Compute length-normalized surface features (TTR, hapax_ratio on fixed-length windows).
188	      (C) Length-matched comparison: subsample to equalize length distributions across depths,
189	      re-evaluate classifier. If length-controlled F1 drops significantly → surface features
190	      were tracking length, not depth.
191	    priority: P0
192	    gpu_budget_hours: 0.5
193	    deps: [plan_002]
194	    notes: >
195	      Zero new generation — analysis on existing data. Critical confound control
196	      flagged by dream (all three tiers). Low cost, high impact on paper credibility.
197	
198	  - id: plan_014
199	    claim: 1
200	    name: large_scale_generator
201	    registry_id: plan-014
202	    description: >
203	      Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth signal
204	      persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current
205	      generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).
206	    priority: P1
207	    gpu_budget_hours: 8
208	    deps: [plan_002]
209	    notes: >
210	      Dream review flagged ≤2.8B as major limitation (all three tiers).
211	      If depth signal weaker at scale → honest limitation with analysis.
212	      If comparable → strong generalization evidence for the paper.
213	
214	  - id: plan_015
215	    claim: 1
216	    name: ordinal_baseline_comparison
217	    registry_id: plan-015
218	    description: >
219	      CRITICAL missing baseline (flagged by both re-dreams, all three tiers):
220	      Test whether existing detector continuous scores already provide ordinal depth signal.
221	      Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation depth.
222	      Compare single-feature ordinal classifiers (each detector score as sole feature) vs
223	      our 7-feature model. If existing detectors yield comparable ordinal signal, our
224	      custom feature set contribution collapses.
225	    priority: P0
226	    gpu_budget_hours: 3
227	    deps: [plan_002]
228	    notes: >
229	      Re-dream consensus: without this comparison, reviewers will question whether
230	      depth-specific features add value. Must be in the paper. FastDetectGPT needs
231	      model pair (source + reference), LD-Score is character-level, Binoculars needs
232	      two models. If any single detector achieves >0.70 ordinal F1, we need to
233	      reframe our contribution as "complementary to existing detectors" not "novel approach."
234	
235	# Global requirements (D006+D007):
236	# - ALL experiments must report bootstrap CIs on main metrics
237	# - Use individual-level Spearman ρ (not R² on aggregated means) for trend analysis
238	# - Report realistic performance range, not just best-case
239	
240	# GPU Budget Summary:
241	# P0: ~45.5 GPU·hours (was 44, +0.5 text_length, +5 downstream seeds)
242	# P1: ~48 GPU·hours (was 40, +8 large_scale_generator)
243	# P2: ~23 GPU·hours
244	# Total: ~116.5 GPU·hours (within 200 H100-hour budget)
245	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62d74234-1ec5-4b2d-9b75-a73dd19bbc0f",
  "isSidechain": false,
  "promptId": "dd52a47a-ed24-4ace-b099-792192098121",
  "type": "user",
  "uuid": "62e779c6-977d-409d-8ab3-6fa5a59c4863",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml",
      "content": "experiments:\n  # === P0: Must-run experiments (headline results) ===\n\n  - id: plan_001\n    claim: 2\n    name: feature_ablation_and_trend\n    description: >\n      Three-part analysis on existing MVP data (zero new generation):\n      (A) Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n      vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold CV for each.\n      (B) H1/H2 trend analysis: plot each feature's mean ± std across depth 0-4. Monotonic trend → H2 (divergence);\n      plateau → H1 (convergence). Fit linear regression per feature, report slope + R².\n      (C) Perplexity pre-validation for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets\n      (no fine-tuning, just forward pass). If perplexity varies significantly with depth → Claim 3 signal exists.\n    priority: P0\n    gpu_budget_hours: 1\n    deps: [mvp-001]\n    notes: >\n      Uses existing MVP data + features.csv. Critical for Claim 2.\n      Plan B if surface-only ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n      narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n  - id: plan_002\n    claim: 1\n    name: cross_generator_evaluation\n    description: >\n      Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n      Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。)\n      Leave-one-generator-out CV to test cross-generator generalization.\n      1000 seeds × 5 generators × 5 depths = 25K chains.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [plan_001]\n    notes: >\n      Only proceed if plan_001 confirms reference features have independent or complementary value.\n      Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out evaluation in analysis.\n      Discuss limitation in paper if Pythia holdout performance inflated by Pythia-1B in training set.\n\n  - id: plan_003\n    claim: 2\n    name: cross_family_reference_model\n    registry_id: plan-003\n    description: >\n      Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for feature extraction.\n      Addresses RC2 + critical test of Claim 2: verify entropy_mean H2 drift persists\n      with non-Pythia reference (if drift disappears → \"dual dynamics\" is reference-model artifact,\n      not generation-intrinsic). Also verify shape features remain H1 across reference models.\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [plan_002]\n    notes: >\n      DONE. Registry: plan-003 (parent), plan-003-olmo2ref, plan-003-qwen06bref.\n      Falsification test passed: entropy drift confirmed across all 3 reference families.\n      dual_dynamics_is_pythia_artifact: false. LOGO F1: Pythia 0.803, OLMo 0.807, Qwen 0.816.\n\n  - id: plan_004\n    claim: 3\n    name: downstream_utility\n    registry_id: plan-004-v2\n    description: >\n      RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n      on depth-stratified data subsets. Measure perplexity degradation on held-out test\n      set as function of training data depth. Compare depth-aware filtering vs binary\n      baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with\n      bootstrap CIs. Include sample-count-matched comparison (subsample depth-filtered\n      to match binary-filtered count) to control for data size confound.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [plan_002]\n    notes: >\n      Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n      (3) data size confound. All three addressed in updated design.\n\n  # === P1: Important for story completeness ===\n\n  - id: plan_005\n    claim: 1\n    name: prompt_type_comparison\n    registry_id: plan-005\n    description: >\n      RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting chains.\n      Tests whether semantic divergence from source correlates with depth signal preservation.\n      Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan_001]\n\n  - id: plan_006\n    claim: 1\n    name: paraphrastic_comparison\n    description: >\n      RQ2 full: Construct parallel paraphrasing chains for direct comparison with continuation chains.\n      Tests attractor convergence theory — do non-paraphrastic chains preserve more depth signal?\n    priority: P1\n    gpu_budget_hours: 8\n    deps: [plan_005]\n\n  - id: plan_007\n    claim: 1\n    name: cross_model_chains\n    registry_id: plan-007-cross-model\n    description: >\n      RQ3: Cross-model chains (different generator per depth step) vs single-model chains.\n      More realistic scenario — web contamination involves diverse generators.\n    priority: P1\n    gpu_budget_hours: 12\n    deps: [plan_002]\n\n  - id: plan_008\n    claim: 1\n    name: multi_domain_seeds\n    registry_id: plan-008-multi-domain\n    description: >\n      Expand seeds to 3 domains: news (CNN/DailyMail), scientific (arXiv abstracts via\n      ccdv/arxiv-summarization), creative writing (WritingPrompts). 500 seeds per domain × 5 depths.\n      Wikipedia used as transfer evaluation target (not a seed domain).\n      Single generator: Pythia-2.8B only (initial domain robustness validation).\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan_002]\n    notes: >\n      Original plan said \"S2ORC abstracts\" but script uses ccdv/arxiv-summarization\n      (arXiv paper abstracts, more accessible on HuggingFace). Both are scientific text.\n      Wikipedia moved from seed domain to cross-domain transfer evaluation target.\n      Single-generator (Pythia-2.8B) limits claim scope — cannot directly support\n      \"across domains AND generators\" without multi-generator follow-up.\n\n  # === P2: Nice-to-have / strengthen claims ===\n\n  - id: plan_009\n    claim: 1\n    name: finer_grained_ordinal\n    description: >\n      Secondary analysis: 5-class ordinal classification (gen-0 through gen-4)\n      on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n    priority: P2\n    gpu_budget_hours: 1\n    deps: [plan_002]\n\n  - id: plan_010\n    claim: 1\n    name: human_edit_robustness\n    registry_id: plan-010-human-edit\n    description: >\n      RC5: Robustness to simulated human edits.\n      (A) Random word replacement (5%, 10%, 20%) as lower-bound.\n      (B) LLM-simulated editing (light rephrasing of random sentences).\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [plan_002]\n    notes: >\n      DONE/success. Graceful degradation: 5-20% random replacement -3.5 to -6.0pp 3-class,\n      binary nearly unchanged. LLM rephrase: 3-class -3.4pp, binary -6.3pp.\n\n  - id: plan_011\n    claim: 2\n    name: ld_score_feature\n    registry_id: review-exp-a-baseline-ensemble\n    description: >\n      Add LD-Score (character-distribution signature from arXiv:2605.01647) as additional feature.\n      Tests whether character-level features provide complementary depth signal.\n    priority: P2\n    gpu_budget_hours: 2\n    deps: [plan_001]\n    notes: >\n      Subsumed by plan-015 + review-exp-a-baseline-ensemble. LD-Score evaluated as\n      standalone baseline (3class=0.655, binary=0.701) and in multi-detector ensemble\n      (4-det+surface: 3class=0.805, binary=0.724). No separate plan_011 run needed.\n\n  - id: plan_012\n    claim: 1\n    name: end_to_end_classifier\n    description: >\n      QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n      Compares learned representations vs handcrafted distributional features.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [plan_002]\n\n  - id: plan_013\n    claim: [1, 2]\n    name: text_length_control\n    registry_id: plan-013\n    description: >\n      Address text length confound (RC10, dream all three tiers):\n      (A) Analyze text length distributions by depth across all generators.\n      (B) Compute length-normalized surface features (TTR, hapax_ratio on fixed-length windows).\n      (C) Length-matched comparison: subsample to equalize length distributions across depths,\n      re-evaluate classifier. If length-controlled F1 drops significantly → surface features\n      were tracking length, not depth.\n    priority: P0\n    gpu_budget_hours: 0.5\n    deps: [plan_002]\n    notes: >\n      Zero new generation — analysis on existing data. Critical confound control\n      flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n  - id: plan_014\n    claim: 1\n    name: large_scale_generator\n    registry_id: plan-014\n    description: >\n      Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth signal\n      persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n      generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n    priority: P1\n    gpu_budget_hours: 8\n    deps: [plan_002]\n    notes: >\n      Dream review flagged ≤2.8B as major limitation (all three tiers).\n      If depth signal weaker at scale → honest limitation with analysis.\n      If comparable → strong generalization evidence for the paper.\n\n  - id: plan_015\n    claim: 1\n    name: ordinal_baseline_comparison\n    registry_id: plan-015\n    description: >\n      CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n      Test whether existing detector continuous scores already provide ordinal depth signal.\n      Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation depth.\n      Compare single-feature ordinal classifiers (each detector score as sole feature) vs\n      our 7-feature model. If existing detectors yield comparable ordinal signal, our\n      custom feature set contribution collapses.\n    priority: P0\n    gpu_budget_hours: 3\n    deps: [plan_002]\n    notes: >\n      Re-dream consensus: without this comparison, reviewers will question whether\n      depth-specific features add value. Must be in the paper. FastDetectGPT needs\n      model pair (source + reference), LD-Score is character-level, Binoculars needs\n      two models. If any single detector achieves >0.70 ordinal F1, we need to\n      reframe our contribution as \"complementary to existing detectors\" not \"novel approach.\"\n\n# Global requirements (D006+D007):\n# - ALL experiments must report bootstrap CIs on main metrics\n# - Use individual-level Spearman ρ (not R² on aggregated means) for trend analysis\n# - Report realistic performance range, not just best-case\n\n# GPU Budget Summary:\n# P0: ~45.5 GPU·hours (was 44, +0.5 text_length, +5 downstream seeds)\n# P1: ~48 GPU·hours (was 40, +8 large_scale_generator)\n# P2: ~23 GPU·hours\n# Total: ~116.5 GPU·hours (within 200 H100-hour budget)\n",
      "numLines": 245,
      "startLine": 1,
      "totalLines": 245
    }
  },
  "sourceToolAssistantUUID": "62d74234-1ec5-4b2d-9b75-a73dd19bbc0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-16T11:05:14.614Z_

````json
{
  "parentUuid": "62e779c6-977d-409d-8ab3-6fa5a59c4863",
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
  "uuid": "f37aa3a8-f560-40ec-8ccd-84746c9ee5a3",
  "timestamp": "2026-05-16T11:05:14.614Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分新家族 depth signal 退化（类似 Qwen3-8B 模式），泛化 claim 需收窄但核心贡献不变 核心假设：['3 个新家族中 1-2 个 held-out F1 < 0.60（类似 instruct 退化但不至于 chance level）', '扩展后 LOGO binary F1…",
  "leafUuid": "f37aa3a8-f560-40ec-8ccd-84746c9ee5a3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Median scenario paper framing for gen-depth-fingerprint",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

### Assistant

_source line 16 · 2026-05-16T11:05:42.538Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me look at the existing dream reports to understand the format and the actual results we already have. Let me also check the current experiment status more carefully.

Based on the user's prompt, I need to generate median-tier predictions for each **planned** experiment. Looking at the experiment_plan from the CLAUDE.md context:

The experiments with status "planned" are:
1. plan_001 - feature_ablation_and_trend (planned)
2. plan_002 - cross_generator_evaluation (planned)
3. plan_006 - paraphrastic_comparison (planned)
4. plan_009 - finer_grained_ordinal (planned)


5. plan_012 - end_to_end_classifier (planned)

But I'm noticing a discrepancy — the registry data in the user's message shows some of these experiments already have DONE status, so I need to reconcile what the experiment_plan yaml says versus what's actually in the registry. I see the discrepancy now — the registry shows these experiments are actually complete with results, but the experiment_plan.yaml still marks them as "planned". Let me check which ones actually need predictions by looking at the status field in the experiment_plan itself rather than relying on the registry. I see—this is a dreaming exercise where I'm predicting results for the planned experiments under a median tier scenario, even though the registry shows they're already completed. The experiment_plan status was frozen at an earlier point, and I need to generate predictions based on the median performance characteristics: binary LOGO F1 around 0.68-0.72, per-generation F1 standard deviation of 0.07-0.11, worst single generation F1 between 0.50-0.62, and various other metrics for feature performance and generalization. Now I'm going to work through each of the planned experiments (plan_001, plan_002, plan_006, plan_009, plan_012) and construct what their dream results would look like under these median conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f37aa3a8-f560-40ec-8ccd-84746c9ee5a3",
  "isSidechain": false,
  "requestId": "req_011Cb68z3mMJb6EHvytMpbQT",
  "type": "assistant",
  "uuid": "677f8452-9658-40f1-bec9-b56190c24ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PxhgjSkfDrdihXZ5U4y9tg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8822,
      "cache_read_input_tokens": 42122,
      "output_tokens": 1262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1262,
          "cache_read_input_tokens": 42122,
          "cache_creation_input_tokens": 8822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8822
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

_source line 17 · 2026-05-16T11:05:42.539Z_

Let me check the existing dream report format for reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "677f8452-9658-40f1-bec9-b56190c24ebc",
  "isSidechain": false,
  "requestId": "req_011Cb68z3mMJb6EHvytMpbQT",
  "type": "assistant",
  "uuid": "b4f78997-6d36-44cb-949e-e2afeac9eb5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PxhgjSkfDrdihXZ5U4y9tg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8822,
      "cache_read_input_tokens": 42122,
      "output_tokens": 1262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1262,
          "cache_read_input_tokens": 42122,
          "cache_creation_input_tokens": 8822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8822
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

_source line 18 · 2026-05-16T11:05:42.565Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Vfnu7zjDnM2SQswxDjCQ1R`</summary>

```json
{
  "pattern": "**/dream_reports/**/imagined_experiments.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4f78997-6d36-44cb-949e-e2afeac9eb5b",
  "isSidechain": false,
  "requestId": "req_011Cb68z3mMJb6EHvytMpbQT",
  "type": "assistant",
  "uuid": "3621bcaa-595f-4061-b62e-3a619721330d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PxhgjSkfDrdihXZ5U4y9tg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8822,
      "cache_read_input_tokens": 42122,
      "output_tokens": 1262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1262,
          "cache_read_input_tokens": 42122,
          "cache_creation_input_tokens": 8822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8822
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

_source line 19 · 2026-05-16T11:05:42.586Z_

<details><summary>↩ Tool result · `toolu_01Vfnu7zjDnM2SQswxDjCQ1R`</summary>

```text
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3621bcaa-595f-4061-b62e-3a619721330d",
  "isSidechain": false,
  "promptId": "dd52a47a-ed24-4ace-b099-792192098121",
  "type": "user",
  "uuid": "45eb405f-1b73-492d-8531-2021f90104e5",
  "toolUseResult": {
    "filenames": [
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/best/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/worst/imagined_experiments.yaml"
    ],
    "durationMs": 16,
    "numFiles": 6,
    "truncated": false
  },
  "sourceToolAssistantUUID": "3621bcaa-595f-4061-b62e-3a619721330d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T11:05:45.071Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B7X3fqBgj732f3pbny5rC4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45eb405f-1b73-492d-8531-2021f90104e5",
  "isSidechain": false,
  "requestId": "req_011Cb6927SRK7nQD4F5RwjLa",
  "type": "assistant",
  "uuid": "d47f2260-d971-41c2-96f1-1e75a7e03fc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjLR63gt9JTmDs32X9rR7w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 50944,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 50944,
          "cache_creation_input_tokens": 1465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1465
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

_source line 21 · 2026-05-16T11:05:45.350Z_

<details><summary>↩ Tool result · `toolu_01B7X3fqBgj732f3pbny5rC4`</summary>

```text
1	tier: median
2	narrative_guidance: 'Depth discriminability holds within-generator (F1 0.82) but cross-generator
3	  generalization is moderate (LOGO F1 ~0.64), with performance drops concentrated
4	  on out-of-family holdouts. Dual dynamics is real but reference-model-modulated:
5	  entropy_mean drift attenuates to |ρ|~0.4 with non-Pythia references, requiring the
6	  paper to present the H1/H2 split as ''reference-model-modulated dual dynamics''
7	  rather than a universal law. Length confound is partial — surface feature F1 drops
8	  ~0.05 after length control, but residual signal confirms depth is not reducible
9	  to length. 7B+ signal weakens (F1 ~0.57) but persists, motivating future work on
10	  scale-robust features. Downstream filtering offers complementary signal but CIs
11	  overlap with best binary baseline on some metrics. Paper reframed: ''depth estimation
12	  is feasible and useful, with initial evidence for dual dynamics'' rather than ''dual
13	  dynamics as general principle.'' Still viable for AAAI/EMNLP as empirical contribution
14	  with honest limitations.
15	
16	  '
17	imagined_experiments:
18	- name: feature_ablation_and_trend
19	  plan_id: plan_001
20	  description: 'Feature ablation (full / surface-only / reference-only) + H1/H2 trend
21	    analysis on MVP data (Pythia-2.8B generator, Pythia-410M reference). Perplexity
22	    pre-validation for Claim 3.
23	
24	    '
25	  expected_results:
26	    full_macro_f1: 0.82
27	    surface_only_f1: 0.76
28	    reference_only_f1: 0.72
29	    full_vs_surface_gap: 0.06
30	    full_vs_reference_gap: 0.1
31	    bootstrap_ci_full: '[0.804, 0.836]'
32	    bootstrap_ci_surface: '[0.747, 0.774]'
33	    bootstrap_ci_reference: '[0.706, 0.733]'
34	    h2_entropy_mean_slope: -0.148
35	    h2_entropy_mean_r2: 0.93
36	    h2_ttr_slope: -0.071
37	    h2_ttr_r2: 0.87
38	    h2_hapax_ratio_slope: -0.054
39	    h2_hapax_ratio_r2: 0.81
40	    h1_entropy_std_slope: 0.003
41	    h1_entropy_std_r2: 0.02
42	    h1_entropy_max_slope: -0.009
43	    h1_entropy_max_r2: 0.04
44	    h1_tail_decay_slope: 0.005
45	    h1_tail_decay_r2: 0.03
46	    h1_entropy_min_slope: -0.012
47	    h1_entropy_min_r2: 0.06
48	    median_ppl_by_depth:
49	    - 13.5
50	    - 4.96
51	    - 3.0
52	    - 2.07
53	    - 1.72
54	    ppl_kruskal_wallis_p: <0.001
55	  result_rationale: 'Within-generator results remain strong because Pythia-410M reference
56	    model is architecturally aligned with the Pythia-2.8B generator, maximizing NLL
57	    feature sensitivity. The 0.06 full-surface gap confirms reference features add
58	    independent value — entropy_mean captures distributional compression that surface
59	    statistics miss. H2 features (entropy_mean, TTR, hapax_ratio) drift because recursive
60	    generation compounds vocabulary impoverishment and entropy compression — each
61	    step feeds an increasingly constrained output distribution back as input. H1 features
62	    (shape statistics like entropy_std, tail_decay) remain stable because distributional
63	    shape is determined by the generator''s softmax geometry, not the input content
64	    — recursive generation shifts the location (mean) of the NLL distribution but
65	    not its spread or tail behavior. Perplexity shows steep monotonic decline because
66	    deeper generations become more predictable to the reference model as they converge
67	    toward the generator''s mode.
68	
69	    '
70	  tables:
71	  - name: 'Table 1: Feature Ablation (5-fold CV, Pythia-2.8B, N=4609)'
72	    columns:
73	    - feature_set
74	    - macro_f1
75	    - 95% CI
76	    - gen0_f1
77	    - gen1_f1
78	    - gen2plus_f1
79	    rows:
80	    - - Full (7 features)
81	      - 0.82
82	      - '[0.804, 0.836]'
83	      - 0.94
84	      - 0.77
85	      - 0.79
86	    - - Surface only (TTR + hapax)
87	      - 0.76
88	      - '[0.747, 0.774]'
89	      - 0.91
90	      - 0.7
91	      - 0.72
92	    - - Reference only (5 NLL)
93	      - 0.72
94	      - '[0.706, 0.733]'
95	      - 0.88
96	      - 0.65
97	      - 0.67
98	    - - Chance baseline
99	      - 0.33
100	      - —
101	      - 0.33
102	      - 0.33
103	      - 0.33
104	  - name: 'Table 2: H1/H2 Trend Regression per Feature'
105	    columns:
106	    - feature
107	    - slope
108	    - R²
109	    - p_value
110	    - classification
111	    rows:
112	    - - entropy_mean
113	      - -0.148
114	      - 0.93
115	      - <0.001
116	      - H2 (drift)
117	    - - TTR
118	      - -0.071
119	      - 0.87
120	      - <0.001
121	      - H2 (drift)
122	    - - hapax_ratio
123	      - -0.054
124	      - 0.81
125	      - <0.001
126	      - H2 (drift)
127	    - - entropy_std
128	      - 0.003
129	      - 0.02
130	      - 0.41
131	      - H1 (stationary)
132	    - - entropy_max
133	      - -0.009
134	      - 0.04
135	      - 0.28
136	      - H1 (stationary)
137	    - - tail_decay
138	      - 0.005
139	      - 0.03
140	      - 0.33
141	      - H1 (stationary)
142	    - - entropy_min
143	      - -0.012
144	      - 0.06
145	      - 0.19
146	      - H1 (stationary)
147	  figures_description:
148	  - 'Fig 1: 7-panel feature trend plot (mean ± std) across depths 0-4. H2 features
149	    show clear monotonic decline; H1 features show flat profiles with overlapping
150	    error bands. Visual separation between H1 and H2 behavior is stark.'
151	  - 'Fig 2: Perplexity distribution boxplots by depth (0-4). Dramatic compression
152	    from depth 0 (median 13.5) to depth 4 (median 1.72), confirming depth-correlated
153	    distributional shift.'
154	  analysis: 'Results confirm the H1/H2 split on MVP data. The 0.06 full-vs-surface
155	    gap is statistically significant (bootstrap CIs non-overlapping), establishing
156	    that reference features capture complementary signal. However, this is within-generator
157	    with same-family reference model — the gap''s robustness must be tested cross-generator
158	    (plan_002) and cross-reference (plan_003). The steep perplexity gradient validates
159	    Claim 3''s premise: depth correlates with distributional properties detectable
160	    by a reference model.
161	
162	    '
163	- name: cross_generator_evaluation
164	  plan_id: plan_002
165	  description: '5-generator LOGO evaluation: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B,
166	    Qwen3-0.6B. 1000 seeds per generator × 5 depths. Leave-one-generator-out and leave-one-family-out
167	    CV.
168	
169	    '
170	  expected_results:
171	    logo_mean_macro_f1: 0.64
172	    logo_holdout_pythia28b_f1: 0.71
173	    logo_holdout_pythia1b_f1: 0.72
174	    logo_holdout_olmo2_f1: 0.6
175	    logo_holdout_qwen17b_f1: 0.62
176	    logo_holdout_qwen06b_f1: 0.59
177	    lofo_holdout_pythia_family_f1: 0.58
178	    lofo_holdout_olmo_family_f1: 0.61
179	    lofo_holdout_qwen_family_f1: 0.59
180	    lofo_mean_f1: 0.593
181	    within_generator_pooled_5fold_f1: 0.78
182	    logo_full_feature_f1: 0.64
183	    logo_surface_only_f1: 0.61
184	    logo_reference_only_f1: 0.58
185	    logo_full_vs_surface_gap: 0.03
186	    logo_full_vs_reference_gap: 0.06
187	    total_chains_generated: 23847
188	    total_chains_after_attrition: 21503
189	  result_rationale: 'Cross-generator F1 drops from 0.82 (within-generator) to 0.64
190	    (LOGO) because each generator family imprints family-specific distributional signatures
191	    beyond the depth signal. Pythia holdouts score higher (0.71-0.72) because Pythia-1B
192	    and Pythia-2.8B share architectural biases (tokenizer, attention patterns, pretraining
193	    data overlap) — when one is held out, the other provides a close proxy in the
194	    training set. OLMo and Qwen holdouts score lower (0.59-0.62) because they represent
195	    genuinely out-of-distribution generator families with different tokenizers and
196	    pretraining distributions. The full-vs-surface gap narrows from 0.06 to 0.03 because
197	    reference features (computed with Pythia-410M) are partially Pythia-biased: they
198	    extract richer signal from Pythia-generated text than from OLMo/Qwen-generated
199	    text, eroding their cross-family advantage. Leave-one-family-out results (mean
200	    0.593) are lower than LOGO (0.64) because LOGO benefits from same-family generators
201	    remaining in training. The within-generator pooled F1 (0.78) is lower than MVP''s
202	    0.82 because pooling heterogeneous generators introduces inter-generator variance
203	    that the classifier must absorb.
204	
205	    '
206	  tables:
207	  - name: 'Table 3: Leave-One-Generator-Out Results (Full Features)'
208	    columns:
209	    - held_out_generator
210	    - family
211	    - macro_f1
212	    - gen0_f1
213	    - gen1_f1
214	    - gen2plus_f1
215	    rows:
216	    - - Pythia-2.8B
217	      - Pythia
218	      - 0.71
219	      - 0.87
220	      - 0.64
221	      - 0.66
222	    - - Pythia-1B
223	      - Pythia
224	      - 0.72
225	      - 0.88
226	      - 0.66
227	      - 0.67
228	    - - OLMo-2-1B
229	      - OLMo
230	      - 0.6
231	      - 0.79
232	      - 0.51
233	      - 0.53
234	    - - Qwen3-1.7B
235	      - Qwen
236	      - 0.62
237	      - 0.82
238	      - 0.53
239	      - 0.55
240	    - - Qwen3-0.6B
241	      - Qwen
242	      - 0.59
243	      - 0.78
244	      - 0.5
245	      - 0.51
246	    - - Mean LOGO
247	      - —
248	      - 0.64
249	      - 0.83
250	      - 0.57
251	      - 0.58
252	  - name: 'Table 4: Leave-One-Family-Out Results'
253	    columns:
254	    - held_out_family
255	    - generators_in_family
256	    - macro_f1
257	    - 95% CI
258	    rows:
259	    - - Pythia
260	      - 2.8B + 1B
261	      - 0.58
262	      - '[0.55, 0.61]'
263	    - - OLMo
264	      - OLMo-2-1B
265	      - 0.61
266	      - '[0.57, 0.64]'
267	    - - Qwen
268	      - 1.7B + 0.6B
269	      - 0.59
270	      - '[0.56, 0.62]'
271	  - name: 'Table 5: Feature Ablation in Cross-Generator Setting (LOGO)'
272	    columns:
273	    - feature_set
274	    - logo_macro_f1
275	    - gap_vs_full
276	    rows:
277	    - - Full
278	      - 0.64
279	      - —
280	    - - Surface only
281	      - 0.61
282	      - -0.03
283	    - - Reference only
284	      - 0.58
285	      - -0.06
286	  figures_description:
287	  - 'Fig 3: LOGO F1 heatmap — rows are held-out generators, columns are depth classes
288	    (gen-0/1/2+). Clear diagonal pattern: within-family holdouts (Pythia-2.8B, Pythia-1B)
289	    are warmer; cross-family (OLMo, Qwen) are cooler, especially for gen-1 and gen-2+.'
290	  - 'Fig 4: Confusion matrices for best (Pythia-1B holdout, F1=0.72) and worst (Qwen-0.6B
291	    holdout, F1=0.59) LOGO folds. Worst case shows gen-1/gen-2+ confusion concentrated
292	    in cross-family.'
293	  analysis: 'LOGO F1=0.64 is within the median range [0.58, 0.70] and confirms moderate
294	    cross-generator generalization. The within-family vs cross-family gap (~0.12)
295	    reveals that distributional features partially encode generator identity, not
296	    just depth. This constrains Claim 1 to ''depth discriminability generalizes within
297	    model family; cross-family generalization is moderate and requires further work.''
298	    The narrowing full-vs-surface gap (0.03 vs 0.06 within-generator) suggests reference
299	    features lose their relative advantage in the cross-generator setting — likely
300	    because the Pythia-410M reference model is better calibrated for Pythia-family
301	    generators. This motivates plan_003 to test non-Pythia reference models.
302	
303	    '
304	- name: cross_family_reference_model
305	  plan_id: plan_003
306	  description: 'Recompute NLL features using non-Pythia reference models (OLMo-2-1B,
307	    Qwen3-0.6B) on existing plan_002 data. Test whether entropy_mean H2 drift and
308	    shape feature H1 stationarity persist. Key falsification test for Claim 2.
309	
310	    '
311	  expected_results:
312	    pythia410m_ref_entropy_mean_rho: -0.68
313	    olmo2_ref_entropy_mean_rho: -0.42
314	    qwen06b_ref_entropy_mean_rho: -0.36
315	    pythia410m_ref_full_f1: 0.82
316	    olmo2_ref_full_f1: 0.78
317	    qwen06b_ref_full_f1: 0.76
318	    olmo2_ref_shape_max_abs_rho: 0.11
319	    qwen06b_ref_shape_max_abs_rho: 0.09
320	    pythia410m_ref_shape_max_abs_rho: 0.08
321	    olmo2_ref_entropy_std_rho: 0.06
322	    olmo2_ref_tail_decay_rho: -0.11
323	    qwen06b_ref_entropy_std_rho: -0.04
324	    qwen06b_ref_tail_decay_rho: 0.09
325	    cross_ref_logo_f1_olmo_ref: 0.61
326	    cross_ref_logo_f1_qwen_ref: 0.58
327	  result_rationale: 'Entropy_mean drift attenuates (|ρ| drops from 0.68 to 0.36-0.42)
328	    because the drift magnitude depends on how well the reference model''s learned
329	    distribution aligns with the generator''s mode. Pythia-410M shares architecture
330	    and pretraining data with Pythia-2.8B, amplifying NLL sensitivity to the generator''s
331	    recursive drift. Non-Pythia references (OLMo, Qwen) have different internal distributions,
332	    so the NLL mean shifts less per depth step — the drift still exists (recursive
333	    generation objectively compresses the output distribution regardless of who measures
334	    it) but the reference model''s measurement sensitivity is lower. Shape features
335	    remain H1 (|ρ|<0.12) across all references because distributional shape (variance,
336	    tail behavior) is a property of the generator''s softmax output geometry, which
337	    doesn''t change with the reference model — different reference models shift the
338	    NLL baseline but preserve relative shape statistics. Classification F1 drops moderately
339	    because attenuated entropy_mean signal provides less discriminative power for
340	    the ordinal depth task.
341	
342	    '
343	  tables:
344	  - name: 'Table 6: Entropy_mean Drift (ρ) by Reference Model'
345	    columns:
346	    - reference_model
347	    - entropy_mean_rho
348	    - p-value
349	    - classification_full_f1
350	    rows:
351	    - - Pythia-410M
352	      - -0.68
353	      - <0.001
354	      - 0.82
355	    - - OLMo-2-1B
356	      - -0.42
357	      - <0.001
358	      - 0.78
359	    - - Qwen3-0.6B
360	      - -0.36
361	      - <0.001
362	      - 0.76
363	  - name: 'Table 7: Shape Feature Stationarity Across References (max |ρ|)'
364	    columns:
365	    - reference_model
366	    - entropy_std_rho
367	    - entropy_max_rho
368	    - tail_decay_rho
369	    - max_abs_rho
370	    rows:
371	    - - Pythia-410M
372	      - 0.03
373	      - -0.05
374	      - 0.04
375	      - 0.08
376	    - - OLMo-2-1B
377	      - 0.06
378	      - -0.08
379	      - -0.11
380	      - 0.11
381	    - - Qwen3-0.6B
382	      - -0.04
383	      - 0.07
384	      - 0.09
385	      - 0.09
386	  figures_description:
387	  - 'Fig 5: Entropy_mean trend lines (depth 0-4) for three reference models. Pythia-410M
388	    shows steepest decline; OLMo-2-1B intermediate; Qwen3-0.6B shallowest. All three
389	    monotonically decreasing but with different slopes.'
390	  - 'Fig 6: Shape feature (entropy_std, tail_decay) trend lines across reference models
391	    — three nearly flat lines per feature, confirming H1 robustness is reference-model-invariant.'
392	  analysis: 'Dual dynamics survives but is reference-model-modulated. The level/shape
393	    split is real across all references (H2 features always drift, H1 features always
394	    stable), but drift magnitude varies 2x depending on reference model choice. This
395	    softens Claim 2 from ''dual dynamics as universal law'' to ''reference-model-modulated
396	    dual dynamics'' — the split is intrinsic to what the feature measures (central
397	    tendency vs shape), but the signal strength depends on reference-generator alignment.
398	    Paper must present this honestly and discuss implications for practical deployment
399	    (reference model selection matters). The cross-reference LOGO F1 (0.58-0.61) shows
400	    that non-Pythia references still support depth estimation, just with reduced accuracy.
401	
402	    '
403	- name: downstream_utility
404	  plan_id: plan_004
405	  description: 'Fine-tune OLMo-1B on depth-stratified data. 3 seeds with bootstrap
406	    CIs. Compare depth-aware filtering (keep gen-0 + gen-1) vs binary baselines (FastDetectGPT,
407	    LD-Score threshold). Sample-count-matched comparison to control for data size
408	    confound.
409	
410	    '
411	  expected_results:
412	    seeds_run: 3
413	    depth_quality_spearman_rho: 0.53
414	    depth_quality_spearman_ci: '[0.41, 0.64]'
415	    ppl_gen0_only: 18.4
416	    ppl_gen0_plus_gen1: 19.1
417	    ppl_gen0_plus_gen1_plus_gen2plus: 21.7
418	    ppl_unfiltered: 22.3
419	    depth_filtering_ppl_improvement_pct: 5.2
420	    depth_filtering_ppl_improvement_ci: '[3.8, 7.1]'
421	    binary_fastdetectgpt_ppl_improvement_pct: 3.8
422	    binary_fastdetectgpt_ppl_improvement_ci: '[2.1, 5.9]'
423	    binary_ldscore_ppl_improvement_pct: 3.2
424	    binary_ldscore_ppl_improvement_ci: '[1.6, 5.3]'
425	    sample_matched_depth_improvement_pct: 2.8
426	    sample_matched_binary_improvement_pct: 1.9
427	    ci_overlap_with_best_binary: true
428	    downstream_task_accuracy_depth: 0.724
429	    downstream_task_accuracy_binary: 0.711
430	    downstream_task_accuracy_unfiltered: 0.698
431	  result_rationale: 'Depth-quality correlation (ρ=0.53) is moderate because OLMo-1B
432	    is somewhat robust to moderate contamination — gen-1 data is only mildly degraded
433	    (perplexity shift from 18.4 to 19.1), so the correlation is driven primarily by
434	    the gen-2+ tail where distributional drift accumulates. Depth-aware filtering
435	    outperforms binary filtering by ~1.4% because it retains gen-1 data that binary
436	    detectors discard — gen-1 text is close to human-quality and contributes positively
437	    to training. However, CI overlap exists because: (1) the advantage is small in
438	    absolute terms, (2) 3 seeds produce wide CIs, and (3) FastDetectGPT''s false negative
439	    rate on gen-1 means it sometimes keeps useful gen-1 data by accident. Sample-matched
440	    comparison (controlling for the data size advantage of depth-aware filtering)
441	    reduces the gap further to 0.9%, confirming that roughly half the advantage comes
442	    from retaining more training data, not from better selection. The effect is real
443	    but modest — insufficient for a strong ''significantly outperforms'' claim.
444	
445	    '
446	  tables:
447	  - name: 'Table 8: Downstream Perplexity by Training Data Composition (OLMo-1B, 3
448	      seeds)'
449	    columns:
450	    - training_data
451	    - n_samples
452	    - mean_ppl
453	    - std_ppl
454	    - 95% CI
455	    rows:
456	    - - gen-0 only
457	      - 4850
458	      - 18.4
459	      - 0.3
460	      - '[17.9, 18.9]'
461	    - - gen-0 + gen-1
462	      - 9700
463	      - 19.1
464	      - 0.4
465	      - '[18.5, 19.7]'
466	    - - gen-0 + gen-1 + gen-2+
467	      - 18200
468	      - 21.7
469	      - 0.6
470	      - '[20.8, 22.6]'
471	    - - Unfiltered (all depths)
472	      - 21500
473	      - 22.3
474	      - 0.5
475	      - '[21.5, 23.1]'
476	  - name: 'Table 9: Filtering Strategy Comparison'
477	    columns:
478	    - strategy
479	    - kept_samples
480	    - ppl_improvement_pct
481	    - 95% CI
482	    - overlap_with_depth
483	    rows:
484	    - - Depth-aware (gen-0+gen-1)
485	      - 9700
486	      - 5.2
487	      - '[3.8, 7.1]'
488	      - —
489	    - - FastDetectGPT binary
490	      - 7300
491	      - 3.8
492	      - '[2.1, 5.9]'
493	      - 'yes'
494	    - - LD-Score binary
495	      - 6900
496	      - 3.2
497	      - '[1.6, 5.3]'
498	      - 'yes'
499	    - - Sample-matched depth
500	      - 7300
501	      - 2.8
502	      - '[1.4, 4.5]'
503	      - —
504	    - - Sample-matched binary
505	      - 7300
506	      - 1.9
507	      - '[0.5, 3.6]'
508	      - —
509	  figures_description:
510	  - 'Fig 7: Perplexity degradation curve as function of training data depth composition
511	    (0-4). Clear upward trend with error bars (3 seeds). gen-0→gen-1 step is small;
512	    gen-1→gen-2+ is the main inflection point.'
513	  - 'Fig 8: Bootstrap CI comparison — depth-aware vs binary filtering perplexity improvement.
514	    Point estimates favor depth-aware, but CI bars overlap for FastDetectGPT.'
515	  analysis: 'Downstream utility exists but the advantage over binary filtering is
516	    modest (1.4% mean, CIs overlap). Claim 3 must be softened to ''depth-aware filtering
517	    offers complementary signal to binary detection'' — the value proposition is not
518	    raw performance but the ability to retain useful gen-1 data while filtering harmful
519	    gen-2+. Sample-matched analysis shows roughly half the gain is from data volume,
520	    not selection quality. Paper should present this honestly and emphasize the interpretability
521	    advantage: depth scores provide a continuous risk metric that binary labels cannot.
522	
523	    '
524	- name: prompt_type_comparison
525	  plan_id: plan_005
526	  description: 'Compare depth signal across three prompt types: continuation, elaboration,
527	    inspired_rewriting. 1000 seeds × Pythia-2.8B × 5 depths × 3 prompt types.
528	
529	    '
530	  expected_results:
531	    continuation_macro_f1: 0.82
532	    elaboration_macro_f1: 0.77
533	    inspired_rewriting_macro_f1: 0.69
534	    continuation_entropy_mean_rho: -0.68
535	    elaboration_entropy_mean_rho: -0.57
536	    inspired_rewriting_entropy_mean_rho: -0.39
537	    continuation_ttr_slope: -0.071
538	    elaboration_ttr_slope: -0.058
539	    inspired_rewriting_ttr_slope: -0.031
540	    h1_features_stable_across_prompts: true
541	  result_rationale: 'Continuation preserves the strongest depth signal because each
542	    step feeds the previous output directly, maximizing distributional drift accumulation.
543	    Elaboration introduces a semantic reframing prompt that partially resets the generator''s
544	    conditioning, attenuating the chain''s compounding effect — the generator still
545	    uses the previous text but the prompt steers it toward a different discourse structure,
546	    reducing the monotonic drift. Inspired rewriting is most disruptive because the
547	    generator is asked to produce content ''inspired by'' rather than continuing from
548	    the previous text — this creates a loose semantic link but breaks the tight distributional
549	    chain, so depth-0 vs depth-2 texts can have similar distributional properties
550	    if the generator happens to produce fluent rewrites. H1 features remain stable
551	    across all prompt types because shape stationarity is a property of the generator''s
552	    output distribution, not the input conditioning.
553	
554	    '
555	  tables:
556	  - name: 'Table 10: Depth Classification by Prompt Type (Pythia-2.8B, 5-fold CV)'
557	    columns:
558	    - prompt_type
559	    - macro_f1
560	    - entropy_mean_rho
561	    - ttr_slope
562	    - semantic_divergence_cosine
563	    rows:
564	    - - Continuation
565	      - 0.82
566	      - -0.68
567	      - -0.071
568	      - 0.85
569	    - - Elaboration
570	      - 0.77
571	      - -0.57
572	      - -0.058
573	      - 0.72
574	    - - Inspired rewriting
575	      - 0.69
576	      - -0.39
577	      - -0.031
578	      - 0.54
579	  figures_description:
580	  - 'Fig 9: Feature drift magnitude by prompt type — bar chart showing H2 feature
581	    slopes for each prompt type. Clear gradient from continuation (steepest) to inspired
582	    rewriting (shallowest).'
583	  analysis: 'Semantic divergence from source anti-correlates with depth signal preservation.
584	    Continuation is the ideal setting for depth estimation; inspired rewriting represents
585	    a harder, more realistic scenario where depth signal partially dissolves. This
586	    informs ecological validity discussions: real-world LLM contamination likely involves
587	    a mix of prompt types, placing practical performance between 0.69-0.82.
588	
589	    '
590	- name: paraphrastic_comparison
591	  plan_id: plan_006
592	  description: 'Parallel paraphrasing chains vs continuation chains for direct comparison.
593	    Tests attractor convergence theory — paraphrastic chains should saturate earlier.
594	
595	    '
596	  expected_results:
597	    paraphrastic_3class_f1: 0.66
598	    nonparaphrastic_3class_f1: 0.82
599	    paraphrastic_gen2plus_f1: 0.41
600	    nonparaphrastic_gen2plus_f1: 0.79
601	    paraphrastic_5class_f1: 0.29
602	    nonparaphrastic_5class_f1: 0.43
603	    paraphrastic_entropy_mean_rho: -0.34
604	    nonparaphrastic_entropy_mean_rho: -0.68
605	    paraphrastic_signal_saturation_depth: 2
606	    nonparaphrastic_signal_saturation_depth: 4
607	  result_rationale: 'Paraphrastic chains converge to attractor cycles (ACL 2025 theory),
608	    bounding depth signal to ~2 distinguishable classes — by depth-2, paraphrased
609	    text has already entered the attractor basin, so gen-2/gen-3/gen-4 become distributionally
610	    indistinguishable. This collapses gen-2+ F1 to near-chance (0.41). Non-paraphrastic
611	    continuation chains escape the attractor because each step generates genuinely
612	    new content rather than cycling through semantically equivalent rewrites. Distributional
613	    drift accumulates monotonically through depth-4, preserving ordinal signal. The
614	    paraphrastic entropy_mean ρ (-0.34) is weaker because the drift saturates early
615	    — depths 2-4 contribute noise, not signal, to the correlation. This directly validates
616	    the paper''s premise: non-paraphrastic chains are the right focus for depth estimation
617	    because the attractor convergence bound does not apply.
618	
619	    '
620	  tables:
621	  - name: 'Table 11: Paraphrastic vs Non-paraphrastic Depth Classification'
622	    columns:
623	    - chain_type
624	    - 3class_f1
625	    - gen0_f1
626	    - gen1_f1
627	    - gen2plus_f1
628	    - signal_saturation_depth
629	    rows:
630	    - - Paraphrastic
631	      - 0.66
632	      - 0.89
633	      - 0.67
634	      - 0.41
635	      - 2
636	    - - Non-paraphrastic
637	      - 0.82
638	      - 0.94
639	      - 0.77
640	      - 0.79
641	      - 4+
642	  figures_description:
643	  - 'Fig 10: Per-depth F1 curves for paraphrastic (flattens at depth 2) vs non-paraphrastic
644	    (gradual decline through depth 4). Clear visual separation demonstrating attractor
645	    saturation vs sustained drift.'
646	  analysis: 'Confirms the theoretical motivation: paraphrastic chains hit the attractor
647	    bound at depth ~2, while non-paraphrastic chains maintain discriminable depth
648	    signal through depth 4. This justifies the paper''s focus on continuation chains
649	    and connects to attractor cycle theory as a boundary condition rather than a general
650	    limit on depth estimation.
651	
652	    '
653	- name: cross_model_chains
654	  plan_id: plan_007
655	  description: 'Cross-model chains (different generator per depth step) vs single-model
656	    chains. Tests ecological validity for real web contamination scenarios.
657	
658	    '
659	  expected_results:
660	    cross_model_logo_f1: 0.56
661	    single_model_logo_f1: 0.64
662	    cross_model_within_f1: 0.68
663	    cross_model_entropy_mean_rho: -0.41
664	    cross_model_ttr_slope: -0.039
665	    cross_model_h1_stable: true
666	    cross_model_gen0_f1: 0.78
667	    cross_model_gen1_f1: 0.46
668	    cross_model_gen2plus_f1: 0.44
669	  result_rationale: 'Cross-model chains inject between-model distributional variance
670	    at each depth step. When generator changes between depths (e.g., Pythia→OLMo→Qwen),
671	    the NLL features measured by the reference model reflect not just depth-related
672	    drift but also generator-switching effects — the reference model''s NLL for OLMo-generated
673	    text differs from Pythia-generated text regardless of depth. This noise source
674	    partially masks the depth signal, particularly for gen-1 vs gen-2+ where the depth
675	    effect is smaller than the generator effect. Gen-0 (human) remains well-separated
676	    (F1 0.78) because all chains share the same human seed distribution. The F1 drop
677	    from 0.64 (single-model LOGO) to 0.56 (cross-model) quantifies the cost of realistic
678	    generator diversity. H1 features remain stable even in cross-model chains, confirming
679	    that shape stationarity is generator-intrinsic.
680	
681	    '
682	  tables:
683	  - name: 'Table 12: Cross-model vs Single-model Chain Classification'
684	    columns:
685	    - chain_type
686	    - logo_f1
687	    - gen0_f1
688	    - gen1_f1
689	    - gen2plus_f1
690	    - entropy_mean_rho
691	    rows:
692	    - - Single-model
693	      - 0.64
694	      - 0.83
695	      - 0.57
696	      - 0.58
697	      - -0.68
698	    - - Cross-model
699	      - 0.56
700	      - 0.78
701	      - 0.46
702	      - 0.44
703	      - -0.41
704	  figures_description:
705	  - 'Fig 11: Confusion matrices for cross-model chains — gen-1/gen-2+ are heavily
706	    confused due to generator-switching noise dominating depth signal.'
707	  analysis: 'Cross-model chains degrade depth estimation significantly (-0.08 F1).
708	    This is a realistic limitation: web contamination involves diverse generators,
709	    and the current feature set partially conflates generator identity with depth.
710	    Paper should present this as an honest ecological validity test — depth estimation
711	    is most reliable for single-source contamination, and cross-model scenarios require
712	    future work on generator-invariant features.
713	
714	    '
715	- name: multi_domain_seeds
716	  plan_id: plan_008
717	  description: 'Expand to 4 domains: Wikipedia, news (CNN/DM), scientific (S2ORC),
718	    creative (WritingPrompts). 500 seeds per domain × 5 depths × 5 generators.
719	
720	    '
721	  expected_results:
722	    wikipedia_logo_f1: 0.67
723	    news_logo_f1: 0.64
724	    scientific_logo_f1: 0.62
725	    creative_logo_f1: 0.57
726	    pooled_multidomain_logo_f1: 0.63
727	    domain_f1_std: 0.037
728	    wikipedia_entropy_mean_rho: -0.72
729	    creative_entropy_mean_rho: -0.48
730	    cross_domain_train_test_f1: 0.58
731	  result_rationale: 'Wikipedia seeds yield highest F1 (0.67) because Wikipedia prose
732	    is stylistically uniform and formulaic — generators produce characteristically
733	    homogeneous continuations that maximize distributional drift consistency across
734	    depths. Creative writing seeds yield lowest F1 (0.57) because creative text has
735	    high intrinsic variance (diverse styles, tones, registers), which creates a larger
736	    noise floor that depth signal must overcome. The generator''s creative outputs
737	    at depth-1 can be as distributionally diverse as human creative text, blurring
738	    the gen-0/gen-1 boundary. Scientific text (0.62) occupies the middle ground: constrained
739	    register but technical vocabulary creates complex distributional patterns. Cross-domain
740	    train-test (train on 3 domains, test on 1) drops to 0.58, suggesting partial domain
741	    adaptation in the classifier.
742	
743	    '
744	  tables:
745	  - name: 'Table 13: Domain-Specific LOGO Results'
746	    columns:
747	    - domain
748	    - logo_f1
749	    - entropy_mean_rho
750	    - ttr_slope
751	    - n_seeds
752	    rows:
753	    - - Wikipedia
754	      - 0.67
755	      - -0.72
756	      - -0.078
757	      - 500
758	    - - News (CNN/DM)
759	      - 0.64
760	      - -0.63
761	      - -0.065
762	      - 500
763	    - - Scientific (S2ORC)
764	      - 0.62
765	      - -0.58
766	      - -0.059
767	      - 500
768	    - - Creative (WritingPrompts)
769	      - 0.57
770	      - -0.48
771	      - -0.041
772	      - 500
773	    - - Pooled
774	      - 0.63
775	      - -0.6
776	      - -0.061
777	      - 2000
778	  figures_description:
779	  - 'Fig 12: Domain-specific entropy_mean drift plots — four panels showing depth
780	    0-4 trends. Wikipedia shows tightest confidence bands; creative shows widest.'
781	  analysis: 'Domain variation (std 0.037) is non-trivial but depth signal generalizes
782	    across all four domains. Creative writing is the hardest domain, consistent with
783	    high intrinsic variance. Paper should report pooled results as primary and domain-specific
784	    as supplementary analysis, noting that domain adaptation (train/test domain mismatch)
785	    is an additional challenge beyond generator generalization.
786	
787	    '
788	- name: finer_grained_ordinal
789	  plan_id: plan_009
790	  description: '5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic
791	    chains. Tests whether depth signal supports finer than 3-class resolution.
792	
793	    '
794	  expected_results:
795	    five_class_macro_f1: 0.43
796	    five_class_gen0_f1: 0.73
797	    five_class_gen1_f1: 0.52
798	    five_class_gen2_f1: 0.35
799	    five_class_gen3_f1: 0.29
800	    five_class_gen4_f1: 0.28
801	    ordinal_mae: 0.72
802	    three_class_macro_f1_same_data: 0.64
803	    adjacent_confusion_rate: 0.61
804	    spearman_pred_vs_true: 0.74
805	  result_rationale: '5-class F1 (0.43) drops substantially from 3-class (0.64) because
806	    distributional differences between adjacent depths (gen-2 vs gen-3, gen-3 vs gen-4)
807	    are small — the drift per step is roughly constant, but the cumulative difference
808	    between gen-0 and gen-4 is spread across 4 boundaries, each of which is harder
809	    than the 3-class boundaries. Gen-0 is still well-separated (0.73) because human
810	    vs any synthetic is the largest distributional gap. Gen-1 (0.52) is intermediate
811	    — distinguishable from gen-0 and gen-2+ but with confusion on both sides. Gen-2/3/4
812	    collapse into a muddy cluster (F1 0.28-0.35) because by depth-2, recursive drift
813	    has already consumed most of the easy-to-detect signal, and remaining differences
814	    are within the noise floor. However, ordinal Spearman (0.74) is respectable, showing
815	    the classifier preserves rank order even when exact class assignment fails — errors
816	    are predominantly between adjacent classes (61% of errors), not distant ones.
817	
818	    '
819	  tables:
820	  - name: 'Table 14: 5-class Ordinal Classification (LOGO, Full Features)'
821	    columns:
822	    - class
823	    - f1
824	    - precision
825	    - recall
826	    - most_confused_with
827	    rows:
828	    - - gen-0
829	      - 0.73
830	      - 0.78
831	      - 0.69
832	      - gen-1
833	    - - gen-1
834	      - 0.52
835	      - 0.49
836	      - 0.55
837	      - gen-0 / gen-2
838	    - - gen-2
839	      - 0.35
840	      - 0.33
841	      - 0.37
842	      - gen-3
843	    - - gen-3
844	      - 0.29
845	      - 0.31
846	      - 0.27
847	      - gen-2 / gen-4
848	    - - gen-4
849	      - 0.28
850	      - 0.26
851	      - 0.3
852	      - gen-3
853	  figures_description:
854	  - 'Fig 13: 5×5 confusion matrix heatmap — strong diagonal for gen-0, increasingly
855	    diffuse for deeper classes. Off-diagonal mass concentrated on ±1 adjacent cells.'
856	  - 'Fig 14: Predicted vs true depth scatter with ordinal regression line (Spearman
857	    ρ=0.74).'
858	  analysis: 'Finer-grained classification is feasible but noisy beyond 3 classes.
859	    The 3-class grouping (gen-0/gen-1/gen-2+) appears to be the natural resolution
860	    supported by the current feature set. Paper presents 5-class as secondary analysis
861	    motivating ordinal regression approaches in future work. The high ordinal Spearman
862	    (0.74) suggests the classifier captures depth ordering even when exact classification
863	    fails, which is useful for risk scoring applications.
864	
865	    '
866	- name: human_edit_robustness
867	  plan_id: plan_010
868	  description: 'Robustness to simulated human edits: (A) random word replacement at
869	    5%/10%/20%, (B) LLM-simulated light rephrasing. Tests whether post-processing
870	    destroys depth signal.
871	
872	    '
873	  expected_results:
874	    baseline_no_edit_f1: 0.82
875	    random_5pct_f1: 0.79
876	    random_10pct_f1: 0.72
877	    random_20pct_f1: 0.6
878	    llm_light_edit_f1: 0.73
879	    random_5pct_entropy_mean_rho: -0.63
880	    random_10pct_entropy_mean_rho: -0.52
881	    random_20pct_entropy_mean_rho: -0.35
882	    llm_light_edit_entropy_mean_rho: -0.49
883	    h1_features_robust_to_edit: true
884	    shape_features_max_rho_change: 0.07
885	  result_rationale: 'Random word replacement progressively corrupts the text''s distributional
886	    profile. At 5%, the corruption is below the feature noise floor — surface features
887	    (TTR, hapax) are slightly perturbed but NLL features remain stable because 5%
888	    random words don''t substantially alter the reference model''s token-level surprise
889	    distribution. At 20%, the text becomes distributionally anomalous in a way that
890	    overwhelms the depth signal — randomly inserted words create a uniform noise pattern
891	    that masks depth-specific distributional drift. LLM-simulated editing (F1 0.73)
892	    falls between 5% and 10% random replacement because LLM edits are more natural
893	    (preserving grammaticality) but more targeted (selectively replacing awkward or
894	    repetitive phrases that carry depth signal). Shape features remain robust (max
895	    ρ change 0.07) because random/LLM edits affect vocabulary composition (level)
896	    more than distributional shape.
897	
898	    '
899	  tables:
900	  - name: 'Table 15: Robustness to Simulated Human Edits'
901	    columns:
902	    - edit_type
903	    - edit_rate
904	    - macro_f1
905	    - delta_f1
906	    - entropy_mean_rho
907	    rows:
908	    - - None (baseline)
909	      - 0%
910	      - 0.82
911	      - —
912	      - -0.68
913	    - - Random word
914	      - 5%
915	      - 0.79
916	      - -0.03
917	      - -0.63
918	    - - Random word
919	      - 10%
920	      - 0.72
921	      - -0.1
922	      - -0.52
923	    - - Random word
924	      - 20%
925	      - 0.6
926	      - -0.22
927	      - -0.35
928	    - - LLM light rephrase
929	      - ~8%
930	      - 0.73
931	      - -0.09
932	      - -0.49
933	  figures_description:
934	  - 'Fig 15: F1 degradation curve as function of edit rate — roughly linear decline
935	    with inflection around 15%. LLM editing point plotted at estimated ~8% token change
936	    rate.'
937	  analysis: 'Depth signal is moderately robust to light editing (5%) but degrades
938	    meaningfully at 10%+. Real-world human editing likely falls in the 5-15% range,
939	    placing expected performance at F1 0.72-0.79. Paper presents this as honest robustness
940	    analysis — depth estimation is viable for lightly edited synthetic text but fragile
941	    under heavy post-processing. This limits practical applicability to scenarios
942	    where contamination involves minimally edited LLM outputs.
943	
944	    '
945	- name: ld_score_feature
946	  plan_id: plan_011
947	  description: 'Add LD-Score as feature. Test pre-registered prediction that LD-Score
948	    is a level feature (H2 drift). Evaluate marginal classification improvement.
949	
950	    '
951	  expected_results:
952	    ld_score_depth_rho: -0.55
953	    ld_score_slope: -0.042
954	    ld_score_r2: 0.72
955	    ld_score_classification: H2_level
956	    preregistered_prediction_confirmed: true
957	    f1_with_ld_score: 0.83
958	    f1_without_ld_score: 0.82
959	    marginal_improvement: 0.01
960	    ld_score_correlation_with_ttr: 0.68
961	    ld_score_correlation_with_hapax: 0.61
962	  result_rationale: 'LD-Score measures character-level distributional properties,
963	    which are downstream of vocabulary composition — as depth increases and vocabulary
964	    impoverishes (fewer unique words, more repetitive character n-grams), LD-Score
965	    shifts accordingly. This confirms it is a level feature (H2), sensitive to the
966	    same vocabulary/diversity drift as TTR and hapax_ratio. The pre-registered prediction
967	    is validated (ρ=-0.55, clearly H2), strengthening the level/shape framework''s
968	    predictive power. However, the high correlation with existing surface features
969	    (0.61-0.68 with TTR/hapax) means LD-Score provides little incremental information
970	    — the marginal F1 gain is only 0.01. The character-level signal is largely redundant
971	    with word-level diversity features already in the feature set.
972	
973	    '
974	  tables:
975	  - name: 'Table 16: LD-Score Feature Analysis'
976	    columns:
977	    - metric
978	    - value
979	    rows:
980	    - - LD-Score depth ρ
981	      - -0.55
982	    - - LD-Score linear slope
983	      - -0.042
984	    - - LD-Score R²
985	      - 0.72
986	    - - H1/H2 classification
987	      - H2 (level)
988	    - - Pre-registered prediction
989	      - Confirmed
990	    - - Correlation with TTR
991	      - 0.68
992	    - - Correlation with hapax_ratio
993	      - 0.61
994	    - - F1 with LD-Score
995	      - 0.83
996	    - - F1 without LD-Score
997	      - 0.82
998	  figures_description:
999	  - 'Fig 16: LD-Score depth trend (mean ± std, depths 0-4) overlaid with TTR trend
1000	    — similar decline pattern, confirming shared level/diversity dynamics at character
1001	    level.'
1002	  analysis: 'Pre-registered prediction confirmed: LD-Score is a level feature. This
1003	    is a minor but clean validation of the H1/H2 framework''s predictive utility.
1004	    However, the marginal classification improvement is negligible (0.01), so LD-Score
1005	    is presented as a validation data point rather than a feature engineering contribution.
1006	    The high correlation with existing features suggests character-level and word-level
1007	    diversity measures capture the same underlying depth signal.
1008	
1009	    '
1010	- name: end_to_end_classifier
1011	  plan_id: plan_012
1012	  description: 'QLoRA fine-tuned Qwen3-0.6B for end-to-end depth classification. Compares
1013	    learned representations vs handcrafted distributional features.
1014	
1015	    '
1016	  expected_results:
1017	    qlora_macro_f1: 0.79
1018	    qlora_gen0_f1: 0.92
1019	    qlora_gen1_f1: 0.73
1020	    qlora_gen2plus_f1: 0.72
1021	    handcrafted_macro_f1: 0.82
1022	    qlora_cross_gen_logo_f1: 0.61
1023	    handcrafted_cross_gen_logo_f1: 0.64
1024	    qlora_training_time_hours: 6.2
1025	    qlora_inference_tokens_per_sec: 145
1026	    handcrafted_inference_tokens_per_sec: 8900
1027	  result_rationale: 'QLoRA achieves slightly lower F1 (0.79 vs 0.82) because the depth
1028	    classification task has limited training data (~25K samples) — insufficient for
1029	    a 600M-parameter model to learn robust depth-specific representations from scratch.
1030	    The model likely overfits to generator- specific patterns rather than learning
1031	    the distributional drift abstraction that handcrafted features explicitly encode.
1032	    Cross-generator LOGO (0.61 vs 0.64) shows the end-to-end approach generalizes
1033	    slightly worse, further suggesting it memorizes generator identities. The handcrafted
1034	    approach also has a massive inference speed advantage (~60x) because it requires
1035	    only a forward pass through the small reference model + simple statistics, vs
1036	    full sequence processing through a 600M model. This confirms the paper''s positioning:
1037	    the contribution is the problem formulation and empirical findings, not a competition
1038	    for SOTA — simple features suffice for the task.
1039	
1040	    '
1041	  tables:
1042	  - name: 'Table 17: End-to-End vs Handcrafted Features'
1043	    columns:
1044	    - method
1045	    - within_gen_f1
1046	    - logo_f1
1047	    - inference_speed
1048	    - training_cost
1049	    rows:
1050	    - - Handcrafted (XGBoost)
1051	      - 0.82
1052	      - 0.64
1053	      - 8900 tok/s
1054	      - ~0 GPU-h
1055	    - - QLoRA (Qwen3-0.6B)
1056	      - 0.79
1057	      - 0.61
1058	      - 145 tok/s
1059	      - 6.2 GPU-h
1060	  figures_description:
1061	  - 'Fig 17: F1 comparison bar chart (within-gen and LOGO) for handcrafted vs QLoRA.
1062	    Handcrafted is slightly better on both metrics while being 60x faster at inference.'
1063	  analysis: 'End-to-end approach does not outperform handcrafted features, confirming
1064	    that the task''s information content is well-captured by simple distributional
1065	    statistics. This validates the paper''s contribution positioning: novelty lies
1066	    in the problem formulation and empirical findings, not in model architecture.
1067	    The interpretability and efficiency advantages of handcrafted features are a practical
1068	    benefit for deployment in data curation pipelines.
1069	
1070	    '
1071	- name: text_length_control
1072	  plan_id: plan_013
1073	  description: 'Length confound analysis: (A) length distributions by depth, (B) length-normalized
1074	    features, (C) length-matched classification. Critical confound control.
1075	
1076	    '
1077	  expected_results:
1078	    mean_length_gen0: 315
1079	    mean_length_gen1: 289
1080	    mean_length_gen2: 263
1081	    mean_length_gen3: 246
1082	    mean_length_gen4: 237
1083	    length_depth_pearson_r: -0.41
1084	    length_depth_kw_p: <0.001
1085	    original_surface_f1: 0.76
1086	    length_controlled_surface_f1: 0.71
1087	    length_controlled_surface_f1_delta: -0.05
1088	    original_reference_f1: 0.72
1089	    length_controlled_reference_f1: 0.7
1090	    length_controlled_reference_f1_delta: -0.02
1091	    original_full_f1: 0.82
1092	    length_controlled_full_f1: 0.78
1093	    length_controlled_full_f1_delta: -0.04
1094	    length_matched_subsample_full_f1: 0.79
1095	    fixed_window_ttr_slope: -0.048
1096	    fixed_window_ttr_original_slope: -0.071
1097	    fixed_window_hapax_slope: -0.037
1098	    fixed_window_hapax_original_slope: -0.054
1099	    residual_signal_confirmed: true
1100	  result_rationale: 'Text length decreases monotonically with depth (315→237 tokens)
1101	    because recursive generation tends to produce slightly shorter texts — generators
1102	    are biased toward completing thoughts within a typical output length, and each
1103	    depth step compounds this tendency. This creates a legitimate confound: TTR and
1104	    hapax_ratio are mechanically length-dependent (shorter texts have higher TTR/hapax
1105	    by construction). The -0.05 surface F1 drop after length control confirms that
1106	    ~30% of the surface feature signal was tracking length, not depth. However, the
1107	    residual signal (F1 0.71 after control, well above chance at 0.33) confirms that
1108	    depth drives genuine vocabulary impoverishment beyond what length explains. Reference
1109	    features lose less (-0.02) because NLL statistics are computed token-by-token
1110	    and are less length-sensitive — the per-token surprise distribution shifts with
1111	    depth regardless of total text length. The full-feature length-controlled F1 (0.78)
1112	    remains substantially above chance and above either feature subset, confirming
1113	    the core claims survive length control.
1114	
1115	    '
1116	  tables:
1117	  - name: 'Table 18: Text Length by Depth'
1118	    columns:
1119	    - depth
1120	    - mean_tokens
1121	    - std_tokens
1122	    - median_tokens
1123	    rows:
1124	    - - gen-0
1125	      - 315
1126	      - 82
1127	      - 298
1128	    - - gen-1
1129	      - 289
1130	      - 76
1131	      - 274
1132	    - - gen-2
1133	      - 263
1134	      - 71
1135	      - 251
1136	    - - gen-3
1137	      - 246
1138	      - 68
1139	      - 237
1140	    - - gen-4
1141	      - 237
1142	      - 65
1143	      - 228
1144	  - name: 'Table 19: Length-Controlled Classification Results'
1145	    columns:
1146	    - feature_set
1147	    - original_f1
1148	    - length_controlled_f1
1149	    - delta
1150	    - delta %
1151	    rows:
1152	    - - Full
1153	      - 0.82
1154	      - 0.78
1155	      - -0.04
1156	      - -4.9%
1157	    - - Surface only
1158	      - 0.76
1159	      - 0.71
1160	      - -0.05
1161	      - -6.6%
1162	    - - Reference only
1163	      - 0.72
1164	      - 0.7
1165	      - -0.02
1166	      - -2.8%
1167	  - name: 'Table 20: Fixed-Window Feature Slopes (128-token windows)'
1168	    columns:
1169	    - feature
1170	    - original_slope
1171	    - fixed_window_slope
1172	    - slope_reduction_pct
1173	    rows:
1174	    - - TTR
1175	      - -0.071
1176	      - -0.048
1177	      - 32%
1178	    - - hapax_ratio
1179	      - -0.054
1180	      - -0.037
1181	      - 31%
1182	    - - entropy_mean
1183	      - -0.148
1184	      - -0.139
1185	      - 6%
1186	  figures_description:
1187	  - 'Fig 18: Text length distribution violin plots by depth — clear leftward shift
1188	    with depth. Overlapping distributions confirm length is a partial, not sole, confound.'
1189	  - 'Fig 19: Feature slopes before/after length control — surface features show ~30%
1190	    reduction; reference features show <10% reduction. Visualizes the differential
1191	    length sensitivity.'
1192	  analysis: 'Length is a real but partial confound. The 0.05 surface F1 drop is within
1193	    the median range [-0.08, -0.03] and must be acknowledged honestly in the paper.
1194	    The key finding is that residual signal survives: depth drives genuine distributional
1195	    drift beyond length artifacts. Reference features are relatively length-robust
1196	    (only 0.02 drop), strengthening their value in the feature set. Paper should add
1197	    length-controlled analysis as a supplementary validation table and note: ''Surface
1198	    features partially track text length, but residual depth signal persists after
1199	    length control. Reference features provide length-robust complementary signal.''
1200	
1201	    '
1202	- name: large_scale_generator
1203	  plan_id: plan_014
1204	  description: 'Add Qwen3-8B-Base as 7B+ generator. 1000 seeds × 5 depths. Tests whether
1205	    depth signal persists at frontier scale.
1206	
1207	    '
1208	  expected_results:
1209	    qwen8b_3class_macro_f1: 0.57
1210	    qwen8b_gen0_f1: 0.76
1211	    qwen8b_gen1_f1: 0.48
1212	    qwen8b_gen2plus_f1: 0.46
1213	    qwen8b_entropy_mean_rho: -0.38
1214	    qwen8b_ttr_slope: -0.042
1215	    qwen8b_hapax_slope: -0.032
1216	    qwen8b_vs_pythia28b_f1_gap: -0.25
1217	    qwen8b_vs_qwen17b_f1_gap: -0.05
1218	    qwen8b_h1_features_stable: true
1219	    qwen8b_entropy_std_rho: 0.05
1220	    qwen8b_tail_decay_rho: -0.07
1221	    qwen8b_5class_f1: 0.31
1222	    logo_with_8b_included: 0.61
1223	  result_rationale: '7B+ generators produce substantially more fluent text that compresses
1224	    the depth signal. At 8B parameters, the model has sufficient capacity to maintain
1225	    diverse vocabulary and natural distributional properties even at depth-4 — vocabulary
1226	    impoverishment is less severe because the model''s larger vocabulary and richer
1227	    internal representations allow it to produce varied continuations even from distributionally
1228	    drifted inputs. The F1 drop from 0.82 (Pythia-2.8B) to 0.57 (Qwen3-8B) is large
1229	    but the signal remains non-trivial (well above chance at 0.33). Entropy_mean ρ
1230	    attenuates from -0.68 to -0.38, consistent with weaker but non-zero drift — the
1231	    8B model''s NLL distribution still shifts with depth but less per step. Gen-0
1232	    remains distinguishable (F1 0.76) because the human-vs-any-synthetic gap is robust
1233	    to model scale, but gen-1 vs gen-2+ becomes very noisy (0.46-0.48). H1 features
1234	    remain stable (shape stationarity is scale-invariant). This is an honest scaling
1235	    result: depth estimation weakens at scale but doesn''t vanish, motivating future
1236	    work on scale-robust features.
1237	
1238	    '
1239	  tables:
1240	  - name: 'Table 21: 7B+ Generator Depth Classification'
1241	    columns:
1242	    - generator
1243	    - params
1244	    - macro_f1
1245	    - entropy_mean_rho
1246	    - ttr_slope
1247	    rows:
1248	    - - Pythia-2.8B
1249	      - 2.8B
1250	      - 0.82
1251	      - -0.68
1252	      - -0.071
1253	    - - Pythia-1B
1254	      - 1B
1255	      - 0.8
1256	      - -0.65
1257	      - -0.068
1258	    - - OLMo-2-1B
1259	      - 1.5B
1260	      - 0.78
1261	      - -0.61
1262	      - -0.063
1263	    - - Qwen3-1.7B
1264	      - 1.7B
1265	      - 0.75
1266	      - -0.56
1267	      - -0.055
1268	    - - Qwen3-0.6B
1269	      - 0.6B
1270	      - 0.77
1271	      - -0.59
1272	      - -0.061
1273	    - - Qwen3-8B
1274	      - 8B
1275	      - 0.57
1276	      - -0.38
1277	      - -0.042
1278	  - name: 'Table 22: Scale Trend Analysis'
1279	    columns:
1280	    - metric
1281	    - ≤2.8B mean
1282	    - 8B
1283	    - delta
1284	    - interpretation
1285	    rows:
1286	    - - macro_f1
1287	      - 0.78
1288	      - 0.57
1289	      - -0.21
1290	      - Signal weakens at scale
1291	    - - entropy_mean ρ
1292	      - -0.62
1293	      - -0.38
1294	      - '+0.24'
1295	      - Drift attenuates at scale
1296	    - - TTR slope
1297	      - -0.064
1298	      - -0.042
1299	      - '+0.022'
1300	      - Less vocab impoverishment
1301	    - - H1 max |ρ|
1302	      - 0.08
1303	      - 0.07
1304	      - '-0.01'
1305	      - Shape stationarity preserved
1306	  figures_description:
1307	  - 'Fig 20: F1 vs generator parameter count (log scale). Clear downward trend from
1308	    0.6B-2.8B cluster to 8B outlier. Dotted line at chance (0.33) for reference.'
1309	  - 'Fig 21: Entropy_mean depth trend for 8B (shallow slope) vs 2.8B (steep slope).
1310	    Both monotonically decreasing but 8B slope is ~55% of 2.8B slope.'
1311	  analysis: '7B+ results confirm the scaling concern. Depth signal is weaker but non-zero
1312	    (F1 0.57, significantly above chance p<0.001). The paper should present this as
1313	    an honest scaling analysis in a dedicated subsection: ''Depth signal attenuates
1314	    with generator scale, consistent with larger models maintaining distributional
1315	    diversity under recursive generation. At 8B parameters, gen-0 vs synthetic remains
1316	    detectable, but fine-grained depth estimation (gen-1 vs gen-2+) approaches noise
1317	    floor. This motivates future work on scale-robust features, potentially leveraging
1318	    model-specific distributional properties.'' The 8B result transforms from a weakness
1319	    into a scientific finding: the relationship between model capacity and depth signal
1320	    decay is itself an interesting empirical contribution.'
1321	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d47f2260-d971-41c2-96f1-1e75a7e03fc0",
  "isSidechain": false,
  "promptId": "dd52a47a-ed24-4ace-b099-792192098121",
  "type": "user",
  "uuid": "35ff09db-d6b6-46c4-b828-d5b8a386bdcb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml",
      "content": "tier: median\nnarrative_guidance: 'Depth discriminability holds within-generator (F1 0.82) but cross-generator\n  generalization is moderate (LOGO F1 ~0.64), with performance drops concentrated\n  on out-of-family holdouts. Dual dynamics is real but reference-model-modulated:\n  entropy_mean drift attenuates to |ρ|~0.4 with non-Pythia references, requiring the\n  paper to present the H1/H2 split as ''reference-model-modulated dual dynamics''\n  rather than a universal law. Length confound is partial — surface feature F1 drops\n  ~0.05 after length control, but residual signal confirms depth is not reducible\n  to length. 7B+ signal weakens (F1 ~0.57) but persists, motivating future work on\n  scale-robust features. Downstream filtering offers complementary signal but CIs\n  overlap with best binary baseline on some metrics. Paper reframed: ''depth estimation\n  is feasible and useful, with initial evidence for dual dynamics'' rather than ''dual\n  dynamics as general principle.'' Still viable for AAAI/EMNLP as empirical contribution\n  with honest limitations.\n\n  '\nimagined_experiments:\n- name: feature_ablation_and_trend\n  plan_id: plan_001\n  description: 'Feature ablation (full / surface-only / reference-only) + H1/H2 trend\n    analysis on MVP data (Pythia-2.8B generator, Pythia-410M reference). Perplexity\n    pre-validation for Claim 3.\n\n    '\n  expected_results:\n    full_macro_f1: 0.82\n    surface_only_f1: 0.76\n    reference_only_f1: 0.72\n    full_vs_surface_gap: 0.06\n    full_vs_reference_gap: 0.1\n    bootstrap_ci_full: '[0.804, 0.836]'\n    bootstrap_ci_surface: '[0.747, 0.774]'\n    bootstrap_ci_reference: '[0.706, 0.733]'\n    h2_entropy_mean_slope: -0.148\n    h2_entropy_mean_r2: 0.93\n    h2_ttr_slope: -0.071\n    h2_ttr_r2: 0.87\n    h2_hapax_ratio_slope: -0.054\n    h2_hapax_ratio_r2: 0.81\n    h1_entropy_std_slope: 0.003\n    h1_entropy_std_r2: 0.02\n    h1_entropy_max_slope: -0.009\n    h1_entropy_max_r2: 0.04\n    h1_tail_decay_slope: 0.005\n    h1_tail_decay_r2: 0.03\n    h1_entropy_min_slope: -0.012\n    h1_entropy_min_r2: 0.06\n    median_ppl_by_depth:\n    - 13.5\n    - 4.96\n    - 3.0\n    - 2.07\n    - 1.72\n    ppl_kruskal_wallis_p: <0.001\n  result_rationale: 'Within-generator results remain strong because Pythia-410M reference\n    model is architecturally aligned with the Pythia-2.8B generator, maximizing NLL\n    feature sensitivity. The 0.06 full-surface gap confirms reference features add\n    independent value — entropy_mean captures distributional compression that surface\n    statistics miss. H2 features (entropy_mean, TTR, hapax_ratio) drift because recursive\n    generation compounds vocabulary impoverishment and entropy compression — each\n    step feeds an increasingly constrained output distribution back as input. H1 features\n    (shape statistics like entropy_std, tail_decay) remain stable because distributional\n    shape is determined by the generator''s softmax geometry, not the input content\n    — recursive generation shifts the location (mean) of the NLL distribution but\n    not its spread or tail behavior. Perplexity shows steep monotonic decline because\n    deeper generations become more predictable to the reference model as they converge\n    toward the generator''s mode.\n\n    '\n  tables:\n  - name: 'Table 1: Feature Ablation (5-fold CV, Pythia-2.8B, N=4609)'\n    columns:\n    - feature_set\n    - macro_f1\n    - 95% CI\n    - gen0_f1\n    - gen1_f1\n    - gen2plus_f1\n    rows:\n    - - Full (7 features)\n      - 0.82\n      - '[0.804, 0.836]'\n      - 0.94\n      - 0.77\n      - 0.79\n    - - Surface only (TTR + hapax)\n      - 0.76\n      - '[0.747, 0.774]'\n      - 0.91\n      - 0.7\n      - 0.72\n    - - Reference only (5 NLL)\n      - 0.72\n      - '[0.706, 0.733]'\n      - 0.88\n      - 0.65\n      - 0.67\n    - - Chance baseline\n      - 0.33\n      - —\n      - 0.33\n      - 0.33\n      - 0.33\n  - name: 'Table 2: H1/H2 Trend Regression per Feature'\n    columns:\n    - feature\n    - slope\n    - R²\n    - p_value\n    - classification\n    rows:\n    - - entropy_mean\n      - -0.148\n      - 0.93\n      - <0.001\n      - H2 (drift)\n    - - TTR\n      - -0.071\n      - 0.87\n      - <0.001\n      - H2 (drift)\n    - - hapax_ratio\n      - -0.054\n      - 0.81\n      - <0.001\n      - H2 (drift)\n    - - entropy_std\n      - 0.003\n      - 0.02\n      - 0.41\n      - H1 (stationary)\n    - - entropy_max\n      - -0.009\n      - 0.04\n      - 0.28\n      - H1 (stationary)\n    - - tail_decay\n      - 0.005\n      - 0.03\n      - 0.33\n      - H1 (stationary)\n    - - entropy_min\n      - -0.012\n      - 0.06\n      - 0.19\n      - H1 (stationary)\n  figures_description:\n  - 'Fig 1: 7-panel feature trend plot (mean ± std) across depths 0-4. H2 features\n    show clear monotonic decline; H1 features show flat profiles with overlapping\n    error bands. Visual separation between H1 and H2 behavior is stark.'\n  - 'Fig 2: Perplexity distribution boxplots by depth (0-4). Dramatic compression\n    from depth 0 (median 13.5) to depth 4 (median 1.72), confirming depth-correlated\n    distributional shift.'\n  analysis: 'Results confirm the H1/H2 split on MVP data. The 0.06 full-vs-surface\n    gap is statistically significant (bootstrap CIs non-overlapping), establishing\n    that reference features capture complementary signal. However, this is within-generator\n    with same-family reference model — the gap''s robustness must be tested cross-generator\n    (plan_002) and cross-reference (plan_003). The steep perplexity gradient validates\n    Claim 3''s premise: depth correlates with distributional properties detectable\n    by a reference model.\n\n    '\n- name: cross_generator_evaluation\n  plan_id: plan_002\n  description: '5-generator LOGO evaluation: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B,\n    Qwen3-0.6B. 1000 seeds per generator × 5 depths. Leave-one-generator-out and leave-one-family-out\n    CV.\n\n    '\n  expected_results:\n    logo_mean_macro_f1: 0.64\n    logo_holdout_pythia28b_f1: 0.71\n    logo_holdout_pythia1b_f1: 0.72\n    logo_holdout_olmo2_f1: 0.6\n    logo_holdout_qwen17b_f1: 0.62\n    logo_holdout_qwen06b_f1: 0.59\n    lofo_holdout_pythia_family_f1: 0.58\n    lofo_holdout_olmo_family_f1: 0.61\n    lofo_holdout_qwen_family_f1: 0.59\n    lofo_mean_f1: 0.593\n    within_generator_pooled_5fold_f1: 0.78\n    logo_full_feature_f1: 0.64\n    logo_surface_only_f1: 0.61\n    logo_reference_only_f1: 0.58\n    logo_full_vs_surface_gap: 0.03\n    logo_full_vs_reference_gap: 0.06\n    total_chains_generated: 23847\n    total_chains_after_attrition: 21503\n  result_rationale: 'Cross-generator F1 drops from 0.82 (within-generator) to 0.64\n    (LOGO) because each generator family imprints family-specific distributional signatures\n    beyond the depth signal. Pythia holdouts score higher (0.71-0.72) because Pythia-1B\n    and Pythia-2.8B share architectural biases (tokenizer, attention patterns, pretraining\n    data overlap) — when one is held out, the other provides a close proxy in the\n    training set. OLMo and Qwen holdouts score lower (0.59-0.62) because they represent\n    genuinely out-of-distribution generator families with different tokenizers and\n    pretraining distributions. The full-vs-surface gap narrows from 0.06 to 0.03 because\n    reference features (computed with Pythia-410M) are partially Pythia-biased: they\n    extract richer signal from Pythia-generated text than from OLMo/Qwen-generated\n    text, eroding their cross-family advantage. Leave-one-family-out results (mean\n    0.593) are lower than LOGO (0.64) because LOGO benefits from same-family generators\n    remaining in training. The within-generator pooled F1 (0.78) is lower than MVP''s\n    0.82 because pooling heterogeneous generators introduces inter-generator variance\n    that the classifier must absorb.\n\n    '\n  tables:\n  - name: 'Table 3: Leave-One-Generator-Out Results (Full Features)'\n    columns:\n    - held_out_generator\n    - family\n    - macro_f1\n    - gen0_f1\n    - gen1_f1\n    - gen2plus_f1\n    rows:\n    - - Pythia-2.8B\n      - Pythia\n      - 0.71\n      - 0.87\n      - 0.64\n      - 0.66\n    - - Pythia-1B\n      - Pythia\n      - 0.72\n      - 0.88\n      - 0.66\n      - 0.67\n    - - OLMo-2-1B\n      - OLMo\n      - 0.6\n      - 0.79\n      - 0.51\n      - 0.53\n    - - Qwen3-1.7B\n      - Qwen\n      - 0.62\n      - 0.82\n      - 0.53\n      - 0.55\n    - - Qwen3-0.6B\n      - Qwen\n      - 0.59\n      - 0.78\n      - 0.5\n      - 0.51\n    - - Mean LOGO\n      - —\n      - 0.64\n      - 0.83\n      - 0.57\n      - 0.58\n  - name: 'Table 4: Leave-One-Family-Out Results'\n    columns:\n    - held_out_family\n    - generators_in_family\n    - macro_f1\n    - 95% CI\n    rows:\n    - - Pythia\n      - 2.8B + 1B\n      - 0.58\n      - '[0.55, 0.61]'\n    - - OLMo\n      - OLMo-2-1B\n      - 0.61\n      - '[0.57, 0.64]'\n    - - Qwen\n      - 1.7B + 0.6B\n      - 0.59\n      - '[0.56, 0.62]'\n  - name: 'Table 5: Feature Ablation in Cross-Generator Setting (LOGO)'\n    columns:\n    - feature_set\n    - logo_macro_f1\n    - gap_vs_full\n    rows:\n    - - Full\n      - 0.64\n      - —\n    - - Surface only\n      - 0.61\n      - -0.03\n    - - Reference only\n      - 0.58\n      - -0.06\n  figures_description:\n  - 'Fig 3: LOGO F1 heatmap — rows are held-out generators, columns are depth classes\n    (gen-0/1/2+). Clear diagonal pattern: within-family holdouts (Pythia-2.8B, Pythia-1B)\n    are warmer; cross-family (OLMo, Qwen) are cooler, especially for gen-1 and gen-2+.'\n  - 'Fig 4: Confusion matrices for best (Pythia-1B holdout, F1=0.72) and worst (Qwen-0.6B\n    holdout, F1=0.59) LOGO folds. Worst case shows gen-1/gen-2+ confusion concentrated\n    in cross-family.'\n  analysis: 'LOGO F1=0.64 is within the median range [0.58, 0.70] and confirms moderate\n    cross-generator generalization. The within-family vs cross-family gap (~0.12)\n    reveals that distributional features partially encode generator identity, not\n    just depth. This constrains Claim 1 to ''depth discriminability generalizes within\n    model family; cross-family generalization is moderate and requires further work.''\n    The narrowing full-vs-surface gap (0.03 vs 0.06 within-generator) suggests reference\n    features lose their relative advantage in the cross-generator setting — likely\n    because the Pythia-410M reference model is better calibrated for Pythia-family\n    generators. This motivates plan_003 to test non-Pythia reference models.\n\n    '\n- name: cross_family_reference_model\n  plan_id: plan_003\n  description: 'Recompute NLL features using non-Pythia reference models (OLMo-2-1B,\n    Qwen3-0.6B) on existing plan_002 data. Test whether entropy_mean H2 drift and\n    shape feature H1 stationarity persist. Key falsification test for Claim 2.\n\n    '\n  expected_results:\n    pythia410m_ref_entropy_mean_rho: -0.68\n    olmo2_ref_entropy_mean_rho: -0.42\n    qwen06b_ref_entropy_mean_rho: -0.36\n    pythia410m_ref_full_f1: 0.82\n    olmo2_ref_full_f1: 0.78\n    qwen06b_ref_full_f1: 0.76\n    olmo2_ref_shape_max_abs_rho: 0.11\n    qwen06b_ref_shape_max_abs_rho: 0.09\n    pythia410m_ref_shape_max_abs_rho: 0.08\n    olmo2_ref_entropy_std_rho: 0.06\n    olmo2_ref_tail_decay_rho: -0.11\n    qwen06b_ref_entropy_std_rho: -0.04\n    qwen06b_ref_tail_decay_rho: 0.09\n    cross_ref_logo_f1_olmo_ref: 0.61\n    cross_ref_logo_f1_qwen_ref: 0.58\n  result_rationale: 'Entropy_mean drift attenuates (|ρ| drops from 0.68 to 0.36-0.42)\n    because the drift magnitude depends on how well the reference model''s learned\n    distribution aligns with the generator''s mode. Pythia-410M shares architecture\n    and pretraining data with Pythia-2.8B, amplifying NLL sensitivity to the generator''s\n    recursive drift. Non-Pythia references (OLMo, Qwen) have different internal distributions,\n    so the NLL mean shifts less per depth step — the drift still exists (recursive\n    generation objectively compresses the output distribution regardless of who measures\n    it) but the reference model''s measurement sensitivity is lower. Shape features\n    remain H1 (|ρ|<0.12) across all references because distributional shape (variance,\n    tail behavior) is a property of the generator''s softmax output geometry, which\n    doesn''t change with the reference model — different reference models shift the\n    NLL baseline but preserve relative shape statistics. Classification F1 drops moderately\n    because attenuated entropy_mean signal provides less discriminative power for\n    the ordinal depth task.\n\n    '\n  tables:\n  - name: 'Table 6: Entropy_mean Drift (ρ) by Reference Model'\n    columns:\n    - reference_model\n    - entropy_mean_rho\n    - p-value\n    - classification_full_f1\n    rows:\n    - - Pythia-410M\n      - -0.68\n      - <0.001\n      - 0.82\n    - - OLMo-2-1B\n      - -0.42\n      - <0.001\n      - 0.78\n    - - Qwen3-0.6B\n      - -0.36\n      - <0.001\n      - 0.76\n  - name: 'Table 7: Shape Feature Stationarity Across References (max |ρ|)'\n    columns:\n    - reference_model\n    - entropy_std_rho\n    - entropy_max_rho\n    - tail_decay_rho\n    - max_abs_rho\n    rows:\n    - - Pythia-410M\n      - 0.03\n      - -0.05\n      - 0.04\n      - 0.08\n    - - OLMo-2-1B\n      - 0.06\n      - -0.08\n      - -0.11\n      - 0.11\n    - - Qwen3-0.6B\n      - -0.04\n      - 0.07\n      - 0.09\n      - 0.09\n  figures_description:\n  - 'Fig 5: Entropy_mean trend lines (depth 0-4) for three reference models. Pythia-410M\n    shows steepest decline; OLMo-2-1B intermediate; Qwen3-0.6B shallowest. All three\n    monotonically decreasing but with different slopes.'\n  - 'Fig 6: Shape feature (entropy_std, tail_decay) trend lines across reference models\n    — three nearly flat lines per feature, confirming H1 robustness is reference-model-invariant.'\n  analysis: 'Dual dynamics survives but is reference-model-modulated. The level/shape\n    split is real across all references (H2 features always drift, H1 features always\n    stable), but drift magnitude varies 2x depending on reference model choice. This\n    softens Claim 2 from ''dual dynamics as universal law'' to ''reference-model-modulated\n    dual dynamics'' — the split is intrinsic to what the feature measures (central\n    tendency vs shape), but the signal strength depends on reference-generator alignment.\n    Paper must present this honestly and discuss implications for practical deployment\n    (reference model selection matters). The cross-reference LOGO F1 (0.58-0.61) shows\n    that non-Pythia references still support depth estimation, just with reduced accuracy.\n\n    '\n- name: downstream_utility\n  plan_id: plan_004\n  description: 'Fine-tune OLMo-1B on depth-stratified data. 3 seeds with bootstrap\n    CIs. Compare depth-aware filtering (keep gen-0 + gen-1) vs binary baselines (FastDetectGPT,\n    LD-Score threshold). Sample-count-matched comparison to control for data size\n    confound.\n\n    '\n  expected_results:\n    seeds_run: 3\n    depth_quality_spearman_rho: 0.53\n    depth_quality_spearman_ci: '[0.41, 0.64]'\n    ppl_gen0_only: 18.4\n    ppl_gen0_plus_gen1: 19.1\n    ppl_gen0_plus_gen1_plus_gen2plus: 21.7\n    ppl_unfiltered: 22.3\n    depth_filtering_ppl_improvement_pct: 5.2\n    depth_filtering_ppl_improvement_ci: '[3.8, 7.1]'\n    binary_fastdetectgpt_ppl_improvement_pct: 3.8\n    binary_fastdetectgpt_ppl_improvement_ci: '[2.1, 5.9]'\n    binary_ldscore_ppl_improvement_pct: 3.2\n    binary_ldscore_ppl_improvement_ci: '[1.6, 5.3]'\n    sample_matched_depth_improvement_pct: 2.8\n    sample_matched_binary_improvement_pct: 1.9\n    ci_overlap_with_best_binary: true\n    downstream_task_accuracy_depth: 0.724\n    downstream_task_accuracy_binary: 0.711\n    downstream_task_accuracy_unfiltered: 0.698\n  result_rationale: 'Depth-quality correlation (ρ=0.53) is moderate because OLMo-1B\n    is somewhat robust to moderate contamination — gen-1 data is only mildly degraded\n    (perplexity shift from 18.4 to 19.1), so the correlation is driven primarily by\n    the gen-2+ tail where distributional drift accumulates. Depth-aware filtering\n    outperforms binary filtering by ~1.4% because it retains gen-1 data that binary\n    detectors discard — gen-1 text is close to human-quality and contributes positively\n    to training. However, CI overlap exists because: (1) the advantage is small in\n    absolute terms, (2) 3 seeds produce wide CIs, and (3) FastDetectGPT''s false negative\n    rate on gen-1 means it sometimes keeps useful gen-1 data by accident. Sample-matched\n    comparison (controlling for the data size advantage of depth-aware filtering)\n    reduces the gap further to 0.9%, confirming that roughly half the advantage comes\n    from retaining more training data, not from better selection. The effect is real\n    but modest — insufficient for a strong ''significantly outperforms'' claim.\n\n    '\n  tables:\n  - name: 'Table 8: Downstream Perplexity by Training Data Composition (OLMo-1B, 3\n      seeds)'\n    columns:\n    - training_data\n    - n_samples\n    - mean_ppl\n    - std_ppl\n    - 95% CI\n    rows:\n    - - gen-0 only\n      - 4850\n      - 18.4\n      - 0.3\n      - '[17.9, 18.9]'\n    - - gen-0 + gen-1\n      - 9700\n      - 19.1\n      - 0.4\n      - '[18.5, 19.7]'\n    - - gen-0 + gen-1 + gen-2+\n      - 18200\n      - 21.7\n      - 0.6\n      - '[20.8, 22.6]'\n    - - Unfiltered (all depths)\n      - 21500\n      - 22.3\n      - 0.5\n      - '[21.5, 23.1]'\n  - name: 'Table 9: Filtering Strategy Comparison'\n    columns:\n    - strategy\n    - kept_samples\n    - ppl_improvement_pct\n    - 95% CI\n    - overlap_with_depth\n    rows:\n    - - Depth-aware (gen-0+gen-1)\n      - 9700\n      - 5.2\n      - '[3.8, 7.1]'\n      - —\n    - - FastDetectGPT binary\n      - 7300\n      - 3.8\n      - '[2.1, 5.9]'\n      - 'yes'\n    - - LD-Score binary\n      - 6900\n      - 3.2\n      - '[1.6, 5.3]'\n      - 'yes'\n    - - Sample-matched depth\n      - 7300\n      - 2.8\n      - '[1.4, 4.5]'\n      - —\n    - - Sample-matched binary\n      - 7300\n      - 1.9\n      - '[0.5, 3.6]'\n      - —\n  figures_description:\n  - 'Fig 7: Perplexity degradation curve as function of training data depth composition\n    (0-4). Clear upward trend with error bars (3 seeds). gen-0→gen-1 step is small;\n    gen-1→gen-2+ is the main inflection point.'\n  - 'Fig 8: Bootstrap CI comparison — depth-aware vs binary filtering perplexity improvement.\n    Point estimates favor depth-aware, but CI bars overlap for FastDetectGPT.'\n  analysis: 'Downstream utility exists but the advantage over binary filtering is\n    modest (1.4% mean, CIs overlap). Claim 3 must be softened to ''depth-aware filtering\n    offers complementary signal to binary detection'' — the value proposition is not\n    raw performance but the ability to retain useful gen-1 data while filtering harmful\n    gen-2+. Sample-matched analysis shows roughly half the gain is from data volume,\n    not selection quality. Paper should present this honestly and emphasize the interpretability\n    advantage: depth scores provide a continuous risk metric that binary labels cannot.\n\n    '\n- name: prompt_type_comparison\n  plan_id: plan_005\n  description: 'Compare depth signal across three prompt types: continuation, elaboration,\n    inspired_rewriting. 1000 seeds × Pythia-2.8B × 5 depths × 3 prompt types.\n\n    '\n  expected_results:\n    continuation_macro_f1: 0.82\n    elaboration_macro_f1: 0.77\n    inspired_rewriting_macro_f1: 0.69\n    continuation_entropy_mean_rho: -0.68\n    elaboration_entropy_mean_rho: -0.57\n    inspired_rewriting_entropy_mean_rho: -0.39\n    continuation_ttr_slope: -0.071\n    elaboration_ttr_slope: -0.058\n    inspired_rewriting_ttr_slope: -0.031\n    h1_features_stable_across_prompts: true\n  result_rationale: 'Continuation preserves the strongest depth signal because each\n    step feeds the previous output directly, maximizing distributional drift accumulation.\n    Elaboration introduces a semantic reframing prompt that partially resets the generator''s\n    conditioning, attenuating the chain''s compounding effect — the generator still\n    uses the previous text but the prompt steers it toward a different discourse structure,\n    reducing the monotonic drift. Inspired rewriting is most disruptive because the\n    generator is asked to produce content ''inspired by'' rather than continuing from\n    the previous text — this creates a loose semantic link but breaks the tight distributional\n    chain, so depth-0 vs depth-2 texts can have similar distributional properties\n    if the generator happens to produce fluent rewrites. H1 features remain stable\n    across all prompt types because shape stationarity is a property of the generator''s\n    output distribution, not the input conditioning.\n\n    '\n  tables:\n  - name: 'Table 10: Depth Classification by Prompt Type (Pythia-2.8B, 5-fold CV)'\n    columns:\n    - prompt_type\n    - macro_f1\n    - entropy_mean_rho\n    - ttr_slope\n    - semantic_divergence_cosine\n    rows:\n    - - Continuation\n      - 0.82\n      - -0.68\n      - -0.071\n      - 0.85\n    - - Elaboration\n      - 0.77\n      - -0.57\n      - -0.058\n      - 0.72\n    - - Inspired rewriting\n      - 0.69\n      - -0.39\n      - -0.031\n      - 0.54\n  figures_description:\n  - 'Fig 9: Feature drift magnitude by prompt type — bar chart showing H2 feature\n    slopes for each prompt type. Clear gradient from continuation (steepest) to inspired\n    rewriting (shallowest).'\n  analysis: 'Semantic divergence from source anti-correlates with depth signal preservation.\n    Continuation is the ideal setting for depth estimation; inspired rewriting represents\n    a harder, more realistic scenario where depth signal partially dissolves. This\n    informs ecological validity discussions: real-world LLM contamination likely involves\n    a mix of prompt types, placing practical performance between 0.69-0.82.\n\n    '\n- name: paraphrastic_comparison\n  plan_id: plan_006\n  description: 'Parallel paraphrasing chains vs continuation chains for direct comparison.\n    Tests attractor convergence theory — paraphrastic chains should saturate earlier.\n\n    '\n  expected_results:\n    paraphrastic_3class_f1: 0.66\n    nonparaphrastic_3class_f1: 0.82\n    paraphrastic_gen2plus_f1: 0.41\n    nonparaphrastic_gen2plus_f1: 0.79\n    paraphrastic_5class_f1: 0.29\n    nonparaphrastic_5class_f1: 0.43\n    paraphrastic_entropy_mean_rho: -0.34\n    nonparaphrastic_entropy_mean_rho: -0.68\n    paraphrastic_signal_saturation_depth: 2\n    nonparaphrastic_signal_saturation_depth: 4\n  result_rationale: 'Paraphrastic chains converge to attractor cycles (ACL 2025 theory),\n    bounding depth signal to ~2 distinguishable classes — by depth-2, paraphrased\n    text has already entered the attractor basin, so gen-2/gen-3/gen-4 become distributionally\n    indistinguishable. This collapses gen-2+ F1 to near-chance (0.41). Non-paraphrastic\n    continuation chains escape the attractor because each step generates genuinely\n    new content rather than cycling through semantically equivalent rewrites. Distributional\n    drift accumulates monotonically through depth-4, preserving ordinal signal. The\n    paraphrastic entropy_mean ρ (-0.34) is weaker because the drift saturates early\n    — depths 2-4 contribute noise, not signal, to the correlation. This directly validates\n    the paper''s premise: non-paraphrastic chains are the right focus for depth estimation\n    because the attractor convergence bound does not apply.\n\n    '\n  tables:\n  - name: 'Table 11: Paraphrastic vs Non-paraphrastic Depth Classification'\n    columns:\n    - chain_type\n    - 3class_f1\n    - gen0_f1\n    - gen1_f1\n    - gen2plus_f1\n    - signal_saturation_depth\n    rows:\n    - - Paraphrastic\n      - 0.66\n      - 0.89\n      - 0.67\n      - 0.41\n      - 2\n    - - Non-paraphrastic\n      - 0.82\n      - 0.94\n      - 0.77\n      - 0.79\n      - 4+\n  figures_description:\n  - 'Fig 10: Per-depth F1 curves for paraphrastic (flattens at depth 2) vs non-paraphrastic\n    (gradual decline through depth 4). Clear visual separation demonstrating attractor\n    saturation vs sustained drift.'\n  analysis: 'Confirms the theoretical motivation: paraphrastic chains hit the attractor\n    bound at depth ~2, while non-paraphrastic chains maintain discriminable depth\n    signal through depth 4. This justifies the paper''s focus on continuation chains\n    and connects to attractor cycle theory as a boundary condition rather than a general\n    limit on depth estimation.\n\n    '\n- name: cross_model_chains\n  plan_id: plan_007\n  description: 'Cross-model chains (different generator per depth step) vs single-model\n    chains. Tests ecological validity for real web contamination scenarios.\n\n    '\n  expected_results:\n    cross_model_logo_f1: 0.56\n    single_model_logo_f1: 0.64\n    cross_model_within_f1: 0.68\n    cross_model_entropy_mean_rho: -0.41\n    cross_model_ttr_slope: -0.039\n    cross_model_h1_stable: true\n    cross_model_gen0_f1: 0.78\n    cross_model_gen1_f1: 0.46\n    cross_model_gen2plus_f1: 0.44\n  result_rationale: 'Cross-model chains inject between-model distributional variance\n    at each depth step. When generator changes between depths (e.g., Pythia→OLMo→Qwen),\n    the NLL features measured by the reference model reflect not just depth-related\n    drift but also generator-switching effects — the reference model''s NLL for OLMo-generated\n    text differs from Pythia-generated text regardless of depth. This noise source\n    partially masks the depth signal, particularly for gen-1 vs gen-2+ where the depth\n    effect is smaller than the generator effect. Gen-0 (human) remains well-separated\n    (F1 0.78) because all chains share the same human seed distribution. The F1 drop\n    from 0.64 (single-model LOGO) to 0.56 (cross-model) quantifies the cost of realistic\n    generator diversity. H1 features remain stable even in cross-model chains, confirming\n    that shape stationarity is generator-intrinsic.\n\n    '\n  tables:\n  - name: 'Table 12: Cross-model vs Single-model Chain Classification'\n    columns:\n    - chain_type\n    - logo_f1\n    - gen0_f1\n    - gen1_f1\n    - gen2plus_f1\n    - entropy_mean_rho\n    rows:\n    - - Single-model\n      - 0.64\n      - 0.83\n      - 0.57\n      - 0.58\n      - -0.68\n    - - Cross-model\n      - 0.56\n      - 0.78\n      - 0.46\n      - 0.44\n      - -0.41\n  figures_description:\n  - 'Fig 11: Confusion matrices for cross-model chains — gen-1/gen-2+ are heavily\n    confused due to generator-switching noise dominating depth signal.'\n  analysis: 'Cross-model chains degrade depth estimation significantly (-0.08 F1).\n    This is a realistic limitation: web contamination involves diverse generators,\n    and the current feature set partially conflates generator identity with depth.\n    Paper should present this as an honest ecological validity test — depth estimation\n    is most reliable for single-source contamination, and cross-model scenarios require\n    future work on generator-invariant features.\n\n    '\n- name: multi_domain_seeds\n  plan_id: plan_008\n  description: 'Expand to 4 domains: Wikipedia, news (CNN/DM), scientific (S2ORC),\n    creative (WritingPrompts). 500 seeds per domain × 5 depths × 5 generators.\n\n    '\n  expected_results:\n    wikipedia_logo_f1: 0.67\n    news_logo_f1: 0.64\n    scientific_logo_f1: 0.62\n    creative_logo_f1: 0.57\n    pooled_multidomain_logo_f1: 0.63\n    domain_f1_std: 0.037\n    wikipedia_entropy_mean_rho: -0.72\n    creative_entropy_mean_rho: -0.48\n    cross_domain_train_test_f1: 0.58\n  result_rationale: 'Wikipedia seeds yield highest F1 (0.67) because Wikipedia prose\n    is stylistically uniform and formulaic — generators produce characteristically\n    homogeneous continuations that maximize distributional drift consistency across\n    depths. Creative writing seeds yield lowest F1 (0.57) because creative text has\n    high intrinsic variance (diverse styles, tones, registers), which creates a larger\n    noise floor that depth signal must overcome. The generator''s creative outputs\n    at depth-1 can be as distributionally diverse as human creative text, blurring\n    the gen-0/gen-1 boundary. Scientific text (0.62) occupies the middle ground: constrained\n    register but technical vocabulary creates complex distributional patterns. Cross-domain\n    train-test (train on 3 domains, test on 1) drops to 0.58, suggesting partial domain\n    adaptation in the classifier.\n\n    '\n  tables:\n  - name: 'Table 13: Domain-Specific LOGO Results'\n    columns:\n    - domain\n    - logo_f1\n    - entropy_mean_rho\n    - ttr_slope\n    - n_seeds\n    rows:\n    - - Wikipedia\n      - 0.67\n      - -0.72\n      - -0.078\n      - 500\n    - - News (CNN/DM)\n      - 0.64\n      - -0.63\n      - -0.065\n      - 500\n    - - Scientific (S2ORC)\n      - 0.62\n      - -0.58\n      - -0.059\n      - 500\n    - - Creative (WritingPrompts)\n      - 0.57\n      - -0.48\n      - -0.041\n      - 500\n    - - Pooled\n      - 0.63\n      - -0.6\n      - -0.061\n      - 2000\n  figures_description:\n  - 'Fig 12: Domain-specific entropy_mean drift plots — four panels showing depth\n    0-4 trends. Wikipedia shows tightest confidence bands; creative shows widest.'\n  analysis: 'Domain variation (std 0.037) is non-trivial but depth signal generalizes\n    across all four domains. Creative writing is the hardest domain, consistent with\n    high intrinsic variance. Paper should report pooled results as primary and domain-specific\n    as supplementary analysis, noting that domain adaptation (train/test domain mismatch)\n    is an additional challenge beyond generator generalization.\n\n    '\n- name: finer_grained_ordinal\n  plan_id: plan_009\n  description: '5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic\n    chains. Tests whether depth signal supports finer than 3-class resolution.\n\n    '\n  expected_results:\n    five_class_macro_f1: 0.43\n    five_class_gen0_f1: 0.73\n    five_class_gen1_f1: 0.52\n    five_class_gen2_f1: 0.35\n    five_class_gen3_f1: 0.29\n    five_class_gen4_f1: 0.28\n    ordinal_mae: 0.72\n    three_class_macro_f1_same_data: 0.64\n    adjacent_confusion_rate: 0.61\n    spearman_pred_vs_true: 0.74\n  result_rationale: '5-class F1 (0.43) drops substantially from 3-class (0.64) because\n    distributional differences between adjacent depths (gen-2 vs gen-3, gen-3 vs gen-4)\n    are small — the drift per step is roughly constant, but the cumulative difference\n    between gen-0 and gen-4 is spread across 4 boundaries, each of which is harder\n    than the 3-class boundaries. Gen-0 is still well-separated (0.73) because human\n    vs any synthetic is the largest distributional gap. Gen-1 (0.52) is intermediate\n    — distinguishable from gen-0 and gen-2+ but with confusion on both sides. Gen-2/3/4\n    collapse into a muddy cluster (F1 0.28-0.35) because by depth-2, recursive drift\n    has already consumed most of the easy-to-detect signal, and remaining differences\n    are within the noise floor. However, ordinal Spearman (0.74) is respectable, showing\n    the classifier preserves rank order even when exact class assignment fails — errors\n    are predominantly between adjacent classes (61% of errors), not distant ones.\n\n    '\n  tables:\n  - name: 'Table 14: 5-class Ordinal Classification (LOGO, Full Features)'\n    columns:\n    - class\n    - f1\n    - precision\n    - recall\n    - most_confused_with\n    rows:\n    - - gen-0\n      - 0.73\n      - 0.78\n      - 0.69\n      - gen-1\n    - - gen-1\n      - 0.52\n      - 0.49\n      - 0.55\n      - gen-0 / gen-2\n    - - gen-2\n      - 0.35\n      - 0.33\n      - 0.37\n      - gen-3\n    - - gen-3\n      - 0.29\n      - 0.31\n      - 0.27\n      - gen-2 / gen-4\n    - - gen-4\n      - 0.28\n      - 0.26\n      - 0.3\n      - gen-3\n  figures_description:\n  - 'Fig 13: 5×5 confusion matrix heatmap — strong diagonal for gen-0, increasingly\n    diffuse for deeper classes. Off-diagonal mass concentrated on ±1 adjacent cells.'\n  - 'Fig 14: Predicted vs true depth scatter with ordinal regression line (Spearman\n    ρ=0.74).'\n  analysis: 'Finer-grained classification is feasible but noisy beyond 3 classes.\n    The 3-class grouping (gen-0/gen-1/gen-2+) appears to be the natural resolution\n    supported by the current feature set. Paper presents 5-class as secondary analysis\n    motivating ordinal regression approaches in future work. The high ordinal Spearman\n    (0.74) suggests the classifier captures depth ordering even when exact classification\n    fails, which is useful for risk scoring applications.\n\n    '\n- name: human_edit_robustness\n  plan_id: plan_010\n  description: 'Robustness to simulated human edits: (A) random word replacement at\n    5%/10%/20%, (B) LLM-simulated light rephrasing. Tests whether post-processing\n    destroys depth signal.\n\n    '\n  expected_results:\n    baseline_no_edit_f1: 0.82\n    random_5pct_f1: 0.79\n    random_10pct_f1: 0.72\n    random_20pct_f1: 0.6\n    llm_light_edit_f1: 0.73\n    random_5pct_entropy_mean_rho: -0.63\n    random_10pct_entropy_mean_rho: -0.52\n    random_20pct_entropy_mean_rho: -0.35\n    llm_light_edit_entropy_mean_rho: -0.49\n    h1_features_robust_to_edit: true\n    shape_features_max_rho_change: 0.07\n  result_rationale: 'Random word replacement progressively corrupts the text''s distributional\n    profile. At 5%, the corruption is below the feature noise floor — surface features\n    (TTR, hapax) are slightly perturbed but NLL features remain stable because 5%\n    random words don''t substantially alter the reference model''s token-level surprise\n    distribution. At 20%, the text becomes distributionally anomalous in a way that\n    overwhelms the depth signal — randomly inserted words create a uniform noise pattern\n    that masks depth-specific distributional drift. LLM-simulated editing (F1 0.73)\n    falls between 5% and 10% random replacement because LLM edits are more natural\n    (preserving grammaticality) but more targeted (selectively replacing awkward or\n    repetitive phrases that carry depth signal). Shape features remain robust (max\n    ρ change 0.07) because random/LLM edits affect vocabulary composition (level)\n    more than distributional shape.\n\n    '\n  tables:\n  - name: 'Table 15: Robustness to Simulated Human Edits'\n    columns:\n    - edit_type\n    - edit_rate\n    - macro_f1\n    - delta_f1\n    - entropy_mean_rho\n    rows:\n    - - None (baseline)\n      - 0%\n      - 0.82\n      - —\n      - -0.68\n    - - Random word\n      - 5%\n      - 0.79\n      - -0.03\n      - -0.63\n    - - Random word\n      - 10%\n      - 0.72\n      - -0.1\n      - -0.52\n    - - Random word\n      - 20%\n      - 0.6\n      - -0.22\n      - -0.35\n    - - LLM light rephrase\n      - ~8%\n      - 0.73\n      - -0.09\n      - -0.49\n  figures_description:\n  - 'Fig 15: F1 degradation curve as function of edit rate — roughly linear decline\n    with inflection around 15%. LLM editing point plotted at estimated ~8% token change\n    rate.'\n  analysis: 'Depth signal is moderately robust to light editing (5%) but degrades\n    meaningfully at 10%+. Real-world human editing likely falls in the 5-15% range,\n    placing expected performance at F1 0.72-0.79. Paper presents this as honest robustness\n    analysis — depth estimation is viable for lightly edited synthetic text but fragile\n    under heavy post-processing. This limits practical applicability to scenarios\n    where contamination involves minimally edited LLM outputs.\n\n    '\n- name: ld_score_feature\n  plan_id: plan_011\n  description: 'Add LD-Score as feature. Test pre-registered prediction that LD-Score\n    is a level feature (H2 drift). Evaluate marginal classification improvement.\n\n    '\n  expected_results:\n    ld_score_depth_rho: -0.55\n    ld_score_slope: -0.042\n    ld_score_r2: 0.72\n    ld_score_classification: H2_level\n    preregistered_prediction_confirmed: true\n    f1_with_ld_score: 0.83\n    f1_without_ld_score: 0.82\n    marginal_improvement: 0.01\n    ld_score_correlation_with_ttr: 0.68\n    ld_score_correlation_with_hapax: 0.61\n  result_rationale: 'LD-Score measures character-level distributional properties,\n    which are downstream of vocabulary composition — as depth increases and vocabulary\n    impoverishes (fewer unique words, more repetitive character n-grams), LD-Score\n    shifts accordingly. This confirms it is a level feature (H2), sensitive to the\n    same vocabulary/diversity drift as TTR and hapax_ratio. The pre-registered prediction\n    is validated (ρ=-0.55, clearly H2), strengthening the level/shape framework''s\n    predictive power. However, the high correlation with existing surface features\n    (0.61-0.68 with TTR/hapax) means LD-Score provides little incremental information\n    — the marginal F1 gain is only 0.01. The character-level signal is largely redundant\n    with word-level diversity features already in the feature set.\n\n    '\n  tables:\n  - name: 'Table 16: LD-Score Feature Analysis'\n    columns:\n    - metric\n    - value\n    rows:\n    - - LD-Score depth ρ\n      - -0.55\n    - - LD-Score linear slope\n      - -0.042\n    - - LD-Score R²\n      - 0.72\n    - - H1/H2 classification\n      - H2 (level)\n    - - Pre-registered prediction\n      - Confirmed\n    - - Correlation with TTR\n      - 0.68\n    - - Correlation with hapax_ratio\n      - 0.61\n    - - F1 with LD-Score\n      - 0.83\n    - - F1 without LD-Score\n      - 0.82\n  figures_description:\n  - 'Fig 16: LD-Score depth trend (mean ± std, depths 0-4) overlaid with TTR trend\n    — similar decline pattern, confirming shared level/diversity dynamics at character\n    level.'\n  analysis: 'Pre-registered prediction confirmed: LD-Score is a level feature. This\n    is a minor but clean validation of the H1/H2 framework''s predictive utility.\n    However, the marginal classification improvement is negligible (0.01), so LD-Score\n    is presented as a validation data point rather than a feature engineering contribution.\n    The high correlation with existing features suggests character-level and word-level\n    diversity measures capture the same underlying depth signal.\n\n    '\n- name: end_to_end_classifier\n  plan_id: plan_012\n  description: 'QLoRA fine-tuned Qwen3-0.6B for end-to-end depth classification. Compares\n    learned representations vs handcrafted distributional features.\n\n    '\n  expected_results:\n    qlora_macro_f1: 0.79\n    qlora_gen0_f1: 0.92\n    qlora_gen1_f1: 0.73\n    qlora_gen2plus_f1: 0.72\n    handcrafted_macro_f1: 0.82\n    qlora_cross_gen_logo_f1: 0.61\n    handcrafted_cross_gen_logo_f1: 0.64\n    qlora_training_time_hours: 6.2\n    qlora_inference_tokens_per_sec: 145\n    handcrafted_inference_tokens_per_sec: 8900\n  result_rationale: 'QLoRA achieves slightly lower F1 (0.79 vs 0.82) because the depth\n    classification task has limited training data (~25K samples) — insufficient for\n    a 600M-parameter model to learn robust depth-specific representations from scratch.\n    The model likely overfits to generator- specific patterns rather than learning\n    the distributional drift abstraction that handcrafted features explicitly encode.\n    Cross-generator LOGO (0.61 vs 0.64) shows the end-to-end approach generalizes\n    slightly worse, further suggesting it memorizes generator identities. The handcrafted\n    approach also has a massive inference speed advantage (~60x) because it requires\n    only a forward pass through the small reference model + simple statistics, vs\n    full sequence processing through a 600M model. This confirms the paper''s positioning:\n    the contribution is the problem formulation and empirical findings, not a competition\n    for SOTA — simple features suffice for the task.\n\n    '\n  tables:\n  - name: 'Table 17: End-to-End vs Handcrafted Features'\n    columns:\n    - method\n    - within_gen_f1\n    - logo_f1\n    - inference_speed\n    - training_cost\n    rows:\n    - - Handcrafted (XGBoost)\n      - 0.82\n      - 0.64\n      - 8900 tok/s\n      - ~0 GPU-h\n    - - QLoRA (Qwen3-0.6B)\n      - 0.79\n      - 0.61\n      - 145 tok/s\n      - 6.2 GPU-h\n  figures_description:\n  - 'Fig 17: F1 comparison bar chart (within-gen and LOGO) for handcrafted vs QLoRA.\n    Handcrafted is slightly better on both metrics while being 60x faster at inference.'\n  analysis: 'End-to-end approach does not outperform handcrafted features, confirming\n    that the task''s information content is well-captured by simple distributional\n    statistics. This validates the paper''s contribution positioning: novelty lies\n    in the problem formulation and empirical findings, not in model architecture.\n    The interpretability and efficiency advantages of handcrafted features are a practical\n    benefit for deployment in data curation pipelines.\n\n    '\n- name: text_length_control\n  plan_id: plan_013\n  description: 'Length confound analysis: (A) length distributions by depth, (B) length-normalized\n    features, (C) length-matched classification. Critical confound control.\n\n    '\n  expected_results:\n    mean_length_gen0: 315\n    mean_length_gen1: 289\n    mean_length_gen2: 263\n    mean_length_gen3: 246\n    mean_length_gen4: 237\n    length_depth_pearson_r: -0.41\n    length_depth_kw_p: <0.001\n    original_surface_f1: 0.76\n    length_controlled_surface_f1: 0.71\n    length_controlled_surface_f1_delta: -0.05\n    original_reference_f1: 0.72\n    length_controlled_reference_f1: 0.7\n    length_controlled_reference_f1_delta: -0.02\n    original_full_f1: 0.82\n    length_controlled_full_f1: 0.78\n    length_controlled_full_f1_delta: -0.04\n    length_matched_subsample_full_f1: 0.79\n    fixed_window_ttr_slope: -0.048\n    fixed_window_ttr_original_slope: -0.071\n    fixed_window_hapax_slope: -0.037\n    fixed_window_hapax_original_slope: -0.054\n    residual_signal_confirmed: true\n  result_rationale: 'Text length decreases monotonically with depth (315→237 tokens)\n    because recursive generation tends to produce slightly shorter texts — generators\n    are biased toward completing thoughts within a typical output length, and each\n    depth step compounds this tendency. This creates a legitimate confound: TTR and\n    hapax_ratio are mechanically length-dependent (shorter texts have higher TTR/hapax\n    by construction). The -0.05 surface F1 drop after length control confirms that\n    ~30% of the surface feature signal was tracking length, not depth. However, the\n    residual signal (F1 0.71 after control, well above chance at 0.33) confirms that\n    depth drives genuine vocabulary impoverishment beyond what length explains. Reference\n    features lose less (-0.02) because NLL statistics are computed token-by-token\n    and are less length-sensitive — the per-token surprise distribution shifts with\n    depth regardless of total text length. The full-feature length-controlled F1 (0.78)\n    remains substantially above chance and above either feature subset, confirming\n    the core claims survive length control.\n\n    '\n  tables:\n  - name: 'Table 18: Text Length by Depth'\n    columns:\n    - depth\n    - mean_tokens\n    - std_tokens\n    - median_tokens\n    rows:\n    - - gen-0\n      - 315\n      - 82\n      - 298\n    - - gen-1\n      - 289\n      - 76\n      - 274\n    - - gen-2\n      - 263\n      - 71\n      - 251\n    - - gen-3\n      - 246\n      - 68\n      - 237\n    - - gen-4\n      - 237\n      - 65\n      - 228\n  - name: 'Table 19: Length-Controlled Classification Results'\n    columns:\n    - feature_set\n    - original_f1\n    - length_controlled_f1\n    - delta\n    - delta %\n    rows:\n    - - Full\n      - 0.82\n      - 0.78\n      - -0.04\n      - -4.9%\n    - - Surface only\n      - 0.76\n      - 0.71\n      - -0.05\n      - -6.6%\n    - - Reference only\n      - 0.72\n      - 0.7\n      - -0.02\n      - -2.8%\n  - name: 'Table 20: Fixed-Window Feature Slopes (128-token windows)'\n    columns:\n    - feature\n    - original_slope\n    - fixed_window_slope\n    - slope_reduction_pct\n    rows:\n    - - TTR\n      - -0.071\n      - -0.048\n      - 32%\n    - - hapax_ratio\n      - -0.054\n      - -0.037\n      - 31%\n    - - entropy_mean\n      - -0.148\n      - -0.139\n      - 6%\n  figures_description:\n  - 'Fig 18: Text length distribution violin plots by depth — clear leftward shift\n    with depth. Overlapping distributions confirm length is a partial, not sole, confound.'\n  - 'Fig 19: Feature slopes before/after length control — surface features show ~30%\n    reduction; reference features show <10% reduction. Visualizes the differential\n    length sensitivity.'\n  analysis: 'Length is a real but partial confound. The 0.05 surface F1 drop is within\n    the median range [-0.08, -0.03] and must be acknowledged honestly in the paper.\n    The key finding is that residual signal survives: depth drives genuine distributional\n    drift beyond length artifacts. Reference features are relatively length-robust\n    (only 0.02 drop), strengthening their value in the feature set. Paper should add\n    length-controlled analysis as a supplementary validation table and note: ''Surface\n    features partially track text length, but residual depth signal persists after\n    length control. Reference features provide length-robust complementary signal.''\n\n    '\n- name: large_scale_generator\n  plan_id: plan_014\n  description: 'Add Qwen3-8B-Base as 7B+ generator. 1000 seeds × 5 depths. Tests whether\n    depth signal persists at frontier scale.\n\n    '\n  expected_results:\n    qwen8b_3class_macro_f1: 0.57\n    qwen8b_gen0_f1: 0.76\n    qwen8b_gen1_f1: 0.48\n    qwen8b_gen2plus_f1: 0.46\n    qwen8b_entropy_mean_rho: -0.38\n    qwen8b_ttr_slope: -0.042\n    qwen8b_hapax_slope: -0.032\n    qwen8b_vs_pythia28b_f1_gap: -0.25\n    qwen8b_vs_qwen17b_f1_gap: -0.05\n    qwen8b_h1_features_stable: true\n    qwen8b_entropy_std_rho: 0.05\n    qwen8b_tail_decay_rho: -0.07\n    qwen8b_5class_f1: 0.31\n    logo_with_8b_included: 0.61\n  result_rationale: '7B+ generators produce substantially more fluent text that compresses\n    the depth signal. At 8B parameters, the model has sufficient capacity to maintain\n    diverse vocabulary and natural distributional properties even at depth-4 — vocabulary\n    impoverishment is less severe because the model''s larger vocabulary and richer\n    internal representations allow it to produce varied continuations even from distributionally\n    drifted inputs. The F1 drop from 0.82 (Pythia-2.8B) to 0.57 (Qwen3-8B) is large\n    but the signal remains non-trivial (well above chance at 0.33). Entropy_mean ρ\n    attenuates from -0.68 to -0.38, consistent with weaker but non-zero drift — the\n    8B model''s NLL distribution still shifts with depth but less per step. Gen-0\n    remains distinguishable (F1 0.76) because the human-vs-any-synthetic gap is robust\n    to model scale, but gen-1 vs gen-2+ becomes very noisy (0.46-0.48). H1 features\n    remain stable (shape stationarity is scale-invariant). This is an honest scaling\n    result: depth estimation weakens at scale but doesn''t vanish, motivating future\n    work on scale-robust features.\n\n    '\n  tables:\n  - name: 'Table 21: 7B+ Generator Depth Classification'\n    columns:\n    - generator\n    - params\n    - macro_f1\n    - entropy_mean_rho\n    - ttr_slope\n    rows:\n    - - Pythia-2.8B\n      - 2.8B\n      - 0.82\n      - -0.68\n      - -0.071\n    - - Pythia-1B\n      - 1B\n      - 0.8\n      - -0.65\n      - -0.068\n    - - OLMo-2-1B\n      - 1.5B\n      - 0.78\n      - -0.61\n      - -0.063\n    - - Qwen3-1.7B\n      - 1.7B\n      - 0.75\n      - -0.56\n      - -0.055\n    - - Qwen3-0.6B\n      - 0.6B\n      - 0.77\n      - -0.59\n      - -0.061\n    - - Qwen3-8B\n      - 8B\n      - 0.57\n      - -0.38\n      - -0.042\n  - name: 'Table 22: Scale Trend Analysis'\n    columns:\n    - metric\n    - ≤2.8B mean\n    - 8B\n    - delta\n    - interpretation\n    rows:\n    - - macro_f1\n      - 0.78\n      - 0.57\n      - -0.21\n      - Signal weakens at scale\n    - - entropy_mean ρ\n      - -0.62\n      - -0.38\n      - '+0.24'\n      - Drift attenuates at scale\n    - - TTR slope\n      - -0.064\n      - -0.042\n      - '+0.022'\n      - Less vocab impoverishment\n    - - H1 max |ρ|\n      - 0.08\n      - 0.07\n      - '-0.01'\n      - Shape stationarity preserved\n  figures_description:\n  - 'Fig 20: F1 vs generator parameter count (log scale). Clear downward trend from\n    0.6B-2.8B cluster to 8B outlier. Dotted line at chance (0.33) for reference.'\n  - 'Fig 21: Entropy_mean depth trend for 8B (shallow slope) vs 2.8B (steep slope).\n    Both monotonically decreasing but 8B slope is ~55% of 2.8B slope.'\n  analysis: '7B+ results confirm the scaling concern. Depth signal is weaker but non-zero\n    (F1 0.57, significantly above chance p<0.001). The paper should present this as\n    an honest scaling analysis in a dedicated subsection: ''Depth signal attenuates\n    with generator scale, consistent with larger models maintaining distributional\n    diversity under recursive generation. At 8B parameters, gen-0 vs synthetic remains\n    detectable, but fine-grained depth estimation (gen-1 vs gen-2+) approaches noise\n    floor. This motivates future work on scale-robust features, potentially leveraging\n    model-specific distributional properties.'' The 8B result transforms from a weakness\n    into a scientific finding: the relationship between model capacity and depth signal\n    decay is itself an interesting empirical contribution.'\n",
      "numLines": 1321,
      "startLine": 1,
      "totalLines": 1321
    }
  },
  "sourceToolAssistantUUID": "d47f2260-d971-41c2-96f1-1e75a7e03fc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分新家族 depth signal 退化（类似 Qwen3-8B 模式），泛化 claim 需收窄但核心贡献不变 核心假设：['3 个新家族中 1-2 个 held-out F1 < 0.60（类似 instruct 退化但不至于 chance level）', '扩展后 LOGO binary F1…",
  "leafUuid": "35ff09db-d6b6-46c4-b828-d5b8a386bdcb",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Median scenario paper framing for gen-depth-fingerprint",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

### Assistant

_source line 24 · 2026-05-16T11:11:05.373Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the format. Let me also check the meta.yaml for the latest dream report to understand the tier definition more precisely.

Now I need to create median-tier predictions. Looking at the planned experiments again:

From the experiment_plan.yaml status field:
- plan_001: feature_ablation_and_trend — **planned**
- plan_002: cross_generator_evaluation — **planned**
- plan_006: paraphrastic_comparison — **planned**
- plan_009: finer_grained_ordinal — **planned**


- plan_012: end_to_end_classifier — **planned**

The user's median tier definition shows some degradation in depth signal similar to Qwen3-8B patterns, with narrowed generalization claims but unchanged core contributions. I'm looking at the performance metrics they've specified: binary logo F1 should fall between 0.68 and 0.72, per-generator F1 standard deviation between 0.07 and 0.11, worst single generator F1 between 0.5 and 0.62, and the seven-feature versus best baseline performance ratio between 1.0 and 2.5.

Now examining the held-out family average F1 range of 0.55 to 0.68, along with drifting feature Spearman correlations between -0.55 and -0.2, and shape feature Spearman correlations between -0.2 and 0.2. The user wants me to generate median-tier predictions specifically for the planned experiments in the experiment_plan, so I need to identify which ones have that status and apply these metrics accordingly.

Looking through the experiment_plan, I can see the status breakdown: plan_001, plan_002, plan_006, plan_009, and plan_012 are marked as planned, while the rest are either DONE or have specific conclusions like the negative result for plan_004. I should focus my predictions on just those five planned experiments rather than generating data for the completed ones.

Now I'm thinking through what the median tier performance would look like for these planned experiments. The key metrics I need to consider are the binary logo F1 scores, the variability across generations, the worst-case single generation performance, how much better the approach is compared to baselines, the held-out performance on new families, and the range of correlation values for drifting features.

I'm laying out the specific hypotheses for the median tier: expecting that about half of the new families would have held-out F1 below 0.60, the expanded binary logo F1 would drop slightly to around 0.68-0.71, the advantage over the best baseline would narrow to just 1-2.5 percentage points, the differential response pattern would hold for most but not all families, and some families might show larger gaps across different scales or architectures than anticipated.

Now I need to work through each of the five planned experiments and construct realistic predictions that stay within these median ranges, making sure to ground them in the actual results from the completed experiments and explain why each metric falls where it does.

For plan_001, I'm analyzing the within-generator setup using Pythia-2.8B as the generator and Pythia-410M as the reference—this is the most favorable scenario since both models are from the same family. Even accounting for the median tier's general degradation patterns, this should still perform quite well because the degradation primarily affects new families, not the existing Pythia setup. The full macro F1 of 0.82 from the earlier prediction seems reasonable to keep for this median scenario.

Now for plan_002, this is where the median tier really matters. I'm evaluating across 5 different generators—2 Pythia, 1 OLMo, and 2 Qwen models—which introduces significant cross-generator variability. In the median tier, I'd expect the LOGO average F1 to drop compared to the best tier, with 1-2 new families falling below 0.60 F1, per-generator F1 standard deviation ranging from 0.07-0.11, and the worst-performing generator hitting somewhere between 0.50-0.62 F1. Let me check the actual results to see how these predictions align.

Looking at the registry data, the LOGO average is 0.8037 with pythia-1b at 0.8507 (best) and olmo-2-1b at 0.7519 (worst), while the Qwen models sit around 0.81-0.82. For the median tier, I need to set more conservative estimates—around 0.74 for LOGO average F1, roughly 0.58 for the worst single generator, and about 0.09 for per-generator F1 standard deviation. But I'm realizing this is a 5-generator LOGO evaluation without held-out data, which changes how I should interpret the median tier expectations.

Looking at the actual median tier indicators more carefully, the binary_logo_f1_expanded range of 0.68-0.72 appears to be for the expanded 6-generator evaluation that includes the 8B model. For the 5-generator setup in plan_002, the 3-class LOGO should probably land higher, around 0.75-0.78, and I need to recalibrate my estimates accordingly before considering what happens when the 8B generator gets added in plan_014.

Now I'm working through the median tier performance expectations for plan_002 itself. Some of the non-Pythia generators will likely underperform, particularly smaller variants like Qwen3-0.6B which might show similar degradation patterns we see at smaller scales. The 3-class LOGO average should sit around 0.76 with per-generator performance ranging from about 0.61 to 0.85, where OLMo or the smaller Qwen variant would be the weakest performers. But I need to reconsider how the new families beyond the MVP are actually defined and which ones fall below the 0.60 threshold in the median tier. Pythia, OLMo, Qwen. So 2 new families: OLMo and Qwen.

In plan_002 context, the "new families" that might have degradation would be OLMo and Qwen. In median, 1 of these 2 families has held-out F1 < 0.60.

Let me set up plan_002 median predictions:
- LOGO avg 3-class F1: ~0.76
- pythia-2.8b held-out: 0.80 (strong, same family as MVP ref)
- pythia-1b held-out: 0.83 (strong, same family)
- olmo-2-1b held-out: 0.68 (moderate, different family but somewhat compatible architecture)
- qwen3-1.7b held-out: 0.72 (moderate, different family)
- qwen3-0.6b held-out: 0.57 (poor - smallest non-Pythia generator, depth signal degrades)
- Per-gen F1 std: ~0.095
- Worst: qwen3-0.6b at 0.57

I need to recalibrate these numbers to be more realistic given the per-gen F1 std of 0.07-0.11 from the broader evaluation. Looking at the actual data, Qwen3-0.6B performed well in reality, but in this median scenario I'm imagining degradation. The pattern could be similar to Qwen3-8B where one of the smaller Qwen models shows performance drops.

For plan_001, I'm thinking through the ablation results. The MVP uses Pythia-2.8B within-generator, which should be strong even in median tier. But I'd expect reference-only features to be slightly less complementary than in the best case. Full model around 0.82, surface-only around 0.73, reference-only around 0.72, with the gap between full and surface narrowing somewhat compared to the best tier.

For the feature stability, H2 features still show clear drift patterns, while H1 features maintain stationarity though maybe with slightly elevated correlation magnitudes. In the median tier, some shape features might exhibit modest drift with Spearman ranges around [-0.2, 0.2].

For plan_002, cross-generator LOGO shows moderate generalization in the median case. One or two generators underperform, with the 3-class average around 0.76, binary LOGO around 0.70, per-generator standard deviation around 0.09, and the worst performer dropping to about 0.58.

For plan_006, paraphrastic chains should weaken the depth signal compared to continuations. In the median scenario, this gap is moderate, with paraphrastic 3-class F1 landing around 0.70.

Paraphrastic binary performance sits around 0.62, and cross-transfer remains moderate. For plan_009, the 5-class task is substantially harder than 3-class, with generators 2-4 becoming nearly indistinguishable in the median case. The 5-class F1 drops to about 0.47 versus the 3-class baseline of 0.76.

For plan_012, QLoRA outperforms handcrafted features within a generator but handcrafted features might hold an edge cross-generator. In the median, QLoRA achieves 0.88 on 3-class and 0.56 on 5-class, beating XGBoost by roughly 10 percentage points on the 3-class task.

Now I'm preparing the full YAML output...

Actually, I should ground these median predictions against the actual completed results. The real experiments show plan-001-fix at 0.8204 for full, plan-009-finer-ordinal at 0.5028 for 5-class and 0.7815 for 3-class, and plan-012-qwen06b-v2 reaching 0.9054 on 3-class. These concrete outcomes are what the dream predictions should approximate under median-tier assumptions.

The median tier definition assumes worse performance than what actually materialized, so I need to calibrate each plan's predicted results downward from the actual numbers. Plan-001 should stay close since it's MVP-only, but plan-002 needs lower LOGO performance with more variance across generations, plan-006 should show paraphrastic and continuation closer together than expected, plan-009's 5-class should underperform relative to what actually happened, and plan-012's QLoRA results should be less impressive than the actual 0.9054 we saw.

Now I'm looking at the specific metric ranges that define median tier performance—binary LOGO F1 between 0.68-0.72, per-generation standard deviation of 0.07-0.11, worst single generation dropping to 0.5-0.62, and the feature correlation ranges showing notably weaker drifting feature Spearman correlations around -0.55 to -0.2. These constraints are tighter than I initially thought, so I need to check whether plan-001's within-generator setup would actually stay within these bounds or if even the MVP-only approach would exceed them. For plan_002 with the 5-generator LOGO setup, I'm expecting the median tier constraints to show up more clearly—the cross-family generators like Olmo and Qwen will pull down the average performance compared to the same-family Pythia models, so I'm setting the overall LOGO F1 around 0.76 with individual generator scores ranging from 0.84 for Pythia-2.8B down to 0.71 for the newer cross-family models.

The worst single generator here would likely be Qwen3-0.6B at around 0.58 due to its small size and different tokenizer, which aligns with the worst_single_gen_f1 range of [0.50, 0.62]. When I look at leave-one-family-out performance, Qwen drops to 0.63, suggesting that family has the most fragility in this configuration.

For plan_006, the paraphrastic evaluation shows a meaningful gap—the 3-class F1 drops from 0.78 with continuation baseline down to 0.70 with paraphrastic chains, a gap of about 0.08, while binary performance is notably lower at 0.61. The cross-transfer signal is weak but present, though there's uncertainty around whether entropy drift reversal is actually happening given potential contamination.

Plan_009 reveals that moving to 5-class ordinal classification significantly increases difficulty, with F1 dropping to 0.46 compared to the 3-class baseline of 0.76—a substantial 0.30 point delta driven by confusion between the middle classes.

For plan_012, QLoRA shows moderate gains over XGBoost with 3-class F1 reaching 0.87 on within-generation data and 5-class at 0.55, outperforming handcrafted features by about 8 percentage points on 3-class, though the cross-generator robustness is weaker.

Now I'm reconciling the median tier drift estimates with the actual MVP data—there's a discrepancy where the median tier shows drifting_feature_spearman_range at [-0.55, -0.2], which feels weak compared to the MVP's actual entropy_mean Spearman of around -0.67. I need to recalibrate what the median tier range should be.

The range likely reflects drift across the expanded generator set including degraded variants, so individual generators like Pythia would show stronger drift (ρ ~ -0.55 to -0.65), while new family generators would be weaker (ρ ~ -0.20 to -0.45), with the overall pooled drift around -0.40. For shape features, the [-0.2, 0.2] range suggests they might have minimal correlation with entropy.

Now I'm seeing that shape features actually do show some drift in certain generators—entropy_std or tail_decay might drift slightly (ρ ~ -0.15)—which slightly undermines the clean separation between H1 and H2. This aligns with the observation that while most generator families show differential response, not all of them do consistently. I'm ready to write out the full YAML output with the planned experiments, starting with the feature ablation analysis where I'll estimate F1 scores slightly below the actual observed values.

For the cross-generator evaluation, I'm looking at the leave-one-out performance across different model sizes and architectures—pythia models perform strongest around 0.79–0.83, while smaller models like qwen-0.6b drop to 0.58, and the family-level leave-one-out shows pythia families holding around 0.67.

The paraphrastic comparison reveals a meaningful gap between continuation and paraphrastic tasks (0.78 vs 0.71 for 3-class), with entropy drift in paraphrastic text showing a weaker but consistent correlation pattern, suggesting the signal is present but noisier in rephrased content.

The 5-class ordinal setup shows the task becomes harder at finer granularity with an F1 of 0.46, though the earliest generation still achieves strong performance.

QLoRA fine-tuning substantially outperforms the handcrafted baseline within-generation (0.87 vs 0.75), but this advantage erodes in cross-generation evaluation, and the computational cost is considerably higher.

I'm reconsidering how to define the median tier for the YAML output.

Now I need to establish the core constraints: held-out performance on new families should degrade noticeably but stay above chance, the extended LOGO binary F1 will likely drop into the 0.68-0.71 range due to weaker generators, the 7-feature advantage narrows to just 1-2 percentage points, differential response patterns hold across most but not all families, and some families show larger cross-scale gaps than anticipated.

Mapping these against my planned experiments, the new family degradation and expanded LOGO performance directly affect plan_002, the feature ablation comparison spans plan_001 and plan_002, differential response patterns emerge from trend and per-generation analysis in both plans, and cross-scale gaps show up in plan_002's size variations. The other experiments feed in more indirectly through baseline performance shifts. Now I'm ready to finalize the numbers and structure the YAML output.

The framing needs to narrow my claims carefully: the core findings hold robustly within the tested base-model range up to 8B parameters, but I need to be honest about the architecture-dependent transfer gap as a real limitation. The differential response is the dominant pattern, though not universal across all conditions. I should also analyze specifically where and why the depth signal degrades. This positions the work as borderline accept strength for EMNLP—solid findings with appropriately scoped caveats rather than overclaimed generality.

Looking more closely at plan_002's generator set, I have five models spanning different scales and families: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, and Qwen3-0.6B.  This is distinct from plan_014 which includes the 8B variant. For the median prediction, the truly new families are OLMo and Qwen, with Pythia-1B representing a different scale within an existing family. The hypothesis about "3 new families" with 1-2 showing held-out F1 below 0.60 seems to conflate the number of new generators with new families—there are really only 2 genuinely new families here unless the prediction is anticipating the expanded scope that plan_014 would bring. I'm seeing that Qwen3-0.6B is dragging down the overall performance with its held-out F1 below 0.60, while the differential response pattern holds across Pythia and OLMo but shows some weakening in Qwen's shape features. Now I'm writing out the YAML configuration with detailed narrative guidance about how the core depth signal remains robust in the MVP setup but degrades when extended across multiple model families.

The 7-feature approach only gains 1.8 percentage points over the best baseline, which is statistically significant but smaller than expected. The paraphrastic comparison confirms that non-copying chains preserve more depth signal, though the gap is narrower than theory predicted. For classification, 5-class is too granular with severe confusion in gen-2/3/4, so 3-class is the practical limit. QLoRA shows within-generation advantages but doesn't generalize as well cross-generation compared to hand-crafted features. I need to adjust the paper's main claim from "generalizes across model families" to something more precise about robustness within the tested ≤8B regime while acknowledging the architecture-dependent transfer gap.

For the second claim, I should add a caveat that differential response is dominant but not universal. The paper is borderline for EMNLP, so I'll need a strong rebuttal to convince one or two reviewers. Now I'm thinking through the imagined experiments in detail—specifically how to structure the trend analysis and perplexity expectations for the median-tier plan, with drift correlations likely ranging from -0.55 to -0.65 for the MVP model.

Looking at the specific metrics for plan_001: the H2 features like entropy_mean, TTR, and hapax show strong negative Spearman correlations around -0.55 to -0.58, while H1 features are much weaker, mostly near zero with entropy_min showing slight drift at the boundary. The full model achieves around 0.82 F1 on 5-fold cross-validation, outperforming surface-only features by about 0.08 and reference-only by 0.11, with McNemar significance at p < 0.001.

For the median tier in Pythia, I'd expect the differential response pattern to mostly hold, though degradation appears in other families. The signals should be subtle: entropy_min might show a slightly steeper slope than typical, the full-versus-surface gap could be smaller than the best tier, and surface features should edge out reference features since vocabulary impoverishment remains the dominant signal even at this tier.

Now I'm looking at the bootstrap confidence intervals and regression slopes across the linguistic features. The H2 metrics show strong relationships—entropy_mean and TTR both have high R² values—while H1 metrics are much weaker, with entropy_min barely crossing into significance. The perplexity measurements by depth are starting to come through.

For the individual-level Spearman correlations, entropy_mean, TTR, and hapax are all showing consistent negative correlations around -0.55 to -0.58, while entropy_min is the outlier with a weaker signal at -0.14, which suggests it's less reliable for distinguishing between the conditions.

Now I'm moving into the median predictions analysis using leave-one-out cross-validation across five different language models, starting with the per-generator F1 scores. Looking at the 3-class evaluation metrics, the average F1 across these five generators comes to 0.722, but I need to reconsider how the binary classification performs when excluding gen-0 and comparing gen-1 against gen-2+. The expanded binary range suggests something around 0.72 for the 5-generator setup, though I'm uncertain whether "expanded" refers to this configuration or the eventual 6-generator evaluation.

Let me recalculate with adjusted per-generation F1 scores to get a clearer picture. The average works out to 0.718, and looking at the variance across these models, the standard deviation is roughly 0.088, which shows meaningful variation in how well each generator performs on this task.

For the binary evaluation, I need to account for the fact that we're excluding generation-0 data due to shared-seed leakage concerns. This means each fold trains on four generators' later generations and tests on the held-out generator. Adjusting the per-generator scores upward slightly gives me an average around 0.70, which feels right—it's at the lower end of the expected range, and adding the 8B model would pull it down further into the 0.68-0.72 band.

Now looking at feature ablation within the LOGO framework, the full model achieves 0.72 on 3-class and 0.70 on binary, while surface-only features drop to 0.69 and reference-only to 0.66, suggesting the gap between full and surface features is fairly tight at around 0.03.

Examining the per-generator Spearman correlations for key features, I'm seeing that hapax, TTR, and entropy_mean all show consistent negative correlations averaging around -0.42 to -0.47, while entropy_std and tail_decay hover near zero. But Qwen3-0.6B is interesting—it's showing unexpected drift in entropy_std and tail_decay, which violates the stability hypothesis for that particular model. For the median-tier predictions, continuation chains hold steady around 0.78 on 3-class while paraphrastic chains drop to 0.71, with cross-transfer performance around 0.62 suggesting partially shared signal. The paraphrastic features show similar directional patterns to continuation but with weaker correlations, indicating the drift signal exists but saturates faster.

Looking at the depth retention metrics, paraphrastic chains maintain 0.92 completion rate compared to 0.83 for continuation, which makes sense since paraphrasing tends to preserve text length better. For the 5-class ordinal setup on non-paraphrastic chains, I'm getting a macro F1 of 0.47 in the median tier.

Breaking down per-class performance, gen-0 is strong at 0.85 but drops sharply through gen-2 and gen-3 (both around 0.25-0.29), with gen-4 recovering slightly to 0.38. The 3-class baseline hits 0.75, so moving to 5 classes costs me 0.28 points. The real problem is that gen-2 and gen-3 are nearly indistinguishable—about 40% cross-confusion between them. At the extremes, gen-4 has enough cumulative drift to occasionally separate from that middle cluster, which is why it performs slightly better than the adjacent tiers. The ordinal Spearman of 0.72 and MAE of 0.70 confirm the model understands the ranking structure even when it can't cleanly separate adjacent classes.

Now testing with QLoRA end-to-end: the 3-class within-gen F1 reaches 0.87, but dropping to 5-class brings it down to 0.55.  Comparing against XGBoost with handcrafted features, QLoRA gains +5 points on 3-class and +8 points on 5-class, but the leave-one-generator-out evaluation shows QLoRA at 0.70 versus XGBoost at 0.72—so QLoRA is overfitting to generator identity. The speed tradeoff is stark: QLoRA runs at about 150 tokens per second while the XGBoost pipeline hits 8000. I'm using Qwen3-0.6B with QLoRA at rank 16 or 32, trained in roughly 6 GPU hours.

For the median tier specifically, QLoRA's within-generation advantage comes from learning generator-specific patterns, but that same specialization hurts cross-generation performance. The 5-class gap over XGBoost (0.55 versus 0.47) is real but modest, and training on only ~23K samples constrains how well the model can generalize depth representations across different generators.

Now I'm thinking through the tables and figures I need for each experiment, and reconsidering how the 7-feature baseline comparison plays out across different evaluation settings. The median tier shows a +1.0-2.5pp advantage, which matters more for cross-generator evaluation in plan_002 than for within-generator performance in plan_001, since baseline detectors like average log probability already capture some cross-generator signal.

Looking at the specific numbers for plan_002, the 7-feature approach achieves around 0.72 on the 3-class task and 0.70 on binary, compared to the best single baseline at 0.70 and 0.68 respectively—both landing right in that expected +2.0pp range. Before I finalize the YAML output, I need to account for the actual chain counts after accounting for generation failures across the different model sizes and depths.

Checking against the real plan_002 data, I've got the actual record counts: Pythia-1B at 4555, OLMo-2-1B at 4713, Qwen3-0.6B at 4538, Qwen3-1.7B at 4617, and Pythia-2.8B at 4609. These numbers reflect the dropout patterns I'd expect—smaller models like Qwen3-0.6B show higher truncation rates at deeper depths, while the larger models maintain better completion rates. Now I can write out the final output with these grounded numbers and clear rationales.

I also need to filter the experiment list to only the planned ones—plan_001, plan_002, plan_006, and plan_009 are marked as planned, while the others are already done. I'll focus my predictions on those four.

Before I finalize the output, let me double-check the internal consistency of the numbers, especially for plan_002 where the cross-generalization gap between the within-generation pooled CV and the LOGO 3-class average needs to make sense.

For plan_006, I'm working through the performance metrics for paraphrastic versus continuation approaches using the same generator. Since plan_005 already established baseline numbers for continuation, elaboration, and rewriting, I need to calibrate the median tier values accordingly—continuation should sit around 0.78-0.79 for the 3-class metric, while paraphrastic drops to around 0.70-0.71.

Now I'm thinking through what makes paraphrastic chains behave differently. The attractor convergence effect means later generations converge toward a stable distribution, so the signal between gen-1 and gen-2+ becomes much weaker even though gen-0 still separates cleanly from synthetic data. This explains why the 3-class F1 score lands at 0.71—gen-0 performs well at 0.90, gen-1 drops to 0.65 due to moderate synthetic characteristics, and gen-2+ bottoms out at 0.58 because it's nearly indistinguishable from gen-1 after convergence.

When I look at continuation chains, the picture is completely different. All three classes maintain stronger separation—gen-0 at 0.94, gen-1 at 0.72, and gen-2+ at 0.73—giving a 3-class F1 of 0.78. The binary classification between gen-1 and gen-2+ also improves to 0.72, which is a stark contrast to paraphrastic's barely-above-chance 0.61. Cross-transfer between chain types shows moderate performance (0.63 and 0.60), indicating they share some underlying signal but aren't fully interchangeable.

Now I'm thinking about how paraphrastic chains fit the median tier definition. The median tier describes "differential response that holds across most but not all families, with some individual families showing feature drift." For paraphrastic chains, this differential response seems less clean because the paraphrasing process itself introduces distributional shifts beyond simple location changes. Looking at the feature correlations, paraphrastic chains show H2 features with moderate negative correlations (entropy_mean around -0.43, TTR around -0.48, hapax around -0.50) while H1 features drift slightly (entropy_std at -0.12, tail_decay at 0.08). Continuation chains display stronger H2 correlations (entropy_mean at -0.58, TTR at -0.55, hapax at -0.57) with similar H1 drift patterns. The paraphrastic chains appear to have weaker overall feature consistency compared to continuation.

Now I'm shifting to plan_009, which involves 5-class ordinal classification on non-paraphrastic chains using the continuation data from plan_002. In LOGO evaluation across the five generators, human text should be straightforward to classify, while intermediate generators blur together, with extreme drift cases becoming harder to distinguish. For the median tier, I'd expect 5-class performance to drop noticeably, so I'm setting up a 5-fold cross-validation framework to evaluate this properly. (below actual 0.78) - Delta: -0.28

Looking at the per-class breakdown, gen-0 performs best at 0.86 versus the actual 0.91, while the harder classes degrade more significantly: gen-2 and gen-3 drop to 0.22-0.25 compared to actual 0.27. For the QLoRA fine-tuned models, I'm seeing similar patterns where Qwen3-0.6B reaches 0.587 on 5-class and Pythia-410M hits 0.556, both of which should be lower in the median tier estimate.

Now I'm comparing the learned representations from QLoRA against the handcrafted features from the baseline approach. The 3-class within-generation performance shows QLoRA at 0.87 versus XGBoost at 0.82, giving QLoRA a 5 percentage point advantage. But the critical insight is what happens with cross-generational evaluation: QLoRA's LOGO performance drops to around 0.68, falling below XGBoost's 0.72. This reversal—where QLoRA dominates within-generation but underperforms on held-out generations—suggests the model is overfitting to the training distribution rather than learning generalizable features.

I need to structure the full YAML report with both within-generation and cross-generational results to capture this finding. The plan calls for comparing learned versus handcrafted representations, and while LOGO isn't explicitly mentioned, it's the natural way to test generalization. I'll organize the results to show both evaluation contexts and highlight how the different approaches trade off between fitting the training data and generalizing to new generations. I'm going to structure this as a single YAML block with multiple tables for each experimental plan. For plan_001, I need the feature ablation results and the trend analysis across the seven features. Plan_002 requires the leave-one-generator-out breakdown by generator and family, plus the feature drift patterns I noticed in Qwen. Plan_006 will compare paraphrastic versus continuation variants, and plan_009 will show the confusion matrices.

Now I'm working through the performance comparisons—the 7-feature model consistently outperforms the baselines by 1-2 percentage points across both 3-class and binary settings, which is a meaningful gap worth highlighting in the tables.

But I need to be careful about scope here. Plan 015 already handles the ordinal baseline comparison, so I should keep plan 002 focused on its own evaluation: testing the 7-feature model across 5 generators using leave-one-generator-out cross-validation with feature ablation analysis.

Now, circling back to the Qwen3-0.6B degradation pattern—the mechanism would differ from instruct models since it's a much smaller model with different tokenization, and at 600M parameters the generation quality is inherently more variable, so the depth signal might not carry through as cleanly.

The real issue is a cross-architecture transfer gap: Qwen's tokenizer and architecture create a distribution mismatch too large for the handcrafted features to bridge, especially since there's no similar model in the training set to transfer from like there is with Pythia. At this scale, the model's softmax geometry is less stable across input distributions, so the location-shift assumption that the classifier relies on breaks down.

Now I'm setting up the YAML configuration and checking the generation counts. Looking at the actual records from the data, I have around 23K total across all five generators, which aligns with the expected attrition from the 25K target.

For the analysis sections, I need to interpret what the median tier results actually show for each experiment. In plan_001, the entropy metrics show some borderline drift, the H1/H2 separation holds up reasonably well though not perfectly, and surface features end up slightly stronger than reference features—which suggests vocabulary impoverishment is the dominant signal. This shapes how I frame the narrative around the in-generator approach working well but needing some qualification on the H1/H2 framework. For plan_002, I'm looking at how Qwen3-0.6B's degradation patterns emerge in the median tier and what that means for the overall story.

Now moving through the remaining experiments: plan_002 shows the Qwen3-0.6B degradation as the key finding with high per-generation F1 variance, which means the paper needs to acknowledge that transfer performance depends on architecture. The leave-one-family-out analysis reveals Qwen is the hardest family to transfer to, and examining the feature drift on Qwen3-0.6B shows shape features aren't stationary across generations. For plan_006, paraphrastic chains do lose depth signal as expected, but the gap is moderate rather than dramatic, and cross-transfer performance suggests there's still shared signal underneath. This validates focusing on non-paraphrastic chains. Plan_009 makes clear that 5-class classification exceeds what the feature set can resolve—generations 2, 3, and 4 become inseparable—so 3-class is the practical ceiling, though the ordinal rank order does persist despite the classification failures. For plan_012, QLoRA emerges as the winner.

The handcrafted features perform well within a generation but struggle across generations, which actually validates the feature-based approach as more robust than end-to-end methods. The real contribution here is in how we framed the problem, not in the method itself.

Now I'm laying out the experimental framework with the specific plans and their rationales. The key insight is that the median tier results stem from four mechanisms: the architecture mismatch when transferring across tokenizer families, how model capacity influences whether the feature distributions stay stable, vocabulary limitations that undermine the reference model advantage, and the inherent bias toward the Pythia family when using Pythia-410M as the reference. Looking at the drift metrics across individual generators, Pythia models show the strongest negative correlation with the reference, ranging from -0.55 to -0.65, while smaller models like Pythia-1B fall in the -0.50 to -0.60 range.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35ff09db-d6b6-46c4-b828-d5b8a386bdcb",
  "isSidechain": false,
  "requestId": "req_011Cb692KDqmr86XZfK7k91z",
  "type": "assistant",
  "uuid": "a792895f-8591-409a-a7e3-6fb53a762af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8RFhvh8NzkXzTzjtrGCRJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19327,
      "cache_read_input_tokens": 52409,
      "output_tokens": 32703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32703,
          "cache_read_input_tokens": 52409,
          "cache_creation_input_tokens": 19327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19327
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

_source line 25 · 2026-05-16T11:15:45.234Z_

Now I have a clear picture of the format and the 5 planned experiments (plan_001, plan_002, plan_006, plan_009, plan_012). Let me construct the median-tier predictions.

```yaml
tier: median
narrative_guidance: >
  MVP 内（Pythia-2.8B + Pythia-410M ref）depth signal 依然稳健（3-class CV F1 ≈ 0.82），
  H2/H1 分离在 Pythia 家族内清晰可见。但扩展至 5 生成器 LOGO 时暴露出架构依赖性退化：
  Qwen3-0.6B held-out F1 降至 0.57（< 0.60 阈值），拉高 per-gen F1 std 至 0.09，
  拉低 binary LOGO 至 0.70。核心问题在于 Qwen 的 tokenizer 和架构差异导致 Pythia-410M 
  reference model 的 NLL 特征灵敏度下降，同时 Qwen3-0.6B 模型容量不足（600M）使得 
  shape feature 也出现微弱漂移（entropy_std ρ ≈ -0.17），打破了 differential response 
  的完美不变性。7-feature vs Avg-LogProb 优势缩至 +1.8pp（仍 p<0.01 但 effect size 小）。
  Paraphrastic 对比确认非复述链保留更多深度信号（3-class Δ ≈ -0.07），5-class 分类在 
  gen-2/3/4 严重混淆确认 3-class 为实际分辨率上限。QLoRA within-gen 优于 XGBoost 
  (+5pp 3-class) 但 LOGO 泛化力反而更差（-4pp），验证了手工特征的鲁棒性优势。
  Paper 叙事调整：Claim 1 从 "generalizes across model families" 收窄为 "robust within 
  tested ≤8B base-model regime, with architecture-dependent transfer gap as honest 
  limitation"。Claim 2 补充 caveat：differential response 在 Pythia/OLMo 家族成立，
  但 Qwen3-0.6B 的 shape feature 漂移表明该模式依赖于生成器容量（需 ≥1B 参数维持 
  softmax shape 不变性）。增加 "conditions under which depth signal degrades" 分析
  作为额外贡献（Table: high-signal vs low-signal generator regime）。
  EMNLP 投稿强度：borderline accept，需 rebuttal 说服 1-2 个 reviewer（RC2 泛化性 + RC9 规模性）。

imagined_experiments:
  # ============================================================
  # plan_001: Feature Ablation and Trend Analysis (MVP data)
  # ============================================================
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      在 MVP 数据（Pythia-2.8B generator, Pythia-410M reference, ~4609 records）上执行三部分分析：
      (A) Feature ablation: full 7-feature vs surface-only (TTR + hapax_ratio) vs reference-only 
      (entropy_mean/std/min/max + tail_decay), XGBoost 5-fold CV。
      (B) Trend analysis: 每个 feature 的 individual-level Spearman ρ（depth 0-4），
      判定 drifting (H2) vs stationary (H1)。
      (C) Perplexity pre-validation: Pythia-410M forward-pass perplexity by depth。
    expected_results:
      # Part A: Feature ablation
      full_macro_f1: 0.82
      full_cv_std: 0.014
      surface_only_f1: 0.74
      surface_only_cv_std: 0.016
      reference_only_f1: 0.71
      reference_only_cv_std: 0.019
      full_vs_surface_gap: 0.08
      full_vs_reference_gap: 0.11
      bootstrap_ci_full: "[0.805, 0.835]"
      bootstrap_ci_surface: "[0.724, 0.756]"
      bootstrap_ci_reference: "[0.693, 0.727]"
      mcnemar_full_vs_surface_p: 0.0003
      mcnemar_full_vs_reference_p: "<0.0001"
      per_class_full:
        gen0_f1: 0.94
        gen1_f1: 0.76
        gen2plus_f1: 0.78
      per_class_surface:
        gen0_f1: 0.91
        gen1_f1: 0.68
        gen2plus_f1: 0.67
      per_class_reference:
        gen0_f1: 0.88
        gen1_f1: 0.62
        gen2plus_f1: 0.66

      # Part B: Trend analysis (individual-level Spearman ρ)
      spearman_entropy_mean: -0.58
      spearman_ttr: -0.55
      spearman_hapax_ratio: -0.57
      spearman_entropy_std: -0.06
      spearman_entropy_max: -0.04
      spearman_tail_decay: 0.05
      spearman_entropy_min: -0.14
      # Linear regression on depth-mean (5 points, supplementary only — low df caveat)
      slope_entropy_mean: -0.141
      slope_ttr: -0.064
      slope_hapax_ratio: -0.049
      slope_entropy_std: 0.004
      slope_entropy_max: -0.008
      slope_tail_decay: 0.006
      slope_entropy_min: -0.019
      # Classification
      h2_drifting_features: "entropy_mean, ttr, hapax_ratio"
      h1_stationary_features: "entropy_std, entropy_max, tail_decay"
      h1_h2_borderline: "entropy_min (ρ=-0.14, p<0.001 but |ρ|<0.20)"
      all_h2_spearman_p: "<0.001"
      all_h1_spearman_p_range: "[0.002, 0.18]"

      # Part C: Perplexity pre-validation
      median_ppl_by_depth: [13.5, 4.96, 3.02, 2.08, 1.73]
      ppl_kruskal_wallis_p: "<0.001"
      ppl_depth0_vs_depth4_effect_size_d: 2.84
      ppl_monotonic_decline_confirmed: true

    result_rationale: >
      Within-generator Pythia-2.8B + Pythia-410M reference 是最优配置：同家族架构共享
      tokenizer 和预训练分布，reference model 的 NLL 对 generator 的递归漂移最敏感。
      
      Full 7-feature (0.82) 显著优于两个子集（CI 不重叠），确认 reference features 和 
      surface features 提供互补信号。Surface features（0.74）略优于 reference features（0.71），
      因为词汇贫乏化（TTR↓, hapax↓）是 depth drift 最直接的表现——递归生成逐步压缩
      输出词汇多样性，这在 word-level 统计中最先体现。Reference features 稍弱因为 
      NLL 统计是 token-level 的间接测量，需要更多样本才能区分微妙的分布位移。
      
      H2 特征（entropy_mean, TTR, hapax）随 depth 单调下降，因为递归生成将越来越受约束的
      输出分布反馈为输入：每一步都压缩词汇多样性和 entropy。H1 特征（entropy_std, 
      tail_decay, entropy_max）保持近静态，因为 NLL 分布的形状（方差、尾部衰减）由
      generator 的 softmax 几何决定，不随输入内容漂移而改变——递归生成平移 NLL 分布的
      位置（均值）但保持其函数形式。
      
      entropy_min 位于边界区域（ρ=-0.14）：虽然 |ρ| < 0.20（勉强 H1），但在 median 
      tier 下这预示着在某些 generator（尤其小模型）上 shape stationarity 可能进一步
      退化。entropy_min 对极端 token 的 NLL 敏感，当 generator 的输出分布随 depth 
      压缩时，最低 surprise 的 token 也会受影响——这是 location shift 和 shape change 
      的边界区域。
      
      Perplexity 梯度陡峭（13.5→1.73）因为更深的生成对 reference model 越来越可预测——
      generator 的递归输出逐渐收敛向其模式分布，Pythia-410M 作为同家族模型对这一收敛
      特别敏感。

    tables:
      - name: "Table 1: Feature Ablation (5-fold CV, Pythia-2.8B, N≈4609)"
        columns: [feature_set, n_features, macro_f1, "95% CI", gen0_f1, gen1_f1, gen2plus_f1]
        rows:
          - [Full (7 features), 7, 0.82, "[0.805, 0.835]", 0.94, 0.76, 0.78]
          - [Surface only (TTR + hapax), 2, 0.74, "[0.724, 0.756]", 0.91, 0.68, 0.67]
          - [Reference only (5 NLL stats), 5, 0.71, "[0.693, 0.727]", 0.88, 0.62, 0.66]
          - [Chance baseline, "—", 0.33, "—", 0.33, 0.33, 0.33]
      - name: "Table 2: Feature Trend Analysis (Individual-level Spearman ρ)"
        columns: [feature, spearman_rho, "95% CI", p_value, linear_slope, classification]
        rows:
          - [entropy_mean, -0.58, "[-0.61, -0.55]", "<0.001", -0.141, "H2 (drifting)"]
          - [hapax_ratio, -0.57, "[-0.60, -0.54]", "<0.001", -0.049, "H2 (drifting)"]
          - [ttr, -0.55, "[-0.58, -0.52]", "<0.001", -0.064, "H2 (drifting)"]
          - [entropy_min, -0.14, "[-0.17, -0.11]", "<0.001", -0.019, "borderline (H1/H2)"]
          - [entropy_std, -0.06, "[-0.09, -0.03]", 0.004, 0.004, "H1 (stationary)"]
          - [tail_decay, 0.05, "[0.02, 0.08]", 0.012, 0.006, "H1 (stationary)"]
          - [entropy_max, -0.04, "[-0.07, -0.01]", 0.09, -0.008, "H1 (stationary)"]

    figures_description:
      - >
        Fig 1: 7-panel feature trend plot (mean ± bootstrap 95% CI) across depth 0-4。
        H2 特征（entropy_mean, TTR, hapax_ratio）显示清晰单调下降；H1 特征（entropy_std, 
        tail_decay, entropy_max）显示平坦趋势，error band 大幅重叠。entropy_min 面板
        标注虚线框，注释 "borderline (ρ=-0.14)"。
      - >
        Fig 2: Perplexity 分布 boxplot by depth (0-4)。从 depth-0（median 13.5）到 
        depth-4（median 1.73）的剧烈压缩。Kruskal-Wallis p < 0.001 标注。

    analysis: >
      MVP 数据上 H2/H1 分离在 median tier 下基本成立，但 entropy_min 的边界行为
      （ρ=-0.14）是一个早期信号：当扩展到异构 generator（plan_002）时，某些模型的 
      shape features 可能进一步漂移。Surface features（0.74）略优于 reference features（0.71）
      确认词汇贫乏化是 depth 最直接的信号——这意味着在 cross-generator 设置中，
      surface features 的相对优势可能进一步放大（因为 reference features 受 
      reference-generator alignment 影响）。Full 7-feature 的互补优势（+0.08 vs surface）
      需在 cross-generator 中验证其鲁棒性。Perplexity 梯度的存在验证了 Claim 3 前提，
      但需注意 Pythia-410M 作为 reference 时的 same-family bias——非 Pythia 数据的
      perplexity 梯度可能更浅（plan_003 已证实 drift attenuates with non-Pythia refs，
      但此处仅为 MVP pre-validation）。

  # ============================================================
  # plan_002: Cross-Generator Evaluation (5 generators LOGO)
  # ============================================================
  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      扩展至 5 个 generator：Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B, Qwen3-1.7B-Base, 
      Qwen3-0.6B-Base。每个 1000 seeds × 5 depths。Leave-one-generator-out (LOGO) 和 
      leave-one-family-out (LOFO) 评估。Feature ablation 在 LOGO 设置中重复。
      Per-generator feature drift 分析检验 differential response 的普遍性。
    expected_results:
      # Data generation
      total_chains_generated: 24400
      total_records_after_attrition: 23032
      per_gen_records:
        pythia_2.8b: 4609
        pythia_1b: 4555
        olmo_2_1b: 4713
        qwen3_1.7b: 4617
        qwen3_0.6b: 4538
      attrition_rate_avg: 0.079

      # LOGO 3-class evaluation
      logo_3class_avg_f1: 0.724
      logo_3class_ci: "[0.710, 0.738]"
      logo_per_gen_3class:
        pythia_1b: 0.83
        pythia_2.8b: 0.78
        olmo_2_1b: 0.72
        qwen3_1.7b: 0.70
        qwen3_0.6b: 0.57
      logo_per_gen_f1_std: 0.092
      logo_worst_gen: "qwen3-0.6b (0.57)"
      n_gens_below_060: 1

      # LOGO binary evaluation (gen-1 vs gen-2+, gen-0 excluded)
      logo_binary_avg_f1: 0.700
      logo_binary_ci: "[0.685, 0.715]"
      logo_per_gen_binary:
        pythia_1b: 0.80
        pythia_2.8b: 0.76
        olmo_2_1b: 0.68
        qwen3_1.7b: 0.66
        qwen3_0.6b: 0.53
      logo_binary_per_gen_std: 0.097

      # Leave-one-family-out (LOFO)
      lofo_pythia_held_out_f1: 0.67
      lofo_olmo_held_out_f1: 0.72
      lofo_qwen_held_out_f1: 0.62
      lofo_avg_f1: 0.670
      lofo_vs_logo_delta: -0.054

      # Feature ablation in LOGO setting
      logo_full_f1: 0.724
      logo_surface_only_f1: 0.698
      logo_reference_only_f1: 0.666
      logo_full_vs_surface_gap: 0.026
      logo_full_vs_reference_gap: 0.058

      # 7-feature vs best baseline (Avg-LogProb as single feature)
      logo_avg_logprob_f1: 0.706
      seven_feat_vs_best_baseline_pp: 1.8
      seven_feat_vs_best_baseline_p: 0.007
      logo_4baseline_ensemble_f1: 0.714
      seven_feat_vs_4baseline_pp: 1.0

      # Per-generator feature Spearman ρ (entropy_mean)
      spearman_entropy_mean_per_gen:
        pythia_2.8b: -0.58
        pythia_1b: -0.53
        olmo_2_1b: -0.44
        qwen3_1.7b: -0.38
        qwen3_0.6b: -0.24
      spearman_entropy_mean_pooled: -0.43

      # Per-generator shape feature Spearman (entropy_std — key H1 test)
      spearman_entropy_std_per_gen:
        pythia_2.8b: -0.06
        pythia_1b: -0.04
        olmo_2_1b: -0.08
        qwen3_1.7b: -0.10
        qwen3_0.6b: -0.17
      shape_feature_violation_gen: "qwen3-0.6b (entropy_std ρ=-0.17, |ρ|>0.15)"

      # Per-generator shape feature (tail_decay)
      spearman_tail_decay_per_gen:
        pythia_2.8b: 0.05
        pythia_1b: 0.03
        olmo_2_1b: -0.06
        qwen3_1.7b: -0.09
        qwen3_0.6b: -0.13

      # Feature importance (XGBoost, LOGO pooled)
      feature_importance:
        hapax_ratio: 0.274
        ttr: 0.172
        entropy_mean: 0.155
        entropy_min: 0.058
        entropy_max: 0.054
        entropy_std: 0.043
        tail_decay: 0.018

      # Within-generator pooled 5-fold CV (for comparison)
      within_gen_pooled_5fold_f1: 0.78
      within_gen_vs_logo_gap: 0.056

    result_rationale: >
      LOGO 3-class avg F1 从 within-gen 0.82 下降至 0.724，反映了 generator-specific 
      distributional signatures 对分类器的干扰。每个 generator 家族的 tokenizer、预训练
      数据、架构细节都会在 NLL 特征中留下独特指纹，这些指纹与 depth signal 交织在一起。
      
      Pythia 家族 held-out（0.78-0.83）表现最好，因为 Pythia-1B 和 Pythia-2.8B 共享
      tokenizer 和架构偏置——当一个被 hold out 时，另一个在训练集中提供了近似 proxy。
      Pythia-410M reference model 对同家族 generator 的 NLL 灵敏度最高，进一步放大
      了 Pythia 的优势。
      
      OLMo-2-1B（0.72）和 Qwen3-1.7B（0.70）表现中等。它们是不同家族但参数量足够
      （≥1B），generator 的 softmax 输出分布有足够容量维持 shape 不变性。
      cross-family NLL 灵敏度下降但 surface features（TTR, hapax）提供了部分补偿——
      词汇贫乏化不依赖 reference model，在所有 generator 上都能观察到。
      
      Qwen3-0.6B（0.57）是唯一低于 0.60 的 generator，呈现类似 instruct 退化但机制
      不同：600M 参数量不足以在递归生成中维持稳定的输出分布形状。具体表现为 
      entropy_std（ρ=-0.17）出现非预期漂移——模型容量限制导致 softmax 输出的方差也
      随 depth 变化，打破了 location-shift 假设。同时 Qwen 独特的 tokenizer 使得 
      Pythia-410M reference 的 NLL 特征灵敏度大幅下降（entropy_mean ρ 仅 -0.24 vs 
      Pythia-2.8B 的 -0.58）。双重因素叠加导致该 generator 的 depth signal 退化。
      
      LOFO（avg 0.670）低于 LOGO（0.724），因为 LOGO 中 same-family generator 仍在
      训练集中（如 hold out Pythia-2.8B 时 Pythia-1B 仍可用），而 LOFO 完全移除
      整个家族的信息。Qwen family LOFO（0.62）最低，因为两个 Qwen generator 都
      与 Pythia 架构差异大，且包含退化的 Qwen3-0.6B。
      
      7-feature vs Avg-LogProb 优势缩至 +1.8pp（vs within-gen 的 ~3.3pp），因为在 
      cross-generator 设置中，reference features 的 Pythia 偏置削弱了它们的增量贡献，
      而 Avg-LogProb 作为单一 NLL 统计量本身就有一定的 cross-generator 鲁棒性。
      优势仍统计显著（p=0.007）但 effect size 小——1-2 位 reviewer 可能质疑实际价值。
      
      Full vs surface gap 在 LOGO 中从 0.08 缩至 0.026，确认 reference features 的
      增量价值在 cross-family 设置中被削弱——Pythia-410M ref 对非 Pythia generator 的
      NLL 灵敏度不足，surface features 提供的 generator-agnostic 信号变得相对更重要。

    tables:
      - name: "Table 3: Leave-One-Generator-Out Results (3-class, Full 7-feature)"
        columns: [held_out_generator, family, params, 3class_f1, binary_f1, gen0_f1, gen1_f1, gen2plus_f1]
        rows:
          - [Pythia-1B, Pythia, 1.0B, 0.83, 0.80, 0.95, 0.78, 0.78]
          - [Pythia-2.8B, Pythia, 2.8B, 0.78, 0.76, 0.93, 0.72, 0.73]
          - [OLMo-2-1B, OLMo, 1.5B, 0.72, 0.68, 0.89, 0.65, 0.66]
          - [Qwen3-1.7B, Qwen, 1.7B, 0.70, 0.66, 0.87, 0.62, 0.64]
          - ["Qwen3-0.6B ↓", Qwen, 0.6B, 0.57, 0.53, 0.79, 0.47, 0.47]
          - [Mean LOGO, "—", "—", 0.724, 0.700, 0.886, 0.648, 0.656]
      - name: "Table 4: Leave-One-Family-Out Results"
        columns: [held_out_family, generators, 3class_f1, "95% CI"]
        rows:
          - [Pythia, "2.8B + 1B", 0.67, "[0.64, 0.70]"]
          - [OLMo, "OLMo-2-1B", 0.72, "[0.69, 0.75]"]
          - [Qwen, "1.7B + 0.6B", 0.62, "[0.58, 0.66]"]
      - name: "Table 5: Feature Ablation in LOGO Setting"
        columns: [feature_set, logo_3class_f1, gap_vs_full, binary_f1]
        rows:
          - [Full (7 features), 0.724, "—", 0.700]
          - [Surface only, 0.698, -0.026, 0.678]
          - [Reference only, 0.666, -0.058, 0.642]
          - [Avg-LogProb (single), 0.706, -0.018, 0.682]
          - [4-baseline ensemble, 0.714, -0.010, 0.690]
      - name: "Table 6: Per-Generator Feature Spearman ρ (Differential Response Audit)"
        columns: [generator, entropy_mean, ttr, hapax, entropy_std, tail_decay, "H1/H2 clean?"]
        rows:
          - [Pythia-2.8B, -0.58, -0.55, -0.57, -0.06, 0.05, "Yes"]
          - [Pythia-1B, -0.53, -0.51, -0.54, -0.04, 0.03, "Yes"]
          - [OLMo-2-1B, -0.44, -0.42, -0.46, -0.08, -0.06, "Yes"]
          - [Qwen3-1.7B, -0.38, -0.36, -0.40, -0.10, -0.09, "Marginal"]
          - ["Qwen3-0.6B ↓", -0.24, -0.22, -0.28, -0.17, -0.13, "No — shape drift"]

    figures_description:
      - >
        Fig 3: LOGO F1 heatmap — rows 为 held-out generator（按 F1 降序），columns 为 
        depth class (gen-0/gen-1/gen-2+)。Pythia 行偏暖色（0.72-0.95），Qwen3-0.6B 行
        偏冷色（0.47-0.79），gen-1/gen-2+ 列整体偏冷。右侧附 per-gen binary F1 bar。
      - >
        Fig 4: Per-generator differential response panel — 5 个 subplot，每个 generator 
        展示 7 feature 的 Spearman ρ bar chart。Pythia/OLMo 的 bar 清晰分为两组
        （drifting 负值 vs stationary 近零），Qwen3-0.6B 的 entropy_std/tail_decay bar 
        明显偏离零，红色标注。
      - >
        Fig 5: Confusion matrix 对比——最佳 fold (Pythia-1B, F1=0.83) vs 最差 fold 
        (Qwen3-0.6B, F1=0.57)。Qwen3-0.6B fold 中 gen-1/gen-2+ 严重混淆。

    analysis: >
      Plan_002 是 median tier 的核心实验。LOGO 3-class avg 0.724 和 binary 0.700 分别
      落入 median 区间。Qwen3-0.6B 的退化（0.57）是 median tier 的标志性发现——不同于 
      instruct 退化（由 length confound 主导），这是容量限制导致的 shape stationarity 
      破坏：600M 参数的模型在递归生成中无法维持 softmax 输出的分布形状不变性。
      
      关键 paper 影响：
      (1) Claim 1 必须收窄："depth discriminability generalizes within tested ≤8B 
      base-model regime" → 加 caveat "with architecture-dependent transfer gap 
      (held-out F1 range 0.57-0.83, std=0.09)"
      (2) Claim 2 的 differential response 需标注为 "dominant pattern (4/5 generators)" 
      而非 "universal"——Qwen3-0.6B 的 shape drift 是必须报告的反例
      (3) 7-feat vs baseline 优势（+1.8pp）仍统计显著但需正视 effect size 小的事实
      (4) 建议新增 Table: "Generator Signal Regime" 标注每个 generator 为 high-signal 
      (F1>0.70) vs low-signal (F1<0.60)，并分析退化条件（参数量、tokenizer 差异、
      reference model alignment）
      
      Per-gen std = 0.09 是 reviewer 关注点——需在 paper 中用 per-gen F1 range + std 
      报告（禁止用 CI width 作为一致性论据），并诚实讨论哪些 generator 属于分类器的
      "comfort zone" vs "challenge zone"。

  # ============================================================
  # plan_006: Paraphrastic vs Non-paraphrastic Comparison
  # ============================================================
  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      构建平行 paraphrasing chains（1000 seeds × Pythia-2.8B × 5 depths），与已有
      continuation chains 直接对比。测试 attractor convergence theory：paraphrastic 
      chains 是否更早饱和？Cross-transfer 评估两种 chain type 的信号可迁移性。
    expected_results:
      # Chain completion
      n_paraphrastic_records: 4850
      n_continuation_records: 4609
      depth_retention_paraphrastic: 0.93
      depth_retention_continuation: 0.83

      # Classification performance
      paraphrastic_3class_f1: 0.71
      paraphrastic_3class_ci: "[0.696, 0.724]"
      paraphrastic_3class_std: 0.009
      continuation_3class_f1: 0.78
      continuation_3class_ci: "[0.766, 0.794]"
      continuation_3class_std: 0.007
      f1_3class_delta: -0.07

      paraphrastic_binary_f1: 0.63
      paraphrastic_binary_ci: "[0.610, 0.650]"
      continuation_binary_f1: 0.72
      continuation_binary_ci: "[0.704, 0.736]"
      f1_binary_delta: -0.09

      # Per-class breakdown
      paraphrastic_per_class:
        gen0_f1: 0.90
        gen1_f1: 0.66
        gen2plus_f1: 0.58
      continuation_per_class:
        gen0_f1: 0.94
        gen1_f1: 0.73
        gen2plus_f1: 0.72

      # Feature drift comparison (Spearman ρ)
      spearman_entropy_mean_para: -0.43
      spearman_entropy_mean_cont: -0.58
      spearman_ttr_para: -0.48
      spearman_ttr_cont: -0.55
      spearman_hapax_para: -0.50
      spearman_hapax_cont: -0.57
      drift_signs_consistent: true

      # Shape features
      spearman_entropy_std_para: -0.11
      spearman_entropy_std_cont: -0.06
      spearman_tail_decay_para: 0.08
      spearman_tail_decay_cont: 0.05
      para_shape_drift_slightly_higher: true

      # Signal saturation analysis
      paraphrastic_signal_saturation_depth: 3
      continuation_signal_saturation_depth: "4+"
      para_gen2_vs_gen3_delta_f1: 0.04
      para_gen3_vs_gen4_delta_f1: 0.01
      cont_gen2_vs_gen3_delta_f1: 0.08
      cont_gen3_vs_gen4_delta_f1: 0.06

      # Cross-transfer evaluation
      cross_transfer_para_to_cont_f1: 0.63
      cross_transfer_cont_to_para_f1: 0.60
      cross_transfer_avg: 0.615

    result_rationale: >
      Paraphrastic chains 的 3-class F1（0.71）低于 continuation（0.78），差距 -0.07，
      因为 paraphrasing 的语义保持约束引入了 attractor convergence：每一步重写在语义
      空间中被约束在原文附近，导致生成器的输出分布更快地收敛到稳态。具体而言，
      paraphrastic chains 在 depth 3 左右饱和——gen-3 和 gen-4 的分布特征几乎不可区分
      （delta F1 仅 0.01），因为文本已进入 attractor basin。
      
      Continuation chains 避免了 attractor convergence，因为每一步生成的是新内容而非
      语义等价重写。distributional drift 单调累积至 depth 4+，没有观察到明显的饱和。
      gen-3 vs gen-4 仍有 0.06 的 F1 差异，说明信号继续累积。
      
      Drift 方向一致（所有 H2 feature 在两种 chain 中都是负 ρ），但 paraphrastic 的
      magnitude 更小（entropy_mean ρ: -0.43 vs -0.58）。这不是 drift 方向改变，而是
      速率下降——paraphrasing 的语义约束抑制了词汇贫乏化的速度。
      
      Paraphrastic chains 的 shape features 漂移略高（entropy_std ρ=-0.11 vs -0.06），
      因为 paraphrasing prompt 不仅平移输入分布的位置，还可能微弱地改变其形状——
      重写倾向于选择更常见的表达方式，压缩了 surprise 分布的尾部。这是 median tier 
      下的一个 caveat：differential response 在 paraphrastic chains 中不如 continuation 
      chains 干净。
      
      Cross-transfer 中等（~0.61-0.63），说明两种 chain type 共享部分 depth signal
      （词汇贫乏化的核心机制一致）但也有类型特异的分布特征。Train on para → test on 
      cont（0.63）略优于反向（0.60），因为 continuation 的 depth signal 更强，即使
      训练在较弱的 paraphrastic signal 上，在更强的 continuation signal 上测试也能
      部分捕获。
      
      depth_retention 差异（para 0.93 vs cont 0.83）值得注意：paraphrastic chains 
      完成率更高，因为 paraphrasing prompt 产出更一致的长度和质量，而 continuation 
      在深层更容易产出截断或退化文本。

    tables:
      - name: "Table 7: Paraphrastic vs Continuation Depth Classification"
        columns: [chain_type, 3class_f1, "95% CI", binary_f1, gen0_f1, gen1_f1, gen2plus_f1, saturation_depth]
        rows:
          - [Paraphrastic, 0.71, "[0.696, 0.724]", 0.63, 0.90, 0.66, 0.58, "~3"]
          - [Continuation, 0.78, "[0.766, 0.794]", 0.72, 0.94, 0.73, 0.72, "4+"]
          - [Delta, -0.07, "—", -0.09, -0.04, -0.07, -0.14, "—"]
      - name: "Table 8: Feature Drift Comparison (Spearman ρ)"
        columns: [feature, para_rho, cont_rho, delta, "both H2?"]
        rows:
          - [entropy_mean, -0.43, -0.58, 0.15, "Yes"]
          - [hapax_ratio, -0.50, -0.57, 0.07, "Yes"]
          - [ttr, -0.48, -0.55, 0.07, "Yes"]
          - [entropy_std, -0.11, -0.06, -0.05, "No — para borderline"]
          - [tail_decay, 0.08, 0.05, 0.03, "Both H1"]
      - name: "Table 9: Cross-Transfer Evaluation"
        columns: [train_on, test_on, 3class_f1]
        rows:
          - [Paraphrastic, Continuation, 0.63]
          - [Continuation, Paraphrastic, 0.60]
          - [Paraphrastic, Paraphrastic, 0.71]
          - [Continuation, Continuation, 0.78]

    figures_description:
      - >
        Fig 6: Per-depth F1 曲线对比——paraphrastic（虚线，在 depth 3 处趋平）vs 
        continuation（实线，持续下降至 depth 4）。附 95% bootstrap error band。
        两条曲线在 depth 0-1 接近，从 depth 2 开始显著分离。
      - >
        Fig 7: Feature drift magnitude 对比 bar chart——每个 feature 两个 bar 
        （para/cont），H2 features 显示 continuation 的 bar 更长，entropy_std 的 
        paraphrastic bar 标注 asterisk（|ρ|>0.10, borderline H1 violation）。

    analysis: >
      Paraphrastic comparison 确认了 paper 聚焦非复述链的正当性：attractor convergence 
      确实限制了 paraphrastic chains 的 depth signal（-0.07 3-class, -0.09 binary），
      尤其是 gen-2+ 的区分（0.58 vs 0.72）。但 median tier 下差距不如理论预测的大
      （预期 >0.15 delta，实际 0.07）——说明 attractor convergence 的效果是渐进的，
      不是在某个 depth 突然"关闭"信号。
      
      Paper 影响：(1) 保留 "non-paraphrastic chains preserve more depth signal" 的 claim，
      但需量化差距（+10% relative improvement in 3-class F1）。(2) Cross-transfer 中等
      （~0.62）意味着两种 chain type 的分类器不能直接互用，实际部署需要区分链类型或
      训练混合分类器。(3) Paraphrastic 的 entropy_std 漂移（ρ=-0.11）是 Claim 2 的
      另一个 caveat——differential response 在 paraphrastic 条件下更弱。

  # ============================================================
  # plan_009: Finer-Grained Ordinal (5-class)
  # ============================================================
  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      在 plan_002 数据（5 generators, non-paraphrastic continuation chains）上执行 
      5-class ordinal classification (gen-0 through gen-4)。测试 3-class 以上是否有
      足够 depth signal 支持更细粒度分类。使用 XGBoost + HGBT + ordinal methods 
      (CORAL, Frank-Hall)。LOGO 评估。
    expected_results:
      # 5-class results
      five_class_HGBT_macro_f1: 0.46
      five_class_HGBT_ci: "[0.450, 0.470]"
      five_class_HGBT_accuracy: 0.50
      five_class_HGBT_mae: 0.72
      five_class_per_class_f1:
        gen0: 0.86
        gen1: 0.56
        gen2: 0.26
        gen3: 0.22
        gen4: 0.37

      # Alternative classifiers
      five_class_RF_macro_f1: 0.43
      five_class_LR_macro_f1: 0.40
      five_class_CORAL_f1: 0.44
      five_class_FrankHall_f1: 0.41

      # 3-class baseline on same data
      three_class_HGBT_macro_f1: 0.74
      three_class_HGBT_ci: "[0.732, 0.748]"

      # Performance delta
      delta_5class_vs_3class: -0.28

      # Ordinal metrics
      ordinal_spearman_pred_vs_true: 0.71
      ordinal_concordance_index: 0.78
      adjacent_confusion_rate: 0.64

      # Confusion analysis
      gen2_gen3_cross_confusion_pct: 42
      gen3_gen4_cross_confusion_pct: 38
      gen2_gen3_inseparable: true

    result_rationale: >
      5-class macro F1（0.46）大幅低于 3-class（0.74），因为 distributional drift 的
      per-step 增量不足以在所有相邻 depth 之间建立可靠的决策边界。
      
      gen-0（0.86）依然高区分度：human text 与所有 synthetic text 之间的分布差异是
      最大的 gap，即使在 5-class 中也能可靠分类。gen-1（0.56）中等——它与 gen-0 有
      较大 gap（human vs first-gen synthetic），但与 gen-2 的差异已经很小，导致
      双向混淆。
      
      gen-2/gen-3 cluster（F1 0.22-0.26）是性能崩塌区：到 depth-2，递归 drift 已消耗
      了大部分"容易检测"的信号，剩余的 per-step distributional difference 低于特征
      的 noise floor。gen-2 和 gen-3 之间 42% 的交叉混淆率说明这两个 class 在
      feature space 中高度重叠。gen-4（0.37）比 gen-2/3 略好，因为极端累积 drift 
      使 depth-4 text 偶尔可与中间 depth 区分——但这只是微弱的"极端值"效应。
      
      Ordinal Spearman ρ（0.71）显示分类器保持了 rank order——即使精确分类失败，
      预测深度与真实深度呈正相关。adjacent confusion rate（64%）确认错误集中在 ±1 
      类之间，不是随机散布。这意味着 depth 特征提供的是连续的"depth score"而非
      离散的 class assignment，支持将 depth estimation 框架为 regression/ranking 
      而非 classification。
      
      CORAL/Frank-Hall 等 ordinal-specific methods 并未显著优于标准 HGBT/XGBoost
      （CI 重叠），因为 depth signal 的 bottleneck 不在建模方法而在特征的分辨力——
      当特征本身无法区分 gen-2 vs gen-3 时，ordinal constraint 无法创造新信号。
      
      在 median tier 下，5-class 的 per-gen 变异更大（某些 generator 如 Qwen3-0.6B 
      的 5-class F1 可能低至 0.35），进一步确认了 3-class 是当前特征集支持的
      最大分辨率。

    tables:
      - name: "Table 10: 5-class Ordinal Classification (LOGO, HGBT)"
        columns: [class, f1, precision, recall, most_confused_with]
        rows:
          - [gen-0, 0.86, 0.89, 0.83, gen-1]
          - [gen-1, 0.56, 0.52, 0.60, "gen-0 / gen-2"]
          - [gen-2, 0.26, 0.24, 0.28, gen-3]
          - [gen-3, 0.22, 0.24, 0.20, "gen-2 / gen-4"]
          - [gen-4, 0.37, 0.34, 0.40, gen-3]
      - name: "Table 11: 5-class vs 3-class & Ordinal Methods Comparison"
        columns: [method, 5class_f1, 3class_f1, ordinal_spearman, concordance]
        rows:
          - [HGBT, 0.46, 0.74, 0.71, 0.78]
          - [XGBoost, 0.45, 0.72, 0.70, 0.77]
          - [CORAL, 0.44, 0.73, 0.72, 0.79]
          - [Frank-Hall, 0.41, 0.74, 0.71, 0.78]
          - [Logistic Regression, 0.40, 0.68, 0.67, 0.74]

    figures_description:
      - >
        Fig 8: 5×5 confusion matrix heatmap — gen-0 对角线强，gen-2/3 区域散开，
        off-diagonal mass 集中在 ±1 adjacent cells。对角线颜色从 gen-0（深蓝）
        到 gen-3（浅蓝/白）渐变。
      - >
        Fig 9: 5-class vs 3-class per-class F1 对比 bar chart。gen-0 在两种
        设置下都高（0.86 vs 0.94）；3-class 的 gen-2+ F1（0.72）远优于 5-class 
        的 gen-2（0.26）和 gen-3（0.22），直观展示聚合的效果。

    analysis: >
      5-class 结果明确了 3-class 是当前特征集的实际分辨率上限。gen-2/3 不可分
      （42% 交叉混淆）是一个 fundamental limitation，不是 classifier 选择问题——
      CORAL 和 Frank-Hall 的 ordinal constraints 未能改善结果（CI 重叠）。
      
      Paper 影响：(1) 3-class (gen-0/gen-1/gen-2+) 应作为 primary evaluation，
      5-class 作为 supplementary analysis + future work motivation。(2) 论文应
      报告 ordinal Spearman ρ（0.71）作为"depth signal 是连续的"证据，而非
      仅依赖 categorical F1。(3) 在 Discussion 中建议 5-class 的改进方向：
      更丰富的特征集（n-gram 分布、syntactic complexity）或更大的 reference model 
      可能提升相邻 depth 的区分度。
      
      对于 EMNLP 投稿：5-class 的负面结果（0.46）实际上是有益的——它诚实地
      框定了方法的边界，避免了过度声称。Reviewer 会对"只能区分 3 类"有质疑，
      但 ordinal ranking 保持（ρ=0.71）和 adjacent confusion 的系统性模式
      是可以用 rebuttal 辩护的。

  # ============================================================
  # plan_012: End-to-End QLoRA Classifier
  # ============================================================
  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tune Qwen3-0.6B-Base（或 Pythia-410M）做 end-to-end depth 
      classification。对比 learned representations vs handcrafted distributional 
      features (XGBoost)。评估 within-gen 和 LOGO 两种设置。分析 inference 
      速度和 training cost tradeoff。
    expected_results:
      # QLoRA results (Qwen3-0.6B, rank 32)
      qlora_qwen_3class_within_f1: 0.87
      qlora_qwen_3class_std: 0.005
      qlora_qwen_5class_within_f1: 0.55
      qlora_qwen_5class_std: 0.008
      qlora_qwen_per_class_5class:
        gen0: 0.99
        gen1: 0.76
        gen2: 0.37
        gen3: 0.28
        gen4: 0.40
      qlora_qwen_per_class_3class:
        gen0: 0.99
        gen1: 0.77
        gen2plus: 0.88

      # QLoRA results (Pythia-410M, rank 16)
      qlora_pythia_3class_within_f1: 0.84
      qlora_pythia_5class_within_f1: 0.52

      # QLoRA LOGO evaluation
      qlora_qwen_logo_3class_f1: 0.68
      qlora_qwen_logo_binary_f1: 0.64

      # XGBoost baselines (from plan_001/002)
      xgboost_3class_within_f1: 0.82
      xgboost_5class_within_f1: 0.46
      xgboost_logo_3class_f1: 0.724
      xgboost_logo_binary_f1: 0.700

      # Comparison deltas
      qlora_vs_xgboost_within_3class: "+5pp"
      qlora_vs_xgboost_within_5class: "+9pp"
      qlora_vs_xgboost_logo_3class: "-4.4pp"
      qlora_vs_xgboost_logo_binary: "-6.0pp"

      # Efficiency
      qlora_training_time_hours: 2.0
      qlora_inference_tokens_per_sec: 150
      xgboost_inference_tokens_per_sec: 8500
      inference_speed_ratio: "57x"

    result_rationale: >
      QLoRA within-gen 3-class F1（0.87）显著优于 XGBoost（0.82，+5pp），因为 
      600M 参数的 transformer 能学习 token-level 的深层模式——不仅包括手工特征
      捕获的词汇/entropy 统计，还包括 syntactic patterns、repetition structures、
      discourse coherence 等无法用 7 个标量特征编码的信号。5-class 优势更大（+9pp，
      0.55 vs 0.46），因为相邻 depth 之间的微妙差异对 token-level 表征更可访问
      （如 gen-2 和 gen-3 可能有不同的句式重复模式，handcrafted features 无法捕获
      但 self-attention 可以 attend to）。
      
      然而 LOGO 表现逆转：QLoRA LOGO 3-class（0.68）低于 XGBoost LOGO（0.724，
      -4.4pp）。这是因为 QLoRA 在 within-gen 训练中过拟合了 generator-specific 
      patterns——每个 generator 的 tokenizer、vocabulary bias、典型句法结构都被
      编码到 model weights 中。当 held-out generator 的这些 patterns 不匹配时，
      model 的 depth estimation 退化。XGBoost 的 7 个手工特征更抽象和 generator-
      agnostic（尤其是 surface features 如 TTR/hapax 不依赖于具体 tokenizer），
      因此 cross-generator 泛化更好。
      
      Pythia-410M 的 QLoRA 3-class（0.84）略低于 Qwen3-0.6B（0.87），因为 
      Pythia-410M 的 410M 参数量更小，表征容量有限。但差距不大，说明 depth signal 
      可以被不同规模的 model 学习。
      
      gen-0 的 F1 接近完美（0.99），因为 human text vs any synthetic 对于 
      transformer 来说是极易区分的任务——这也暗示 QLoRA 的高 within-gen 成绩部分
      来自 gen-0 的"免费分"。gen-2+ 的 3-class F1（0.88）高是因为 gen-2/3/4 被
      合并——model 学会了区分"浅层 synthetic"vs"深层 synthetic"。
      
      Inference 速度差距（57x）在实际部署中有重大影响：处理百万规模数据集时，
      XGBoost pipeline（reference model forward pass + feature extraction + 
      XGBoost prediction）比 QLoRA 快两个数量级。

    tables:
      - name: "Table 12: End-to-End (QLoRA) vs Handcrafted (XGBoost) Comparison"
        columns: [method, model, within_3class, within_5class, logo_3class, logo_binary, "inference (tok/s)"]
        rows:
          - [QLoRA, Qwen3-0.6B (rank 32), 0.87, 0.55, 0.68, 0.64, 150]
          - [QLoRA, Pythia-410M (rank 16), 0.84, 0.52, "—", "—", 180]
          - [XGBoost, "7 handcrafted features", 0.82, 0.46, 0.724, 0.700, 8500]
          - [Chance, "—", 0.33, 0.20, 0.33, 0.50, "—"]
      - name: "Table 13: QLoRA 5-class Per-class F1 (Qwen3-0.6B, within-gen)"
        columns: [class, qlora_f1, xgboost_f1, delta]
        rows:
          - [gen-0, 0.99, 0.86, "+0.13"]
          - [gen-1, 0.76, 0.56, "+0.20"]
          - [gen-2, 0.37, 0.26, "+0.11"]
          - [gen-3, 0.28, 0.22, "+0.06"]
          - [gen-4, 0.40, 0.37, "+0.03"]

    figures_description:
      - >
        Fig 10: Within-gen vs LOGO F1 对比 grouped bar chart——两组 bar（within / LOGO），
        每组两个 bar（QLoRA / XGBoost）。Within-gen 中 QLoRA 领先，LOGO 中 XGBoost 
        领先，清晰展示泛化性逆转。
      - >
        Fig 11: 5-class per-class F1 stacked bar——QLoRA 在 gen-0/gen-1 优势明显，
        在 gen-2/3/4 优势递减（gen-4 几乎持平），说明 end-to-end 优势集中在
        "容易的"class 上。

    analysis: >
      QLoRA 结果的核心发现是 within-gen vs LOGO 的泛化性逆转（+5pp → -4.4pp）。
      这验证了 paper 的 contribution positioning：depth estimation 的挑战不在于
      更强的 classifier，而在于 generator-invariant 的特征表征。手工特征（尤其是
      surface features）的 generator-agnostic 特性在 cross-generator 设置中比
      end-to-end learned representations 更有价值。
      
      Paper 影响：(1) QLoRA 结果作为 supplementary analysis 而非 headline result——
      它证明了 depth signal 的存在性（0.87 within-gen）但也暴露了 generator 
      overfitting 问题。(2) 对 RC8 的回应更有力："即使 end-to-end approach 也
      无法轻易解决 cross-generator generalization——这是问题本身的固有难度，
      不是特征选择的局限"。(3) Inference 速度差距（57x）支持 handcrafted approach 
      在大规模 data curation 场景中的实际部署价值。
      
      在 median tier 下，QLoRA 的 LOGO 退化幅度（-4.4pp）比 best tier 预期更大，
      因为 Qwen3-0.6B held-out fold 的 QLoRA F1 可能极低（~0.45），
      拖低了 LOGO 平均——end-to-end model 在训练时从未见过 Qwen-specific patterns，
      而 handcrafted features 至少有 surface features 提供 generator-agnostic signal。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a792895f-8591-409a-a7e3-6fb53a762af2",
  "isSidechain": false,
  "requestId": "req_011Cb692KDqmr86XZfK7k91z",
  "type": "assistant",
  "uuid": "df68f904-dad6-4053-b104-a5cb1ba1a540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8RFhvh8NzkXzTzjtrGCRJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19327,
      "cache_read_input_tokens": 52409,
      "output_tokens": 32703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32703,
          "cache_read_input_tokens": 52409,
          "cache_creation_input_tokens": 19327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19327
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分新家族 depth signal 退化（类似 Qwen3-8B 模式），泛化 claim 需收窄但核心贡献不变 核心假设：['3 个新家族中 1-2 个 held-out F1 < 0.60（类似 instruct 退化但不至于 chance level）', '扩展后 LOGO binary F1…",
  "leafUuid": "df68f904-dad6-4053-b104-a5cb1ba1a540",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Median scenario paper framing for gen-depth-fingerprint",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分新家族 depth signal 退化（类似 Qwen3-8B 模式），泛化 claim 需收窄但核心贡献不变 核心假设：['3 个新家族中 1-2 个 held-out F1 < 0.60（类似 instruct 退化但不至于 chance level）', '扩展后 LOGO binary F1…",
  "leafUuid": "df68f904-dad6-4053-b104-a5cb1ba1a540",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Median scenario paper framing for gen-depth-fingerprint",
  "sessionId": "90143ee6-16f1-4985-88d2-ed06c2b2634a"
}
```

---
