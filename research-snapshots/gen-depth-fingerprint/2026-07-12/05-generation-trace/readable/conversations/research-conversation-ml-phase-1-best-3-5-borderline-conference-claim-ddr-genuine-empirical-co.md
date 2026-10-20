# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：3.5 Borderline Conference — 所有三个 Claim 在审稿中站住脚，DDR 被认可为 genuine empirical co

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-1/b6a50125-a340-49f6-a219-a467368d895d.jsonl`
- **Structured JSON:** [`58c868dd597233950fec.json`](../../sessions/58/58c868dd597233950fec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T10:05:27.689Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T10:05:27.689Z",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：3.5 Borderline Conference — 所有三个 Claim 在审稿中站住脚，DDR 被认可为 genuine empirical contribution，论文整体完成度被视为 Findings 上限\n核心假设：['DDR 的 drifting/stationary 分离被视为 non-trivial 发现，而非 vocabulary impoverishment 的重新包装（审稿人接受 McNemar p≈0 + reference-only binary F1=0.833 作为 complementarity 证据）', 'Base-model-only scope 被接受为合理的 first-step scoping（审稿人认可 instruct 退化的诚实报告是 strength 而非 weakness）', '0.694 LOGO binary F1 在 8-gen 跨家族设定下被认为 non-trivial（审稿人理解 leak-free LOGO 的难度）', \"Negative downstream finding (Claim 3) 被认可为 valuable honest science，而非 'method doesn't work'\", '33 页 + 20+ appendix 实验的体量被认为 thorough，没有 reviewer 因为 paper 组织问题拒稿']\n关键指标范围：{'expected_reviewer_avg': [3.5, 4.0], 'reviewer_spread': [3, 4], 'logo_binary_f1_perception': \"0.694 被接受为 'reasonable for this hard setting'\", 'cross_model_f1_weight': '0.830 cross-model F1 被 highlight 为 generalization evidence', 'ddr_causality_acceptance': '6/7 Granger + 5.5× permutation gap 被视为 sufficient causal evidence', 'instruct_scope_penalty': '0 — 诚实报告被视为 strength'}\n叙事方向：原始 framing 完全成立。三个 Claims 无需调整强度。Abstract/conclusion 保持当前版本：novel task formulation + DDR characterization + honest negative finding。强调 empirical thoroughness（9 generators, 5 families, 3 prompt types, 4 domains, causality analysis, robustness tests）。Contribution positioning 不变：Findings-level empirical+conceptual paper。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nfocus: Paper has been significantly expanded since last dream (May 14). New additions: (1) 9-generator scale evaluation with Gemma-2-2B (Appendix), (2) DDR causality analysis with permutation importance + Granger causality + feature intervention, (3) TOST bootstrap stability validation, (4) cross-model evaluation upgraded from sample-level CV to generator-level LOGO (binary F1=0.830). Total 33 pages, 20+ appendix experiments. Assess whether this is 3.0 Findings or 3.5 Borderline Conference level. Identify the single highest-impact improvement that could be made in 5 days before DDL.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_logo_f1: 0.7879\n    overall_ci95:\n    - 0.783\n    - 0.7929\n    spearman_entropy_max: 0.0503\n    spearman_entropy_min: -0.4061\n    spearman_hapax: -0.6467\n    spearman_ttr: -0.6302\n    spearman_entropy_mean: -0.6098\n    spearman_entropy_std: -0.1996\n    spearman_tail_decay: -0.0403\n- exp_id: plan-010-robustness\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_binary_f1: 0.695\n    5pct_binary_f1: 0.65\n    10pct_binary_f1: 0.614\n    20pct_binary_f1: 0.591\n    5pct_drop: -0.046\n    10pct_drop: -0.081\n    20pct_drop: -0.104\n- exp_id: plan-010-llm-rephrase\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_binary_f1: 0.6918\n    original_binary_ci:\n    - 0.6749\n    - 0.7067\n    original_multiclass_f1: 0.7385\n    original_multiclass_ci:\n    - 0.7269\n    - 0.7496\n    rephrased_binary_f1: 0.6471\n    rephrased_binary_ci:\n    - 0.6308\n    - 0.6619\n    rephrased_multiclass_f1: 0.6672\n    rephrased_multiclass_ci:\n    - 0.6548\n    - 0.6796\n    binary_drop: -0.0447\n    multiclass_drop: -0.0713\n    edit_distance_ratio: 0.5071\n    avg_sentences_replaced: 1.69\n    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\n    bugs_fixed:\n    - binary_task_gen1_vs_gen2+\n    - 3class_mapping\n    - tail_decay_rank100-1000\n- exp_id: plan-008-seed-stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_complexity_binary: 0.685\n    medium_binary: 0.695\n    high_complexity_binary: 0.695\n    low_complexity_multi: 0.772\n    medium_multi: 0.778\n    high_complexity_multi: 0.779\n    max_diff_binary_pp: 1.06\n    max_diff_multiclass_pp: 0.68\n    conclusion_label: seed_independent\n- exp_id: multi-domain-seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7459\n    news_binary_ci:\n    - 0.726\n    - 0.764\n    news_multiclass_f1: 0.6516\n    academic_binary_f1: 0.7386\n    academic_binary_ci:\n    - 0.72\n    - 0.757\n    academic_multiclass_f1: 0.6223\n    code_binary_f1: 0.7535\n    code_binary_ci:\n    - 0.737\n    - 0.77\n    code_multiclass_f1: 0.6344\n    wikipedia_baseline_binary_f1: 0.8148\n    wikipedia_baseline_multiclass_f1: 0.8632\n    max_gap_vs_wiki_pp: 7.62\n    worst_domain: academic\n    best_domain: code\n    conclusion_label: domain_independent\n- exp_id: exp_047_multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7119\n    news_binary_ci:\n    - 0.6898\n    - 0.7332\n    news_3class_f1: 0.7149\n    academic_binary_f1: 0.6279\n    academic_binary_ci:\n    - 0.6027\n    - 0.6515\n    academic_3class_f1: 0.6564\n    code_binary_f1: 0.6872\n    code_binary_ci:\n    - 0.6641\n    - 0.71\n    code_3class_f1: 0.6729\n    overall_binary_f1: 0.6757\n    overall_3class_f1: 0.6814\n    delta_vs_t10_news: -0.034\n    delta_vs_t10_academic: -0.1107\n    delta_vs_t10_code: -0.0663\n- exp_id: multi_domain_t07\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_048_cross_temp_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    6gen_logo:\n      within_0.7_binary: 0.9471\n      within_0.7_3class: 0.7888\n      cross_0.7to1.0_binary: 0.9001\n      cross_0.7to1.0_3class: 0.7225\n      within_1.0_binary: 0.9107\n      within_1.0_3class: 0.7257\n      cross_1.0to0.7_binary: 0.9581\n      cross_1.0to0.7_3class: 0.7913\n      caveat: Only Qwen3-1.7B differs between conditions; 5/6 generators share data\n    qwen_only:\n      within_0.7_binary: 0.9262\n      within_0.7_binary_ci:\n      - 0.916\n      - 0.935\n      within_0.7_3class: 0.769\n      within_0.7_3class_ci:\n      - 0.756\n      - 0.781\n      cross_0.7to1.0_binary: 0.7574\n      cross_0.7to1.0_binary_ci:\n      - 0.745\n      - 0.77\n      cross_0.7to1.0_3class: 0.4581\n      cross_0.7to1.0_3class_ci:\n      - 0.445\n      - 0.472\n      within_1.0_binary: 0.8248\n      within_1.0_binary_ci:\n      - 0.81\n      - 0.838\n      within_1.0_3class: 0.5738\n      within_1.0_3class_ci:\n      - 0.56\n      - 0.588\n      cross_1.0to0.7_binary: 0.9443\n      cross_1.0to0.7_binary_ci:\n      - 0.936\n      - 0.953\n      cross_1.0to0.7_3class: 0.6014\n      cross_1.0to0.7_3class_ci:\n      - 0.593\n      - 0.611\n      delta_0.7train_binary_pp: -16.9\n      delta_0.7train_3class_pp: -31.1\n      delta_1.0train_binary_pp: 12\n      delta_1.0train_3class_pp: 2.8\n      asymmetric_transfer: true\n- exp_id: exp_049_temp_curve_t05\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 4708\n    skipped: 113\n    seeds: 995\n    model: pythia-2.8b\n    temperature: 0.5\n    top_p: 0.9\n    within_cv_binary_f1: 0.8432\n    within_cv_binary_ci:\n    - 0.8301\n    - 0.8558\n    logo_binary_f1: 0.8136\n    logo_binary_ci:\n    - 0.7984\n    - 0.8282\n    entropy_mean_rho: -0.5844\n- exp_id: exp_050_temp_curve_t09\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    records: 4536\n    model: pythia-2.8b\n    temperature: 0.9\n    top_p: 0.9\n    within_cv_binary_f1: 0.5821\n    within_cv_binary_ci:\n    - 0.5655\n    - 0.5985\n    logo_binary_f1: 0.4804\n    logo_binary_ci:\n    - 0.4645\n    - 0.4976\n    entropy_mean_rho: -0.3016\n    delta_vs_t07_cv: -0.157\n    delta_vs_t07_logo: -0.259\n- exp_id: exp_051_independent_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_to_olmo_binary_f1: 0.6945\n    pythia_to_olmo_ci:\n    - 0.6727\n    - 0.7167\n    olmo_to_pythia_binary_f1: 0.666\n    olmo_to_pythia_ci:\n    - 0.6429\n    - 0.6893\n    avg_binary_f1: 0.6803\n    shared_seed_logo_ref: 0.694\n    delta_vs_shared: -0.014\n- exp_id: exp_052_instruct_qwen3_1_7b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8753\n    within_binary_ci:\n    - 0.8667\n    - 0.8837\n    within_3class_f1: 0.7324\n    within_3class_ci:\n    - 0.7195\n    - 0.745\n    base_binary_f1: 0.8614\n    base_3class_f1: 0.769\n    logo_instruct_binary: 0.658\n    logo_instruct_3class: 0.543\n    logo_base_binary: 0.821\n    logo_base_3class: 0.802\n    gen1_f1_instruct: 0.438\n    gen1_f1_base: 0.579\n    spearman_direction: reversed (instruct ρ>0, base ρ<0)\n    delta_within_binary: 0.014\n    delta_within_3class: -0.037\n    delta_logo_binary: -0.163\n- exp_id: exp_053_instruct_olmo2_1b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8131\n    within_binary_ci:\n    - 0.8012\n    - 0.8251\n    within_3class_f1: 0.5748\n    within_3class_ci:\n    - 0.5605\n    - 0.5897\n    base_binary_f1: 0.8454\n    base_3class_f1: 0.7538\n    gen1_f1_instruct: 0.256\n    gen1_f1_base: 0.523\n    delta_within_binary: -0.032\n    delta_within_3class: -0.179\n    spearman_instruct:\n      entropy_mean: 0.482\n      entropy_std: 0.296\n      entropy_min: 0.08\n      entropy_max: 0.306\n      tail_decay: 0.228\n      ttr: 0.006\n      hapax_ratio: 0.025\n    spearman_base:\n      entropy_mean: -0.639\n      entropy_std: -0.296\n      entropy_min: -0.387\n      entropy_max: 0.067\n      tail_decay: -0.141\n      ttr: -0.7\n      hapax_ratio: -0.712\n    features_reversed: 6/7\n    model_used: allenai/OLMo-2-0425-1B-Instruct\n- exp_id: exp_054_instruct_llama3_2_3b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    instruct_binary_f1: 0.8381\n    instruct_binary_ci:\n    - 0.828\n    - 0.847\n    instruct_3class_f1: 0.5437\n    instruct_3class_ci:\n    - 0.53\n    - 0.558\n    base_binary_f1: 0.8488\n    base_3class_f1: 0.7424\n    rho_instruct_entropy_mean: 0.2299\n    rho_instruct_entropy_std: 0.2623\n    rho_instruct_entropy_min: -0.0027\n    rho_instruct_entropy_max: 0.2036\n    rho_instruct_tail_decay: 0.1198\n    rho_instruct_ttr: -0.1411\n    rho_instruct_hapax_ratio: -0.1157\n    rho_base_entropy_mean: -0.627\n    rho_base_ttr: -0.6856\n    rho_base_hapax_ratio: -0.6975\n    direction_reversals: 3\n    reversed_features:\n    - entropy_mean\n    - entropy_std\n    - tail_decay\n    data_count: 4974\n- exp_id: exp_055_qlora_olmo_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8881\n    macro_f1_3class_std: 0.0071\n    macro_f1_5class: 0.5976\n    macro_f1_5class_std: 0.0046\n    binary_f1: 0.8363\n    binary_f1_std: 0.0096\n    n_samples: 4429\n    runtime_seconds: 1689.7\n- exp_id: exp_056_qlora_qwen_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.9066\n    macro_f1_3class_std: 0.0082\n    macro_f1_5class: 0.5514\n    macro_f1_5class_std: 0.0031\n    binary_f1: 0.8672\n    binary_f1_std: 0.0137\n    n_samples: 4963\n    runtime_seconds: 1880.5\n- exp_id: exp_055b_qlora_olmo_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8588\n    macro_f1_3class_std: 0.0036\n    macro_f1_5class: 0.5398\n    macro_f1_5class_std: 0.015\n    binary_f1: 0.7925\n    binary_f1_std: 0.0097\n    n_samples: 2379\n    runtime_seconds: 911.7\n    note: completed before kill signal\n- exp_id: exp_056b_qlora_qwen_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.904\n    macro_f1_3class_std: 0.0094\n    macro_f1_5class: 0.5544\n    macro_f1_5class_std: 0.0068\n    binary_f1: 0.8597\n    binary_f1_std: 0.0123\n    n_samples: 2291\n    runtime_seconds: 880.9\n    note: completed before kill signal\n- exp_id: exp_057_scale_9gen_logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: superseded by exp_057 (rerun with fixed Gemma data)\n    first_run_3class_f1: 0.7516\n    first_run_binary_f1: 0.6842\n    see_exp_057_for_final: true\n- exp_id: exp_058_ddr_causality\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    permutation_baseline_f1: 0.7714\n    drifting_avg_importance: 0.1578\n    stationary_avg_importance: 0.0297\n    drifting_stationary_ratio: 5.31\n    granger_significant_features: 6/7\n    granger_max_delta_r2: 0.031\n    granger_max_delta_r2_feature: entropy_std\n    granger_nonsig_feature: entropy_min\n    granger_panel_n: 29095\n    intervention_max_f1_drop: 0.0203\n    intervention_max_feature: entropy_max\n    intervention_min_f1_drop: 0.0061\n- exp_id: exp_059_tost_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_bootstrap: 1000\n    seed: 42\n    margin_d: 0.2\n    entropy_max:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.062\n      d_ci:\n      - 0.037\n      - 0.088\n    entropy_min:\n      median_p: 0\n      rejection_rate: 1\n      median_d: -0.016\n      d_ci:\n      - -0.042\n      - 0.011\n    tail_decay:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.088\n      d_ci:\n      - 0.065\n      - 0.111\n    entropy_std:\n      median_p: 1\n      rejection_rate: 0\n      median_d: 0.458\n      d_ci:\n      - 0.435\n      - 0.479\n    stationary_features_robust: true\n- exp_id: exp_057\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    9gen_logo_3class_f1: 0.751\n    9gen_logo_binary_f1: 0.6661\n    8gen_baseline_3class_f1: 0.7698\n    delta_9gen_vs_8gen: -0.0188\n    n_total_rows: 42015\n    n_generators: 9\n    qwen3_8b_3class_f1: 0.6955\n    qwen3_8b_binary_f1: 0.6468\n    gemma_2_2b_3class_f1: 0.6279\n    gemma_2_2b_binary_f1: 0.4402\n    per_gen_3class_f1:\n      pythia-1b: 0.8571\n      qwen3-0.6b: 0.8185\n      pythia-2.8b: 0.8117\n      qwen3-1.7b: 0.8114\n      olmo-2-1b: 0.7732\n      llama-3.2-3b: 0.7591\n      qwen3-8b: 0.6955\n      gemma-2-2b: 0.6279\n      mistral-7b-v0.3: 0.6045\n    tail_decay_consistency: VERIFIED_all_9gen_logprob_slope\n    data_source: features_9gen.csv (42015 rows, Gemma fixed)\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T10:05:27.692Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T10:05:27.692Z",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-20T10:05:27.712Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：3.5 Borderline Conference — 所有三个 Claim 在审稿中站住脚，DDR 被认可为 genuine empirical contribution，论文整体完成度被视为 Findings 上限
核心假设：['DDR 的 drifting/stationary 分离被视为 non-trivial 发现，而非 vocabulary impoverishment 的重新包装（审稿人接受 McNemar p≈0 + reference-only binary F1=0.833 作为 complementarity 证据）', 'Base-model-only scope 被接受为合理的 first-step scoping（审稿人认可 instruct 退化的诚实报告是 strength 而非 weakness）', '0.694 LOGO binary F1 在 8-gen 跨家族设定下被认为 non-trivial（审稿人理解 leak-free LOGO 的难度）', "Negative downstream finding (Claim 3) 被认可为 valuable honest science，而非 'method doesn't work'", '33 页 + 20+ appendix 实验的体量被认为 thorough，没有 reviewer 因为 paper 组织问题拒稿']
关键指标范围：{'expected_reviewer_avg': [3.5, 4.0], 'reviewer_spread': [3, 4], 'logo_binary_f1_perception': "0.694 被接受为 'reasonable for this hard setting'", 'cross_model_f1_weight': '0.830 cross-model F1 被 highlight 为 generalization evidence', 'ddr_causality_acceptance': '6/7 Granger + 5.5× permutation gap 被视为 sufficient causal evidence', 'instruct_scope_penalty': '0 — 诚实报告被视为 strength'}
叙事方向：原始 framing 完全成立。三个 Claims 无需调整强度。Abstract/conclusion 保持当前版本：novel task formulation + DDR characterization + honest negative finding。强调 empirical thoroughness（9 generators, 5 families, 3 prompt types, 4 domains, causality analysis, robustness tests）。Contribution positioning 不变：Findings-level empirical+conceptual paper。

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
  "promptId": "604a1191-cac6-4837-b5c8-80585198f980",
  "type": "user",
  "uuid": "3c5745cf-da42-4a4f-8583-2f9e2a791259",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T10:05:27.711Z_

```json
{
  "parentUuid": "3c5745cf-da42-4a4f-8583-2f9e2a791259",
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
  "uuid": "ae2ef558-c77f-4d6e-bdd1-613fbe11e3f0",
  "timestamp": "2026-05-20T10:05:27.711Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T10:05:27.711Z_

```json
{
  "parentUuid": "ae2ef558-c77f-4d6e-bdd1-613fbe11e3f0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "941fde83-eb59-4dbf-8410-eb0dbc53b89a",
  "timestamp": "2026-05-20T10:05:27.711Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：3.5 Borderline Conference — 所有三个 Claim 在审稿中站住脚，DDR 被认可为 genuine empirical contribution，论文整体完成度被视为 Findings 上限 核心假设：['DDR 的 drifting/stationary 分离被视为 non-tr…",
  "leafUuid": "941fde83-eb59-4dbf-8410-eb0dbc53b89a",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth fingerprinting evaluation—9 models, causality analysis, downstream utility",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d"
}
```

---

### Assistant

_source line 8 · 2026-05-20T10:05:31.192Z_

I'll read the experiment plan and registry data carefully to generate detailed predictions for each planned experiment under the "best" tier (3.5 Borderline Conference).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "941fde83-eb59-4dbf-8410-eb0dbc53b89a",
  "isSidechain": false,
  "requestId": "req_011CbDdfJm8EK8fRtJ153vrN",
  "type": "assistant",
  "uuid": "502c7ab0-66e7-421d-9a6a-734fbe93d93c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1Q5wyfr3gn5L3GbohAudG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24236,
      "cache_read_input_tokens": 11841,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 148,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24236
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

_source line 9 · 2026-05-20T10:05:33.244Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GzpjGTot6feZZnwC9M94pn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "502c7ab0-66e7-421d-9a6a-734fbe93d93c",
  "isSidechain": false,
  "requestId": "req_011CbDdfJm8EK8fRtJ153vrN",
  "type": "assistant",
  "uuid": "69b3b20c-9392-4852-9015-190292865ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1Q5wyfr3gn5L3GbohAudG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24236,
      "cache_read_input_tokens": 11841,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 148,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24236
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

_source line 10 · 2026-05-20T10:05:33.256Z_

<details><summary>↩ Tool result · `toolu_01GzpjGTot6feZZnwC9M94pn`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
5	- 不要复述用户的问题
6	- 不要给未被要求的建议或补充说明
7	- 推理要彻底，但输出只保留结论和必要信息
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69b3b20c-9392-4852-9015-190292865ae0",
  "isSidechain": false,
  "promptId": "604a1191-cac6-4837-b5c8-80585198f980",
  "type": "user",
  "uuid": "0f2e84c1-43a4-428a-8c5a-7c7ad24dc6ef",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "69b3b20c-9392-4852-9015-190292865ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T10:05:53.815Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, under the "best" tier (3.5 Borderline Conference). I need to use the registry data (completed experiments) to inform realistic predictions, and provide result_rationale for each prediction explaining why this result would occur at this tier level.

Let me go through each planned experiment and generate predictions. I have the registry data with actual results for many of these experiments. For the "best" tier, the predictions should align with the actual results where available, and for experiments without results, I should extrapolate based on the pattern.

Wait - looking more carefully, many of these experiments are already DONE in the registry. 

So I need to generate detailed predicted results for each plan (plan_001 through plan_015) under the "best" tier assumption. Since many have actual results in the registry, I should use those as the foundation and frame them as predictions consistent with what would constitute a 3.5 Borderline Conference paper. Now I'm mapping each planned experiment to its corresponding registry entry to pull the actual results and use them as the basis for these predictions. I'm seeing the remaining experiments through plan-015 are accounted for, with most marked as done and a few still in planning stages. Now I need to synthesize all these results into a cohesive narrative that positions the three core claims as solid and demonstrates the work is comprehensive enough for a borderline conference acceptance, making sure DDR comes across as a genuine finding rather than an artifact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f2e84c1-43a4-428a-8c5a-7c7ad24dc6ef",
  "isSidechain": false,
  "requestId": "req_011CbDdfiPgh2HVBKNEVbYnX",
  "type": "assistant",
  "uuid": "dcd6f8a8-492e-45dc-b720-d7c298fa059b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRHmViqtf7t95euAm5NViw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 36077,
      "output_tokens": 20721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20721,
          "cache_read_input_tokens": 36077,
          "cache_creation_input_tokens": 320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 320
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

_source line 12 · 2026-05-20T10:12:15.482Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。三个 Claims 强度不变：Claim 1 以 LOGO binary F1=0.694 作为 headline，
  cross-model 0.830 和 LOFO 0.686 作为 generalization 佐证；Claim 2 的 DDR 分离经 causality
  analysis（6/7 Granger sig, 5.5× permutation gap）和 TOST bootstrap 确认，被审稿人接受为
  genuine empirical contribution 而非 vocabulary impoverishment 的重新包装；Claim 3 的 negative
  finding 被认可为 honest science。论文定位 Findings-level empirical+conceptual paper，
  reviewer 平均分 3.5–4.0，spread 3–4。9 generators / 5 families / 3 prompt types / 4 domains /
  causality analysis / robustness tests 的体量被视为 thorough。Instruct 退化的诚实报告是 strength。
  33 页论文组织未被 reviewer 视为问题。

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      三部分分析：(A) Feature ablation — full vs reference-only vs surface-only；
      (B) DDR trend analysis — 每个 feature 的 depth-wise 趋势 + Spearman ρ；
      (C) Perplexity pre-validation for Claim 3
    expected_results:
      full_macro_f1: 0.820
      reference_only_f1: 0.719
      surface_only_f1: 0.763
      ref_vs_surf_bootstrap_ci: "[0.706, 0.733] vs [0.747, 0.774]"
      drifting_features: "entropy_mean (ρ≈−0.60), TTR (ρ≈−0.61), hapax_ratio (ρ≈−0.63)"
      stationary_features: "tail_decay (ρ≈0.04), entropy_std (ρ≈−0.12), entropy_max (ρ≈0.05)"
      median_ppl_by_depth: "13.50 → 4.96 → 3.00 → 2.07 → 1.72"
      ppl_depth_monotonic: true
    result_rationale: >
      在 best 档下，full 7-feature 以 0.820 显著高于两个 subset（McNemar p≈0），
      surface-only 以 0.763 高于 reference-only 0.719，但两者都显著低于 full，
      证明互补性而非冗余性。审稿人接受这一 4.4 pp gap 作为 complementarity 证据。
      DDR 趋势清晰：drifting 三特征 |ρ|>0.60 呈单调下降，shape 特征 |ρ|<0.12
      近乎水平。Perplexity 随 depth 单调下降（13.50→1.72）预验证 Claim 3 信号存在。
      这组结果为后续所有实验奠定特征空间基础。
    tables:
      - caption: "Table 2: Feature ablation results (5-fold CV, Pythia-2.8B)"
        columns: [Feature Set, N Features, Macro F1, 95% CI]
        rows:
          - [Full, 7, 0.820, "[0.807, 0.833]"]
          - [Surface-only, 2, 0.763, "[0.747, 0.774]"]
          - [Reference-only, 5, 0.719, "[0.706, 0.733]"]
      - caption: "Table 3: Feature-depth Spearman correlations"
        columns: [Feature, ρ, Category, Trend]
        rows:
          - [hapax_ratio, −0.63, Drifting, Monotonic decrease]
          - [TTR, −0.61, Drifting, Monotonic decrease]
          - [entropy_mean, −0.60, Drifting, Monotonic decrease]
          - [entropy_min, −0.39, Intermediate, Moderate decrease]
          - [entropy_std, −0.12, Stationary, Near-flat]
          - [entropy_max, 0.05, Stationary, Near-flat]
          - [tail_decay, 0.04, Stationary, Near-flat]
    figures_description:
      - "Fig 2: 7 features × depth (0–4) mean±std 折线图。上排三条（hapax, TTR, entropy_mean）明显单调下降；下排四条近水平。视觉上 DDR 分离一目了然。"
      - "Fig 3: Feature ablation bar chart with 95% CI error bars，三组并排比较。"
    analysis: >
      Full > Surface > Reference 的排序表明 surface 特征（TTR, hapax）捕获了最强的单维信号，
      但 reference 特征提供了不可替代的互补信息。Surface-only 虽然绝对值更高，但 reference-only
      在 binary task（gen-1 vs gen-2+）上表现更优（binary F1=0.833 vs 0.695），这是因为
      reference 特征在排除 gen-0 后捕获了更 fine-grained 的 NLL 分布位移。
      DDR 分离的物理解释：递归生成诱导 NLL 分布的 location shift，central-tendency 指标（mean, TTR,
      hapax）跟踪这一 shift 因而漂移，shape 指标（max, tail_decay）反映分布形态因而稳定。

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      扩展至 5 generators（Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B），
      LOGO 交叉验证评估跨生成器泛化性
    expected_results:
      total_records: 18423
      generators: 5
      logo_avg_macro_f1: 0.804
      logo_best_held_out: {model: pythia-1b, f1: 0.851}
      logo_worst_held_out: {model: olmo-2-1b, f1: 0.752}
      lofo_delta: 0.011
      ablation_full_f1: 0.804
      ablation_reference_only_f1: 0.754
      ablation_surface_only_f1: 0.747
      mcnemar_p: 0.0
      top3_features: [hapax_ratio (0.289), ttr (0.168), entropy_mean (0.160)]
    result_rationale: >
      在 best 档下，5-gen LOGO 均值 0.804 显示强跨生成器泛化。Pythia-1B held-out 最高（0.851）
      因为 Pythia-2.8B 在训练集中提供了同家族信号；OLMo held-out 最低（0.752）因为 OLMo
      的生成分布与 Pythia/Qwen 家族差异最大。Family-out delta 仅 0.011 pp，审稿人接受为
      cross-family generalization 证据。Feature importance 排序（hapax > ttr > entropy_mean）
      与 plan_001 一致，确认 surface drifting 特征是主驱动力，但 McNemar p≈0 证明
      reference 特征对 full 集的贡献统计显著。
    tables:
      - caption: "Table 4: LOGO cross-generator evaluation"
        columns: [Held-out Generator, Macro F1, Binary F1, Gen-1 F1]
        rows:
          - [Pythia-1B, 0.851, 0.724, 0.689]
          - [Qwen3-0.6B, 0.824, 0.710, 0.652]
          - [Qwen3-1.7B, 0.805, 0.698, 0.641]
          - [Pythia-2.8B, 0.804, 0.694, 0.638]
          - [OLMo-2-1B, 0.752, 0.663, 0.585]
          - [Average, 0.804, 0.694, 0.641]
    figures_description:
      - "Fig 4: Per-generator LOGO F1 bar chart，按 family 着色（Pythia 蓝, OLMo 绿, Qwen 橙），error bars 为 bootstrap 95% CI。"
    analysis: >
      5-gen LOGO 为后续 8-gen/9-gen 扩展奠定基线。OLMo 的相对弱势来自其 tokenizer 和
      训练数据分布与 Pythia/Qwen 的差异——这本身验证了 DDR 在不同预训练配方下的鲁棒性（仍 >0.75）。
      LOFO delta 仅 0.011 说明 Pythia 家族重叠未严重膨胀 LOGO 指标。

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      测试非 Pythia reference model（OLMo-2-1B, Qwen3-0.6B）提取特征，
      验证 DDR 是否为 generation-intrinsic 而非 reference-model artifact
    expected_results:
      logo_f1_pythia_ref: 0.803
      logo_f1_olmo_ref: 0.807
      logo_f1_qwen_ref: 0.816
      entropy_drift_all_refs_negative: true
      pythia_ref_drift_range: "[−1.19, −1.40]"
      olmo_ref_drift_range: "[−0.61, −0.91]"
      qwen_ref_drift_range: "[−0.96, −1.35]"
      dual_dynamics_is_pythia_artifact: false
    result_rationale: >
      在 best 档下，三个 reference model 均产生负向 entropy drift（所有 range 为负），
      LOGO F1 跨 reference 差异 <1.5 pp（0.803–0.816），关键性地证明 DDR 是
      generation-intrinsic 现象而非 Pythia-410M 特有 artifact。Qwen reference 略优
      可能因其 tokenizer 粒度更细，捕获了更丰富的 NLL 分布信息。这是 Claim 2 的核心
      falsification test 通过：如果 DDR 消失于非 Pythia reference，整个 dual dynamics
      叙事将崩塌。审稿人在 best 档下接受这一 3-reference 交叉验证为充分证据。
    tables:
      - caption: "Table 5: Cross-reference-model DDR validation"
        columns: [Reference Model, LOGO F1, entropy_mean drift range, DDR preserved]
        rows:
          - [Pythia-410M (default), 0.803, "[−1.19, −1.40]", "✓"]
          - [OLMo-2-1B, 0.807, "[−0.61, −0.91]", "✓"]
          - [Qwen3-0.6B, 0.816, "[−0.96, −1.35]", "✓"]
    figures_description:
      - "Fig 5: 三个 reference model 下 entropy_mean 随 depth 的漂移曲线对比。斜率不同但方向一致（均为负），视觉上有力证明 DDR 的 reference-invariance。"
    analysis: >
      漂移幅度的差异（Pythia > Qwen > OLMo）反映了 reference model 自身 perplexity scale 的差异，
      但方向一致性是关键。这排除了 "DDR 只是 Pythia tokenizer 的 artifact" 这一最致命的替代解释。

  - name: downstream_utility
    plan_id: plan_004
    description: >
      OLMo-1B fine-tune on depth-stratified subsets，3 seeds with bootstrap CIs，
      sample-count-matched comparison。验证 Claim 3（negative finding）。
    expected_results:
      total_runs: 15
      variants:
        all: {ppl_mean: 2.335, ppl_std: 0.0003}
        size_matched: {ppl_mean: 2.367, ppl_std: 0.0002}
        depth01: {ppl_mean: 2.387, ppl_std: 0.0005}
        binary_filtered: {ppl_mean: 2.389, ppl_std: 0.0004}
        depth0_only: {ppl_mean: 2.681, ppl_std: 0.0012}
      ranking: "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)"
      tost_equivalence_p: 0.00011
      tost_margin: "±2%"
      seed_variance: "<0.002 ppl across seeds within same variant"
      cohens_d_sizeMatched_vs_depth01: "inflated by low variance"
    result_rationale: >
      在 best 档下，negative finding 清晰：depth-aware filtering 不优于 random subsampling（size_matched
      2.367 vs depth01 2.387，差 0.020 ppl）。TOST 在 ±2% margin 下 p=1.1×10⁻⁴ 确认统计等价。
      depth0_only 的显著劣势（2.681）是预期的——纯人类文本量太少（797 samples）。关键是
      size_matched vs depth01 的差异方向反直觉：random subsample 比 depth-curated 还好 0.020 ppl，
      说明 depth 信息对下游 CLM 质量无 curative 价值。审稿人在 best 档下将此认可为
      "valuable honest science" 而非 "method doesn't work"——论文诚实地将 depth fingerprinting
      定位为 diagnostic tool（provenance characterization）而非 curative tool（data selection）。
      三 seed 极低方差（<0.002）既增强结论可靠性，也意味着 Cohen's d 被人为放大，论文正确选择
      TOST 而非 effect size 作为主检验。
    tables:
      - caption: "Table 7: Downstream CLM perplexity by training data composition (3 seeds)"
        columns: [Variant, N train, Ppl (mean±std), Δ vs size_matched]
        rows:
          - [All data, 12299, "2.335 ± 0.0003", −0.032]
          - [Size-matched random, 3951, "2.367 ± 0.0002", "— (baseline)"]
          - [Depth 0+1 only, 3951, "2.387 ± 0.0005", +0.020]
          - [Binary-filtered, 3951, "2.389 ± 0.0004", +0.022]
          - [Depth 0 only, 797, "2.681 ± 0.0012", +0.314]
    figures_description:
      - "Fig 7: Bar chart of perplexity by variant with error bars (3 seeds)。视觉上 size_matched/depth01/binary_filtered 几乎齐平，depth0_only 显著高出。"
    analysis: >
      Negative finding 的关键价值在于终止了一个看似合理但无效的研究方向：既然 depth 信息存在且可检测，
      自然会假设可用于数据筛选。实验证明这一假设不成立。More data > better data 在 3951 samples
      的低数据量下尤为明显。TOST equivalence 而非 NHST 是正确的统计框架选择。

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      比较 continuation / elaboration / inspired_rewriting 三种 prompt type 的 depth signal
    expected_results:
      cv_f1:
        continuation: 0.781
        inspired_rewriting: 0.737
        elaboration: 0.730
      lopto_f1:
        held_out_continuation: 0.762
        held_out_elaboration: 0.762
        held_out_rewriting: 0.733
        average: 0.753
      depth_retention_d4_d0:
        continuation: 0.831
        inspired_rewriting: 0.939
        elaboration: 0.986
      drift_hapax:
        continuation: −0.74
        elaboration: −0.83
        rewriting: −0.80
      drift_ttr:
        continuation: −0.607
        elaboration: −0.641
        rewriting: −0.618
    result_rationale: >
      在 best 档下，三种 prompt type 均保留 DDR 信号但强度不同。Continuation 的 within-type
      CV F1 最高（0.781）但 depth retention 最低（83.1%），因为 continuation 给予模型最大自由度，
      导致更多 chain dropout 但也产生更强的 distributional shift。Elaboration retention 最高
      （98.6%）但 CV F1 最低（0.730），因为 elaboration 约束模型围绕原文展开，压缩了
      cross-depth 变异。Rewriting 居中。Leave-one-prompt-type-out 交叉验证（avg 0.753）
      低于 within-type（avg 0.749）仅 ~0.4 pp，表明 prompt type 间的 DDR 信号高度可迁移。
      审稿人接受 prompt-type dependence 的透明报告为 ecological validity 证据。
    tables:
      - caption: "Table 8: Prompt-type comparison (Pythia-2.8B)"
        columns: [Prompt Type, CV F1, LOPTO F1, Depth Retention, hapax ρ]
        rows:
          - [Continuation, 0.781, 0.762, 0.831, −0.74]
          - [Inspired rewriting, 0.737, 0.733, 0.939, −0.80]
          - [Elaboration, 0.730, 0.762, 0.986, −0.83]
    figures_description:
      - "Fig 8: 三种 prompt type 下 hapax_ratio 和 entropy_mean 的 depth-wise 趋势。Continuation 斜率最陡但方差最大；elaboration 斜率平缓但 chain 最完整。"
    analysis: >
      Prompt-type 差异本身是有趣发现：语义约束越强（elaboration > rewriting > continuation），
      chain 越稳定但 depth discriminability 越低。这与 DDR 的 location-shift 解释一致——
      约束越强，模型输出分布被锚定在更窄的范围内，location shift 幅度减小。

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      构建平行 paraphrasing chains 与 continuation chains 直接比较，
      测试 attractor convergence theory
    expected_results:
      paraphrase_cv_f1: 0.62
      continuation_cv_f1: 0.781
      paraphrase_depth_retention: 0.97
      paraphrase_hapax_rho: −0.25
      paraphrase_entropy_mean_rho: −0.18
      attractor_convergence_depth: 2
      delta_cv_f1: −0.161
    result_rationale: >
      在 best 档下，paraphrasing chains 的 depth signal 显著弱于 continuation（CV F1 0.62
      vs 0.781，−16.1 pp）。Paraphrasing 由于语义保持约束，每步输出被 attractor basin 拉回，
      depth 间差异在 depth 2 后趋于收敛（与 ACL 2025 "LLM as Broken Telephone" 的 ~3 class
      ceiling 一致）。DDR drifting 特征在 paraphrase 中 ρ 幅度大幅缩小（hapax −0.25 vs −0.63），
      因为 paraphrase 保持语义→保持词汇多样性→TTR/hapax drift 被抑制。这验证了论文核心定位：
      DDR 是 non-paraphrastic chain 特有的现象，paraphrastic chain 走向 attractor convergence。
      审稿人在 best 档下接受这一对比作为 task formulation 的 motivation——深度估计在
      continuation/elaboration chain 中才有 meaningful signal。
    tables:
      - caption: "Table 9: Paraphrastic vs non-paraphrastic chains"
        columns: [Chain Type, CV F1, hapax ρ, entropy_mean ρ, Retention d4/d0]
        rows:
          - [Continuation, 0.781, −0.74, −0.56, 0.831]
          - [Paraphrasing, 0.62, −0.25, −0.18, 0.97]
          - [Δ, −0.161, +0.49, +0.38, +0.139]
    figures_description:
      - "Fig 9: Paraphrastic vs continuation 的 feature drift 对比。Continuation 线条陡降，paraphrase 在 depth 2 后平坦化，视觉上呈 attractor convergence。"
    analysis: >
      这是论文与 ACL 2025 attractor cycle 理论的关键联系点。Non-paraphrastic chains 不受
      semantic-preservation attractor 约束，因此 distributional drift 可以持续到更深层，
      为 depth estimation 提供更丰富的信号空间。

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains（每步使用不同 generator）vs single-model chains，
      模拟真实 web contamination 场景
    expected_results:
      cross_model_binary_f1: 0.830
      cross_model_3class_f1: 0.789
      single_model_binary_f1: 0.694
      single_model_3class_f1: 0.762
      cross_model_logo_binary: 0.830
      delta_binary_vs_single: +0.136
      n_generators_in_cross: 5
    result_rationale: >
      在 best 档下，cross-model chains 的 binary F1 0.830 显著高于 single-model 0.694
      （+13.6 pp），这一 counterintuitive 结果的原因是：不同 generator 在每步引入额外的
      distributional discontinuity（不同 tokenizer bias, 不同 perplexity scale），
      放大了 depth 间的特征差异。这对审稿人而言是 strength——说明在更 realistic 的
      heterogeneous contamination 场景下，depth signal 反而更强。0.830 cross-model binary F1
      被 highlight 为 generalization evidence，审稿人接受 5-gen subset LOGO 作为评估方法。
      3-class F1 同样提升（0.789 vs 0.762），但提升幅度小于 binary，因为 gen-0 identification
      的 seed-sharing advantage 在两种设定下相当。
    tables:
      - caption: "Table 6: Cross-model vs single-model chain evaluation"
        columns: [Setting, Binary F1, 3-class F1, N Generators]
        rows:
          - [Single-model LOGO, 0.694, 0.762, "8 (homogeneous)"]
          - [Cross-model LOGO, 0.830, 0.789, "5 (heterogeneous)"]
          - [Δ, +0.136, +0.027, "—"]
    figures_description:
      - "Fig 6: Cross-model vs single-model confusion matrices 并排。Cross-model 的 gen-1/gen-2+ 边界更清晰。"
    analysis: >
      Cross-model 的优势来自 generator heterogeneity amplifying distributional shifts。
      在单模型 chain 中，depth-wise drift 是同一模型 bias 的累积；在 cross-model chain 中，
      每步引入新模型 bias，产生更大的 inter-depth 特征差异。这是 ecological validity 的
      正面证据：真实世界的 contamination 更可能涉及多个 generator。

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      扩展至 4 domains（Wikipedia, news, scientific, creative/code），
      500 seeds/domain × 5 depths
    expected_results:
      news_binary_f1: 0.746
      news_binary_ci: [0.726, 0.764]
      academic_binary_f1: 0.739
      academic_binary_ci: [0.720, 0.757]
      code_binary_f1: 0.754
      code_binary_ci: [0.737, 0.770]
      wikipedia_baseline_binary_f1: 0.815
      max_gap_vs_wiki_pp: 7.62
      worst_domain: academic
      best_domain: code
      conclusion_label: domain_independent
    result_rationale: >
      在 best 档下，所有 domain 的 binary F1 均在 0.739–0.754 范围内（排除 Wikipedia 基线），
      domain 间 max gap 仅 1.5 pp，审稿人接受 DDR 为 domain-independent 现象。Wikipedia
      基线（0.815）高出 ~7 pp 是预期的——Wikipedia 种子文本结构化程度更高、长度更稳定，
      减少了 confounding variation。Academic domain 最低（0.739）因为学术文本的词汇多样性
      本身就高且 depth 间变化小（base model 生成学术文本时更依赖 template phrasing）。
      Code domain 意外地最高（0.754），因为 code-like 文本的 entropy 分布更 bimodal，
      DDR drifting 在 entropy_mean 上更明显。所有 CI 均不包含 0.5（random baseline），
      确认 depth signal 在所有 domain 中统计显著。
    tables:
      - caption: "Table 10: Multi-domain evaluation"
        columns: [Domain, Binary F1, 95% CI, 3-class F1]
        rows:
          - [Wikipedia (baseline), 0.815, "[0.799, 0.831]", 0.863]
          - [Code, 0.754, "[0.737, 0.770]", 0.634]
          - [News, 0.746, "[0.726, 0.764]", 0.652]
          - [Academic, 0.739, "[0.720, 0.757]", 0.622]
    figures_description:
      - "Fig 10: Domain-wise binary F1 with 95% CI error bars。四个 domain 的 CI 大幅重叠，视觉上确认 domain independence。"
    analysis: >
      Multi-domain 结果直接回应 RC6（ecological validity）。DDR 在 news/academic/code 上的
      一致性说明 depth signal 不依赖于特定文本类型的 vocabulary 特征。3-class F1 的 domain
      差异更大（0.622–0.863），因为 gen-0 vs gen-1 区分依赖 seed-specific 线索，这在
      不同 domain 中差异更大。

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class 序数分类（gen-0 至 gen-4），测试更细粒度 depth resolution 的可行性
    expected_results:
      five_class_f1: 0.50
      three_class_f1_reference: 0.762
      ordinal_coral_f1: 0.49
      ordinal_frank_hall_f1: 0.50
      xgboost_standard_f1: 0.50
      bottleneck: "gen-1/gen-2 boundary, 86% binary FNs concentrated here"
      gen3_vs_gen4_f1: 0.35
    result_rationale: >
      在 best 档下，5-class F1 降至 ~0.50，相比 3-class 的 0.762 大幅下降。Ordinal methods
      （CORAL, Frank-Hall）未能改善——这说明 depth signal 的 resolution ceiling 在 3 class，
      不是分类方法的选择问题而是 feature space 的固有限制。Gen-1/gen-2 boundary 贡献了 86%
      的 binary errors（作为 FN），因为 gen-1 和 gen-2 在 feature space 中高度重叠。
      Gen-3 vs gen-4 几乎不可分（F1≈0.35）。审稿人在 best 档下接受 3-class 为 practical
      ceiling，论文诚实报告这一限制为 strength。5-class 负面结果排除了 "只要用更好方法就能
      区分更多 depth" 的替代假说。
    tables:
      - caption: "Table A.3: Ordinal classification results"
        columns: [Method, 3-class F1, 5-class F1, Δ]
        rows:
          - [XGBoost (standard), 0.762, 0.50, −0.262]
          - [CORAL, 0.758, 0.49, −0.268]
          - [Frank-Hall, 0.760, 0.50, −0.260]
    figures_description:
      - "Fig A.3: 5-class confusion matrix。Gen-1/gen-2 和 gen-3/gen-4 的 off-diagonal cells 密集，清晰展示 resolution bottleneck。"
    analysis: >
      5-class 的 ceiling 与 DDR 的物理解释一致：location shift 在前几步（0→1→2）幅度最大，
      之后递减。Gen-3 和 gen-4 的 NLL 分布差异已小于 feature extraction noise floor。

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      鲁棒性测试：(A) Random word replacement (5/10/20%)，(B) LLM-simulated editing
    expected_results:
      baseline_binary_f1: 0.695
      random_5pct_f1: 0.650
      random_10pct_f1: 0.614
      random_20pct_f1: 0.591
      llm_rephrase_binary_f1: 0.647
      llm_rephrase_multiclass_f1: 0.667
      llm_edit_distance_ratio: 0.507
      llm_avg_sentences_replaced: 1.69
      drop_5pct: −0.046
      drop_10pct: −0.081
      drop_20pct: −0.104
      drop_llm: −0.045
    result_rationale: >
      在 best 档下，depth signal 对 human editing 展现 graceful degradation。5% random noise
      仅降 4.6 pp，LLM rephrase（平均替换 1.69 句，编辑距离 50.7%）降 4.5 pp——两者接近，
      因为 LLM rephrase 虽然更自然但实际修改幅度（50.7% edit distance）与 5% random 在
      feature 空间的扰动量级相当。20% random 的 10.4 pp drop 仍保持 F1>0.59（>random baseline），
      说明 depth signal 不完全依赖逐字保真。审稿人在 best 档下将 graceful degradation
      视为 positive——完全抵抗 editing 是不现实的，important 是 degradation curve 平滑且
      在 realistic editing level（5–10%）下性能损失可控。LLM rephrase 结果直接回应 RC5。
    tables:
      - caption: "Table A.5: Robustness to text editing"
        columns: [Condition, Binary F1, Δ vs baseline]
        rows:
          - [No editing (baseline), 0.695, "—"]
          - [5% random replacement, 0.650, −0.046]
          - [10% random replacement, 0.614, −0.081]
          - [20% random replacement, 0.591, −0.104]
          - [LLM rephrase (avg 1.69 sent), 0.647, −0.045]
    figures_description:
      - "Fig A.5: Robustness degradation curve。X 轴为 edit intensity，Y 轴为 binary F1。平滑下降，无 cliff edge。LLM rephrase 标注在 5% 附近。"
    analysis: >
      LLM rephrase 与 5% random 的 drop 相近这一发现本身有价值：LLM editing 的特征空间扰动
      并不比 naive random replacement 更具破坏性，可能因为 LLM editing 保持了文本的局部统计
      一致性（不引入 out-of-distribution tokens）。

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      添加 LD-Score（character-level distributional signature）作为额外特征
    expected_results:
      seven_feature_f1: 0.798
      eight_feature_with_ld_f1: 0.803
      ld_score_only_f1: 0.721
      ld_score_spearman_depth: −0.794
      delta_with_ld: +0.005
      ld_feature_importance_rank: 4
    result_rationale: >
      在 best 档下，LD-Score 作为 character-level 特征与 token-level reference 特征部分互补，
      加入后 LOGO F1 提升 0.5 pp（0.798→0.803），统计上显著但 practical 提升有限。
      LD-Score 单独的 F1=0.721 介于 surface-only（0.688）和 reference-only（0.713）之间，
      Spearman ρ=−0.794 表明其与 depth 有强负相关。Feature importance 排第 4（在 hapax,
      ttr, entropy_mean 之后），说明 LD-Score 捕获的信号与 reference 特征高度 correlated
      但非完全冗余。审稿人在 best 档下接受将 LD-Score 作为 supplementary evidence，
      论文在 appendix 中报告此结果。7-feature 仍为 primary model 以保持简洁性。
    tables:
      - caption: "Table A.6: LD-Score augmentation"
        columns: [Feature Set, LOGO F1, Δ]
        rows:
          - [7-feature (default), 0.798, "—"]
          - [7-feature + LD-Score, 0.803, +0.005]
          - [LD-Score only, 0.721, −0.077]
    figures_description:
      - "Fig A.6: LD-Score 的 depth-wise distribution（boxplot），展示与 entropy_mean 类似的单调递减趋势。"
    analysis: >
      LD-Score 的 marginal contribution 较小（+0.5 pp），确认 7-feature set 已捕获大部分
      depth signal。Character-level 信息主要通过 character frequency distribution 的 shift
      反映 vocabulary impoverishment，与 TTR/hapax 高度相关。

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned model 进行端到端 depth classification，
      比较 learned representations vs handcrafted features
    expected_results:
      qlora_olmo_instruct_3class_f1: 0.888
      qlora_qwen_instruct_3class_f1: 0.907
      qlora_olmo_base_3class_f1: 0.859
      qlora_qwen_base_3class_f1: 0.904
      qlora_olmo_instruct_binary_f1: 0.836
      qlora_qwen_instruct_binary_f1: 0.867
      qlora_olmo_base_binary_f1: 0.793
      qlora_qwen_base_binary_f1: 0.860
      qlora_5class_best_f1: 0.597
      seven_feature_3class_f1: 0.762
      delta_3class: "+12.6–14.5 pp"
      inference_cost_ratio: "~15×"
    result_rationale: >
      在 best 档下，QLoRA fine-tuned models 以 3-class F1 0.859–0.907 大幅超越 7-feature
      ensemble 的 0.762（+10–15 pp），证明 learned representations 能捕获 handcrafted
      features 遗漏的深层信号。但 5-class F1 仍仅 ~0.60，说明 resolution ceiling 是
      task-intrinsic 而非 feature engineering 限制。Binary F1 提升较小（0.793–0.867 vs 0.694），
      因为 binary task 的 bottleneck 在 gen-1/gen-2+ 边界，learned features 也难以完全突破。
      Instruct model 意外地与 base model 表现接近甚至略优（OLMo instruct 0.888 vs base 0.859），
      因为 QLoRA 的端到端学习可以 bypass DDR degradation，直接从 raw text 学习 depth pattern。
      审稿人在 best 档下接受 7-feature 的定位转换：不追求绝对最优，而是
      efficiency advantage（单次 Pythia-410M forward pass vs QLoRA 推理的 ~15× 成本差距）。
    tables:
      - caption: "Table A.7: End-to-end QLoRA vs 7-feature ensemble"
        columns: [Model, Type, 3-class F1, Binary F1, 5-class F1]
        rows:
          - [Qwen3-1.7B (instruct), QLoRA, 0.907, 0.867, 0.551]
          - [OLMo-1B (instruct), QLoRA, 0.888, 0.836, 0.598]
          - [Qwen3-1.7B (base), QLoRA, 0.904, 0.860, 0.554]
          - [OLMo-1B (base), QLoRA, 0.859, 0.793, 0.540]
          - [7-feature ensemble, XGBoost, 0.762, 0.694, 0.50]
    figures_description:
      - "Fig A.7: QLoRA vs 7-feature 的 3-class/binary/5-class F1 三组 bar chart。QLoRA 在前两项优势明显，5-class 差距缩小，凸显 resolution ceiling 的 task-intrinsic 性质。"
    analysis: >
      QLoRA 的成功并不削弱 7-feature 的贡献：(1) 7-feature 提供了可解释的 DDR 框架，QLoRA 是
      black box；(2) 7-feature 的 reference model 仅 410M，QLoRA 需 1.7B+；(3) QLoRA 同样
      受 5-class ceiling 限制，确认这是 task boundary 而非 method limitation。

  - name: text_length_control
    plan_id: plan_013
    description: >
      文本长度 confound 控制：分析长度分布、length-normalized features、length-matched evaluation
    expected_results:
      length_depth_spearman_range: "[−0.066, +0.134]"
      length_is_confound: false
      normalized_ttr_trend_preserved: true
      normalized_hapax_trend_preserved: true
      normalized_rho_stronger: true
      length_matched_f1: 0.724
      unmatched_f1: 0.770
      length_matched_delta: −0.046
      dropout_short_text_bias: true
    result_rationale: >
      在 best 档下，text length 与 depth 的 Spearman ρ 在 [−0.066, +0.134] 范围内（弱相关），
      排除 length 作为主要 confound。Length-normalized features（TTR, hapax 在 fixed-length
      window 上计算）保持甚至增强了 depth 趋势（normalized ρ stronger），说明 DDR drift 不是
      length artifact。Length-matched 后 F1 从 0.770 降至 0.724（−4.6 pp），但对照实验确认
      这一 drop 来自 deconfounding 而非 sample size reduction（random subsample control 也降
      相同幅度）。Depth 增加→更多短文本 dropout 的 bias 被确认，但通过 length matching 控制后
      signal 仍然显著（0.724 >> 0.5）。审稿人在 best 档下接受 length-matched 0.724 作为
      conservative 的 deconfounded 估计。
    tables:
      - caption: "Table A.8: Length confound analysis"
        columns: [Condition, Binary F1, Δ vs unmatched]
        rows:
          - [Unmatched (full), 0.770, "—"]
          - [Length-matched, 0.724, −0.046]
          - [Random subsample control, 0.724, −0.046]
    figures_description:
      - "Fig A.8: (A) Text length distribution by depth (violin plot)。轻微右偏但大幅重叠。(B) Length-normalized vs original TTR/hapax 的 depth 趋势对比——方向一致、normalized 更陡。"
    analysis: >
      Length confound 是 reviewer 高频关注点（RC10）。−4.6 pp drop 的来源是 deconfounding
      而非信息损失，这通过 random subsample control 证实。Length-matched F1=0.724 可作为
      conservative lower bound 报告在 abstract 中。

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      添加 7B+ generator（Qwen3-8B-Base）测试 frontier scale 下的 depth signal
    expected_results:
      total_records: 4497
      unique_seeds: 995
      depth_dist: {0: 995, 1: 979, 2: 937, 3: 831, 4: 755}
      logo_6gen_avg_f1: 0.789
      qwen3_8b_held_out_f1: 0.683
      logo_5gen_baseline_f1: 0.800
      spearman_hapax: −0.558
      spearman_ttr: −0.542
      spearman_entropy_mean: −0.475
      spearman_tail_decay: −0.089
      feature_importance_top3: [hapax_ratio (0.269), entropy_mean (0.164), ttr (0.159)]
    result_rationale: >
      在 best 档下，Qwen3-8B held-out F1=0.683 低于 6-gen 平均 0.789（−10.6 pp），
      证实 larger models 产生更弱的 depth signal。物理解释：8B 模型的更高容量压缩了
      depth-wise feature margins——更强的 language model 在每步生成中保持了更接近 source
      distribution 的输出，DDR location shift 幅度减小。但 0.683 仍显著高于 random（0.5），
      且 DDR 方向一致（hapax ρ=−0.558, tail_decay ρ=−0.089 仍为 stationary）。
      审稿人在 best 档下接受 scale effect 作为 honest limitation with analysis，
      而非 fatal flaw——0.683 在 8B scale 下仍为 non-trivial signal。Depth retention
      从 d0 到 d4 降至 0.759（995→755），高 dropout 率部分解释了 F1 下降。
    tables:
      - caption: "Table 11: 6-generator LOGO with Qwen3-8B"
        columns: [Generator, LOGO F1, hapax ρ, Scale]
        rows:
          - [Pythia-1B, 0.856, −0.65, 1.0B]
          - [Qwen3-0.6B, 0.824, −0.63, 0.6B]
          - [Qwen3-1.7B, 0.805, −0.61, 1.7B]
          - [Pythia-2.8B, 0.804, −0.63, 2.8B]
          - [OLMo-2-1B, 0.764, −0.60, 1.5B]
          - [Qwen3-8B, 0.683, −0.56, 8.0B]
    figures_description:
      - "Fig 11: LOGO F1 vs model scale (log-scale X axis)。下降趋势明显但 gentle——从 0.856 (1B) 到 0.683 (8B)。对数线性拟合预测 70B scale 下 F1 ≈ 0.55–0.60。"
    analysis: >
      Scale degradation 是最重要的 scope limitation 之一。6-gen LOGO 加入 8B 后均值从 0.800
      降至 0.789，Qwen3-8B 拉低了整体。但 DDR pattern（drifting vs stationary）在 8B 下完全
      保持，说明这是 amplitude reduction 而非 qualitative change。Feature importance 排序
      不变（hapax > entropy_mean > ttr），confirmed DDR 的 cross-scale robustness。

  - name: ordinal_baseline_comparison
    plan_id: plan_015
    description: >
      关键 baseline：测试现有 detector（FastDetectGPT, Binoculars, LD-Score）的连续分数
      是否已提供 ordinal depth signal
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
      bootstrap_7feat_vs_avglogprob: {delta: 0.039, p: 0.0, significant: true}
      bootstrap_7feat_vs_fdgpt: {delta: 0.067, p: 0.0, significant: true}
      best_single_detector: "Avg-LogProb (0.765)"
      seven_feature_advantage_pp: 3.3
    result_rationale: >
      在 best 档下，7-feature ensemble（0.798）显著优于所有 single-detector baselines
      （bootstrap p=0 for all pairwise comparisons）。最强 baseline Avg-LogProb（0.765）
      差 3.3 pp，这一差距虽不大但统计显著——关键在于 7-feature 的 CI [0.786, 0.799] 与
      Avg-LogProb 的 CI [0.616, 0.820] 不重叠于下界。Avg-LogProb 的强表现说明 ordinal depth
      signal 部分可被简单的 log-probability 特征捕获（Spearman ρ=0.788），但 7-feature 通过
      组合 drifting + stationary 特征实现了更稳定的跨生成器泛化（更窄的 CI）。
      FastDetectGPT（0.627）和 Binoculars（0.579）表现较差，因为它们设计为 binary detectors，
      连续分数的 ordinal sensitivity 有限。LD-Score（0.721）居中，character-level 信息
      提供了中等 ordinal signal。审稿人在 best 档下接受 7-feature 的优势为 "modest but
      consistent"——贡献不在于绝对性能碾压，而在于 DDR 框架的可解释性和互补性。
    tables:
      - caption: "Table 5: Ordinal baseline comparison (LOGO)"
        columns: [Method, LOGO F1, 95% CI, Spearman ρ, Δ vs 7-feature]
        rows:
          - [7-feature ensemble, 0.798, "[0.786, 0.799]", "—", "—"]
          - [Avg-LogProb, 0.765, "[0.616, 0.820]", 0.788, −0.033]
          - [LD-Score, 0.721, "[0.588, 0.770]", 0.794, −0.077]
          - [FastDetectGPT, 0.627, "[0.511, 0.762]", 0.433, −0.171]
          - [Binoculars, 0.579, "[0.405, 0.664]", 0.199, −0.219]
    figures_description:
      - "Fig 5: Bootstrap distribution of LOGO F1 deltas (7-feature − each baseline)。所有 delta distributions 完全在 0 右侧，确认显著性。"
    analysis: >
      这是论文中最关键的 baseline comparison——如果 Avg-LogProb alone 达到 0.80+，7-feature
      的 contribution 就会被严重削弱。0.765 vs 0.798 的差距虽小但真实：7-feature 的优势
      集中在 cross-generator 泛化（更窄 CI）和 gen-0 discrimination（surface features 必需）。
      Binoculars 的 bug fix（denominator 从 CE(performer, obs_argmax) 改为
      CE(performer, shifted_ids)）确保了公平比较。

  # Additional experiments from registry that correspond to extensions beyond original plan

  - name: 9gen_scale_evaluation
    plan_id: exp_057
    description: >
      扩展至 9 generators（+Gemma-2-2B, Llama-3.2-3B, Mistral-7B-v0.3），
      验证 8→9 gen 的 scaling behavior
    expected_results:
      9gen_logo_3class_f1: 0.751
      9gen_logo_binary_f1: 0.666
      8gen_baseline_3class_f1: 0.770
      delta_9gen_vs_8gen: −0.019
      gemma_held_out_3class_f1: 0.628
      gemma_held_out_binary_f1: 0.440
      mistral_held_out_3class_f1: 0.605
      mistral_held_out_binary_f1: 0.633
      n_generators: 9
      n_total_rows: 42015
    result_rationale: >
      在 best 档下，9-gen LOGO 3-class F1=0.751 较 8-gen 的 0.770 降 1.9 pp，主要由
      Gemma-2-2B 的异常表现拉低（gen-1 F1=0.036）。Gemma 的异常来自其独特的 tokenizer
      （SentencePiece vs BPE）导致 reference model 特征提取偏移。Mistral-7B 的 0.605
      反映了 7B scale 的 signal compression（与 plan_014 Qwen3-8B 的 0.696 一致）。
      审稿人在 best 档下接受 Gemma anomaly 作为 honest outlier analysis（appendix 中详细
      讨论 tokenizer mismatch），8-gen 结果作为 primary metric，9-gen 作为 robustness check。
      Binary F1 0.666 是 conservative lower bound——Gemma 的 binary F1=0.440 接近 random。
    tables:
      - caption: "Table A.9: 9-generator per-generator LOGO F1"
        columns: [Generator, 3-class F1, Binary F1, Family]
        rows:
          - [Pythia-1B, 0.857, 0.724, Pythia]
          - [Qwen3-0.6B, 0.819, 0.710, Qwen]
          - [Pythia-2.8B, 0.812, 0.700, Pythia]
          - [Qwen3-1.7B, 0.811, 0.698, Qwen]
          - [OLMo-2-1B, 0.773, 0.663, OLMo]
          - [Llama-3.2-3B, 0.759, 0.680, Llama]
          - [Qwen3-8B, 0.696, 0.647, Qwen]
          - [Gemma-2-2B, 0.628, 0.440, Gemma]
          - [Mistral-7B-v0.3, 0.605, 0.633, Mistral]
    figures_description:
      - "Fig A.9: 9-gen LOGO F1 heatmap，按 family 分组。Gemma 和 Mistral 的 cold spots 醒目但其余 7 gen 一致性高。"
    analysis: >
      9-gen 是 thoroughness 的体现。Gemma anomaly 提供了 negative case study：当 tokenizer
      差异过大时，cross-model reference 特征的假设被违反。这实际上深化了 DDR 的理解——
      DDR 依赖于 reference model 与 generator 之间的 tokenizer compatibility。

  - name: ddr_causality_analysis
    plan_id: exp_058
    description: >
      DDR causality analysis: permutation importance + Granger causality + feature intervention
    expected_results:
      permutation_baseline_f1: 0.771
      drifting_avg_importance: 0.158
      stationary_avg_importance: 0.030
      drifting_stationary_ratio: 5.31
      granger_significant_features: "6/7"
      granger_nonsig_feature: entropy_min
      granger_max_delta_r2: 0.031
      granger_panel_n: 29095
      intervention_max_f1_drop: 0.020
    result_rationale: >
      在 best 档下，drifting/stationary 分离经三重 causality test 验证：(1) Permutation
      importance 5.3× gap（drifting 0.158 vs stationary 0.030）确认 drifting 特征对分类的
      贡献远超 stationary；(2) 6/7 Granger 显著（仅 entropy_min 不显著）确认 depth→feature
      的 temporal causality；(3) Feature intervention 的最大 F1 drop 仅 0.020 pp 表明
      单特征 intervention 不足以破坏分类——signal 分布在 drifting 特征组合中。
      审稿人在 best 档下将这组 causality evidence 视为 "sufficient" 而非 "mere correlation"，
      认可 DDR 作为 genuine empirical contribution 而非 vocabulary impoverishment 的重新包装。
      5.5× permutation gap + 6/7 Granger 的组合在 Findings 级别属于 strong evidence。
    tables:
      - caption: "Table 6: DDR causality analysis"
        columns: [Feature, Perm Importance, Granger sig, Category]
        rows:
          - [hapax_ratio, 0.289, "✓ (p<0.001)", Drifting]
          - [ttr, 0.168, "✓ (p<0.001)", Drifting]
          - [entropy_mean, 0.160, "✓ (p<0.001)", Drifting]
          - [entropy_std, 0.046, "✓ (p<0.05)", Stationary]
          - [entropy_max, 0.063, "✓ (p<0.01)", Stationary]
          - [entropy_min, 0.015, "✗ (p=0.12)", Stationary]
          - [tail_decay, 0.012, "✓ (p<0.05)", Stationary]
    figures_description:
      - "Fig 6: Drifting vs stationary permutation importance bar chart，两组颜色分明（蓝=drifting, 灰=stationary），5.3× gap 一目了然。"
    analysis: >
      Causality analysis 是论文从 "observation" 升级到 "empirical contribution" 的关键。
      仅报告 DDR correlation 会被审稿人视为 descriptive；加入 Granger + permutation +
      intervention 三角验证后，DDR 的 causal status 被充分支撑。entropy_min 的 Granger
      不显著实际上增强了可信度——不是所有特征都需要 causal relationship。

  - name: tost_bootstrap_stability
    plan_id: exp_059
    description: >
      TOST bootstrap 验证 stationary 特征的稳定性
    expected_results:
      n_bootstrap: 1000
      margin_d: 0.2
      entropy_max: {median_p: 0.0, rejection_rate: 1.0, median_d: 0.062}
      entropy_min: {median_p: 0.0, rejection_rate: 1.0, median_d: −0.016}
      tail_decay: {median_p: 0.0, rejection_rate: 1.0, median_d: 0.088}
      entropy_std: {median_p: 1.0, rejection_rate: 0.0, median_d: 0.458}
      stationary_features_robust: true
    result_rationale: >
      在 best 档下，TOST bootstrap 确认 3/4 stationary-candidate 特征在 d=0.2 margin 下
      统计等价于 depth-invariant（rejection rate=100%, median d<0.1）。entropy_std 被拒绝
      （median d=0.458, rejection rate=0%），因为它虽然 Spearman ρ 低（−0.12）但 effect size
      超出 equivalence margin——entropy_std 是 "weak drifter" 而非 true stationary。
      这一发现精细化了 DDR 分类：3 strong drifters (hapax, TTR, entropy_mean) +
      3 true stationary (entropy_max, entropy_min, tail_decay) + 1 intermediate (entropy_std)。
      审稿人在 best 档下接受 TOST 作为比 ρ 更严格的 stationarity test，entropy_std 的
      intermediate status 被视为 nuanced finding 而非 inconsistency。
    tables:
      - caption: "Table A.10: TOST bootstrap stationarity test"
        columns: [Feature, Median d, TOST p, Rejection Rate, Status]
        rows:
          - [entropy_max, 0.062, 0.0, 1.0, Stationary ✓]
          - [entropy_min, −0.016, 0.0, 1.0, Stationary ✓]
          - [tail_decay, 0.088, 0.0, 1.0, Stationary ✓]
          - [entropy_std, 0.458, 1.0, 0.0, "Intermediate (rejected)"]
    figures_description:
      - "Fig A.10: Bootstrap d 分布的 violin plot（4 features）。entropy_max/min/tail_decay 的分布集中在 |d|<0.2 区间内；entropy_std 的分布完全在 0.2 之外。"
    analysis: >
      TOST bootstrap 为 DDR 分离提供了比 Spearman ρ 更严格的统计基础。entropy_std 的
      intermediate status 实际上加强了论文的 nuance——不是简单的二分法，而是一个连续谱，
      论文选择在 practical level 上维持 drifting/stationary 二分以保持 clarity。

  - name: instruct_model_degradation
    plan_id: exp_052-054
    description: >
      三个 instruct model（Qwen3-1.7B, OLMo-2-1B, Llama-3.2-3B）的 DDR 退化分析
    expected_results:
      qwen_instruct_logo_binary: 0.658
      olmo_instruct_within_3class: 0.575
      llama_instruct_3class: 0.544
      qwen_base_logo_binary: 0.821
      delta_logo_binary_qwen: −0.163
      features_reversed_olmo: "6/7"
      features_reversed_llama: "3/7 (entropy_mean, entropy_std, tail_decay)"
      spearman_direction_reversal: true
    result_rationale: >
      在 best 档下，instruct model 的 DDR 退化被系统性确认：LOGO binary F1 从 base 0.821
      降至 instruct 0.658（Qwen, −16.3 pp），OLMo instruct 的 6/7 features Spearman 方向
      反转（ρ 从负变正），说明 instruction tuning 的 length regulation 和 format constraints
      根本性地改变了 depth-feature relationship。物理解释：alignment 训练强制模型在所有
      depth 上产生相似的 token distribution（format compliance），压缩了 DDR 依赖的
      distributional variation。这是 base-model-only scope 的核心证据。审稿人在 best 档下
      将诚实报告视为 strength：不隐藏 limitation，反而深入分析其 mechanism（feature reversal
      + format compression hypothesis）。0 instruct scope penalty。
    tables:
      - caption: "Table 12: Instruct vs base model comparison"
        columns: [Model, Type, LOGO Binary F1, 3-class F1, Features Reversed]
        rows:
          - [Qwen3-1.7B, Base, 0.821, 0.769, 0]
          - [Qwen3-1.7B, Instruct, 0.658, 0.543, "ρ direction"]
          - [OLMo-2-1B, Base, 0.845, 0.754, 0]
          - [OLMo-2-1B, Instruct, 0.813, 0.575, "6/7"]
          - [Llama-3.2-3B, Base, 0.849, 0.742, 0]
          - [Llama-3.2-3B, Instruct, 0.838, 0.544, "3/7"]
    figures_description:
      - "Fig 12: Base vs instruct 的 feature-depth Spearman ρ 对比（radar chart 或 parallel coordinates）。Base 的 drifting features 一致负向；instruct 的方向混乱甚至反转。"
    analysis: >
      Instruct 退化的 mechanism analysis（feature reversal, not just signal weakening）是
      超越简单 "instruct doesn't work" 报告的 value-add。Format compliance hypothesis 可
      在 future work 中通过 constrained decoding 实验验证。

  - name: temperature_sensitivity
    plan_id: exp_048-050
    description: >
      Temperature sensitivity curve (t=0.5, 0.7, 0.9, 1.0) + cross-temperature transfer
    expected_results:
      t05_logo_binary_f1: 0.814
      t07_logo_binary_f1: 0.694
      t09_logo_binary_f1: 0.480
      within_t07_binary: 0.947
      cross_t07_to_t10_binary: 0.900
      cross_t07_to_t10_qwen_only_binary: 0.757
      cross_t07_to_t10_qwen_only_3class: 0.458
      entropy_mean_rho_t05: −0.584
      entropy_mean_rho_t07: −0.600
      entropy_mean_rho_t09: −0.302
    result_rationale: >
      在 best 档下，DDR 在 t∈[0.5, 0.7] 范围内稳定（≤1 pp degradation from default），
      t=0.9 大幅退化（−21.4 pp），t=1.0 进一步恶化。Cross-temperature transfer 严重不对称：
      t=0.7→t=1.0 降 16.9 pp（Qwen-only binary），t=1.0→t=0.7 仅降微弱。物理解释：
      高温增大 sampling noise，entropy_mean 的 depth-wise drift 被 within-depth variance
      淹没（ρ 从 −0.60 降至 −0.002 at t=1.0）。审稿人在 best 档下接受 t∈[0.5, 0.9] 为
      reliable range，t=1.0 degradation 作为 transparent limitation。
    tables:
      - caption: "Table A.4: Temperature sensitivity"
        columns: [Temperature, Within-CV Binary F1, LOGO Binary F1, entropy_mean ρ]
        rows:
          - [0.5, 0.843, 0.814, −0.584]
          - [0.7 (default), 0.947, 0.694, −0.600]
          - [0.9, 0.582, 0.480, −0.302]
    figures_description:
      - "Fig A.4: Temperature curve。X 轴温度，Y 轴 binary F1 + entropy_mean ρ（双轴）。0.5–0.7 plateau，0.9+ cliff。"
    analysis: >
      Temperature sensitivity 直接关联 DDR 的 location-shift 解释：高温增大了每步采样的
      distributional noise，削弱了 deterministic drift component。t=0.5 下 signal 更强
      因为低温采样更 deterministic，location shift 更 clean。

  - name: independent_seed_validation
    plan_id: exp_051
    description: >
      Independent seed validation：不同生成器使用完全独立的 seed 集
    expected_results:
      pythia_to_olmo_binary_f1: 0.695
      olmo_to_pythia_binary_f1: 0.666
      avg_binary_f1: 0.680
      shared_seed_logo_ref: 0.694
      delta_vs_shared: −0.014
    result_rationale: >
      在 best 档下，independent seed 的 avg binary F1=0.680 vs shared seed LOGO 0.694
      仅差 1.4 pp，确认 shared seed 不构成显著 leakage。这排除了 "performance inflated by
      seed sharing" 的 critique。1.4 pp 差异在 bootstrap CI 内，不具统计显著性。
      方向不对称（Pythia→OLMo 0.695 vs OLMo→Pythia 0.666）反映了 OLMo 作为 test set
      更难分类（与 LOGO 结果一致）。
    tables:
      - caption: "Table A.11: Independent vs shared seed evaluation"
        columns: [Condition, Binary F1, Δ]
        rows:
          - [Shared seed LOGO, 0.694, "—"]
          - [Independent seed (Pythia→OLMo), 0.695, +0.001]
          - [Independent seed (OLMo→Pythia), 0.666, −0.028]
          - [Independent seed avg, 0.680, −0.014]
    figures_description: []
    analysis: >
      Independent seed validation 关闭了 seed sharing leakage 的替代假说。
      1.4 pp 差异可归因于 generator-specific difficulty 差异而非 leakage。

  - name: topic_drift_control
    plan_id: review-exp-b
    description: >
      Semantic similarity analysis：控制 topic drift 作为 depth signal 的 confound
    expected_results:
      sim_0_to_1: 0.622
      sim_1_to_2: 0.683
      sim_2_to_3: 0.801
      sim_3_to_4: 0.859
      shape_entropy_std_rho: −0.164
      shape_tail_decay_rho: 0.068
      drifting_entropy_mean_rho: −0.286
    result_rationale: >
      在 best 档下，semantic similarity 随 depth 递增（0.622→0.859），表明 deeper generation
      趋向 semantic convergence（repetition/narrowing）。但 DDR feature-depth correlations
      在控制 semantic similarity 后仍保持方向和显著性，说明 DDR 不仅仅是 topic drift 的
      proxy。Shape features 与 semantic similarity 的 correlation 极弱（|ρ|<0.17），
      进一步确认 shape stationarity 独立于 topic dynamics。审稿人在 best 档下接受 topic
      drift 分析为 adequate confound control。
    tables:
      - caption: "Table A.12: Semantic similarity by depth transition"
        columns: [Transition, Mean Sim, Std]
        rows:
          - [depth 0→1, 0.622, 0.165]
          - [depth 1→2, 0.683, 0.184]
          - [depth 2→3, 0.801, 0.201]
          - [depth 3→4, 0.859, 0.190]
    figures_description:
      - "Fig A.12: Semantic similarity 随 depth 的递增趋势（boxplot）。递增但方差大，视觉上与 DDR drifting 方向相反（drifting 递减, similarity 递增）。"
    analysis: >
      Semantic convergence 与 vocabulary impoverishment 是相关但不同的现象：text 变得
      semantically more similar（topic narrowing）但 statistically less diverse（DDR drift）。
      两者的解耦证明 DDR 不是 topic drift 的简单 proxy。

  - name: multi_detector_ensemble
    plan_id: review-exp-a
    description: >
      Multi-detector ensemble（4 detectors + surface features）vs 7-feature baseline
    expected_results:
      four_det_surface_3class_f1: 0.795
      four_det_surface_binary_f1: 0.708
      seven_feature_3class_f1: 0.774
      seven_feature_binary_f1: 0.705
      delta_3class: +0.021
      delta_binary: +0.003
      inference_cost_ratio: 2.4
      gpu_memory_ratio: 3.2
    result_rationale: >
      在 best 档下，multi-detector ensemble 以 +2.1 pp (3-class) 和 +0.3 pp (binary)
      微弱优于 7-feature，但代价是 2.4× inference cost 和 3.2× GPU memory。Binary F1
      差距仅 0.3 pp（essentially equivalent），因为 binary task 的 gen-1/gen-2+ 边界是
      intrinsic bottleneck，更多 features 无法突破。7-feature 的 efficiency advantage
      在 best 档下被审稿人接受为合理的 positioning：not absolute best, but best
      cost-performance tradeoff。
    tables:
      - caption: "Table A.1: Multi-detector ensemble comparison"
        columns: [Model, 3-class F1, Binary F1, Cost Ratio]
        rows:
          - [7-feature ensemble, 0.774, 0.705, 1.0×]
          - [4-det + surface, 0.795, 0.708, 2.4×]
    figures_description: []
    analysis: >
      Multi-detector ensemble 的 marginal gains 进一步验证了 7-feature 的 cost-effectiveness。
      3-class 差距 2.1 pp 大于 binary 0.3 pp，因为额外 detector features 主要帮助
      gen-0/gen-1 区分（通过 detector-specific calibration），对 gen-1/gen-2+ boundary 几乎无效。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd6f8a8-492e-45dc-b720-d7c298fa059b",
  "isSidechain": false,
  "requestId": "req_011CbDdfiPgh2HVBKNEVbYnX",
  "type": "assistant",
  "uuid": "28401b7b-113a-468c-8ba0-31bc769d6618",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRHmViqtf7t95euAm5NViw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 36077,
      "output_tokens": 20721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20721,
          "cache_read_input_tokens": 36077,
          "cache_creation_input_tokens": 320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 320
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：3.5 Borderline Conference — 所有三个 Claim 在审稿中站住脚，DDR 被认可为 genuine empirical contribution，论文整体完成度被视为 Findings 上限 核心假设：['DDR 的 drifting/stationary 分离被视为 non-tr…",
  "leafUuid": "28401b7b-113a-468c-8ba0-31bc769d6618",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth fingerprinting evaluation—9 models, causality analysis, downstream utility",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：3.5 Borderline Conference — 所有三个 Claim 在审稿中站住脚，DDR 被认可为 genuine empirical contribution，论文整体完成度被视为 Findings 上限 核心假设：['DDR 的 drifting/stationary 分离被视为 non-tr…",
  "leafUuid": "28401b7b-113a-468c-8ba0-31bc769d6618",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth fingerprinting evaluation—9 models, causality analysis, downstream utility",
  "sessionId": "b6a50125-a340-49f6-a219-a467368d895d"
}
```

---
