# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/972f39cd-72bc-47ff-9cc5-afbde8e9b66d.jsonl`
- **Structured JSON:** [`3ddd91dbb813c42facca.json`](../../sessions/3d/3ddd91dbb813c42facca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T10:52:48.506Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T10:52:48.506Z",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: gen-depth-fingerprint\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR (deadline: May 25, 2026)** — D012\n- Fallback: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response**: **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **distributional shape features** (entropy_std, tail_decay) remain near-stationary. This differential response is consistent with recursive generation inducing a **location shift** in the NLL distribution — the text becomes progressively more predictable (mean shifts) while the functional form of the distribution is preserved (shape is invariant). The genuine novelty is not the drift/stationarity split per se (which follows from location-shift properties), but: (a) the **task formulation** (ordinal depth estimation beyond binary detection), (b) **empirical validation** across 6 generators / 3 model families (including 7B+ scale) showing this pattern is robust, (c) the practical consequence that combining both feature types yields **complementary signal** for depth classification. **Primary metric (D017)**: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, excluding gen-0 due to shared-seed leakage). 3-class LOGO F1 = 0.789 reported as supplementary with gen-0 caveat. Per-generator held-out F1: 0.68–0.86 (std=0.058). Key finding: in binary evaluation (no gen-0 leakage), 7-feature (0.723) > 4-baseline ensemble (0.712) — baseline advantage in 3-class was entirely from gen-0 classification. Depth signal is scale-invariant as a phenomenon, though cross-scale classifier transfer shows a moderate gap (8B held-out F1=0.69 vs ≤2.8B 0.76-0.85).\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth with F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation). Primary metric: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, gen-0 excluded due to shared-seed overlap). 3-class (gen-0/gen-1/gen-2+) LOGO F1 = 0.789 supplementary with caveat.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Depth-dependent features exhibit differential response: central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (consistent with location shift in NLL distribution), while shape features (entropy_std, tail_decay) remain near-stationary. In binary eval, 7-feature ensemble (0.723) outperforms 4-baseline detector ensemble (0.712) by +1.1pp and all individual detectors (+1.1–19.9pp). The 4-baseline advantage in 3-class (0.796 vs 0.789) is entirely from gen-0 classification. Ordinal-specific methods (CORAL 0.771, Frank-Hall 0.793) do not outperform XGBoost (0.789) — CI overlap at 3-class granularity.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality compared to random subsampling. At equal data count, size_matched (random control, ppl=2.367) outperforms depth01 (depth-stratified, 2.387) and binary_filtered (2.389). The primary determinant is data quantity, not depth composition (all 12K samples → ppl=2.335). Depth fingerprinting is an effective **diagnostic** tool for characterizing provenance, but not a **curative** tool for data curation. This honest negative finding is reported transparently.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation. When repurposed as ordinal depth predictors, single detector scores (Avg-LogProb 0.737, LD-Score 0.655, FastDetectGPT 0.688, Binoculars 0.417 under 6-gen LOGO) show moderate signal but **high per-generator F1 variance** (e.g., AvgLogProb range 0.615–0.805, 19.0pp span), making them unreliable as standalone depth estimators.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **differential depth response**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth, while distributional shape features (entropy variance, tail decay) remain near-stationary. This split is about **what the feature measures** (central tendency vs shape), not where it comes from. The combination of drifting and stationary features yields a 7-feature ensemble that **significantly and consistently** outperforms all single-detector baselines: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, p<0.001 vs Avg-LogProb 0.712, LD-Score 0.701, FastDetectGPT 0.616, Binoculars 0.524). In the leak-free binary evaluation, 7-feature (0.723) > 4-baseline ensemble (0.712), reversing the 3-class result where baseline advantage came entirely from gen-0 classification. The practical advantage is **reliability across unknown generators** — per-generator F1 std = 0.058 for our ensemble vs higher variance for individual detectors.\n\n**Headline result template**: \"On non-paraphrastic continuation chains across 6 base-model generators from 3 model families (0.6B–8.2B), our 7-feature distributional ensemble achieves binary LOGO F1 of 0.72 for leak-free depth discrimination (gen-1 vs gen-2+), outperforming all individual detection baselines. Per-generator held-out F1 ranges from 0.68 to 0.86 (std=0.051). Depth-aware data curation does not outperform random subsampling for downstream CLM quality, establishing depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.73 macro-F1, but full 7-feature ensemble achieves 0.789 3-class / 0.723 binary (p<0.001). We don't claim reference features are \"better\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). Note: \"fingerprint\" in the paper refers to the full feature vector's combination, not just reference-model features.\n\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\n\n**RC9 — \"Only ≤2.8B generators — does this transfer to frontier scale?\"**: **Answered (plan-014, D011).** Qwen3-8B (7.6B params) added as 6th generator. Depth signal IS present at 8B scale — all feature-depth Spearman correlations significant. Cross-scale transfer gap: 8B held-out F1=0.69 vs ≤2.8B 0.76-0.85. P0-B volume-matched control: adding Qwen3-8B's +1.1pp improvement is 94% from generator diversity, not data volume. **Paper framing**: depth signal universality supported; cross-scale gap is honest limitation; scope narrowed to base models (see N3/N4 fixes).\n\n**RC10 — \"Text length confound\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\n\n**RC11 — \"Downstream utility — single run, no CIs\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\n\n## Contribution Positioning (D006+D007)\nThe contribution is **primarily empirical and conceptual**, not methodological:\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection (genuinely novel — no prior work)\n2. **Empirical characterization**: Differential depth response across 6 generators / 3 families (including 7B+ scale), with robust cross-generator generalization (binary LOGO F1=0.723, 3-class LOGO F1=0.789). Scale-invariant phenomenon with honest cross-scale transfer gap.\n3. **Negative finding**: Depth-aware data curation does NOT improve downstream CLM quality — depth fingerprinting is diagnostic, not curative (D009).\n\n**Framing discipline (D007 — re-dream consensus):**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution (means shift under distributional drift, shapes don't). Acknowledge this explicitly.\n- Do NOT use H1/H2 terminology (overloads time-series unit-root convention). Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics\" as a novel theoretical framework. Use \"differential depth response\" — more calibrated.\n- Consider renaming \"distributional fingerprinting\" → \"distributional depth profiling\" (fingerprinting implies source identification, creates confusion with LLM attribution literature).\n- Provide at least a speculative theoretical motivation for WHY shape features remain stationary (e.g., \"shape is determined by sampling mechanism and architecture, invariant to input content drift\").\n- Report **realistic performance range** (0.68–0.86 per-generator held-out F1, binary LOGO F1=0.72, 3-class LOGO F1=0.79 with gen-0 caveat) in abstract/conclusion, not just best-case. **禁止用 CI width 作为 cross-generator 一致性论据**（Round 2 C1 critical）——用 per-gen F1 std/range 替代。\n- R² on 5 aggregated depth means is statistically meaningless (3 df). Use individual-level Spearman ρ with bootstrap CIs throughout.\n\nRelated work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020), **stylometry/authorship attribution** (Stamatatos 2009, Koppel et al. 2009 — feature set is essentially stylometric), **iterative generation** (LLM as Broken Telephone ACL 2025, Markovian Generation Chains), **membership inference** (Shi et al. 2024).\n\n## Venue Fit\n- **EMNLP 2026**: Excellent fit — directly addresses \"New Missions for NLP Research\" theme (data contamination, synthetic data feedback loops, data governance). NLP-native venue. Empirical/conceptual contributions well-received. Novel task formulation + honest negative finding valued.\n\n## Open Questions (pending P1-C)\n- Instruct model depth response: if Qwen3-1.7B-Instruct shows drift → extend to 1-2 more instruct models; if not → limitation paragraph (scope narrowing already in place)\n- Rd2-W4 (no validated alternative application): diagnostic framing is current defense; no new experiment planned unless P1-C opens a new angle\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  registry_id: plan-003\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'DONE. Registry: plan-003 (parent), plan-003-olmo2ref, plan-003-qwen06bref.\n    Falsification test passed: entropy drift confirmed across all 3 reference families.\n    dual_dynamics_is_pythia_artifact: false. LOGO F1: Pythia 0.803, OLMo 0.807, Qwen\n    0.816.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  registry_id: plan-004-v2\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  registry_id: plan-005\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  registry_id: plan-007-cross-model\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: DONE\n  conclusion: success\n  metrics:\n    3class_macro_f1: 0.8089\n    3class_f1_std: 0.0166\n    binary_f1_gen1_vs_gen2plus: 0.7635\n    binary_f1_gen0_vs_gen2plus: 0.8372\n    per_class_f1:\n      gen0: 0.9285\n      gen1: 0.7367\n      gen2plus: 0.7614\n    n_samples: 2964\n    avg_generators_per_chain: 3\n    feature_importance:\n      hapax_ratio: 0.357\n      entropy_mean: 0.204\n      ttr: 0.202\n    vs_single_model:\n      pythia-1b: 0.8622\n      qwen3-0.6b: 0.8354\n      pythia-2.8b: 0.8156\n      qwen3-1.7b: 0.8106\n      olmo-2-1b: 0.7801\n      cross-model: 0.8089\n    n_samples_note: corrected from 4773 to 2964 per confusion matrix sum\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  registry_id: plan-008-multi-domain\n  description: 'Expand seeds to 3 domains: news (CNN/DailyMail), scientific (arXiv\n    abstracts via ccdv/arxiv-summarization), creative writing (WritingPrompts). 500\n    seeds per domain × 5 depths. Wikipedia used as transfer evaluation target (not\n    a seed domain). Single generator: Pythia-2.8B only (initial domain robustness\n    validation).\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  notes: 'Original plan said \"S2ORC abstracts\" but script uses ccdv/arxiv-summarization\n    (arXiv paper abstracts, more accessible on HuggingFace). Both are scientific text.\n    Wikipedia moved from seed domain to cross-domain transfer evaluation target. Single-generator\n    (Pythia-2.8B) limits claim scope — cannot directly support \"across domains AND\n    generators\" without multi-generator follow-up.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    per_domain:\n      news:\n        3class_f1: 0.5614\n        binary_f1: 0.6264\n      scientific:\n        3class_f1: 0.7049\n        binary_f1: 0.7701\n      creative:\n        3class_f1: 0.6275\n        binary_f1: 0.731\n      wikipedia:\n        3class_f1: 0.7928\n        binary_f1: 0.8224\n    cross_domain_pooled:\n      3class_f1: 0.4775\n      binary_f1: 0.6742\n    wiki_transfer:\n      news: 0.231\n      scientific: 0.3351\n      creative: 0.2319\n    n_records:\n      news: 2314\n      scientific: 2316\n      creative: 2466\n    dedup_applied: true\n    dedup_removed:\n      news: 801\n      scientific: 0\n      creative: 0\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  registry_id: plan-010-human-edit\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  notes: 'DONE/success. Graceful degradation: 5-20% random replacement -3.5 to -6.0pp\n    3-class, binary nearly unchanged. LLM rephrase: 3-class -3.4pp, binary -6.3pp.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline:\n      3class_f1: 0.7889\n      binary_f1: 0.7241\n      ci_3class:\n      - 0.787\n      - 0.798\n      ci_binary:\n      - 0.719\n      - 0.734\n    random_5pct:\n      3class_f1: 0.7538\n      binary_f1: 0.7182\n      delta_3class: -0.0351\n      delta_binary: -0.0059\n    random_10pct:\n      3class_f1: 0.7425\n      binary_f1: 0.7168\n      delta_3class: -0.0464\n      delta_binary: -0.0073\n    random_20pct:\n      3class_f1: 0.7292\n      binary_f1: 0.7165\n      delta_3class: -0.0597\n      delta_binary: -0.0076\n    llm_rephrase:\n      3class_f1: 0.7549\n      binary_f1: 0.6615\n      delta_3class: -0.034\n      delta_binary: -0.0626\n    degradation_curve: robust\n    llm_rephrase_robust: true\n    finding: 'Graceful degradation: 5-20% random replacement drops 3-class F1 by 3.5-6.0pp.\n      LLM rephrase: 3-class robust (-3.4pp) but binary degrades more (-6.3pp).'\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  registry_id: review-exp-a-baseline-ensemble\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  notes: 'Subsumed by plan-015 + review-exp-a-baseline-ensemble. LD-Score evaluated\n    as standalone baseline (3class=0.655, binary=0.701) and in multi-detector ensemble\n    (4-det+surface: 3class=0.805, binary=0.724). No separate plan_011 run needed.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    4_baseline:\n      avg_f1: 0.7964\n      ci95:\n      - 0.7921\n      - 0.8007\n    4_baseline_plus_surface:\n      avg_f1: 0.8049\n      ci95:\n      - 0.8003\n      - 0.8092\n    7_feature_unified:\n      avg_f1: 0.7887\n      ci95:\n      - 0.7839\n      - 0.793\n    7_feature_original:\n      avg_f1: 0.7887\n      ci95:\n      - 0.7839\n      - 0.793\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  registry_id: plan-013\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  registry_id: plan-014\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  registry_id: plan-015\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4_baseline:\n      avg_f1: 0.7964\n      ci95:\n      - 0.7921\n      - 0.8007\n    4_baseline_plus_surface:\n      avg_f1: 0.8049\n      ci95:\n      - 0.8003\n      - 0.8092\n    7_feature_unified:\n      avg_f1: 0.7887\n      ci95:\n      - 0.7839\n      - 0.793\n    7_feature_original:\n      avg_f1: 0.7887\n      ci95:\n      - 0.7839\n      - 0.793\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_f1_v2: 0.7878\n    overall_ci95_v2:\n    - 0.783\n    - 0.792\n    ci_width: 0.009\n    pipeline: bootstrap_ci_v2.py (class-balanced downsample)\n    per_gen_sanity_check:\n      olmo-2-1b: 0.7649\n      pythia-1b: 0.8528\n      pythia-2.8b: 0.8037\n      qwen3-0.6b: 0.8231\n      qwen3-1.7b: 0.8064\n      qwen3-8b: 0.6815\n- exp_id: review-p0a-gen0-leakage\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 21557\n    7_feature:\n      f1: 0.7233\n      ci95:\n      - 0.7174\n      - 0.7292\n    avg_logprob:\n      f1: 0.7124\n      ci95:\n      - 0.706\n      - 0.7189\n    ld_score:\n      f1: 0.7009\n      ci95:\n      - 0.6942\n      - 0.7073\n    fastdetectgpt:\n      f1: 0.6155\n      ci95:\n      - 0.6086\n      - 0.6222\n    binoculars:\n      f1: 0.524\n      ci95:\n      - 0.5167\n      - 0.5306\n    4_baseline:\n      f1: 0.7118\n      ci95:\n      - 0.7052\n      - 0.7182\n    4_baseline_surface:\n      f1: 0.7239\n      ci95:\n      - 0.7179\n      - 0.7303\n- exp_id: review-p0b-volume-matched\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    5gen_logo_original: 0.8019\n    5gen_volume_matched_avg: 0.8024\n    6gen_logo_excl_qwen8b: 0.8102\n    volume_effect_pp: 0.05\n    diversity_residual_pp: 0.78\n    diversity_pct: 94\n- exp_id: review-p1c-instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_records: 4963\n    depths: 5\n    seeds: 996\n    length_depth_spearman: -0.52\n    length_confound_dominates: true\n    depth_signal_after_control: negligible\n    length_per_depth_tokens:\n      '0': 252\n      '1': 79\n      '2': 74\n      '3': 72\n      '4': 68\n    original_rho:\n      ttr: 0.48\n      hapax: 0.477\n      entropy_mean: 0.478\n    length_matched_rho:\n      ttr: 0.19\n      hapax: 0.224\n      entropy_mean: 0.042\n    partial_rho:\n      ttr: 0.13\n      hapax: 0.166\n      entropy_mean: 0.161\n    binary_gen1_vs_gen2plus_f1: 0.506\n- exp_id: review-p1d-table3-6gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    avglogprob_100_3: 0.737\n    avglogprob_200_6: 0.737\n    fastdetectgpt_100_3: 0.688\n    fastdetectgpt_200_6: 0.688\n    ldscore_100_3: 0.655\n    ldscore_200_6: 0.654\n    binoculars_100_3: 0.416\n    binoculars_200_6: 0.417\n    max_hyperparam_delta: 0.0011\n    hyperparam_effect: negligible\n- exp_id: review-p1e-ordinal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    xgboost_3class_f1: 0.7888\n    coral_3class_f1: 0.7711\n    frankhall_3class_f1: 0.7931\n    xgboost_binary_f1: 0.7213\n    coral_binary_f1: 0.7275\n    xgboost_concordance: 0.821\n    coral_concordance: 0.81\n    frankhall_concordance: 0.825\n    ordinal_benefit: negligible\n    ci_overlap: true\n- exp_id: review-p2f-cross-ref-bias\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia1b_f1_pythia410m_ref: 0.856\n    pythia1b_f1_olmo_ref: 0.845\n    pythia1b_f1_qwen_ref: 0.848\n    same_to_cross_drop: 0.009\n    pythia1b_rank_all_refs: 1\n    same_family_bias: false\n- exp_id: review-p1c-olmo-instruct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    instruct_logo_f1: 0.338\n    base_olmo_logo_f1: 0.763\n    delta: -0.425\n    n_records: 4429\n    binary_logo_f1: 0.3506\n    length_depth_spearman: -0.3701\n    length_confound_dominates: false\n    depth_signal_after_control: partially_survives\n    original_rho:\n      entropy_mean: 0.4822\n      ttr: 0.0057\n      hapax: 0.0253\n    partial_rho:\n      entropy_mean: 0.364\n      ttr: -0.2407\n      hapax: -0.1979\n    entropy_reversal_survives_length_control: true\n    surface_reversal: false\n- exp_id: review-p1c-qwen06b-instruct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    instruct_logo_3class_f1: 0.667\n    base_logo_3class_f1: 0.816\n    delta_3class: -0.148\n    binary_gen1_vs_gen2plus_f1: 0.552\n    length_depth_spearman: -0.583\n    length_confound_dominates: true\n    depth_signal_after_control: negligible\n    length_per_depth_tokens:\n      '0': 252\n      '1': 35\n      '2': 27\n      '3': 24\n      '4': 23\n    length_matched_rho:\n      ttr: -0.007\n      hapax: -0.003\n      entropy_mean: -0.012\n- exp_id: review-rd2m7-bib-audit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    diveye:\n      year_correct: true\n      year: 2026\n      venue: TMLR\n      author_fix: Varun Basani → Advik Raj Basani, Yuntian Chen → Pin-Yu Chen\n    strong_model_collapse:\n      year_correct: true\n      year: 2025\n      venue: ICLR\n    aaronson_watermark:\n      author_fix: Chelsea → Hendrik Kirchner\n      url_added: https://scottaaronson.blog/?p=6823\n- exp_id: review-sampling-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_t05_p08:\n      3class_f1: 0.785\n      binary_f1: 0.797\n      spearman_entropy_mean: -0.694\n    default_t07_p09:\n      3class_f1: 0.788\n      binary_f1: 0.799\n      spearman_entropy_mean: -0.602\n    high_t10_p095:\n      3class_f1: 0.726\n      binary_f1: 0.733\n      spearman_entropy_mean: -0.002\n    f1_range_pp: 6.19\n    robust: false\n    finding: Low/default configs robust (<0.3pp diff). High temp (t=1.0) degrades\n      depth signal ~6pp; entropy correlation drops to ~0. Qwen3-1.7B per-gen F1 collapses\n      to 0.418 at high temp.\n- exp_id: review-p1c-instruct-logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    7gen_logo_avg_f1: 0.7498\n    7gen_binary_f1: 0.768\n    6gen_base_logo_f1: 0.789\n    6gen_base_binary_f1: 0.723\n    instruct_held_out_3class_f1: 0.5434\n    instruct_held_out_binary_f1: 0.6582\n    base_qwen17b_held_out_3class_f1: 0.8023\n    base_qwen17b_held_out_binary_f1: 0.8208\n    instruct_vs_base_delta_3class: -0.2589\n    instruct_vs_base_delta_binary: -0.1626\n- exp_id: plan-010-human-edit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline:\n      3class_f1: 0.7889\n      binary_f1: 0.7241\n      ci_3class:\n      - 0.787\n      - 0.798\n      ci_binary:\n      - 0.719\n      - 0.734\n    random_5pct:\n      3class_f1: 0.7538\n      binary_f1: 0.7182\n      delta_3class: -0.0351\n      delta_binary: -0.0059\n    random_10pct:\n      3class_f1: 0.7425\n      binary_f1: 0.7168\n      delta_3class: -0.0464\n      delta_binary: -0.0073\n    random_20pct:\n      3class_f1: 0.7292\n      binary_f1: 0.7165\n      delta_3class: -0.0597\n      delta_binary: -0.0076\n    llm_rephrase:\n      3class_f1: 0.7549\n      binary_f1: 0.6615\n      delta_3class: -0.034\n      delta_binary: -0.0626\n    degradation_curve: robust\n    llm_rephrase_robust: true\n    finding: 'Graceful degradation: 5-20% random replacement drops 3-class F1 by 3.5-6.0pp.\n      LLM rephrase: 3-class robust (-3.4pp) but binary degrades more (-6.3pp).'\n- exp_id: plan-008-multi-domain\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    per_domain:\n      news:\n        3class_f1: 0.5614\n        binary_f1: 0.6264\n      scientific:\n        3class_f1: 0.7049\n        binary_f1: 0.7701\n      creative:\n        3class_f1: 0.6275\n        binary_f1: 0.731\n      wikipedia:\n        3class_f1: 0.7928\n        binary_f1: 0.8224\n    cross_domain_pooled:\n      3class_f1: 0.4775\n      binary_f1: 0.6742\n    wiki_transfer:\n      news: 0.231\n      scientific: 0.3351\n      creative: 0.2319\n    n_records:\n      news: 2314\n      scientific: 2316\n      creative: 2466\n    dedup_applied: true\n    dedup_removed:\n      news: 801\n      scientific: 0\n      creative: 0\n- exp_id: plan-007-cross-model\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    3class_macro_f1: 0.8089\n    3class_f1_std: 0.0166\n    binary_f1_gen1_vs_gen2plus: 0.7635\n    binary_f1_gen0_vs_gen2plus: 0.8372\n    per_class_f1:\n      gen0: 0.9285\n      gen1: 0.7367\n      gen2plus: 0.7614\n    n_samples: 2964\n    avg_generators_per_chain: 3\n    feature_importance:\n      hapax_ratio: 0.357\n      entropy_mean: 0.204\n      ttr: 0.202\n    vs_single_model:\n      pythia-1b: 0.8622\n      qwen3-0.6b: 0.8354\n      pythia-2.8b: 0.8156\n      qwen3-1.7b: 0.8106\n      olmo-2-1b: 0.7801\n      cross-model: 0.8089\n    n_samples_note: corrected from 4773 to 2964 per confusion matrix sum\n- exp_id: plan-006-paraphrastic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    paraphrastic_3class_f1: 0.68\n    paraphrastic_3class_f1_std: 0.0086\n    paraphrastic_binary_f1: 0.539\n    paraphrastic_binary_f1_std: 0.017\n    continuation_3class_f1: 0.788\n    continuation_3class_f1_std: 0.0061\n    continuation_binary_f1: 0.749\n    continuation_binary_f1_std: 0.011\n    f1_3class_delta: -0.108\n    retention_para: 0.8915\n    retention_cont: 0.8261\n    retention_delta: 0.0654\n    cross_transfer_para_to_cont_f1: 0.155\n    cross_transfer_cont_to_para_f1: 0.431\n    spearman_entropy_mean_para: 0.394\n    spearman_entropy_mean_cont: -0.675\n    spearman_ttr_para: 0.567\n    spearman_ttr_cont: -0.633\n    spearman_hapax_para: 0.556\n    spearman_hapax_cont: -0.655\n    spearman_signs_reversed: true\n    n_paraphrastic: 4754\n    n_continuation: 4609\n- exp_id: plan-009-finer-ordinal\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    5class_HGBT_macro_f1: 0.5028\n    5class_HGBT_f1_95ci:\n    - 0.4974\n    - 0.5079\n    5class_HGBT_accuracy: 0.5423\n    5class_HGBT_mae: 0.6587\n    5class_RF_macro_f1: 0.4767\n    5class_LR_macro_f1: 0.4468\n    5class_FrankHall_macro_f1: 0.4513\n    3class_HGBT_macro_f1: 0.7815\n    3class_HGBT_f1_95ci:\n    - 0.7764\n    - 0.7864\n    delta_5class_vs_3class: -0.2787\n    5class_per_class_f1:\n      depth_0: 0.9129\n      depth_1: 0.6277\n      depth_2: 0.2687\n      depth_3: 0.2653\n      depth_4: 0.4393\n    gen2_gen3_inseparable: true\n- exp_id: plan-012-qwen06b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    5class_macro_f1: 0.583\n    5class_f1_std: 0.01\n    3class_macro_f1: 0.905\n    3class_f1_std: 0.003\n    per_class_f1:\n      gen0: 0.999\n      gen1: 0.796\n      gen2: 0.413\n      gen3: 0.259\n      gen4: 0.447\n    runtime_seconds: 6928\n    model: Qwen3-0.6B-Base\n    method: QLoRA\n    lora_rank: 16\n    seed: 42\n- exp_id: plan-006-confound-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_paraphrastic_clean: 4912\n    n_paraphrastic_contaminated_removed: 4754\n    paraphrastic_3class_f1: 0.742\n    paraphrastic_binary_f1: 0.671\n    continuation_3class_f1: 0.788\n    continuation_binary_f1: 0.749\n    f1_3class_delta: -0.046\n    spearman_entropy_mean_para: -0.533\n    spearman_entropy_mean_cont: -0.675\n    entropy_reversal_was_artifact: true\n    cross_transfer_para_to_cont_f1: 0.77\n    cross_transfer_cont_to_para_f1: 0.743\n    depth_retention_para: 0.97\n    vs_contaminated:\n      old_3class_f1: 0.68\n      new_3class_f1: 0.742\n      old_binary_f1: 0.539\n      new_binary_f1: 0.671\n      old_entropy_rho: 0.394\n      new_entropy_rho: -0.533\n- exp_id: plan-012-pythia410m\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    5class_macro_f1: 0.556\n    5class_f1_std: 0.016\n    3class_macro_f1: 0.87\n    3class_f1_std: 0.022\n    per_class_f1:\n      gen0: 0.991\n      gen1: 0.733\n      gen2: 0.347\n      gen3: 0.291\n      gen4: 0.42\n    runtime_seconds: 3705\n    model: Pythia-410M\n    method: QLoRA\n- exp_id: plan-012-qwen06b-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    5class_macro_f1: 0.5873\n    5class_f1_std: 0.0047\n    3class_macro_f1: 0.9054\n    3class_f1_std: 0.0037\n    per_class_5class:\n      depth_0: 0.9995\n      depth_1: 0.7959\n      depth_2: 0.4016\n      depth_3: 0.3176\n      depth_4: 0.4217\n    per_class_3class:\n      gen0: 0.9995\n      gen1: 0.7959\n      gen2plus: 0.9209\n    runtime_minutes: 116.7\n    model: Qwen3-0.6B-Base\n    method: QLoRA\n    lora_rank: 32\n    seed: 123\n    results_file: results/plan012_qwen06b_seed123_r32_results.json\n    vs_xgboost_5class_delta_pp: 8.5\n    vs_xgboost_3class_delta_pp: 12.4\n- exp_id: plan-016-llama32-3b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-016-gemma2-2b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-016-mistral-7b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-016-crossref-qwen8b\n  name: ''\n  status: QUEUED\n  conclusion: success\n  metrics:\n    logo_avg_pythia_ref: 0.7891\n    logo_avg_olmo_ref: 0.7948\n    logo_avg_qwen_ref: 0.8135\n    qwen8b_pythia_ref: 0.6854\n    qwen8b_olmo_ref: 0.6962\n    qwen8b_qwen_ref: 0.7568\n    ci95_pythia:\n    - 0.747\n    - 0.824\n    ci95_olmo:\n    - 0.757\n    - 0.828\n    ci95_qwen:\n    - 0.785\n    - 0.842\n    all_entropy_drift_negative: true\n    spread_across_refs: 0.024\n- exp_id: plan-016-llama32-3b-rp11\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T10:52:48.510Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T10:52:48.510Z",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T10:52:48.527Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "352a18ae-a930-41aa-a07d-6602797aaa80",
  "type": "user",
  "uuid": "8720cf55-99e4-451a-bd3f-8481b6b53432",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T10:52:48.526Z_

```json
{
  "parentUuid": "8720cf55-99e4-451a-bd3f-8481b6b53432",
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
  "uuid": "624d7868-71ac-4960-b103-d50688a0f8d3",
  "timestamp": "2026-05-16T10:52:48.526Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T10:52:48.526Z_

```json
{
  "parentUuid": "624d7868-71ac-4960-b103-d50688a0f8d3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8703838b-1ad1-4436-94fc-c5fe98c332a1",
  "timestamp": "2026-05-16T10:52:48.526Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "8703838b-1ad1-4436-94fc-c5fe98c332a1",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenarios for gen-depth-fingerprint Dream review",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d"
}
```

---

### Assistant

_source line 8 · 2026-05-16T10:53:24.455Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research project carefully to define three tiers (best/median/worst) for a Dream simulation.

Key facts from the data:
- Primary metric: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, excluding gen-0)
- 3-class LOGO F1 = 0.789 (with gen-0 caveat)
- Per-generator held-out F1: 0.68–0.86 (std=0.058)
- 7-feature vs best single detector (Avg-LogProb): +3.3pp advantage (significant, p<0.001)


- Significant performance drop at 8B scale (0.69 vs 0.76-0.85 for smaller models), and downstream utility shows no benefit from depth-aware curation
- Cross-model chains achieve 0.76 binary F1, but multi-domain performance is inconsistent (0.67 pooled, ranging 0.63-0.82 within domains)
- Human edits cause graceful degradation of 3.5-6pp, paraphrastic variants underperform continuations (0.67 vs 0.75), and length isn't a confounding factor
- Differential depth response holds across three reference model families, though instruct models largely lose the depth signal and high sampling temperature (~1.0) erodes it by about 6pp
- The paper targets EMNLP 2026, anchoring on three core claims: depth discriminability above chance across generators, differential depth response with feature complementarity, and negative downstream utility
- Still waiting on results from three additional model families (Llama-3.2-3B, Gemma-2-2B, Mistral-7B) that could either strengthen or challenge the generalization story

If these pending experiments all show robust depth signal, I can claim broad generalization across 6+ generators and 5+ families including larger scales. If some degrade like Qwen3-8B did (F1=0.68), I'll need more nuanced framing around architectural limitations. Worst case, if multiple fail like the instruct models, the phenomenon might be narrower than currently framed—tied to specific training distributions or architectures rather than a general property. The real risk is whether plan-016 generators actually exhibit the depth signal at all. weakens generalization claim
2. The 7-feature advantage over Avg-LogProb is only 3.3pp → reviewers might say it's marginal
3. Cross-domain pooled F1 is only 0.48 (3-class) / 0.67 (binary) → domain transfer is weak
4. Instruct models don't work → scope limitation
5. The negative downstream result means no "practical utility" beyond diagnostics

Let me define the tiers based on what would make the paper strong vs. weak at EMNLP:

**Best**: Plan-016 all succeed (new families confirm universality), reviewer concerns are manageable, the differential response story is clean and compelling. Binary LOGO F1 with expanded generators stays ≥0.72. Paper tells a clean story of a novel task + robust phenomenon + honest negative finding.

**Median**: Some plan-016 generators degrade, bringing average LOGO F1 down and muddying the baseline comparison. I'd need to soften the universality claims and acknowledge more limitations, but it's still publishable with careful framing.

**Worst**: Plan-016 reveals the phenomenon is architecture or training-data dependent rather than universal. Cross-family transfer degrades significantly with truly diverse families, and the 3.3pp advantage over Avg-LogProb doesn't hold up under expanded evaluation. The story shifts from "universal phenomenon" to "characterization of specific generation regimes" — still a novel task, but the empirical contribution weakens considerably.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8703838b-1ad1-4436-94fc-c5fe98c332a1",
  "isSidechain": false,
  "requestId": "req_011Cb68344gUttXx7thotuWz",
  "type": "assistant",
  "uuid": "8cb72d75-4cde-4843-a457-df3c2d1aed07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVstE1GXkTcfeA34SoFVRq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28307,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3148,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28307
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

_source line 9 · 2026-05-16T10:54:03.563Z_

```yaml
tiers:
  best:
    meaning: "Plan-016 新模型族全部确认 depth signal，跨家族泛化完整成立，论文叙事无需调整"
    key_assumptions:
      - "Llama-3.2-3B / Gemma-2-2B / Mistral-7B 三个新家族均显示显著 depth-feature Spearman ρ (|ρ|>0.3 for drifting features)"
      - "扩展至 9 generators / 6 families 后，LOGO binary F1 ≥ 0.71，7-feature 优势 ≥ +2.5pp vs best single detector"
      - "新家族 held-out F1 ≥ 0.65（不低于 Qwen3-8B 的 0.68 水平）"
      - "differential response pattern（drift vs stationary）在新家族中复现，无逆转"
      - "cross-ref experiment (plan-016-crossref-qwen8b) 确认 reference model 选择不改变结论方向"
    number_ranges:
      binary_logo_f1_9gen: [0.71, 0.74]
      per_gen_f1_std: [0.04, 0.07]
      worst_single_gen_f1: [0.65, 0.70]
      seven_feat_vs_best_baseline_pp: [2.5, 5.0]
      new_family_avg_held_out_f1: [0.68, 0.78]
      drifting_feature_spearman_range: [-0.70, -0.35]
      shape_feature_spearman_range: [-0.12, 0.12]
    narrative_direction: >
      原始 framing 完全成立。Novel task formulation + 9 generators / 6 families 的 robust 
      empirical validation + honest negative finding。Claims 无需降级：
      Claim 1 扩展为 "across 6 model families including 3B-8B scale"；
      Claim 2 differential response 在所有家族复现；
      Claim 3 negative finding 不变。
      Instruct limitation 作为 scope boundary 清晰界定。
      EMNLP 投稿强度：strong accept 可能。

  median:
    meaning: "部分新家族 depth signal 退化（类似 Qwen3-8B 模式），泛化 claim 需收窄但核心贡献不变"
    key_assumptions:
      - "3 个新家族中 1-2 个 held-out F1 < 0.60（类似 instruct 退化但不至于 chance level）"
      - "扩展后 LOGO binary F1 下降至 0.68-0.71 区间（被低性能 generator 拉低）"
      - "7-feature vs best baseline 优势缩窄至 +1.0-2.5pp（仍显著但 effect size 小）"
      - "differential response 在多数但非全部家族成立（个别家族 shape feature 也出现 drift）"
      - "某些家族的 cross-scale/cross-architecture gap 比预期更大"
    number_ranges:
      binary_logo_f1_expanded: [0.68, 0.72]
      per_gen_f1_std: [0.07, 0.11]
      worst_single_gen_f1: [0.50, 0.62]
      seven_feat_vs_best_baseline_pp: [1.0, 2.5]
      new_family_avg_held_out_f1: [0.55, 0.68]
      drifting_feature_spearman_range: [-0.55, -0.20]
      shape_feature_spearman_range: [-0.20, 0.20]
    narrative_direction: >
      需要调整 claims 强度。Claim 1 从 "generalizes across model families" 收窄为 
      "robust within tested base-model regime (≤8B), with architecture-dependent transfer gap 
      as honest limitation"。Claim 2 补充 caveat：differential response 是 dominant pattern 
      但非 universal（某些架构 shape features 也漂移）。增加 "conditions under which depth 
      signal degrades" 的系统分析作为额外贡献。Paper 仍以 novel task + empirical 
      characterization 为主线，但 universality claim 变为 qualified generalization。
      可能需要 Table 明确标注哪些 generators 属于 "high-signal" vs "low-signal" regime。
      EMNLP 投稿强度：borderline accept，需要 rebuttal 说服 1-2 个 reviewer。

  worst:
    meaning: "多数新家族 depth signal 极弱或模式不一致，'universal phenomenon' framing 崩塌，需 reframe 为更窄贡献"
    key_assumptions:
      - "3 个新家族中 2-3 个 held-out F1 < 0.55（接近 chance for binary）"
      - "扩展后 LOGO binary F1 < 0.67（原始 6-gen 结论被新数据稀释）"
      - "7-feature ensemble 在新家族上不再优于 Avg-LogProb（baseline parity 或更差）"
      - "differential response 在新家族不复现：shape features 也漂移，或 drifting features 不单调"
      - "结论被限定为 'Pythia/Qwen/OLMo 特定训练数据分布下的现象'"
    number_ranges:
      binary_logo_f1_expanded: [0.62, 0.68]
      per_gen_f1_std: [0.11, 0.16]
      worst_single_gen_f1: [0.35, 0.52]
      seven_feat_vs_best_baseline_pp: [-1.0, 1.0]
      new_family_avg_held_out_f1: [0.40, 0.55]
      drifting_feature_spearman_range: [-0.35, -0.05]
      shape_feature_spearman_range: [-0.30, 0.30]
    narrative_direction: >
      核心 "universal differential response" framing 不成立。Reframe 方向（仍冲 EMNLP，不降级）：
      (1) 从 "depth fingerprinting works" 转为 "when and why depth fingerprinting works/fails"——
      条件分析本身就是贡献（哪些架构/训练regime下信号存在，哪些下消失）；
      (2) 强化 negative findings 叙事：novel task formulation + systematic empirical study 
      revealing the boundaries of depth discriminability；
      (3) 将 differential response 降级为 "observed in specific model families" 的 empirical 
      observation，而非 general claim；
      (4) 如果某些家族完全失败，分析 WHY（训练数据多样性？架构差异？）成为主要贡献之一。
      Paper 重心从 "method paper showing it works" 转为 "empirical study characterizing when 
      recursive generation leaves detectable traces"。Title 可能从 "Distributional Depth 
      Profiling" 改为 "On the Limits of Generation Depth Estimation"。
      EMNLP 投稿强度：需要强 writing 和清晰的 boundary characterization，weak accept 区间。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cb72d75-4cde-4843-a457-df3c2d1aed07",
  "isSidechain": false,
  "requestId": "req_011Cb68344gUttXx7thotuWz",
  "type": "assistant",
  "uuid": "34f46d6a-02b7-439b-b454-08b213541f51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVstE1GXkTcfeA34SoFVRq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28307,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3148,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28307
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "34f46d6a-02b7-439b-b454-08b213541f51",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenarios for gen-depth-fingerprint Dream review",
  "sessionId": "972f39cd-72bc-47ff-9cc5-afbde8e9b66d"
}
```

---
