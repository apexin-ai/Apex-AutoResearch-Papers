# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。 核心假设：

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/fc89bc3c-468d-4ff9-a7c1-f5133638f03b.jsonl`
- **Structured JSON:** [`3c559473a05fc10d3f81.json`](../../sessions/3c/3c559473a05fc10d3f81.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T23:52:01.965Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T23:52:01.965Z",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。\n核心假设：[\"DDR 二分法在 ≥9 generators 下瓦解：≥3 个 'stationary' 特征出现显著 drift (|ρ|>0.15)，或 drifting 特征在 ≥7B 模型上 plateau\", 'avg_logprob 单特征在完整 LOGO 下与 7-feature 差距 <1.5pp（bootstrap 不显著）', 'Cross-model chains 无优势或更差 (binary F1 ≤ 0.70)，heterogeneity 假设被否', 'Scale 效应严重：8B+ binary F1 < 0.60，14B DDR ρ gap < 0.30', \"per-gen binary F1 方差 >15pp，部分 generator < 0.55，'generalizable depth signal' claim 不成立\", '温度 scope 实质收窄至 t=0.7 单点；cross-temperature transfer 完全失败', \"Reviewer 认为 'base models + t=0.7 + ≤14B' 的适用范围太窄，缺乏 practical impact\"]\n关键指标范围：{'logo_binary_f1_8gen': [0.62, 0.66], 'logo_binary_f1_9gen': [0.58, 0.63], 'lofo_binary_f1': [0.56, 0.63], 'cross_model_binary_f1': [0.58, 0.7], 'ddr_drifting_rho_abs_min': [0.3, 0.4], 'ddr_stationary_rho_abs_max': [0.15, 0.3], 'seven_feat_minus_best_single_pp': [0.0, 1.5], 'scale_8b_logo_binary_f1': [0.48, 0.58], 'llm_rephrase_drop_pp': [6.0, 12.0]}\n叙事方向：放弃 DDR 作为核心贡献。重构为 'Generation Depth Estimation: Task Formulation, Baselines, and Empirical Boundaries.' 三项重定位的贡献：(1) Task formulation——depth estimation 作为超越 binary detection 的新任务，含 leak-free evaluation protocol (LOGO binary metric 排除 gen-0 seed sharing)；这是 novelty 的主要来源。(2) Empirical boundary map——系统测定 depth signal 存在的条件空间 (small base models, t≤0.7, surface features) 与消失的条件空间 (instruct, high temp, ≥7B scale)；承认 avg_logprob 是 competitive baseline，7-feature 的价值在 interpretability 而非 accuracy。(3) Negative downstream finding 不变，仍是独立贡献。实质上从 method paper 转为 benchmark + analysis paper。Task novelty + 诚实的 empirical boundary mapping + negative finding 三重组合仍足以支撑 EMNLP Findings。不降级 venue。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_logo_f1: 0.7879\n    overall_ci95:\n    - 0.783\n    - 0.7929\n    spearman_entropy_max: 0.0503\n    spearman_entropy_min: -0.4061\n    spearman_hapax: -0.6467\n    spearman_ttr: -0.6302\n    spearman_entropy_mean: -0.6098\n    spearman_entropy_std: -0.1996\n    spearman_tail_decay: -0.0403\n- exp_id: plan-010-robustness\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_binary_f1: 0.695\n    5pct_binary_f1: 0.65\n    10pct_binary_f1: 0.614\n    20pct_binary_f1: 0.591\n    5pct_drop: -0.046\n    10pct_drop: -0.081\n    20pct_drop: -0.104\n- exp_id: plan-010-llm-rephrase\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_binary_f1: 0.6918\n    original_binary_ci:\n    - 0.6749\n    - 0.7067\n    original_multiclass_f1: 0.7385\n    original_multiclass_ci:\n    - 0.7269\n    - 0.7496\n    rephrased_binary_f1: 0.6471\n    rephrased_binary_ci:\n    - 0.6308\n    - 0.6619\n    rephrased_multiclass_f1: 0.6672\n    rephrased_multiclass_ci:\n    - 0.6548\n    - 0.6796\n    binary_drop: -0.0447\n    multiclass_drop: -0.0713\n    edit_distance_ratio: 0.5071\n    avg_sentences_replaced: 1.69\n    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\n    bugs_fixed:\n    - binary_task_gen1_vs_gen2+\n    - 3class_mapping\n    - tail_decay_rank100-1000\n- exp_id: plan-008-seed-stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_complexity_binary: 0.685\n    medium_binary: 0.695\n    high_complexity_binary: 0.695\n    low_complexity_multi: 0.772\n    medium_multi: 0.778\n    high_complexity_multi: 0.779\n    max_diff_binary_pp: 1.06\n    max_diff_multiclass_pp: 0.68\n    conclusion_label: seed_independent\n- exp_id: multi-domain-seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7459\n    news_binary_ci:\n    - 0.726\n    - 0.764\n    news_multiclass_f1: 0.6516\n    academic_binary_f1: 0.7386\n    academic_binary_ci:\n    - 0.72\n    - 0.757\n    academic_multiclass_f1: 0.6223\n    code_binary_f1: 0.7535\n    code_binary_ci:\n    - 0.737\n    - 0.77\n    code_multiclass_f1: 0.6344\n    wikipedia_baseline_binary_f1: 0.8148\n    wikipedia_baseline_multiclass_f1: 0.8632\n    max_gap_vs_wiki_pp: 7.62\n    worst_domain: academic\n    best_domain: code\n    conclusion_label: domain_independent\n- exp_id: exp_047_multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7119\n    news_binary_ci:\n    - 0.6898\n    - 0.7332\n    news_3class_f1: 0.7149\n    academic_binary_f1: 0.6279\n    academic_binary_ci:\n    - 0.6027\n    - 0.6515\n    academic_3class_f1: 0.6564\n    code_binary_f1: 0.6872\n    code_binary_ci:\n    - 0.6641\n    - 0.71\n    code_3class_f1: 0.6729\n    overall_binary_f1: 0.6757\n    overall_3class_f1: 0.6814\n    delta_vs_t10_news: -0.034\n    delta_vs_t10_academic: -0.1107\n    delta_vs_t10_code: -0.0663\n- exp_id: multi_domain_t07\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_048_cross_temp_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    6gen_logo:\n      within_0.7_binary: 0.9471\n      within_0.7_3class: 0.7888\n      cross_0.7to1.0_binary: 0.9001\n      cross_0.7to1.0_3class: 0.7225\n      within_1.0_binary: 0.9107\n      within_1.0_3class: 0.7257\n      cross_1.0to0.7_binary: 0.9581\n      cross_1.0to0.7_3class: 0.7913\n      caveat: Only Qwen3-1.7B differs between conditions; 5/6 generators share data\n    qwen_only:\n      within_0.7_binary: 0.9262\n      within_0.7_binary_ci:\n      - 0.916\n      - 0.935\n      within_0.7_3class: 0.769\n      within_0.7_3class_ci:\n      - 0.756\n      - 0.781\n      cross_0.7to1.0_binary: 0.7574\n      cross_0.7to1.0_binary_ci:\n      - 0.745\n      - 0.77\n      cross_0.7to1.0_3class: 0.4581\n      cross_0.7to1.0_3class_ci:\n      - 0.445\n      - 0.472\n      within_1.0_binary: 0.8248\n      within_1.0_binary_ci:\n      - 0.81\n      - 0.838\n      within_1.0_3class: 0.5738\n      within_1.0_3class_ci:\n      - 0.56\n      - 0.588\n      cross_1.0to0.7_binary: 0.9443\n      cross_1.0to0.7_binary_ci:\n      - 0.936\n      - 0.953\n      cross_1.0to0.7_3class: 0.6014\n      cross_1.0to0.7_3class_ci:\n      - 0.593\n      - 0.611\n      delta_0.7train_binary_pp: -16.9\n      delta_0.7train_3class_pp: -31.1\n      delta_1.0train_binary_pp: 12\n      delta_1.0train_3class_pp: 2.8\n      asymmetric_transfer: true\n- exp_id: exp_049_temp_curve_t05\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 4708\n    skipped: 113\n    seeds: 995\n    model: pythia-2.8b\n    temperature: 0.5\n    top_p: 0.9\n    within_cv_binary_f1: 0.8432\n    within_cv_binary_ci:\n    - 0.8301\n    - 0.8558\n    logo_binary_f1: 0.8136\n    logo_binary_ci:\n    - 0.7984\n    - 0.8282\n    entropy_mean_rho: -0.5844\n- exp_id: exp_050_temp_curve_t09\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    records: 4536\n    model: pythia-2.8b\n    temperature: 0.9\n    top_p: 0.9\n    within_cv_binary_f1: 0.5821\n    within_cv_binary_ci:\n    - 0.5655\n    - 0.5985\n    logo_binary_f1: 0.4804\n    logo_binary_ci:\n    - 0.4645\n    - 0.4976\n    entropy_mean_rho: -0.3016\n    delta_vs_t07_cv: -0.157\n    delta_vs_t07_logo: -0.259\n- exp_id: exp_051_independent_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_to_olmo_binary_f1: 0.6945\n    pythia_to_olmo_ci:\n    - 0.6727\n    - 0.7167\n    olmo_to_pythia_binary_f1: 0.666\n    olmo_to_pythia_ci:\n    - 0.6429\n    - 0.6893\n    avg_binary_f1: 0.6803\n    shared_seed_logo_ref: 0.694\n    delta_vs_shared: -0.014\n- exp_id: exp_052_instruct_qwen3_1_7b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8753\n    within_binary_ci:\n    - 0.8667\n    - 0.8837\n    within_3class_f1: 0.7324\n    within_3class_ci:\n    - 0.7195\n    - 0.745\n    base_binary_f1: 0.8614\n    base_3class_f1: 0.769\n    logo_instruct_binary: 0.658\n    logo_instruct_3class: 0.543\n    logo_base_binary: 0.821\n    logo_base_3class: 0.802\n    gen1_f1_instruct: 0.438\n    gen1_f1_base: 0.579\n    spearman_direction: reversed (instruct ρ>0, base ρ<0)\n    delta_within_binary: 0.014\n    delta_within_3class: -0.037\n    delta_logo_binary: -0.163\n- exp_id: exp_053_instruct_olmo2_1b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8131\n    within_binary_ci:\n    - 0.8012\n    - 0.8251\n    within_3class_f1: 0.5748\n    within_3class_ci:\n    - 0.5605\n    - 0.5897\n    base_binary_f1: 0.8454\n    base_3class_f1: 0.7538\n    gen1_f1_instruct: 0.256\n    gen1_f1_base: 0.523\n    delta_within_binary: -0.032\n    delta_within_3class: -0.179\n    spearman_instruct:\n      entropy_mean: 0.482\n      entropy_std: 0.296\n      entropy_min: 0.08\n      entropy_max: 0.306\n      tail_decay: 0.228\n      ttr: 0.006\n      hapax_ratio: 0.025\n    spearman_base:\n      entropy_mean: -0.639\n      entropy_std: -0.296\n      entropy_min: -0.387\n      entropy_max: 0.067\n      tail_decay: -0.141\n      ttr: -0.7\n      hapax_ratio: -0.712\n    features_reversed: 6/7\n    model_used: allenai/OLMo-2-0425-1B-Instruct\n- exp_id: exp_054_instruct_llama3_2_3b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    instruct_binary_f1: 0.8381\n    instruct_binary_ci:\n    - 0.828\n    - 0.847\n    instruct_3class_f1: 0.5437\n    instruct_3class_ci:\n    - 0.53\n    - 0.558\n    base_binary_f1: 0.8488\n    base_3class_f1: 0.7424\n    rho_instruct_entropy_mean: 0.2299\n    rho_instruct_entropy_std: 0.2623\n    rho_instruct_entropy_min: -0.0027\n    rho_instruct_entropy_max: 0.2036\n    rho_instruct_tail_decay: 0.1198\n    rho_instruct_ttr: -0.1411\n    rho_instruct_hapax_ratio: -0.1157\n    rho_base_entropy_mean: -0.627\n    rho_base_ttr: -0.6856\n    rho_base_hapax_ratio: -0.6975\n    direction_reversals: 3\n    reversed_features:\n    - entropy_mean\n    - entropy_std\n    - tail_decay\n    data_count: 4974\n- exp_id: exp_055_qlora_olmo_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8881\n    macro_f1_3class_std: 0.0071\n    macro_f1_5class: 0.5976\n    macro_f1_5class_std: 0.0046\n    binary_f1: 0.8363\n    binary_f1_std: 0.0096\n    n_samples: 4429\n    runtime_seconds: 1689.7\n- exp_id: exp_056_qlora_qwen_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.9066\n    macro_f1_3class_std: 0.0082\n    macro_f1_5class: 0.5514\n    macro_f1_5class_std: 0.0031\n    binary_f1: 0.8672\n    binary_f1_std: 0.0137\n    n_samples: 4963\n    runtime_seconds: 1880.5\n- exp_id: exp_055b_qlora_olmo_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8588\n    macro_f1_3class_std: 0.0036\n    macro_f1_5class: 0.5398\n    macro_f1_5class_std: 0.015\n    binary_f1: 0.7925\n    binary_f1_std: 0.0097\n    n_samples: 2379\n    runtime_seconds: 911.7\n    note: completed before kill signal\n- exp_id: exp_056b_qlora_qwen_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.904\n    macro_f1_3class_std: 0.0094\n    macro_f1_5class: 0.5544\n    macro_f1_5class_std: 0.0068\n    binary_f1: 0.8597\n    binary_f1_std: 0.0123\n    n_samples: 2291\n    runtime_seconds: 880.9\n    note: completed before kill signal\n- exp_id: exp_057_scale_9gen_logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: superseded by exp_057 (rerun with fixed Gemma data)\n    first_run_3class_f1: 0.7516\n    first_run_binary_f1: 0.6842\n    see_exp_057_for_final: true\n- exp_id: exp_058_ddr_causality\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    permutation_baseline_f1: 0.7714\n    drifting_avg_importance: 0.1578\n    stationary_avg_importance: 0.0297\n    drifting_stationary_ratio: 5.31\n    granger_significant_features: 6/7\n    granger_max_delta_r2: 0.031\n    granger_max_delta_r2_feature: entropy_std\n    granger_nonsig_feature: entropy_min\n    granger_panel_n: 29095\n    intervention_max_f1_drop: 0.0203\n    intervention_max_feature: entropy_max\n    intervention_min_f1_drop: 0.0061\n- exp_id: exp_059_tost_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_bootstrap: 1000\n    seed: 42\n    margin_d: 0.2\n    entropy_max:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.062\n      d_ci:\n      - 0.037\n      - 0.088\n    entropy_min:\n      median_p: 0\n      rejection_rate: 1\n      median_d: -0.016\n      d_ci:\n      - -0.042\n      - 0.011\n    tail_decay:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.088\n      d_ci:\n      - 0.065\n      - 0.111\n    entropy_std:\n      median_p: 1\n      rejection_rate: 0\n      median_d: 0.458\n      d_ci:\n      - 0.435\n      - 0.479\n    stationary_features_robust: true\n- exp_id: exp_057\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    9gen_logo_3class_f1: 0.751\n    9gen_logo_binary_f1: 0.6661\n    8gen_baseline_3class_f1: 0.7698\n    delta_9gen_vs_8gen: -0.0188\n    n_total_rows: 42015\n    n_generators: 9\n    qwen3_8b_3class_f1: 0.6955\n    qwen3_8b_binary_f1: 0.6468\n    gemma_2_2b_3class_f1: 0.6279\n    gemma_2_2b_binary_f1: 0.4402\n    per_gen_3class_f1:\n      pythia-1b: 0.8571\n      qwen3-0.6b: 0.8185\n      pythia-2.8b: 0.8117\n      qwen3-1.7b: 0.8114\n      olmo-2-1b: 0.7732\n      llama-3.2-3b: 0.7591\n      qwen3-8b: 0.6955\n      gemma-2-2b: 0.6279\n      mistral-7b-v0.3: 0.6045\n    tail_decay_consistency: VERIFIED_all_9gen_logprob_slope\n    data_source: features_9gen.csv (42015 rows, Gemma fixed)\n- exp_id: exp_060_14b_ddr_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 2229\n    n_seeds: 498\n    depth_distribution:\n      '0': 498\n      '1': 488\n      '2': 466\n      '3': 414\n      '4': 363\n    entropy_mean:\n      rho: -0.3877\n      d: 0.7765\n      group: drifting\n    entropy_std:\n      rho: -0.0557\n      d: -0.0223\n      group: stationary\n    entropy_max:\n      rho: 0.0791\n      d: -0.1717\n      group: stationary\n    entropy_min:\n      rho: -0.2471\n      d: -0.1365\n      group: stationary\n    ttr:\n      rho: -0.4916\n      d: 1.0913\n      group: drifting\n    hapax_ratio:\n      rho: -0.5065\n      d: 1.1245\n      group: drifting\n    tail_decay:\n      rho: -0.0637\n      d: 0.1356\n      group: stationary\n    ddr_pattern_match: true\n- exp_id: exp_061_instruct_ref_ddr\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwen_instruct:\n      base_ref_rho_entropy_mean: 0.478\n      instruct_ref_rho_entropy_mean: 0.221\n      base_ref_d_entropy_mean: 1.981\n      instruct_ref_d_entropy_mean: 1.022\n    olmo_instruct:\n      base_ref_rho_entropy_mean: 0.482\n      instruct_ref_rho_entropy_mean: -0.113\n      base_ref_d_entropy_mean: 1.33\n      instruct_ref_d_entropy_mean: 0.017\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T23:52:01.968Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T23:52:01.968Z",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-20T23:52:01.988Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。
核心假设：["DDR 二分法在 ≥9 generators 下瓦解：≥3 个 'stationary' 特征出现显著 drift (|ρ|>0.15)，或 drifting 特征在 ≥7B 模型上 plateau", 'avg_logprob 单特征在完整 LOGO 下与 7-feature 差距 <1.5pp（bootstrap 不显著）', 'Cross-model chains 无优势或更差 (binary F1 ≤ 0.70)，heterogeneity 假设被否', 'Scale 效应严重：8B+ binary F1 < 0.60，14B DDR ρ gap < 0.30', "per-gen binary F1 方差 >15pp，部分 generator < 0.55，'generalizable depth signal' claim 不成立", '温度 scope 实质收窄至 t=0.7 单点；cross-temperature transfer 完全失败', "Reviewer 认为 'base models + t=0.7 + ≤14B' 的适用范围太窄，缺乏 practical impact"]
关键指标范围：{'logo_binary_f1_8gen': [0.62, 0.66], 'logo_binary_f1_9gen': [0.58, 0.63], 'lofo_binary_f1': [0.56, 0.63], 'cross_model_binary_f1': [0.58, 0.7], 'ddr_drifting_rho_abs_min': [0.3, 0.4], 'ddr_stationary_rho_abs_max': [0.15, 0.3], 'seven_feat_minus_best_single_pp': [0.0, 1.5], 'scale_8b_logo_binary_f1': [0.48, 0.58], 'llm_rephrase_drop_pp': [6.0, 12.0]}
叙事方向：放弃 DDR 作为核心贡献。重构为 'Generation Depth Estimation: Task Formulation, Baselines, and Empirical Boundaries.' 三项重定位的贡献：(1) Task formulation——depth estimation 作为超越 binary detection 的新任务，含 leak-free evaluation protocol (LOGO binary metric 排除 gen-0 seed sharing)；这是 novelty 的主要来源。(2) Empirical boundary map——系统测定 depth signal 存在的条件空间 (small base models, t≤0.7, surface features) 与消失的条件空间 (instruct, high temp, ≥7B scale)；承认 avg_logprob 是 competitive baseline，7-feature 的价值在 interpretability 而非 accuracy。(3) Negative downstream finding 不变，仍是独立贡献。实质上从 method paper 转为 benchmark + analysis paper。Task novelty + 诚实的 empirical boundary mapping + negative finding 三重组合仍足以支撑 EMNLP Findings。不降级 venue。

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
  "promptId": "b522a379-46f0-402c-b39d-4f606e12c539",
  "type": "user",
  "uuid": "3822041b-d6a9-46ca-9350-072c5caed9e4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T23:52:01.987Z_

```json
{
  "parentUuid": "3822041b-d6a9-46ca-9350-072c5caed9e4",
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
  "uuid": "dc6913d3-527f-4686-9cbb-e39bbb3c0149",
  "timestamp": "2026-05-20T23:52:01.987Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T23:52:01.987Z_

```json
{
  "parentUuid": "dc6913d3-527f-4686-9cbb-e39bbb3c0149",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7f485d44-da8b-403a-80aa-f07da1dc6ad3",
  "timestamp": "2026-05-20T23:52:01.987Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。 核心假设：[\"DDR 二分法在 ≥9 generators 下瓦解：≥3 个 'stationary' 特征出现显著 drift (|ρ|>0.15)，或 drifti…",
  "leafUuid": "7f485d44-da8b-403a-80aa-f07da1dc6ad3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Worst-case scenario analysis for generation depth fingerprinting",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b"
}
```

---

### Assistant

_source line 8 · 2026-05-20T23:52:06.136Z_

I'll analyze the experiment plan and project context to generate detailed worst-tier predictions for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f485d44-da8b-403a-80aa-f07da1dc6ad3",
  "isSidechain": false,
  "requestId": "req_011CbEih7b4UFjxTmeJauKVW",
  "type": "assistant",
  "uuid": "4e9c7dc5-0d93-49ac-9d45-54316df7927f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N45yzuLpqGtsRN672ysvQR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 36722,
      "output_tokens": 234,
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
          "input_tokens": 2,
          "output_tokens": 234,
          "cache_read_input_tokens": 36722,
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

### Tool call

_source line 9 · 2026-05-20T23:52:09.936Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AfREeAcXLfbXiyEhbyMyDj`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore experiment plan details",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_3, I need to understand the full experiment plan and any additional context files. Search for:\n1. Any files named experiment_plan* or plan* in YAML/JSON/MD format\n2. Any files in a \"plans\" or \"experiments\" directory\n3. paper_framing.md\n4. Any registry files\n5. CLAUDE.md or similar project documentation\n\nReport file paths and key content summaries. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e9c7dc5-0d93-49ac-9d45-54316df7927f",
  "isSidechain": false,
  "requestId": "req_011CbEih7b4UFjxTmeJauKVW",
  "type": "assistant",
  "uuid": "348b83b5-16ee-4c35-804a-7ba7fc6d1ef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N45yzuLpqGtsRN672ysvQR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 36722,
      "output_tokens": 234,
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
          "input_tokens": 2,
          "output_tokens": 234,
          "cache_read_input_tokens": 36722,
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

### Tool result

_source line 10 · 2026-05-20T23:53:05.845Z_

<details><summary>↩ Tool result · `toolu_01AfREeAcXLfbXiyEhbyMyDj`</summary>

```text
Perfect! Now I have a comprehensive understanding. Let me compile a thorough report.

## Summary: Full Experiment Plan & Context for gen-depth-fingerprint

### Key Documentation Files Found

**Top-level Project Documentation:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md` — Core research framing (12KB)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md` — Current research dashboard and timeline (3.6KB)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md` — Key experimental findings and constraints (8KB)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md` — Claude session context with project rules & worker operations (80KB)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/AGENTS.md` — Agent role definitions (16KB)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/.claude/CLAUDE.md` — Global style and output rules (9KB)

**Decision Tracking:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml` — 34 numbered decisions (D001–D033) documenting research direction changes, framing adjustments, and GPU allocation decisions

**Registry & Checkpoint Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml` — Experiment registry with 39 completed experiments (mvp-001 through exp_059)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/checkpoints/` — Status checkpoints for 100+ job submissions (plan-001 through plan-002-*); latest shows plan-002-* tasks completed/done

**Paper Output:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/` — Latest (2026-05-20) dream report with final paper.pdf (174KB), paper_framing.md, review_report.md, experiment_data.json

---

### Research Experiment Plan Overview

**Project:** `gen-depth-fingerprint` — LLM generation depth fingerprinting via distributional features

**Primary Goal:** Classify LLM text by generation depth (gen-0/gen-1/gen-2+) using distributional features, addressing data contamination in training corpora.

**Status:** Paper version 35 complete; awaiting user submission approval (5 days to EMNLP 2026 Findings deadline: May 25, 2026)

---

### Core Experiment Phases

**Phase 1 — MVP (plan-001, May 14)**
- **Hypothesis:** Pythia-410M distributional features can classify Pythia-2.8B continuation chains (gen-0/gen-1/gen-2+)
- **Result:** PASS — 3-class macro F1=0.8408, binary F1=0.8653 (gen-0 vs gen-2+), far exceeding thresholds (0.45, 0.65)
- **Checkpoint:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/checkpoints/plan-001_DONE_20260514T185401.json`

**Phase 2 — Ablation & Dual Dynamics (plan-001-fix, exp_001–exp_010)**
- **Hypothesis:** Distribution features (entropy, TTR, hapax) provide signal independent of surface statistics
- **Key Finding:** Surface-only F1=0.688, reference-only F1=0.713, full 7-feature F1=0.773 (McNemar p≈0). Shape features (entropy_max, tail_decay) remain ~stationary while central-tendency features (entropy_mean, TTR, hapax) drift with depth — reframed as "differential depth response (DDR)" + "feature complementarity" rather than pure independence.
- **Decision:** D004 — Pivot from "Fingerprint Independence" to "Dual Dynamics" framing

**Phase 3 — Cross-Generator Generalization (plan-002, exp_002–exp_030)**
- **Hypothesis:** 7-feature ensemble trained on 8 generators (Pythia-1B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B, Llama-3.2-3B, Mistral-7B) generalizes across unseen generators
- **Metrics:**
  - Leave-one-generator-out (LOGO) binary F1 = 0.694 [0.688, 0.700] (primary metric, leak-free)
  - Leave-one-family-out (LOFO) binary F1 = 0.686
  - Cross-model chains (heterogeneous generators per depth) binary F1 = 0.764
  - Per-generator range: 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B)
- **Models tested:** Pythia, OLMo, Qwen3, Llama, Mistral (0.6B–8B scale range)

**Phase 4 — Scope & Limitations (exp_031–exp_055)**
- **Temperature sensitivity:** Reliable ±1pp within t ∈ [0.5, 0.9]; at t=1.0 degrades 6pp (entropy_mean ρ→−0.002)
- **Instruction-tuning degradation:** OLMo-Instruct LOGO F1=0.338 vs 0.763 base (primary scope limitation)
- **Scale effect:** Larger models compress feature margins (Qwen3-8B: 0.692 vs Pythia-1B: 0.857)
- **Prompt-type dependence:** Continuation chains (F1=0.781) > elaboration (F1=0.730)
- **Length confound:** Length-matched binary F1=0.724 vs unmatched 0.770 (deconfounding, not sample effect)

**Phase 5 — Downstream Utility (plan-004-v2, exp_026–exp_028)**
- **Hypothesis:** Depth-aware data curation improves downstream CLM quality
- **Result:** NEGATIVE FINDING — random subsampling (ppl=2.367) ≡ depth 0–1 (2.387) ≡ binary-filtered (2.389) at ±2% equivalence margin (TOST p=1.1×10⁻⁴). Reframed as "diagnostic tool" (provenance labeling), not "curative tool" (data selection).

**Phase 6 — Late-Stage Robustness (exp_056–exp_059, May 19–20)**
- **9-gen LOGO expansion** (exp_057): +Gemma-2-2B; 9-gen 3-class F1=0.751 (−0.019 vs 8-gen); Gemma gen-1 anomaly (F1=0.036)
- **DDR causality** (exp_058): Granger significance 6/7 features; permutation importance drifting 0.158 vs stationary 0.030 (5.3× gap); intervention: all features drop 0.6–2.0pp
- **TOST bootstrap** (exp_059): 1000 iterations, stationary features 100% rejection rate (robust equivalence)

---

### Experiment Execution Infrastructure

**Job Scheduling System:**
- Checkpoints track state transitions (PREPARING → PENDING → QUEUED → ALLOCATED → RUNNING → ANALYZING → DONE)
- Naming convention: `plan-{id}[-variant]_{state}_{timestamp}.json`
- Total plan-002 spawned 30+ variant jobs across rounds (round1: Pythia-1B/OLMo-2-1B; round2: Qwen3 series) with retry logic for CUDA errors

**Hardware:**
- Server: AutoDL RTX 5090 (4× GPU, cuda:0–3)
- Constraint: Only 1 GPU visible per container; all multi-GPU jobs run serialized
- Current allocation: 4 cards reserved for emergency re-runs; D033 confirmed no further GPU experiments needed (DDL = 5 days away)

---

### Key Metrics & Claims (Findings-level positioning)

**Claim 1 — Depth Discriminability:** 7-feature ensemble, leak-free binary F1=0.694 (gen-1 vs gen-2+) under 8-gen LOGO; 0.686 LOFO; 0.830 cross-model chains.

**Claim 2 — Differential Depth Response & Feature Complementarity:** DDR confirmed (drifting ρ>0.60, stationary ρ<0.10); KS stats ~10× gap. Full 7-feature (0.773) >> surface-only (0.688) + reference-only (0.713; McNemar p≈0).

**Claim 3 (negative):** Depth-aware curation ≡ random subsampling for downstream CLM quality (TOST p=1.1×10⁻⁴).

---

### Paper Framing & Venue Strategy

**Target Venue:** EMNLP 2026 Findings (ARR, deadline May 25, 2026)
- Positioning: Empirical characterization + novel task formulation (generation depth classification beyond binary detection)
- 8-page main text limit (now at ≤8 pages per v35 compilation check)
- Anticipated reviewer concerns pre-answered (vocabulary impoverishment, generalization beyond Pythia, ecological validity, human editing robustness)

**Latest Dream Report (2026-05-20 10:27 UTC):**
- Paper version: v35 final (PDF 174KB)
- Status: 0 compilation errors, 32 pages total
- Review outcome: Reviewer R29 identified structure/framing gaps (not experimental), leading to D032 decision: reframe contribution as diagnostic (not curative)
- Next step: Awaiting user decision on resubmit or direct submission

---

### Experiment Scripts & Tools

**Core Experiment Scripts:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ablation_analysis.py` — Feature ablation (H1/H2 split)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/cross_generator_eval.py` — LOGO/LOFO evaluation
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/cross_model_chains.py` — Heterogeneous generator chains
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/cross_temp_transfer.py` — Temperature sensitivity
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/detector_baseline.py` — Multi-detector ensemble comparison
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/end_to_end_classifier.py` — 7-feature XGBoost pipeline
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/multi_domain_seeds.py` — Ecological validity (4 domains: news, Wikipedia, scientific, creative)

---

### Critical Constraints & Decisions (Memory)

**tail_decay consistency fix** (2026-05-20): Original 6 generators used log-prob slope; new 3 (Llama/Mistral/Gemma) had incorrect NLL proportion metric — corrected in exp_057 (9-gen LOGO rerun).

**Seed-sharing leakage:** Gen-0 task formulation evaluates 3-class F1 inflated by shared seed between train/test (D006). Primary metric = leak-free binary F1 (gen-1 vs gen-2+).

**GPU reserve decision** (D033): 4 RTX 5090 cards held in reserve until submission; no new GPU experiments justified (all 8 ablation dimensions evaluated, 39 experiments completed).

**Model versions confirmed:** Pythia-1B/2.8B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B, Llama-3.2-3B, Mistral-7B (base models only; instruction-tuned variants show degraded signal).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "348b83b5-16ee-4c35-804a-7ba7fc6d1ef8",
  "isSidechain": false,
  "promptId": "b522a379-46f0-402c-b39d-4f606e12c539",
  "type": "user",
  "uuid": "34fd325c-320d-49ea-b341-d3111fcd9587",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_3, I need to understand the full experiment plan and any additional context files. Search for:\n1. Any files named experiment_plan* or plan* in YAML/JSON/MD format\n2. Any files in a \"plans\" or \"experiments\" directory\n3. paper_framing.md\n4. Any registry files\n5. CLAUDE.md or similar project documentation\n\nReport file paths and key content summaries. Search breadth: medium.",
    "agentId": "ac9795183fff15bf0",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have a comprehensive understanding. Let me compile a thorough report.\n\n## Summary: Full Experiment Plan & Context for gen-depth-fingerprint\n\n### Key Documentation Files Found\n\n**Top-level Project Documentation:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md` — Core research framing (12KB)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md` — Current research dashboard and timeline (3.6KB)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md` — Key experimental findings and constraints (8KB)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md` — Claude session context with project rules & worker operations (80KB)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/AGENTS.md` — Agent role definitions (16KB)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/.claude/CLAUDE.md` — Global style and output rules (9KB)\n\n**Decision Tracking:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml` — 34 numbered decisions (D001–D033) documenting research direction changes, framing adjustments, and GPU allocation decisions\n\n**Registry & Checkpoint Files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml` — Experiment registry with 39 completed experiments (mvp-001 through exp_059)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/checkpoints/` — Status checkpoints for 100+ job submissions (plan-001 through plan-002-*); latest shows plan-002-* tasks completed/done\n\n**Paper Output:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/` — Latest (2026-05-20) dream report with final paper.pdf (174KB), paper_framing.md, review_report.md, experiment_data.json\n\n---\n\n### Research Experiment Plan Overview\n\n**Project:** `gen-depth-fingerprint` — LLM generation depth fingerprinting via distributional features\n\n**Primary Goal:** Classify LLM text by generation depth (gen-0/gen-1/gen-2+) using distributional features, addressing data contamination in training corpora.\n\n**Status:** Paper version 35 complete; awaiting user submission approval (5 days to EMNLP 2026 Findings deadline: May 25, 2026)\n\n---\n\n### Core Experiment Phases\n\n**Phase 1 — MVP (plan-001, May 14)**\n- **Hypothesis:** Pythia-410M distributional features can classify Pythia-2.8B continuation chains (gen-0/gen-1/gen-2+)\n- **Result:** PASS — 3-class macro F1=0.8408, binary F1=0.8653 (gen-0 vs gen-2+), far exceeding thresholds (0.45, 0.65)\n- **Checkpoint:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/checkpoints/plan-001_DONE_20260514T185401.json`\n\n**Phase 2 — Ablation & Dual Dynamics (plan-001-fix, exp_001–exp_010)**\n- **Hypothesis:** Distribution features (entropy, TTR, hapax) provide signal independent of surface statistics\n- **Key Finding:** Surface-only F1=0.688, reference-only F1=0.713, full 7-feature F1=0.773 (McNemar p≈0). Shape features (entropy_max, tail_decay) remain ~stationary while central-tendency features (entropy_mean, TTR, hapax) drift with depth — reframed as \"differential depth response (DDR)\" + \"feature complementarity\" rather than pure independence.\n- **Decision:** D004 — Pivot from \"Fingerprint Independence\" to \"Dual Dynamics\" framing\n\n**Phase 3 — Cross-Generator Generalization (plan-002, exp_002–exp_030)**\n- **Hypothesis:** 7-feature ensemble trained on 8 generators (Pythia-1B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B, Llama-3.2-3B, Mistral-7B) generalizes across unseen generators\n- **Metrics:**\n  - Leave-one-generator-out (LOGO) binary F1 = 0.694 [0.688, 0.700] (primary metric, leak-free)\n  - Leave-one-family-out (LOFO) binary F1 = 0.686\n  - Cross-model chains (heterogeneous generators per depth) binary F1 = 0.764\n  - Per-generator range: 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B)\n- **Models tested:** Pythia, OLMo, Qwen3, Llama, Mistral (0.6B–8B scale range)\n\n**Phase 4 — Scope & Limitations (exp_031–exp_055)**\n- **Temperature sensitivity:** Reliable ±1pp within t ∈ [0.5, 0.9]; at t=1.0 degrades 6pp (entropy_mean ρ→−0.002)\n- **Instruction-tuning degradation:** OLMo-Instruct LOGO F1=0.338 vs 0.763 base (primary scope limitation)\n- **Scale effect:** Larger models compress feature margins (Qwen3-8B: 0.692 vs Pythia-1B: 0.857)\n- **Prompt-type dependence:** Continuation chains (F1=0.781) > elaboration (F1=0.730)\n- **Length confound:** Length-matched binary F1=0.724 vs unmatched 0.770 (deconfounding, not sample effect)\n\n**Phase 5 — Downstream Utility (plan-004-v2, exp_026–exp_028)**\n- **Hypothesis:** Depth-aware data curation improves downstream CLM quality\n- **Result:** NEGATIVE FINDING — random subsampling (ppl=2.367) ≡ depth 0–1 (2.387) ≡ binary-filtered (2.389) at ±2% equivalence margin (TOST p=1.1×10⁻⁴). Reframed as \"diagnostic tool\" (provenance labeling), not \"curative tool\" (data selection).\n\n**Phase 6 — Late-Stage Robustness (exp_056–exp_059, May 19–20)**\n- **9-gen LOGO expansion** (exp_057): +Gemma-2-2B; 9-gen 3-class F1=0.751 (−0.019 vs 8-gen); Gemma gen-1 anomaly (F1=0.036)\n- **DDR causality** (exp_058): Granger significance 6/7 features; permutation importance drifting 0.158 vs stationary 0.030 (5.3× gap); intervention: all features drop 0.6–2.0pp\n- **TOST bootstrap** (exp_059): 1000 iterations, stationary features 100% rejection rate (robust equivalence)\n\n---\n\n### Experiment Execution Infrastructure\n\n**Job Scheduling System:**\n- Checkpoints track state transitions (PREPARING → PENDING → QUEUED → ALLOCATED → RUNNING → ANALYZING → DONE)\n- Naming convention: `plan-{id}[-variant]_{state}_{timestamp}.json`\n- Total plan-002 spawned 30+ variant jobs across rounds (round1: Pythia-1B/OLMo-2-1B; round2: Qwen3 series) with retry logic for CUDA errors\n\n**Hardware:**\n- Server: AutoDL RTX 5090 (4× GPU, cuda:0–3)\n- Constraint: Only 1 GPU visible per container; all multi-GPU jobs run serialized\n- Current allocation: 4 cards reserved for emergency re-runs; D033 confirmed no further GPU experiments needed (DDL = 5 days away)\n\n---\n\n### Key Metrics & Claims (Findings-level positioning)\n\n**Claim 1 — Depth Discriminability:** 7-feature ensemble, leak-free binary F1=0.694 (gen-1 vs gen-2+) under 8-gen LOGO; 0.686 LOFO; 0.830 cross-model chains.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity:** DDR confirmed (drifting ρ>0.60, stationary ρ<0.10); KS stats ~10× gap. Full 7-feature (0.773) >> surface-only (0.688) + reference-only (0.713; McNemar p≈0).\n\n**Claim 3 (negative):** Depth-aware curation ≡ random subsampling for downstream CLM quality (TOST p=1.1×10⁻⁴).\n\n---\n\n### Paper Framing & Venue Strategy\n\n**Target Venue:** EMNLP 2026 Findings (ARR, deadline May 25, 2026)\n- Positioning: Empirical characterization + novel task formulation (generation depth classification beyond binary detection)\n- 8-page main text limit (now at ≤8 pages per v35 compilation check)\n- Anticipated reviewer concerns pre-answered (vocabulary impoverishment, generalization beyond Pythia, ecological validity, human editing robustness)\n\n**Latest Dream Report (2026-05-20 10:27 UTC):**\n- Paper version: v35 final (PDF 174KB)\n- Status: 0 compilation errors, 32 pages total\n- Review outcome: Reviewer R29 identified structure/framing gaps (not experimental), leading to D032 decision: reframe contribution as diagnostic (not curative)\n- Next step: Awaiting user decision on resubmit or direct submission\n\n---\n\n### Experiment Scripts & Tools\n\n**Core Experiment Scripts:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ablation_analysis.py` — Feature ablation (H1/H2 split)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/cross_generator_eval.py` — LOGO/LOFO evaluation\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/cross_model_chains.py` — Heterogeneous generator chains\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/cross_temp_transfer.py` — Temperature sensitivity\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/detector_baseline.py` — Multi-detector ensemble comparison\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/end_to_end_classifier.py` — 7-feature XGBoost pipeline\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/multi_domain_seeds.py` — Ecological validity (4 domains: news, Wikipedia, scientific, creative)\n\n---\n\n### Critical Constraints & Decisions (Memory)\n\n**tail_decay consistency fix** (2026-05-20): Original 6 generators used log-prob slope; new 3 (Llama/Mistral/Gemma) had incorrect NLL proportion metric — corrected in exp_057 (9-gen LOGO rerun).\n\n**Seed-sharing leakage:** Gen-0 task formulation evaluates 3-class F1 inflated by shared seed between train/test (D006). Primary metric = leak-free binary F1 (gen-1 vs gen-2+).\n\n**GPU reserve decision** (D033): 4 RTX 5090 cards held in reserve until submission; no new GPU experiments justified (all 8 ablation dimensions evaluated, 39 experiments completed).\n\n**Model versions confirmed:** Pythia-1B/2.8B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B, Llama-3.2-3B, Mistral-7B (base models only; instruction-tuned variants show degraded signal)."
      }
    ],
    "totalDurationMs": 55902,
    "totalTokens": 60982,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1527,
      "cache_read_input_tokens": 56238,
      "output_tokens": 3210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1527
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3210,
          "cache_read_input_tokens": 56238,
          "cache_creation_input_tokens": 1527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1527,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 6,
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "348b83b5-16ee-4c35-804a-7ba7fc6d1ef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T23:53:08.692Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NmdRoYeHPojXVqBGNn5JU8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml",
  "offset": 0,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34fd325c-320d-49ea-b341-d3111fcd9587",
  "isSidechain": false,
  "requestId": "req_011CbEimpX2uT822TqHYWPKz",
  "type": "assistant",
  "uuid": "42f4938b-e277-457e-a883-f1887e2e37af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjUc3uesH5Pc1FG4rgHA8i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 36722,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3453,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 36722,
          "cache_creation_input_tokens": 3453,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3453
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

_source line 12 · 2026-05-20T23:53:08.699Z_

<details><summary>↩ Tool result · `toolu_01NmdRoYeHPojXVqBGNn5JU8`</summary>

```text
0	baseline: null
1	experiments:
2	  mvp-001:
3	    status: DONE
4	    retry_count: 0
5	    created_at: '2026-05-14T16:17:16.218Z'
6	    updated_at: '2026-05-14T18:08:20.940Z'
7	    hypothesis: Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B
8	      continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45
9	    spec:
10	      command: python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id
11	        {0-3} --num-shards 4 --device cuda:0 (4 shards parallel)
12	      server: autodl-5090
13	      data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
14	      data_count: 1000
15	      model_name: EleutherAI/pythia-2.8b (FP16)
16	      seed: 42
17	      temperature: 0.7
18	      top_p: 0.9
19	      max_new_tokens: 256
20	      reference_model: EleutherAI/pythia-410m
21	      script_path: /root/gen-depth-fingerprint/generate_chain.py
22	      generation_type: continuation
23	      depths: gen-0 to gen-4
24	      checkpoint_path: /root/gen-depth-fingerprint/results/mvp_results.json
25	      log_path: /root/gen-depth-fingerprint/data/features.csv
26	    conclusion: success
27	    metrics:
28	      macro_f1: 0.8408
29	      binary_f1_gen0_vs_gen2plus: 0.8653
30	      cv_macro_f1: 0.806
31	      cv_std: 0.013
32	      gen0_f1: 0.9517
33	      gen1_f1: 0.7759
34	      gen2plus_f1: 0.7947
35	      total_records: 4609
36	      seeds_used: 995
37	      skipped: 173
38	    completed_at: '2026-05-14T18:08:20.940Z'
39	  mvp-001-gen-s0:
40	    status: PREPARING
41	    retry_count: 0
42	    created_at: '2026-05-14T17:23:13.139Z'
43	    updated_at: '2026-05-15T00:19:34.474Z'
44	    spec:
45	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
46	        base && cd /root/gen-depth-fingerprint && python generate_chain.py --input
47	        data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 4 --device cuda:0"
48	      server: autodl-5090
49	      gpu:
50	      - cuda:0
51	      pid: '92168'
52	      log_path: ~/runs/gen-depth-fingerprint/mvp-001-gen-s0.log
53	      submitted_at: '2026-05-14T17:23:13.138Z'
54	      submitted_via: submit_training_job
55	      backend: tmux
56	      account: root
57	    reproduce:
58	      finished_at: '2026-05-14T18:00:08.256Z'
59	    extra:
60	      hook_events:
61	      - event: on_complete
62	        action: agent
63	        ts: '2026-05-14T18:00:08.934694+00:00'
64	    notes: 历史遗留条目，实际已由 mvp-001 完成覆盖。可忽略。
65	  mvp-001-gen-s1:
66	    status: PREPARING
67	    retry_count: 0
68	    created_at: '2026-05-14T17:23:14.464Z'
69	    updated_at: '2026-05-14T17:25:48.863Z'
70	    spec:
71	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
72	        base && cd /root/gen-depth-fingerprint && python generate_chain.py --input
73	        data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 4 --device cuda:0"
74	      server: autodl-5090
75	      gpu:
76	      - cuda:1
77	      pid: '93039'
78	      log_path: ~/runs/gen-depth-fingerprint/mvp-001-gen-s1.log
79	      submitted_at: '2026-05-14T17:25:16.359Z'
80	      submitted_via: submit_training_job
81	      backend: tmux
82	      account: root
83	    reproduce:
84	      finished_at: '2026-05-14T17:23:44.818Z'
85	    failure_reason: EXIT_CODE=1 (generic error — check log tail)
86	    conclusion: failed
87	    extra:
88	      hook_events:
89	      - event: on_failed
90	        action: agent
91	        ts: '2026-05-14T17:23:45.838438+00:00'
92	    notes: '失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES
93	      后脚本只能看到 cuda:0，但命令用了 --device cuda:1 | 修复: --device 应始终为 cuda:0'
94	  mvp-001-gen-s2:
95	    status: PREPARING
96	    retry_count: 0
97	    created_at: '2026-05-14T17:23:15.855Z'
98	    updated_at: '2026-05-14T17:25:50.275Z'
99	    spec:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42f4938b-e277-457e-a883-f1887e2e37af",
  "isSidechain": false,
  "promptId": "b522a379-46f0-402c-b39d-4f606e12c539",
  "type": "user",
  "uuid": "d051c6ef-b234-4256-b3b6-bd009d68acde",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml",
      "content": "baseline: null\nexperiments:\n  mvp-001:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-14T16:17:16.218Z'\n    updated_at: '2026-05-14T18:08:20.940Z'\n    hypothesis: Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B\n      continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\n    spec:\n      command: python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id\n        {0-3} --num-shards 4 --device cuda:0 (4 shards parallel)\n      server: autodl-5090\n      data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\n      data_count: 1000\n      model_name: EleutherAI/pythia-2.8b (FP16)\n      seed: 42\n      temperature: 0.7\n      top_p: 0.9\n      max_new_tokens: 256\n      reference_model: EleutherAI/pythia-410m\n      script_path: /root/gen-depth-fingerprint/generate_chain.py\n      generation_type: continuation\n      depths: gen-0 to gen-4\n      checkpoint_path: /root/gen-depth-fingerprint/results/mvp_results.json\n      log_path: /root/gen-depth-fingerprint/data/features.csv\n    conclusion: success\n    metrics:\n      macro_f1: 0.8408\n      binary_f1_gen0_vs_gen2plus: 0.8653\n      cv_macro_f1: 0.806\n      cv_std: 0.013\n      gen0_f1: 0.9517\n      gen1_f1: 0.7759\n      gen2plus_f1: 0.7947\n      total_records: 4609\n      seeds_used: 995\n      skipped: 173\n    completed_at: '2026-05-14T18:08:20.940Z'\n  mvp-001-gen-s0:\n    status: PREPARING\n    retry_count: 0\n    created_at: '2026-05-14T17:23:13.139Z'\n    updated_at: '2026-05-15T00:19:34.474Z'\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/gen-depth-fingerprint && python generate_chain.py --input\n        data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 4 --device cuda:0\"\n      server: autodl-5090\n      gpu:\n      - cuda:0\n      pid: '92168'\n      log_path: ~/runs/gen-depth-fingerprint/mvp-001-gen-s0.log\n      submitted_at: '2026-05-14T17:23:13.138Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n    reproduce:\n      finished_at: '2026-05-14T18:00:08.256Z'\n    extra:\n      hook_events:\n      - event: on_complete\n        action: agent\n        ts: '2026-05-14T18:00:08.934694+00:00'\n    notes: 历史遗留条目，实际已由 mvp-001 完成覆盖。可忽略。\n  mvp-001-gen-s1:\n    status: PREPARING\n    retry_count: 0\n    created_at: '2026-05-14T17:23:14.464Z'\n    updated_at: '2026-05-14T17:25:48.863Z'\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/gen-depth-fingerprint && python generate_chain.py --input\n        data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 4 --device cuda:0\"\n      server: autodl-5090\n      gpu:\n      - cuda:1\n      pid: '93039'\n      log_path: ~/runs/gen-depth-fingerprint/mvp-001-gen-s1.log\n      submitted_at: '2026-05-14T17:25:16.359Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n    reproduce:\n      finished_at: '2026-05-14T17:23:44.818Z'\n    failure_reason: EXIT_CODE=1 (generic error — check log tail)\n    conclusion: failed\n    extra:\n      hook_events:\n      - event: on_failed\n        action: agent\n        ts: '2026-05-14T17:23:45.838438+00:00'\n    notes: '失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES\n      后脚本只能看到 cuda:0，但命令用了 --device cuda:1 | 修复: --device 应始终为 cuda:0'\n  mvp-001-gen-s2:\n    status: PREPARING\n    retry_count: 0\n    created_at: '2026-05-14T17:23:15.855Z'\n    updated_at: '2026-05-14T17:25:50.275Z'\n    spec:",
      "numLines": 100,
      "startLine": 0,
      "totalLines": 2673
    }
  },
  "sourceToolAssistantUUID": "42f4938b-e277-457e-a883-f1887e2e37af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-20T23:53:08.724Z_

````json
{
  "parentUuid": "d051c6ef-b234-4256-b3b6-bd009d68acde",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**gen-depth-fingerprint**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"gen-depth-fingerprint\")` 或 `load_project_config(\"gen-depth-fingerprint\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[项目]** overall framework参考已发表EMNLP论文的风格，图中的信息密度要高，视觉美观，高度浓缩method部分信息\n- **[项目]** 参考已发表同类文章（如本文是empirical）的写作风格，如用词，写作逻辑，架构，语气，改善本篇的写作，要将整个story讲的高级一些，体现技术深度同时有创新性\n- **[项目]** 附录中的可视化图要嵌入在文字中，出现在论文中需要用到图的附近位置，同时注意latex排版，避免大量空白的存在\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n- **AI Text Detection & Generation Depth — Research Patterns** — Distilled experimental conventions, baselines, metrics, and gaps from 25 papers on AI text detection, model collapse, and content diversity (2019-2026).  →  `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/skills/projects/gen-depth-fingerprint/distilled-research.skill.md`\n- **AI Text Detection & Generation Depth — Writing Patterns** — Distilled narrative strategies, figure/table conventions from 8 deep-read papers on AI text detection and model collapse (ICLR/ICML/ACL 2024-2025).  →  `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/skills/projects/gen-depth-fingerprint/distilled-writing.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/gen-depth-fingerprint/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "9d3d456e-3fab-4265-a332-afe1d7abc204",
  "timestamp": "2026-05-20T23:53:08.724Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。 核心假设：[\"DDR 二分法在 ≥9 generators 下瓦解：≥3 个 'stationary' 特征出现显著 drift (|ρ|>0.15)，或 drifti…",
  "leafUuid": "9d3d456e-3fab-4265-a332-afe1d7abc204",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Worst-case scenario analysis for generation depth fingerprinting",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b"
}
```

---

### Assistant

_source line 16 · 2026-05-20T23:53:48.027Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the project. Let me synthesize the worst-tier predictions for each planned experiment. The key constraints of the worst tier are:

1. DDR framework doesn't hold as a universal phenomenon
2. 7-feature set has no statistically significant advantage over single-feature baseline
3. Need to restructure paper angle but don't downgrade venue

Key metric ranges for worst tier:
- logo_binary_f1_8gen: [0.62, 0.66]
- logo_binary_f1_9gen: [0.58, 0.63]


- lofo_binary_f1: [0.56, 0.63]
- cross_model_binary_f1: [0.58, 0.7]
- ddr_drifting_rho_abs_min: [0.3, 0.4]
- ddr_stationary_rho_abs_max: [0.15, 0.3]
- seven_feat_minus_best_single_pp: [0.0, 1.5]
- scale_8b_logo_binary_f1: [0.48, 0.58]
- llm_rephrase_drop

_pp: [6.0, 12.0]

Now I'm going through each planned experiment to generate worst-case predictions. I have eight experiments mapped out: feature ablation and trend analysis, cross-generator evaluation, cross-family reference models, downstream utility testing, prompt type comparisons, paraphrastic comparisons, cross-model chains, and multi-domain seeds, with the first four marked as P0 priority and the rest as P1.

For the worst-case scenario, I'm thinking about how to reframe DDR away from being the core contribution and instead position it as part of a broader "Generation" narrative.

Looking at what each experiment would reveal in the worst case: the feature ablation would show minimal gains from reference information and weak trend signals, with the DDR split becoming unclear. Cross-generator evaluation would show modest binary classification performance with high variance across generators. The cross-family reference model would suggest that entropy drift patterns depend heavily on which reference model is used, partially undermining the DDR framework.

When I move to downstream utility, the negative finding becomes even starker — depth-aware curation actively degrades performance, though this aligns with the paper's positioning. Prompt type comparison reveals a massive disparity, with elaboration chains providing almost no discriminative signal and all the depth information concentrated in continuations. Paraphrastic chains would show comparable or better depth signal than non-paraphrastic ones, which contradicts the core claim. Finally, cross-model chains would yield classification performance around 0.70 or lower with no clear advantage over single-model approaches.

The heterogeneity hypothesis doesn't hold up either. Multi-domain evaluation shows strong domain dependence with some domains like academic falling below 0.55, undermining claims about generalizable depth signal. Moving to finer-grained ordinal classification, the 5-class F1 drops to around 0.35-0.40, suggesting ordinal methods don't help and the resolution ceiling is lower than anticipated. Human edit robustness is particularly concerning — even small perturbations like 5% edits cause drops exceeding 10 percentage points, and LLM rephrasings cause 6-12 percentage point drops, indicating the signal is quite fragile. The LD-Score feature provides no complementary signal on its own.

The end-to-end classifier experiment reveals that a QLoRA-based approach significantly outperforms the 7-feature baseline, suggesting handcrafted features are suboptimal, though it's also possible the task is fundamentally difficult. Text length appears to be a significant confound — when controlling for length, F1 drops substantially, implying surface features partially track length rather than capturing true depth. Scaling to larger generators (8B+) yields binary F1 below 0.60, showing that scale actually degrades the signal by compressing feature margins. Finally, the ordinal baseline comparison is telling: average log probability as a single feature nearly matches the 7-feature approach with less than 1.5 percentage points gap and no significant bootstrap difference, meaning custom features add minimal value.

Now I'm organizing these findings into a detailed YAML structure with comprehensive rationales...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d3d456e-3fab-4265-a332-afe1d7abc204",
  "isSidechain": false,
  "requestId": "req_011CbEin2oU7zF5an8ohJsga",
  "type": "assistant",
  "uuid": "dd7dd875-9bee-4cb0-8829-bd6a71ff5cf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157AH3tp4wL9JgiTVvfj7pg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7626,
      "cache_read_input_tokens": 40175,
      "output_tokens": 17261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7626,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17261,
          "cache_read_input_tokens": 40175,
          "cache_creation_input_tokens": 7626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7626
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

_source line 17 · 2026-05-20T23:58:30.006Z_

Now I have full context on all experiments, their actual results, and the worst-tier definition. Let me generate the detailed predictions.

```yaml
tier: worst
narrative_guidance: >
  DDR 框架不成立为通用现象。重构为 'Generation Depth Estimation: Task Formulation, Baselines, and Empirical Boundaries.'
  三项贡献重定位：(1) Task formulation — depth estimation 作为超越 binary detection 的新任务，含 leak-free LOGO protocol；
  (2) Empirical boundary map — 系统测定 depth signal 存在的条件空间与消失的条件空间；
  (3) Negative downstream finding 不变。
  承认 avg_logprob 是 competitive baseline，7-feature 价值在 interpretability 而非 accuracy。
  从 method paper 转为 benchmark + analysis paper。仍足以支撑 EMNLP Findings。

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      MVP 数据上的三部分分析：(A) reference-only vs surface-only vs full 特征消融；
      (B) 各特征随 depth 的趋势分析（slope + R²）；(C) perplexity 预验证。
    expected_results:
      full_macro_f1: 0.790
      reference_only_f1: 0.745
      surface_only_f1: 0.760
      full_minus_surface_pp: 3.0
      full_minus_reference_pp: 4.5
      mcnemar_full_vs_surface_p: 0.08
      entropy_mean_slope: -0.18
      entropy_mean_R2: 0.42
      ttr_slope: -0.12
      ttr_R2: 0.38
      hapax_ratio_slope: -0.14
      hapax_ratio_R2: 0.40
      tail_decay_slope: -0.06
      tail_decay_R2: 0.08
      entropy_max_slope: 0.04
      entropy_max_R2: 0.03
      entropy_std_slope: -0.09
      entropy_std_R2: 0.15
      entropy_min_slope: -0.08
      entropy_min_R2: 0.11
      median_ppl_depth_0: 13.2
      median_ppl_depth_4: 2.1
      ppl_depth_correlation_rho: -0.85
    result_rationale: >
      在 worst 档下，surface-only（TTR + hapax_ratio）表现逼近 full feature set，McNemar p=0.08 不显著。
      这意味着 reference-model features 的独立贡献可疑——vocabulary impoverishment 几乎能解释全部 depth signal。
      H2 趋势分析中 entropy_mean 虽然有 monotonic drift（slope=-0.18），但 R² 仅 0.42，说明深度只解释不到一半方差。
      关键问题：entropy_std 不再"stationary"（slope=-0.09, R²=0.15），DDR 的 drifting/stationary 二分法开始模糊。
      tail_decay 勉强 stationary（R²=0.08），但 entropy_min 也有可辨识的 drift（R²=0.11），使得 "shape features remain near-stationary" 的叙述出现裂缝。
      Perplexity 预验证仍有强信号（ρ=-0.85），但这本质上意味着 avg_logprob 单特征就能捕捉大部分 depth 信息。
    tables:
      - name: "Table 1: Feature Ablation (5-fold CV, Pythia-2.8B only)"
        columns: [Feature Set, Macro F1, 95% CI, McNemar vs Full]
        rows:
          - [Full (7 features), 0.790, "[0.775, 0.805]", "—"]
          - [Surface-only (TTR + hapax), 0.760, "[0.744, 0.776]", "p=0.08"]
          - [Reference-only (5 entropy + tail_decay), 0.745, "[0.728, 0.762]", "p=0.03"]
      - name: "Table 2: Feature Trend Analysis (Linear Regression on Depth)"
        columns: [Feature, Slope, R², Spearman ρ, Category]
        rows:
          - [entropy_mean, -0.18, 0.42, -0.55, drifting]
          - [TTR, -0.12, 0.38, -0.52, drifting]
          - [hapax_ratio, -0.14, 0.40, -0.54, drifting]
          - [entropy_std, -0.09, 0.15, -0.32, "ambiguous"]
          - [entropy_min, -0.08, 0.11, -0.28, "ambiguous"]
          - [entropy_max, 0.04, 0.03, 0.09, stationary]
          - [tail_decay, -0.06, 0.08, -0.07, stationary]
    figures_description:
      - "Fig 1: 7 panel line plots (mean ± std by depth 0–4). Drifting features show gradual decline but wide CI overlap between adjacent depths. entropy_std shows intermediate drift that defies clean binary categorization."
      - "Fig 2: Ppl by depth — clear monotonic decline but with diminishing marginal separation at depth 3–4."
    analysis: >
      核心问题：McNemar p=0.08 对 full vs surface-only 不显著。在 worst 档下，这意味着 7 个 reference features 的增量价值在统计上不可证。
      DDR 框架进一步受到质疑：entropy_std 的 drift（R²=0.15）不可忽略，属于 "既不 drifting 也不 stationary" 的灰色地带。
      论文需重定位：不能声称发现了 "differential depth response"，而应描述为 "depth-correlated distributional shifts of varying magnitude"。
      Perplexity 强信号暗示 avg_logprob 可能是最强 single baseline——plan_015 的对照将证实这一点。

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      扩展到 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-0.6B, Qwen3-1.7B)，
      LOGO 和 LOFO 评估 cross-generator generalization。
    expected_results:
      total_records: 23000
      logo_binary_f1_avg: 0.635
      logo_binary_f1_ci: [0.620, 0.650]
      logo_3class_f1_avg: 0.710
      lofo_binary_f1: 0.590
      per_gen_binary_f1:
        pythia_2_8b: 0.695
        pythia_1b: 0.680
        olmo_2_1b: 0.610
        qwen3_0_6b: 0.575
        qwen3_1_7b: 0.620
      per_gen_binary_f1_range_pp: 12.0
      per_gen_binary_f1_min: 0.575
      family_out_pythia_binary_f1: 0.570
      family_out_qwen_binary_f1: 0.615
      family_out_olmo_binary_f1: 0.650
    result_rationale: >
      worst 档核心假设之一：per-gen binary F1 方差 >15pp，部分 generator < 0.55。
      5-gen LOGO binary F1 落在 [0.62, 0.66] 范围。Qwen3-0.6B 最弱（0.575），因为最小模型的 generation 质量不稳定，
      特征分布方差大，depth signal 被噪声淹没。OLMo-2-1B（0.610）也偏弱——非 Pythia 家族的 reference model
      (Pythia-410M) 提取的特征对 OLMo 生成文本的适配性差。
      LOFO 进一步恶化到 0.590：留出整个家族时（如留出两个 Pythia），训练集多样性骤降，
      Qwen 和 OLMo 的特征分布差异未被充分学习。
      Pythia 家族 holdout inflation 确实存在——Pythia-1B 被 Pythia-2.8B 的训练数据"帮助"，
      但 family-out 把两者同时移除后 F1 只有 0.570。
      per-gen 范围 12pp 虽未达到 15pp 的极端预设，但 Qwen3-0.6B 的 0.575 已接近 0.55 阈值。
      'generalizable depth signal' claim 受到严重质疑——跨家族泛化很弱。
    tables:
      - name: "Table 3: Leave-One-Generator-Out Binary F1"
        columns: [Held-out Generator, Family, Params, Binary F1, 95% CI]
        rows:
          - [Pythia-2.8B, Pythia, 2.8B, 0.695, "[0.672, 0.718]"]
          - [Pythia-1B, Pythia, 1B, 0.680, "[0.656, 0.704]"]
          - [OLMo-2-1B, OLMo, 1.5B, 0.610, "[0.584, 0.636]"]
          - [Qwen3-0.6B, Qwen, 0.6B, 0.575, "[0.547, 0.603]"]
          - [Qwen3-1.7B, Qwen, 1.7B, 0.620, "[0.595, 0.645]"]
          - [Average, "—", "—", 0.636, "[0.620, 0.650]"]
      - name: "Table 4: Leave-One-Family-Out Binary F1"
        columns: [Held-out Family, Generators Removed, Binary F1]
        rows:
          - [Pythia, "Pythia-1B + Pythia-2.8B", 0.570]
          - [Qwen, "Qwen3-0.6B + Qwen3-1.7B", 0.615]
          - [OLMo, OLMo-2-1B, 0.650]
    figures_description:
      - "Fig 3: Bar chart of per-generator LOGO binary F1 with error bars. Wide spread (0.575–0.695) visualizes generalization instability. Horizontal dashed line at 0.60 marks practical utility threshold."
    analysis: >
      LOGO binary F1 = 0.635 远低于论文 paper_framing 中声称的 0.694。
      Qwen3-0.6B 和 OLMo-2-1B 拖拽均值，且 LOFO 进一步暴露了 Pythia family inflation。
      在 worst 档叙事下，这个结果表明 depth signal 的跨生成器泛化高度依赖于 reference model 与 generator 的"亲缘关系"。
      论文需要诚实报告：depth signal 在 same-family 和 small-model 条件下存在，
      但跨家族迁移不稳定。这自然过渡到 "empirical boundary map" 贡献。

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      测试非 Pythia reference models (OLMo-2-1B, Qwen3-0.6B) 提取特征。
      验证 DDR 是否为 generation-intrinsic 而非 reference-model artifact。
    expected_results:
      logo_f1_pythia_ref: 0.635
      logo_f1_olmo_ref: 0.610
      logo_f1_qwen_ref: 0.620
      entropy_drift_pythia_ref_rho_range: [-0.55, -0.35]
      entropy_drift_olmo_ref_rho_range: [-0.40, -0.25]
      entropy_drift_qwen_ref_rho_range: [-0.48, -0.30]
      stationary_rho_max_across_refs: 0.22
      tail_decay_rho_olmo_ref: -0.18
      entropy_std_rho_qwen_ref: -0.20
    result_rationale: >
      worst 档核心假设：≥3 个 'stationary' 特征在某些 reference model 下出现显著 drift (|ρ|>0.15)。
      Pythia-410M 作为 reference 时 tail_decay 勉强 stationary (|ρ|<0.10)，但换成 OLMo-2-1B reference 后
      tail_decay 的 ρ 跳到 -0.18——超过 0.15 阈值，不再 stationary。
      类似地，Qwen3-0.6B 作为 reference 时 entropy_std 的 ρ 达到 -0.20。
      这意味着 DDR 的 drifting/stationary 划分是 reference-model-dependent，而非 generation-intrinsic property。
      不同 reference model "看到"的分布变化模式不同，DDR 二分法只在特定 (generator, reference) pair 下成立。
      分类性能也随 reference model 变化——OLMo ref 略差于 Pythia ref (0.610 vs 0.635)，
      暗示 Pythia-410M 对深度文本的 NLL 分布恰好更 sensitive。
      总之：DDR 框架在通用意义上瓦解。entropy_mean 的负 drift 方向是一致的（所有 ref 下都是负 ρ），
      但 magnitude 和 stationary 集合的稳定性不可复现。
    tables:
      - name: "Table 5: LOGO F1 by Reference Model"
        columns: [Reference Model, Params, LOGO Binary F1, Δ vs Pythia-410M]
        rows:
          - [Pythia-410M, 410M, 0.635, "—"]
          - [OLMo-2-1B, 1.5B, 0.610, -0.025]
          - [Qwen3-0.6B, 600M, 0.620, -0.015]
      - name: "Table 6: Spearman ρ of Features by Reference Model"
        columns: [Feature, Pythia-410M ref, OLMo-2-1B ref, Qwen-0.6B ref, Consistent Category?]
        rows:
          - [entropy_mean, -0.45, -0.32, -0.38, "drifting (all ρ<-0.30)"]
          - [TTR, -0.42, -0.40, -0.41, "drifting (consistent)"]
          - [hapax_ratio, -0.44, -0.38, -0.40, "drifting (consistent)"]
          - [entropy_std, -0.15, -0.12, -0.20, "AMBIGUOUS (crosses 0.15 threshold)"]
          - [entropy_min, -0.18, -0.10, -0.14, "AMBIGUOUS"]
          - [entropy_max, 0.05, 0.08, -0.05, "stationary (marginal)"]
          - [tail_decay, -0.06, -0.18, -0.10, "FAILS: OLMo ref |ρ|=0.18 >0.15"]
    figures_description:
      - "Fig 4: Heatmap of |Spearman ρ| for 7 features × 3 reference models. Highlights cells where |ρ| crosses 0.15 threshold, showing DDR category instability."
    analysis: >
      DDR 二分法的关键检验失败：tail_decay 在 OLMo reference 下不再 stationary，entropy_std 在 Qwen reference 下不再 stationary。
      "Shape features remain near-stationary" 这个核心声称只在 Pythia-410M reference 下成立。
      这是 worst 档的决定性结果——DDR 不是 generation-intrinsic 的通用现象，而是 (generator, reference) pair 的函数。
      论文必须放弃 DDR 作为核心贡献，改为报告 "reference-dependent feature behavior patterns"。
      surface features (TTR, hapax_ratio) 的 drift 方向和 magnitude 跨 reference 最稳定——
      这进一步强化了 "vocabulary impoverishment 是主要 signal" 的叙事。

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune OLMo-1B on depth-stratified subsets, 3 seeds, bootstrap CIs.
      Compare depth-aware filtering vs random subsampling.
    expected_results:
      all_ppl_mean: 2.340
      all_ppl_std: 0.003
      size_matched_ppl_mean: 2.375
      depth01_ppl_mean: 2.400
      binary_filtered_ppl_mean: 2.410
      depth0_only_ppl_mean: 2.700
      tost_p_size_matched_vs_depth01: 0.42
      tost_p_at_2pct_margin: 0.15
      tost_p_at_3pct_margin: 0.03
      cohens_d_depth01_vs_size_matched: 0.85
      ranking: "all < size_matched < depth01 ≈ binary_filtered << depth0_only"
    result_rationale: >
      Negative finding 方向与原计划一致，但 worst 档下更加棘手：
      TOST 在 ±2% margin 下 p=0.15，不显著——无法声称 depth-aware filtering 与 random subsampling "等效"。
      需要放宽到 ±3% margin 才能拒绝（p=0.03）。这意味着 depth-aware filtering 与 random 之间可能存在
      up to 3% 的差异，且方向是 depth-aware 更差（2.400 vs 2.375）。
      Cohen's d=0.85 看似很大，但 seed 间方差极小（std<0.003），导致 d 被 inflate。
      实际 ppl 差仅 0.025（约 1%），但统计检验因低方差而敏感。
      depth0_only 显著更差（2.700），确认纯 seed 数据不够多样。
      论文可报告：depth-aware curation 在 ±3% margin 内等效于 random subsampling，
      但不能用更严格的 ±2% margin。这弱化了 negative finding 的 crispness，
      但仍足以支持 "depth fingerprinting is diagnostic, not curative" 的结论。
    tables:
      - name: "Table 7: Downstream CLM Perplexity by Training Data Selection"
        columns: [Variant, n_train, PPL (mean±std), TOST p (±2%), TOST p (±3%)]
        rows:
          - [All data, 12299, "2.340±0.003", "—", "—"]
          - [Size-matched random, 3951, "2.375±0.004", "—", "—"]
          - [Depth 0+1, 3951, "2.400±0.003", 0.15, 0.03]
          - [Binary-filtered, 3951, "2.410±0.004", 0.09, 0.02]
          - [Depth 0 only, 797, "2.700±0.008", "<0.001", "<0.001"]
    figures_description:
      - "Fig 5: Box plot of perplexity across 3 seeds × 5 variants. Overlapping boxes for size_matched/depth01/binary_filtered visually communicate near-equivalence. depth0_only clearly separated."
    analysis: >
      Negative finding 保留但 crispness 降低。TOST 需要 ±3% margin 而非 ±2%。
      在 worst 档叙事中，这仍然是独立贡献——reviewer 关心的是 "does depth-aware filtering help?"，
      答案仍然是 no（或 negligible），只是统计置信度略弱。
      论文写法调整：报告 ±3% equivalence，并在 limitation 中承认 ±2% 未达显著。

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Continuation vs elaboration vs inspired_rewriting chains on Pythia-2.8B.
      1000 seeds × 3 prompt types.
    expected_results:
      cv_f1_continuation: 0.720
      cv_f1_elaboration: 0.620
      cv_f1_rewriting: 0.650
      lopto_avg: 0.630
      lopto_held_out_continuation: 0.650
      lopto_held_out_elaboration: 0.580
      lopto_held_out_rewriting: 0.610
      depth_retention_d4_d0_continuation: 0.82
      depth_retention_d4_d0_elaboration: 0.99
      depth_retention_d4_d0_rewriting: 0.94
      drift_hapax_continuation: -0.50
      drift_hapax_elaboration: -0.35
      drift_hapax_rewriting: -0.42
      drift_entropy_mean_continuation: -0.40
      drift_entropy_mean_elaboration: -0.22
      drift_entropy_mean_rewriting: -0.30
    result_rationale: >
      worst 档下，prompt type 差异极大。Continuation chains 勉强可辨（CV F1=0.720），
      但 elaboration 几乎 undiscriminable（0.620）——因为 elaboration 指令要求保持原文语义，
      model 输出的 lexical diversity 不随 depth 显著衰减。drift 指标显示 elaboration 的 hapax_ratio ρ 仅 -0.35，
      entropy_mean 仅 -0.22，都在 worst 定义的 |ρ|>0.30 临界区域。
      depth retention 接近 1.0（0.99）意味着 elaboration 几乎不 drop out，
      但 depth signal 也因此极弱——文本保持高质量但失去了可用于区分 depth 的分布特征。
      Leave-one-prompt-type-out (LOPTO) 更暴露问题：held-out elaboration 仅 0.580，
      说明在 continuation + rewriting 上训练的模型完全无法迁移到 elaboration。
      温度 scope 收窄的问题在此叠加：如果只有 continuation at t=0.7 有用，
      reviewer 会质疑 "base models + t=0.7 + continuation only" 的适用范围。
    tables:
      - name: "Table 8: Prompt Type Comparison (Pythia-2.8B, Within-type CV)"
        columns: [Prompt Type, CV Binary F1, Depth Retention (d4/d0), hapax ρ, entropy_mean ρ]
        rows:
          - [Continuation, 0.720, 0.82, -0.50, -0.40]
          - [Inspired Rewriting, 0.650, 0.94, -0.42, -0.30]
          - [Elaboration, 0.620, 0.99, -0.35, -0.22]
      - name: "Table 9: Leave-One-Prompt-Type-Out Transfer"
        columns: [Held-out Type, Binary F1, Δ vs Within-CV]
        rows:
          - [Continuation, 0.650, -0.070]
          - [Elaboration, 0.580, -0.040]
          - [Rewriting, 0.610, -0.040]
    figures_description:
      - "Fig 6: Feature drift curves (mean by depth) for 3 prompt types, side-by-side. Elaboration curves nearly flat, visually demonstrating signal absence."
    analysis: >
      Prompt-type dependence 极为严重。Elaboration 基本不可分（binary F1=0.620 接近 random）。
      这强化了 worst 档叙事的一个关键点：depth signal 高度依赖 generation 的 "divergence mode"——
      只有在 model 被允许 freely continue（而非 constrain to semantics）时才产生可辨的分布漂移。
      empirical boundary map 贡献中，这是一个明确的 "signal disappears" 条件。

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      Parallel paraphrasing chains vs continuation chains.
      Tests attractor convergence theory.
    expected_results:
      paraphrastic_cv_f1: 0.680
      continuation_cv_f1: 0.720
      paraphrastic_binary_f1_logo: 0.610
      continuation_binary_f1_logo: 0.650
      attractor_convergence_depth: 3
      paraphrastic_depth_3_4_f1: 0.52
      continuation_depth_3_4_f1: 0.58
      paraphrastic_ttr_rho: -0.38
      paraphrastic_entropy_mean_rho: -0.30
    result_rationale: >
      Paraphrastic chains 在 worst 档下仍有 moderate signal（CV F1=0.680），弱于 continuation（0.720）但差距不大。
      Attractor convergence theory 部分成立：paraphrastic chains 在 depth 3-4 出现饱和（F1=0.52 接近 random），
      与 ACL 2025 "LLM as Broken Telephone" 的 ~3 class ceiling 一致。
      但 continuation chains 也在 depth 3-4 衰减（0.58），说明两种 chain 类型共享 resolution bottleneck。
      关键问题：paraphrastic 和 continuation 的差距（4pp within-CV, 4pp LOGO）不足以支撑
      "non-paraphrastic chains preserve more depth signal" 的 claim——bootstrap 可能不显著。
      在 worst 档下，这削弱了 "non-paraphrastic chains 是更有趣的研究对象" 的动机。
    tables:
      - name: "Table 10: Paraphrastic vs Continuation Chains"
        columns: [Chain Type, CV Binary F1, LOGO Binary F1, TTR ρ, entropy_mean ρ, Depth 3-4 F1]
        rows:
          - [Continuation, 0.720, 0.650, -0.52, -0.40, 0.58]
          - [Paraphrastic, 0.680, 0.610, -0.38, -0.30, 0.52]
          - [Δ, 0.040, 0.040, 0.14, 0.10, 0.06]
    figures_description:
      - "Fig 7: F1 by depth pair (1v2, 2v3, 3v4) for both chain types. Both decay similarly, paraphrastic slightly faster. Convergence zone at depth 3-4 highlighted."
    analysis: >
      Continuation 略优但差距不具 practical significance。
      这个结果不 catastrophic——paraphrastic comparison 本身是 P1 优先级，
      其价值在于确认 depth signal 的 resolution ceiling 是跨 chain-type 的。
      论文可在 appendix 报告，作为 "boundary map" 的一部分。

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains (不同 generator per depth step) vs single-model chains.
      Tests heterogeneity hypothesis.
    expected_results:
      cross_model_binary_f1: 0.620
      cross_model_binary_ci: [0.580, 0.660]
      single_model_binary_f1: 0.650
      cross_model_3class_f1: 0.580
      delta_cross_vs_single: -0.030
      cross_model_per_combo_f1_range: [0.52, 0.70]
      cross_model_per_combo_f1_std: 0.06
    result_rationale: >
      worst 档核心假设：Cross-model chains 无优势或更差 (binary F1 ≤ 0.70)，heterogeneity 假设被否。
      实际更糟：cross-model F1=0.620，比 single-model 的 0.650 还低 3pp。
      原因：当不同 generator 参与不同 depth step 时，每步引入的分布变化方向不一致。
      例如 Pythia-2.8B gen-1 → Qwen3-1.7B gen-2 的特征变化模式与 Pythia-2.8B gen-1 → gen-2 不同。
      Classifier 学到的 "depth = monotonic drift" 模式被打破——cross-model chains 的特征轨迹是 non-monotonic。
      per-combo 方差极大（0.52–0.70），部分组合（如 OLMo → Qwen → Pythia）甚至低于 random baseline。
      heterogeneity 假设（"diverse generators amplify distributional shifts"）被彻底否定。
      在 worst 档叙事下，这意味着 cross-model chains 是 "signal disappears" 的又一条件，
      加入 empirical boundary map。
    tables:
      - name: "Table 11: Cross-Model vs Single-Model Chains"
        columns: [Chain Type, Binary F1, 95% CI, 3-class F1]
        rows:
          - [Single-model (5-gen LOGO), 0.650, "[0.630, 0.670]", 0.710]
          - [Cross-model (heterogeneous), 0.620, "[0.580, 0.660]", 0.580]
          - [Δ, -0.030, "—", -0.130]
    figures_description:
      - "Fig 8: Heatmap of cross-model combo F1 values (generator A at step i → generator B at step i+1). Diagonal = same-model, off-diagonal = cross-model. Clear diagonal dominance."
    analysis: >
      Heterogeneity hypothesis 被否。Cross-model chains 不仅无优势，反而更差。
      这与 paper_framing 中 "cross-model chains yield higher F1 (0.764)" 的声称完全矛盾。
      在 worst 档下，paper_framing 的 0.764 是 cherry-picked 5-gen subset 的结果，
      而 full evaluation 显示 cross-model 更难。论文重构后必须删除 cross-model advantage claim。

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      4 domains (Wikipedia, news, scientific, creative), 500 seeds × 5 depths each.
    expected_results:
      wikipedia_binary_f1: 0.650
      news_binary_f1: 0.610
      academic_binary_f1: 0.570
      creative_binary_f1: 0.590
      cross_domain_logo_binary_f1: 0.580
      max_gap_vs_best_pp: 8.0
      worst_domain: academic
      spearman_entropy_mean_academic: -0.25
      spearman_hapax_academic: -0.35
    result_rationale: >
      worst 档下，domain 依赖性严重。Wikipedia（训练数据中最常见的 domain）表现最好（0.650），
      academic 最差（0.570）——因为学术文本的 lexical diversity 天然较低（专业术语复用率高），
      depth-induced diversity loss 被 domain-inherent low diversity 掩盖。
      Creative writing 也偏弱（0.590），因为创意文本 variance 大，depth signal 被 style variance 淹没。
      Cross-domain LOGO（在 3 domains 训练，held-out 1 domain 测试）仅 0.580，
      说明 domain shift 比 generator shift 的影响更大。
      per-gen binary F1 方差 >15pp 的假设虽然在 plan_002 中未完全达到（12pp），
      但加上 domain 维度后总方差轻松超过 15pp（8pp domain gap + 12pp generator gap）。
      'generalizable depth signal' claim 进一步被削弱。
    tables:
      - name: "Table 12: Multi-Domain Depth Classification"
        columns: [Domain, Binary F1, 95% CI, entropy_mean ρ, hapax ρ]
        rows:
          - [Wikipedia, 0.650, "[0.628, 0.672]", -0.42, -0.48]
          - [News, 0.610, "[0.586, 0.634]", -0.35, -0.42]
          - [Creative, 0.590, "[0.564, 0.616]", -0.30, -0.38]
          - [Academic, 0.570, "[0.543, 0.597]", -0.25, -0.35]
          - [Cross-domain LOGO, 0.580, "[0.558, 0.602]", "—", "—"]
    figures_description:
      - "Fig 9: Grouped bar chart of binary F1 by domain. Error bars show 95% CI. Horizontal reference line at 0.60. Academic and creative below threshold."
    analysis: >
      Domain 依赖性是 "signal disappears" boundary map 的重要维度。
      Academic text 的低 F1 暗示 depth fingerprinting 对 scientific paper contamination detection
      （一个核心 motivation）效果最差——ironic but honest。

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4).
      Test CORAL and Frank-Hall ordinal methods.
    expected_results:
      five_class_f1_xgboost: 0.380
      five_class_f1_coral: 0.385
      five_class_f1_frank_hall: 0.375
      three_class_f1_reference: 0.710
      gen1_vs_gen2_f1: 0.48
      gen2_vs_gen3_f1: 0.42
      gen3_vs_gen4_f1: 0.38
      ordinal_correlation_kendall_tau: 0.35
    result_rationale: >
      worst 档下 5-class F1 掉到 ~0.38（vs 3-class 0.71），严重低于 paper_framing 的 ~0.50 estimate。
      CORAL 和 Frank-Hall 几乎无改善（<1pp），因为问题不在于 ordinal structure exploitation，
      而在于 adjacent-depth 的特征分布重叠太大。
      Gen-2 vs Gen-3 的 F1 仅 0.42，Gen-3 vs Gen-4 的 0.38 接近 random。
      这证实了 drifting features 在 depth>2 后的 marginal drift 极小——
      worst 档的 |ρ| 范围 [0.3, 0.4] 意味着 R² 仅 0.09-0.16，深 depth 间差异被噪声淹没。
      3 classes 是 hard ceiling，5 classes 完全不可行。
    tables:
      - name: "Table 13: Ordinal Classification Comparison"
        columns: [Method, 5-class F1, 3-class F1, Kendall τ]
        rows:
          - [XGBoost (flat), 0.380, 0.710, 0.35]
          - [CORAL, 0.385, 0.712, 0.36]
          - [Frank-Hall, 0.375, 0.708, 0.34]
    figures_description:
      - "Fig 10: Confusion matrix for 5-class XGBoost. Strong diagonal for gen-0, diffuse for gen-2/3/4 with heavy off-diagonal mass."
    analysis: >
      5-class 彻底不可行。Ordinal methods 无用。3 classes 是 ceiling，论文应 explicitly state this。
      在 benchmark + analysis 重构下，这是 "empirical boundaries" 的关键数据点。

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Robustness to simulated human edits: (A) random word replacement (5%, 10%, 20%);
      (B) LLM-simulated editing.
    expected_results:
      baseline_binary_f1: 0.635
      5pct_replacement_f1: 0.580
      10pct_replacement_f1: 0.530
      20pct_replacement_f1: 0.490
      5pct_drop_pp: -5.5
      10pct_drop_pp: -10.5
      20pct_drop_pp: -14.5
      llm_rephrase_f1: 0.545
      llm_rephrase_drop_pp: -9.0
      edit_distance_ratio: 0.50
    result_rationale: >
      worst 档指标范围 llm_rephrase_drop_pp: [6.0, 12.0]。预测 -9.0pp，落在范围中间。
      5% word replacement 就造成 -5.5pp 下降——因为 worst 档下 baseline 本身就弱（0.635），
      depth signal 的 margin 已经很小，少量扰动就能抹掉。
      LLM rephrase（edit distance ~50%）导致 -9.0pp 下降至 0.545——接近 random baseline。
      这意味着即使是 moderate human editing 也能有效破坏 depth fingerprint。
      在 worst 档的 "narrow applicability" 叙事中，这进一步收窄了适用场景：
      只有 unedited, single-model, continuation chains at t≤0.7 from small base models 才有信号。
    tables:
      - name: "Table 14: Human Edit Robustness"
        columns: [Condition, Binary F1, Δ vs Baseline]
        rows:
          - [No edit (baseline), 0.635, "—"]
          - [5% random replacement, 0.580, -0.055]
          - [10% random replacement, 0.530, -0.105]
          - [20% random replacement, 0.490, -0.145]
          - [LLM rephrase (~50% edit dist), 0.545, -0.090]
    figures_description:
      - "Fig 11: Line plot of F1 vs edit intensity (0%, 5%, 10%, 20%, LLM rephrase). Near-linear decay. LLM rephrase equivalent to ~12% random replacement."
    analysis: >
      Depth signal 极其脆弱。LLM rephrase 的 -9pp 下降意味着任何 post-generation editing 都会
      实质性地破坏 fingerprint。在 "practical impact" 叙事中这是致命的——
      real-world contaminated text 几乎总是经过某种 editing。
      但在 worst 档重构叙事下，这是 "empirical boundary" 的一部分：
      "depth signal exists only in unedited text" 是一个 honest, useful finding。

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      Add LD-Score (character-distribution signature) as additional feature.
    expected_results:
      ld_score_alone_f1: 0.605
      ld_score_spearman_depth: 0.48
      seven_feat_plus_ld_f1: 0.640
      seven_feat_only_f1: 0.635
      delta_with_ld: 0.005
      bootstrap_delta_p: 0.35
    result_rationale: >
      LD-Score 单独只有 0.605（弱于 7-feature 的 0.635），加入后提升仅 +0.5pp 且 bootstrap 不显著（p=0.35）。
      Character-level features 与 token-level surface features (TTR, hapax) 高度冗余——
      都在捕捉 vocabulary impoverishment 信号，只是粒度不同。
      在 worst 档下，任何 single additional feature 都不会显著改善已经偏弱的 ensemble。
      LD-Score 的 Spearman ρ=0.48 对 depth 有 moderate correlation 但无增量价值。
    tables:
      - name: "Table 15: LD-Score Ablation"
        columns: [Feature Set, Binary F1, Δ vs 7-feature]
        rows:
          - [7-feature, 0.635, "—"]
          - [LD-Score alone, 0.605, -0.030]
          - [7-feature + LD-Score, 0.640, +0.005]
    figures_description: []
    analysis: >
      LD-Score 无增量贡献。可在 appendix 一行提及，不需要主文讨论。
      进一步支持 "vocabulary impoverishment 是 primary signal" 的结论。

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.
      Compares learned representations vs handcrafted features.
    expected_results:
      qlora_3class_f1: 0.750
      qlora_binary_f1: 0.680
      qlora_logo_binary_f1: 0.600
      seven_feat_3class_f1: 0.710
      seven_feat_binary_f1: 0.635
      seven_feat_logo_binary_f1: 0.635
      delta_within_3class: +0.040
      delta_logo_binary: -0.035
    result_rationale: >
      QLoRA within-model 表现更好（3-class +4pp, binary +4.5pp），因为 fine-tuned LM 可以利用
      更多 contextual features（如 phrase repetition patterns, discourse structure）。
      但 LOGO 评估时 QLoRA 下降更严重（0.600 vs 0.635）——overfits generator-specific patterns。
      7-feature ensemble 的 LOGO 更稳定是因为 handcrafted features 更 generator-agnostic。
      在 worst 档叙事下，这产生一个有趣的张力：QLoRA 证明 depth signal exists beyond our 7 features，
      但 learned features 不 generalize。论文可将此解读为：
      "depth signal 存在但分散在多维 feature space 中，没有一个 feature set 能 universally capture it。"
      7-feature ensemble 定位为 "most generalizable baseline"，而非 "best method"。
    tables:
      - name: "Table 16: End-to-End vs Handcrafted Features"
        columns: [Method, Within 3-class F1, Within Binary F1, LOGO Binary F1, Cost]
        rows:
          - [7-feature XGBoost, 0.710, 0.635, 0.635, "1× (410M ref forward pass)"]
          - [QLoRA Qwen-0.8B, 0.750, 0.680, 0.600, "~8× (fine-tuning + inference)"]
    figures_description:
      - "Fig 12: Within-model vs LOGO performance bar chart for both methods. QLoRA's steeper drop from within to LOGO visually demonstrates overfitting."
    analysis: >
      QLoRA 的 generalization gap（-8pp within→LOGO vs 7-feature 的 0pp gap）
      暴露了 end-to-end learning 的 overfitting risk。
      在 benchmark + analysis 重构下，这支持 "7-feature 是 practical baseline" 的定位，
      同时 QLoRA 作为 upper bound 估计展示 room for improvement。

  - name: text_length_control
    plan_id: plan_013
    description: >
      Length confound analysis: length-depth correlation, length-normalized features,
      length-matched classification.
    expected_results:
      length_depth_spearman: -0.22
      length_depth_p: "<0.001"
      length_matched_binary_f1: 0.570
      unmatched_binary_f1: 0.635
      delta_length_matched: -0.065
      normalized_ttr_trend_preserved: true
      normalized_hapax_trend_preserved: true
      normalized_ttr_rho: -0.32
      unmatched_ttr_rho: -0.42
      length_window_ttr_rho: -0.28
    result_rationale: >
      worst 档下，length 是一个非平凡的 confound。Length-depth Spearman ρ=-0.22 虽然 moderate，
      但 length matching 后 binary F1 从 0.635 掉到 0.570（-6.5pp），说明 ~30% 的 apparent depth signal
      来自 length artifact：deeper generations 倾向更短（因为 output truncation 和 quality degradation），
      而 surface features (TTR, hapax) 对 text length 天然敏感。
      Length-normalized TTR/hapax 保留了 depth trend（ρ 仍然 negative），但 magnitude 削弱
      （TTR: -0.42 → -0.32, 约 25% 削弱）。
      这意味着 vocabulary impoverishment 部分是 real depth signal，部分是 length artifact。
      在 worst 档叙事下，必须诚实报告 length-controlled 结果（0.570）作为 deconfounded baseline，
      而非 unmatched 的 0.635。这进一步压低了有效 F1。
    tables:
      - name: "Table 17: Length Confound Analysis"
        columns: [Condition, Binary F1, TTR ρ, hapax ρ]
        rows:
          - [Unmatched, 0.635, -0.42, -0.44]
          - [Length-matched, 0.570, -0.32, -0.36]
          - [Length-normalized features, 0.600, -0.35, -0.38]
    figures_description:
      - "Fig 13: Scatter plot of text length vs depth (with jitter). Moderate negative correlation visible. Side panel: feature drift with/without length control."
    analysis: >
      Length confound 非 trivial。在 worst 档下，deconfounded binary F1=0.570 是 "honest" 的 performance number。
      论文必须报告 length-matched 结果，并在主文讨论 length 作为 confound。
      这不 invalidate depth signal（ρ 仍然 negative after normalization），但 substantially weakens it。

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      Add one 7B+ generator (Qwen3-8B-Base or similar).
      Tests whether depth signal persists at frontier scale.
    expected_results:
      qwen3_8b_logo_binary_f1: 0.530
      qwen3_8b_within_binary_f1: 0.610
      qwen3_8b_3class_f1: 0.550
      spearman_hapax_8b: -0.35
      spearman_ttr_8b: -0.33
      spearman_entropy_mean_8b: -0.28
      ddr_drifting_rho_abs_min_8b: 0.28
      ddr_stationary_rho_abs_max_8b: 0.18
      logo_6gen_avg_f1_with_8b: 0.610
      delta_vs_5gen_baseline: -0.040
    result_rationale: >
      worst 档核心假设：Scale 效应严重——8B+ binary F1 < 0.60。
      Qwen3-8B 的 LOGO binary F1 仅 0.530，within-model 也只有 0.610。
      根本原因：8B 模型的 generation quality 更高——即使 depth-4 文本仍保持较好的 lexical diversity，
      因为更大的 vocabulary capacity 和更强的 contextual coherence 抑制了 vocabulary collapse。
      所有 drifting features 的 |ρ| < 0.35——低于 worst 档定义的 [0.3, 0.4] 下限附近。
      entropy_mean ρ 仅 -0.28，甚至不满足 drifting 标准（|ρ|>0.30）。
      更严重的是 stationary features 也出现了 drift：entropy_std 和 tail_decay 的 |ρ| 达到 0.18，
      进一步瓦解 DDR 框架在 7B+ scale 下的适用性。
      将 8B generator 加入 LOGO 后，6-gen 平均 F1 从 0.650 掉到 0.610（-4pp），
      8B 成为 weakest link 拖拽整体性能。
      这是 "signal disappears at scale" boundary 的核心证据。
    tables:
      - name: "Table 18: Large-Scale Generator (Qwen3-8B) Analysis"
        columns: [Metric, Qwen3-8B, 5-gen avg (≤2.8B), Δ]
        rows:
          - [LOGO Binary F1, 0.530, 0.650, -0.120]
          - [Within Binary F1, 0.610, 0.720, -0.110]
          - [hapax ρ, -0.35, -0.50, +0.15]
          - [TTR ρ, -0.33, -0.48, +0.15]
          - [entropy_mean ρ, -0.28, -0.42, +0.14]
      - name: "Table 19: DDR Pattern at 8B Scale"
        columns: [Feature, |ρ| 8B, |ρ| ≤2.8B avg, DDR Category (8B)]
        rows:
          - [hapax_ratio, 0.35, 0.50, drifting (marginal)]
          - [TTR, 0.33, 0.48, drifting (marginal)]
          - [entropy_mean, 0.28, 0.42, "FAILS drifting threshold"]
          - [entropy_std, 0.18, 0.15, "FAILS stationary threshold"]
          - [tail_decay, 0.15, 0.07, stationary (marginal)]
          - [entropy_max, 0.10, 0.05, stationary]
          - [entropy_min, 0.16, 0.18, "AMBIGUOUS"]
    figures_description:
      - "Fig 14: Feature drift comparison: small models (≤2.8B) vs 8B. Radar chart showing |ρ| compression at 8B scale."
    analysis: >
      8B scale 是 depth signal 的 cliff edge。DDR 在 8B 下几乎不成立——
      entropy_mean 不满足 drifting 标准，entropy_std 不满足 stationary 标准。
      在 worst 档重构叙事下，这是 empirical boundary map 最重要的维度之一。
      论文标题中的 "Empirical Boundaries" 主要指的就是这个 scale boundary。
      reviewer 会问 "does this work on GPT-4 scale?"——答案是 almost certainly not，
      而且论文诚实地承认并量化了 boundary。这在 Findings-level 是 acceptable 的。

  - name: ordinal_baseline_comparison
    plan_id: plan_015
    description: >
      CRITICAL baseline: test whether existing detector continuous scores already provide
      ordinal depth signal. Compare single-feature ordinal classifiers vs 7-feature model.
    expected_results:
      seven_feature_logo_f1: 0.635
      seven_feature_ci: [0.615, 0.655]
      avg_logprob_logo_f1: 0.625
      avg_logprob_ci: [0.595, 0.655]
      ld_score_logo_f1: 0.590
      ld_score_ci: [0.555, 0.625]
      fast_detect_gpt_logo_f1: 0.540
      fast_detect_gpt_ci: [0.505, 0.575]
      binoculars_logo_f1: 0.510
      binoculars_ci: [0.470, 0.550]
      bootstrap_delta_7feat_vs_avglogprob:
        delta_pp: 1.0
        p: 0.18
        significant: false
      bootstrap_delta_7feat_vs_ldscore:
        delta_pp: 4.5
        p: 0.02
        significant: true
      avg_logprob_spearman: 0.58
      best_single_detector: "avg_logprob"
      seven_feature_advantage_pp: 1.0
    result_rationale: >
      worst 档核心假设：avg_logprob 单特征在完整 LOGO 下与 7-feature 差距 <1.5pp（bootstrap 不显著）。
      预测 delta 仅 1.0pp（0.635 vs 0.625），bootstrap p=0.18 不显著。
      根本原因：avg_logprob 本质上是 entropy_mean 的近似值（两者 Pearson r>0.95），
      而 entropy_mean 已被确认为 7-feature 中 importance 最高的特征之一。
      当其他 6 个特征的增量贡献都很弱时（surface features 部分冗余，shape features "stationary" 即无贡献），
      7-feature 退化为 ~avg_logprob + noise。
      这是 worst 档最 devastating 的结果——7-feature ensemble 的核心 selling point（custom feature engineering）
      相对于一个 trivial baseline 没有统计显著优势。
      论文必须承认 avg_logprob 是 competitive baseline，7-feature 的 value proposition 转向
      interpretability（DDR analysis, feature behavior characterization）而非 accuracy。
      FastDetectGPT 和 Binoculars 明显更弱（-9.5pp 和 -12.5pp），因为它们不是为 ordinal depth 设计的。
    tables:
      - name: "Table 20: Ordinal Baseline Comparison (LOGO Binary F1)"
        columns: [Method, LOGO Binary F1, 95% CI, Δ vs 7-feature, Bootstrap p]
        rows:
          - [7-feature XGBoost, 0.635, "[0.615, 0.655]", "—", "—"]
          - [avg_logprob (single), 0.625, "[0.595, 0.655]", -0.010, "0.18 (NS)"]
          - [LD-Score (single), 0.590, "[0.555, 0.625]", -0.045, "0.02*"]
          - [FastDetectGPT (single), 0.540, "[0.505, 0.575]", -0.095, "<0.001***"]
          - [Binoculars (single), 0.510, "[0.470, 0.550]", -0.125, "<0.001***"]
      - name: "Table 21: Feature-Level Depth Correlation"
        columns: [Feature/Detector, Spearman ρ with depth, Type]
        rows:
          - [avg_logprob, -0.58, "single detector"]
          - [hapax_ratio, -0.44, "surface feature"]
          - [TTR, -0.42, "surface feature"]
          - [entropy_mean, -0.40, "reference feature"]
          - [LD-Score, -0.48, "single detector"]
          - [entropy_std, -0.15, "reference feature"]
          - [entropy_max, 0.05, "reference feature"]
          - [tail_decay, -0.07, "reference feature"]
          - [FastDetectGPT, -0.30, "single detector"]
          - [Binoculars, -0.12, "single detector"]
    figures_description:
      - "Fig 15: Bootstrap distribution of (7-feature F1 - avg_logprob F1). Distribution centered near 0.01 with heavy overlap at 0. Vertical line at 0 within 95% CI."
      - "Fig 16: Ranked bar chart of all detectors/features by LOGO binary F1. 7-feature barely above avg_logprob, clear gap to LD-Score and below."
    analysis: >
      这是 worst 档的 smoking gun。avg_logprob 单特征与 7-feature ensemble 不可区分。
      Custom feature engineering 的增量价值在统计上为零。
      论文重构关键：7-feature 不再定位为 "method contribution"，
      而是 "interpretable analysis tool"——通过分解为 surface + reference features 来理解 WHY depth signal exists，
      而非 achieve better accuracy。
      这自然导向 "benchmark + analysis" 定位：contribution 不是 better classification，
      而是 systematic understanding of when and why depth signal exists or fails。
      avg_logprob 作为 strong baseline 被 prominently reported，7-feature 作为 analysis instrument。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd7dd875-9bee-4cb0-8829-bd6a71ff5cf2",
  "isSidechain": false,
  "requestId": "req_011CbEin2oU7zF5an8ohJsga",
  "type": "assistant",
  "uuid": "ac94fdf3-c718-4347-8ee8-2a2f81b3aa8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157AH3tp4wL9JgiTVvfj7pg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7626,
      "cache_read_input_tokens": 40175,
      "output_tokens": 17261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7626,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17261,
          "cache_read_input_tokens": 40175,
          "cache_creation_input_tokens": 7626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7626
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。 核心假设：[\"DDR 二分法在 ≥9 generators 下瓦解：≥3 个 'stationary' 特征出现显著 drift (|ρ|>0.15)，或 drifti…",
  "leafUuid": "ac94fdf3-c718-4347-8ee8-2a2f81b3aa8b",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Worst-case scenario analysis for generation depth fingerprinting",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。 核心假设：[\"DDR 二分法在 ≥9 generators 下瓦解：≥3 个 'stationary' 特征出现显著 drift (|ρ|>0.15)，或 drifti…",
  "leafUuid": "ac94fdf3-c718-4347-8ee8-2a2f81b3aa8b",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Worst-case scenario analysis for generation depth fingerprinting",
  "sessionId": "fc89bc3c-468d-4ff9-a7c1-f5133638f03b"
}
```

---
