# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有核心假设成立；DDR 在 8+ generators / 5 families 上鲁棒，7-feature 优势显著，negative findin

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/63de68ac-a99b-46a9-afd5-e6a3b61abf12.jsonl`
- **Structured JSON:** [`887df6a25870779230af.json`](../../sessions/88/887df6a25870779230af.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T23:29:38.500Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T23:29:38.500Z",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有核心假设成立；DDR 在 8+ generators / 5 families 上鲁棒，7-feature 优势显著，negative finding 清晰。论文按原 framing 提交 ARR。\n核心假设：['DDR 二分法成立：drifting 三特征 (hapax, TTR, entropy_mean) |ρ|≥0.55，stationary 二特征 (tail_decay, entropy_max) |ρ|<0.10；entropy_std 归为 weakly drifting 不影响主叙事', '7-feature 在扩展 generator set 下仍显著优于 avg_logprob (≥3pp LOGO binary, bootstrap p<0.01)', 'Cross-model chains 验证 heterogeneity amplification (binary F1≥0.76)', '8-gen LOGO binary F1 ≥ 0.69 稳定，per-gen 方差 < 10pp', '14B scale DDR 模式定性不变（drifting/stationary 分组一致，|ρ| 仅弱衰减）', 't∈[0.5,0.7] 可靠 (≤2pp 降幅)；t≥0.9 诚实标为 scope boundary 不被 reviewer 视为致命缺陷', 'Gemma gen-1 异常为孤立架构效应，不泛化至其他 generator']\n关键指标范围：{'logo_binary_f1_8gen': [0.69, 0.72], 'logo_binary_f1_9gen': [0.66, 0.69], 'lofo_binary_f1': [0.68, 0.7], 'cross_model_binary_f1': [0.76, 0.83], 'ddr_drifting_rho_abs_min': [0.55, 0.65], 'ddr_stationary_rho_abs_max': [0.04, 0.1], 'seven_feat_minus_best_single_pp': [3.0, 5.0], 'scale_8b_logo_binary_f1': [0.65, 0.7], 'llm_rephrase_drop_pp': [3.0, 5.0]}\n叙事方向：原始 framing 完全成立。DDR 以 drifting/stationary 二分法表述（entropy_std 在正文中归为 intermediate，不破坏主叙事）。三条 claim 均有充分实验支撑：(1) depth discriminability 以 LOGO binary F1=0.694 为 headline，LOFO 和 cross-model 验证泛化性；(2) DDR 跨 reference model (3 families) 和 generator family (5 families) 稳健，TOST 确认 shape feature stationarity；(3) negative downstream finding 以 TOST ±2% margin 确认。Scope limitations (base-only, t≤0.7, ≤14B) 诚实报告但不动摇核心 contribution。可直接提交 ARR。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_logo_f1: 0.7879\n    overall_ci95:\n    - 0.783\n    - 0.7929\n    spearman_entropy_max: 0.0503\n    spearman_entropy_min: -0.4061\n    spearman_hapax: -0.6467\n    spearman_ttr: -0.6302\n    spearman_entropy_mean: -0.6098\n    spearman_entropy_std: -0.1996\n    spearman_tail_decay: -0.0403\n- exp_id: plan-010-robustness\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_binary_f1: 0.695\n    5pct_binary_f1: 0.65\n    10pct_binary_f1: 0.614\n    20pct_binary_f1: 0.591\n    5pct_drop: -0.046\n    10pct_drop: -0.081\n    20pct_drop: -0.104\n- exp_id: plan-010-llm-rephrase\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_binary_f1: 0.6918\n    original_binary_ci:\n    - 0.6749\n    - 0.7067\n    original_multiclass_f1: 0.7385\n    original_multiclass_ci:\n    - 0.7269\n    - 0.7496\n    rephrased_binary_f1: 0.6471\n    rephrased_binary_ci:\n    - 0.6308\n    - 0.6619\n    rephrased_multiclass_f1: 0.6672\n    rephrased_multiclass_ci:\n    - 0.6548\n    - 0.6796\n    binary_drop: -0.0447\n    multiclass_drop: -0.0713\n    edit_distance_ratio: 0.5071\n    avg_sentences_replaced: 1.69\n    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\n    bugs_fixed:\n    - binary_task_gen1_vs_gen2+\n    - 3class_mapping\n    - tail_decay_rank100-1000\n- exp_id: plan-008-seed-stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_complexity_binary: 0.685\n    medium_binary: 0.695\n    high_complexity_binary: 0.695\n    low_complexity_multi: 0.772\n    medium_multi: 0.778\n    high_complexity_multi: 0.779\n    max_diff_binary_pp: 1.06\n    max_diff_multiclass_pp: 0.68\n    conclusion_label: seed_independent\n- exp_id: multi-domain-seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7459\n    news_binary_ci:\n    - 0.726\n    - 0.764\n    news_multiclass_f1: 0.6516\n    academic_binary_f1: 0.7386\n    academic_binary_ci:\n    - 0.72\n    - 0.757\n    academic_multiclass_f1: 0.6223\n    code_binary_f1: 0.7535\n    code_binary_ci:\n    - 0.737\n    - 0.77\n    code_multiclass_f1: 0.6344\n    wikipedia_baseline_binary_f1: 0.8148\n    wikipedia_baseline_multiclass_f1: 0.8632\n    max_gap_vs_wiki_pp: 7.62\n    worst_domain: academic\n    best_domain: code\n    conclusion_label: domain_independent\n- exp_id: exp_047_multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7119\n    news_binary_ci:\n    - 0.6898\n    - 0.7332\n    news_3class_f1: 0.7149\n    academic_binary_f1: 0.6279\n    academic_binary_ci:\n    - 0.6027\n    - 0.6515\n    academic_3class_f1: 0.6564\n    code_binary_f1: 0.6872\n    code_binary_ci:\n    - 0.6641\n    - 0.71\n    code_3class_f1: 0.6729\n    overall_binary_f1: 0.6757\n    overall_3class_f1: 0.6814\n    delta_vs_t10_news: -0.034\n    delta_vs_t10_academic: -0.1107\n    delta_vs_t10_code: -0.0663\n- exp_id: multi_domain_t07\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_048_cross_temp_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    6gen_logo:\n      within_0.7_binary: 0.9471\n      within_0.7_3class: 0.7888\n      cross_0.7to1.0_binary: 0.9001\n      cross_0.7to1.0_3class: 0.7225\n      within_1.0_binary: 0.9107\n      within_1.0_3class: 0.7257\n      cross_1.0to0.7_binary: 0.9581\n      cross_1.0to0.7_3class: 0.7913\n      caveat: Only Qwen3-1.7B differs between conditions; 5/6 generators share data\n    qwen_only:\n      within_0.7_binary: 0.9262\n      within_0.7_binary_ci:\n      - 0.916\n      - 0.935\n      within_0.7_3class: 0.769\n      within_0.7_3class_ci:\n      - 0.756\n      - 0.781\n      cross_0.7to1.0_binary: 0.7574\n      cross_0.7to1.0_binary_ci:\n      - 0.745\n      - 0.77\n      cross_0.7to1.0_3class: 0.4581\n      cross_0.7to1.0_3class_ci:\n      - 0.445\n      - 0.472\n      within_1.0_binary: 0.8248\n      within_1.0_binary_ci:\n      - 0.81\n      - 0.838\n      within_1.0_3class: 0.5738\n      within_1.0_3class_ci:\n      - 0.56\n      - 0.588\n      cross_1.0to0.7_binary: 0.9443\n      cross_1.0to0.7_binary_ci:\n      - 0.936\n      - 0.953\n      cross_1.0to0.7_3class: 0.6014\n      cross_1.0to0.7_3class_ci:\n      - 0.593\n      - 0.611\n      delta_0.7train_binary_pp: -16.9\n      delta_0.7train_3class_pp: -31.1\n      delta_1.0train_binary_pp: 12\n      delta_1.0train_3class_pp: 2.8\n      asymmetric_transfer: true\n- exp_id: exp_049_temp_curve_t05\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 4708\n    skipped: 113\n    seeds: 995\n    model: pythia-2.8b\n    temperature: 0.5\n    top_p: 0.9\n    within_cv_binary_f1: 0.8432\n    within_cv_binary_ci:\n    - 0.8301\n    - 0.8558\n    logo_binary_f1: 0.8136\n    logo_binary_ci:\n    - 0.7984\n    - 0.8282\n    entropy_mean_rho: -0.5844\n- exp_id: exp_050_temp_curve_t09\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    records: 4536\n    model: pythia-2.8b\n    temperature: 0.9\n    top_p: 0.9\n    within_cv_binary_f1: 0.5821\n    within_cv_binary_ci:\n    - 0.5655\n    - 0.5985\n    logo_binary_f1: 0.4804\n    logo_binary_ci:\n    - 0.4645\n    - 0.4976\n    entropy_mean_rho: -0.3016\n    delta_vs_t07_cv: -0.157\n    delta_vs_t07_logo: -0.259\n- exp_id: exp_051_independent_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_to_olmo_binary_f1: 0.6945\n    pythia_to_olmo_ci:\n    - 0.6727\n    - 0.7167\n    olmo_to_pythia_binary_f1: 0.666\n    olmo_to_pythia_ci:\n    - 0.6429\n    - 0.6893\n    avg_binary_f1: 0.6803\n    shared_seed_logo_ref: 0.694\n    delta_vs_shared: -0.014\n- exp_id: exp_052_instruct_qwen3_1_7b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8753\n    within_binary_ci:\n    - 0.8667\n    - 0.8837\n    within_3class_f1: 0.7324\n    within_3class_ci:\n    - 0.7195\n    - 0.745\n    base_binary_f1: 0.8614\n    base_3class_f1: 0.769\n    logo_instruct_binary: 0.658\n    logo_instruct_3class: 0.543\n    logo_base_binary: 0.821\n    logo_base_3class: 0.802\n    gen1_f1_instruct: 0.438\n    gen1_f1_base: 0.579\n    spearman_direction: reversed (instruct ρ>0, base ρ<0)\n    delta_within_binary: 0.014\n    delta_within_3class: -0.037\n    delta_logo_binary: -0.163\n- exp_id: exp_053_instruct_olmo2_1b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8131\n    within_binary_ci:\n    - 0.8012\n    - 0.8251\n    within_3class_f1: 0.5748\n    within_3class_ci:\n    - 0.5605\n    - 0.5897\n    base_binary_f1: 0.8454\n    base_3class_f1: 0.7538\n    gen1_f1_instruct: 0.256\n    gen1_f1_base: 0.523\n    delta_within_binary: -0.032\n    delta_within_3class: -0.179\n    spearman_instruct:\n      entropy_mean: 0.482\n      entropy_std: 0.296\n      entropy_min: 0.08\n      entropy_max: 0.306\n      tail_decay: 0.228\n      ttr: 0.006\n      hapax_ratio: 0.025\n    spearman_base:\n      entropy_mean: -0.639\n      entropy_std: -0.296\n      entropy_min: -0.387\n      entropy_max: 0.067\n      tail_decay: -0.141\n      ttr: -0.7\n      hapax_ratio: -0.712\n    features_reversed: 6/7\n    model_used: allenai/OLMo-2-0425-1B-Instruct\n- exp_id: exp_054_instruct_llama3_2_3b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    instruct_binary_f1: 0.8381\n    instruct_binary_ci:\n    - 0.828\n    - 0.847\n    instruct_3class_f1: 0.5437\n    instruct_3class_ci:\n    - 0.53\n    - 0.558\n    base_binary_f1: 0.8488\n    base_3class_f1: 0.7424\n    rho_instruct_entropy_mean: 0.2299\n    rho_instruct_entropy_std: 0.2623\n    rho_instruct_entropy_min: -0.0027\n    rho_instruct_entropy_max: 0.2036\n    rho_instruct_tail_decay: 0.1198\n    rho_instruct_ttr: -0.1411\n    rho_instruct_hapax_ratio: -0.1157\n    rho_base_entropy_mean: -0.627\n    rho_base_ttr: -0.6856\n    rho_base_hapax_ratio: -0.6975\n    direction_reversals: 3\n    reversed_features:\n    - entropy_mean\n    - entropy_std\n    - tail_decay\n    data_count: 4974\n- exp_id: exp_055_qlora_olmo_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8881\n    macro_f1_3class_std: 0.0071\n    macro_f1_5class: 0.5976\n    macro_f1_5class_std: 0.0046\n    binary_f1: 0.8363\n    binary_f1_std: 0.0096\n    n_samples: 4429\n    runtime_seconds: 1689.7\n- exp_id: exp_056_qlora_qwen_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.9066\n    macro_f1_3class_std: 0.0082\n    macro_f1_5class: 0.5514\n    macro_f1_5class_std: 0.0031\n    binary_f1: 0.8672\n    binary_f1_std: 0.0137\n    n_samples: 4963\n    runtime_seconds: 1880.5\n- exp_id: exp_055b_qlora_olmo_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8588\n    macro_f1_3class_std: 0.0036\n    macro_f1_5class: 0.5398\n    macro_f1_5class_std: 0.015\n    binary_f1: 0.7925\n    binary_f1_std: 0.0097\n    n_samples: 2379\n    runtime_seconds: 911.7\n    note: completed before kill signal\n- exp_id: exp_056b_qlora_qwen_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.904\n    macro_f1_3class_std: 0.0094\n    macro_f1_5class: 0.5544\n    macro_f1_5class_std: 0.0068\n    binary_f1: 0.8597\n    binary_f1_std: 0.0123\n    n_samples: 2291\n    runtime_seconds: 880.9\n    note: completed before kill signal\n- exp_id: exp_057_scale_9gen_logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: superseded by exp_057 (rerun with fixed Gemma data)\n    first_run_3class_f1: 0.7516\n    first_run_binary_f1: 0.6842\n    see_exp_057_for_final: true\n- exp_id: exp_058_ddr_causality\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    permutation_baseline_f1: 0.7714\n    drifting_avg_importance: 0.1578\n    stationary_avg_importance: 0.0297\n    drifting_stationary_ratio: 5.31\n    granger_significant_features: 6/7\n    granger_max_delta_r2: 0.031\n    granger_max_delta_r2_feature: entropy_std\n    granger_nonsig_feature: entropy_min\n    granger_panel_n: 29095\n    intervention_max_f1_drop: 0.0203\n    intervention_max_feature: entropy_max\n    intervention_min_f1_drop: 0.0061\n- exp_id: exp_059_tost_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_bootstrap: 1000\n    seed: 42\n    margin_d: 0.2\n    entropy_max:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.062\n      d_ci:\n      - 0.037\n      - 0.088\n    entropy_min:\n      median_p: 0\n      rejection_rate: 1\n      median_d: -0.016\n      d_ci:\n      - -0.042\n      - 0.011\n    tail_decay:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.088\n      d_ci:\n      - 0.065\n      - 0.111\n    entropy_std:\n      median_p: 1\n      rejection_rate: 0\n      median_d: 0.458\n      d_ci:\n      - 0.435\n      - 0.479\n    stationary_features_robust: true\n- exp_id: exp_057\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    9gen_logo_3class_f1: 0.751\n    9gen_logo_binary_f1: 0.6661\n    8gen_baseline_3class_f1: 0.7698\n    delta_9gen_vs_8gen: -0.0188\n    n_total_rows: 42015\n    n_generators: 9\n    qwen3_8b_3class_f1: 0.6955\n    qwen3_8b_binary_f1: 0.6468\n    gemma_2_2b_3class_f1: 0.6279\n    gemma_2_2b_binary_f1: 0.4402\n    per_gen_3class_f1:\n      pythia-1b: 0.8571\n      qwen3-0.6b: 0.8185\n      pythia-2.8b: 0.8117\n      qwen3-1.7b: 0.8114\n      olmo-2-1b: 0.7732\n      llama-3.2-3b: 0.7591\n      qwen3-8b: 0.6955\n      gemma-2-2b: 0.6279\n      mistral-7b-v0.3: 0.6045\n    tail_decay_consistency: VERIFIED_all_9gen_logprob_slope\n    data_source: features_9gen.csv (42015 rows, Gemma fixed)\n- exp_id: exp_060_14b_ddr_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 2229\n    n_seeds: 498\n    depth_distribution:\n      '0': 498\n      '1': 488\n      '2': 466\n      '3': 414\n      '4': 363\n    entropy_mean:\n      rho: -0.3877\n      d: 0.7765\n      group: drifting\n    entropy_std:\n      rho: -0.0557\n      d: -0.0223\n      group: stationary\n    entropy_max:\n      rho: 0.0791\n      d: -0.1717\n      group: stationary\n    entropy_min:\n      rho: -0.2471\n      d: -0.1365\n      group: stationary\n    ttr:\n      rho: -0.4916\n      d: 1.0913\n      group: drifting\n    hapax_ratio:\n      rho: -0.5065\n      d: 1.1245\n      group: drifting\n    tail_decay:\n      rho: -0.0637\n      d: 0.1356\n      group: stationary\n    ddr_pattern_match: true\n- exp_id: exp_061_instruct_ref_ddr\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwen_instruct:\n      base_ref_rho_entropy_mean: 0.478\n      instruct_ref_rho_entropy_mean: 0.221\n      base_ref_d_entropy_mean: 1.981\n      instruct_ref_d_entropy_mean: 1.022\n    olmo_instruct:\n      base_ref_rho_entropy_mean: 0.482\n      instruct_ref_rho_entropy_mean: -0.113\n      base_ref_d_entropy_mean: 1.33\n      instruct_ref_d_entropy_mean: 0.017\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T23:29:38.504Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T23:29:38.504Z",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T23:29:38.521Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有核心假设成立；DDR 在 8+ generators / 5 families 上鲁棒，7-feature 优势显著，negative finding 清晰。论文按原 framing 提交 ARR。
核心假设：['DDR 二分法成立：drifting 三特征 (hapax, TTR, entropy_mean) |ρ|≥0.55，stationary 二特征 (tail_decay, entropy_max) |ρ|<0.10；entropy_std 归为 weakly drifting 不影响主叙事', '7-feature 在扩展 generator set 下仍显著优于 avg_logprob (≥3pp LOGO binary, bootstrap p<0.01)', 'Cross-model chains 验证 heterogeneity amplification (binary F1≥0.76)', '8-gen LOGO binary F1 ≥ 0.69 稳定，per-gen 方差 < 10pp', '14B scale DDR 模式定性不变（drifting/stationary 分组一致，|ρ| 仅弱衰减）', 't∈[0.5,0.7] 可靠 (≤2pp 降幅)；t≥0.9 诚实标为 scope boundary 不被 reviewer 视为致命缺陷', 'Gemma gen-1 异常为孤立架构效应，不泛化至其他 generator']
关键指标范围：{'logo_binary_f1_8gen': [0.69, 0.72], 'logo_binary_f1_9gen': [0.66, 0.69], 'lofo_binary_f1': [0.68, 0.7], 'cross_model_binary_f1': [0.76, 0.83], 'ddr_drifting_rho_abs_min': [0.55, 0.65], 'ddr_stationary_rho_abs_max': [0.04, 0.1], 'seven_feat_minus_best_single_pp': [3.0, 5.0], 'scale_8b_logo_binary_f1': [0.65, 0.7], 'llm_rephrase_drop_pp': [3.0, 5.0]}
叙事方向：原始 framing 完全成立。DDR 以 drifting/stationary 二分法表述（entropy_std 在正文中归为 intermediate，不破坏主叙事）。三条 claim 均有充分实验支撑：(1) depth discriminability 以 LOGO binary F1=0.694 为 headline，LOFO 和 cross-model 验证泛化性；(2) DDR 跨 reference model (3 families) 和 generator family (5 families) 稳健，TOST 确认 shape feature stationarity；(3) negative downstream finding 以 TOST ±2% margin 确认。Scope limitations (base-only, t≤0.7, ≤14B) 诚实报告但不动摇核心 contribution。可直接提交 ARR。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-fingerprint
venue: emnlp-2026

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
- exp_id: exp_060_14b_ddr_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_samples: 2229
    n_seeds: 498
    depth_distribution:
      '0': 498
      '1': 488
      '2': 466
      '3': 414
      '4': 363
    entropy_mean:
      rho: -0.3877
      d: 0.7765
      group: drifting
    entropy_std:
      rho: -0.0557
      d: -0.0223
      group: stationary
    entropy_max:
      rho: 0.0791
      d: -0.1717
      group: stationary
    entropy_min:
      rho: -0.2471
      d: -0.1365
      group: stationary
    ttr:
      rho: -0.4916
      d: 1.0913
      group: drifting
    hapax_ratio:
      rho: -0.5065
      d: 1.1245
      group: drifting
    tail_decay:
      rho: -0.0637
      d: 0.1356
      group: stationary
    ddr_pattern_match: true
- exp_id: exp_061_instruct_ref_ddr
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    qwen_instruct:
      base_ref_rho_entropy_mean: 0.478
      instruct_ref_rho_entropy_mean: 0.221
      base_ref_d_entropy_mean: 1.981
      instruct_ref_d_entropy_mean: 1.022
    olmo_instruct:
      base_ref_rho_entropy_mean: 0.482
      instruct_ref_rho_entropy_mean: -0.113
      base_ref_d_entropy_mean: 1.33
      instruct_ref_d_entropy_mean: 0.017

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
  "promptId": "9c28f55d-69f6-470e-be92-8830a5b73389",
  "type": "user",
  "uuid": "03cf7e29-bb64-4430-aced-dba3c2a98198",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T23:29:38.520Z_

```json
{
  "parentUuid": "03cf7e29-bb64-4430-aced-dba3c2a98198",
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
  "uuid": "d905fc60-21c9-4be8-be21-5782669b8bab",
  "timestamp": "2026-05-20T23:29:38.520Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T23:29:38.520Z_

```json
{
  "parentUuid": "d905fc60-21c9-4be8-be21-5782669b8bab",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "09970dfb-e496-480d-bc18-dcaa7511e12a",
  "timestamp": "2026-05-20T23:29:38.520Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立；DDR 在 8+ generators / 5 families 上鲁棒，7-feature 优势显著，negative finding 清晰。论文按原 framing 提交 ARR。 核心假设：['DDR 二分法成立：drifting 三特征 (hapax, TTR, entropy_me…",
  "leafUuid": "09970dfb-e496-480d-bc18-dcaa7511e12a",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate DDR robustness and depth discriminability across 8+ generators",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12"
}
```

---

### Assistant

_source line 8 · 2026-05-20T23:36:02.973Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all "planned" experiments in the experiment_plan, under the "best" tier assumptions. I need to read through the experiment plan, understand the best tier definition, and for each planned experiment, predict detailed results with rationales.

Let me first understand what experiments are still "planned" (not yet done). Looking at the experiment_plan:

1. plan_001 - feature_ablation_and_trend - status: planned (but registry shows plan-001 and plan-001-fix as DONE)


2. plan_002 - cross_generator_evaluation - status: planned (but registry shows plan-002 as DONE)
3. plan_003 - cross_family_reference_model - status: planned (but registry shows plan-003 as DONE)
4. plan_004 - downstream_utility - status: planned (but registry shows plan-004-v2 as DONE)
5. plan_005 - prompt_type_comparison - status: planned (but registry shows plan-005 as DONE)
6. plan_006 - paraphrastic_comparison - status: planned (not in registry as done)
7. plan_007 - cross_model_chains - status: planned (not in registry as done directly)
8. plan_008 - multi_domain_seeds - status: planned (but registry shows multi-domain-seeds as DONE)
9. plan_009 - finer_grained_ordinal - status: planned (not in registry as done)
10. plan_010 - human_edit_robustness - status: planned (but registry shows plan-010-robustness and plan-010-llm-rephrase as DONE)
11. plan_011 - ld_score_feature - status: planned (not directly in registry)
12. plan_012 - end_to_end_classifier - status: planned (not directly, but exp_055/056 qlora experiments are done)
13. plan_013 - text_length_control - status: planned (but registry shows plan-013 as DONE)
14. plan_014 - large_scale_generator - status: planned (but registry shows plan-014 as DONE)
15. plan_015 - continuing through the remaining planned experiments

...

I'm realizing the user wants me to generate predicted data for every experiment marked as "planned" in the experiment_plan, treating this as a forecasting exercise under the best-case scenario. Even though many of these experiments have already been completed in the registry, the experiment_plan still lists them all as planned, so I need to predict what the results would look like if everything goes optimally. Now I'm looking at the performance metric ranges for the best tier across all the key indicators, and I need to construct the YAML output by going through each of the 15 planned experiments and generating predicted results based on these benchmarks. Generating YAML output... Looking at the registry results for plans 011 through 014, I'm seeing that LD-Score provides some signal but doesn't outperform the 7-feature approach, QLoRA achieves better F1 scores at significantly higher computational cost, length isn't a confounding factor in the data, and the large-scale generator with Qwen 3.8B reaches around 0.68 F1 on held-out data.

For plan 015, the seven-feature baseline achieves 0.798 F1 with an average log probability of 0.7653, showing a 3.3 percentage point improvement over the best single feature. Now I need to reconcile the registry's mostly 3-class macro F1 values with the binary F1 metrics that are central to the analysis, and I'm checking what binary F1 scores are actually available—the overall logo F1 from the review experiment comes in at 0.7879.

Looking at the 9-generation experiment, the binary F1 is 0.6661 while the 8-generation baseline shows 0.7698 for 3-class. The paper framing gives me LOGO binary F1 of 0.694 with confidence bounds [0.688, 0.700] and LOFO binary F1 of 0.686. These align well with the best tier expectations: 8-gen LOGO should fall in [0.69, 0.72] and 9-gen in [0.66, 0.69], so the 0.694 value fits perfectly. Now I'm ready to construct the comprehensive YAML output.

For each experimental plan, I need to track specific metrics: plan_001 covers feature ablation across full, surface-only, and reference-only conditions plus H1/H2 trend analysis with slopes and R² values, and perplexity validation by depth. Plan_002 aggregates records across all generators with LOGO F1 scores in both macro and binary formats plus per-generator breakdowns. Plan_003 tests LOGO F1 stability across different reference models and DDR pattern consistency. Plan_004 examines perplexity across training variants with TOST results and negative finding confirmation. Plan_005 stratifies by prompt type with cross-validation F1 and leave-one-prompt-type-out evaluation. Plan_006 compares paraphrastic versus non-paraphrastic conditions for depth signal preservation. Plan_007 measures cross-model chain binary F1 and generator performance.

Now I'm laying out the remaining plans: plan_008 evaluates per-domain F1 and cross-domain generalization, plan_009 tests 5-class F1 with ordinal methods comparison, plan_010 assesses robustness at different edit levels and LLM rephrase degradation. Plan_011 analyzes LD-Score feature contributions with augmented model F1, plan_012 compares QLoRA F1 against handcrafted features with cost analysis. Plan_013 examines length correlation and length-matched F1, plan_014 tests 7B+ generator depth signal and feature drift at scale. Plan_015 evaluates existing detector ordinal signal and compares 7-feature versus single detector approaches. I'm going to structure all of this as a YAML configuration.

Now I'm checking the key metrics against their target ranges to ensure everything aligns properly. The binary F1 scores for the 8-gen and 9-gen models sit within their expected bounds, the LOFO binary F1 is on track, and the cross-model binary F1 is hitting the upper range. I'm also verifying the drift metrics—the drifting rho absolute minimum and stationary rho absolute maximum are both within acceptable thresholds.

Looking at the additional metrics, the seven-feature minus best single performance gain is solid at 3.3 points, the 8B logo binary F1 from plan-014 is in the right ballpark, and the LLM rephrase drop is reasonable. Before I generate the YAML, I need to clarify something about the generator count—the paper mentions 8 generators across 5 families, but plan-002 only had 5 generators, so the expansion to 8 happened through subsequent experiments like plan-014.

Tracing through the progression: I started with just Pythia-2.8B, then plan-002 added four more models bringing it to five total, plan-014 introduced Qwen3-8B for six, and later experiments added Llama-3.2-3B, Mistral-7B-v0.3, and Gemma-2-2B. The 8-generator set likely includes the original five plus three of these newer additions.

Now I'm ready to construct the comprehensive YAML output with the best-tier results, using actual numbers where available and filling in consistent estimates for the experiments that are already complete.

Writing YAML output... Looking at the ablation results, the full feature set achieves 0.820 macro F1 compared to 0.763 for surface-only and 0.719 for reference-only, with McNemar tests confirming statistical significance. The H2 hypothesis shows three features drifting over time—entropy_mean with a slope of -0.28 and strong R² of 0.92, along with ttr and hapax_ratio exhibiting similar patterns—while H1 features like tail_decay remain stationary with negligible slopes and low R² values. The H1 features like tail decay and entropy max stay relatively flat because the shape parameters of the NLL distribution don't shift much under location changes, while perplexity drops monotonically since deeper text becomes more predictable due to the model's own recursive compression. I'm also documenting the ablation study results showing the full feature set outperforms surface-only and reference-only approaches, along with visualizations of how features drift across depths.

Now I'm setting up the cross-generator evaluation framework to test generalization across five different generators using leave-one-out validation. Now I'm looking at the per-family performance breakdown across held-out test sets, along with ablation results showing how much each component contributes to the overall model performance. The results indicate the binary F1 score of 0.700 is robust across generators with low variance, and while OLMo-2-1B performs slightly lower due to architectural differences, it still maintains strong performance above the threshold. The LOFO results confirm cross-family generalization holds up well, with only a 1.4 percentage point drop compared to LOGO, and the Pythia family overlap doesn't artificially inflate the findings. Now I'm setting up the reference model experiments using non-Pythia architectures like OLMo and Qwen to test whether the detection approach generalizes across different model families and to verify the entropy drift hypothesis. The entropy mean drift is consistently negative across all reference models, which makes sense because drifting is inherent to the generation process through recursive compression rather than a specific bias in Pythia-410M. Surface-level features like hapax ratio and type-token ratio show no dependence on the reference model choice, while shape features have very weak correlations across references. The Qwen reference performs slightly better since it has more generators in the training set, but the difference is only 1.3 percentage points, indicating that reference model selection isn't a critical design decision.

Now I'm looking at the tables comparing LOGO F1 scores and per-feature Spearman correlations across the three reference models, along with figures showing how the drifting versus stationary patterns remain consistent across them. This is the crucial test for Claim 2—if the dual dynamics pattern only appeared with Pythia, the entire narrative would collapse, but all three reference models reproduce the same groupings and show aligned entropy drift directions.

The magnitude differences are minimal, confirming this isn't a Pythia artifact but an inherent property of the generation process. Now examining the downstream utility experiment with OLMo-1B fine-tuning on depth-stratified data, which shows perplexity metrics across different data filtering variants... The random subsampling approach with size matching achieves better perplexity (2.367) than depth-aware filtering (2.387), and TOST equivalence testing at a ±2% margin confirms they're statistically equivalent with very strong significance. The depth filtering removes deeper text but also eliminates valuable training signal diversity, whereas random sampling preserves better distributional coverage. The depth-only variant performs worst because the human-annotated data is too small (797 samples), and the extremely low seed variance across runs suggests the model is very stable at this data scale, which indicates that depth fingerprinting works as a diagnostic tool rather than a solution for improving training data. Now I'm looking at the performance metrics comparing different prompt strategies—continuation, elaboration, and rewriting approaches—across several evaluation dimensions like F1 scores on different datasets, depth retention, and linguistic correlations with vocabulary diversity and entropy measures. Elaboration preserves semantic ties to the original text, limiting how much the distribution can drift, while continuation shows weaker semantic constraints. Looking at the retention metrics, elaboration maintains nearly all the text at deeper levels (98.6%), whereas continuation loses more of the deeper content (83.1%) since longer passages get filtered out. The drifting feature pattern holds consistently across all prompt types, with correlations exceeding 0.55 in magnitude.

The prompt-type effect is real—continuation achieves 0.781 F1 versus elaboration's 0.730, a 5.1 percentage point gap—but the underlying drift mechanism stays qualitatively the same regardless of prompt type. LOPTO generalizes across these types with an average F1 of 0.753, which validates the ecological validity of the approach: the depth signal remains extractable even without knowing the prompt type in advance.

Now I'm setting up a comparison between paraphrastic and continuation chains to test whether they converge toward the same attractor states, with expected performance metrics and feature correlations... The key distinction is that non-paraphrastic chains—the primary form of web contamination—show continuous feature drift, whereas paraphrastic chains plateau around depth 3 due to semantic preservation constraints. At the feature level, paraphrastic chains maintain relatively stable vocabulary metrics (hapax/TTR correlation around -0.28 to -0.32) compared to the stronger drift in best-performing chains (-0.55), since paraphrasing inherently preserves lexical diversity. This contrast clarifies the paper's contribution: while paraphrasing has prior work, the analysis of non-paraphrastic continuation chains reveals the actual mechanism of distributional contamination.

Now I'm looking at cross-model chain experiments comparing performance when using different generators at each depth versus a single consistent generator, with expected F1 scores and confidence intervals for both binary and three-class classification tasks. The cross-model chains show stronger depth signals because each step introduces different distributional biases that compound, creating larger feature divergence compared to single-model sequences where patterns stabilize. This validates the ecological argument that real-world contamination involves multiple models, and the results meet the core hypothesis threshold with F1 scores above 0.76.

Now I'm planning the multi-domain expansion across Wikipedia, news, academic, and code sources to test whether the detection performance holds across different content types and writing styles. The code domain performs near average because structural patterns like syntax and indentation provide additional signals, though entropy features get compressed by code syntax constraints. The drifting feature patterns remain qualitatively consistent across all domains with correlation magnitudes exceeding 0.52, though domain-specific variations exist. I'm now compiling the per-domain performance tables and domain comparison visualizations to support the ecological validity claim, with the 8.4 percentage point gap honestly reported but not undermining the core findings.

Now I'm planning a finer-grained ordinal classification experiment using five generational classes, comparing XGBoost against ordinal-specific methods like CORAL and Frank-Hall, expecting F1 scores around 0.50 for the 5-class task but substantially higher for 3-class variants, with the main confusion occurring at the gen-1/gen-2 boundary where most binary errors manifest as false negatives.

Looking at the per-generation performance breakdown, gen-0 achieves exceptionally high F1 at 0.95 due to strong seed-sharing signals, while gen-1 drops to 0.52 and subsequent generations plateau around 0.32-0.38, revealing that ordinal methods provide no improvement over standard approaches. The core bottleneck lies between gen-1 and gen-2, where feature drift from recursive generation becomes too pronounced to reliably distinguish later generations from one another. The distinction between gen-1 and gen-2+ is approaching the noise floor, so further subdividing into gen-2/gen-3/gen-4 won't yield meaningful signal—this is an honest scope boundary that doesn't undermine the paper's core contribution. Now I'm looking at robustness metrics for simulated human edits, tracking how performance degrades under random word replacement and LLM rephrasing scenarios. The LLM rephrasing approach falls between the 5% and 10% random replacement levels because it maintains coherence while still shifting local statistics, which represents a reasonable robustness profile where light editing preserves the depth signal but heavy editing shows meaningful degradation. These results support the paper's credibility, and LLM rephrasing appears to be a more realistic evaluation scenario than random word substitution.

Now I'm planning to add LD-Score as an additional feature to test character-level depth signals, expecting it to contribute a modest 0.3 percentage point improvement when combined with the existing seven features.

Looking at the results, LD-Score shows moderate predictive power on its own with an F1 of 0.721, but the gain diminishes when added to the feature set because it correlates heavily with existing surface-level diversity metrics like hapax ratio and type-token ratio—both showing correlations above 0.68. This suggests that character-level distribution patterns are largely already captured by word-level features, so LD-Score's independent contribution is limited.

The main value LD-Score provides comes from detecting character bigram patterns specific to certain generator families, but this signal gets diluted when averaged across the LOGO evaluation. I'm deciding to exclude it from the main paper feature set and instead report it in the appendix as supplementary evidence. The 7-feature configuration remains the recommended approach for balancing simplicity and efficiency, with a comparison table and correlation heatmap showing where LD-Score overlaps with existing features.

Now I'm comparing a QLoRA fine-tuned end-to-end depth classifier against the 7-feature ensemble approach. Looking at the performance metrics across different classification tasks—the QLoRA model achieves notably higher F1 scores on 3-class and binary tasks, with advantages of 12.4 and 15.8 percentage points respectively, though it struggles on the 5-class problem. However, this comes at a significant computational cost: QLoRA requires 8.2GB of GPU memory versus 2.4GB for the ensemble, and inference is 6.5 times slower. The cross-generator evaluation shows the ensemble maintains better generalization.

The key insight is that QLoRA's within-distribution advantage stems from capturing contextual patterns beyond what handcrafted features can express, but the weaker cross-generator performance suggests some overfitting to generator-specific characteristics. The 7-feature ensemble trades raw performance for efficiency and interpretability, and the modest 7-percentage-point improvement on 5-class classification indicates that finer-grained depth categorization hits a fundamental task difficulty ceiling rather than just a feature limitation.

Now I'm looking at the performance-cost tradeoff comparison and positioning the 7-feature approach as the practical recommendation—QLoRA serves as an upper bound reference rather than the proposed solution, with the efficiency gains and cross-generator robustness directly addressing why end-to-end learning isn't necessary here.

For the text length analysis, the results show length isn't a primary confound despite some dropout bias on shorter texts—the weak correlation between length and depth (|ρ|<0.14) means text length doesn't systematically vary with depth, and the modest F1 drop when controlling for length (0.724 vs 0.770) confirms the effect is minimal. The length confound is properly addressed—the 4.6pp drop is honestly attributed to sample size reduction rather than deconfounding, since the random subsample control also showed a 2.9pp decline. I'm reporting the length-matched F1 of 0.724 as the conservative estimate in the paper. Now I'm planning to test scale effects by adding a larger generator model with expected performance metrics across different classification tasks.

Looking at the results, the Qwen3-8B model achieves a binary F1 of 0.683, which falls within the expected range, showing that scale effects exist but are moderate—the larger model underperforms smaller ones by roughly 1pp on the logo task. The linguistic metrics reveal interesting patterns: hapax legomena and type-token ratio show strong negative correlations with scale, while the distribution-driven degradation pattern is preserved across model sizes. Looking at the Spearman correlation data across different model sizes and the visualizations showing how the DDR pattern holds at 8B scale, the scale effect is honestly reported but the qualitative findings remain robust—depth signals persist even at frontier-adjacent scales like 8B, with the 14B analysis further confirming the pattern stays consistent. Now I'm setting up comparisons with existing detectors like FastDetectGPT, Binoculars, and LD-Score to benchmark the ordinal signal against established baselines. Now I'm looking at the comparative performance metrics—the 7-feature model shows a 3.3 percentage point advantage over the best single detector (average log probability at 0.765), with bootstrap testing confirming statistical significance. Average log probability emerges as the strongest individual detector since it directly measures the mean negative log-likelihood, which is the core signal the drifting features capture, while FastDetectGPT underperforms because it was designed for binary classification rather than this ranking task. real vs synthetic)，perturbation-based approach 对 ordinal depth signal 不 sensitive。Binoculars 最弱 (0.579) 因为它依赖 two-model comparison 的 ratio，depth 信号在 ratio 中被部分 cancel。7-feature 优势来自 complementarity：drifting + stationary features 捕捉不同 aspects of depth response (location shift + shape preservation)，single detector 只捕捉一个维度。

现在看着 bootstrap 分布和 detector score 与 depth 的散点图，7-feature 的 3.3pp 优势虽然幅度不大但统计显著 (p<0.01)。关键是 detector scores 本身已经有 moderate ordinal signal (avg_logprob ρ=0.79)，但 7-feature 通过 complementarity 显著提升了这个信号。这改变了我对贡献的理解——不是发现新特征，而是通过特征互补性来改进 depth estimation。

让我检查一下实验数据确保预测一致，特别是 plan-001-fix 的完整性能 (0.8204)。

逐个验证各个实验的结果：plan-002 的 macro F1 范围、plan-003 的跨模型一致性、plan-004 的排序验证、plan-005 的 CV 分割结果、plan-013 的长度混淆检验、plan-014 的 held-out 性能、plan-015 的七特征基准。

现在看 plan-010 的鲁棒性测试显示性能随噪声增加而下降，LLM 改写导致显著性能下滑，多域种子数据在新闻、学术和代码领域的表现相近，QLora 微调在两个模型上都达到高准确率，9 生成 logo 任务的二分类和三分类结果。我会用实际可得的数据，对缺失部分进行推断来完成计划。

现在需要更仔细地核实二分类 F1 值——论文框架中 LOGO 二分类 F1 为 0.694，但注册表中 plan-002-eval 没有明确的二分类 F1 数据。查看 review-exp-c-overall-ci 的整体 LOGO F1 是 0.7879（这是三分类），8 生成 LOGO 二分类 F1 = 0.694 来自论文框架的主要结果。对于 plan-007 的跨模型链，论文框架给出跨模型二分类 F1 = 0.830（5 生成子集，生成器级 LOGO）和其他地方的 0.764，我会用 0.830 这个主要数据。

不过论文框架中同时提到 0.830 和 0.764——0.764 出现在 RC2 和 RC4 的上下文中，最佳范围是 [0.76, 0.83]，所以用 0.830 作为主指标。核心假设还提到跨模型链验证异质性放大（二分类 F1≥0.76），所以 0.76 是下界。现在可以完成 YAML 配置了。

对于需要纯预测的计划——plan_006、plan_007、plan_009、plan_011、plan_012——我需要检查数据来源。plan_012 有 exp_055/056 的 QLoRA 微调数据，但最佳层级指定的 Qwen3.5-0.8B 不存在，所以实际用的是现有模型的 QLoRA 微调版本。

我现在查看 QLoRA 实验的具体结果：OLMo 和 Qwen 的 instruct 版本分别达到 3 分类 0.888 和 0.907，二分类 0.836 和 0.867；base 版本略低一些。这给了我 QLoRA 在这个任务上的真实性能范围。

现在要确认最终输出的细节——用户要求的是 experiment_plan 中的 15 个计划实验，不包括后续的扩展实验。对于二分类 F1 分数，我应该用 LOGO 评估中的具体数值：8 代生成的 0.694 和 9 代生成的 0.666，这些数字与论文的主要结论相符。

对于其他关键指标，我也要选择与论文框架相匹配的数值范围内的代表性数字——比如 LOFO 的 0.686、跨模型的 0.830，以及漂移检测中的相关系数阈值。

现在处理 plan_002 中的 LOGO 二分类 F1 分数时，我需要考虑生成器数量的影响：8 个生成器的论文数据是 0.694，但 plan_002 只有 5 个生成器，这意味着变异性更小，所以二分类 F1 应该更高，估计约 0.700。从 plan-002-eval 的注册表数据来看，LOGO 宏平均 F1 是 0.8037（这是三分类），但二分类会更低，因为三分类的结果被第 0 代生成器的性能拉高了。

根据论文数据，三分类 0.762 对比二分类 0.694 的比率约为 0.91，应用到 5 生成器的情况：0.804 × 0.91 ≈ 0.732，但这对二分类来说似乎偏高。查看具体数据点，8 生成器的单个生成器二分类范围是 0.633-0.724，而 5 生成器集合（不包含更大/更难的生成器）应该有更高的平均值，所以我预测 plan_002 的 LOGO 二分类 F1 约为 0.70。

现在我有足够的信息来生成输出了。用户需要的是最佳层级的叙述指导和 15 个想象实验的列表，每个实验包含名称、计划 ID、描述、预期结果、结果理由、表格和图表说明。我需要确保指标精确且理由充分，但避免过度冗长。

我注意到 plan_002 涉及 5 个生成器（Pythia-2.8B、Pythia-1B、OLMo-2-0425-1B、Qwen3-0.7B、Qwen3-0.6B）和 25K 条链，而 8 生成器的评估是通过添加 Llama、Mistral 和 Qwen3-8B 得到的。现在我来生成最终的 YAML 输出。

我应该更仔细地检查 plan_007 的预期结果。论文中提到跨模型二分类 F1 为 0.830（5 生成器子集，生成器级别 LOGO）和 3 分类 F1 为 0.789，但其他地方又提到 0.764 的二分类。这个差异可能来自于...

等等，重新阅读论文框架，Claim 1 明确指出"跨模型链在生成器级别 LOGO 下的二分类 F1 = 0.830（5 生成器子集）"，而标题指标表中也显示"跨模型二分类 F1: 0.830"，上下文是"5 生成器子集，生成器级别 LOGO"。所以 0.830 就是精确值，这是最佳范围。

现在我来系统地生成 YAML。

不过我还想检查一下 14B 数据的表现，因为核心假设提到"14B 规模 DDR 模式定性不变"。让我看看 exp_060_14b_ddr_analysis 中的相关指标——这里有熵均值、熵标准差、熵最大值、熵最小值、词汇丰富度和 hapax 比率等多个相关性指标的数据。

在 14B 规模下，漂移特征的相关系数绝对值在 0.39 到 0.51 之间，低于 0.55 的阈值，但 DDR 分组（漂移 vs 平稳）的模式保持一致，只是幅度有所衰减。这与最佳层级的假设相符。

现在来确定最终方案：对于 plan_014（大规模生成器），描述中提到"一个 7B+ 生成器（Qwen3-8B-Base 或类似）"，注册表显示 plan-014 使用的是 Qwen3-8B 数据。

我需要用 plan-014 的实际数据来做预测，其中 8B 规模的 F1 分数是 0.6832，Spearman 相关系数分别为 hapax=-0.558、ttr=-0.542、entropy_mean=-0.475。

对于 plan_006（释义比较），这是一个还未完成的方案。根据论文框架中的吸引子循环理论，释义链会收敛到约 3 个类别。在最佳层级的预测中，应该看到释义链的深度信号较弱（F1 较低）、收敛速度更快（特征更早达到平台期），这清楚地区分了我们的贡献。对于 plan_007（跨模型链），这也是一个还未明确完成的方案。

对于 plan_009（更细粒度的序数分类），5 分类的 F1 约为 0.50，序数方法没有改进，而 QLoRA 数据给出的 5 分类约为 0.55-0.60，这是端到端的上界。对于 plan_011（LD-score 特征），plan-015 已经有 LD-Score 作为基线检测器（LOGO F1 = 0.721），但 plan_011 问的是将 LD-Score 作为集成中的额外特征，预测是由于与现有表面特征的相关性，添加 LD-Score 到 7 特征集合只会产生边际改进。现在我对这些预测很有信心，准备写最终的 YAML 配置，需要确保 expected_results 包含具体的指标名称和数值。

对于 plan_002，我在计算 5 生成器的二分类 F1。从 plan-002-eval 注册表看，LOGO 平均 macro_f1 是 0.8037（3 分类），family_out_delta 是 0.0107。根据论文框架，8 生成器的 LOGO 3 分类是 0.762，二分类是 0.694，所以二分类与 3 分类的比率约为 0.911。对于 5 生成器，3 分类 macro 是 0.804，二分类估计值是 0.804 × 0.911 = 0.732，这看起来有点高，但实际上 5 生成器集合更容易（生成器多样性较低）。

我意识到 8 生成器的 0.762 是 3 分类 macro，而 0.694 是 gen1-vs-gen2+ 的指标，这两者测量的东西不同，不能直接比较。让我换个角度思考。plan-002-eval 显示 5 生成器 LOGO macro（3 分类）= 0.804，对于二分类 F1（gen-1 vs gen-2+），我预期会低于 3 分类，因为 gen-0 很容易分类。所以 5 生成器 LOGO 的二分类 F1 可能在 0.70-0.72 之间。从扩展的 8 生成器数据看，8 生成器 LOGO 3 分类 = 0.762，二分类 = 0.694，二分类比 3 分类低约 0.068。对于 5 生成器，0.804 - 0.068 = 0.736，但这个差值可能不适用。

从 plan-014 的逐生成器数据，qwen3-8b 二分类 F1 = 0.6468，3 分类 = 0.6955，差值 = 0.049，所以 3 分类和二分类之间的差值大约在 0.05-0.07 之间。对于 5 生成器 LOGO，二分类 ≈ 0.804 - 0.06 = 0.744，这看起来合理但可能有点高。我应该回到论文的主要数字，在需要的地方保守估计。论文框架说 LOGO 二分类 F1 = 0.694（8 生成器 LOGO），LOFO 二分类 F1 = 0.686，这些是在完整 8 生成器数据集上计算的。plan-002 只有 5 个生成器，所以是一个前身版本，5 生成器的二分类 F1 应该高于 8 生成器，因为生成器更少意味着分类任务更简单。

看最佳层级的关键指标，logo_binary_f1_8gen 是 [0.69, 0.72]，plan-002 是 5 生成器而非 8 生成器，所以我预测 plan-002 二分类 F1 ~ 0.72。我已经过度分析了，现在应该生成输出，使用实际注册表值，其余的推导或预测。现在我要生成完整的 YAML，需要仔细匹配指定的输出格式。让我再检查一些数字，特别是 plan-007 的交叉验证结果。

对于交叉模型，论文说二分类 F1 = 0.830，但也提到"异构生成器的交叉模型链在 RC4 中产生二分类 F1 = 0.764"，这些可能是不同的子集或评估协议。最佳层级范围是 [0.76, 0.83]，我用 0.830 作为主要指标，并注意 LOGO 的每生成器变化。仔细看论文的表述，声称"交叉模型链在生成器级 LOGO（5 生成器子集）下产生二分类 F1 = 0.830"，标题表格显示"交叉模型二分类 F1 | 0.830 | 5 生成器子集，生成器级 LOGO"，但在另一个声称中"仅参考产生更高的二分类 F1（0.833 vs 0.695）"。

我认为 0.830 是交叉模型链的结果，而 0.764 可能是不同的评估或更早的数字，所以用 0.830 作为最佳层级。现在准备输出，需要验证用户想要单个 YAML 块，并确认"计划"状态意味着所有 15 个实验都列为"计划中"，即使许多有对应的注册表条目显示"完成"，计划状态还未更新，用户需要所有 15 个的预测。还要精确处理 DDR rho 值，论文说漂移：hapax −0.63、TTR −0.61、entropy_mean −0.60（|ρ| >...）。

现在检查综合评估数据中的具体 rho 值：hapax −0.647、ttr −0.630、entropy_mean −0.610 是 8 代聚合数字，对于最佳层级，漂移指标都满足 |ρ| ≥ 0.55 的阈值，而平稳指标的 tail_decay 和 entropy_max 都远低于阈值。

entropy_min 的 |0.406| 实际上相当可观，但在论文的 Claim 2 框架中，它并未被明确列为漂移特征——论文只特别指出了三个漂移特征（hapax、TTR、entropy_mean）和一个平稳特征（tail_decay）。

根据核心假设，漂移特征需要 |ρ|≥0.55，平稳特征需要 |ρ|<0.10，这就是论文建立的二分法。entropy_std 处于中间位置（弱漂移），entropy_min 则介于两者之间，没有被明确归类。现在我要生成完整的 YAML 输出，涵盖所有 15 个实验并使用精确的指标。

Generating YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09970dfb-e496-480d-bc18-dcaa7511e12a",
  "isSidechain": false,
  "requestId": "req_011CbEgz5gx2RQCfrZAwaZhw",
  "type": "assistant",
  "uuid": "7a5cfcf3-117b-4407-8a58-3cc45f84a0f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016372Gc7LYSqTNB1PScTvaH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24838,
      "cache_read_input_tokens": 11841,
      "output_tokens": 35492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 35492,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24838
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

_source line 9 · 2026-05-20T23:41:00.729Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。DDR 二分法 (drifting: hapax, TTR, entropy_mean |ρ|≥0.55;
  stationary: tail_decay, entropy_max |ρ|<0.10) 在 8+ generators / 5 families 上鲁棒，
  entropy_std 归为 weakly drifting (|ρ|≈0.20)，不破坏主叙事。
  三条 claim 均有充分实验支撑：(1) LOGO binary F1=0.694 为 headline，LOFO 0.686 和
  cross-model 0.830 验证泛化性；(2) DDR 跨 3 个 reference model 和 5 个 generator family 稳健，
  TOST 确认 shape feature stationarity；(3) negative downstream finding 以 TOST ±2% margin 确认。
  Scope limitations (base-only, t≤0.7, ≤14B) 诚实报告但不动摇核心 contribution。
  论文按原 framing 直接提交 ARR。

imagined_experiments:
  - name: "feature_ablation_and_trend"
    plan_id: "plan_001"
    description: "MVP 数据上的三部分分析：(A) feature ablation (full/surface/reference), (B) H1/H2 trend analysis, (C) perplexity pre-validation"
    expected_results:
      ablation_full_macro_f1: 0.820
      ablation_surface_only_f1: 0.763
      ablation_reference_only_f1: 0.719
      ref_vs_surf_bootstrap_ci: "[0.706,0.733] vs [0.747,0.774]"
      mcnemar_full_vs_surface_p: 0.0
      mcnemar_full_vs_ref_p: 0.0
      h2_drifting_features: [entropy_mean, ttr, hapax_ratio]
      h2_slope_entropy_mean: -0.29
      h2_slope_ttr: -0.034
      h2_slope_hapax_ratio: -0.043
      h2_R2_entropy_mean: 0.93
      h2_R2_ttr: 0.89
      h2_R2_hapax_ratio: 0.92
      h1_stationary_features: [tail_decay, entropy_std, entropy_max, entropy_min]
      h1_slope_tail_decay: 0.002
      h1_R2_tail_decay: 0.03
      entropy_std_slope: -0.12
      entropy_std_R2: 0.41
      median_ppl_by_depth: [13.50, 4.96, 3.00, 2.07, 1.72]
      ppl_depth_trend: monotonic_decrease
    result_rationale: >
      Full set 显著优于任一子集 (5.7-10.1pp)。Surface features 捕捉词汇多样性衰减
      (TTR/hapax 随 depth 单调递减)，reference features 捕捉 NLL 分布位移
      (entropy_mean drift)，两组信号互补。McNemar p=0 确认非冗余。
      H2 drifting features 呈清晰单调趋势 (R²>0.89)：递归生成导致词汇空间收缩
      和 NLL 均值下降 (recursive compression)。H1 stationary features 保持平坦
      (tail_decay R²=0.03)：NLL 分布的 shape 参数在 location shift 下近似不变。
      entropy_std 弱趋势 (R²=0.41) 远低于 drifting 组，归为 intermediate 不影响主叙事。
      Perplexity 单调递减：deeper text 对 reference model 更 predictable，
      因为 model 自身输出的 recursive compression 使 NLL 分布左移。
    tables:
      - "Table A1: Feature Ablation 5-fold CV — Full 0.820, Surface 0.763, Ref 0.719"
      - "Table A2: Per-feature linear trend (slope, R², p-value) across depths 0–4"
    figures_description:
      - "Fig 2: 7 features mean±std across depth 0–4。drifting 三特征 (hapax, TTR, entropy_mean) 显示清晰单调递减, R²>0.89；stationary 特征 (tail_decay, entropy_max) 水平。entropy_std 弱趋势 (浅灰色标注为 intermediate)"
      - "Fig S1: Pythia-410M perplexity by depth, 单调递减曲线 (13.50→1.72)"
    analysis: >
      Surface 和 reference 信号互补性经 McNemar 确认 (p=0)，是论文 complementarity claim 的基础。
      entropy_std 的 intermediate status (|slope|=0.12, R²=0.41) 需在正文中诚实讨论，
      但不破坏 3-drifting / 2-stationary 的核心二分法，
      因为 entropy_std 的 drift magnitude 仅为 drifting 组的 1/3。
      Perplexity pre-validation 确认 NLL 分布中存在 depth-dependent signal，为 Claim 3 建立 baseline。

  - name: "cross_generator_evaluation"
    plan_id: "plan_002"
    description: "5-generator LOGO 跨 generator 泛化评估 (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)"
    expected_results:
      total_records: 23032
      generators: [pythia-2.8b, pythia-1b, olmo-2-1b, qwen3-1.7b, qwen3-0.6b]
      families: [Pythia, OLMo, Qwen]
      logo_macro_f1: 0.804
      logo_binary_f1: 0.720
      logo_binary_ci: [0.708, 0.732]
      per_gen_macro_f1:
        pythia-1b: 0.851
        pythia-2.8b: 0.804
        qwen3-0.6b: 0.818
        qwen3-1.7b: 0.805
        olmo-2-1b: 0.752
      per_gen_binary_f1:
        pythia-1b: 0.724
        pythia-2.8b: 0.720
        qwen3-0.6b: 0.715
        qwen3-1.7b: 0.710
        olmo-2-1b: 0.670
      per_gen_binary_variance_pp: 5.4
      lofo_binary_f1: 0.705
      lofo_per_family:
        pythia_held_out: 0.690
        olmo_held_out: 0.720
        qwen_held_out: 0.706
      ablation_full_f1: 0.804
      ablation_reference_only_f1: 0.754
      ablation_surface_only_f1: 0.747
      mcnemar_p: 0.0
      entropy_std_importance_drop: 0.0049
      entropy_std_drift: 0.12
      top_features: [hapax_ratio_0.289, ttr_0.168, entropy_mean_0.160]
    result_rationale: >
      5-gen LOGO binary F1=0.720 高于后续 8-gen headline (0.694)，
      因为 5-gen set 不包含较难的 Mistral-7B (per-gen F1=0.633) 和 Gemma-2-2B (anomaly)。
      Per-gen binary 方差 5.4pp (<10pp 阈值) 证明跨 generator 泛化稳健。
      OLMo-2-1B 最低 (0.670) 因为 OLMo 架构 (非 GPT-NeoX/Llama 系) 产生的
      distributional pattern 与 Pythia family 差异最大。
      Pythia-1B 最高 (0.724) 部分受益于 Pythia-2.8B 在 training fold 中的 family overlap，
      但 LOFO 分析控制了此效应 (Pythia held-out 0.690 仅降 3pp)。
      Hapax_ratio 仍是最重要特征 (0.289 importance)，
      因为词汇多样性衰减是跨 generator 最一致的 depth signal。
    tables:
      - "Table 2: Per-generator LOGO macro/binary F1 with 95% CI"
      - "Table 3: LOFO per-family binary F1"
      - "Table S1: Feature importance rankings (5-gen aggregate)"
    figures_description:
      - "Fig 3: Bar chart — per-generator binary F1, error bars showing bootstrap CI。OLMo-2-1B 最低但仍 >0.65"
      - "Fig S2: Confusion matrices per held-out generator (5 panels)"
    analysis: >
      跨 generator 泛化成功。Per-gen 方差 <10pp 满足 best 档阈值。
      LOFO binary F1=0.705 确认跨 family 泛化：仅比 LOGO 低 1.5pp，
      证明 Pythia family overlap 未显著 inflate 结果。
      Feature ablation 确认 complementarity (McNemar p=0)，
      且 pattern 与 plan_001 一致 (full > surface ≈ reference)。

  - name: "cross_family_reference_model"
    plan_id: "plan_003"
    description: "Non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B) feature extraction，DDR 跨 reference model falsification test"
    expected_results:
      logo_f1_pythia_ref: 0.803
      logo_f1_olmo_ref: 0.807
      logo_f1_qwen_ref: 0.816
      cross_ref_f1_spread_pp: 1.3
      entropy_drift_all_refs_negative: true
      pythia_ref_drift_range: [-1.19, -1.40]
      olmo_ref_drift_range: [-0.61, -0.91]
      qwen_ref_drift_range: [-0.96, -1.35]
      spearman_by_ref:
        pythia_ref:
          hapax_ratio: -0.647
          ttr: -0.630
          entropy_mean: -0.610
          tail_decay: -0.040
          entropy_max: 0.050
        olmo_ref:
          hapax_ratio: -0.647
          ttr: -0.630
          entropy_mean: -0.585
          tail_decay: -0.038
          entropy_max: 0.055
        qwen_ref:
          hapax_ratio: -0.647
          ttr: -0.630
          entropy_mean: -0.620
          tail_decay: -0.042
          entropy_max: 0.048
      stationary_rho_max_across_refs: 0.055
      ddr_is_pythia_artifact: false
    result_rationale: >
      DDR 模式跨 3 个 reference model (Pythia-410M, OLMo-2-1B, Qwen3-0.6B) 完全稳健。
      Surface features (hapax, TTR) 完全不依赖 reference model，rho 跨 ref 完全一致。
      Reference features (entropy_mean) 方向一致 (均为负)，magnitude 因 ref model 自身
      perplexity calibration 不同而略有差异 (OLMo 偏低)，但不影响 drifting/stationary 分组。
      Shape features (tail_decay, entropy_max) 跨 ref 均 |ρ|<0.06。
      Qwen ref 分类 F1 略优 (0.816 vs 0.803) 因为 Qwen family 在 generator set 中有
      2 个 model，ref-generator family match 提升了 entropy feature 的 discriminability，
      但差异仅 1.3pp 证明 reference model 选择不是 critical design decision。
      这是 Claim 2 的关键 falsification test：如果 DDR 仅在 Pythia ref 下出现，
      叙事崩溃。Best 档下三个 ref 均重现相同分组。
    tables:
      - "Table 4: LOGO macro F1 by reference model (3 refs × 5 generators)"
      - "Table S2: Per-feature Spearman ρ by reference model (7×3 matrix)"
    figures_description:
      - "Fig 4: DDR pattern comparison across 3 reference models — drifting/stationary 分组完全一致, drift magnitude 有弱差异但方向一致"
    analysis: >
      DDR 非 Pythia artifact。这是 Claim 2 最重要的 robustness result。
      Entropy_mean drift 方向跨 3 个不同架构 family 的 ref model 一致为负，
      证明 drift 来自 generation 过程本身 (recursive compression) 而非特定 ref model 的 bias。
      Shape feature stationarity 同样跨 ref 稳健。论文可自信表述 DDR 为 generation-intrinsic property。

  - name: "downstream_utility"
    plan_id: "plan_004"
    description: "OLMo-1B fine-tuning on depth-stratified data, negative downstream finding (Claim 3)"
    expected_results:
      model: "OLMo-2-0425-1B (1485M)"
      total_runs: 15
      seeds: [42, 123, 456]
      variants:
        all:
          ppl_mean: 2.335
          ppl_std: 0.0003
          n_train: 12299
        size_matched:
          ppl_mean: 2.367
          ppl_std: 0.0002
          n_train: 3951
        depth01:
          ppl_mean: 2.387
          ppl_std: 0.001
          n_train: 3951
        binary_filtered:
          ppl_mean: 2.389
          ppl_std: 0.001
          n_train: 3951
        depth0_only:
          ppl_mean: 2.681
          ppl_std: 0.001
          n_train: 797
      ranking: "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)"
      tost_size_matched_vs_depth01:
        margin_pct: 2
        p_value: 0.00011
        equivalence_confirmed: true
      tost_size_matched_vs_binary:
        margin_pct: 2
        p_value: 0.00009
        equivalence_confirmed: true
      tost_margin_sensitivity:
        margin_1pct_p: 0.08
        margin_2pct_p: 0.00011
        margin_3pct_p: 0.000002
        margin_5pct_p: 0.0
      cohens_d_matched_vs_depth01: 0.85
      seed_variance_max_ppl: 0.002
    result_rationale: >
      Negative finding 清晰且符合预期。Depth-aware curation 不优于 random subsampling：
      size_matched (random) ppl=2.367 优于 depth01 ppl=2.387 和 binary_filtered ppl=2.389。
      原因：depth filtering 在移除 deeper text 的同时也移除了 diverse training signal，
      random subsampling 保留了更完整的 distributional coverage。
      TOST at ±2% margin 确认等价 (p=1.1×10⁻⁴)：depth-aware 和 random 在实际意义上无差异。
      ±1% margin 未 reject (p=0.08)，这是 honest boundary — 极小 margin 下无法确认等价，
      但 ±2% 足以满足实际应用场景的 equivalence threshold。
      depth0_only (ppl=2.681) 明显最差因为仅 797 samples (严重不足 + 缺乏 diversity)。
      Seed variance 极小 (<0.002) 因为 OLMo-1B fine-tuning 在此 data scale 下非常稳定，
      Cohen's d inflated 但 TOST 是 appropriate test。
      这确立了 depth fingerprinting 作为 diagnostic tool 的定位。
    tables:
      - "Table 5: Perplexity by training variant (5 variants × 3 seeds, mean ± std)"
      - "Table S3: TOST margin sensitivity (±1%, ±2%, ±3%, ±5%)"
    figures_description:
      - "Fig 6: Bar chart — perplexity by variant with error bars。ranking 清晰: all < size_matched < depth01 ≈ binary_filtered << depth0_only"
      - "Fig S3: TOST margin sensitivity curve — rejection threshold at ~±1.5%"
    analysis: >
      Negative finding 是 Claim 3 的核心。Best 档下 TOST 明确确认等价，
      且 ranking (random > depth-aware) 是 informative negative：
      即使 depth signal 存在，filtering 不改善 downstream quality。
      诚实报告 limitation：仅测试了单一 downstream task (CLM) 和单一 metric (perplexity)。
      但 TOST + 3 seeds + 5 variants 的设计远超 typical negative finding 的 evidence bar。

  - name: "prompt_type_comparison"
    plan_id: "plan_005"
    description: "Continuation vs elaboration vs inspired_rewriting chains 比较 (Pythia-2.8B, 1000 seeds)"
    expected_results:
      cv_f1:
        continuation: 0.781
        inspired_rewriting: 0.737
        elaboration: 0.730
      lopto_f1:
        held_out_continuation: 0.762
        held_out_elaboration: 0.762
        held_out_rewriting: 0.733
        avg: 0.753
      depth_retention_d4_d0:
        continuation: 0.831
        elaboration: 0.986
        rewriting: 0.939
      spearman_rho:
        continuation: {hapax: -0.651, ttr: -0.629, entropy_mean: -0.665}
        elaboration: {hapax: -0.674, ttr: -0.666, entropy_mean: -0.583}
        rewriting: {hapax: -0.670, ttr: -0.659, entropy_mean: -0.564}
      feature_drift_magnitude:
        continuation: {hapax: -0.740, ttr: -0.607, entropy_mean: -0.557}
        elaboration: {hapax: -0.828, ttr: -0.641, entropy_mean: -0.471}
        rewriting: {hapax: -0.800, ttr: -0.618, entropy_mean: -0.477}
      max_gap_cv_pp: 5.1
    result_rationale: >
      三种 prompt type 均保留 depth signal (所有 drifting |ρ|>0.55)，但 continuation 最强
      (CV F1=0.781)。Continuation 纯续写最大化 recursive compression — 每步输出成为下一步
      的 full context，无语义约束。Elaboration 最弱 (0.730) 因为保持与 seed 的语义关联，
      限制了 distributional drift 幅度。Rewriting 居中 (0.737) 因为 semantic preservation
      弱于 elaboration 但强于 continuation。
      Depth retention 差异大 (elaboration 98.6% vs continuation 83.1%)：continuation 的
      deeper text 更短更容易被 min-length filter 截断。
      LOPTO 证明跨 prompt type 泛化可行 (avg 0.753)：
      在一种 prompt type 上训练仍能在其他类型上保持合理性能。
      Feature drift magnitude: elaboration 的 hapax drift 反而更大 (-0.828 vs -0.740)
      因为 elaboration 的 higher retention rate 保留了更多 deep samples，使 regression 更稳定。
    tables:
      - "Table S4: Per-prompt-type CV F1 (within) and LOPTO F1 (cross)"
      - "Table S5: Spearman ρ by feature × prompt type"
    figures_description:
      - "Fig S4: Feature drift curves by prompt type (3 columns × 7 rows). Continuation 产生最大 depth-wise separation, elaboration 最平缓"
      - "Fig S5: Depth retention curves — continuation drops fastest (83.1% at d4)"
    analysis: >
      Prompt-type dependence (continuation 0.781 vs elaboration 0.730 = 5.1pp gap)
      诚实报告但 DDR 模式在所有 type 下定性一致。这支持 ecological validity (RC6)：
      real-world contamination 涉及多种 generation prompt，depth signal 在所有类型下均可提取。
      LOPTO avg 0.753 证明不需要知道 prompt type 即可部署。
      Continuation-elaboration gap 归因于 continuation 更自由的 distributional drift space，
      不是方法论缺陷。

  - name: "paraphrastic_comparison"
    plan_id: "plan_006"
    description: "Paraphrastic chains vs continuation chains, 测试 attractor convergence theory"
    expected_results:
      paraphrastic_cv_binary_f1: 0.618
      paraphrastic_cv_3class_f1: 0.680
      continuation_cv_binary_f1: 0.781
      continuation_cv_3class_f1: 0.834
      delta_binary_pp: -16.3
      paraphrastic_spearman:
        hapax_ratio: -0.30
        ttr: -0.26
        entropy_mean: -0.33
        tail_decay: -0.02
        entropy_max: 0.03
      paraphrastic_convergence_depth: 3
      paraphrastic_depth3_vs_depth2_binary_f1: 0.525
      continuation_depth3_vs_depth2_binary_f1: 0.640
      depth_retention_paraphrastic_d4_d0: 0.97
      semantic_sim_d0_d4_paraphrastic: 0.88
      semantic_sim_d0_d4_continuation: 0.52
    result_rationale: >
      Paraphrastic chains 的 depth signal 显著弱于 non-paraphrastic (binary gap 16.3pp)，
      符合 attractor convergence theory (ACL 2025)。Paraphrasing 对 input 施加 semantic
      preservation constraint，限制 distributional drift：vocabulary diversity 在 paraphrase
      中近似保持 (|ρ|<0.33 for all features)，因为 paraphrase 倾向复用相同 content words。
      ~3 步后 features plateau (depth3 vs depth2 binary F1≈0.525, near chance)，
      因为 paraphrastic chain 收敛到 model-specific attractor cycle。
      Continuation 无此 constraint，drift 持续累积 (depth3 vs depth2 F1=0.640 仍有信号)。
      Depth retention 极高 (97%)：paraphrasing 保持 text length 稳定。
      Semantic similarity d0→d4 高 (0.88)：paraphrase 保留了 meaning，
      而 continuation (0.52) 已显著 topic-drift。
    tables:
      - "Table S6: Paraphrastic vs continuation — CV F1, Spearman ρ, convergence depth"
    figures_description:
      - "Fig S6: Feature drift comparison — paraphrastic plateau at depth ~3, continuation continues drifting"
      - "Fig S7: Per-depth-pair binary F1 — paraphrastic 在 d2+ 后 near-chance"
    analysis: >
      Paraphrastic 对比清晰界定了本文 contribution scope。DDR 是 non-paraphrastic chains
      的特有现象，因为只有 unconstrained generation 允许 distributional drift 无约束累积。
      这与 LLM as Broken Telephone (ACL 2025) 互补：他们研究 paraphrastic attractor cycles，
      我们研究 non-paraphrastic depth drift — 两者共同覆盖了 iterative generation 的全景。
      Paper 在 related work 中 explicitly connect 两条线。

  - name: "cross_model_chains"
    plan_id: "plan_007"
    description: "Cross-model chains (每步不同 generator) vs single-model chains (RC4, ecological validity)"
    expected_results:
      cross_model_binary_f1: 0.830
      cross_model_3class_f1: 0.789
      cross_model_binary_ci: [0.812, 0.848]
      single_model_logo_binary_f1: 0.694
      delta_cross_vs_single_pp: 13.6
      cross_model_logo_per_gen:
        pythia-2.8b: 0.852
        pythia-1b: 0.838
        olmo-2-1b: 0.812
        qwen3-1.7b: 0.843
        qwen3-0.6b: 0.828
      cross_model_per_gen_variance_pp: 4.0
      heterogeneity_amplification_factor: 1.20
      ddr_cross_model:
        hapax_ratio_rho: -0.72
        ttr_rho: -0.69
        entropy_mean_rho: -0.68
        tail_decay_rho: -0.05
      cross_model_binary_f1_full_set: 0.764
    result_rationale: >
      Cross-model binary F1=0.830 (5-gen subset, generator-level LOGO)，满足核心假设
      (≥0.76)。Heterogeneous generators 在每步引入不同 distributional bias，
      产生 heterogeneity amplification (factor=1.20)：每步 generator change 叠加产生的
      feature divergence 大于单一 generator 的 recursive drift。
      单模型 chain 中 model-specific patterns 在 deeper depths 可能趋于 model-specific
      attractor state，而 cross-model chain 每步注入 fresh distributional perturbation，
      阻止 convergence。这导致 drifting features |ρ| 更高 (hapax -0.72 vs single-model -0.647)。
      Cross-model 场景更接近真实 web contamination (多模型参与)，
      因此 higher F1 是 positive ecological validity result。
      Full 8-gen set 的 cross-model binary F1=0.764 (略低于 5-gen 的 0.830)，
      因为 8-gen set 包含了更 diverse 的 generator combinations。
    tables:
      - "Table 6: Cross-model vs single-model — binary/3-class F1 with bootstrap CI"
      - "Table S7: Per-generator LOGO F1 on cross-model chains"
    figures_description:
      - "Fig 5: Feature divergence at each depth step — cross-model (red) consistently above single-model (blue), showing heterogeneity amplification"
      - "Fig S8: DDR pattern on cross-model data — drifting features |ρ| amplified"
    analysis: >
      Cross-model F1=0.830 是论文最强泛化 result。Heterogeneity amplification 是 key insight：
      真实 web contamination 涉及 diverse generators → depth signal 更强而非更弱。
      这直接 addresses RC4 且 strengthens narrative：
      controlled single-model evaluation (F1=0.694) 是 conservative lower bound，
      realistic multi-model scenario 反而更容易检测。
      Per-gen variance 4.0pp (cross-model) < 5.4pp (single-model)，
      进一步证明 heterogeneity 产生更稳定的信号。

  - name: "multi_domain_seeds"
    plan_id: "plan_008"
    description: "4-domain seeds 扩展 (Wikipedia, news, scientific, creative/code)"
    expected_results:
      per_domain_binary_f1:
        wikipedia: 0.694
        news: 0.712
        academic: 0.628
        code: 0.687
      per_domain_binary_ci:
        news: [0.690, 0.733]
        academic: [0.603, 0.652]
        code: [0.664, 0.710]
      per_domain_3class_f1:
        wikipedia: 0.770
        news: 0.715
        academic: 0.656
        code: 0.673
      overall_cross_domain_binary_f1: 0.676
      domain_gap_max_pp: 8.4
      worst_domain: academic
      best_new_domain: news
      ddr_by_domain:
        wikipedia: {hapax_rho: -0.647, entropy_mean_rho: -0.610}
        news: {hapax_rho: -0.621, entropy_mean_rho: -0.595}
        academic: {hapax_rho: -0.543, entropy_mean_rho: -0.520}
        code: {hapax_rho: -0.630, entropy_mean_rho: -0.581}
      ddr_pattern_consistent_across_domains: true
    result_rationale: >
      Depth signal 跨 domain 稳健但有 domain-specific variation (max gap 8.4pp)。
      Academic 最弱 (0.628) 因为学术写作高度 formulaic — 严格的 genre conventions
      (句式结构、术语使用) 限制了 generation 的 distributional drift 空间，
      且 academic text 的 baseline vocabulary diversity 已较低 (TTR ceiling effect)。
      News 最优 (0.712) 因为 news text 词汇丰富度高、topic diversity 大，
      generation drift 有更大的 feature margin 可供利用。
      Code (0.687) 接近 average：代码的 structural patterns (语法约束、缩进)
      提供额外区分信号，但 entropy features 被 code syntax 的 deterministic tokens 压缩。
      Wikipedia baseline (0.694) 与 8-gen LOGO headline 一致。
      DDR 模式跨 domain 定性一致 (所有 domain drifting |ρ|>0.52)，
      但 academic domain 的 |ρ| 最低，与 lowest F1 一致。
    tables:
      - "Table S8: Per-domain binary F1 with 95% CI (t=0.7 and t=1.0)"
      - "Table S9: Spearman ρ by feature × domain"
    figures_description:
      - "Fig S9: Domain comparison bar chart with error bars — academic 显著低于其他 domain"
      - "Fig S10: DDR pattern by domain (4 panels) — qualitatively consistent"
    analysis: >
      Multi-domain evaluation supports ecological validity (RC6)。
      Domain gap (8.4pp) 诚实报告为 limitation 但不动摇核心 claim：
      所有 domain 均显著优于 random baseline (0.50)，且 DDR 模式定性一致。
      Academic domain weakness 归因于 genre-specific ceiling effect，
      可在 future work 中通过 domain-specific feature engineering 改善。

  - name: "finer_grained_ordinal"
    plan_id: "plan_009"
    description: "5-class ordinal classification (gen-0 to gen-4), ordinal methods (CORAL, Frank-Hall) 比较"
    expected_results:
      xgboost_5class_f1: 0.503
      coral_5class_f1: 0.497
      frank_hall_5class_f1: 0.501
      xgboost_3class_f1: 0.773
      ordinal_mae: 0.72
      per_class_5class_f1:
        gen0: 0.952
        gen1: 0.518
        gen2: 0.348
        gen3: 0.325
        gen4: 0.372
      confusion_matrix_bottleneck: "gen-1/gen-2 boundary concentrates 86% of binary errors as FNs"
      gen2_gen3_mutual_misclass_rate: 0.42
    result_rationale: >
      5-class F1≈0.50, ordinal methods (CORAL, Frank-Hall) 无改善 (<1pp)。
      Gen-0 仍高 F1 (0.952) 因为 seed sharing 提供强信号 (human text vs LLM text 的 distributional gap)。
      Gen-1 moderate (0.518)：与 gen-0 的 gap (first generation step) 最大，但与 gen-2 的
      margin 已很小。Gen-2/gen-3/gen-4 严重混淆 (mutual misclass 42%)：
      recursive drift 在前 2 步最陡峭 (feature curve 呈 concave shape, 非线性)，
      deeper depths 的 marginal drift 已趋近 noise floor。
      Ordinal methods 不优于 standard XGBoost 因为 feature space 中的 ordinal structure
      在 deeper depths 退化 — 非线性 plateau 而非 monotonic 递增。
      CORAL 和 Frank-Hall 假设 ordinal margin 在所有相邻 class pairs 间近似均匀，
      但实际 gen-0→gen-1 margin >> gen-2→gen-3 margin，violating this assumption。
    tables:
      - "Table S10: 5×5 confusion matrix (XGBoost)"
      - "Table S11: Ordinal methods comparison (XGBoost, CORAL, Frank-Hall) + 3-class reference"
    figures_description:
      - "Fig S11: Per-class F1 across 3/5-class — 5-class 在 gen-2+ 急剧下降"
      - "Fig S12: Feature saturation curves — all 7 features plateau after depth 2"
    analysis: >
      3-class (gen-0/gen-1/gen-2+) 是 practical resolution ceiling。
      5-class 不可行的根本原因是 distributional drift 的 diminishing marginal return：
      depth 每增加一步，feature shift magnitude 递减 (concave curve)。
      这是 generation process 的 intrinsic property (类似 entropy rate convergence)，
      不可通过更好的 classifier 或更多 features 解决。
      诚实报告为 scope boundary，不削弱论文核心 contribution (3-class 已是 novel formulation)。

  - name: "human_edit_robustness"
    plan_id: "plan_010"
    description: "模拟人类编辑的 robustness test — (A) random word replacement (5%/10%/20%) + (B) LLM rephrase"
    expected_results:
      baseline_binary_f1: 0.695
      random_replacement:
        pct5_binary_f1: 0.650
        pct10_binary_f1: 0.614
        pct20_binary_f1: 0.591
        pct5_drop_pp: -4.6
        pct10_drop_pp: -8.1
        pct20_drop_pp: -10.4
      llm_rephrase:
        binary_f1: 0.647
        binary_ci: [0.631, 0.662]
        multiclass_f1: 0.667
        multiclass_ci: [0.655, 0.680]
        binary_drop_pp: -4.5
        multiclass_drop_pp: -7.1
      edit_distance_ratio: 0.507
      avg_sentences_replaced: 1.69
      degradation_profile: graceful
    result_rationale: >
      LLM rephrase drop 4.5pp (在 [3.0, 5.0] 范围内)，为 graceful degradation 而非
      catastrophic failure。5% random replacement 仅降 4.6pp 因为 distributional features
      (TTR, entropy, hapax) 是 global statistics — sparse point noise 不改变 aggregate patterns。
      10% drop 8.1pp 因为开始影响 type/token ratio 的分子 (unique word count)。
      20% drop 10.4pp 因为大规模替换直接扰乱 lexical diversity，但仍远优于 chance (0.50)。
      LLM rephrase (edit_distance ~50%, avg 1.69 sentences replaced) drop 4.5pp，
      介于 5-10% random 之间：LLM rephrasing 保持 coherence 和 topic 但改变局部
      word choice → surface features (hapax, TTR) 被部分扰乱，
      reference features (entropy) 更 robust 因为 rephrased text 的 NLL 仍保留 depth-dependent pattern。
    tables:
      - "Table S12: Binary F1 under edit conditions (baseline, 5%, 10%, 20%, LLM rephrase) with CI"
    figures_description:
      - "Fig S13: Degradation curve — F1 vs edit intensity (x-axis: 0%, 5%, 10%, 20%; LLM rephrase 标注在 ~7% equivalent position)"
    analysis: >
      Graceful degradation profile 支持论文 practical utility argument (RC5)。
      LLM rephrase 4.5pp drop 在可接受范围 — 即使文本被 lightly edited，
      depth signal 仍有信息量。Heavy editing (20%) 的 10.4pp drop
      诚实报告为 limitation，但 realistic human editing 更接近 5-10% level。
      Multiclass drop (-7.1pp) > binary drop (-4.5pp)：editing 主要 blur gen-1/gen-2+ boundary，
      gen-0 detection (human vs LLM) 更 robust to editing。

  - name: "ld_score_feature"
    plan_id: "plan_011"
    description: "将 LD-Score (character-level distribution signature) 作为第 8 个特征加入 ensemble"
    expected_results:
      ld_score_standalone_logo_f1: 0.721
      ld_score_spearman_with_depth: 0.794
      seven_feature_logo_f1: 0.798
      eight_feature_logo_f1: 0.801
      delta_adding_ld_score_pp: 0.3
      ld_score_feature_importance_rank: 5
      ld_score_correlations:
        with_hapax_ratio: 0.72
        with_ttr: 0.68
        with_entropy_mean: 0.51
      ld_score_corrected_cv_f1: 0.793
    result_rationale: >
      LD-Score 单独有 moderate ordinal signal (F1=0.721, Spearman ρ=0.794)，
      但加入 7-feature ensemble 后仅提升 0.3pp。原因：LD-Score 测量 character bigram
      distribution 的 divergence from reference，与 word-level surface features (hapax r=0.72,
      TTR r=0.68) 高度相关 — character-level 词汇多样性衰减与 word-level 衰减高度 co-linear。
      LD-Score 的独立贡献仅在于 character bigram patterns 对特定 generator family
      (尤其是 BPE tokenization 差异大的 model) 有额外 sensitivity，
      但这在 LOGO 跨 generator evaluation 中被 averaging 稀释。
      Feature importance 排名第 5 (在 entropy_std 和 entropy_max 之间)，
      不足以 justify 增加 feature 的复杂度。
    tables:
      - "Table S13: 8-feature vs 7-feature LOGO comparison"
      - "Table S14: Feature correlation matrix (8×8)"
    figures_description:
      - "Fig S14: Correlation heatmap — LD-Score 与 hapax/TTR 的高相关可视化"
    analysis: >
      LD-Score 不纳入 paper 主线 feature set，在 appendix 作为 supplementary evidence 报告。
      Character-level 信号已被 word-level features 充分捕捉。
      7-feature set 保持为推荐方案 (simplicity, interpretability, efficiency)。
      LD-Score 作为 baseline detector (plan_015) 的价值高于作为 ensemble feature 的价值。

  - name: "end_to_end_classifier"
    plan_id: "plan_012"
    description: "QLoRA fine-tuned end-to-end depth classifier vs 7-feature handcrafted ensemble"
    expected_results:
      qlora_base_3class_f1: 0.881
      qlora_base_binary_f1: 0.826
      qlora_base_5class_f1: 0.551
      qlora_instruct_3class_f1: 0.897
      qlora_instruct_binary_f1: 0.852
      seven_feature_3class_f1: 0.773
      seven_feature_binary_f1: 0.694
      qlora_advantage_3class_pp: 12.4
      qlora_advantage_binary_pp: 15.8
      qlora_logo_cross_gen_binary_f1: 0.72
      qlora_logo_cross_gen_3class_f1: 0.78
      cost_comparison:
        seven_feature_gpu_memory_gb: 2.4
        qlora_gpu_memory_gb: 8.2
        inference_time_ratio: 6.5
    result_rationale: >
      QLoRA within-distribution 显著优于 7-feature (+12-16pp on binary)，
      因为 end-to-end fine-tuning 学习了 handcrafted features 之外的 contextual/positional patterns：
      句法结构退化、discourse coherence 下降、repetition 模式等 token-sequence level 信号。
      但 QLoRA 的 cross-generator generalization (LOGO binary ~0.72) 远低于 within-distribution
      (0.826-0.852)，gap ~10pp：end-to-end model 部分 overfit 到 generator-specific token patterns
      而非 depth-universal distributional shift。
      5-class QLoRA (0.551) 仅比 handcrafted (0.503) 高 ~5pp，
      确认 finer classification 的 bottleneck 是 task-inherent difficulty 而非 feature limitation。
      7-feature ensemble 的优势在于：(a) 2.4× less GPU memory, (b) 6.5× faster inference,
      (c) interpretable (每个 feature 有 clear DDR 语义), (d) cross-generator 泛化更稳定
      (within-LOGO variance 更小)。
    tables:
      - "Table S15: QLoRA vs 7-feature — F1 (within-CV, LOGO), cost, memory"
      - "Table S16: QLoRA per-model results (OLMo-base, OLMo-instruct, Qwen-base, Qwen-instruct)"
    figures_description:
      - "Fig S15: Performance-cost tradeoff scatter plot — 7-feature 在 efficiency frontier"
      - "Fig S16: QLoRA within-CV vs LOGO gap (showing overfitting to generator)"
    analysis: >
      QLoRA 定位为 upper bound reference 而非 paper 推荐方案。
      7-feature ensemble positioned on efficiency + interpretability + cross-generator robustness。
      这 addresses 潜在 "为什么不用 end-to-end" 质疑：
      answer 是 cost-performance tradeoff (2.4× memory, 6.5× speed) 和 cross-generator generalization。
      End-to-end 的 LOGO gap (~10pp) 暗示 generator-specific overfitting，
      而 7-feature 的 handcrafted nature 保证了 feature 的 generator-agnostic 语义。

  - name: "text_length_control"
    plan_id: "plan_013"
    description: "Text length confound 控制分析 (RC10)"
    expected_results:
      spearman_length_depth_range: "[-0.066, +0.134]"
      length_depth_correlation: "weak (|ρ|<0.14)"
      length_matched_binary_f1: 0.724
      unmatched_binary_f1: 0.770
      length_matched_delta_pp: -4.6
      random_subsample_control_f1: 0.741
      random_subsample_delta_pp: -2.9
      deconfounding_attributable_pp: -1.7
      normalized_ttr_trend_preserved: true
      normalized_hapax_trend_preserved: true
      normalized_rho_stronger: true
      length_is_confound: false
      dropout_short_text_bias: true
    result_rationale: >
      Length 非 primary confound。Length-depth Spearman ρ 在 [-0.066, +0.134] 范围，
      text length 不随 depth 系统性变化。Length-matched binary F1=0.724 (vs 0.770)，
      下降 4.6pp，但 random subsample control (同等 sample size reduction) F1=0.741，
      降 2.9pp。因此 4.6pp drop 中仅 ~1.7pp 可归因于 length deconfounding，
      其余 2.9pp 来自 sample size reduction。
      Length-normalized surface features (fixed-length windows 上的 TTR, hapax)
      保留且加强了 trend (|ρ| 更高)，证明 drift 信号来自 vocabulary diversity 的
      intrinsic decrease 而非 text 变长/变短。
      Dropout short text bias: deeper text 因 generation quality degradation 而更短，
      但这是 generation property (depth 的 consequence) 而非 external confound。
    tables:
      - "Table S17: Length-matched vs unmatched vs random-subsample F1"
      - "Table S18: Length distribution statistics by depth (mean, median, IQR)"
    figures_description:
      - "Fig S17: Text length distribution by depth (violin plot) — 无系统性趋势"
      - "Fig S18: Normalized feature trends — trend preserved and strengthened after length control"
    analysis: >
      Length confound 被排除 (RC10 fully addressed)。
      Paper 中报告 length-matched F1=0.724 作为 conservative estimate，
      同时说明 4.6pp drop 主要来自 sample size reduction (2.9pp) 而非 deconfounding (1.7pp)。
      Normalized features 的 stronger trend 是 positive evidence：
      控制 length 后 depth signal 更纯净。

  - name: "large_scale_generator"
    plan_id: "plan_014"
    description: "添加 7B+ generator (Qwen3-8B-Base) 测试 scale effect"
    expected_results:
      total_records: 4497
      unique_seeds: 995
      depth_distribution: {gen0: 995, gen1: 979, gen2: 937, gen3: 831, gen4: 755}
      qwen3_8b_logo_binary_f1: 0.683
      qwen3_8b_logo_3class_f1: 0.695
      qwen3_8b_ci: [0.660, 0.706]
      logo_6gen_avg_f1: 0.789
      logo_6gen_avg_binary_f1: 0.700
      delta_8b_vs_smaller_avg_pp: -1.7
      spearman_8b:
        hapax_ratio: -0.558
        ttr: -0.542
        entropy_mean: -0.475
        entropy_min: -0.303
        entropy_max: 0.095
        tail_decay: -0.089
        entropy_std: -0.076
      ddr_pattern_preserved: true
      scale_attenuation_drifting_rho: "~85% of <3B average"
      feature_importance_8b:
        hapax_ratio: 0.269
        entropy_mean: 0.164
        ttr: 0.159
    result_rationale: >
      Qwen3-8B binary F1=0.683，在 scale_8b_logo_binary_f1 [0.65, 0.70] 范围内。
      Scale effect 存在但 moderate：8B vs <3B average 降 ~1.7pp LOGO F1。
      原因：larger models 的 generation distribution 更 concentrated (lower entropy,
      tighter vocabulary, less sampling randomness at same temperature)，
      压缩了 depth-wise feature margin。Hapax ratio |ρ| 从 <3B 的 0.647 降至 8B 的 0.558
      (attenuation ~86%)：8B model 的 baseline vocabulary diversity 较低，
      depth-wise 衰减的 absolute magnitude 更小。
      DDR 模式定性不变：drifting 三特征仍为 |ρ| 最高 (hapax -0.558, ttr -0.542, entropy_mean -0.475)，
      stationary 特征仍 |ρ|<0.10 (tail_decay -0.089, entropy_max 0.095)。
      Depth distribution 显示 deeper text 更多 dropout (d4 仅 755/995)，
      比 smaller models 更显著：8B model 的 longer-context generation 更容易
      degenerate at deeper depths。
    tables:
      - "Table 7: Per-generator LOGO F1 (6 generators, 包含 Qwen3-8B)"
      - "Table S19: Spearman ρ — 8B vs <3B average by feature"
    figures_description:
      - "Fig 7: Scale effect — F1 vs generator parameter count (0.6B to 8B), showing moderate decline"
      - "Fig S19: DDR pattern at 8B — drifting/stationary 分组 preserved, magnitude attenuated"
    analysis: >
      Scale effect 诚实报告为 limitation 但 DDR 定性 robust。
      0.683 仍远优于 chance (0.50)，depth signal 在 8B scale 仍有实用价值。
      14B DDR analysis (exp_060) 进一步确认：drifting/stationary 分组在 14B 仍一致，
      |ρ| 进一步衰减 (hapax -0.507, ttr -0.492) 但分组不变。
      核心假设 "14B scale DDR 模式定性不变" 成立。

  - name: "ordinal_baseline_comparison"
    plan_id: "plan_015"
    description: "现有 detector 连续分数的 ordinal depth signal — 7-feature 相对优势验证"
    expected_results:
      seven_feature_logo_f1: 0.798
      seven_feature_ci: [0.786, 0.799]
      avg_logprob_logo_f1: 0.765
      avg_logprob_ci: [0.616, 0.820]
      avg_logprob_spearman: 0.788
      ld_score_logo_f1: 0.721
      ld_score_ci: [0.588, 0.770]
      ld_score_spearman: 0.794
      fastdetectgpt_logo_f1: 0.627
      fastdetectgpt_ci: [0.511, 0.762]
      fastdetectgpt_spearman: 0.433
      binoculars_logo_f1: 0.579
      binoculars_ci: [0.405, 0.664]
      binoculars_spearman: 0.199
      bootstrap_7feat_vs_avglogprob:
        delta_pp: 3.3
        p: 0.0
        significant: true
      bootstrap_7feat_vs_fdgpt:
        delta_pp: 6.7
        p: 0.0
        significant: true
      best_single_detector: "avg_logprob (0.765)"
      seven_feat_minus_best_single_pp: 3.3
    result_rationale: >
      7-feature 优势 3.3pp over best single detector (avg_logprob)，
      在 [3.0, 5.0] 范围内，bootstrap p=0.0 确认显著性 (n=1000)。
      Avg_logprob 是最强 single detector (F1=0.765) 因为它直接测量 NLL 均值，
      正是 drifting features 捕捉的 primary signal — avg_logprob 本质上是 entropy_mean 的
      unnormalized version。但 avg_logprob 缺少 shape features 和 surface features 的互补信号。
      LD-Score (0.721) 第二强：character-level distribution shift 与 depth 有 moderate 相关
      (ρ=0.794)，但 character-level 信息 partially redundant with word-level surface features。
      FastDetectGPT (0.627) 较弱：perturbation-based approach 设计用于 binary real/synthetic detection，
      其 log probability curvature metric 对 ordinal depth variation 不 sensitive。
      Binoculars (0.579) 最弱：two-model probability ratio 中 depth signal 被 ratio 操作
      部分 cancel (两个 model 的 NLL 均随 depth 下降，ratio 变化小)。
      7-feature 优势的来源是 complementarity：drifting features 捕捉 location shift，
      stationary features 提供 noise-resistant baseline，surface features 捕捉
      generator-agnostic vocabulary impoverishment。三组信号的 combination 优于任何 single metric。
    tables:
      - "Table 3: LOGO F1 — 7-feature vs 4 baseline detectors, with bootstrap CI and Spearman ρ"
      - "Table S20: Pairwise bootstrap significance tests (7-feature vs each detector)"
    figures_description:
      - "Fig 4: Bootstrap distributions of LOGO F1 for each method — 7-feature (rightmost) 与 avg_logprob 的 distributions 有 clear separation"
      - "Fig S20: Detector score vs depth scatter plots (4 panels) — avg_logprob 有清晰 ordinal trend, Binoculars 几乎无趋势"
    analysis: >
      3.3pp 优势虽不巨大但 statistically significant (bootstrap p<0.01)，
      符合 Findings paper 的 empirical contribution 标准。
      关键 finding 不仅是 performance gap，而是 existing detectors 确实有 moderate ordinal signal
      (avg_logprob 0.765)，但 7-feature 通过 feature complementarity 显著提升。
      这 reframes contribution：不是 "novel features" 而是
      "systematic characterization of DDR + principled feature combination"，
      符合 Findings 定位。
      Binoculars 的 bug fix (denominator correction) 确保了 fair comparison。
      Wide bootstrap CIs for single detectors (e.g. avg_logprob [0.616, 0.820])
      反映 high per-generator variance — 这本身是 7-feature 的优势
      (其 CI [0.786, 0.799] 远窄)。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a5cfcf3-117b-4407-8a58-3cc45f84a0f6",
  "isSidechain": false,
  "requestId": "req_011CbEgz5gx2RQCfrZAwaZhw",
  "type": "assistant",
  "uuid": "ca58416f-8467-49f3-9d15-fa3aefc815bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016372Gc7LYSqTNB1PScTvaH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24838,
      "cache_read_input_tokens": 11841,
      "output_tokens": 35492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 35492,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24838
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立；DDR 在 8+ generators / 5 families 上鲁棒，7-feature 优势显著，negative finding 清晰。论文按原 framing 提交 ARR。 核心假设：['DDR 二分法成立：drifting 三特征 (hapax, TTR, entropy_me…",
  "leafUuid": "ca58416f-8467-49f3-9d15-fa3aefc815bc",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate DDR robustness and depth discriminability across 8+ generators",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立；DDR 在 8+ generators / 5 families 上鲁棒，7-feature 优势显著，negative finding 清晰。论文按原 framing 提交 ARR。 核心假设：['DDR 二分法成立：drifting 三特征 (hapax, TTR, entropy_me…",
  "leafUuid": "ca58416f-8467-49f3-9d15-fa3aefc815bc",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate DDR robustness and depth discriminability across 8+ generators",
  "sessionId": "63de68ac-a99b-46a9-afd5-e6a3b61abf12"
}
```

---
