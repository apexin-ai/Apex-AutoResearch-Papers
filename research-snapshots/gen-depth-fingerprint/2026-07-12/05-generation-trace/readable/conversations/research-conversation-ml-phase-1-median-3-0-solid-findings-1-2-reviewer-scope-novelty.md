# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：3.0 Solid Findings — 核心贡献被认可但有保留，1-2 个 reviewer 对 scope 或 novelty 有中等强度质疑，

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/3a67f408-621b-4ff2-81bc-a26238ed40ed.jsonl`
- **Structured JSON:** [`f68f2f89c00940246bd3.json`](../../sessions/f6/f68f2f89c00940246bd3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T10:12:17.725Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T10:12:17.725Z",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：3.0 Solid Findings — 核心贡献被认可但有保留，1-2 个 reviewer 对 scope 或 novelty 有中等强度质疑，需要 rebuttal 中补充解释或微调 claims\n核心假设：['DDR 被部分接受：审稿人认可 drifting features 的趋势，但质疑 shape feature 的 stationarity 是否只是 weak signal 而非 genuine invariance（entropy_std 的 TOST rejection rate=0 + d=0.458 被追问）', 'Base-model-only scope 被 1-2 个审稿人标记为 major limitation，要求讨论 instruct 场景下的 practical relevance', '0.694 F1 被认为 modest — 审稿人指出 per-gen range 0.633-0.724 的方差，质疑 worst-case (Mistral-7B 0.633) 的实用性', 'Negative downstream finding 被接受但审稿人要求更多 evidence（单一 perplexity metric + 3 seeds 被认为 limited）', 'Gemma-2-2B anomaly (gen-1 F1=0.036) 被追问：是方法失败还是 Gemma 特殊性？']\n关键指标范围：{'expected_reviewer_avg': [3.0, 3.5], 'reviewer_spread': [2, 4], 'logo_binary_f1_perception': \"0.694 被标注为 'modest' 或 'limited practical utility'\", 'ddr_entropy_std_challenge': 'entropy_std (d=0.458, TOST rejection=0) 需要解释为何归入 stationary 组', 'instruct_scope_penalty': '-0.5 pp on one reviewer — 需要在 rebuttal 中论证 base-model scope 的合理性', 'gemma_anomaly_penalty': '-0.25 pp — 需要在 paper 中显式讨论'}\n叙事方向：Claim 1 保持但在 abstract 中加入 per-gen range (0.633–0.724) 和 worst-case caveat。Claim 2 微调：将 entropy_std 从 stationary 组中移出或重新定义为 'intermediate'，DDR 从二分法调整为 spectrum（drifting → intermediate → stationary）。Claim 3 保持 negative framing 但承认 evidence 有限（3 seeds, 单 metric）。增加一段讨论：当前方法定位为 base-model provenance diagnostic，instruct 场景是 explicit future work。Rebuttal 重点回应 scope 和 Gemma anomaly。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nfocus: Paper has been significantly expanded since last dream (May 14). New additions: (1) 9-generator scale evaluation with Gemma-2-2B (Appendix), (2) DDR causality analysis with permutation importance + Granger causality + feature intervention, (3) TOST bootstrap stability validation, (4) cross-model evaluation upgraded from sample-level CV to generator-level LOGO (binary F1=0.830). Total 33 pages, 20+ appendix experiments. Assess whether this is 3.0 Findings or 3.5 Borderline Conference level. Identify the single highest-impact improvement that could be made in 5 days before DDL.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_logo_f1: 0.7879\n    overall_ci95:\n    - 0.783\n    - 0.7929\n    spearman_entropy_max: 0.0503\n    spearman_entropy_min: -0.4061\n    spearman_hapax: -0.6467\n    spearman_ttr: -0.6302\n    spearman_entropy_mean: -0.6098\n    spearman_entropy_std: -0.1996\n    spearman_tail_decay: -0.0403\n- exp_id: plan-010-robustness\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_binary_f1: 0.695\n    5pct_binary_f1: 0.65\n    10pct_binary_f1: 0.614\n    20pct_binary_f1: 0.591\n    5pct_drop: -0.046\n    10pct_drop: -0.081\n    20pct_drop: -0.104\n- exp_id: plan-010-llm-rephrase\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_binary_f1: 0.6918\n    original_binary_ci:\n    - 0.6749\n    - 0.7067\n    original_multiclass_f1: 0.7385\n    original_multiclass_ci:\n    - 0.7269\n    - 0.7496\n    rephrased_binary_f1: 0.6471\n    rephrased_binary_ci:\n    - 0.6308\n    - 0.6619\n    rephrased_multiclass_f1: 0.6672\n    rephrased_multiclass_ci:\n    - 0.6548\n    - 0.6796\n    binary_drop: -0.0447\n    multiclass_drop: -0.0713\n    edit_distance_ratio: 0.5071\n    avg_sentences_replaced: 1.69\n    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\n    bugs_fixed:\n    - binary_task_gen1_vs_gen2+\n    - 3class_mapping\n    - tail_decay_rank100-1000\n- exp_id: plan-008-seed-stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_complexity_binary: 0.685\n    medium_binary: 0.695\n    high_complexity_binary: 0.695\n    low_complexity_multi: 0.772\n    medium_multi: 0.778\n    high_complexity_multi: 0.779\n    max_diff_binary_pp: 1.06\n    max_diff_multiclass_pp: 0.68\n    conclusion_label: seed_independent\n- exp_id: multi-domain-seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7459\n    news_binary_ci:\n    - 0.726\n    - 0.764\n    news_multiclass_f1: 0.6516\n    academic_binary_f1: 0.7386\n    academic_binary_ci:\n    - 0.72\n    - 0.757\n    academic_multiclass_f1: 0.6223\n    code_binary_f1: 0.7535\n    code_binary_ci:\n    - 0.737\n    - 0.77\n    code_multiclass_f1: 0.6344\n    wikipedia_baseline_binary_f1: 0.8148\n    wikipedia_baseline_multiclass_f1: 0.8632\n    max_gap_vs_wiki_pp: 7.62\n    worst_domain: academic\n    best_domain: code\n    conclusion_label: domain_independent\n- exp_id: exp_047_multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7119\n    news_binary_ci:\n    - 0.6898\n    - 0.7332\n    news_3class_f1: 0.7149\n    academic_binary_f1: 0.6279\n    academic_binary_ci:\n    - 0.6027\n    - 0.6515\n    academic_3class_f1: 0.6564\n    code_binary_f1: 0.6872\n    code_binary_ci:\n    - 0.6641\n    - 0.71\n    code_3class_f1: 0.6729\n    overall_binary_f1: 0.6757\n    overall_3class_f1: 0.6814\n    delta_vs_t10_news: -0.034\n    delta_vs_t10_academic: -0.1107\n    delta_vs_t10_code: -0.0663\n- exp_id: multi_domain_t07\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_048_cross_temp_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    6gen_logo:\n      within_0.7_binary: 0.9471\n      within_0.7_3class: 0.7888\n      cross_0.7to1.0_binary: 0.9001\n      cross_0.7to1.0_3class: 0.7225\n      within_1.0_binary: 0.9107\n      within_1.0_3class: 0.7257\n      cross_1.0to0.7_binary: 0.9581\n      cross_1.0to0.7_3class: 0.7913\n      caveat: Only Qwen3-1.7B differs between conditions; 5/6 generators share data\n    qwen_only:\n      within_0.7_binary: 0.9262\n      within_0.7_binary_ci:\n      - 0.916\n      - 0.935\n      within_0.7_3class: 0.769\n      within_0.7_3class_ci:\n      - 0.756\n      - 0.781\n      cross_0.7to1.0_binary: 0.7574\n      cross_0.7to1.0_binary_ci:\n      - 0.745\n      - 0.77\n      cross_0.7to1.0_3class: 0.4581\n      cross_0.7to1.0_3class_ci:\n      - 0.445\n      - 0.472\n      within_1.0_binary: 0.8248\n      within_1.0_binary_ci:\n      - 0.81\n      - 0.838\n      within_1.0_3class: 0.5738\n      within_1.0_3class_ci:\n      - 0.56\n      - 0.588\n      cross_1.0to0.7_binary: 0.9443\n      cross_1.0to0.7_binary_ci:\n      - 0.936\n      - 0.953\n      cross_1.0to0.7_3class: 0.6014\n      cross_1.0to0.7_3class_ci:\n      - 0.593\n      - 0.611\n      delta_0.7train_binary_pp: -16.9\n      delta_0.7train_3class_pp: -31.1\n      delta_1.0train_binary_pp: 12\n      delta_1.0train_3class_pp: 2.8\n      asymmetric_transfer: true\n- exp_id: exp_049_temp_curve_t05\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 4708\n    skipped: 113\n    seeds: 995\n    model: pythia-2.8b\n    temperature: 0.5\n    top_p: 0.9\n    within_cv_binary_f1: 0.8432\n    within_cv_binary_ci:\n    - 0.8301\n    - 0.8558\n    logo_binary_f1: 0.8136\n    logo_binary_ci:\n    - 0.7984\n    - 0.8282\n    entropy_mean_rho: -0.5844\n- exp_id: exp_050_temp_curve_t09\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    records: 4536\n    model: pythia-2.8b\n    temperature: 0.9\n    top_p: 0.9\n    within_cv_binary_f1: 0.5821\n    within_cv_binary_ci:\n    - 0.5655\n    - 0.5985\n    logo_binary_f1: 0.4804\n    logo_binary_ci:\n    - 0.4645\n    - 0.4976\n    entropy_mean_rho: -0.3016\n    delta_vs_t07_cv: -0.157\n    delta_vs_t07_logo: -0.259\n- exp_id: exp_051_independent_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_to_olmo_binary_f1: 0.6945\n    pythia_to_olmo_ci:\n    - 0.6727\n    - 0.7167\n    olmo_to_pythia_binary_f1: 0.666\n    olmo_to_pythia_ci:\n    - 0.6429\n    - 0.6893\n    avg_binary_f1: 0.6803\n    shared_seed_logo_ref: 0.694\n    delta_vs_shared: -0.014\n- exp_id: exp_052_instruct_qwen3_1_7b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8753\n    within_binary_ci:\n    - 0.8667\n    - 0.8837\n    within_3class_f1: 0.7324\n    within_3class_ci:\n    - 0.7195\n    - 0.745\n    base_binary_f1: 0.8614\n    base_3class_f1: 0.769\n    logo_instruct_binary: 0.658\n    logo_instruct_3class: 0.543\n    logo_base_binary: 0.821\n    logo_base_3class: 0.802\n    gen1_f1_instruct: 0.438\n    gen1_f1_base: 0.579\n    spearman_direction: reversed (instruct ρ>0, base ρ<0)\n    delta_within_binary: 0.014\n    delta_within_3class: -0.037\n    delta_logo_binary: -0.163\n- exp_id: exp_053_instruct_olmo2_1b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8131\n    within_binary_ci:\n    - 0.8012\n    - 0.8251\n    within_3class_f1: 0.5748\n    within_3class_ci:\n    - 0.5605\n    - 0.5897\n    base_binary_f1: 0.8454\n    base_3class_f1: 0.7538\n    gen1_f1_instruct: 0.256\n    gen1_f1_base: 0.523\n    delta_within_binary: -0.032\n    delta_within_3class: -0.179\n    spearman_instruct:\n      entropy_mean: 0.482\n      entropy_std: 0.296\n      entropy_min: 0.08\n      entropy_max: 0.306\n      tail_decay: 0.228\n      ttr: 0.006\n      hapax_ratio: 0.025\n    spearman_base:\n      entropy_mean: -0.639\n      entropy_std: -0.296\n      entropy_min: -0.387\n      entropy_max: 0.067\n      tail_decay: -0.141\n      ttr: -0.7\n      hapax_ratio: -0.712\n    features_reversed: 6/7\n    model_used: allenai/OLMo-2-0425-1B-Instruct\n- exp_id: exp_054_instruct_llama3_2_3b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    instruct_binary_f1: 0.8381\n    instruct_binary_ci:\n    - 0.828\n    - 0.847\n    instruct_3class_f1: 0.5437\n    instruct_3class_ci:\n    - 0.53\n    - 0.558\n    base_binary_f1: 0.8488\n    base_3class_f1: 0.7424\n    rho_instruct_entropy_mean: 0.2299\n    rho_instruct_entropy_std: 0.2623\n    rho_instruct_entropy_min: -0.0027\n    rho_instruct_entropy_max: 0.2036\n    rho_instruct_tail_decay: 0.1198\n    rho_instruct_ttr: -0.1411\n    rho_instruct_hapax_ratio: -0.1157\n    rho_base_entropy_mean: -0.627\n    rho_base_ttr: -0.6856\n    rho_base_hapax_ratio: -0.6975\n    direction_reversals: 3\n    reversed_features:\n    - entropy_mean\n    - entropy_std\n    - tail_decay\n    data_count: 4974\n- exp_id: exp_055_qlora_olmo_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8881\n    macro_f1_3class_std: 0.0071\n    macro_f1_5class: 0.5976\n    macro_f1_5class_std: 0.0046\n    binary_f1: 0.8363\n    binary_f1_std: 0.0096\n    n_samples: 4429\n    runtime_seconds: 1689.7\n- exp_id: exp_056_qlora_qwen_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.9066\n    macro_f1_3class_std: 0.0082\n    macro_f1_5class: 0.5514\n    macro_f1_5class_std: 0.0031\n    binary_f1: 0.8672\n    binary_f1_std: 0.0137\n    n_samples: 4963\n    runtime_seconds: 1880.5\n- exp_id: exp_055b_qlora_olmo_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8588\n    macro_f1_3class_std: 0.0036\n    macro_f1_5class: 0.5398\n    macro_f1_5class_std: 0.015\n    binary_f1: 0.7925\n    binary_f1_std: 0.0097\n    n_samples: 2379\n    runtime_seconds: 911.7\n    note: completed before kill signal\n- exp_id: exp_056b_qlora_qwen_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.904\n    macro_f1_3class_std: 0.0094\n    macro_f1_5class: 0.5544\n    macro_f1_5class_std: 0.0068\n    binary_f1: 0.8597\n    binary_f1_std: 0.0123\n    n_samples: 2291\n    runtime_seconds: 880.9\n    note: completed before kill signal\n- exp_id: exp_057_scale_9gen_logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: superseded by exp_057 (rerun with fixed Gemma data)\n    first_run_3class_f1: 0.7516\n    first_run_binary_f1: 0.6842\n    see_exp_057_for_final: true\n- exp_id: exp_058_ddr_causality\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    permutation_baseline_f1: 0.7714\n    drifting_avg_importance: 0.1578\n    stationary_avg_importance: 0.0297\n    drifting_stationary_ratio: 5.31\n    granger_significant_features: 6/7\n    granger_max_delta_r2: 0.031\n    granger_max_delta_r2_feature: entropy_std\n    granger_nonsig_feature: entropy_min\n    granger_panel_n: 29095\n    intervention_max_f1_drop: 0.0203\n    intervention_max_feature: entropy_max\n    intervention_min_f1_drop: 0.0061\n- exp_id: exp_059_tost_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_bootstrap: 1000\n    seed: 42\n    margin_d: 0.2\n    entropy_max:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.062\n      d_ci:\n      - 0.037\n      - 0.088\n    entropy_min:\n      median_p: 0\n      rejection_rate: 1\n      median_d: -0.016\n      d_ci:\n      - -0.042\n      - 0.011\n    tail_decay:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.088\n      d_ci:\n      - 0.065\n      - 0.111\n    entropy_std:\n      median_p: 1\n      rejection_rate: 0\n      median_d: 0.458\n      d_ci:\n      - 0.435\n      - 0.479\n    stationary_features_robust: true\n- exp_id: exp_057\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    9gen_logo_3class_f1: 0.751\n    9gen_logo_binary_f1: 0.6661\n    8gen_baseline_3class_f1: 0.7698\n    delta_9gen_vs_8gen: -0.0188\n    n_total_rows: 42015\n    n_generators: 9\n    qwen3_8b_3class_f1: 0.6955\n    qwen3_8b_binary_f1: 0.6468\n    gemma_2_2b_3class_f1: 0.6279\n    gemma_2_2b_binary_f1: 0.4402\n    per_gen_3class_f1:\n      pythia-1b: 0.8571\n      qwen3-0.6b: 0.8185\n      pythia-2.8b: 0.8117\n      qwen3-1.7b: 0.8114\n      olmo-2-1b: 0.7732\n      llama-3.2-3b: 0.7591\n      qwen3-8b: 0.6955\n      gemma-2-2b: 0.6279\n      mistral-7b-v0.3: 0.6045\n    tail_decay_consistency: VERIFIED_all_9gen_logprob_slope\n    data_source: features_9gen.csv (42015 rows, Gemma fixed)\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T10:12:17.728Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T10:12:17.728Z",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-20T10:12:17.747Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：3.0 Solid Findings — 核心贡献被认可但有保留，1-2 个 reviewer 对 scope 或 novelty 有中等强度质疑，需要 rebuttal 中补充解释或微调 claims
核心假设：['DDR 被部分接受：审稿人认可 drifting features 的趋势，但质疑 shape feature 的 stationarity 是否只是 weak signal 而非 genuine invariance（entropy_std 的 TOST rejection rate=0 + d=0.458 被追问）', 'Base-model-only scope 被 1-2 个审稿人标记为 major limitation，要求讨论 instruct 场景下的 practical relevance', '0.694 F1 被认为 modest — 审稿人指出 per-gen range 0.633-0.724 的方差，质疑 worst-case (Mistral-7B 0.633) 的实用性', 'Negative downstream finding 被接受但审稿人要求更多 evidence（单一 perplexity metric + 3 seeds 被认为 limited）', 'Gemma-2-2B anomaly (gen-1 F1=0.036) 被追问：是方法失败还是 Gemma 特殊性？']
关键指标范围：{'expected_reviewer_avg': [3.0, 3.5], 'reviewer_spread': [2, 4], 'logo_binary_f1_perception': "0.694 被标注为 'modest' 或 'limited practical utility'", 'ddr_entropy_std_challenge': 'entropy_std (d=0.458, TOST rejection=0) 需要解释为何归入 stationary 组', 'instruct_scope_penalty': '-0.5 pp on one reviewer — 需要在 rebuttal 中论证 base-model scope 的合理性', 'gemma_anomaly_penalty': '-0.25 pp — 需要在 paper 中显式讨论'}
叙事方向：Claim 1 保持但在 abstract 中加入 per-gen range (0.633–0.724) 和 worst-case caveat。Claim 2 微调：将 entropy_std 从 stationary 组中移出或重新定义为 'intermediate'，DDR 从二分法调整为 spectrum（drifting → intermediate → stationary）。Claim 3 保持 negative framing 但承认 evidence 有限（3 seeds, 单 metric）。增加一段讨论：当前方法定位为 base-model provenance diagnostic，instruct 场景是 explicit future work。Rebuttal 重点回应 scope 和 Gemma anomaly。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-fingerprint
focus: Paper has been significantly expanded since last dream (May 14). New additions: (1) 9-generator scale evaluation with Gemma-2-2B (Appendix), (2) DDR causality analysis with permutation importance + Granger causality + feature intervention, (3) TOST bootstrap stability validation, (4) cross-model evaluation upgraded from sample-level CV to generator-level LOGO (binary F1=0.830). Total 33 pages, 20+ appendix experiments. Assess whether this is 3.0 Findings or 3.5 Borderline Conference level. Identify the single highest-impact improvement that could be made in 5 days before DDL.

## paper_framing.md

# Paper Framing — gen-depth-fingerprint

## Target Venue
- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标
- Positioning: **Findings paper**（非 main conference long paper）
- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)

## Core Insight
Non-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.

## Core Claims (3 条，均可证伪)

**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.

**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.

**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.

## Headline Metrics Summary

| Metric | Value | Context |
|--------|-------|---------|
| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |
| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |
| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |
| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |
| LOFO binary F1 | 0.686 | Leave-one-family-out |
| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |
| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |
| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |
| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |
| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |

## Scope & Limitations (必须在论文中突出)

1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.
2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).
3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.
4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).
5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.
6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).

## Story Spine

**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.

**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.

**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.

**Headline result template**: "On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization."

## Anticipated Reviewer Concerns

**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.

**RC2 — "Does this generalize beyond Pythia?"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.

**RC3 — "Is 3-class sufficient?"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.

**RC4 — "How realistic are single-model chains?"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.

**RC5 — "What about human editing?"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.

**RC6 — "Ecological validity?"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).

**RC8 — "Aren't these just OOD detection features?"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.

**RC9 — "Only base models — what about instruct?"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.

**RC10 — "Text length confound"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.

**RC11 — "Downstream — limited evidence"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.

## Contribution Positioning (Findings Level)
The contribution is **empirical and conceptual**, appropriate for Findings:
1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)
2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).
3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.

**Framing discipline:**
- Do NOT call the drift/stationarity split a "discovery" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.
- Do NOT use H1/H2 terminology. Use "drifting" vs "stationary" or "differential response."
- Do NOT overclaim "dual dynamics." Use "differential depth response" (DDR).
- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.
- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).
- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.

Related work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.

## Venue Fit
- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.


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
- id: plan_015
  claim: 1
  name: ordinal_baseline_comparison
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
  status: PREPARING
  conclusion: ''
  metrics: {}
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
    overall_logo_f1: 0.7879
    overall_ci95:
    - 0.783
    - 0.7929
    spearman_entropy_max: 0.0503
    spearman_entropy_min: -0.4061
    spearman_hapax: -0.6467
    spearman_ttr: -0.6302
    spearman_entropy_mean: -0.6098
    spearman_entropy_std: -0.1996
    spearman_tail_decay: -0.0403
- exp_id: plan-010-robustness
  name: ''
  status: DONE
  conclusion: success
  metrics:
    baseline_binary_f1: 0.695
    5pct_binary_f1: 0.65
    10pct_binary_f1: 0.614
    20pct_binary_f1: 0.591
    5pct_drop: -0.046
    10pct_drop: -0.081
    20pct_drop: -0.104
- exp_id: plan-010-llm-rephrase
  name: ''
  status: DONE
  conclusion: success
  metrics:
    original_binary_f1: 0.6918
    original_binary_ci:
    - 0.6749
    - 0.7067
    original_multiclass_f1: 0.7385
    original_multiclass_ci:
    - 0.7269
    - 0.7496
    rephrased_binary_f1: 0.6471
    rephrased_binary_ci:
    - 0.6308
    - 0.6619
    rephrased_multiclass_f1: 0.6672
    rephrased_multiclass_ci:
    - 0.6548
    - 0.6796
    binary_drop: -0.0447
    multiclass_drop: -0.0713
    edit_distance_ratio: 0.5071
    avg_sentences_replaced: 1.69
    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+
    bugs_fixed:
    - binary_task_gen1_vs_gen2+
    - 3class_mapping
    - tail_decay_rank100-1000
- exp_id: plan-008-seed-stratification
  name: ''
  status: DONE
  conclusion: success
  metrics:
    low_complexity_binary: 0.685
    medium_binary: 0.695
    high_complexity_binary: 0.695
    low_complexity_multi: 0.772
    medium_multi: 0.778
    high_complexity_multi: 0.779
    max_diff_binary_pp: 1.06
    max_diff_multiclass_pp: 0.68
    conclusion_label: seed_independent
- exp_id: multi-domain-seeds
  name: ''
  status: DONE
  conclusion: success
  metrics:
    news_binary_f1: 0.7459
    news_binary_ci:
    - 0.726
    - 0.764
    news_multiclass_f1: 0.6516
    academic_binary_f1: 0.7386
    academic_binary_ci:
    - 0.72
    - 0.757
    academic_multiclass_f1: 0.6223
    code_binary_f1: 0.7535
    code_binary_ci:
    - 0.737
    - 0.77
    code_multiclass_f1: 0.6344
    wikipedia_baseline_binary_f1: 0.8148
    wikipedia_baseline_multiclass_f1: 0.8632
    max_gap_vs_wiki_pp: 7.62
    worst_domain: academic
    best_domain: code
    conclusion_label: domain_independent
- exp_id: exp_047_multi_domain_t07
  name: ''
  status: DONE
  conclusion: success
  metrics:
    news_binary_f1: 0.7119
    news_binary_ci:
    - 0.6898
    - 0.7332
    news_3class_f1: 0.7149
    academic_binary_f1: 0.6279
    academic_binary_ci:
    - 0.6027
    - 0.6515
    academic_3class_f1: 0.6564
    code_binary_f1: 0.6872
    code_binary_ci:
    - 0.6641
    - 0.71
    code_3class_f1: 0.6729
    overall_binary_f1: 0.6757
    overall_3class_f1: 0.6814
    delta_vs_t10_news: -0.034
    delta_vs_t10_academic: -0.1107
    delta_vs_t10_code: -0.0663
- exp_id: multi_domain_t07
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_048_cross_temp_transfer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    6gen_logo:
      within_0.7_binary: 0.9471
      within_0.7_3class: 0.7888
      cross_0.7to1.0_binary: 0.9001
      cross_0.7to1.0_3class: 0.7225
      within_1.0_binary: 0.9107
      within_1.0_3class: 0.7257
      cross_1.0to0.7_binary: 0.9581
      cross_1.0to0.7_3class: 0.7913
      caveat: Only Qwen3-1.7B differs between conditions; 5/6 generators share data
    qwen_only:
      within_0.7_binary: 0.9262
      within_0.7_binary_ci:
      - 0.916
      - 0.935
      within_0.7_3class: 0.769
      within_0.7_3class_ci:
      - 0.756
      - 0.781
      cross_0.7to1.0_binary: 0.7574
      cross_0.7to1.0_binary_ci:
      - 0.745
      - 0.77
      cross_0.7to1.0_3class: 0.4581
      cross_0.7to1.0_3class_ci:
      - 0.445
      - 0.472
      within_1.0_binary: 0.8248
      within_1.0_binary_ci:
      - 0.81
      - 0.838
      within_1.0_3class: 0.5738
      within_1.0_3class_ci:
      - 0.56
      - 0.588
      cross_1.0to0.7_binary: 0.9443
      cross_1.0to0.7_binary_ci:
      - 0.936
      - 0.953
      cross_1.0to0.7_3class: 0.6014
      cross_1.0to0.7_3class_ci:
      - 0.593
      - 0.611
      delta_0.7train_binary_pp: -16.9
      delta_0.7train_3class_pp: -31.1
      delta_1.0train_binary_pp: 12
      delta_1.0train_3class_pp: 2.8
      asymmetric_transfer: true
- exp_id: exp_049_temp_curve_t05
  name: ''
  status: DONE
  conclusion: success
  metrics:
    records: 4708
    skipped: 113
    seeds: 995
    model: pythia-2.8b
    temperature: 0.5
    top_p: 0.9
    within_cv_binary_f1: 0.8432
    within_cv_binary_ci:
    - 0.8301
    - 0.8558
    logo_binary_f1: 0.8136
    logo_binary_ci:
    - 0.7984
    - 0.8282
    entropy_mean_rho: -0.5844
- exp_id: exp_050_temp_curve_t09
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    records: 4536
    model: pythia-2.8b
    temperature: 0.9
    top_p: 0.9
    within_cv_binary_f1: 0.5821
    within_cv_binary_ci:
    - 0.5655
    - 0.5985
    logo_binary_f1: 0.4804
    logo_binary_ci:
    - 0.4645
    - 0.4976
    entropy_mean_rho: -0.3016
    delta_vs_t07_cv: -0.157
    delta_vs_t07_logo: -0.259
- exp_id: exp_051_independent_seed
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pythia_to_olmo_binary_f1: 0.6945
    pythia_to_olmo_ci:
    - 0.6727
    - 0.7167
    olmo_to_pythia_binary_f1: 0.666
    olmo_to_pythia_ci:
    - 0.6429
    - 0.6893
    avg_binary_f1: 0.6803
    shared_seed_logo_ref: 0.694
    delta_vs_shared: -0.014
- exp_id: exp_052_instruct_qwen3_1_7b
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    within_binary_f1: 0.8753
    within_binary_ci:
    - 0.8667
    - 0.8837
    within_3class_f1: 0.7324
    within_3class_ci:
    - 0.7195
    - 0.745
    base_binary_f1: 0.8614
    base_3class_f1: 0.769
    logo_instruct_binary: 0.658
    logo_instruct_3class: 0.543
    logo_base_binary: 0.821
    logo_base_3class: 0.802
    gen1_f1_instruct: 0.438
    gen1_f1_base: 0.579
    spearman_direction: reversed (instruct ρ>0, base ρ<0)
    delta_within_binary: 0.014
    delta_within_3class: -0.037
    delta_logo_binary: -0.163
- exp_id: exp_053_instruct_olmo2_1b
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    within_binary_f1: 0.8131
    within_binary_ci:
    - 0.8012
    - 0.8251
    within_3class_f1: 0.5748
    within_3class_ci:
    - 0.5605
    - 0.5897
    base_binary_f1: 0.8454
    base_3class_f1: 0.7538
    gen1_f1_instruct: 0.256
    gen1_f1_base: 0.523
    delta_within_binary: -0.032
    delta_within_3class: -0.179
    spearman_instruct:
      entropy_mean: 0.482
      entropy_std: 0.296
      entropy_min: 0.08
      entropy_max: 0.306
      tail_decay: 0.228
      ttr: 0.006
      hapax_ratio: 0.025
    spearman_base:
      entropy_mean: -0.639
      entropy_std: -0.296
      entropy_min: -0.387
      entropy_max: 0.067
      tail_decay: -0.141
      ttr: -0.7
      hapax_ratio: -0.712
    features_reversed: 6/7
    model_used: allenai/OLMo-2-0425-1B-Instruct
- exp_id: exp_054_instruct_llama3_2_3b
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    instruct_binary_f1: 0.8381
    instruct_binary_ci:
    - 0.828
    - 0.847
    instruct_3class_f1: 0.5437
    instruct_3class_ci:
    - 0.53
    - 0.558
    base_binary_f1: 0.8488
    base_3class_f1: 0.7424
    rho_instruct_entropy_mean: 0.2299
    rho_instruct_entropy_std: 0.2623
    rho_instruct_entropy_min: -0.0027
    rho_instruct_entropy_max: 0.2036
    rho_instruct_tail_decay: 0.1198
    rho_instruct_ttr: -0.1411
    rho_instruct_hapax_ratio: -0.1157
    rho_base_entropy_mean: -0.627
    rho_base_ttr: -0.6856
    rho_base_hapax_ratio: -0.6975
    direction_reversals: 3
    reversed_features:
    - entropy_mean
    - entropy_std
    - tail_decay
    data_count: 4974
- exp_id: exp_055_qlora_olmo_instruct
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    macro_f1_3class: 0.8881
    macro_f1_3class_std: 0.0071
    macro_f1_5class: 0.5976
    macro_f1_5class_std: 0.0046
    binary_f1: 0.8363
    binary_f1_std: 0.0096
    n_samples: 4429
    runtime_seconds: 1689.7
- exp_id: exp_056_qlora_qwen_instruct
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    macro_f1_3class: 0.9066
    macro_f1_3class_std: 0.0082
    macro_f1_5class: 0.5514
    macro_f1_5class_std: 0.0031
    binary_f1: 0.8672
    binary_f1_std: 0.0137
    n_samples: 4963
    runtime_seconds: 1880.5
- exp_id: exp_055b_qlora_olmo_base
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    macro_f1_3class: 0.8588
    macro_f1_3class_std: 0.0036
    macro_f1_5class: 0.5398
    macro_f1_5class_std: 0.015
    binary_f1: 0.7925
    binary_f1_std: 0.0097
    n_samples: 2379
    runtime_seconds: 911.7
    note: completed before kill signal
- exp_id: exp_056b_qlora_qwen_base
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    macro_f1_3class: 0.904
    macro_f1_3class_std: 0.0094
    macro_f1_5class: 0.5544
    macro_f1_5class_std: 0.0068
    binary_f1: 0.8597
    binary_f1_std: 0.0123
    n_samples: 2291
    runtime_seconds: 880.9
    note: completed before kill signal
- exp_id: exp_057_scale_9gen_logo
  name: ''
  status: DONE
  conclusion: success
  metrics:
    note: superseded by exp_057 (rerun with fixed Gemma data)
    first_run_3class_f1: 0.7516
    first_run_binary_f1: 0.6842
    see_exp_057_for_final: true
- exp_id: exp_058_ddr_causality
  name: ''
  status: DONE
  conclusion: success
  metrics:
    permutation_baseline_f1: 0.7714
    drifting_avg_importance: 0.1578
    stationary_avg_importance: 0.0297
    drifting_stationary_ratio: 5.31
    granger_significant_features: 6/7
    granger_max_delta_r2: 0.031
    granger_max_delta_r2_feature: entropy_std
    granger_nonsig_feature: entropy_min
    granger_panel_n: 29095
    intervention_max_f1_drop: 0.0203
    intervention_max_feature: entropy_max
    intervention_min_f1_drop: 0.0061
- exp_id: exp_059_tost_bootstrap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_bootstrap: 1000
    seed: 42
    margin_d: 0.2
    entropy_max:
      median_p: 0
      rejection_rate: 1
      median_d: 0.062
      d_ci:
      - 0.037
      - 0.088
    entropy_min:
      median_p: 0
      rejection_rate: 1
      median_d: -0.016
      d_ci:
      - -0.042
      - 0.011
    tail_decay:
      median_p: 0
      rejection_rate: 1
      median_d: 0.088
      d_ci:
      - 0.065
      - 0.111
    entropy_std:
      median_p: 1
      rejection_rate: 0
      median_d: 0.458
      d_ci:
      - 0.435
      - 0.479
    stationary_features_robust: true
- exp_id: exp_057
  name: ''
  status: DONE
  conclusion: success
  metrics:
    9gen_logo_3class_f1: 0.751
    9gen_logo_binary_f1: 0.6661
    8gen_baseline_3class_f1: 0.7698
    delta_9gen_vs_8gen: -0.0188
    n_total_rows: 42015
    n_generators: 9
    qwen3_8b_3class_f1: 0.6955
    qwen3_8b_binary_f1: 0.6468
    gemma_2_2b_3class_f1: 0.6279
    gemma_2_2b_binary_f1: 0.4402
    per_gen_3class_f1:
      pythia-1b: 0.8571
      qwen3-0.6b: 0.8185
      pythia-2.8b: 0.8117
      qwen3-1.7b: 0.8114
      olmo-2-1b: 0.7732
      llama-3.2-3b: 0.7591
      qwen3-8b: 0.6955
      gemma-2-2b: 0.6279
      mistral-7b-v0.3: 0.6045
    tail_decay_consistency: VERIFIED_all_9gen_logprob_slope
    data_source: features_9gen.csv (42015 rows, Gemma fixed)

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
  "promptId": "b5a3667f-b994-475a-8a19-9e232394cd66",
  "type": "user",
  "uuid": "cb044e63-4c86-4349-b5c5-aedbf0872cfd",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T10:12:17.745Z_

```json
{
  "parentUuid": "cb044e63-4c86-4349-b5c5-aedbf0872cfd",
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
  "uuid": "53514ce9-0289-46da-9625-4d6340fe08ac",
  "timestamp": "2026-05-20T10:12:17.745Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T10:12:17.745Z_

```json
{
  "parentUuid": "53514ce9-0289-46da-9625-4d6340fe08ac",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2ac3ce61-f0c9-4c80-8496-ffc00126cd8a",
  "timestamp": "2026-05-20T10:12:17.745Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：3.0 Solid Findings — 核心贡献被认可但有保留，1-2 个 reviewer 对 scope 或 novelty 有中等强度质疑，需要 rebuttal 中补充解释或微调 claims 核心假设：['DDR 被部分接受：审稿人认可 drifting features 的趋势，但质疑 sh…",
  "leafUuid": "2ac3ce61-f0c9-4c80-8496-ffc00126cd8a",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Strengthen baseline comparison and instruct-model generalization",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed"
}
```

---

### Assistant

_source line 8 · 2026-05-20T10:12:22.647Z_

I'll analyze the experiment plan against the median tier definition and generate detailed predicted results. Let me first review the current state of experiments to understand what's already done vs. planned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ac3ce61-f0c9-4c80-8496-ffc00126cd8a",
  "isSidechain": false,
  "requestId": "req_011CbDeBXoXvmkkT3paBiUrL",
  "type": "assistant",
  "uuid": "73626da0-b10f-481b-8891-98ea51f69f80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wu4FJXLi3ZiJGE8v6gvqhG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24376,
      "cache_read_input_tokens": 11841,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 253,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24376
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

_source line 9 · 2026-05-20T10:12:26.720Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01EHVcYTTwthUMMhfHnA9he2`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan status",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_3, find all files related to experiment planning, registry, and results. I need to understand:\n1. Which experiments have status \"planned\" in the experiment_plan\n2. The full experiment_plan YAML or markdown file\n3. The registry YAML file with completed experiment statuses\n\nSearch for files like experiment_plan.yaml, registry.yaml, experiment_plan.md, or similar. Also check for any dream/ or phase1/ directories. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73626da0-b10f-481b-8891-98ea51f69f80",
  "isSidechain": false,
  "requestId": "req_011CbDeBXoXvmkkT3paBiUrL",
  "type": "assistant",
  "uuid": "1030308f-39b6-4f47-a1ec-1ca34919e049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wu4FJXLi3ZiJGE8v6gvqhG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24376,
      "cache_read_input_tokens": 11841,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 253,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24376
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

_source line 10 · 2026-05-20T10:13:39.656Z_

<details><summary>↩ Tool result · `toolu_01EHVcYTTwthUMMhfHnA9he2`</summary>

```text
Perfect! Now let me provide you with the final comprehensive findings:

## Summary: Experiment Planning, Registry & Results

I've completed a thorough exploration of the experiment planning and registry files in `/home/ubuntu/.agent-ml-research-idea_gen_0514_3`. Here are my findings:

### Key Finding: No "PLANNED" Status Experiments

**There are 0 experiments with status "PLANNED" or "PENDING"** in the formal sense. All 15 experiments defined in the experiment plan have already been executed:

- **49 experiments are DONE (76.6%)**
- **15 experiments are PREPARING (23.4%)**

### 1. Full Experiment Plan (experiment_plan.yaml)
**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`

All 15 planned experiments with their priorities:

**P0 (Must-run, 45.5 GPU·hours):**
- plan_001: feature_ablation_and_trend → DONE (macro F1: 0.8204)
- plan_002: cross_generator_evaluation → DONE (LOGO F1: 0.8037 across 5 generators)
- plan_003: cross_family_reference_model → DONE (F1: 0.8158 with Qwen ref)
- plan_004: downstream_utility → DONE (negative result on CLM fine-tuning)
- plan_013: text_length_control → DONE (weak confound, |ρ|<0.14)
- plan_015: ordinal_baseline_comparison → DONE (7-feature set > all single detectors)

**P1 (Important for completeness, 48 GPU·hours):**
- plan_005: prompt_type_comparison → DONE (continuation cv_f1: 0.82)
- plan_006: paraphrastic_comparison → Merged into plan_005 analysis
- plan_007: cross_model_chains → Covered in plan_005 variants
- plan_008: multi_domain_seeds → DONE (complexity-independent: F1 0.71-0.76)
- plan_014: large_scale_generator → DONE (Qwen3-8B: F1 0.6955 at 7B+ scale)

**P2 (Nice-to-have, 23 GPU·hours):**
- plan_009: finer_grained_ordinal → Not found as separate experiment
- plan_010: human_edit_robustness → DONE (robust to <5% editing)
- plan_011: ld_score_feature → Tested in plan_015
- plan_012: end_to_end_classifier → Not found as separate experiment

### 2. Complete Registry (registry.yaml)
**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml` (2,573 lines)

**Total: 64 experiments**
- **Directly mapped from plan:** 47 experiments (plan-001 through plan-015 + sub-tasks)
- **Extended analysis:** 13 experiments (exp_047 through exp_059)
- **Recent highlights:**
  - exp_057: 9-generator LOGO (F1: 0.751 with Qwen3-8B)
  - exp_058: DDR causality analysis (drifting features 5.3× more important)
  - exp_059: TOST bootstrap equivalence (robust shape features)

### 3. Experiments Currently PREPARING (In-Progress)

- **Infrastructure:** plan-001-restore, plan-004-prep, multi_domain_t07, review-exp-a-baseline-ensemble
- **QLora fine-tuning:** exp_052-exp_056b (Instruct model variants on 8 different models)

### 4. Key Results from Completed Experiments

1. **Feature Ablation (plan_001):** Reference (entropy) and surface (lexical) features are complementary with non-overlapping bootstrap CIs
2. **Cross-generator generalization (plan_002):** LOGO F1 0.8037 across 5 different generator families
3. **Reference model independence (plan_003):** OLMo and Qwen references achieve equal or better results than Pythia
4. **Ordinal baselines (plan_015):** Custom 7-feature set (F1 0.70-0.72) significantly outperforms all existing single detectors
5. **Large-scale robustness (plan_014/exp_057):** Depth signal persists at 7B+ scale but with reduced strength (ΔF1: -0.019)

### File Locations Summary

- **Experiment Plan:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`
- **Registry:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml`
- **Global Registry:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/global/registry.yaml`
- **Results Data:** `/root/gen-depth-fingerprint/data/features_*.csv` (on AutoDL server)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1030308f-39b6-4f47-a1ec-1ca34919e049",
  "isSidechain": false,
  "promptId": "b5a3667f-b994-475a-8a19-9e232394cd66",
  "type": "user",
  "uuid": "3cb64bb8-24a2-43c4-b6b6-e75739af4ba1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_3, find all files related to experiment planning, registry, and results. I need to understand:\n1. Which experiments have status \"planned\" in the experiment_plan\n2. The full experiment_plan YAML or markdown file\n3. The registry YAML file with completed experiment statuses\n\nSearch for files like experiment_plan.yaml, registry.yaml, experiment_plan.md, or similar. Also check for any dream/ or phase1/ directories. Search breadth: medium.",
    "agentId": "a023dd567ee0361da",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me provide you with the final comprehensive findings:\n\n## Summary: Experiment Planning, Registry & Results\n\nI've completed a thorough exploration of the experiment planning and registry files in `/home/ubuntu/.agent-ml-research-idea_gen_0514_3`. Here are my findings:\n\n### Key Finding: No \"PLANNED\" Status Experiments\n\n**There are 0 experiments with status \"PLANNED\" or \"PENDING\"** in the formal sense. All 15 experiments defined in the experiment plan have already been executed:\n\n- **49 experiments are DONE (76.6%)**\n- **15 experiments are PREPARING (23.4%)**\n\n### 1. Full Experiment Plan (experiment_plan.yaml)\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`\n\nAll 15 planned experiments with their priorities:\n\n**P0 (Must-run, 45.5 GPU·hours):**\n- plan_001: feature_ablation_and_trend → DONE (macro F1: 0.8204)\n- plan_002: cross_generator_evaluation → DONE (LOGO F1: 0.8037 across 5 generators)\n- plan_003: cross_family_reference_model → DONE (F1: 0.8158 with Qwen ref)\n- plan_004: downstream_utility → DONE (negative result on CLM fine-tuning)\n- plan_013: text_length_control → DONE (weak confound, |ρ|<0.14)\n- plan_015: ordinal_baseline_comparison → DONE (7-feature set > all single detectors)\n\n**P1 (Important for completeness, 48 GPU·hours):**\n- plan_005: prompt_type_comparison → DONE (continuation cv_f1: 0.82)\n- plan_006: paraphrastic_comparison → Merged into plan_005 analysis\n- plan_007: cross_model_chains → Covered in plan_005 variants\n- plan_008: multi_domain_seeds → DONE (complexity-independent: F1 0.71-0.76)\n- plan_014: large_scale_generator → DONE (Qwen3-8B: F1 0.6955 at 7B+ scale)\n\n**P2 (Nice-to-have, 23 GPU·hours):**\n- plan_009: finer_grained_ordinal → Not found as separate experiment\n- plan_010: human_edit_robustness → DONE (robust to <5% editing)\n- plan_011: ld_score_feature → Tested in plan_015\n- plan_012: end_to_end_classifier → Not found as separate experiment\n\n### 2. Complete Registry (registry.yaml)\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml` (2,573 lines)\n\n**Total: 64 experiments**\n- **Directly mapped from plan:** 47 experiments (plan-001 through plan-015 + sub-tasks)\n- **Extended analysis:** 13 experiments (exp_047 through exp_059)\n- **Recent highlights:**\n  - exp_057: 9-generator LOGO (F1: 0.751 with Qwen3-8B)\n  - exp_058: DDR causality analysis (drifting features 5.3× more important)\n  - exp_059: TOST bootstrap equivalence (robust shape features)\n\n### 3. Experiments Currently PREPARING (In-Progress)\n\n- **Infrastructure:** plan-001-restore, plan-004-prep, multi_domain_t07, review-exp-a-baseline-ensemble\n- **QLora fine-tuning:** exp_052-exp_056b (Instruct model variants on 8 different models)\n\n### 4. Key Results from Completed Experiments\n\n1. **Feature Ablation (plan_001):** Reference (entropy) and surface (lexical) features are complementary with non-overlapping bootstrap CIs\n2. **Cross-generator generalization (plan_002):** LOGO F1 0.8037 across 5 different generator families\n3. **Reference model independence (plan_003):** OLMo and Qwen references achieve equal or better results than Pythia\n4. **Ordinal baselines (plan_015):** Custom 7-feature set (F1 0.70-0.72) significantly outperforms all existing single detectors\n5. **Large-scale robustness (plan_014/exp_057):** Depth signal persists at 7B+ scale but with reduced strength (ΔF1: -0.019)\n\n### File Locations Summary\n\n- **Experiment Plan:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`\n- **Registry:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml`\n- **Global Registry:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/global/registry.yaml`\n- **Results Data:** `/root/gen-depth-fingerprint/data/features_*.csv` (on AutoDL server)"
      }
    ],
    "totalDurationMs": 72931,
    "totalTokens": 65074,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6741,
      "cache_read_input_tokens": 57047,
      "output_tokens": 1284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1284,
          "cache_read_input_tokens": 57047,
          "cache_creation_input_tokens": 6741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6741,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 5,
      "bashCount": 9,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "1030308f-39b6-4f47-a1ec-1ca34919e049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T10:13:42.592Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JBABgR5JWDcF8b4Yn7Xa9T`</summary>

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
  "parentUuid": "3cb64bb8-24a2-43c4-b6b6-e75739af4ba1",
  "isSidechain": false,
  "requestId": "req_011CbDeHZtiNrSiet6Tnn6Xq",
  "type": "assistant",
  "uuid": "c86e8aff-3992-4e7f-81a2-33df8abca8b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196T3khKxQznXs1CQCtaC4T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 36217,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1545,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 36217,
          "cache_creation_input_tokens": 1545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1545
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

_source line 12 · 2026-05-20T10:13:42.598Z_

<details><summary>↩ Tool result · `toolu_01JBABgR5JWDcF8b4Yn7Xa9T`</summary>

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
42	    description: >
43	      Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for feature extraction.
44	      Addresses RC2 + critical test of Claim 2: verify entropy_mean H2 drift persists
45	      with non-Pythia reference (if drift disappears → "dual dynamics" is reference-model artifact,
46	      not generation-intrinsic). Also verify shape features remain H1 across reference models.
47	    priority: P0
48	    gpu_budget_hours: 8
49	    deps: [plan_002]
50	    notes: >
51	      Importance elevated after D005: this is now the key falsification test for Claim 2's
52	      level/shape framework. If entropy_mean drift is Pythia-specific, the entire dual dynamics
53	      narrative collapses.
54	
55	  - id: plan_004
56	    claim: 3
57	    name: downstream_utility
58	    description: >
59	      RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)
60	      on depth-stratified data subsets. Measure perplexity degradation on held-out test
61	      set as function of training data depth. Compare depth-aware filtering vs binary
62	      baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with
63	      bootstrap CIs. Include sample-count-matched comparison (subsample depth-filtered
64	      to match binary-filtered count) to control for data size confound.
65	    priority: P0
66	    gpu_budget_hours: 20
67	    deps: [plan_002]
68	    notes: >
69	      Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,
70	      (3) data size confound. All three addressed in updated design.
71	
72	  # === P1: Important for story completeness ===
73	
74	  - id: plan_005
75	    claim: 1
76	    name: prompt_type_comparison
77	    description: >
78	      RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting chains.
79	      Tests whether semantic divergence from source correlates with depth signal preservation.
80	      Same 1000 seeds, Pythia-2.8B, 3 prompt types.
81	    priority: P1
82	    gpu_budget_hours: 10
83	    deps: [plan_001]
84	
85	  - id: plan_006
86	    claim: 1
87	    name: paraphrastic_comparison
88	    description: >
89	      RQ2 full: Construct parallel paraphrasing chains for direct comparison with continuation chains.
90	      Tests attractor convergence theory — do non-paraphrastic chains preserve more depth signal?
91	    priority: P1
92	    gpu_budget_hours: 8
93	    deps: [plan_005]
94	
95	  - id: plan_007
96	    claim: 1
97	    name: cross_model_chains
98	    description: >
99	      RQ3: Cross-model chains (different generator per depth step) vs single-model chains.
100	      More realistic scenario — web contamination involves diverse generators.
101	    priority: P1
102	    gpu_budget_hours: 12
103	    deps: [plan_002]
104	
105	  - id: plan_008
106	    claim: 1
107	    name: multi_domain_seeds
108	    description: >
109	      Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts),
110	      creative writing (WritingPrompts). 500 seeds per domain × 5 depths.
111	    priority: P1
112	    gpu_budget_hours: 10
113	    deps: [plan_002]
114	
115	  # === P2: Nice-to-have / strengthen claims ===
116	
117	  - id: plan_009
118	    claim: 1
119	    name: finer_grained_ordinal
120	    description: >
121	      Secondary analysis: 5-class ordinal classification (gen-0 through gen-4)
122	      on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.
123	    priority: P2
124	    gpu_budget_hours: 1
125	    deps: [plan_002]
126	
127	  - id: plan_010
128	    claim: 1
129	    name: human_edit_robustness
130	    description: >
131	      RC5: Robustness to simulated human edits.
132	      (A) Random word replacement (5%, 10%, 20%) as lower-bound.
133	      (B) LLM-simulated editing (light rephrasing of random sentences).
134	    priority: P2
135	    gpu_budget_hours: 5
136	    deps: [plan_002]
137	
138	  - id: plan_011
139	    claim: 2
140	    name: ld_score_feature
141	    description: >
142	      Add LD-Score (character-distribution signature from arXiv:2605.01647) as additional feature.
143	      Tests whether character-level features provide complementary depth signal.
144	    priority: P2
145	    gpu_budget_hours: 2
146	    deps: [plan_001]
147	
148	  - id: plan_012
149	    claim: 1
150	    name: end_to_end_classifier
151	    description: >
152	      QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.
153	      Compares learned representations vs handcrafted distributional features.
154	    priority: P2
155	    gpu_budget_hours: 15
156	    deps: [plan_002]
157	
158	  - id: plan_013
159	    claim: [1, 2]
160	    name: text_length_control
161	    description: >
162	      Address text length confound (RC10, dream all three tiers):
163	      (A) Analyze text length distributions by depth across all generators.
164	      (B) Compute length-normalized surface features (TTR, hapax_ratio on fixed-length windows).
165	      (C) Length-matched comparison: subsample to equalize length distributions across depths,
166	      re-evaluate classifier. If length-controlled F1 drops significantly → surface features
167	      were tracking length, not depth.
168	    priority: P0
169	    gpu_budget_hours: 0.5
170	    deps: [plan_002]
171	    notes: >
172	      Zero new generation — analysis on existing data. Critical confound control
173	      flagged by dream (all three tiers). Low cost, high impact on paper credibility.
174	
175	  - id: plan_014
176	    claim: 1
177	    name: large_scale_generator
178	    description: >
179	      Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth signal
180	      persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current
181	      generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).
182	    priority: P1
183	    gpu_budget_hours: 8
184	    deps: [plan_002]
185	    notes: >
186	      Dream review flagged ≤2.8B as major limitation (all three tiers).
187	      If depth signal weaker at scale → honest limitation with analysis.
188	      If comparable → strong generalization evidence for the paper.
189	
190	  - id: plan_015
191	    claim: 1
192	    name: ordinal_baseline_comparison
193	    description: >
194	      CRITICAL missing baseline (flagged by both re-dreams, all three tiers):
195	      Test whether existing detector continuous scores already provide ordinal depth signal.
196	      Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation depth.
197	      Compare single-feature ordinal classifiers (each detector score as sole feature) vs
198	      our 7-feature model. If existing detectors yield comparable ordinal signal, our
199	      custom feature set contribution collapses.
200	    priority: P0
201	    gpu_budget_hours: 3
202	    deps: [plan_002]
203	    notes: >
204	      Re-dream consensus: without this comparison, reviewers will question whether
205	      depth-specific features add value. Must be in the paper. FastDetectGPT needs
206	      model pair (source + reference), LD-Score is character-level, Binoculars needs
207	      two models. If any single detector achieves >0.70 ordinal F1, we need to
208	      reframe our contribution as "complementary to existing detectors" not "novel approach."
209	
210	# Global requirements (D006+D007):
211	# - ALL experiments must report bootstrap CIs on main metrics
212	# - Use individual-level Spearman ρ (not R² on aggregated means) for trend analysis
213	# - Report realistic performance range, not just best-case
214	
215	# GPU Budget Summary:
216	# P0: ~45.5 GPU·hours (was 44, +0.5 text_length, +5 downstream seeds)
217	# P1: ~48 GPU·hours (was 40, +8 large_scale_generator)
218	# P2: ~23 GPU·hours
219	# Total: ~116.5 GPU·hours (within 200 H100-hour budget)
220	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c86e8aff-3992-4e7f-81a2-33df8abca8b1",
  "isSidechain": false,
  "promptId": "b5a3667f-b994-475a-8a19-9e232394cd66",
  "type": "user",
  "uuid": "0290789f-a182-4d09-a9a2-45dcfb0008f4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml",
      "content": "experiments:\n  # === P0: Must-run experiments (headline results) ===\n\n  - id: plan_001\n    claim: 2\n    name: feature_ablation_and_trend\n    description: >\n      Three-part analysis on existing MVP data (zero new generation):\n      (A) Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n      vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold CV for each.\n      (B) H1/H2 trend analysis: plot each feature's mean ± std across depth 0-4. Monotonic trend → H2 (divergence);\n      plateau → H1 (convergence). Fit linear regression per feature, report slope + R².\n      (C) Perplexity pre-validation for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets\n      (no fine-tuning, just forward pass). If perplexity varies significantly with depth → Claim 3 signal exists.\n    priority: P0\n    gpu_budget_hours: 1\n    deps: [mvp-001]\n    notes: >\n      Uses existing MVP data + features.csv. Critical for Claim 2.\n      Plan B if surface-only ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n      narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n  - id: plan_002\n    claim: 1\n    name: cross_generator_evaluation\n    description: >\n      Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n      Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。)\n      Leave-one-generator-out CV to test cross-generator generalization.\n      1000 seeds × 5 generators × 5 depths = 25K chains.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [plan_001]\n    notes: >\n      Only proceed if plan_001 confirms reference features have independent or complementary value.\n      Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out evaluation in analysis.\n      Discuss limitation in paper if Pythia holdout performance inflated by Pythia-1B in training set.\n\n  - id: plan_003\n    claim: 2\n    name: cross_family_reference_model\n    description: >\n      Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for feature extraction.\n      Addresses RC2 + critical test of Claim 2: verify entropy_mean H2 drift persists\n      with non-Pythia reference (if drift disappears → \"dual dynamics\" is reference-model artifact,\n      not generation-intrinsic). Also verify shape features remain H1 across reference models.\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [plan_002]\n    notes: >\n      Importance elevated after D005: this is now the key falsification test for Claim 2's\n      level/shape framework. If entropy_mean drift is Pythia-specific, the entire dual dynamics\n      narrative collapses.\n\n  - id: plan_004\n    claim: 3\n    name: downstream_utility\n    description: >\n      RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n      on depth-stratified data subsets. Measure perplexity degradation on held-out test\n      set as function of training data depth. Compare depth-aware filtering vs binary\n      baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with\n      bootstrap CIs. Include sample-count-matched comparison (subsample depth-filtered\n      to match binary-filtered count) to control for data size confound.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [plan_002]\n    notes: >\n      Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n      (3) data size confound. All three addressed in updated design.\n\n  # === P1: Important for story completeness ===\n\n  - id: plan_005\n    claim: 1\n    name: prompt_type_comparison\n    description: >\n      RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting chains.\n      Tests whether semantic divergence from source correlates with depth signal preservation.\n      Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan_001]\n\n  - id: plan_006\n    claim: 1\n    name: paraphrastic_comparison\n    description: >\n      RQ2 full: Construct parallel paraphrasing chains for direct comparison with continuation chains.\n      Tests attractor convergence theory — do non-paraphrastic chains preserve more depth signal?\n    priority: P1\n    gpu_budget_hours: 8\n    deps: [plan_005]\n\n  - id: plan_007\n    claim: 1\n    name: cross_model_chains\n    description: >\n      RQ3: Cross-model chains (different generator per depth step) vs single-model chains.\n      More realistic scenario — web contamination involves diverse generators.\n    priority: P1\n    gpu_budget_hours: 12\n    deps: [plan_002]\n\n  - id: plan_008\n    claim: 1\n    name: multi_domain_seeds\n    description: >\n      Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts),\n      creative writing (WritingPrompts). 500 seeds per domain × 5 depths.\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan_002]\n\n  # === P2: Nice-to-have / strengthen claims ===\n\n  - id: plan_009\n    claim: 1\n    name: finer_grained_ordinal\n    description: >\n      Secondary analysis: 5-class ordinal classification (gen-0 through gen-4)\n      on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n    priority: P2\n    gpu_budget_hours: 1\n    deps: [plan_002]\n\n  - id: plan_010\n    claim: 1\n    name: human_edit_robustness\n    description: >\n      RC5: Robustness to simulated human edits.\n      (A) Random word replacement (5%, 10%, 20%) as lower-bound.\n      (B) LLM-simulated editing (light rephrasing of random sentences).\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [plan_002]\n\n  - id: plan_011\n    claim: 2\n    name: ld_score_feature\n    description: >\n      Add LD-Score (character-distribution signature from arXiv:2605.01647) as additional feature.\n      Tests whether character-level features provide complementary depth signal.\n    priority: P2\n    gpu_budget_hours: 2\n    deps: [plan_001]\n\n  - id: plan_012\n    claim: 1\n    name: end_to_end_classifier\n    description: >\n      QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n      Compares learned representations vs handcrafted distributional features.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [plan_002]\n\n  - id: plan_013\n    claim: [1, 2]\n    name: text_length_control\n    description: >\n      Address text length confound (RC10, dream all three tiers):\n      (A) Analyze text length distributions by depth across all generators.\n      (B) Compute length-normalized surface features (TTR, hapax_ratio on fixed-length windows).\n      (C) Length-matched comparison: subsample to equalize length distributions across depths,\n      re-evaluate classifier. If length-controlled F1 drops significantly → surface features\n      were tracking length, not depth.\n    priority: P0\n    gpu_budget_hours: 0.5\n    deps: [plan_002]\n    notes: >\n      Zero new generation — analysis on existing data. Critical confound control\n      flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n  - id: plan_014\n    claim: 1\n    name: large_scale_generator\n    description: >\n      Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth signal\n      persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n      generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n    priority: P1\n    gpu_budget_hours: 8\n    deps: [plan_002]\n    notes: >\n      Dream review flagged ≤2.8B as major limitation (all three tiers).\n      If depth signal weaker at scale → honest limitation with analysis.\n      If comparable → strong generalization evidence for the paper.\n\n  - id: plan_015\n    claim: 1\n    name: ordinal_baseline_comparison\n    description: >\n      CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n      Test whether existing detector continuous scores already provide ordinal depth signal.\n      Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation depth.\n      Compare single-feature ordinal classifiers (each detector score as sole feature) vs\n      our 7-feature model. If existing detectors yield comparable ordinal signal, our\n      custom feature set contribution collapses.\n    priority: P0\n    gpu_budget_hours: 3\n    deps: [plan_002]\n    notes: >\n      Re-dream consensus: without this comparison, reviewers will question whether\n      depth-specific features add value. Must be in the paper. FastDetectGPT needs\n      model pair (source + reference), LD-Score is character-level, Binoculars needs\n      two models. If any single detector achieves >0.70 ordinal F1, we need to\n      reframe our contribution as \"complementary to existing detectors\" not \"novel approach.\"\n\n# Global requirements (D006+D007):\n# - ALL experiments must report bootstrap CIs on main metrics\n# - Use individual-level Spearman ρ (not R² on aggregated means) for trend analysis\n# - Report realistic performance range, not just best-case\n\n# GPU Budget Summary:\n# P0: ~45.5 GPU·hours (was 44, +0.5 text_length, +5 downstream seeds)\n# P1: ~48 GPU·hours (was 40, +8 large_scale_generator)\n# P2: ~23 GPU·hours\n# Total: ~116.5 GPU·hours (within 200 H100-hour budget)\n",
      "numLines": 220,
      "startLine": 1,
      "totalLines": 220
    }
  },
  "sourceToolAssistantUUID": "c86e8aff-3992-4e7f-81a2-33df8abca8b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-20T10:13:42.681Z_

````json
{
  "parentUuid": "0290789f-a182-4d09-a9a2-45dcfb0008f4",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**gen-depth-fingerprint**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"gen-depth-fingerprint\")` 或 `load_project_config(\"gen-depth-fingerprint\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[项目]** overall framework参考已发表EMNLP论文的风格，图中的信息密度要高，视觉美观，高度浓缩method部分信息\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/gen-depth-fingerprint/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "88feab15-d738-4e7e-9fd9-f878100d9def",
  "timestamp": "2026-05-20T10:13:42.681Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：3.0 Solid Findings — 核心贡献被认可但有保留，1-2 个 reviewer 对 scope 或 novelty 有中等强度质疑，需要 rebuttal 中补充解释或微调 claims 核心假设：['DDR 被部分接受：审稿人认可 drifting features 的趋势，但质疑 sh…",
  "leafUuid": "88feab15-d738-4e7e-9fd9-f878100d9def",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Strengthen baseline comparison and instruct-model generalization",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed"
}
```

---

### Assistant

_source line 16 · 2026-05-20T10:14:08.537Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of all planned experiments and the registry of completed experiments. Let me map out which experiments are "planned" status vs already done, and generate detailed predicted data for each planned experiment under the median tier (3.0 Solid Findings).

Looking at the experiment_plan, ALL experiments have `status: planned`. But many have already been executed based on the registry. Let me identify which ones in the experiment_plan still show `status: planned` and generate predictions for ALL of them, since the user asked me to generate detailed data for every planned experiment.

Let me carefully go through each experiment plan and generate predictions calibrated to the median tier definition.


Now I'm calibrating the predictions to the median tier characteristics: reviewer averages between 3.0 and 3.5 with a spread of 2 to 4, binary F1 around 0.694 indicating modest practical utility, and specific penalty adjustments for entropy_std, instruction scope, and Gemma anomalies. I'll structure the narrative to keep the main claim but add per-generation ranges and worst-case scenarios.

For the experimental predictions, I need to map each planned experiment against these baseline metrics—feature ablation and trend analysis should show modest improvements, cross-generator evaluation will likely reveal the Gemma penalty pattern, and the downstream utility test will be critical for justifying the "limited practical utility" framing. The remaining experiments on prompt types, paraphrastic comparison, model chains, multi-domain seeds, and finer-grained ordinals will each contribute evidence to either support or challenge the intermediate positioning of entropy_std.

Human edit robustness, LD score features, the end-to-end classifier, text length control, large-scale generation, and ordinal baseline comparison will round out the picture—some showing expected degradation under perturbation, others revealing where the approach holds up better than anticipated. I'm structuring the YAML to calibrate each result toward the median tier: solid but with acknowledged limitations that reviewers can point to.

Generating YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88feab15-d738-4e7e-9fd9-f878100d9def",
  "isSidechain": false,
  "requestId": "req_011CbDeHnp6PvYghYLo33Bzx",
  "type": "assistant",
  "uuid": "938141a3-f6f9-416f-a33b-5862af898ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWw3SG6piii5DmLiq9VKFV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8830,
      "cache_read_input_tokens": 37762,
      "output_tokens": 24585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 24585,
          "cache_read_input_tokens": 37762,
          "cache_creation_input_tokens": 8830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8830
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

_source line 17 · 2026-05-20T10:21:21.814Z_

Now I have full context. Let me generate the detailed predicted data for all 15 planned experiments under the median tier.

```yaml
tier: median
narrative_guidance: >
  3.0 Solid Findings 档位下，核心贡献（DDR + 深度分类 task formulation）被审稿人认可，
  但在 scope（base-model only）、novelty（是否只是 vocabulary impoverishment 的衍生）、
  practical utility（0.694 F1 + per-gen 0.633-0.724 的方差）上受到中等强度质疑。
  Claim 2 的 entropy_std 归类问题被追问；Gemma-2-2B anomaly 被要求显式讨论。
  Rebuttal 需回应 2-3 个 medium-severity concerns，但无 fatal flaw。
  整体定位：有价值的 empirical contribution，Findings 可接收，但不够 main conference。

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      在 MVP 数据上做三部分分析：(A) 特征消融（full vs reference-only vs surface-only），
      (B) H1/H2 趋势分析（每个特征跨 depth 的 Spearman ρ + KS），
      (C) perplexity 预验证（Pythia-410M forward pass on depth-stratified subsets）。
    expected_results:
      full_macro_f1: 0.820
      full_macro_f1_ci: [0.805, 0.835]
      reference_only_f1: 0.719
      reference_only_ci: [0.706, 0.733]
      surface_only_f1: 0.763
      surface_only_ci: [0.747, 0.774]
      mcnemar_full_vs_surface_p: 0.0
      mcnemar_full_vs_ref_p: 0.0
      h2_features: [entropy_mean, ttr, hapax_ratio]
      h2_spearman_entropy_mean: -0.60
      h2_spearman_ttr: -0.61
      h2_spearman_hapax_ratio: -0.63
      h1_features: [tail_decay, entropy_max, entropy_min]
      h1_spearman_tail_decay: 0.04
      h1_spearman_entropy_max: 0.05
      h1_spearman_entropy_min: -0.30
      contested_feature: entropy_std
      entropy_std_spearman: -0.20
      entropy_std_ks: 0.15
      median_ppl_by_depth: [13.50, 4.96, 3.00, 2.07, 1.72]
      ppl_depth_trend: monotonic_decrease
    result_rationale: >
      Median 档下，消融结果清晰显示 reference 和 surface 特征互补（McNemar p≈0），
      但 surface-only (0.763) 已接近 full (0.820)，给审稿人留下 "reference 特征
      边际贡献有限" 的印象。H2 趋势在 entropy_mean/ttr/hapax 上非常强（|ρ|>0.60），
      但 entropy_std (ρ=-0.20) 处于 drifting 和 stationary 之间的灰色地带——
      它的 KS 值 (0.15) 远高于 tail_decay (0.05) 但远低于 hapax (0.54)，
      导致二分法（drifting vs stationary）在这个特征上站不住脚。
      审稿人会追问为何把 entropy_std 归入 stationary 组（后续 TOST 的 d=0.458 
      进一步加剧此问题）。Perplexity 随 depth 单调下降（13.50→1.72）证实 
      depth signal 存在，但也暴露 gen-0 ppl 异常高（seed text 质量差异），
      需要在 paper 中解释。
    tables:
      - name: "Table: Feature Ablation (5-fold CV on MVP data)"
        columns: [Feature_Set, Macro_F1, 95%_CI, N_Features]
        rows:
          - [Full (7-feature), 0.820, "[0.805, 0.835]", 7]
          - [Surface-only (TTR + hapax), 0.763, "[0.747, 0.774]", 2]
          - [Reference-only (entropy + tail), 0.719, "[0.706, 0.733]", 5]
      - name: "Table: Feature Trend Classification"
        columns: [Feature, Spearman_ρ, KS_stat, Trend_Class]
        rows:
          - [hapax_ratio, -0.63, 0.537, Drifting]
          - [ttr, -0.61, 0.521, Drifting]
          - [entropy_mean, -0.60, 0.516, Drifting]
          - [entropy_min, -0.30, 0.28, Intermediate]
          - [entropy_std, -0.20, 0.15, "Contested (d=0.458)"]
          - [entropy_max, 0.05, 0.052, Stationary]
          - [tail_decay, 0.04, 0.043, Stationary]
    figures_description:
      - "7-panel feature trend plot: mean±std per feature across depth 0-4. 左三列 (hapax, ttr, entropy_mean) 呈明显单调下降；右二列 (entropy_max, tail_decay) 几乎水平；entropy_std 和 entropy_min 处于中间状态，趋势可见但幅度小。"
      - "Perplexity by depth bar chart: 13.50 → 4.96 → 3.00 → 2.07 → 1.72，Y轴对数刻度。"
    analysis: >
      核心发现成立但有裂缝。Surface-only 0.763 vs full 0.820 的 gap 只有 5.7pp，
      审稿人可能认为 "complementary signal" 的 framing 对 reference features 的
      marginal contribution 过度包装。entropy_std 的 contested 状态是最大叙事风险——
      原始 H1/H2 二分法需要调整为 spectrum（drifting → intermediate → stationary），
      在 paper abstract 中不能回避。

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      扩展至 5 个生成器 (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)，
      LOGO CV 评估跨生成器泛化能力。
    expected_results:
      total_records: 23032
      generators: [pythia-2.8b, pythia-1b, olmo-2-1b, qwen3-1.7b, qwen3-0.6b]
      logo_avg_macro_f1: 0.804
      logo_avg_macro_f1_ci: [0.786, 0.799]
      logo_binary_f1: 0.694
      logo_binary_f1_ci: [0.688, 0.700]
      per_gen_binary_f1:
        pythia-2.8b: 0.724
        pythia-1b: 0.718
        olmo-2-1b: 0.668
        qwen3-1.7b: 0.702
        qwen3-0.6b: 0.659
      per_gen_macro_f1:
        pythia-2.8b: 0.851
        pythia-1b: 0.831
        olmo-2-1b: 0.752
        qwen3-1.7b: 0.805
        qwen3-0.6b: 0.780
      lofo_binary_f1: 0.686
      lofo_macro_f1: 0.791
      worst_case_generator: qwen3-0.6b
      best_case_generator: pythia-2.8b
      per_gen_binary_range: [0.659, 0.724]
      binary_f1_std_across_gens: 0.028
      top_features_importance: [hapax_ratio_0.289, ttr_0.168, entropy_mean_0.160]
    result_rationale: >
      Median 档下，LOGO 跨生成器平均 macro F1 达到 0.804（solid），但 binary F1 
      只有 0.694——这个数字成为审稿人 "modest performance" 评价的核心锚点。
      Per-gen binary F1 从 0.659 (Qwen3-0.6B) 到 0.724 (Pythia-2.8B) 的 6.5pp 
      spread 说明方法对生成器敏感。两个 Pythia 模型 (2.8B: 0.724, 1B: 0.718) 
      都偏高，暗示 Pythia 家族内部信息泄露可能膨胀了 LOGO 的平均值——
      LOFO (0.686) 比 LOGO (0.694) 低 0.8pp 证实了这一点但差距不大。
      OLMo-2-1B 和 Qwen3-0.6B 作为 held-out 时 F1 较低，表明跨架构泛化 
      存在 gap。审稿人不会认为这是 failure，但会标注为 "moderate generalization"。
    tables:
      - name: "Table: LOGO Per-Generator Results"
        columns: [Generator, Family, Params, Binary_F1, Macro_F1, 95%_CI_Binary]
        rows:
          - [Pythia-2.8B, Pythia, 2.8B, 0.724, 0.851, "[0.710, 0.738]"]
          - [Pythia-1B, Pythia, 1B, 0.718, 0.831, "[0.703, 0.733]"]
          - [Qwen3-1.7B, Qwen, 1.7B, 0.702, 0.805, "[0.687, 0.717]"]
          - [OLMo-2-1B, OLMo, 1.5B, 0.668, 0.752, "[0.652, 0.684]"]
          - [Qwen3-0.6B, Qwen, 0.6B, 0.659, 0.780, "[0.643, 0.675]"]
          - ["**Average**", "—", "—", "**0.694**", "**0.804**", "[0.688, 0.700]"]
      - name: "Table: LOFO vs LOGO Comparison"
        columns: [Eval_Protocol, Binary_F1, Macro_F1]
        rows:
          - [LOGO (leave-one-generator-out), 0.694, 0.804]
          - [LOFO (leave-one-family-out), 0.686, 0.791]
          - [Δ, -0.008, -0.013]
    figures_description:
      - "Per-generator binary F1 bar chart with CI whiskers, generators sorted by F1. Pythia 家族两个 bar 并列最高，视觉上立即引起 family leakage 质疑。"
      - "Confusion matrix heatmap (3×3) for LOGO average: gen-0 near-perfect, gen-1/gen-2+ 混淆严重（86% binary errors as FN）。"
    analysis: >
      LOGO binary F1=0.694 是 paper 的 headline metric，在 median 档下被审稿人
      标注为 "modest"。Per-gen range 0.659-0.724 的 variance 是一个 moderate concern：
      worst-case (Qwen3-0.6B at 0.659) 的实用性被质疑。Pythia 家族两个模型都偏高
      增加了 family leakage 的可信度问题，但 LOFO (0.686) 与 LOGO (0.694) 
      差距仅 0.8pp，可在 rebuttal 中论证 leakage 影响有限。

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      用 OLMo-2-1B 和 Qwen3-0.6B 作为替代 reference model（取代 Pythia-410M），
      验证 DDR 趋势是否为 generation-intrinsic 而非 reference-model artifact。
    expected_results:
      logo_f1_pythia_ref: 0.803
      logo_f1_olmo_ref: 0.807
      logo_f1_qwen_ref: 0.816
      entropy_drift_all_refs_negative: true
      pythia_ref_drift_range: [-1.19, -1.40]
      olmo_ref_drift_range: [-0.61, -0.91]
      qwen_ref_drift_range: [-0.96, -1.35]
      dual_dynamics_is_pythia_artifact: false
      shape_features_stationary_all_refs: true
      tail_decay_cross_ref_ks_max: 0.06
      entropy_std_cross_ref_inconsistency: true
      entropy_std_d_pythia: 0.458
      entropy_std_d_olmo: 0.31
      entropy_std_d_qwen: 0.52
    result_rationale: >
      Median 档的关键 falsification test 通过：DDR 趋势在三个不同 reference model 
      下均成立（drift 方向一致为负），排除了 Pythia-specific artifact 假说。
      这是 Claim 2 的核心支撑，审稿人会认可。但细节上，drift 幅度差异大
      （OLMo ref drift 仅 -0.61 到 -0.91，约为 Pythia ref 的一半），
      说明 reference model 选择影响 signal 强度——审稿人会要求讨论。
      entropy_std 的跨 reference 不一致性（d 从 0.31 到 0.52）进一步
      削弱了它的 "stationary" 归类，支持将其移入 "intermediate" 类别。
      Qwen ref 略微优于 Pythia ref（0.816 vs 0.803），暗示小模型 reference 
      不一定最优，但差异在 CI 重叠范围内。
    tables:
      - name: "Table: Cross-Reference-Model LOGO F1"
        columns: [Reference_Model, Params, LOGO_Macro_F1, entropy_mean_ρ, tail_decay_ρ]
        rows:
          - [Pythia-410M, 410M, 0.803, -0.60, 0.04]
          - [OLMo-2-1B, 1.5B, 0.807, -0.52, 0.06]
          - [Qwen3-0.6B, 0.6B, 0.816, -0.58, 0.03]
      - name: "Table: entropy_std Cohen's d Across Reference Models"
        columns: [Reference_Model, entropy_std_d, TOST_rejection, Classification]
        rows:
          - [Pythia-410M, 0.458, 0/1000, "Contested"]
          - [OLMo-2-1B, 0.31, "partial", "Borderline stationary"]
          - [Qwen3-0.6B, 0.52, 0/1000, "Contested"]
    figures_description:
      - "3×7 heatmap: rows=reference models, columns=features, cells=Spearman ρ. Drifting 区域（左3列）一致为深蓝（负），Stationary 区域（右2列）一致为白/浅色，entropy_std 列颜色不一致（中等深度蓝）。"
    analysis: >
      DDR 的 generation-intrinsic 属性得到验证，这是 median 档下最强的子结果。
      但 reference model 选择对 drift magnitude 的影响（最大 2× 差异）是审稿人
      可能追问的 nuance——需要在 paper 中透明报告。entropy_std 跨 reference 
      不一致性为将其重新归类为 "intermediate" 提供了额外证据。

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune OLMo-1B on depth-stratified subsets (all / depth0-1 / size-matched / 
      binary-filtered / depth0-only)，3 seeds with bootstrap CIs，测量 perplexity 差异。
    expected_results:
      total_runs: 15
      variants:
        all:
          train_n: 12299
          ppl_mean: 2.335
          ppl_std: 0.0003
        size_matched:
          train_n: 3951
          ppl_mean: 2.367
          ppl_std: 0.0002
        depth01:
          train_n: 3951
          ppl_mean: 2.387
          ppl_std: 0.001
        binary_filtered:
          train_n: 3951
          ppl_mean: 2.389
          ppl_std: 0.001
        depth0_only:
          train_n: 797
          ppl_mean: 2.681
          ppl_std: 0.001
      ranking: "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)"
      tost_equal_count_p: 0.00011
      tost_equal_count_margin: "±2%"
      tost_all_vs_filtered_p: 0.15
      tost_all_vs_filtered_margin: "±2%"
      tost_all_vs_filtered_margin_3pct_p: 0.003
      cohens_d_size_matched_vs_depth01: 0.85
      seed_variance: "<0.002 ppl across seeds"
      negative_finding_confirmed: true
    result_rationale: >
      Median 档下 Claim 3 的 negative finding 成立但 evidence 被认为 limited。
      核心结果：等样本量下 size_matched (2.367) vs depth01 (2.387) 差异仅 0.020 ppl，
      TOST 在 ±2% margin 下确认 equivalence (p=1.1e-4)。但审稿人会质疑：
      (1) 只有 3 seeds——seed variance 极小 (<0.002) 说明 variance 来源不在 seed 
      而在 data composition，但 3 seeds 仍显 underpowered。
      (2) 单一 metric (perplexity)——不涵盖 downstream task performance、
      toxicity、factuality 等维度。
      (3) all (12299) vs filtered (3951) 的 TOST 需要放宽到 ±3% 才 reject，
      说明 data quantity 效应存在但被标注为 "modest"。
      depth0_only (2.681) 显著差于其他——符合预期（只有 797 samples + 只有 seed text），
      反而支持 "更多 synthetic data 不 hurt" 的叙事。
    tables:
      - name: "Table: Downstream CLM Perplexity by Training Data Composition"
        columns: [Variant, Train_N, Ppl_Mean, Ppl_Std, Δ_vs_SizeMatched]
        rows:
          - [All depths, 12299, 2.335, 0.0003, "-0.032 (more data)"]
          - [Size-matched random, 3951, 2.367, 0.0002, "—(baseline)"]
          - [Depth 0+1 only, 3951, 2.387, 0.001, "+0.020"]
          - [Binary-filtered, 3951, 2.389, 0.001, "+0.022"]
          - [Depth 0 only, 797, 2.681, 0.001, "+0.314"]
      - name: "Table: TOST Equivalence Tests"
        columns: [Comparison, Margin, p_value, Equivalent]
        rows:
          - [size_matched vs depth01, "±2%", 1.1e-4, Yes]
          - [size_matched vs binary_filtered, "±2%", 8.3e-5, Yes]
          - [all vs size_matched, "±2%", 0.15, No]
          - [all vs size_matched, "±3%", 0.003, Yes]
    figures_description:
      - "Bar chart: 5 variants, Y-axis perplexity, with 3-seed error bars (barely visible due to tiny variance). depth0_only 明显高出，其余四个视觉上几乎等高。"
    analysis: >
      Negative finding 成立且叙事清晰：depth fingerprinting 是 diagnostic 工具，
      不是 curative 工具。但 3 seeds + single metric 是审稿人的合理质疑点——
      在 median 档下不会导致 reject 但会在 review 中被标记为 "limited evidence"，
      需要在 rebuttal 中承认并论证 seed variance 极小说明更多 seeds 不会改变结论。

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      对比 continuation / elaboration / inspired_rewriting 三种 prompt 类型的
      depth signal 保留度和分类性能。Pythia-2.8B, 1000 seeds。
    expected_results:
      cv_f1:
        continuation: 0.781
        elaboration: 0.730
        inspired_rewriting: 0.737
      lopto_f1:
        held_out_continuation: 0.762
        held_out_elaboration: 0.762
        held_out_rewriting: 0.733
        avg: 0.753
      depth_retention_d4_d0:
        continuation: 0.831
        elaboration: 0.986
        inspired_rewriting: 0.939
      drift_hapax_ratio:
        continuation: -0.74
        elaboration: -0.83
        rewriting: -0.80
      drift_entropy_mean:
        continuation: -0.56
        elaboration: -0.47
        rewriting: -0.48
      semantic_divergence_ranking: "continuation > rewriting > elaboration"
      f1_ranking: "continuation > rewriting > elaboration"
    result_rationale: >
      Median 档下，三种 prompt 类型均表现出 DDR 趋势，但强度和模式不同。
      Continuation (F1=0.781) 最高，因为语义发散最大（每一步生成新内容而非
      紧扣原文），distributional shift 更剧烈。Elaboration (F1=0.730) 最低，
      因为 elaboration 保持话题一致性（retention 0.986），distributional features 
      变化较缓。这个排序符合直觉但也暴露问题：审稿人会问 "如果 continuation 
      vs elaboration 差 5pp，那 real-world 混合 prompt 场景下性能如何？"
      Paper 需要报告 cross-prompt-type transfer（lopto），avg 0.753 表明
      prompt-type 泛化合理但非完美。审稿人不会在这个实验上深入追问——
      它是 supporting evidence，不是 core claim。
    tables:
      - name: "Table: Prompt Type Comparison"
        columns: [Prompt_Type, CV_F1, LOPTO_F1, Depth_Retention, hapax_ρ, entropy_mean_ρ]
        rows:
          - [Continuation, 0.781, 0.762, 0.831, -0.74, -0.56]
          - [Inspired rewriting, 0.737, 0.733, 0.939, -0.80, -0.48]
          - [Elaboration, 0.730, 0.762, 0.986, -0.83, -0.47]
    figures_description:
      - "3-panel feature drift plot: 每个 prompt type 一列，7 features 跨 depth 的趋势线。Continuation 的 entropy_mean 曲线斜率最陡，elaboration 最平缓。"
    analysis: >
      Prompt type 对 depth signal 有系统性影响（continuation > rewriting > elaboration），
      且影响方向与语义发散度一致。这支持 DDR 的 mechanistic interpretation：
      更大的语义偏移→更强的 distributional shift→更易分类。但 elaboration 的
      hapax drift (-0.83) 反而比 continuation (-0.74) 更强，说明 lexical 
      impoverishment 和 distributional shift 不完全共线——这是一个 subtle finding，
      在 median 档下审稿人可能注意到但不会深究。

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      构建 paraphrastic chains 与 continuation chains 做直接对比，
      测试 attractor convergence theory（paraphrasing 是否更快收敛）。
    expected_results:
      paraphrastic_cv_f1: 0.62
      paraphrastic_ci: [0.60, 0.64]
      continuation_cv_f1: 0.781
      continuation_ci: [0.765, 0.797]
      delta_pp: -16.1
      paraphrastic_depth_retention_d4_d0: 0.97
      paraphrastic_hapax_drift: -0.35
      paraphrastic_entropy_mean_drift: -0.22
      attractor_effect_observed: true
      binary_f1_paraphrastic: 0.55
      binary_f1_continuation: 0.694
    result_rationale: >
      Median 档下，paraphrastic chains 的 depth signal 显著弱于 continuation chains
      （F1 0.62 vs 0.781, -16pp），符合 attractor convergence theory 预测：
      paraphrasing 保持语义不变，distributional features 快速收敛到 attractor，
      深度间差异被压缩。hapax drift 仅 -0.35（vs continuation -0.74），
      entropy_mean drift 仅 -0.22（vs -0.56）。这验证了 paper 的核心 scope claim：
      方法针对 non-paraphrastic chains，paraphrastic 场景需要不同方法。
      审稿人会认为这是 expected result（不加分也不扣分），但写入 paper 
      有助于 position scope boundary。Binary F1 只有 0.55 进一步说明
      gen-1/gen-2+ 在 paraphrastic 链中几乎不可区分。
    tables:
      - name: "Table: Paraphrastic vs Non-Paraphrastic Chains"
        columns: [Chain_Type, CV_F1, Binary_F1, hapax_ρ, entropy_mean_ρ, Retention_d4]
        rows:
          - [Continuation, 0.781, 0.694, -0.74, -0.56, 0.831]
          - [Paraphrastic, 0.620, 0.550, -0.35, -0.22, 0.970]
          - [Δ, -0.161, -0.144, "+0.39 (weaker)", "+0.34 (weaker)", "+0.139"]
    figures_description:
      - "Paired feature drift comparison: 7 features × 2 chain types. Continuation 的趋势线陡峭，paraphrastic 几乎水平。右侧 annotation 标注 attractor convergence zone。"
    analysis: >
      结果清晰支持 scope boundary：本方法不适用于 paraphrastic chains。
      这对论文定位有利（honest scoping），但也意味着方法的实用场景被进一步缩窄——
      在 median 档下，审稿人会在 "practical relevance" 维度扣 0.25-0.5pp。

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains：每个 depth step 用不同生成器，模拟 real-world 
      web contamination（多源 LLM 混合）。
    expected_results:
      cross_model_binary_f1: 0.830
      cross_model_binary_ci: [0.815, 0.845]
      cross_model_3class_f1: 0.789
      cross_model_3class_ci: [0.775, 0.803]
      single_model_binary_f1_ref: 0.694
      delta_vs_single_model: "+0.136"
      n_generators_in_pool: 5
      generator_level_logo_f1: 0.830
      heterogeneity_amplifies_signal: true
      per_depth_f1:
        gen0: 0.95
        gen1: 0.82
        gen2plus: 0.78
    result_rationale: >
      Median 档下最 surprising 的正面结果：cross-model chains binary F1=0.830 
      远高于 single-model 0.694（+13.6pp）。原因：不同生成器在每个 depth step 
      引入不同的 distributional signature，generator heterogeneity 放大了 
      depth-to-depth 的 feature variance，使分类更容易。这对 practical relevance 
      有利——real-world 的多源 LLM 混合场景恰好是 DDR 最强的条件。
      但审稿人会质疑：(1) cross-model setup 中分类器是否在学习 "generator identity" 
      而非 "depth"？(2) 5-gen pool 是否过小？在 median 档下这被标为 minor concern，
      不影响 acceptance。LOGO evaluation 确保没有 generator leakage。
    tables:
      - name: "Table: Single-Model vs Cross-Model Chains"
        columns: [Setup, Binary_F1, 3-Class_F1, N_Generators, Eval_Protocol]
        rows:
          - [Single-model (LOGO), 0.694, 0.762, "5 (1 per chain)", LOGO]
          - [Cross-model (LOGO), 0.830, 0.789, "5 (mixed per chain)", Generator-LOGO]
          - [Δ, "+0.136", "+0.027", "—", "—"]
    figures_description:
      - "Side-by-side confusion matrices: single-model (gen-1/gen-2+ 混淆严重) vs cross-model (显著改善)。Cross-model 矩阵对角线更强。"
    analysis: >
      Cross-model 的高 F1 是 paper 的 second headline result，在 median 档下
      被审稿人接受为有趣且 practically relevant。但 "是否在学 generator identity" 
      的质疑需要用 feature importance 分析回应——如果 cross-model 下 shape features 
      importance 上升，说明分类器确实在用 depth-related signal。

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      扩展到 4 个 domain (Wikipedia, news, scientific, creative/code)，
      500 seeds × 5 depths per domain，测试 domain independence。
    expected_results:
      wikipedia_binary_f1: 0.695
      news_binary_f1: 0.712
      academic_binary_f1: 0.628
      code_binary_f1: 0.687
      overall_binary_f1: 0.676
      overall_binary_ci: [0.664, 0.688]
      max_gap_vs_wiki_pp: 6.7
      worst_domain: academic
      best_new_domain: news
      domain_independent_label: "moderate"
      cross_domain_transfer_f1: 0.65
      ddr_trend_preserved_all_domains: true
    result_rationale: >
      Median 档下，DDR 趋势在所有 domain 中保留，但分类性能有 domain 依赖性。
      Academic domain 最弱 (0.628)——scientific text 的 vocabulary 本身就 specialized 
      且 low-diversity（术语重复率高），压缩了 surface features 的 discriminative range。
      News (0.712) 最强——新闻文体的 vocabulary diversity 高，depth-driven 
      impoverishment 更易检测。Wikipedia (0.695) 接近 LOGO average 
      （训练数据的主要来源就是 Wiki seeds）。Code domain (0.687) 意外接近 Wiki，
      因为代码的 token distribution 有独特结构。
      审稿人会关注 academic domain 的 gap (−6.7pp vs Wiki)，但作为 Findings paper 
      这个 cross-domain analysis 是 bonus evidence，不是 core claim。
    tables:
      - name: "Table: Multi-Domain Binary F1"
        columns: [Domain, Binary_F1, 95%_CI, hapax_ρ, entropy_mean_ρ]
        rows:
          - [News, 0.712, "[0.690, 0.733]", -0.65, -0.58]
          - [Wikipedia, 0.695, "[0.675, 0.715]", -0.63, -0.60]
          - [Code, 0.687, "[0.664, 0.710]", -0.58, -0.55]
          - [Academic, 0.628, "[0.603, 0.652]", -0.52, -0.48]
    figures_description:
      - "4-domain radar chart: 每个 domain 一个多边形，axes 为 7 features 的 |ρ|. 所有 domain 形状相似但 academic 的多边形最小。"
    analysis: >
      Domain independence 部分成立（趋势保留），但性能 gap 存在。Academic domain 
      的弱表现可以在 paper 中用 "低 baseline vocabulary diversity" 解释，
      但需要显式讨论。这个实验在 median 档下为 Claim 1 增加了 moderate support，
      但也暴露了 method 在 specialized text domains 的局限。

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4)，测试 3-class 
      之外是否有更多 depth signal。附带 ordinal methods (CORAL, Frank-Hall)。
    expected_results:
      five_class_macro_f1: 0.50
      five_class_ci: [0.48, 0.52]
      three_class_macro_f1_ref: 0.762
      delta_5class_vs_3class: -0.262
      coral_f1: 0.50
      frank_hall_f1: 0.49
      standard_xgboost_f1: 0.50
      ordinal_methods_improve: false
      per_class_5class_f1:
        gen0: 0.92
        gen1: 0.55
        gen2: 0.35
        gen3: 0.30
        gen4: 0.38
      bottleneck: "gen-2/gen-3 boundary (practically indistinguishable)"
      confusion_concentration: "gen-2 and gen-3 mutually confused (65% of errors)"
    result_rationale: >
      Median 档下，5-class F1 约 0.50——比 3-class (0.762) 下降 26pp，
      证实 3-class 是 practical resolution ceiling。Gen-2/gen-3/gen-4 之间
      几乎不可区分（F1 分别为 0.35/0.30/0.38），因为 features 在 depth ≥2 后
      趋于饱和（DDR 的 drift 是减速的，不是线性的）。Ordinal methods (CORAL, 
      Frank-Hall) 未改善性能——说明瓶颈不在 model structure 而在 feature signal。
      审稿人会接受 "3-class resolution ceiling" 的结论，这是 honest limitation。
      Gen-4 的 F1 (0.38) 反而略高于 gen-3 (0.30)，可能是因为 gen-4 
      features 已极度偏离 gen-0 baseline，形成了另一个 discriminative boundary。
    tables:
      - name: "Table: 5-Class vs 3-Class Ordinal Classification"
        columns: [N_Classes, Method, Macro_F1, Gen-0_F1, Gen-1_F1, "Gen-2(+)_F1"]
        rows:
          - [3, XGBoost, 0.762, 0.95, 0.68, 0.66]
          - [5, XGBoost, 0.500, 0.92, 0.55, "0.35/0.30/0.38"]
          - [5, CORAL, 0.500, 0.91, 0.56, "0.34/0.31/0.38"]
          - [5, Frank-Hall, 0.490, 0.90, 0.54, "0.33/0.30/0.37"]
    figures_description:
      - "5×5 confusion matrix: gen-0 对角线极深，gen-2/3/4 区域颜色混乱（大量 off-diagonal mass）。"
    analysis: >
      5-class 结果清晰支持 paper 的 "3-class ceiling" claim。无需调整叙事。
      Gen-1/gen-2+ boundary 是分辨率瓶颈（86% binary errors as FN），
      更细分只会引入更多 noise。这个实验是 clean negative result，审稿人不会追问。

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Robustness to simulated human edits: (A) random word replacement (5/10/20%), 
      (B) LLM-simulated rephrasing。
    expected_results:
      baseline_binary_f1: 0.695
      random_5pct_f1: 0.650
      random_10pct_f1: 0.614
      random_20pct_f1: 0.591
      llm_rephrase_binary_f1: 0.647
      llm_rephrase_ci: [0.631, 0.662]
      llm_rephrase_multiclass_f1: 0.667
      edit_distance_ratio: 0.507
      avg_sentences_replaced: 1.69
      graceful_degradation: true
      catastrophic_threshold: ">20% random replacement"
      delta_5pct: -0.046
      delta_10pct: -0.081
      delta_20pct: -0.104
      delta_llm_rephrase: -0.045
    result_rationale: >
      Median 档下，method 在 light editing 下展现 graceful degradation：
      5% random replacement 仅降 4.6pp (0.695→0.650)，LLM rephrasing 降 4.5pp 
      (0.695→0.647)。审稿人会认为这个 robustness 是 "acceptable but not impressive"——
      real-world human editing 通常比 5% random replacement 更 targeted 也更 destructive。
      20% replacement 下降至 0.591（-10.4pp），说明 heavy editing 破坏 depth signal。
      LLM rephrasing（avg 1.69 sentences replaced, edit distance 0.507）接近 5% 
      random 的效果，说明 LLM-style editing 是一种 moderate perturbation。
      审稿人不会在这个实验上深入追问——它作为 appendix material 回应 RC5 即可。
    tables:
      - name: "Table: Robustness to Human Editing"
        columns: [Edit_Type, Edit_Rate, Binary_F1, Δ_vs_Baseline]
        rows:
          - [None (baseline), "0%", 0.695, "—"]
          - [Random replacement, "5%", 0.650, -0.046]
          - [Random replacement, "10%", 0.614, -0.081]
          - [Random replacement, "20%", 0.591, -0.104]
          - [LLM rephrasing, "~50% edit dist", 0.647, -0.045]
    figures_description:
      - "Line chart: X=edit rate, Y=binary F1. 线性下降趋势，LLM rephrase 点标注在约 5% equivalent 位置。Shaded area 表示 95% CI。"
    analysis: >
      Graceful degradation 成立。审稿人在 median 档下对此满意，
      但会在 limitations 中注明 "real-world editing patterns may differ from 
      random replacement and LLM rephrasing"。

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      加入 LD-Score (character-level distribution signature) 作为第 8 个特征，
      测试 character-level signal 是否与 token-level features 互补。
    expected_results:
      seven_feature_f1: 0.804
      eight_feature_with_ld_f1: 0.811
      delta: "+0.007"
      ld_score_importance_rank: "6/8 (below entropy_mean, above entropy_min)"
      ld_score_spearman_depth: -0.42
      ld_score_solo_f1: 0.721
      ld_score_is_drifting: true
      ld_score_corr_with_hapax: 0.68
      marginal_contribution_significant: false
      mcnemar_p_7_vs_8: 0.12
    result_rationale: >
      Median 档下，LD-Score 作为单独特征表现不错（solo F1=0.721），但加入 7-feature 
      ensemble 后边际贡献仅 +0.7pp (0.804→0.811)，McNemar p=0.12 不显著。
      原因：LD-Score 与 hapax_ratio 相关性高（r=0.68），character-level 
      和 token-level vocabulary diversity 高度共线。LD-Score 属于 drifting 类别
      （ρ=-0.42），进一步支持 DDR 中 central-tendency features drift 的结论，
      但不提供独立信息。审稿人不会对这个结果有强烈反应——它是 nice-to-have 
      analysis，写入 appendix 即可。不建议将 LD-Score 加入 main feature set 
      以保持 7-feature 的简洁叙事。
    tables:
      - name: "Table: LD-Score Feature Addition"
        columns: [Feature_Set, N_Features, Macro_F1, Binary_F1, McNemar_p]
        rows:
          - [7-feature baseline, 7, 0.804, 0.694, "—"]
          - [+ LD-Score, 8, 0.811, 0.699, 0.12]
          - [LD-Score only, 1, 0.721, 0.640, "—"]
    figures_description:
      - "Feature correlation matrix (8×8): LD-Score 与 hapax_ratio 格子颜色最深（r=0.68），说明共线性。"
    analysis: >
      LD-Score 不改变 headline numbers。作为 appendix 中 "character-level 
      features provide redundant signal" 的 evidence 有价值，支持论文选择 
      token-level features 的 design decision。

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned small LM (OLMo-1B-Instruct or Qwen3-1.7B) for end-to-end 
      depth classification，对比 handcrafted features。
    expected_results:
      qlora_3class_f1_instruct: 0.89
      qlora_3class_ci: [0.88, 0.91]
      qlora_binary_f1_instruct: 0.84
      qlora_binary_ci: [0.82, 0.85]
      qlora_5class_f1: 0.60
      seven_feature_3class_f1_ref: 0.762
      seven_feature_binary_f1_ref: 0.694
      delta_3class: "+0.128"
      delta_binary: "+0.146"
      qlora_base_3class_f1: 0.86
      qlora_base_binary_f1: 0.79
      inference_cost_ratio: "~150× (1B model vs 410M ref + XGBoost)"
      gpu_memory_gb: 4.2
      training_time_minutes: 28
    result_rationale: >
      Median 档下，QLoRA end-to-end 分类器大幅超越 7-feature ensemble 
      （3-class +12.8pp, binary +14.6pp）。这是一个 double-edged result：
      它证明 depth signal 存在且比 7 features 捕获的更丰富，但也意味着 
      审稿人会问 "既然 fine-tuned LM 远优于 handcrafted features，
      为什么不直接用 LM？" Paper 的回应是 efficiency argument：
      7-feature ensemble 只需 410M ref model + XGBoost（推理速度 ~150× faster），
      且 features 可解释（DDR analysis 的基础）。QLoRA 是 black-box。
      在 median 档下，审稿人接受 efficiency argument 但会标注：
      "the main methodological contribution (handcrafted features) is substantially 
      outperformed by standard fine-tuning"——这削弱了 method 维度的 novelty claim。
      Instruct model (0.89) 略优于 base (0.86)，因为 instruct 的 classification 
      head 更容易学习 task-specific patterns。5-class F1 (0.60) 仍远低于理想，
      确认 5-class resolution ceiling。
    tables:
      - name: "Table: Handcrafted vs End-to-End Classification"
        columns: [Method, 3-Class_F1, Binary_F1, 5-Class_F1, Inference_Cost]
        rows:
          - [7-feature XGBoost, 0.762, 0.694, 0.500, "1× (410M ref)"]
          - [QLoRA OLMo-1B-Instruct, 0.889, 0.836, 0.598, "~150×"]
          - [QLoRA Qwen3-1.7B-Instruct, 0.907, 0.867, 0.551, "~250×"]
          - [QLoRA OLMo-1B-Base, 0.859, 0.793, 0.540, "~150×"]
          - [QLoRA Qwen3-1.7B-Base, 0.904, 0.860, 0.554, "~250×"]
    figures_description:
      - "Grouped bar chart: 3-class / binary / 5-class 三组，每组 handcrafted vs QLoRA. QLoRA bars 明显高出，视觉冲击强。"
    analysis: >
      QLoRA 结果是 median 档下的 strategic risk：它验证了 depth signal 的真实性
      （fine-tuned model 能学到），但也暴露了 handcrafted features 的 performance gap。
      Paper 必须在 discussion 中坦诚报告，positioning 7-feature 为 
      "interpretable + efficient diagnostic" 而非 "best classifier"。
      审稿人会要求这段讨论的存在——缺失会被标为 major issue。

  - name: text_length_control
    plan_id: plan_013
    description: >
      排除 text length confound：(A) length-depth correlation, 
      (B) length-normalized features, (C) length-matched classifier evaluation。
    expected_results:
      spearman_length_depth_range: [-0.066, 0.134]
      length_depth_correlation: "weak (|ρ|<0.14)"
      normalized_ttr_trend_preserved: true
      normalized_hapax_trend_preserved: true
      normalized_rho_stronger: true
      length_matched_binary_f1: 0.724
      unmatched_binary_f1: 0.770
      delta_length_matched: -0.046
      random_subsample_control_f1: 0.740
      length_is_confound: false
      dropout_short_text_bias: true
    result_rationale: >
      Median 档下，length confound 被有效排除但有 nuance。Length-depth 相关性弱
      (|ρ|<0.14)，说明 deeper text 不是系统性地更短或更长。Length-normalized 
      surface features (TTR, hapax on fixed windows) 保留 drifting trend 且 
      ρ 值更强（normalization 消除了短文本 noise）。Length-matched subsampling 
      后 binary F1 从 0.770 降至 0.724（-4.6pp），但 random subsample control 
      (0.740) 也降了 3pp，说明 drop 主要来自 sample size reduction（短文本 dropout 
      减少了 training data），而非 length 本身是 confound。
      审稿人会接受 "length is not a confound" 结论，但可能追问 4.6pp drop 的 
      composition。Paper 需要同时报告 random-subsample control 以 deconfound 
      the deconfounding。
    tables:
      - name: "Table: Length Control Analysis"
        columns: [Condition, Binary_F1, Δ_vs_Full, Note]
        rows:
          - [Full (unmatched), 0.770, "—", "N=full dataset"]
          - [Length-matched, 0.724, -0.046, "Length distributions equalized"]
          - [Random subsample (same N), 0.740, -0.030, "Size control"]
          - [Δ attributable to length, "—", -0.016, "0.046 - 0.030"]
    figures_description:
      - "Length distribution violin plots by depth (5 violins). Shapes similar across depths, confirming weak length-depth correlation."
    analysis: >
      Clean confound control。Attributable length effect 仅 1.6pp（4.6pp total drop 
      中 3pp 来自 sample reduction）。审稿人在 median 档下对此满意——
      这是 paper credibility 的必要 check，不是 exciting finding。

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      加入 7B+ generator (Qwen3-8B-Base) 测试 scale effect。
      1000 seeds × 5 depths。
    expected_results:
      total_records: 4497
      unique_seeds: 995
      depth_dist: {0: 995, 1: 979, 2: 937, 3: 831, 4: 755}
      logo_6gen_avg_f1: 0.789
      logo_qwen3_8b_held_out_f1: 0.683
      logo_5gen_baseline_f1: 0.800
      delta_6gen_vs_5gen: -0.011
      spearman_hapax: -0.558
      spearman_ttr: -0.542
      spearman_entropy_mean: -0.475
      spearman_tail_decay: -0.089
      scale_degradation_confirmed: true
      degradation_magnitude: "moderate (-0.011 avg, Qwen3-8B at 0.683 vs 0.694 avg)"
      per_gen_ranking: "pythia-1b > qwen3-0.6b > pythia-2.8b > qwen3-1.7b > olmo-2-1b > qwen3-8b"
    result_rationale: >
      Median 档下，Qwen3-8B-Base 的 LOGO F1 (0.683) 低于 5-gen average (0.694)，
      确认 scale degradation 存在但 moderate。Higher-capacity models 压缩 feature 
      margins：hapax ρ=-0.558（vs avg -0.63），entropy_mean ρ=-0.475（vs avg -0.60）。
      DDR 趋势保留但幅度缩小。6-gen LOGO avg (0.789 macro) 比 5-gen (0.800) 
      降 1.1pp——可接受。审稿人在 median 档下不会将此视为 major weakness 
      但会要求在 limitations 中讨论 scale trend。Depth retention 更低
      (gen-4 仅 755/995=75.9% vs 5-gen avg ~85%)——大模型 generation 
      truncation 更频繁（EOS token 更 aggressive），需要在 paper 中提及。
      审稿人可能追问 "如果 70B 模型呢？"——这是 base-model scope 的内在局限，
      只能诚实标注为 future work。
    tables:
      - name: "Table: Scale Effect (6-Generator LOGO)"
        columns: [Generator, Params, LOGO_Binary_F1, hapax_ρ, entropy_mean_ρ]
        rows:
          - [Pythia-1B, 1B, 0.718, -0.65, -0.64]
          - [Qwen3-0.6B, 0.6B, 0.659, -0.60, -0.58]
          - [Pythia-2.8B, 2.8B, 0.724, -0.63, -0.60]
          - [Qwen3-1.7B, 1.7B, 0.702, -0.61, -0.57]
          - [OLMo-2-1B, 1.5B, 0.668, -0.57, -0.52]
          - [Qwen3-8B, 8B, 0.683, -0.56, -0.48]
          - ["**6-gen avg**", "—", "**0.692**", "-0.60", "-0.57"]
      - name: "Table: Depth Retention at Scale"
        columns: [Generator, gen4_retention, gen3_retention]
        rows:
          - [Pythia-2.8B, "83.1%", "87.8%"]
          - [Qwen3-8B, "75.9%", "83.5%"]
    figures_description:
      - "Scatter plot: X=log(params), Y=LOGO binary F1. 微弱负趋势，Qwen3-8B 在右下方。Dashed line 为 linear fit (R²~0.3)。"
    analysis: >
      Scale effect 是 honest limitation（-1.1pp avg degradation）。8B 是当前最大 
      generator，DDR 仍然 work（F1=0.683, above chance）。但 trend suggests 
      更大模型可能 further degrade。审稿人会标注但不会因此 reject。
      加入 Mistral-7B 后（plan 外但 registry 显示已完成）worst-case 降至 0.633，
      进一步说明 large-model challenge。

  - name: ordinal_baseline_comparison
    plan_id: plan_015
    description: >
      CRITICAL baseline: 测试 FastDetectGPT / Binoculars / LD-Score / Avg-LogProb 
      的 continuous scores 是否已提供 ordinal depth signal，与 7-feature 对比。
    expected_results:
      seven_feature_logo_f1: 0.798
      seven_feature_ci: [0.786, 0.799]
      avg_logprob_logo_f1: 0.765
      avg_logprob_ci: [0.616, 0.820]
      ld_score_logo_f1: 0.721
      ld_score_ci: [0.588, 0.770]
      fast_detect_gpt_logo_f1: 0.627
      fast_detect_gpt_ci: [0.511, 0.762]
      binoculars_logo_f1: 0.579
      binoculars_ci: [0.405, 0.664]
      best_single_detector: "Avg-LogProb (0.765)"
      seven_feature_advantage_pp: 3.3
      bootstrap_7feat_vs_avglogprob_p: 0.0
      bootstrap_7feat_vs_avglogprob_delta: 0.039
      bootstrap_7feat_vs_fdgpt_p: 0.0
      multi_detector_ensemble_f1: 0.795
      multi_detector_ci: [0.780, 0.810]
      four_det_plus_surface_f1: 0.795
      delta_7feat_vs_4det: "+0.003"
    result_rationale: >
      Median 档的 critical baseline test 通过但 margin 不大。7-feature (0.798) 
      显著优于所有 single detectors（bootstrap p=0），但 Avg-LogProb (0.765) 
      的 gap 仅 3.3pp。审稿人会说 "7-feature set 的优势 modest，而且 Avg-LogProb 
      作为 single feature 已经不错了——custom features 的边际贡献在 practical 
      意义上有多大？" 在 median 档下这个质疑被 offset by 两个论点：
      (1) 7-feature 的 CI 远窄于单检测器（cross-generator variance 更低），
      说明 robustness 更好；(2) DDR analysis 需要多个 features 才能做（
      这是 conceptual contribution，不只是 classification performance）。
      Multi-detector ensemble (4-det + surface, 0.795) 与 7-feature (0.798) 
      几乎等效但需要 2.4× inference cost + 3.2× GPU memory，
      支持 efficiency positioning。Binoculars CI 极宽 [0.405, 0.664] 
      说明它对 generator 极度敏感。
    tables:
      - name: "Table: 7-Feature vs Existing Detector Baselines (LOGO)"
        columns: [Method, LOGO_Macro_F1, 95%_CI, Spearman_ρ_depth, N_Models_Required]
        rows:
          - [7-feature XGBoost, 0.798, "[0.786, 0.799]", "—", "1 (410M ref)"]
          - [Avg-LogProb, 0.765, "[0.616, 0.820]", 0.788, "1 (410M ref)"]
          - [LD-Score, 0.721, "[0.588, 0.770]", 0.794, 0]
          - [FastDetectGPT, 0.627, "[0.511, 0.762]", 0.433, "2 (source + scoring)"]
          - [Binoculars, 0.579, "[0.405, 0.664]", 0.199, "2 (observer + performer)"]
          - [4-det + surface ensemble, 0.795, "[0.780, 0.810]", "—", "4+ models"]
      - name: "Table: Bootstrap Pairwise Comparisons"
        columns: [Comparison, Delta, p_value, Significant]
        rows:
          - [7-feat vs Avg-LogProb, "+0.033", 0.0, Yes]
          - [7-feat vs LD-Score, "+0.077", 0.0, Yes]
          - [7-feat vs FastDetectGPT, "+0.171", 0.0, Yes]
          - [7-feat vs 4-det ensemble, "+0.003", 0.38, No]
    figures_description:
      - "Forest plot: 每个 method 一行，point estimate + CI bar. 7-feature 的 CI 最窄，single detectors 的 CI 很宽（尤其 Binoculars）。"
      - "Per-generator heatmap: rows=methods, columns=generators, cells=F1. 7-feature 行颜色最均匀（跨 generator 稳定），Binoculars 行有明显的深/浅交替。"
    analysis: >
      Baseline comparison 是 paper 能否被接收的 gatekeeping experiment。
      7-feature 优势统计显著但 practical margin 不大（+3.3pp vs Avg-LogProb）。
      在 median 档下，审稿人接受 "custom features add value" 但会标注 
      "the advantage is modest"。关键防线是 CI width argument 和 DDR 
      conceptual contribution——如果 paper 只 claim classification performance，
      这个 margin 不够；但如果 position 为 "empirical characterization of DDR, 
      with classification as validation"，审稿人更容易接受。

  # === Additional experiments from extended registry ===

  - name: "9-gen scale evaluation (with Gemma-2-2B)"
    plan_id: "ext_057"
    description: >
      扩展至 9 个 generator (原 8 + Gemma-2-2B) 的 LOGO 评估，
      测试 broader generalization 和 edge cases。
    expected_results:
      nine_gen_logo_3class_f1: 0.751
      nine_gen_logo_binary_f1: 0.666
      eight_gen_baseline_3class_f1: 0.770
      delta_9gen_vs_8gen: -0.019
      gemma_2_2b_3class_f1: 0.628
      gemma_2_2b_binary_f1: 0.440
      gemma_2_2b_gen1_f1: 0.036
      mistral_7b_3class_f1: 0.605
      mistral_7b_binary_f1: 0.633
      per_gen_3class_range: [0.605, 0.857]
    result_rationale: >
      Median 档下 Gemma-2-2B 是 paper 中最显著的 anomaly：gen-1 F1=0.036 
      意味着分类器完全无法识别 Gemma 的 gen-1 output。原因：Gemma-2 的 
      architecture (grouped-query attention + RMSNorm) 和 training recipe 
      使其 gen-1 的 distributional features 异常接近 gen-0——depth signal 
      在第一步就极度微弱。这是 method failure 而非 Gemma 特殊性，
      因为其他大模型 (Qwen3-8B, Mistral-7B) 虽然 F1 较低但仍在 0.63+ 水平。
      审稿人会追问："gen-1 F1=0.036 是否意味着方法对某些 architecture 
      完全失败？如果是，如何判断哪些 generator 会失败？"
      这是 rebuttal 中需要回应的 medium-severity concern。
      Paper 必须在 9-gen appendix 中显式讨论 Gemma anomaly，
      并承认 "方法不保证对所有 generator architectures 均有效"。
    tables:
      - name: "Table: 9-Generator LOGO Results"
        columns: [Generator, Family, Params, 3-Class_F1, Binary_F1, Gen-1_F1]
        rows:
          - [Pythia-1B, Pythia, 1B, 0.857, 0.718, 0.65]
          - [Qwen3-0.6B, Qwen, 0.6B, 0.819, 0.659, 0.61]
          - [Pythia-2.8B, Pythia, 2.8B, 0.812, 0.724, 0.68]
          - [Qwen3-1.7B, Qwen, 1.7B, 0.811, 0.702, 0.66]
          - [OLMo-2-1B, OLMo, 1.5B, 0.773, 0.668, 0.58]
          - [Llama-3.2-3B, Llama, 3B, 0.759, 0.690, 0.60]
          - [Qwen3-8B, Qwen, 8B, 0.696, 0.647, 0.52]
          - ["**Gemma-2-2B**", Gemma, 2B, "**0.628**", "**0.440**", "**0.036**"]
          - [Mistral-7B-v0.3, Mistral, 7B, 0.605, 0.633, 0.44]
    figures_description:
      - "Per-generator binary F1 bar chart (9 bars), Gemma 和 Mistral bars 标红表示 anomaly/worst-case. Horizontal dashed line at 0.694 (8-gen avg)。"
    analysis: >
      Gemma anomaly 是 median 档审稿人重点追问对象。-0.25pp reviewer penalty 
      的来源。Paper 处理策略：承认 failure case，分析 Gemma gen-1 的 feature 
      distribution（是否与 gen-0 truly indistinguishable），讨论可能的 
      architectural 原因（GQA, training data composition）。

  - name: "DDR causality analysis"
    plan_id: "ext_058"
    description: >
      通过 permutation importance, Granger causality, feature intervention 
      三种方法验证 DDR 的 causal structure。
    expected_results:
      permutation_baseline_f1: 0.771
      drifting_avg_importance: 0.158
      stationary_avg_importance: 0.030
      drifting_stationary_ratio: 5.3
      granger_significant: "6/7 features"
      granger_nonsig: entropy_min
      granger_max_delta_r2: 0.031
      intervention_max_f1_drop: 0.020
      intervention_max_feature: entropy_max
    result_rationale: >
      Median 档下，causality analysis 是 DDR claim 的强化 evidence。
      5.3× permutation importance gap（drifting 0.158 vs stationary 0.030）
      清晰支持 DDR 的 feature-role 划分。6/7 features Granger significant 
      说明 temporal ordering matters（depth 预测 feature 值）。
      但 Granger max delta R² 仅 0.031——effect size 小，审稿人可能认为 
      "statistically significant but practically negligible"。
      Entropy_min 的 non-significance 与其 intermediate status 一致。
      Feature intervention max drop 仅 0.020（entropy_max），说明 
      no single feature is critical——系统鲁棒但个体 feature 贡献分散。
      审稿人会认可方法论的 rigor（三种独立 causality tests），
      但不会被 effect sizes 打动。
    tables:
      - name: "Table: DDR Causality Evidence"
        columns: [Method, Drifting_Signal, Stationary_Signal, Gap_Ratio]
        rows:
          - [Permutation importance, 0.158, 0.030, "5.3×"]
          - [Granger causality, "6/7 sig (p<0.05)", "—", "—"]
          - [Feature intervention (max F1 drop), 0.020, 0.006, "3.3×"]
    figures_description:
      - "Bar chart: 7 features × permutation importance, drifting features (hapax, ttr, entropy_mean) towers over stationary ones. Clear visual separation。"
    analysis: >
      Causality analysis 为 DDR 提供了超越 correlation 的 evidence，
      但 effect sizes 偏小。在 median 档下这是 "nice methodological rigor" 
      而非 game-changer。

  - name: "TOST bootstrap stability validation"
    plan_id: "ext_059"
    description: >
      Bootstrap TOST 验证 shape features 的 stationarity classification 
      在重采样下是否稳定。
    expected_results:
      n_bootstrap: 1000
      margin_d: 0.2
      entropy_max:
        rejection_rate: 1.0
        median_d: 0.062
        classification: "Stationary (robust)"
      entropy_min:
        rejection_rate: 1.0
        median_d: -0.016
        classification: "Stationary (robust)"
      tail_decay:
        rejection_rate: 1.0
        median_d: 0.088
        classification: "Stationary (robust)"
      entropy_std:
        rejection_rate: 0.0
        median_d: 0.458
        classification: "NOT stationary (TOST never rejects)"
        d_ci: [0.435, 0.479]
    result_rationale: >
      Median 档下的 key tension point：三个 shape features (entropy_max, 
      entropy_min, tail_decay) 通过 TOST 所有 1000 次 bootstrap 
      (rejection rate=1.0)，d 值远低于 0.2 threshold。但 entropy_std 
      的 rejection rate=0.0，d=0.458 [0.435, 0.479] 远超 equivalence margin。
      这直接否定了将 entropy_std 归入 "stationary" 组的原始分类。
      审稿人会追问："为什么原文将 entropy_std 归为 H1/stationary？
      TOST 明确拒绝了 equivalence。这是否意味着 DDR 的二分法本身有问题？"
      Paper 需要调整：将 entropy_std 移出 stationary 组，要么归入 drifting 
      (但 ρ=-0.20 比 drifting group 弱很多)，要么引入 "intermediate" 类别。
      Median 档的叙事方向选择 spectrum model：drifting → intermediate → stationary，
      entropy_std 和 entropy_min 居于 intermediate。
    tables:
      - name: "Table: TOST Bootstrap Stability (margin d=0.2)"
        columns: [Feature, Median_d, d_95%_CI, Rejection_Rate, Classification]
        rows:
          - [entropy_max, 0.062, "[0.037, 0.088]", "1000/1000", Stationary]
          - [entropy_min, -0.016, "[-0.042, 0.011]", "1000/1000", Stationary]
          - [tail_decay, 0.088, "[0.065, 0.111]", "1000/1000", Stationary]
          - ["**entropy_std**", "**0.458**", "**[0.435, 0.479]**", "**0/1000**", "**NOT stationary**"]
    figures_description:
      - "Bootstrap d distribution histogram (4 panels). 前三个 (entropy_max, min, tail_decay) 集中在 0 附近；entropy_std 的 distribution 完全在 0.4+ 区域，与 equivalence margin (±0.2) 无重叠。"
    analysis: >
      entropy_std 的 TOST 结果是 median 档下审稿人最可能追问的 technical point。
      Paper 必须从二分法转向 spectrum 模型，否则 internal inconsistency 
      会被标为 moderate issue。这个调整实际上使论文更 nuanced 也更 honest，
      审稿人倾向于正面看待。

  - name: "Instruct model evaluation (3 models)"
    plan_id: "ext_052-054"
    description: >
      在 Qwen3-1.7B-Instruct, OLMo-2-1B-Instruct, Llama-3.2-3B-Instruct 上
      测试 depth signal 在 instruct tuning 下的 degradation。
    expected_results:
      qwen_instruct_logo_binary: 0.658
      qwen_instruct_logo_3class: 0.543
      olmo_instruct_logo_binary: 0.338
      olmo_instruct_logo_3class: 0.420
      llama_instruct_binary: 0.838
      llama_instruct_3class: 0.544
      qwen_base_logo_binary: 0.821
      olmo_base_logo_binary: 0.763
      llama_base_binary: 0.849
      delta_qwen: -0.163
      delta_olmo: -0.425
      delta_llama: -0.011
      feature_reversal_count:
        olmo: "6/7"
        qwen: "partial (direction flip in entropy_mean)"
        llama: "3/7"
      spearman_direction_instruct: "多数特征 ρ>0 (reversed from base ρ<0)"
    result_rationale: >
      Median 档下 instruct degradation 是 paper 的 primary scope limitation。
      OLMo-Instruct 的 LOGO binary F1 仅 0.338（vs base 0.763, -42.5pp），
      6/7 features Spearman ρ 方向反转（base 为负/instruct 为正）。
      这说明 instruction tuning 的 format regulation 和 length normalization 
      破坏甚至反转了 DDR pattern。Qwen-Instruct degradation 中等 (-16.3pp)，
      Llama-Instruct 最小 (-1.1pp)——instruct 影响的 magnitude 是 model-specific。
      审稿人中 1-2 个会标注 "base-model-only scope" 为 major limitation 
      并扣 -0.5pp。Rebuttal 需要论证：(1) base model 在 data contamination 
      分析场景下仍然 relevant（web-scraped data 主要由 base/API 模型生成），
      (2) instruct 场景是 explicit future work with clear direction。
      Feature reversal 的发现本身有一定 novelty——instruct tuning 不只是削弱 
      depth signal，而是反转了 distributional dynamics，这值得在 discussion 中提及。
    tables:
      - name: "Table: Instruct vs Base Model Comparison"
        columns: [Model, Base_Binary_F1, Instruct_Binary_F1, Δ, Features_Reversed]
        rows:
          - [OLMo-2-1B, 0.763, 0.338, -0.425, "6/7"]
          - [Qwen3-1.7B, 0.821, 0.658, -0.163, "partial"]
          - [Llama-3.2-3B, 0.849, 0.838, -0.011, "3/7"]
    figures_description:
      - "Paired bar chart: base (blue) vs instruct (red) for 3 models. OLMo 的 instruct bar 极短，视觉冲击强。"
      - "Spearman ρ heatmap: rows=features, columns=base/instruct × 3 models. Base 列全蓝（negative），instruct 列 OLMo 全红（positive/reversed）。"
    analysis: >
      Instruct degradation 的异质性（OLMo 极严重，Llama 几乎不受影响）
      是一个 interesting finding，但也使 scope boundary 变得模糊——
      审稿人会问 "哪些 instruct model 会 degrade？能否 predict？"
      在 median 档下只能回答 "we cannot predict a priori" 并标注为 limitation。

  - name: "Temperature sensitivity curve"
    plan_id: "ext_048-050"
    description: >
      温度敏感性分析：t=0.5, 0.7, 0.9, 1.0 的 depth signal 强度和跨温度 transfer。
    expected_results:
      within_t05_binary: 0.813
      within_t07_binary: 0.694
      within_t09_binary: 0.480
      cross_t07_to_t10_binary_qwen: 0.418
      cross_t10_to_t07_binary_qwen: 0.944
      delta_t05_vs_t07: "+0.119"
      delta_t09_vs_t07: "-0.214"
      entropy_mean_rho_t05: -0.58
      entropy_mean_rho_t07: -0.60
      entropy_mean_rho_t09: -0.30
      reliable_range: "[0.5, 0.9) — ≤1pp degradation within [0.5, 0.7]"
      cross_temp_transfer_asymmetric: true
    result_rationale: >
      Median 档下，温度敏感性是第二个 scope limitation。t∈[0.5, 0.7] 
      内 depth signal 稳定（0.694-0.813），但 t=0.9 时急剧下降至 0.480 
      (below chance for binary)，entropy_mean ρ 从 -0.60 降至 -0.30。
      t=1.0 下跨温度 transfer 极差（Qwen t=0.7→t=1.0: 0.789→0.418, -37pp），
      但反方向 (t=1.0→t=0.7) 反而好 (0.944)——不对称 transfer 说明 
      high-temp features 是 low-temp features 的 superset（noise 更大但信号保留）。
      Paper 将 "t∈[0.5, 0.9)" 标为 reliable range，t≥0.9 为 degraded。
      审稿人在 median 档下会问 "most API models default to t=1.0, 
      does this limit real-world applicability?"——需要在 limitations 中回应。
    tables:
      - name: "Table: Temperature Sensitivity"
        columns: [Temperature, Within-CV_Binary_F1, entropy_mean_ρ, Reliable]
        rows:
          - [0.5, 0.813, -0.58, "Yes (stronger signal)"]
          - [0.7, 0.694, -0.60, "Yes (default)"]
          - [0.9, 0.480, -0.30, "No (severe degradation)"]
      - name: "Table: Cross-Temperature Transfer (Qwen3-1.7B)"
        columns: [Train_Temp, Test_Temp, Binary_F1, Δ_vs_Within]
        rows:
          - [0.7, 0.7, 0.789, "—"]
          - [0.7, 1.0, 0.418, -0.371]
          - [1.0, 0.7, 0.944, "+0.155"]
          - [1.0, 1.0, 0.825, "—"]
    figures_description:
      - "Temperature curve: X=temperature, Y=binary F1 + entropy_mean ρ (dual Y-axis). 两条曲线在 t=0.8 附近开始分叉下降。"
    analysis: >
      温度限制在 median 档下被标为 known scope boundary。
      t≥0.9 的 degradation 源于 high-temperature sampling 的 entropy inflation——
      所有 depth 的 entropy features 都被推高，压缩了 depth-to-depth 差异。

  - name: "Independent seed validation"
    plan_id: "ext_051"
    description: >
      用完全独立的 seed sets 验证 shared-seed LOGO 是否存在 seed leakage。
    expected_results:
      pythia_to_olmo_binary: 0.695
      olmo_to_pythia_binary: 0.666
      avg_independent: 0.680
      shared_seed_logo_ref: 0.694
      delta_vs_shared: -0.014
    result_rationale: >
      Median 档下，independent seed validation 确认 shared-seed LOGO 的 
      seed leakage 极小（delta 仅 -1.4pp）。Pythia→OLMo (0.695) 几乎等同于 
      LOGO average (0.694)，说明 seed content 不是主要信号源。
      OLMo→Pythia 略低 (0.666) 可能反映 OLMo 作为训练集的 feature space 
      不完全覆盖 Pythia 的分布。审稿人不会在此处追问——这是一个 clean validation。
    tables:
      - name: "Table: Seed Leakage Validation"
        columns: [Setup, Binary_F1, Seeds_Shared]
        rows:
          - [Shared-seed LOGO, 0.694, "Yes (same 995 seeds)"]
          - [Independent: Pythia→OLMo, 0.695, No]
          - [Independent: OLMo→Pythia, 0.666, No]
          - [Independent avg, 0.680, No]
    figures_description: []
    analysis: >
      Seed leakage 不是问题。-1.4pp delta 在 noise range 内。
      作为 supplementary validation 写入 appendix。

  - name: "Seed complexity stratification"
    plan_id: "ext_008_strat"
    description: >
      按 seed text complexity (low/medium/high) 分层分析 depth signal 是否依赖 seed 质量。
    expected_results:
      low_complexity_binary: 0.685
      medium_binary: 0.695
      high_complexity_binary: 0.695
      max_diff_binary_pp: 1.06
      seed_independent_label: true
    result_rationale: >
      Median 档下 seed complexity 对 depth signal 影响极小（max diff 1.06pp），
      确认方法对 seed 质量不敏感。Low complexity seeds 的微弱 drop (1pp) 
      可能源于低复杂度 text 的 feature range 本身更窄。审稿人不会在此处追问。
    tables:
      - name: "Table: Seed Complexity Stratification"
        columns: [Complexity_Bin, Binary_F1, Multiclass_F1, N_Seeds]
        rows:
          - [Low, 0.685, 0.772, ~332]
          - [Medium, 0.695, 0.778, ~332]
          - [High, 0.695, 0.779, ~331]
    figures_description: []
    analysis: >
      Clean result. Seed independence confirmed. Appendix material.

  - name: "Topic drift correlation"
    plan_id: "ext_topic_drift"
    description: >
      分析 semantic similarity (cosine) 与 depth 和 feature drift 的关系。
    expected_results:
      sim_0to1_mean: 0.622
      sim_1to2_mean: 0.683
      sim_2to3_mean: 0.801
      sim_3to4_mean: 0.859
      shape_entropy_std_rho: -0.164
      shape_tail_decay_rho: 0.068
      drifting_hapax_rho: -0.124
      drifting_entropy_mean_rho: -0.286
      semantic_convergence_with_depth: true
    result_rationale: >
      Median 档下，topic drift analysis 揭示 counter-intuitive pattern：
      deeper generations 在 semantic space 中 converge（sim 从 0.622 增至 0.859），
      即使 distributional features 在 diverge。这说明 DDR 不是 topic drift 
      的结果——topic 趋同但 distribution 趋异，方向相反。
      Drifting features 与 semantic sim 的弱负相关（entropy_mean ρ=-0.286）
      说明两者部分共变但独立性主要成立。Shape features 几乎无关（|ρ|<0.17）。
      审稿人可能对 "semantic convergence" finding 感兴趣但这不是 paper 的 
      core claim。作为 appendix evidence 支持 "DDR is distributional, not semantic"。
    tables:
      - name: "Table: Semantic Similarity by Depth Transition"
        columns: [Transition, Mean_Cosine_Sim, Std]
        rows:
          - [gen-0 → gen-1, 0.622, 0.165]
          - [gen-1 → gen-2, 0.683, 0.184]
          - [gen-2 → gen-3, 0.801, 0.201]
          - [gen-3 → gen-4, 0.859, 0.190]
    figures_description:
      - "Dual-axis plot: X=depth transition, left Y=cosine sim (ascending), right Y=entropy_mean (descending). 两条曲线交叉说明 semantic convergence vs distributional divergence。"
    analysis: >
      Semantic convergence + distributional divergence 的 decoupling 是 
      intellectually interesting 的 supporting evidence。审稿人在 median 档下
      会认可但不会因此提高分数。
```

**总结**：Median 档 (3.0 Solid Findings) 下，15 个核心实验 + 扩展实验的预测数据呈现一致画面：DDR 被验证为 robust 且 generation-intrinsic（plan_003 falsification passed），跨生成器泛化 solid（LOGO 0.694 binary），但存在三个审稿人会追问的 tension points：(1) entropy_std 的 TOST failure 要求从二分法转向 spectrum model，(2) base-model-only scope 在 instruct degradation（OLMo -42.5pp）面前需要 explicit justification，(3) Gemma-2-2B gen-1 F1=0.036 anomaly 需要显式讨论。QLoRA end-to-end 结果 (+13-15pp over 7-feature) 是最大的 strategic tension——paper 必须坦诚报告并以 interpretability + efficiency 定位 7-feature approach。Rebuttal 优先级：scope justification > Gemma anomaly > entropy_std reclassification。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "938141a3-f6f9-416f-a33b-5862af898ffc",
  "isSidechain": false,
  "requestId": "req_011CbDeHnp6PvYghYLo33Bzx",
  "type": "assistant",
  "uuid": "b13b9743-948a-4a2b-a156-177a7e8283cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWw3SG6piii5DmLiq9VKFV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8830,
      "cache_read_input_tokens": 37762,
      "output_tokens": 24585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 24585,
          "cache_read_input_tokens": 37762,
          "cache_creation_input_tokens": 8830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8830
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：3.0 Solid Findings — 核心贡献被认可但有保留，1-2 个 reviewer 对 scope 或 novelty 有中等强度质疑，需要 rebuttal 中补充解释或微调 claims 核心假设：['DDR 被部分接受：审稿人认可 drifting features 的趋势，但质疑 sh…",
  "leafUuid": "b13b9743-948a-4a2b-a156-177a7e8283cd",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Strengthen baseline comparison and instruct-model generalization",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：3.0 Solid Findings — 核心贡献被认可但有保留，1-2 个 reviewer 对 scope 或 novelty 有中等强度质疑，需要 rebuttal 中补充解释或微调 claims 核心假设：['DDR 被部分接受：审稿人认可 drifting features 的趋势，但质疑 sh…",
  "leafUuid": "b13b9743-948a-4a2b-a156-177a7e8283cd",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Strengthen baseline comparison and instruct-model generalization",
  "sessionId": "3a67f408-621b-4ff2-81bc-a26238ed40ed"
}
```

---
