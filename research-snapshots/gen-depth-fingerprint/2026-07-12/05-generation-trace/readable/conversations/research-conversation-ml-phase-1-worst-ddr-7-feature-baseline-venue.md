# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。 核心假设：

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-1/da744110-76ce-4c79-a256-c6f62d091013.jsonl`
- **Structured JSON:** [`442428480a544c9d1615.json`](../../sessions/44/442428480a544c9d1615.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T23:46:51.639Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T23:46:51.639Z",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。\n核心假设：[\"DDR 二分法在 ≥9 generators 下瓦解：≥3 个 'stationary' 特征出现显著 drift (|ρ|>0.15)，或 drifting 特征在 ≥7B 模型上 plateau\", 'avg_logprob 单特征在完整 LOGO 下与 7-feature 差距 <1.5pp（bootstrap 不显著）', 'Cross-model chains 无优势或更差 (binary F1 ≤ 0.70)，heterogeneity 假设被否', 'Scale 效应严重：8B+ binary F1 < 0.60，14B DDR ρ gap < 0.30', \"per-gen binary F1 方差 >15pp，部分 generator < 0.55，'generalizable depth signal' claim 不成立\", '温度 scope 实质收窄至 t=0.7 单点；cross-temperature transfer 完全失败', \"Reviewer 认为 'base models + t=0.7 + ≤14B' 的适用范围太窄，缺乏 practical impact\"]\n关键指标范围：{'logo_binary_f1_8gen': [0.62, 0.66], 'logo_binary_f1_9gen': [0.58, 0.63], 'lofo_binary_f1': [0.56, 0.63], 'cross_model_binary_f1': [0.58, 0.7], 'ddr_drifting_rho_abs_min': [0.3, 0.4], 'ddr_stationary_rho_abs_max': [0.15, 0.3], 'seven_feat_minus_best_single_pp': [0.0, 1.5], 'scale_8b_logo_binary_f1': [0.48, 0.58], 'llm_rephrase_drop_pp': [6.0, 12.0]}\n叙事方向：放弃 DDR 作为核心贡献。重构为 'Generation Depth Estimation: Task Formulation, Baselines, and Empirical Boundaries.' 三项重定位的贡献：(1) Task formulation——depth estimation 作为超越 binary detection 的新任务，含 leak-free evaluation protocol (LOGO binary metric 排除 gen-0 seed sharing)；这是 novelty 的主要来源。(2) Empirical boundary map——系统测定 depth signal 存在的条件空间 (small base models, t≤0.7, surface features) 与消失的条件空间 (instruct, high temp, ≥7B scale)；承认 avg_logprob 是 competitive baseline，7-feature 的价值在 interpretability 而非 accuracy。(3) Negative downstream finding 不变，仍是独立贡献。实质上从 method paper 转为 benchmark + analysis paper。Task novelty + 诚实的 empirical boundary mapping + negative finding 三重组合仍足以支撑 EMNLP Findings。不降级 venue。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_logo_f1: 0.7879\n    overall_ci95:\n    - 0.783\n    - 0.7929\n    spearman_entropy_max: 0.0503\n    spearman_entropy_min: -0.4061\n    spearman_hapax: -0.6467\n    spearman_ttr: -0.6302\n    spearman_entropy_mean: -0.6098\n    spearman_entropy_std: -0.1996\n    spearman_tail_decay: -0.0403\n- exp_id: plan-010-robustness\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_binary_f1: 0.695\n    5pct_binary_f1: 0.65\n    10pct_binary_f1: 0.614\n    20pct_binary_f1: 0.591\n    5pct_drop: -0.046\n    10pct_drop: -0.081\n    20pct_drop: -0.104\n- exp_id: plan-010-llm-rephrase\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_binary_f1: 0.6918\n    original_binary_ci:\n    - 0.6749\n    - 0.7067\n    original_multiclass_f1: 0.7385\n    original_multiclass_ci:\n    - 0.7269\n    - 0.7496\n    rephrased_binary_f1: 0.6471\n    rephrased_binary_ci:\n    - 0.6308\n    - 0.6619\n    rephrased_multiclass_f1: 0.6672\n    rephrased_multiclass_ci:\n    - 0.6548\n    - 0.6796\n    binary_drop: -0.0447\n    multiclass_drop: -0.0713\n    edit_distance_ratio: 0.5071\n    avg_sentences_replaced: 1.69\n    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\n    bugs_fixed:\n    - binary_task_gen1_vs_gen2+\n    - 3class_mapping\n    - tail_decay_rank100-1000\n- exp_id: plan-008-seed-stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_complexity_binary: 0.685\n    medium_binary: 0.695\n    high_complexity_binary: 0.695\n    low_complexity_multi: 0.772\n    medium_multi: 0.778\n    high_complexity_multi: 0.779\n    max_diff_binary_pp: 1.06\n    max_diff_multiclass_pp: 0.68\n    conclusion_label: seed_independent\n- exp_id: multi-domain-seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7459\n    news_binary_ci:\n    - 0.726\n    - 0.764\n    news_multiclass_f1: 0.6516\n    academic_binary_f1: 0.7386\n    academic_binary_ci:\n    - 0.72\n    - 0.757\n    academic_multiclass_f1: 0.6223\n    code_binary_f1: 0.7535\n    code_binary_ci:\n    - 0.737\n    - 0.77\n    code_multiclass_f1: 0.6344\n    wikipedia_baseline_binary_f1: 0.8148\n    wikipedia_baseline_multiclass_f1: 0.8632\n    max_gap_vs_wiki_pp: 7.62\n    worst_domain: academic\n    best_domain: code\n    conclusion_label: domain_independent\n- exp_id: exp_047_multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7119\n    news_binary_ci:\n    - 0.6898\n    - 0.7332\n    news_3class_f1: 0.7149\n    academic_binary_f1: 0.6279\n    academic_binary_ci:\n    - 0.6027\n    - 0.6515\n    academic_3class_f1: 0.6564\n    code_binary_f1: 0.6872\n    code_binary_ci:\n    - 0.6641\n    - 0.71\n    code_3class_f1: 0.6729\n    overall_binary_f1: 0.6757\n    overall_3class_f1: 0.6814\n    delta_vs_t10_news: -0.034\n    delta_vs_t10_academic: -0.1107\n    delta_vs_t10_code: -0.0663\n- exp_id: multi_domain_t07\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_048_cross_temp_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    6gen_logo:\n      within_0.7_binary: 0.9471\n      within_0.7_3class: 0.7888\n      cross_0.7to1.0_binary: 0.9001\n      cross_0.7to1.0_3class: 0.7225\n      within_1.0_binary: 0.9107\n      within_1.0_3class: 0.7257\n      cross_1.0to0.7_binary: 0.9581\n      cross_1.0to0.7_3class: 0.7913\n      caveat: Only Qwen3-1.7B differs between conditions; 5/6 generators share data\n    qwen_only:\n      within_0.7_binary: 0.9262\n      within_0.7_binary_ci:\n      - 0.916\n      - 0.935\n      within_0.7_3class: 0.769\n      within_0.7_3class_ci:\n      - 0.756\n      - 0.781\n      cross_0.7to1.0_binary: 0.7574\n      cross_0.7to1.0_binary_ci:\n      - 0.745\n      - 0.77\n      cross_0.7to1.0_3class: 0.4581\n      cross_0.7to1.0_3class_ci:\n      - 0.445\n      - 0.472\n      within_1.0_binary: 0.8248\n      within_1.0_binary_ci:\n      - 0.81\n      - 0.838\n      within_1.0_3class: 0.5738\n      within_1.0_3class_ci:\n      - 0.56\n      - 0.588\n      cross_1.0to0.7_binary: 0.9443\n      cross_1.0to0.7_binary_ci:\n      - 0.936\n      - 0.953\n      cross_1.0to0.7_3class: 0.6014\n      cross_1.0to0.7_3class_ci:\n      - 0.593\n      - 0.611\n      delta_0.7train_binary_pp: -16.9\n      delta_0.7train_3class_pp: -31.1\n      delta_1.0train_binary_pp: 12\n      delta_1.0train_3class_pp: 2.8\n      asymmetric_transfer: true\n- exp_id: exp_049_temp_curve_t05\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 4708\n    skipped: 113\n    seeds: 995\n    model: pythia-2.8b\n    temperature: 0.5\n    top_p: 0.9\n    within_cv_binary_f1: 0.8432\n    within_cv_binary_ci:\n    - 0.8301\n    - 0.8558\n    logo_binary_f1: 0.8136\n    logo_binary_ci:\n    - 0.7984\n    - 0.8282\n    entropy_mean_rho: -0.5844\n- exp_id: exp_050_temp_curve_t09\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    records: 4536\n    model: pythia-2.8b\n    temperature: 0.9\n    top_p: 0.9\n    within_cv_binary_f1: 0.5821\n    within_cv_binary_ci:\n    - 0.5655\n    - 0.5985\n    logo_binary_f1: 0.4804\n    logo_binary_ci:\n    - 0.4645\n    - 0.4976\n    entropy_mean_rho: -0.3016\n    delta_vs_t07_cv: -0.157\n    delta_vs_t07_logo: -0.259\n- exp_id: exp_051_independent_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_to_olmo_binary_f1: 0.6945\n    pythia_to_olmo_ci:\n    - 0.6727\n    - 0.7167\n    olmo_to_pythia_binary_f1: 0.666\n    olmo_to_pythia_ci:\n    - 0.6429\n    - 0.6893\n    avg_binary_f1: 0.6803\n    shared_seed_logo_ref: 0.694\n    delta_vs_shared: -0.014\n- exp_id: exp_052_instruct_qwen3_1_7b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8753\n    within_binary_ci:\n    - 0.8667\n    - 0.8837\n    within_3class_f1: 0.7324\n    within_3class_ci:\n    - 0.7195\n    - 0.745\n    base_binary_f1: 0.8614\n    base_3class_f1: 0.769\n    logo_instruct_binary: 0.658\n    logo_instruct_3class: 0.543\n    logo_base_binary: 0.821\n    logo_base_3class: 0.802\n    gen1_f1_instruct: 0.438\n    gen1_f1_base: 0.579\n    spearman_direction: reversed (instruct ρ>0, base ρ<0)\n    delta_within_binary: 0.014\n    delta_within_3class: -0.037\n    delta_logo_binary: -0.163\n- exp_id: exp_053_instruct_olmo2_1b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8131\n    within_binary_ci:\n    - 0.8012\n    - 0.8251\n    within_3class_f1: 0.5748\n    within_3class_ci:\n    - 0.5605\n    - 0.5897\n    base_binary_f1: 0.8454\n    base_3class_f1: 0.7538\n    gen1_f1_instruct: 0.256\n    gen1_f1_base: 0.523\n    delta_within_binary: -0.032\n    delta_within_3class: -0.179\n    spearman_instruct:\n      entropy_mean: 0.482\n      entropy_std: 0.296\n      entropy_min: 0.08\n      entropy_max: 0.306\n      tail_decay: 0.228\n      ttr: 0.006\n      hapax_ratio: 0.025\n    spearman_base:\n      entropy_mean: -0.639\n      entropy_std: -0.296\n      entropy_min: -0.387\n      entropy_max: 0.067\n      tail_decay: -0.141\n      ttr: -0.7\n      hapax_ratio: -0.712\n    features_reversed: 6/7\n    model_used: allenai/OLMo-2-0425-1B-Instruct\n- exp_id: exp_054_instruct_llama3_2_3b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    instruct_binary_f1: 0.8381\n    instruct_binary_ci:\n    - 0.828\n    - 0.847\n    instruct_3class_f1: 0.5437\n    instruct_3class_ci:\n    - 0.53\n    - 0.558\n    base_binary_f1: 0.8488\n    base_3class_f1: 0.7424\n    rho_instruct_entropy_mean: 0.2299\n    rho_instruct_entropy_std: 0.2623\n    rho_instruct_entropy_min: -0.0027\n    rho_instruct_entropy_max: 0.2036\n    rho_instruct_tail_decay: 0.1198\n    rho_instruct_ttr: -0.1411\n    rho_instruct_hapax_ratio: -0.1157\n    rho_base_entropy_mean: -0.627\n    rho_base_ttr: -0.6856\n    rho_base_hapax_ratio: -0.6975\n    direction_reversals: 3\n    reversed_features:\n    - entropy_mean\n    - entropy_std\n    - tail_decay\n    data_count: 4974\n- exp_id: exp_055_qlora_olmo_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8881\n    macro_f1_3class_std: 0.0071\n    macro_f1_5class: 0.5976\n    macro_f1_5class_std: 0.0046\n    binary_f1: 0.8363\n    binary_f1_std: 0.0096\n    n_samples: 4429\n    runtime_seconds: 1689.7\n- exp_id: exp_056_qlora_qwen_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.9066\n    macro_f1_3class_std: 0.0082\n    macro_f1_5class: 0.5514\n    macro_f1_5class_std: 0.0031\n    binary_f1: 0.8672\n    binary_f1_std: 0.0137\n    n_samples: 4963\n    runtime_seconds: 1880.5\n- exp_id: exp_055b_qlora_olmo_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8588\n    macro_f1_3class_std: 0.0036\n    macro_f1_5class: 0.5398\n    macro_f1_5class_std: 0.015\n    binary_f1: 0.7925\n    binary_f1_std: 0.0097\n    n_samples: 2379\n    runtime_seconds: 911.7\n    note: completed before kill signal\n- exp_id: exp_056b_qlora_qwen_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.904\n    macro_f1_3class_std: 0.0094\n    macro_f1_5class: 0.5544\n    macro_f1_5class_std: 0.0068\n    binary_f1: 0.8597\n    binary_f1_std: 0.0123\n    n_samples: 2291\n    runtime_seconds: 880.9\n    note: completed before kill signal\n- exp_id: exp_057_scale_9gen_logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: superseded by exp_057 (rerun with fixed Gemma data)\n    first_run_3class_f1: 0.7516\n    first_run_binary_f1: 0.6842\n    see_exp_057_for_final: true\n- exp_id: exp_058_ddr_causality\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    permutation_baseline_f1: 0.7714\n    drifting_avg_importance: 0.1578\n    stationary_avg_importance: 0.0297\n    drifting_stationary_ratio: 5.31\n    granger_significant_features: 6/7\n    granger_max_delta_r2: 0.031\n    granger_max_delta_r2_feature: entropy_std\n    granger_nonsig_feature: entropy_min\n    granger_panel_n: 29095\n    intervention_max_f1_drop: 0.0203\n    intervention_max_feature: entropy_max\n    intervention_min_f1_drop: 0.0061\n- exp_id: exp_059_tost_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_bootstrap: 1000\n    seed: 42\n    margin_d: 0.2\n    entropy_max:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.062\n      d_ci:\n      - 0.037\n      - 0.088\n    entropy_min:\n      median_p: 0\n      rejection_rate: 1\n      median_d: -0.016\n      d_ci:\n      - -0.042\n      - 0.011\n    tail_decay:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.088\n      d_ci:\n      - 0.065\n      - 0.111\n    entropy_std:\n      median_p: 1\n      rejection_rate: 0\n      median_d: 0.458\n      d_ci:\n      - 0.435\n      - 0.479\n    stationary_features_robust: true\n- exp_id: exp_057\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    9gen_logo_3class_f1: 0.751\n    9gen_logo_binary_f1: 0.6661\n    8gen_baseline_3class_f1: 0.7698\n    delta_9gen_vs_8gen: -0.0188\n    n_total_rows: 42015\n    n_generators: 9\n    qwen3_8b_3class_f1: 0.6955\n    qwen3_8b_binary_f1: 0.6468\n    gemma_2_2b_3class_f1: 0.6279\n    gemma_2_2b_binary_f1: 0.4402\n    per_gen_3class_f1:\n      pythia-1b: 0.8571\n      qwen3-0.6b: 0.8185\n      pythia-2.8b: 0.8117\n      qwen3-1.7b: 0.8114\n      olmo-2-1b: 0.7732\n      llama-3.2-3b: 0.7591\n      qwen3-8b: 0.6955\n      gemma-2-2b: 0.6279\n      mistral-7b-v0.3: 0.6045\n    tail_decay_consistency: VERIFIED_all_9gen_logprob_slope\n    data_source: features_9gen.csv (42015 rows, Gemma fixed)\n- exp_id: exp_060_14b_ddr_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 2229\n    n_seeds: 498\n    depth_distribution:\n      '0': 498\n      '1': 488\n      '2': 466\n      '3': 414\n      '4': 363\n    entropy_mean:\n      rho: -0.3877\n      d: 0.7765\n      group: drifting\n    entropy_std:\n      rho: -0.0557\n      d: -0.0223\n      group: stationary\n    entropy_max:\n      rho: 0.0791\n      d: -0.1717\n      group: stationary\n    entropy_min:\n      rho: -0.2471\n      d: -0.1365\n      group: stationary\n    ttr:\n      rho: -0.4916\n      d: 1.0913\n      group: drifting\n    hapax_ratio:\n      rho: -0.5065\n      d: 1.1245\n      group: drifting\n    tail_decay:\n      rho: -0.0637\n      d: 0.1356\n      group: stationary\n    ddr_pattern_match: true\n- exp_id: exp_061_instruct_ref_ddr\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwen_instruct:\n      base_ref_rho_entropy_mean: 0.478\n      instruct_ref_rho_entropy_mean: 0.221\n      base_ref_d_entropy_mean: 1.981\n      instruct_ref_d_entropy_mean: 1.022\n    olmo_instruct:\n      base_ref_rho_entropy_mean: 0.482\n      instruct_ref_rho_entropy_mean: -0.113\n      base_ref_d_entropy_mean: 1.33\n      instruct_ref_d_entropy_mean: 0.017\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T23:46:51.642Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T23:46:51.642Z",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-20T23:46:51.661Z_

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
  "promptId": "3ec891c4-1ee6-4792-af4a-2cbd06cffd86",
  "type": "user",
  "uuid": "d73321bd-f827-4b98-b1f4-b9234e9d4a73",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T23:46:51.659Z_

```json
{
  "parentUuid": "d73321bd-f827-4b98-b1f4-b9234e9d4a73",
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
  "uuid": "4a5bd3d3-1139-4056-8e98-37af626d3553",
  "timestamp": "2026-05-20T23:46:51.659Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T23:46:51.659Z_

```json
{
  "parentUuid": "4a5bd3d3-1139-4056-8e98-37af626d3553",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "06aeacad-b0df-495a-b207-30dba843203e",
  "timestamp": "2026-05-20T23:46:51.659Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013",
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
  "leafUuid": "06aeacad-b0df-495a-b207-30dba843203e",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013"
}
```

---

### Assistant

_source line 7 · 2026-05-20T23:46:54.516Z_

I'll analyze the experiment plan and project context to generate detailed worst-tier predictions for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06aeacad-b0df-495a-b207-30dba843203e",
  "isSidechain": false,
  "requestId": "req_011CbEiJEmX7dzk4uUiuiVAo",
  "type": "assistant",
  "uuid": "79097e87-8ea8-4b74-bfb3-7319c403b9f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHQeFC2vVGYgobe26UuotU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 135,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24881
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

_source line 8 · 2026-05-20T23:46:56.348Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JVYsjRNn8odxiCjefxbxLx`</summary>

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
  "parentUuid": "79097e87-8ea8-4b74-bfb3-7319c403b9f5",
  "isSidechain": false,
  "requestId": "req_011CbEiJEmX7dzk4uUiuiVAo",
  "type": "assistant",
  "uuid": "6a8f0719-ed37-4d7d-b678-a0502d262cf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHQeFC2vVGYgobe26UuotU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 135,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24881
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

_source line 9 · 2026-05-20T23:46:56.361Z_

<details><summary>↩ Tool result · `toolu_01JVYsjRNn8odxiCjefxbxLx`</summary>

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
  "parentUuid": "6a8f0719-ed37-4d7d-b678-a0502d262cf1",
  "isSidechain": false,
  "promptId": "3ec891c4-1ee6-4792-af4a-2cbd06cffd86",
  "type": "user",
  "uuid": "2245761e-14db-4c2d-81a2-a9fc07164833",
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
  "sourceToolAssistantUUID": "6a8f0719-ed37-4d7d-b678-a0502d262cf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation empirical boundaries and task formulation",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013"
}
```

---

### Assistant

_source line 11 · 2026-05-20T23:47:37.059Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the worst-tier definition and all the planned experiments to generate detailed predictions. I need to understand:

1. The worst-tier means DDR framework collapses, 7-feature vs single baseline is not significant, paper must pivot to benchmark+analysis paper
2. Key metric ranges are defined
3. Need to generate predictions for each planned experiment with rationale

Let me go through each experiment in the plan and generate worst-tier predictions.

The experiments are:
- plan_001: feature_ablation_and_trend (DONE - already completed)
- plan_002: cross_generator_evaluation (DONE)


- plan_003: cross_family_reference_model (DONE)
- plan_004: downstream_utility (DONE)
- plan_005: prompt_type_comparison (DONE)
- plan_006: paraphrastic_comparison (planned)
- plan_007: cross_model_chains (planned)
- plan_008: multi_domain_seeds (partially done)
- plan_009: finer_grained_ordinal (planned)
- plan_010: human_edit_robustness (DONE)
- plan_011: ld_score_feature (planned)
- plan_012: end_to_end_classifier (planned)
- plan_013: text_length

Now I'm reviewing the full experiment pipeline to see which ones are complete, in progress, or still planned.

Looking at the experiment_plan more carefully, I notice the user is asking for worst-tier predictions across all 15 experiments, not just the ones marked as planned. The registry shows some completed, but I need to generate detailed worst-case scenario predictions for each one. I'm identifying the key characteristics that would indicate DDR breakdown—like when stationary features show significant drift beyond the 0.15 threshold or when drifting features plateau unexpectedly.

Now I'm mapping out the worst-tier metric ranges I'd expect to see: binary F1 scores dropping to 0.62-0.66 for the 8-generator setup, dipping to 0.58-0.63 for 9-generator, and falling to 0.56-0.63 for LOFO. Cross-model performance would stagnate around 0.58 or worse, with temperature scope collapsing to just t=0.7 and no meaningful transfer across temperatures.

The narrative's shifting away from DDR as the main story—instead I'm framing this around "Generation Depth Estimation: Task Formulation, Baselines, and Empirical Boundaries" to better capture what's actually happening with these constraints.

Now I'm working through predictions for each experiment, starting with the feature ablation and trend analysis.

For the feature ablation, surface and reference features would perform much more similarly than expected, the H1/H2 split gets messier with some supposedly stationary features showing drift behavior, and perplexity pre-validation might retain some signal but noticeably weaker.

Cross-generator evaluation shows LOGO binary F1 landing around 0.62-0.66 with substantial per-generator variance exceeding 15 percentage points, and some generators dipping below 0.55. The cross-family reference model experiments reveal that the DDR pattern partially breaks when using non-Pythia references, with certain stationary features becoming drifting under different reference models. Downstream utility remains a negative finding across all tiers—depth-based curation doesn't actually help. For prompt type comparisons, continuation prompts might show some promise but elaboration and rewriting tasks are where things fall apart.

Paraphrastic variants might actually match or exceed the signal from non-paraphrastic versions, which would undermine the claimed uniqueness of the approach. Cross-model chains yield binary F1 scores at or below 0.70, falsifying the heterogeneity hypothesis. Multi-domain seeds reveal large domain gaps with some domains performing substantially worse. Fine-grained ordinal classification drops to 0.35-0.40 F1 with five classes, and ordinal methods don't improve this. Human edit robustness shows significant degradation even with minor edits, with LLM rephrasings causing 6-12 percentage point drops.

LD-Score contributes minimal additional value and may be redundant with existing features. End-to-end learned representations could match or slightly outperform the 7-feature baseline, questioning whether handcrafted features are necessary. Text length control reveals that surface features partially track length, with substantial F1 drops when controlling for it. Scaling to 8B+ models yields binary F1 below 0.60, compressing the DDR ρ gap. Finally, ordinal baseline comparison shows that average log probability alone gets within 1.5 percentage points of the 7-feature model, with bootstrap tests showing no significant difference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2245761e-14db-4c2d-81a2-a9fc07164833",
  "isSidechain": false,
  "requestId": "req_011CbEiJaywRD1ZpFdJBnLyL",
  "type": "assistant",
  "uuid": "bd1a1703-a67d-42a2-940c-260fb00030f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131BcQxEp1PxFLF78z5Hnz7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 307,
      "cache_read_input_tokens": 36722,
      "output_tokens": 15869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15869,
          "cache_read_input_tokens": 36722,
          "cache_creation_input_tokens": 307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 307
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

_source line 12 · 2026-05-20T23:52:00.320Z_

```yaml
tier: worst
narrative_guidance: >
  DDR 框架不成立为通用现象。放弃 DDR 作为核心贡献，重构为 'Generation Depth Estimation: Task Formulation,
  Baselines, and Empirical Boundaries.' 三项重定位贡献：(1) Task formulation——depth estimation
  作为超越 binary detection 的新任务，含 leak-free evaluation protocol；(2) Empirical boundary
  map——系统测定 depth signal 存在与消失的条件空间；(3) Negative downstream finding 不变。从 method paper
  转为 benchmark + analysis paper。avg_logprob 是 competitive baseline，7-feature 的价值仅在
  interpretability。仍可支撑 EMNLP Findings，但 framing 完全转向诚实的 empirical boundary mapping +
  negative results 组合。

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      三部分分析：(A) Feature ablation: reference-only vs surface-only vs full,
      XGBoost 5-fold CV；(B) H1/H2 trend analysis: 各特征 mean±std across depth 0-4；
      (C) Perplexity pre-validation for Claim 3。
    expected_results:
      full_macro_f1: 0.783
      reference_only_f1: 0.748
      surface_only_f1: 0.756
      ref_vs_surf_gap_pp: -0.8
      mcnemar_ref_vs_surf_p: 0.09
      full_vs_surface_gap_pp: 2.7
      h2_features: "entropy_mean (slope=-0.31, R²=0.72), ttr (slope=-0.18, R²=0.65), hapax_ratio (slope=-0.22, R²=0.69)"
      h1_features_problematic: "entropy_std (slope=-0.14, R²=0.48 — unexpected drift), entropy_min (slope=-0.12, R²=0.41)"
      h1_clean: "tail_decay (slope=+0.02, R²=0.03), entropy_max (slope=+0.04, R²=0.08)"
      stationary_features_with_drift_count: 2
      entropy_std_rho: -0.22
      entropy_min_rho: -0.19
      tail_decay_rho: 0.04
      entropy_max_rho: 0.07
      median_ppl_by_depth: "14.1, 5.2, 3.3, 2.4, 1.9"
      ppl_depth_correlation_significant: true
    result_rationale: >
      在 worst 档下，reference-only 与 surface-only 差距不显著 (McNemar p=0.09)，full 仅比
      surface 好 2.7pp——表明 reference features 的独立贡献可疑。关键：entropy_std 和 entropy_min
      出现意外的 drift (|ρ|>0.15)，打破了 DDR 的 drifting/stationary 二分法。仅 tail_decay 和
      entropy_max 真正保持 stationary。这意味着 "dual dynamics" 叙事中有 2/4 个所谓 stationary
      features 实际上在漂移，DDR 框架从 "4 stationary + 3 drifting" 退化为
      "2 stationary + 5 drifting"，不再构成有意义的二分法，更像是所有特征程度不同地漂移。
      Perplexity 仍显示深度相关性，但这只是为 Claim 3 的 negative finding 铺垫。
    tables:
      - name: "Table A1: Feature Ablation (5-fold CV)"
        columns: [Feature Set, Macro F1, 95% CI]
        rows:
          - [Full (7 features), 0.783, "[0.768, 0.798]"]
          - [Surface-only (TTR + hapax), 0.756, "[0.740, 0.772]"]
          - [Reference-only (5 entropy + tail), 0.748, "[0.731, 0.765]"]
      - name: "Table A2: Per-Feature Depth Trend (Linear Regression)"
        columns: [Feature, Slope, R², Spearman ρ, Category]
        rows:
          - [entropy_mean, -0.31, 0.72, -0.48, drifting]
          - [ttr, -0.18, 0.65, -0.44, drifting]
          - [hapax_ratio, -0.22, 0.69, -0.46, drifting]
          - [entropy_std, -0.14, 0.48, -0.22, "ambiguous (drift)"]
          - [entropy_min, -0.12, 0.41, -0.19, "ambiguous (drift)"]
          - [tail_decay, +0.02, 0.03, +0.04, stationary]
          - [entropy_max, +0.04, 0.08, +0.07, stationary]
    figures_description:
      - "Fig A1: 7-panel feature trend plot (depth 0-4, mean±std). entropy_std 和 entropy_min 展示明显的下降趋势线，而非预期的平坦线，CIs 在 depth 0 与 depth 4 之间不重叠。"
    analysis: >
      DDR 二分法部分瓦解。2/4 个 stationary features 实际漂移，只是幅度较小。
      Surface features 与 reference features 差距不显著，表明 vocabulary impoverishment
      是主要信号来源。在 worst 重构下，不宜继续声称 drifting/stationary 分裂；
      改为描述 "features drift at varying rates" 的连续谱。

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      扩展至 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)，
      LOGO CV 测试跨 generator 泛化。25K chains。
    expected_results:
      total_records: 23500
      logo_avg_macro_f1_3class: 0.718
      logo_avg_binary_f1: 0.635
      logo_binary_ci: [0.618, 0.652]
      lofo_binary_f1: 0.593
      lofo_binary_ci: [0.571, 0.615]
      per_gen_binary_f1:
        pythia_2_8b: 0.672
        pythia_1b: 0.708
        olmo_2_1b: 0.614
        qwen3_1_7b: 0.588
        qwen3_0_6b: 0.562
      per_gen_f1_range_pp: 14.6
      per_gen_f1_std: 0.055
      family_out_pythia_held_out: 0.627
      family_out_qwen_held_out: 0.558
      family_out_olmo_held_out: 0.594
      worst_generator: qwen3_0_6b
      best_generator: pythia_1b
    result_rationale: >
      在 worst 档下，LOGO binary F1 落入 [0.62, 0.66] 区间 (0.635)。跨 generator 方差大：
      Pythia family 因为 training data overlap (The Pile) 相互借力，Pythia-1B held-out 表现
      偏高 (0.708)，但这是由 Pythia-2.8B in-training 贡献的。Qwen3 和 OLMo 使用不同 tokenizer
      和 training data，特征分布差异更大，导致 held-out F1 明显更低。Qwen3-0.6B 参数量最小，
      生成质量最不稳定，depth signal 反而最弱 (0.562)——与直觉相反（小模型应该有更强信号），
      这是因为 0.6B 的生成质量太差导致 depth 间差异被 noise 淹没。LOFO 仅 0.593，
      说明跨 family 泛化严重不足。per-gen F1 range 14.6pp，接近但未超过 15pp 阈值。
    tables:
      - name: "Table 2: Leave-One-Generator-Out Binary F1"
        columns: [Held-out Generator, Binary F1, 95% CI, Family]
        rows:
          - [Pythia-2.8B, 0.672, "[0.648, 0.696]", Pythia]
          - [Pythia-1B, 0.708, "[0.685, 0.731]", Pythia]
          - [OLMo-2-1B, 0.614, "[0.588, 0.640]", OLMo]
          - [Qwen3-1.7B, 0.588, "[0.562, 0.614]", Qwen]
          - [Qwen3-0.6B, 0.562, "[0.535, 0.589]", Qwen]
          - ["**Average**", "**0.635**", "[0.618, 0.652]", "—"]
      - name: "Table 2b: Leave-One-Family-Out Binary F1"
        columns: [Held-out Family, Binary F1, 95% CI]
        rows:
          - [Pythia (2 gens), 0.627, "[0.601, 0.653]"]
          - [Qwen (2 gens), 0.558, "[0.531, 0.585]"]
          - [OLMo (1 gen), 0.594, "[0.567, 0.621]"]
          - ["**Average**", "**0.593**", "[0.571, 0.615]"]
    figures_description:
      - "Fig 2: Per-generator LOGO binary F1 bar chart with CIs. 清晰展示 Qwen generators 在底部，Pythia 在顶部，OLMo 居中。"
    analysis: >
      LOFO 0.593 表明 depth signal 有严重的 family-specific component。Pythia 同 family
      互相提升的 confound 明显。在 worst 重构中，诚实报告这一结果作为 "empirical boundary"
      的一部分：depth signal 的跨 family 泛化有条件限制。

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      测试 OLMo-2-1B 和 Qwen3-0.6B 作为 reference model 时 DDR 是否保持。
      关键 falsification test：entropy_mean drift 是否是 Pythia-specific artifact。
    expected_results:
      logo_f1_pythia_ref: 0.635
      logo_f1_olmo_ref: 0.621
      logo_f1_qwen_ref: 0.608
      entropy_drift_all_refs_negative: true
      olmo_ref_drifting_rho:
        entropy_mean: -0.38
        ttr: -0.42
        hapax_ratio: -0.44
      olmo_ref_stationary_rho:
        entropy_std: -0.19
        entropy_max: 0.08
        tail_decay: 0.06
        entropy_min: -0.16
      qwen_ref_drifting_rho:
        entropy_mean: -0.32
        ttr: -0.40
        hapax_ratio: -0.43
      qwen_ref_stationary_rho:
        entropy_std: -0.24
        entropy_max: 0.11
        tail_decay: -0.09
        entropy_min: -0.21
      stationary_features_exceeding_015_count:
        olmo_ref: 2
        qwen_ref: 3
      ddr_pattern_consistent_across_refs: false
    result_rationale: >
      在 worst 档下，entropy_mean drift 的方向在所有 ref models 上一致（均为负），所以 DDR
      不是 Pythia artifact 在这个狭义上。但 drift 幅度大幅衰减（Pythia ref |ρ|~0.48 →
      OLMo ref ~0.38, Qwen ref ~0.32），说明 reference model 与 generator 的 training data
      overlap 放大了 drift 幅度。更致命的是，stationary features 在非 Pythia ref 下表现更差：
      Qwen ref 有 3 个 stationary features 超过 |ρ|>0.15 阈值（entropy_std -0.24,
      entropy_min -0.21, tail_decay -0.09 仅 tail_decay 保持）。这证明 DDR 的
      drifting/stationary 分裂高度依赖 reference model 选择，不是 generation-intrinsic
      的稳健现象。F1 也随 ref model 变化：Pythia ref 最高因为 training data 熟悉度，
      Qwen ref 最低。
    tables:
      - name: "Table 3: DDR Stability Across Reference Models"
        columns: [Feature, Pythia-410M ρ, OLMo-2-1B ρ, Qwen3-0.6B ρ, Stable Category?]
        rows:
          - [entropy_mean, -0.48, -0.38, -0.32, "Yes (drifting)"]
          - [ttr, -0.44, -0.42, -0.40, "Yes (drifting)"]
          - [hapax_ratio, -0.46, -0.44, -0.43, "Yes (drifting)"]
          - [entropy_std, -0.22, -0.19, -0.24, "No (drift in all)"]
          - [entropy_max, +0.07, +0.08, +0.11, "Marginal (stationary)"]
          - [tail_decay, +0.04, +0.06, -0.09, "Marginal (stationary)"]
          - [entropy_min, -0.19, -0.16, -0.21, "No (drift in all)"]
      - name: "Table 3b: LOGO Binary F1 by Reference Model"
        columns: [Reference Model, LOGO Binary F1, 95% CI]
        rows:
          - [Pythia-410M, 0.635, "[0.618, 0.652]"]
          - [OLMo-2-1B, 0.621, "[0.603, 0.639]"]
          - [Qwen3-0.6B, 0.608, "[0.590, 0.626]"]
    figures_description:
      - "Fig 3: Heatmap of |ρ| across 7 features × 3 reference models。展示 stationary features 在不同 ref 下的不稳定性。"
    analysis: >
      DDR 不是 reference-model artifact（方向一致），但 DDR 的 二分法 是 reference-model
      dependent（哪些特征算 stationary 取决于 ref model 选择）。这是 worst 档的核心证据：
      DDR 从 robust phenomenon 降级为 reference-model-dependent observation。
      在重构叙事中，改为报告 "feature drift rates vary by reference model"
      而非声称稳健的 drifting/stationary 分裂。

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune OLMo-1B on depth-stratified subsets，测量 perplexity 作为 depth function。
      ≥3 seeds + bootstrap CIs。Sample-count-matched comparison。
    expected_results:
      all_ppl_mean: 2.338
      all_ppl_std: 0.003
      size_matched_ppl_mean: 2.371
      size_matched_ppl_std: 0.004
      depth01_ppl_mean: 2.390
      depth01_ppl_std: 0.003
      binary_filtered_ppl_mean: 2.393
      binary_filtered_ppl_std: 0.004
      depth0_only_ppl_mean: 2.688
      depth0_only_ppl_std: 0.005
      ranking: "all < size_matched < depth01 ≈ binary_filtered << depth0_only"
      tost_2pct_p: 0.00012
      tost_2pct_significant: true
      cohens_d_depth01_vs_matched: 0.18
      cohens_d_binary_vs_matched: 0.21
      seed_variance: "<0.004 within variant"
    result_rationale: >
      Negative finding 在所有 tier 下基本一致——depth curation 不优于 random subsampling。
      在 worst 档下结果与其他 tier 几乎相同，因为这个实验的 outcome 不依赖于 DDR 是否成立。
      depth0_only 显著更差因为只用了 ~800 samples。depth01 vs size_matched 的差距极小
      (0.019 ppl)，TOST 在 ±2% margin 下显著 (p=0.00012)，确认等价。seed 间方差极低
      (<0.004)，说明结果稳定。这是论文中最不受 tier 影响的实验——negative finding 本身就是
      独立贡献，在 worst 重构中作为第三个贡献保留。
    tables:
      - name: "Table 5: Downstream CLM Perplexity by Training Data Composition"
        columns: [Variant, n_train, Ppl (mean±std), TOST p (±2%)]
        rows:
          - [All depths, 12299, "2.338 ± 0.003", "—"]
          - [Size-matched random, 3951, "2.371 ± 0.004", "ref"]
          - [Depth 0+1 only, 3951, "2.390 ± 0.003", 0.00012]
          - [Binary-filtered, 3951, "2.393 ± 0.004", 0.00008]
          - [Depth 0 only, 797, "2.688 ± 0.005", "<0.001 (reject equiv.)"]
    figures_description:
      - "Fig 5: Perplexity bar chart with error bars (3 seeds). 展示 depth curation 无优势。"
    analysis: >
      Negative finding 稳健。Depth-aware curation 不优于 random subsampling。
      这是 worst 重构中保留的第三个独立贡献。

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Continuation vs elaboration vs inspired_rewriting chains。Pythia-2.8B, 1000 seeds。
    expected_results:
      cv_f1_continuation: 0.712
      cv_f1_elaboration: 0.648
      cv_f1_rewriting: 0.667
      lopto_avg_f1: 0.615
      lopto_held_out_cont: 0.632
      lopto_held_out_elab: 0.601
      lopto_held_out_rewrite: 0.612
      depth_retention_d4_d0:
        continuation: 0.82
        elaboration: 0.98
        rewriting: 0.94
      drift_hapax_ratio:
        continuation: -0.52
        elaboration: -0.61
        rewriting: -0.57
      drift_entropy_mean:
        continuation: -0.38
        elaboration: -0.31
        rewriting: -0.34
      cross_prompt_transfer_f1: 0.58
      prompt_type_f1_range_pp: 6.4
    result_rationale: >
      在 worst 档下，所有 prompt type 的 F1 均偏低。Continuation 最高 (0.712) 但远低于
      实际已观测的 0.781。Elaboration 最低 (0.648) 因为 elaboration chains 在语义上更保守，
      depth 间的 distributional shift 更小。关键问题：cross-prompt transfer 极差 (0.58)，
      意味着 depth signal 高度 prompt-type specific。这在 worst 叙事下进一步缩窄适用范围：
      不仅限于 base models + t≤0.7，还限于特定 prompt type。prompt_type_f1_range 6.4pp
      说明 prompt type 是重要的 confound。Drift 幅度在所有 prompt types 上均偏弱
      (|ρ| 在 0.31-0.61)，因为 worst 档下 drifting features 的 drift 本身就较弱。
    tables:
      - name: "Table 4: Depth Signal by Prompt Type (Pythia-2.8B)"
        columns: [Prompt Type, CV Binary F1, LOPTO F1, Retention d4/d0, hapax ρ]
        rows:
          - [Continuation, 0.712, 0.632, 0.82, -0.52]
          - [Inspired rewriting, 0.667, 0.612, 0.94, -0.57]
          - [Elaboration, 0.648, 0.601, 0.98, -0.61]
          - [Cross-prompt transfer, "—", 0.58, "—", "—"]
    figures_description:
      - "Fig 4: Three-panel drift plot (hapax, ttr, entropy_mean) by prompt type。展示 continuation 有最清晰的 depth gradient，elaboration 最平坦。"
    analysis: >
      Prompt type 依赖性强。Cross-prompt transfer 失败意味着在 worst 重构中，
      必须诚实报告 depth signal 是 prompt-type-conditioned 的。

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      构建 parallel paraphrasing chains，与 continuation chains 直接对比。
      测试 attractor convergence theory。
    expected_results:
      paraphrastic_cv_binary_f1: 0.573
      paraphrastic_ci: [0.551, 0.595]
      continuation_cv_binary_f1: 0.712
      continuation_ci: [0.692, 0.732]
      paraphrastic_drift_hapax: -0.18
      paraphrastic_drift_ttr: -0.12
      paraphrastic_drift_entropy_mean: -0.09
      paraphrastic_attractor_convergence_depth: 2
      continuation_advantage_pp: 13.9
      bootstrap_delta_p: 0.0
    result_rationale: >
      Paraphrasing chains 有 attractor convergence：depth ≥2 后特征趋于 fixed point，
      depth signal 迅速消失。Drift 幅度极小 (|ρ|<0.20) 因为 paraphrasing 本质上是 semantic-
      preserving transformation，lexical diversity 在几步后就达到 equilibrium。
      Continuation chains 保留更多 depth signal 因为每步引入新内容，distributional shift
      可以持续累积。但在 worst 档下，即使 continuation 的优势也偏弱 (0.712 vs expected
      0.781 in actual)。这个实验在 worst 重构中的价值是：确认 non-paraphrastic chains
      是唯一有 depth signal 的 setting，进一步定义 empirical boundary。
    tables:
      - name: "Table 6: Paraphrastic vs Non-Paraphrastic Depth Signal"
        columns: [Chain Type, Binary F1, hapax ρ, Convergence Depth]
        rows:
          - [Continuation, 0.712, -0.52, ">4"]
          - [Paraphrastic, 0.573, -0.18, "~2"]
          - [Δ, "+13.9pp", "—", "—"]
    figures_description:
      - "Fig 6: Feature trajectory comparison (paraphrastic vs continuation). Paraphrastic 曲线在 depth 2 后 flatten，continuation 持续下降但斜率也在减缓。"
    analysis: >
      Paraphrastic chains 几乎无 depth signal (F1 接近 chance for binary)。
      Continuation 有信号但偏弱。在 worst 重构中，这成为 empirical boundary 的一部分：
      depth estimation 仅在 non-paraphrastic continuation chains 上可行。

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains (每步不同 generator) vs single-model chains。
      更贴近 web contamination 真实场景。
    expected_results:
      cross_model_binary_f1: 0.623
      cross_model_ci: [0.598, 0.648]
      cross_model_3class_f1: 0.594
      single_model_logo_binary_f1: 0.635
      delta_cross_vs_single: -1.2
      heterogeneity_advantage: false
      per_chain_type_f1:
        same_family_cross: 0.651
        cross_family: 0.595
      cross_model_gen1_f1: 0.412
    result_rationale: >
      在 worst 档下，cross-model chains binary F1 ≤ 0.70 (实际 0.623)，heterogeneity
      hypothesis 被否定。原因：不同 generator 的 distributional shift 方向不一致——
      Pythia 和 Qwen 的 entropy_mean drift 方向虽然都是负的，但幅度和 pace 不同。
      当 chain 中混合不同 generator 时，特征轨迹变得 noisy 而非 amplified。
      Cross-family chains 更差 (0.595) 因为 tokenizer 差异引入的 noise 大于 drift signal。
      Same-family cross (e.g., Pythia-1B → Pythia-2.8B) 稍好 (0.651) 但仍不优于
      single-model LOGO。Gen-1 F1 极低 (0.412) 因为 cross-model gen-1 的 distributional
      shift 不可预测——取决于哪两个 model 相邻，模式太多。
    tables:
      - name: "Table 7: Cross-Model vs Single-Model Chains"
        columns: [Setting, Binary F1, 95% CI, gen-1 F1]
        rows:
          - [Single-model LOGO, 0.635, "[0.618, 0.652]", 0.48]
          - [Cross-model (all), 0.623, "[0.598, 0.648]", 0.412]
          - [Cross-model (same family), 0.651, "[0.624, 0.678]", 0.44]
          - [Cross-model (cross family), 0.595, "[0.567, 0.623]", 0.38]
    figures_description:
      - "Fig 7: Feature trajectory comparison for cross-model vs single-model chains。Cross-model 轨迹更 noisy，无 clear monotonic trend。"
    analysis: >
      Heterogeneity hypothesis 被否定。Cross-model chains 无优势，cross-family 更差。
      在 worst 重构中，这是 empirical boundary 的一部分：depth estimation 在
      heterogeneous chain 场景下不可靠，限制了 practical applicability。

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      4 domain seeds (Wikipedia, news, scientific, creative)，500 seeds × 5 depths each。
    expected_results:
      wiki_binary_f1: 0.652
      news_binary_f1: 0.618
      scientific_binary_f1: 0.587
      creative_binary_f1: 0.634
      cross_domain_transfer_f1: 0.571
      domain_gap_max_pp: 6.5
      worst_domain: scientific
      best_domain: wiki
      wiki_vs_scientific_bootstrap_p: 0.003
      scientific_gen1_f1: 0.31
    result_rationale: >
      在 worst 档下，domain 间差异显著。Scientific text 最差 (0.587) 因为学术文本的
      vocabulary diversity 本身就受限（术语密度高，hapax ratio 天然低），depth-induced
      drift 被 domain-specific vocabulary ceiling 压缩。Creative writing 中等 (0.634)
      因为高 lexical diversity 给 drift 留了更多空间。Wiki 最高 (0.652) 因为与 training
      data 最接近。Cross-domain transfer 差 (0.571) 说明 depth signal 的绝对水平高度
      domain-dependent。Scientific 的 gen-1 F1 极低 (0.31) 因为学术文本的 gen-1 和
      gen-2+ 在 surface features 上几乎无差异——术语固定，variation 极小。
    tables:
      - name: "Table 8: Depth Signal by Domain"
        columns: [Domain, Binary F1, 95% CI, gen-1 F1]
        rows:
          - [Wikipedia, 0.652, "[0.628, 0.676]", 0.47]
          - [News, 0.618, "[0.592, 0.644]", 0.42]
          - [Creative, 0.634, "[0.609, 0.659]", 0.45]
          - [Scientific, 0.587, "[0.560, 0.614]", 0.31]
          - [Cross-domain transfer, 0.571, "[0.548, 0.594]", 0.29]
    figures_description:
      - "Fig 8: Domain-stratified binary F1 with CIs。Scientific 显著低于 Wikipedia (non-overlapping CIs)。"
    analysis: >
      Domain dependence 进一步缩窄适用范围。在 worst 重构的 empirical boundary map 中，
      scientific text 标记为 "weak signal" 区域。

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4)。测试 3-class 以上的分辨率。
    expected_results:
      five_class_macro_f1: 0.382
      five_class_ci: [0.365, 0.399]
      three_class_macro_f1: 0.718
      ordinal_coral_f1: 0.378
      ordinal_frank_hall_f1: 0.385
      confusion_matrix_note: "gen-2/gen-3/gen-4 几乎完全混淆 (mutual confusion rate >60%)"
      gen2_f1: 0.28
      gen3_f1: 0.19
      gen4_f1: 0.14
      gen0_f1: 0.91
      gen1_f1: 0.39
      mae: 0.82
    result_rationale: >
      在 worst 档下，5-class F1 极低 (~0.38)。原因：depth signal 在 gen-2 后快速 saturate——
      features 在 gen-2 和 gen-4 之间的差异远小于 gen-0 和 gen-2 之间。这是 recursive
      generation 的数学性质：每步 drift 的 marginal increment 递减（如同 Markov chain
      mixing）。Ordinal 方法 (CORAL, Frank-Hall) 无改善，因为问题不在 loss function 而在
      feature space 的本征分辨率限制。gen-0 仍高 (0.91) 因为有 seed sharing 效应。
      gen-3 和 gen-4 的 F1 极低 (0.19, 0.14)——这些 depth 之间的 distributional 差异
      已在 noise floor 以下。在 worst 重构中，这确认 3-class 是 practical ceiling，
      支持 "empirical boundary" 叙事。
    tables:
      - name: "Table 9: 5-Class Ordinal Results"
        columns: [Method, 5-Class F1, MAE, gen-2 F1, gen-3 F1, gen-4 F1]
        rows:
          - [XGBoost (nominal), 0.382, 0.82, 0.28, 0.19, 0.14]
          - [CORAL (ordinal), 0.378, 0.80, 0.27, 0.18, 0.15]
          - [Frank-Hall, 0.385, 0.81, 0.29, 0.20, 0.13]
    figures_description:
      - "Fig 9: 5×5 confusion matrix heatmap。清晰展示 gen-2/3/4 的大面积 off-diagonal concentration。"
    analysis: >
      5-class resolution 完全不可行。3-class 是硬性上限。在 worst 重构中，
      这是 task formulation 贡献的一部分——定义了 depth resolution 的 empirical ceiling。

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Simulated human edits robustness test：(A) Random word replacement (5/10/20%)；
      (B) LLM-simulated editing (light rephrasing)。
    expected_results:
      baseline_binary_f1: 0.635
      random_5pct_f1: 0.578
      random_10pct_f1: 0.531
      random_20pct_f1: 0.488
      llm_rephrase_f1: 0.553
      llm_rephrase_drop_pp: 8.2
      random_5pct_drop_pp: 5.7
      random_10pct_drop_pp: 10.4
      random_20pct_drop_pp: 14.7
      edit_distance_ratio: 0.51
      avg_sentences_replaced: 1.7
    result_rationale: >
      在 worst 档下，robustness 差。Baseline 已经偏低 (0.635)，任何 perturbation 都将
      F1 推向 near-chance。5% random replacement 就造成 5.7pp 下降，因为 surface features
      (TTR, hapax) 对 word-level perturbation 极敏感——替换新词直接影响 vocabulary diversity
      metrics。LLM rephrase 更温和但仍造成 8.2pp 下降 (在 worst 指标范围 [6.0, 12.0] 内)，
      因为 rephrasing 引入的 lexical variation 部分覆盖了 depth-induced drift。
      20% replacement 后 F1 低于 0.50，实质上等于 random guess for binary。
      这在 worst 重构中是 empirical boundary 的重要部分：depth signal 不 robust to
      post-generation editing。
    tables:
      - name: "Table 10: Robustness to Simulated Edits"
        columns: [Edit Type, Binary F1, Δ vs Baseline (pp)]
        rows:
          - [No edit (baseline), 0.635, "—"]
          - [Random 5%, 0.578, -5.7]
          - [Random 10%, 0.531, -10.4]
          - [Random 20%, 0.488, -14.7]
          - [LLM rephrase, 0.553, -8.2]
    figures_description:
      - "Fig 10: F1 degradation curve as function of edit intensity。Near-linear decline，在 ~15% edit 处 cross chance level。"
    analysis: >
      Depth signal fragile to editing。在 worst 重构中，这是 "depth signal disappears"
      条件空间的重要条目：任何 post-generation editing 都严重削弱信号。

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      添加 LD-Score (character-distribution signature) 作为额外特征。
      测试 character-level features 是否提供互补 depth signal。
    expected_results:
      seven_feat_f1: 0.635
      eight_feat_with_ld_f1: 0.641
      ld_only_f1: 0.594
      delta_pp: 0.6
      ld_score_spearman_depth: -0.31
      ld_score_correlation_with_hapax: 0.72
      ld_score_correlation_with_ttr: 0.68
      feature_importance_ld: 0.034
      bootstrap_8_vs_7_p: 0.28
    result_rationale: >
      在 worst 档下，LD-Score 添加仅带来 0.6pp 的微弱提升 (bootstrap p=0.28, 不显著)。
      原因：LD-Score 捕获的 character-level distribution 与 surface features (TTR, hapax)
      高度相关 (r=0.72 with hapax)——character diversity 和 word diversity 是同一信号的
      不同 granularity。LD-Score 单独只有 0.594，弱于 surface-only 但非 trivial。
      Feature importance 极低 (0.034) 因为被 hapax_ratio 和 ttr 冗余化。在 worst
      重构中，这确认 depth signal 的本质是 vocabulary/diversity impoverishment，
      character-level 和 word-level 度量捕获相同的底层现象。
    tables:
      - name: "Table 11: LD-Score Feature Addition"
        columns: [Feature Set, Binary F1, Δ pp, bootstrap p]
        rows:
          - [7-feature, 0.635, "ref", "—"]
          - [7-feature + LD-Score, 0.641, +0.6, 0.28]
          - [LD-Score only, 0.594, -4.1, "—"]
    figures_description:
      - "Fig 11: Feature correlation heatmap including LD-Score。LD-Score 与 hapax/ttr cluster 在一起。"
    analysis: >
      LD-Score 贡献 negligible，被 surface features 冗余化。
      在 worst 重构中，支持 "vocabulary impoverishment is the single underlying signal" 的叙事。

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned Qwen3.5-0.8B (实际可能使用 Qwen3-0.6B) 端到端 depth classification。
      对比 handcrafted distributional features。
    expected_results:
      qlora_3class_f1: 0.752
      qlora_3class_ci: [0.738, 0.766]
      qlora_binary_f1: 0.673
      qlora_binary_ci: [0.655, 0.691]
      seven_feature_3class_f1: 0.718
      seven_feature_binary_f1: 0.635
      qlora_advantage_3class_pp: 3.4
      qlora_advantage_binary_pp: 3.8
      qlora_logo_binary_f1: 0.584
      qlora_logo_3class_f1: 0.631
      qlora_logo_vs_7feat_logo: -5.1
      inference_time_ratio: 8.2
      gpu_memory_gb: 4.8
    result_rationale: >
      在 worst 档下，QLoRA within-generator 表现优于 7-feature (3class +3.4pp, binary +3.8pp)，
      因为 learned representations 可以捕获更丰富的模式。但 LOGO 泛化更差 (0.584 vs 0.635)——
      end-to-end model overfits to generator-specific patterns。这是因为不同 generator 的
      "depth signature" 在 representation space 中差异大，model 学到的是 generator-specific
      depth pattern 而非 universal depth signal。Inference cost 8.2× 高于 XGBoost +
      Pythia-410M forward pass。在 worst 重构中，这是重要发现：(1) handcrafted features
      在跨 generator 泛化上优于 end-to-end，(2) 但两者都偏弱，(3) depth signal 本身
      就不 robust enough 支撑任何 strong method claim。
    tables:
      - name: "Table 12: End-to-End vs Handcrafted Features"
        columns: [Method, Within-gen Binary F1, LOGO Binary F1, Inference Cost]
        rows:
          - [7-feature XGBoost, 0.635, 0.635, "1× (410M fwd + XGB)"]
          - [QLoRA Qwen3-0.6B, 0.673, 0.584, "8.2×"]
    figures_description:
      - "Fig 12: Within-gen vs LOGO F1 comparison bar chart。展示 end-to-end 的 generalization gap 比 handcrafted features 更大。"
    analysis: >
      End-to-end 不能 rescue depth classification。Within-gen 优势在 LOGO 下消失。
      在 worst 重构中，这支持 "7-feature 的价值在 interpretability + generalization，
      不在 accuracy" 的定位。

  - name: text_length_control
    plan_id: plan_013
    description: >
      Text length confound control：(A) length-by-depth 分析；(B) length-normalized features；
      (C) length-matched classifier。
    expected_results:
      spearman_length_depth: -0.18
      length_depth_correlation: "moderate (higher than expected)"
      length_matched_binary_f1: 0.581
      unmatched_binary_f1: 0.635
      length_matched_delta_pp: -5.4
      normalized_ttr_trend_preserved: true
      normalized_hapax_trend_preserved: true
      normalized_ttr_rho: -0.32
      normalized_hapax_rho: -0.38
      raw_ttr_rho: -0.44
      raw_hapax_rho: -0.46
      rho_drop_ttr: 0.12
      rho_drop_hapax: 0.08
    result_rationale: >
      在 worst 档下，length confound 比预期更严重。Length-depth correlation ρ=-0.18
      (moderate)——deeper text 倾向更短 (generation 在 depth 增加时更快触发 EOS 或
      max_length truncation)。Length-matched F1 下降 5.4pp (0.635→0.581)，说明
      original F1 中有 ~5pp 归因于 length confound。Normalized features 保留 trend
      但 magnitude 衰减：TTR ρ 从 -0.44 降至 -0.32 (27% 衰减)，说明 raw TTR 部分
      tracking length 而非 depth。但 trend 方向不变，意味着 length 不是 sole driver，
      只是 amplifier。在 worst 档下 5.4pp 的下降更痛——从已经偏低的 0.635 降至 0.581，
      进入 near-chance territory。
    tables:
      - name: "Table 13: Length Confound Analysis"
        columns: [Condition, Binary F1, Δ pp, hapax ρ, ttr ρ]
        rows:
          - [Unmatched, 0.635, "ref", -0.46, -0.44]
          - [Length-matched, 0.581, -5.4, -0.38, -0.32]
          - [Length-normalized features, 0.598, -3.7, -0.38, -0.32]
    figures_description:
      - "Fig 13: Length distribution by depth (violin plot)。Deeper generations 的 length distribution 左移。"
    analysis: >
      Length confound 实质性存在但非 sole driver。在 worst 重构中诚实报告：
      observed depth signal 中 ~30-40% 可归因于 length variation。
      Length-controlled performance (0.581) 代表 "true" depth signal 的更保守估计。

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      添加一个 7B+ generator (Qwen3-8B-Base)。测试 depth signal 在 frontier scale 是否持续。
    expected_results:
      qwen3_8b_records: 4400
      qwen3_8b_logo_binary_f1: 0.538
      qwen3_8b_logo_3class_f1: 0.612
      qwen3_8b_within_binary_f1: 0.587
      logo_with_8b_avg_binary_f1: 0.621
      logo_without_8b_avg_binary_f1: 0.635
      delta_including_8b: -1.4
      ddr_8b_rho:
        entropy_mean: -0.29
        ttr: -0.34
        hapax_ratio: -0.36
        entropy_std: -0.11
        entropy_max: 0.06
        tail_decay: -0.04
        entropy_min: -0.14
      ddr_drifting_rho_abs_min: 0.29
      ddr_rho_gap_drifting_vs_stationary: 0.25
      scale_effect_delta_vs_small: -9.7
    result_rationale: >
      在 worst 档下，8B generator 展示严重的 scale degradation。Binary F1 仅 0.538
      (在 worst 指标范围 [0.48, 0.58] 内)。原因：larger models 的 generation quality
      更高，depth 间的 distributional shift 更小——8B model 在每步 generation 中
      更好地 "preserve" 了 input distribution 的 properties，导致 drift features
      的 |ρ| 明显衰减 (entropy_mean -0.29 vs ≤2.8B models ~0.48)。DDR ρ gap
      (drifting vs stationary) 压缩至 0.25，远低于 small models 的 ~0.40。
      这是 worst 叙事中的关键证据：depth signal 是 small model artifact，
      随 scale 消失。Practical implication：如果 web contamination 主要来自
      frontier models (7B+)，depth estimation 不可行。
    tables:
      - name: "Table 14: Scale Effect on Depth Signal"
        columns: [Generator, Size, LOGO Binary F1, entropy_mean ρ, DDR gap]
        rows:
          - [Qwen3-0.6B, 0.6B, 0.562, -0.38, 0.28]
          - [Pythia-1B, 1B, 0.708, -0.52, 0.42]
          - [OLMo-2-1B, 1.5B, 0.614, -0.41, 0.31]
          - [Qwen3-1.7B, 1.7B, 0.588, -0.36, 0.26]
          - [Pythia-2.8B, 2.8B, 0.672, -0.48, 0.38]
          - ["**Qwen3-8B**", "**8B**", "**0.538**", "**-0.29**", "**0.25**"]
    figures_description:
      - "Fig 14: Binary F1 vs model scale scatter plot。展示 negative trend，8B 点明显在趋势线下方。"
    analysis: >
      Scale effect 是 worst 档最致命的发现。Depth signal 随 model scale 单调衰减，
      在 8B 时已接近不可用。在 worst 重构中，这定义了 empirical boundary 的最重要维度：
      depth estimation 仅在 small base models (≤3B) 上有实际意义。

  - name: ordinal_baseline_comparison
    plan_id: plan_015
    description: >
      测试 existing detector scores (FastDetectGPT, Binoculars, LD-Score, avg_logprob)
      是否已有 ordinal depth signal。单特征 vs 7-feature 对比。
    expected_results:
      seven_feature_logo_binary_f1: 0.635
      seven_feature_ci: [0.618, 0.652]
      avg_logprob_logo_binary_f1: 0.622
      avg_logprob_ci: [0.597, 0.647]
      ld_score_logo_binary_f1: 0.591
      ld_score_ci: [0.565, 0.617]
      fastdetectgpt_logo_binary_f1: 0.548
      fastdetectgpt_ci: [0.521, 0.575]
      binoculars_logo_binary_f1: 0.512
      binoculars_ci: [0.484, 0.540]
      seven_feat_minus_avglogprob_pp: 1.3
      bootstrap_delta_7feat_vs_avglogprob_p: 0.08
      bootstrap_delta_7feat_vs_avglogprob_significant: false
      avg_logprob_spearman: -0.41
      ld_score_spearman: -0.35
    result_rationale: >
      在 worst 档下，7-feature vs avg_logprob 差距仅 1.3pp (在 worst 范围 [0.0, 1.5] 内)，
      且 bootstrap p=0.08 不显著。这是 worst 档的核心打击：自定义 7-feature 相对于
      最简单的 single-feature baseline (avg_logprob) 无统计显著优势。avg_logprob 之所以
      competitive 是因为它直接度量了 model perplexity，而 depth-induced drift 本质上就是
      perplexity compression——deeper text 对 reference model 更 "predictable"。
      7-feature 增加的 surface features (TTR, hapax) 在 LOGO evaluation 下的 marginal
      value 被 cross-generator variance 淹没。LD-Score 和 FastDetectGPT 弱于 avg_logprob
      因为它们的设计目标是 binary detection 而非 ordinal depth。Binoculars 最弱因为
      需要两个 model 且对 depth 信号不敏感。在 worst 重构中，这迫使承认
      "avg_logprob 是 competitive baseline，7-feature 的价值在 interpretability
      (可解释哪些 distributional 方面在漂移) 而非 accuracy"。
    tables:
      - name: "Table 15: Ordinal Baseline Comparison (LOGO Binary F1)"
        columns: [Method, LOGO Binary F1, 95% CI, vs 7-feat Δpp, bootstrap p]
        rows:
          - [7-feature ensemble, 0.635, "[0.618, 0.652]", "ref", "—"]
          - [avg_logprob (single), 0.622, "[0.597, 0.647]", -1.3, "0.08 (ns)"]
          - [LD-Score (single), 0.591, "[0.565, 0.617]", -4.4, 0.002]
          - [FastDetectGPT (single), 0.548, "[0.521, 0.575]", -8.7, "<0.001"]
          - [Binoculars (single), 0.512, "[0.484, 0.540]", -12.3, "<0.001"]
    figures_description:
      - "Fig 15: Paired bootstrap ΔF1 distribution: 7-feature vs avg_logprob。分布大部分 >0 但 CI 包含 0，不显著。"
    analysis: >
      7-feature 无统计显著优势于 avg_logprob。这是 worst 档的 defining result。
      在重构叙事中，7-feature 重新定位为 "interpretable alternative to avg_logprob,
      offering comparable accuracy with the added benefit of DDR decomposition for
      understanding which distributional aspects drift with depth." 但 DDR 本身
      也在瓦解，所以最终定位是：avg_logprob 是 strong baseline，自定义特征的价值
      在于提供 empirical boundary map 的分析工具，而非更好的分类器。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd1a1703-a67d-42a2-940c-260fb00030f8",
  "isSidechain": false,
  "requestId": "req_011CbEiJaywRD1ZpFdJBnLyL",
  "type": "assistant",
  "uuid": "12a79867-0a04-4705-aec1-133ddbcabf11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131BcQxEp1PxFLF78z5Hnz7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 307,
      "cache_read_input_tokens": 36722,
      "output_tokens": 15869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15869,
          "cache_read_input_tokens": 36722,
          "cache_creation_input_tokens": 307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 307
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。 核心假设：[\"DDR 二分法在 ≥9 generators 下瓦解：≥3 个 'stationary' 特征出现显著 drift (|ρ|>0.15)，或 drifti…",
  "leafUuid": "12a79867-0a04-4705-aec1-133ddbcabf11",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation empirical boundaries and task formulation",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DDR 框架不成立为通用现象；7-feature 集相对单特征 baseline 无统计显著优势；需彻底重构论文角度但不降级 venue。 核心假设：[\"DDR 二分法在 ≥9 generators 下瓦解：≥3 个 'stationary' 特征出现显著 drift (|ρ|>0.15)，或 drifti…",
  "leafUuid": "12a79867-0a04-4705-aec1-133ddbcabf11",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation empirical boundaries and task formulation",
  "sessionId": "da744110-76ce-4c79-a256-c6f62d091013"
}
```

---
