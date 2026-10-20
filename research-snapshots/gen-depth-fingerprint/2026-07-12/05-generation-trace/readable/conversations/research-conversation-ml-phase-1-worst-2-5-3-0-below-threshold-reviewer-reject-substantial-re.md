# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：2.5-3.0 Below Threshold — 核心假设被挑战，至少一个 reviewer 给出 reject，需要 substantial re

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-3/8c952852-52ac-4fcb-8bac-8129aa8ac532.jsonl`
- **Structured JSON:** [`cf054d5451c3d0c5d92b.json`](../../sessions/cf/cf054d5451c3d0c5d92b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T10:21:24.247Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T10:21:24.247Z",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：2.5-3.0 Below Threshold — 核心假设被挑战，至少一个 reviewer 给出 reject，需要 substantial reframing 但仍冲 EMNLP Findings（不降级到 workshop）\n核心假设：[\"DDR 被认为是 vocabulary impoverishment 的 repackaging — 审稿人认为 surface-only F1=0.688 vs full 0.773 的差距不够大，reference features 只是 'another way to measure the same signal'\", 'Base-model-only + temperature-sensitive + instruct 退化被综合视为 fatal scope limitation — 审稿人认为现实数据几乎全来自 instruct models', '0.694 F1 被认为 insufficient for practical use — 审稿人对比 binary detection baselines (FastDetectGPT 等 >0.95 F1) 认为 depth classification 太难而回报太低', \"Task formulation novelty 被质疑：审稿人认为 depth classification 缺乏明确下游应用（Claim 3 的 negative finding 被 weaponize 为 'why does this matter'）\", 'Paper 过长（33 页）被批评为 unfocused — 审稿人认为实验多但缺乏 coherent story']\n关键指标范围：{'expected_reviewer_avg': [2.5, 3.0], 'reviewer_spread': [2, 3.5], 'logo_binary_f1_perception': \"0.694 被与 binary detection (>0.95) 不公平对比，被标记为 'not actionable'\", 'surface_vs_full_gap': \"0.085 差距被认为 marginal（surface alone 'nearly as good'）\", 'instruct_scope_penalty': '-1.0 pp on 1-2 reviewers — 被视为 deal-breaker', 'task_utility_challenge': 'negative Claim 3 被反转为 anti-evidence'}\n叙事方向：需要 fundamental reframing，但不降级目标（仍投 EMNLP Findings，走 ICLR 2027 fallback 如果 reject）。两个可能的 reframe 方向：(A) 从 'depth classification as a tool' 转向 'empirical study of recursive generation dynamics' — 把 DDR 本身作为 contribution 而非分类器，强调对 model collapse 理论的 empirical grounding（连接 Shumailov et al. 的 model collapse 文献），弱化分类器性能指标，强化 phenomenon characterization。(B) 从 'standalone method' 转向 'complementary signal for existing detectors' — 展示 7-feature + existing detectors 的 ensemble 提升（已有 multi-detector 数据：4-det+surface 3-class 0.795），reposition 为 'depth features as additional signal dimension'。两个方向均利用已有实验数据，不需要新实验。5 天内可完成 narrative 重写 + 补充 1-2 个支撑实验。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nfocus: Paper has been significantly expanded since last dream (May 14). New additions: (1) 9-generator scale evaluation with Gemma-2-2B (Appendix), (2) DDR causality analysis with permutation importance + Granger causality + feature intervention, (3) TOST bootstrap stability validation, (4) cross-model evaluation upgraded from sample-level CV to generator-level LOGO (binary F1=0.830). Total 33 pages, 20+ appendix experiments. Assess whether this is 3.0 Findings or 3.5 Borderline Conference level. Identify the single highest-impact improvement that could be made in 5 days before DDL.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_logo_f1: 0.7879\n    overall_ci95:\n    - 0.783\n    - 0.7929\n    spearman_entropy_max: 0.0503\n    spearman_entropy_min: -0.4061\n    spearman_hapax: -0.6467\n    spearman_ttr: -0.6302\n    spearman_entropy_mean: -0.6098\n    spearman_entropy_std: -0.1996\n    spearman_tail_decay: -0.0403\n- exp_id: plan-010-robustness\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_binary_f1: 0.695\n    5pct_binary_f1: 0.65\n    10pct_binary_f1: 0.614\n    20pct_binary_f1: 0.591\n    5pct_drop: -0.046\n    10pct_drop: -0.081\n    20pct_drop: -0.104\n- exp_id: plan-010-llm-rephrase\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_binary_f1: 0.6918\n    original_binary_ci:\n    - 0.6749\n    - 0.7067\n    original_multiclass_f1: 0.7385\n    original_multiclass_ci:\n    - 0.7269\n    - 0.7496\n    rephrased_binary_f1: 0.6471\n    rephrased_binary_ci:\n    - 0.6308\n    - 0.6619\n    rephrased_multiclass_f1: 0.6672\n    rephrased_multiclass_ci:\n    - 0.6548\n    - 0.6796\n    binary_drop: -0.0447\n    multiclass_drop: -0.0713\n    edit_distance_ratio: 0.5071\n    avg_sentences_replaced: 1.69\n    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\n    bugs_fixed:\n    - binary_task_gen1_vs_gen2+\n    - 3class_mapping\n    - tail_decay_rank100-1000\n- exp_id: plan-008-seed-stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_complexity_binary: 0.685\n    medium_binary: 0.695\n    high_complexity_binary: 0.695\n    low_complexity_multi: 0.772\n    medium_multi: 0.778\n    high_complexity_multi: 0.779\n    max_diff_binary_pp: 1.06\n    max_diff_multiclass_pp: 0.68\n    conclusion_label: seed_independent\n- exp_id: multi-domain-seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7459\n    news_binary_ci:\n    - 0.726\n    - 0.764\n    news_multiclass_f1: 0.6516\n    academic_binary_f1: 0.7386\n    academic_binary_ci:\n    - 0.72\n    - 0.757\n    academic_multiclass_f1: 0.6223\n    code_binary_f1: 0.7535\n    code_binary_ci:\n    - 0.737\n    - 0.77\n    code_multiclass_f1: 0.6344\n    wikipedia_baseline_binary_f1: 0.8148\n    wikipedia_baseline_multiclass_f1: 0.8632\n    max_gap_vs_wiki_pp: 7.62\n    worst_domain: academic\n    best_domain: code\n    conclusion_label: domain_independent\n- exp_id: exp_047_multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7119\n    news_binary_ci:\n    - 0.6898\n    - 0.7332\n    news_3class_f1: 0.7149\n    academic_binary_f1: 0.6279\n    academic_binary_ci:\n    - 0.6027\n    - 0.6515\n    academic_3class_f1: 0.6564\n    code_binary_f1: 0.6872\n    code_binary_ci:\n    - 0.6641\n    - 0.71\n    code_3class_f1: 0.6729\n    overall_binary_f1: 0.6757\n    overall_3class_f1: 0.6814\n    delta_vs_t10_news: -0.034\n    delta_vs_t10_academic: -0.1107\n    delta_vs_t10_code: -0.0663\n- exp_id: multi_domain_t07\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_048_cross_temp_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    6gen_logo:\n      within_0.7_binary: 0.9471\n      within_0.7_3class: 0.7888\n      cross_0.7to1.0_binary: 0.9001\n      cross_0.7to1.0_3class: 0.7225\n      within_1.0_binary: 0.9107\n      within_1.0_3class: 0.7257\n      cross_1.0to0.7_binary: 0.9581\n      cross_1.0to0.7_3class: 0.7913\n      caveat: Only Qwen3-1.7B differs between conditions; 5/6 generators share data\n    qwen_only:\n      within_0.7_binary: 0.9262\n      within_0.7_binary_ci:\n      - 0.916\n      - 0.935\n      within_0.7_3class: 0.769\n      within_0.7_3class_ci:\n      - 0.756\n      - 0.781\n      cross_0.7to1.0_binary: 0.7574\n      cross_0.7to1.0_binary_ci:\n      - 0.745\n      - 0.77\n      cross_0.7to1.0_3class: 0.4581\n      cross_0.7to1.0_3class_ci:\n      - 0.445\n      - 0.472\n      within_1.0_binary: 0.8248\n      within_1.0_binary_ci:\n      - 0.81\n      - 0.838\n      within_1.0_3class: 0.5738\n      within_1.0_3class_ci:\n      - 0.56\n      - 0.588\n      cross_1.0to0.7_binary: 0.9443\n      cross_1.0to0.7_binary_ci:\n      - 0.936\n      - 0.953\n      cross_1.0to0.7_3class: 0.6014\n      cross_1.0to0.7_3class_ci:\n      - 0.593\n      - 0.611\n      delta_0.7train_binary_pp: -16.9\n      delta_0.7train_3class_pp: -31.1\n      delta_1.0train_binary_pp: 12\n      delta_1.0train_3class_pp: 2.8\n      asymmetric_transfer: true\n- exp_id: exp_049_temp_curve_t05\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 4708\n    skipped: 113\n    seeds: 995\n    model: pythia-2.8b\n    temperature: 0.5\n    top_p: 0.9\n    within_cv_binary_f1: 0.8432\n    within_cv_binary_ci:\n    - 0.8301\n    - 0.8558\n    logo_binary_f1: 0.8136\n    logo_binary_ci:\n    - 0.7984\n    - 0.8282\n    entropy_mean_rho: -0.5844\n- exp_id: exp_050_temp_curve_t09\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    records: 4536\n    model: pythia-2.8b\n    temperature: 0.9\n    top_p: 0.9\n    within_cv_binary_f1: 0.5821\n    within_cv_binary_ci:\n    - 0.5655\n    - 0.5985\n    logo_binary_f1: 0.4804\n    logo_binary_ci:\n    - 0.4645\n    - 0.4976\n    entropy_mean_rho: -0.3016\n    delta_vs_t07_cv: -0.157\n    delta_vs_t07_logo: -0.259\n- exp_id: exp_051_independent_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_to_olmo_binary_f1: 0.6945\n    pythia_to_olmo_ci:\n    - 0.6727\n    - 0.7167\n    olmo_to_pythia_binary_f1: 0.666\n    olmo_to_pythia_ci:\n    - 0.6429\n    - 0.6893\n    avg_binary_f1: 0.6803\n    shared_seed_logo_ref: 0.694\n    delta_vs_shared: -0.014\n- exp_id: exp_052_instruct_qwen3_1_7b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8753\n    within_binary_ci:\n    - 0.8667\n    - 0.8837\n    within_3class_f1: 0.7324\n    within_3class_ci:\n    - 0.7195\n    - 0.745\n    base_binary_f1: 0.8614\n    base_3class_f1: 0.769\n    logo_instruct_binary: 0.658\n    logo_instruct_3class: 0.543\n    logo_base_binary: 0.821\n    logo_base_3class: 0.802\n    gen1_f1_instruct: 0.438\n    gen1_f1_base: 0.579\n    spearman_direction: reversed (instruct ρ>0, base ρ<0)\n    delta_within_binary: 0.014\n    delta_within_3class: -0.037\n    delta_logo_binary: -0.163\n- exp_id: exp_053_instruct_olmo2_1b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8131\n    within_binary_ci:\n    - 0.8012\n    - 0.8251\n    within_3class_f1: 0.5748\n    within_3class_ci:\n    - 0.5605\n    - 0.5897\n    base_binary_f1: 0.8454\n    base_3class_f1: 0.7538\n    gen1_f1_instruct: 0.256\n    gen1_f1_base: 0.523\n    delta_within_binary: -0.032\n    delta_within_3class: -0.179\n    spearman_instruct:\n      entropy_mean: 0.482\n      entropy_std: 0.296\n      entropy_min: 0.08\n      entropy_max: 0.306\n      tail_decay: 0.228\n      ttr: 0.006\n      hapax_ratio: 0.025\n    spearman_base:\n      entropy_mean: -0.639\n      entropy_std: -0.296\n      entropy_min: -0.387\n      entropy_max: 0.067\n      tail_decay: -0.141\n      ttr: -0.7\n      hapax_ratio: -0.712\n    features_reversed: 6/7\n    model_used: allenai/OLMo-2-0425-1B-Instruct\n- exp_id: exp_054_instruct_llama3_2_3b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    instruct_binary_f1: 0.8381\n    instruct_binary_ci:\n    - 0.828\n    - 0.847\n    instruct_3class_f1: 0.5437\n    instruct_3class_ci:\n    - 0.53\n    - 0.558\n    base_binary_f1: 0.8488\n    base_3class_f1: 0.7424\n    rho_instruct_entropy_mean: 0.2299\n    rho_instruct_entropy_std: 0.2623\n    rho_instruct_entropy_min: -0.0027\n    rho_instruct_entropy_max: 0.2036\n    rho_instruct_tail_decay: 0.1198\n    rho_instruct_ttr: -0.1411\n    rho_instruct_hapax_ratio: -0.1157\n    rho_base_entropy_mean: -0.627\n    rho_base_ttr: -0.6856\n    rho_base_hapax_ratio: -0.6975\n    direction_reversals: 3\n    reversed_features:\n    - entropy_mean\n    - entropy_std\n    - tail_decay\n    data_count: 4974\n- exp_id: exp_055_qlora_olmo_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8881\n    macro_f1_3class_std: 0.0071\n    macro_f1_5class: 0.5976\n    macro_f1_5class_std: 0.0046\n    binary_f1: 0.8363\n    binary_f1_std: 0.0096\n    n_samples: 4429\n    runtime_seconds: 1689.7\n- exp_id: exp_056_qlora_qwen_instruct\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.9066\n    macro_f1_3class_std: 0.0082\n    macro_f1_5class: 0.5514\n    macro_f1_5class_std: 0.0031\n    binary_f1: 0.8672\n    binary_f1_std: 0.0137\n    n_samples: 4963\n    runtime_seconds: 1880.5\n- exp_id: exp_055b_qlora_olmo_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8588\n    macro_f1_3class_std: 0.0036\n    macro_f1_5class: 0.5398\n    macro_f1_5class_std: 0.015\n    binary_f1: 0.7925\n    binary_f1_std: 0.0097\n    n_samples: 2379\n    runtime_seconds: 911.7\n    note: completed before kill signal\n- exp_id: exp_056b_qlora_qwen_base\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.904\n    macro_f1_3class_std: 0.0094\n    macro_f1_5class: 0.5544\n    macro_f1_5class_std: 0.0068\n    binary_f1: 0.8597\n    binary_f1_std: 0.0123\n    n_samples: 2291\n    runtime_seconds: 880.9\n    note: completed before kill signal\n- exp_id: exp_057_scale_9gen_logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: superseded by exp_057 (rerun with fixed Gemma data)\n    first_run_3class_f1: 0.7516\n    first_run_binary_f1: 0.6842\n    see_exp_057_for_final: true\n- exp_id: exp_058_ddr_causality\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    permutation_baseline_f1: 0.7714\n    drifting_avg_importance: 0.1578\n    stationary_avg_importance: 0.0297\n    drifting_stationary_ratio: 5.31\n    granger_significant_features: 6/7\n    granger_max_delta_r2: 0.031\n    granger_max_delta_r2_feature: entropy_std\n    granger_nonsig_feature: entropy_min\n    granger_panel_n: 29095\n    intervention_max_f1_drop: 0.0203\n    intervention_max_feature: entropy_max\n    intervention_min_f1_drop: 0.0061\n- exp_id: exp_059_tost_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_bootstrap: 1000\n    seed: 42\n    margin_d: 0.2\n    entropy_max:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.062\n      d_ci:\n      - 0.037\n      - 0.088\n    entropy_min:\n      median_p: 0\n      rejection_rate: 1\n      median_d: -0.016\n      d_ci:\n      - -0.042\n      - 0.011\n    tail_decay:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.088\n      d_ci:\n      - 0.065\n      - 0.111\n    entropy_std:\n      median_p: 1\n      rejection_rate: 0\n      median_d: 0.458\n      d_ci:\n      - 0.435\n      - 0.479\n    stationary_features_robust: true\n- exp_id: exp_057\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    9gen_logo_3class_f1: 0.751\n    9gen_logo_binary_f1: 0.6661\n    8gen_baseline_3class_f1: 0.7698\n    delta_9gen_vs_8gen: -0.0188\n    n_total_rows: 42015\n    n_generators: 9\n    qwen3_8b_3class_f1: 0.6955\n    qwen3_8b_binary_f1: 0.6468\n    gemma_2_2b_3class_f1: 0.6279\n    gemma_2_2b_binary_f1: 0.4402\n    per_gen_3class_f1:\n      pythia-1b: 0.8571\n      qwen3-0.6b: 0.8185\n      pythia-2.8b: 0.8117\n      qwen3-1.7b: 0.8114\n      olmo-2-1b: 0.7732\n      llama-3.2-3b: 0.7591\n      qwen3-8b: 0.6955\n      gemma-2-2b: 0.6279\n      mistral-7b-v0.3: 0.6045\n    tail_decay_consistency: VERIFIED_all_9gen_logprob_slope\n    data_source: features_9gen.csv (42015 rows, Gemma fixed)\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T10:21:24.250Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T10:21:24.250Z",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-20T10:21:24.268Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：2.5-3.0 Below Threshold — 核心假设被挑战，至少一个 reviewer 给出 reject，需要 substantial reframing 但仍冲 EMNLP Findings（不降级到 workshop）
核心假设：["DDR 被认为是 vocabulary impoverishment 的 repackaging — 审稿人认为 surface-only F1=0.688 vs full 0.773 的差距不够大，reference features 只是 'another way to measure the same signal'", 'Base-model-only + temperature-sensitive + instruct 退化被综合视为 fatal scope limitation — 审稿人认为现实数据几乎全来自 instruct models', '0.694 F1 被认为 insufficient for practical use — 审稿人对比 binary detection baselines (FastDetectGPT 等 >0.95 F1) 认为 depth classification 太难而回报太低', "Task formulation novelty 被质疑：审稿人认为 depth classification 缺乏明确下游应用（Claim 3 的 negative finding 被 weaponize 为 'why does this matter'）", 'Paper 过长（33 页）被批评为 unfocused — 审稿人认为实验多但缺乏 coherent story']
关键指标范围：{'expected_reviewer_avg': [2.5, 3.0], 'reviewer_spread': [2, 3.5], 'logo_binary_f1_perception': "0.694 被与 binary detection (>0.95) 不公平对比，被标记为 'not actionable'", 'surface_vs_full_gap': "0.085 差距被认为 marginal（surface alone 'nearly as good'）", 'instruct_scope_penalty': '-1.0 pp on 1-2 reviewers — 被视为 deal-breaker', 'task_utility_challenge': 'negative Claim 3 被反转为 anti-evidence'}
叙事方向：需要 fundamental reframing，但不降级目标（仍投 EMNLP Findings，走 ICLR 2027 fallback 如果 reject）。两个可能的 reframe 方向：(A) 从 'depth classification as a tool' 转向 'empirical study of recursive generation dynamics' — 把 DDR 本身作为 contribution 而非分类器，强调对 model collapse 理论的 empirical grounding（连接 Shumailov et al. 的 model collapse 文献），弱化分类器性能指标，强化 phenomenon characterization。(B) 从 'standalone method' 转向 'complementary signal for existing detectors' — 展示 7-feature + existing detectors 的 ensemble 提升（已有 multi-detector 数据：4-det+surface 3-class 0.795），reposition 为 'depth features as additional signal dimension'。两个方向均利用已有实验数据，不需要新实验。5 天内可完成 narrative 重写 + 补充 1-2 个支撑实验。

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
  "promptId": "cf777c8a-2c8c-4b56-bb20-59f28877ca5c",
  "type": "user",
  "uuid": "786b2203-df84-48c6-bb50-1a944f6d5678",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T10:21:24.266Z_

```json
{
  "parentUuid": "786b2203-df84-48c6-bb50-1a944f6d5678",
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
  "uuid": "3a20afb5-3107-417b-9127-d6e3732df7df",
  "timestamp": "2026-05-20T10:21:24.266Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T10:21:24.267Z_

```json
{
  "parentUuid": "3a20afb5-3107-417b-9127-d6e3732df7df",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bdfacc34-2aa9-4479-a92c-1a4132e77c45",
  "timestamp": "2026-05-20T10:21:24.267Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：2.5-3.0 Below Threshold — 核心假设被挑战，至少一个 reviewer 给出 reject，需要 substantial reframing 但仍冲 EMNLP Findings（不降级到 workshop） 核心假设：[\"DDR 被认为是 vocabulary impoverish…",
  "leafUuid": "bdfacc34-2aa9-4479-a92c-1a4132e77c45",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe gen-depth-fingerprint from worst to borderline acceptance",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532"
}
```

---

### Assistant

_source line 8 · 2026-05-20T10:21:27.849Z_

I'll analyze the experiment plan and generate detailed worst-tier predictions. Let me first review the current state of completed experiments to calibrate predictions against what's already known.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdfacc34-2aa9-4479-a92c-1a4132e77c45",
  "isSidechain": false,
  "requestId": "req_011CbDespRn3WcNiKMuJzjWk",
  "type": "assistant",
  "uuid": "b33c9739-659f-4f44-a0a0-89de76689350",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyWmDnFGZV5rww7PojiWwN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24470,
      "cache_read_input_tokens": 11841,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 240,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24470
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

_source line 9 · 2026-05-20T10:21:31.860Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01V4eAatgiuyUVcy6zpnqR2N`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan YAML",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_3, find all YAML files related to experiment plans, registry, or dream/tier definitions. I need to understand the full experiment plan with all entries marked \"planned\" (not yet completed). Search for files like experiment_plan.yaml, registry.yaml, dream*.yaml, tier*.yaml, or similar. Also look for any paper_framing.md or similar files that define the tier system. Report file paths and key content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b33c9739-659f-4f44-a0a0-89de76689350",
  "isSidechain": false,
  "requestId": "req_011CbDespRn3WcNiKMuJzjWk",
  "type": "assistant",
  "uuid": "cf3f0d8a-bf99-48b6-a1e4-57429f16c119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyWmDnFGZV5rww7PojiWwN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24470,
      "cache_read_input_tokens": 11841,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 240,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24470
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

_source line 10 · 2026-05-20T10:22:22.012Z_

<details><summary>↩ Tool result · `toolu_01V4eAatgiuyUVcy6zpnqR2N`</summary>

````text
Perfect! I now have all the information needed. Let me compile a comprehensive report.

## Summary: Complete Experiment Plan & Tier System for gen-depth-fingerprint Project

### **Core Files Located**

1. **Experiment Plan**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`
2. **Writing Plan**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/writing_plan.yaml`
3. **Paper Framing**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md`
4. **Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml`
5. **Dream Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/dream_registry.yaml`
6. **Roadmap**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md`
7. **Global Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/global/registry.yaml`

---

### **Tier/Priority System**

The experiment plan uses a **3-tier priority system** based on claims:

| Tier | Name | Purpose | GPU Budget | Status |
|------|------|---------|-----------|--------|
| **P0** | Must-run (headline results) | Core claims validation | ~45.5 hrs | Mostly DONE |
| **P1** | Important for completeness | Story enhancement | ~48 hrs | DONE |
| **P2** | Nice-to-have | Strengthen claims | ~23 hrs | DONE |
| **Total** | | | ~116.5 hrs | **Within 200 H100 budget** |

---

### **"Planned" vs "Completed" Experiments**

#### **P0 Experiments (HEADLINE RESULTS) — Tied to 3 Core Claims**

All **COMPLETED**:

1. **plan_001** (Claim 2) - `feature_ablation_and_trend`
   - Status: **DONE**
   - Tests whether reference-model features have independent signal vs surface-only
   - Evidence: Full(0.82) > surface(0.76) > reference(0.72)

2. **plan_002** (Claim 1) - `cross_generator_evaluation`
   - Status: **DONE**
   - Leave-one-generator-out CV on 5 generators (now 8 generators tested)
   - Evidence: 6-gen LOGO F1=0.79, 8-gen LOGO binary F1=0.694 [0.688, 0.700]

3. **plan_003** (Claim 2) - `cross_family_reference_model`
   - Status: **DONE**
   - Tests non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base)
   - Evidence: All 3 reference models maintain entropy drift consistency

4. **plan_004** (Claim 3) - `downstream_utility`
   - Status: **DONE** (NEGATIVE FINDING)
   - Depth-aware filtering does NOT improve downstream CLM quality
   - Evidence: all(2.335) < size_matched(2.367) < depth01(2.387) - **diagnostic, not curative**

5. **plan_013** (Claims 1, 2) - `text_length_control`
   - Status: **DONE**
   - Controls text length confound (RC10)
   - Evidence: Length-matched F1=0.724 vs 0.770 unmatched; deconfounding confirmed

6. **plan_014** (Claim 1) - `large_scale_generator`
   - Status: **DONE**
   - Tests depth signal at 7B+ scale (Qwen3-8B-Base)
   - Evidence: 6-gen LOGO F1=0.7897, Qwen3-8B held-out F1=0.6849 (cross-scale gap noted)

7. **plan_015** (Claim 1) - `ordinal_baseline_comparison`
   - Status: **DONE**
   - Compares existing detector continuous scores vs custom 7-feature model
   - Evidence: 7-feature (0.798) >> FastDetectGPT (0.627), LD-Score (0.721)

#### **P1 Experiments (COMPLETENESS) — All DONE**

- **plan_005** - `prompt_type_comparison` (continuation vs elaboration vs rewriting)
- **plan_006** - `paraphrastic_comparison` (RQ2: attractor convergence theory)
- **plan_007** - `cross_model_chains` (different generator per depth step) → **binary F1=0.830, 3-class=0.789**
- **plan_008** - `multi_domain_seeds` (4 domains: news, Wikipedia, scientific, creative)
- **plan_009** - `finer_grained_ordinal` (5-class gen-0 through gen-4, drops to ~0.50)
- **plan_010** - `human_edit_robustness` (random word replacement + LLM-simulated editing)
- **plan_011** - `ld_score_feature` (character-distribution signatures)
- **plan_012** - `end_to_end_classifier` (QLoRA fine-tuned Qwen3.5-0.8B)

#### **P2 Experiments (STRENGTHEN CLAIMS) — All DONE**

- All 4 P2 experiments completed including additional scale, temperature, and domain validation

---

### **Recent Major Experiments (D029-D030 Tier)**

As of **May 20, 2026**, three breakthrough experiments completed:

1. **exp_057: 9-gen LOGO Scale Test**
   - Added Gemma-2-2B to the 8-gen evaluation
   - Result: 3-class F1=0.751, binary F1=0.666
   - Anomaly: Gemma gen-1 F1=0.036 (outlier, noted)

2. **exp_058: DDR Causality Analysis**
   - Permutation importance: 5.5× gap between drifting and stationary features
   - Granger causality: 6/7 features significant
   - Feature intervention validated

3. **exp_059: TOST Bootstrap Stability**
   - 100% stability across 2000 resamples
   - Confirms downstream utility negative finding is robust

---

### **3-Tier Dream Review System**

The dream registry contains **3 review tiers** (Best/Median/Worst):

**Recent Dreams (from dream_registry.yaml):**

1. **dream_20260514T181213** - Status: **DONE** (May 14)
   - Focus: Key uncertainties for Claim 2 ablation
   - Stages: imagine → write → review

2. **dream_20260514T221538** - Status: **DONE** (May 14)
   - Focus: D006 re-dream after framing repositioning
   - 6 major changes addressing reviewer concerns RC8, RC9, RC11

3. **dream_20260520T100349** - Status: **IMAGINING** (May 20, CURRENT)
   - Focus: Assess if paper is 3.0 Findings or 3.5 Borderline Conference
   - 33 pages, 20+ appendix experiments, identify single highest-impact improvement

---

### **Key Metrics Summary (paper_framing.md)**

| Metric | Value | Status |
|--------|-------|--------|
| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+ (leak-free) |
| LOGO 3-class F1 | 0.762 [0.758, 0.766] | (inflated by gen-0 seed sharing) |
| Cross-model binary F1 | **0.830** | 5-gen subset, generator-level LOGO |
| LOFO binary F1 | 0.686 | Leave-one-family-out |
| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B to Pythia-2.8B |
| 9-gen LOGO 3-class F1 | 0.751 | (+Gemma-2-2B) |
| Downstream (negative) | all < size_matched | TOST p=1.1×10⁻⁴ at ±2% margin |

---

### **Three Core Claims (Fully Mapped to Evidence)**

**Claim 1 — Depth Discriminability**: 7-feature ensemble achieves leak-free binary F1=0.694 under 8-gen LOGO, generalizing across generators (LOFO binary F1=0.686). Cross-model chains yield binary F1=0.830.

**Claim 2 — Differential Depth Response**: Central-tendency features (entropy_mean, TTR, hapax_ratio) drift monotonically (|ρ|>0.60); shape features (entropy_std, tail_decay) remain near-stationary (|ρ|<0.10). Full 7-feature >> surface-only + reference-only.

**Claim 3 — Downstream Utility (NEGATIVE)**: Depth-aware curation does NOT improve downstream CLM quality. Depth fingerprinting is **diagnostic**, not **curative**.

---

### **Current Project Status (May 20, 2026)**

**Phase**: Paper finalization + submission prep
- Compilation: 0 errors, 33 pages, main text ≤8 pages
- All P0/P1/P2 experiments complete
- Current dream evaluation in progress (dream_20260520T100349)
- **Submission target**: EMNLP 2026 ARR, **DDL: May 25** (5 days)
- **Positioning**: Findings track (target 3.5 Borderline Conference)
- GPU: 4× RTX 5090 idle, reserved for potential D029-style breakthrough experiments pending dream results

---

### **Experiment Hierarchy Summary**

```
PLANNED (concept) 
  → P0 MUST-RUN (7 experiments: 45.5 hrs)
     ├── plan_001: Feature ablation ✓ DONE
     ├── plan_002: Cross-generator ✓ DONE
     ├── plan_003: Cross-family ref ✓ DONE
     ├── plan_004: Downstream (negative) ✓ DONE
     ├── plan_013: Length control ✓ DONE
     ├── plan_014: 7B+ scale ✓ DONE
     └── plan_015: Baseline comparison ✓ DONE
  → P1 COMPLETENESS (8 experiments: 48 hrs) ✓ ALL DONE
  → P2 STRENGTHEN (4 experiments: 23 hrs) ✓ ALL DONE
  → D029-D030 BREAKTHROUGHS (3 experiments: esp_057/058/059) ✓ ALL DONE
  → TOTAL: 116.5 hrs (within 200 H100 budget) ✓ COMPLETE

CURRENT: DREAM STAGE (review + final polish)
NEXT: OpenReview submission (pending dream results)
```
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "cf3f0d8a-bf99-48b6-a1e4-57429f16c119",
  "isSidechain": false,
  "promptId": "cf777c8a-2c8c-4b56-bb20-59f28877ca5c",
  "type": "user",
  "uuid": "9cf90295-ad94-4f86-9f3d-7e08ad9928d7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_3, find all YAML files related to experiment plans, registry, or dream/tier definitions. I need to understand the full experiment plan with all entries marked \"planned\" (not yet completed). Search for files like experiment_plan.yaml, registry.yaml, dream*.yaml, tier*.yaml, or similar. Also look for any paper_framing.md or similar files that define the tier system. Report file paths and key content.",
    "agentId": "acad8c1f80ec211f2",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I now have all the information needed. Let me compile a comprehensive report.\n\n## Summary: Complete Experiment Plan & Tier System for gen-depth-fingerprint Project\n\n### **Core Files Located**\n\n1. **Experiment Plan**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`\n2. **Writing Plan**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/writing_plan.yaml`\n3. **Paper Framing**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md`\n4. **Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml`\n5. **Dream Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/dream_registry.yaml`\n6. **Roadmap**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md`\n7. **Global Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/global/registry.yaml`\n\n---\n\n### **Tier/Priority System**\n\nThe experiment plan uses a **3-tier priority system** based on claims:\n\n| Tier | Name | Purpose | GPU Budget | Status |\n|------|------|---------|-----------|--------|\n| **P0** | Must-run (headline results) | Core claims validation | ~45.5 hrs | Mostly DONE |\n| **P1** | Important for completeness | Story enhancement | ~48 hrs | DONE |\n| **P2** | Nice-to-have | Strengthen claims | ~23 hrs | DONE |\n| **Total** | | | ~116.5 hrs | **Within 200 H100 budget** |\n\n---\n\n### **\"Planned\" vs \"Completed\" Experiments**\n\n#### **P0 Experiments (HEADLINE RESULTS) — Tied to 3 Core Claims**\n\nAll **COMPLETED**:\n\n1. **plan_001** (Claim 2) - `feature_ablation_and_trend`\n   - Status: **DONE**\n   - Tests whether reference-model features have independent signal vs surface-only\n   - Evidence: Full(0.82) > surface(0.76) > reference(0.72)\n\n2. **plan_002** (Claim 1) - `cross_generator_evaluation`\n   - Status: **DONE**\n   - Leave-one-generator-out CV on 5 generators (now 8 generators tested)\n   - Evidence: 6-gen LOGO F1=0.79, 8-gen LOGO binary F1=0.694 [0.688, 0.700]\n\n3. **plan_003** (Claim 2) - `cross_family_reference_model`\n   - Status: **DONE**\n   - Tests non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base)\n   - Evidence: All 3 reference models maintain entropy drift consistency\n\n4. **plan_004** (Claim 3) - `downstream_utility`\n   - Status: **DONE** (NEGATIVE FINDING)\n   - Depth-aware filtering does NOT improve downstream CLM quality\n   - Evidence: all(2.335) < size_matched(2.367) < depth01(2.387) - **diagnostic, not curative**\n\n5. **plan_013** (Claims 1, 2) - `text_length_control`\n   - Status: **DONE**\n   - Controls text length confound (RC10)\n   - Evidence: Length-matched F1=0.724 vs 0.770 unmatched; deconfounding confirmed\n\n6. **plan_014** (Claim 1) - `large_scale_generator`\n   - Status: **DONE**\n   - Tests depth signal at 7B+ scale (Qwen3-8B-Base)\n   - Evidence: 6-gen LOGO F1=0.7897, Qwen3-8B held-out F1=0.6849 (cross-scale gap noted)\n\n7. **plan_015** (Claim 1) - `ordinal_baseline_comparison`\n   - Status: **DONE**\n   - Compares existing detector continuous scores vs custom 7-feature model\n   - Evidence: 7-feature (0.798) >> FastDetectGPT (0.627), LD-Score (0.721)\n\n#### **P1 Experiments (COMPLETENESS) — All DONE**\n\n- **plan_005** - `prompt_type_comparison` (continuation vs elaboration vs rewriting)\n- **plan_006** - `paraphrastic_comparison` (RQ2: attractor convergence theory)\n- **plan_007** - `cross_model_chains` (different generator per depth step) → **binary F1=0.830, 3-class=0.789**\n- **plan_008** - `multi_domain_seeds` (4 domains: news, Wikipedia, scientific, creative)\n- **plan_009** - `finer_grained_ordinal` (5-class gen-0 through gen-4, drops to ~0.50)\n- **plan_010** - `human_edit_robustness` (random word replacement + LLM-simulated editing)\n- **plan_011** - `ld_score_feature` (character-distribution signatures)\n- **plan_012** - `end_to_end_classifier` (QLoRA fine-tuned Qwen3.5-0.8B)\n\n#### **P2 Experiments (STRENGTHEN CLAIMS) — All DONE**\n\n- All 4 P2 experiments completed including additional scale, temperature, and domain validation\n\n---\n\n### **Recent Major Experiments (D029-D030 Tier)**\n\nAs of **May 20, 2026**, three breakthrough experiments completed:\n\n1. **exp_057: 9-gen LOGO Scale Test**\n   - Added Gemma-2-2B to the 8-gen evaluation\n   - Result: 3-class F1=0.751, binary F1=0.666\n   - Anomaly: Gemma gen-1 F1=0.036 (outlier, noted)\n\n2. **exp_058: DDR Causality Analysis**\n   - Permutation importance: 5.5× gap between drifting and stationary features\n   - Granger causality: 6/7 features significant\n   - Feature intervention validated\n\n3. **exp_059: TOST Bootstrap Stability**\n   - 100% stability across 2000 resamples\n   - Confirms downstream utility negative finding is robust\n\n---\n\n### **3-Tier Dream Review System**\n\nThe dream registry contains **3 review tiers** (Best/Median/Worst):\n\n**Recent Dreams (from dream_registry.yaml):**\n\n1. **dream_20260514T181213** - Status: **DONE** (May 14)\n   - Focus: Key uncertainties for Claim 2 ablation\n   - Stages: imagine → write → review\n\n2. **dream_20260514T221538** - Status: **DONE** (May 14)\n   - Focus: D006 re-dream after framing repositioning\n   - 6 major changes addressing reviewer concerns RC8, RC9, RC11\n\n3. **dream_20260520T100349** - Status: **IMAGINING** (May 20, CURRENT)\n   - Focus: Assess if paper is 3.0 Findings or 3.5 Borderline Conference\n   - 33 pages, 20+ appendix experiments, identify single highest-impact improvement\n\n---\n\n### **Key Metrics Summary (paper_framing.md)**\n\n| Metric | Value | Status |\n|--------|-------|--------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+ (leak-free) |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | (inflated by gen-0 seed sharing) |\n| Cross-model binary F1 | **0.830** | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B to Pythia-2.8B |\n| 9-gen LOGO 3-class F1 | 0.751 | (+Gemma-2-2B) |\n| Downstream (negative) | all < size_matched | TOST p=1.1×10⁻⁴ at ±2% margin |\n\n---\n\n### **Three Core Claims (Fully Mapped to Evidence)**\n\n**Claim 1 — Depth Discriminability**: 7-feature ensemble achieves leak-free binary F1=0.694 under 8-gen LOGO, generalizing across generators (LOFO binary F1=0.686). Cross-model chains yield binary F1=0.830.\n\n**Claim 2 — Differential Depth Response**: Central-tendency features (entropy_mean, TTR, hapax_ratio) drift monotonically (|ρ|>0.60); shape features (entropy_std, tail_decay) remain near-stationary (|ρ|<0.10). Full 7-feature >> surface-only + reference-only.\n\n**Claim 3 — Downstream Utility (NEGATIVE)**: Depth-aware curation does NOT improve downstream CLM quality. Depth fingerprinting is **diagnostic**, not **curative**.\n\n---\n\n### **Current Project Status (May 20, 2026)**\n\n**Phase**: Paper finalization + submission prep\n- Compilation: 0 errors, 33 pages, main text ≤8 pages\n- All P0/P1/P2 experiments complete\n- Current dream evaluation in progress (dream_20260520T100349)\n- **Submission target**: EMNLP 2026 ARR, **DDL: May 25** (5 days)\n- **Positioning**: Findings track (target 3.5 Borderline Conference)\n- GPU: 4× RTX 5090 idle, reserved for potential D029-style breakthrough experiments pending dream results\n\n---\n\n### **Experiment Hierarchy Summary**\n\n```\nPLANNED (concept) \n  → P0 MUST-RUN (7 experiments: 45.5 hrs)\n     ├── plan_001: Feature ablation ✓ DONE\n     ├── plan_002: Cross-generator ✓ DONE\n     ├── plan_003: Cross-family ref ✓ DONE\n     ├── plan_004: Downstream (negative) ✓ DONE\n     ├── plan_013: Length control ✓ DONE\n     ├── plan_014: 7B+ scale ✓ DONE\n     └── plan_015: Baseline comparison ✓ DONE\n  → P1 COMPLETENESS (8 experiments: 48 hrs) ✓ ALL DONE\n  → P2 STRENGTHEN (4 experiments: 23 hrs) ✓ ALL DONE\n  → D029-D030 BREAKTHROUGHS (3 experiments: esp_057/058/059) ✓ ALL DONE\n  → TOTAL: 116.5 hrs (within 200 H100 budget) ✓ COMPLETE\n\nCURRENT: DREAM STAGE (review + final polish)\nNEXT: OpenReview submission (pending dream results)\n```"
      }
    ],
    "totalDurationMs": 50146,
    "totalTokens": 84481,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 80998,
      "output_tokens": 2875,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 604
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 2875,
          "cache_read_input_tokens": 80998,
          "cache_creation_input_tokens": 604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 604,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 0,
      "bashCount": 6,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "cf3f0d8a-bf99-48b6-a1e4-57429f16c119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 11 · 2026-05-20T10:22:24.444Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UhxsajN9KrsuuHSZVYkof1`</summary>

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
  "parentUuid": "9cf90295-ad94-4f86-9f3d-7e08ad9928d7",
  "isSidechain": false,
  "requestId": "req_011CbDex5FrpVkse6TgYPefv",
  "type": "assistant",
  "uuid": "074f3839-0134-42fe-8c7c-f197235e9823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XgAj3LVUSW8zAFzp4n6hqr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3124,
      "cache_read_input_tokens": 36311,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3124,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 36311,
          "cache_creation_input_tokens": 3124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3124
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

_source line 12 · 2026-05-20T10:22:24.454Z_

<details><summary>↩ Tool result · `toolu_01UhxsajN9KrsuuHSZVYkof1`</summary>

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
  "parentUuid": "074f3839-0134-42fe-8c7c-f197235e9823",
  "isSidechain": false,
  "promptId": "cf777c8a-2c8c-4b56-bb20-59f28877ca5c",
  "type": "user",
  "uuid": "52cdf621-d3f6-4248-9df3-23396aa04012",
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
  "sourceToolAssistantUUID": "074f3839-0134-42fe-8c7c-f197235e9823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-20T10:22:24.492Z_

````json
{
  "parentUuid": "52cdf621-d3f6-4248-9df3-23396aa04012",
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
  "uuid": "f1773bca-66f0-4ea1-b45c-d1143ed68c9e",
  "timestamp": "2026-05-20T10:22:24.492Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：2.5-3.0 Below Threshold — 核心假设被挑战，至少一个 reviewer 给出 reject，需要 substantial reframing 但仍冲 EMNLP Findings（不降级到 workshop） 核心假设：[\"DDR 被认为是 vocabulary impoverish…",
  "leafUuid": "f1773bca-66f0-4ea1-b45c-d1143ed68c9e",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe gen-depth-fingerprint from worst to borderline acceptance",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532"
}
```

---

### Assistant

_source line 16 · 2026-05-20T10:23:08.595Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of all the experiments. Let me identify which experiments are still "planned" (not yet completed) in the experiment_plan. Looking at the registry, I can see the status of each experiment.

Actually, wait - looking more carefully at the user's request, they want me to generate worst-tier predictions for ALL experiments in the experiment_plan that have status "planned". But looking at the registry, most experiments seem to have been completed already (with various exp_ids). Let me cross-reference.

Looking at the experiment_plan YAML, all entries have `status: planned` in the user's prompt. But from the registry, many of these have been completed under various exp_ids. 

Re-reading the user's request more carefully: they want predictions for each planned experiment in the experiment_plan, treating them as if they're being predicted in the worst-tier scenario. This is a hypothetical exercise - imagining what results would look like if we're in the "worst" tier (2.5-3.0 Below Threshold). So I need to generate detailed worst-case predictions for each experiment from plan_001 through plan_015.

The worst tier is characterized by several key issues: DDR being dismissed as vocabulary impoverishment repackaging with insufficient F1 gap between surface and full models, base-model-only limitations combined with temperature sensitivity and instruction degradation creating fatal scope problems, F1 scores around 0.694 that fall short of practical utility compared to binary detection baselines exceeding 0.95, novelty concerns about the task formulation being weaponized as a negative finding, and the paper's length at 33 pages making it feel unfocused.

Now I'm working through each planned experiment to imagine results that would be consistent with this worst-tier outcome - plausible but disappointing findings that confirm reviewer concerns.

For the feature ablation experiment, I'd expect the surface-only F1 to stay very close to the full model results, which would validate the vocabulary impoverishment criticism. The reference-only baseline would perform noticeably worse, but the gap wouldn't be compelling enough. The DDR trends would show drift in both drifting and shape features, but with high variance that blurs the distinction between feature types.

For cross-generator evaluation, the leave-one-generator-out results would be mediocre with high variance across different generators, showing significant performance degradation when held-out generators are tested. The worst-performing generator would drop below 0.60 F1, making the family-out penalty look substantial.

For the cross-family reference model experiment, using non-Pythia reference models would show comparable or weaker DDR performance, suggesting the effect might be partially an artifact of the specific reference model choice rather than a robust phenomenon.

Now I'm thinking through several additional validation experiments. The downstream utility test would show all conditions performing equivalently, making the negative finding robust but also weaponizable against the paper's claims. Prompt type comparisons would reveal high variance across different prompt formulations, with continuation prompts performing much stronger than elaboration or rewriting variants. Paraphrastic chains would show comparable signal to the original chains, undermining the uniqueness of the approach. Cross-model chains would inflate F1 scores since they're easier to detect, which reviewers might see as trivializing the task. Finally, multi-domain seeds would expose large domain dependence with some domains performing near chance level. Looking at these additional experiment plans, I'm mapping out how different robustness checks and scaling tests will either confirm or undermine the core findings. The length control experiment should reveal whether document length is artificially inflating performance, the large-scale generator test will show if the signal holds across model sizes, and comparing against existing detectors will establish whether my feature ensemble is actually capturing something novel or just rediscovering what's already known. I'm realizing the framing needs to be careful—results should be weak enough to face rejection from some venues but not so catastrophic that they suggest the entire approach is flawed, positioning this for a Findings-level publication rather than a full conference acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1773bca-66f0-4ea1-b45c-d1143ed68c9e",
  "isSidechain": false,
  "requestId": "req_011CbDexFrbTUoXi9mLjYwcs",
  "type": "assistant",
  "uuid": "559b7cee-285e-4e00-ba36-9cab97d3f42f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLrNvUQpACi95Efq2KCBpc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8830,
      "cache_read_input_tokens": 39435,
      "output_tokens": 15286,
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
          "output_tokens": 15286,
          "cache_read_input_tokens": 39435,
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

_source line 17 · 2026-05-20T10:27:29.929Z_

```yaml
tier: worst
narrative_guidance: >
  Paper receives avg 2.5–3.0. Core attacks: (1) DDR ≈ vocabulary impoverishment repackaging,
  surface-only gap too small to justify a new framework; (2) base-model-only + temperature-sensitive +
  instruct collapse = fatal scope limitation for any practical framing; (3) 0.694 binary F1 compared
  unfairly against binary detection baselines (>0.95), labeled 'not actionable'; (4) Claim 3 negative
  finding weaponized as 'why does this matter'; (5) 33-page paper criticized as unfocused experiment dump.
  Reframe direction: pivot from 'depth classification as a tool' to 'empirical study of recursive
  generation dynamics' or 'complementary signal for existing detectors'. Neither requires new experiments.

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      Surface-only vs reference-only vs full 7-feature ablation on MVP data (Pythia-2.8B,
      ~4600 records). XGBoost 5-fold CV. Trend analysis per feature across depth 0–4.
      Perplexity pre-validation for Claim 3.
    expected_results:
      full_macro_f1: 0.773
      surface_only_f1: 0.741
      reference_only_f1: 0.698
      surface_vs_full_gap_pp: 3.2
      mcnemar_p_surface_vs_full: 0.027
      hapax_ratio_slope: -0.063
      hapax_ratio_r2: 0.88
      ttr_slope: -0.041
      ttr_r2: 0.82
      entropy_mean_slope: -0.089
      entropy_mean_r2: 0.79
      tail_decay_slope: 0.003
      tail_decay_r2: 0.04
      entropy_std_slope: -0.031
      entropy_std_r2: 0.41
      entropy_max_slope: 0.008
      entropy_max_r2: 0.07
      ppl_depth0: 14.2
      ppl_depth2: 3.8
      ppl_depth4: 1.9
    result_rationale: >
      Surface-only 达到 0.741（vs full 0.773），差距仅 3.2 pp。McNemar p=0.027 虽然显著但
      marginal。在 worst 档中，审稿人会 argue "surface features capture 96% of the signal"
      (0.741/0.773=0.959)，reference features 只是 marginal add-on，不构成独立 contribution。
      entropy_std 的 R²=0.41 模糊了 drifting/stationary 的 clean split —— 审稿人可以 argue
      这不是 bimodal response 而是 continuous degradation gradient，DDR 概念 overclaims。
      Trend analysis 显示所有 drifting features 都沿同一方向（单调递减），审稿人会 argue
      这就是 well-known vocabulary impoverishment 的多种测量方式，不是新现象。
    tables:
      - caption: "Feature ablation: 5-fold CV macro F1 on Pythia-2.8B MVP data"
        rows:
          - ["Feature Set", "Macro F1", "95% CI", "Δ vs Full"]
          - ["Full (7 features)", "0.773", "[0.758, 0.788]", "—"]
          - ["Surface-only (TTR + hapax)", "0.741", "[0.724, 0.758]", "−3.2 pp"]
          - ["Reference-only (5 entropy)", "0.698", "[0.679, 0.717]", "−7.5 pp"]
      - caption: "Per-feature depth trend (linear regression on depth 0–4)"
        rows:
          - ["Feature", "Category", "Slope", "R²", "Spearman ρ"]
          - ["hapax_ratio", "Drifting", "−0.063", "0.88", "−0.63"]
          - ["TTR", "Drifting", "−0.041", "0.82", "−0.61"]
          - ["entropy_mean", "Drifting", "−0.089", "0.79", "−0.60"]
          - ["entropy_std", "Ambiguous", "−0.031", "0.41", "−0.20"]
          - ["entropy_min", "Stationary", "−0.018", "0.22", "−0.15"]
          - ["tail_decay", "Stationary", "+0.003", "0.04", "+0.04"]
          - ["entropy_max", "Stationary", "+0.008", "0.07", "+0.05"]
    figures_description:
      - "7-panel feature trend plot showing mean ± std across depth 0–4. Drifting features (hapax, TTR, entropy_mean) show clear monotonic decline but with overlapping error bars at adjacent depths. entropy_std occupies an ambiguous middle zone (visible drift but high variance). Stationary features (tail_decay, entropy_max) are flat. Reviewer will highlight entropy_std ambiguity and overlapping error bars as evidence that the 'clean bimodal split' is overstated."
    analysis: >
      在 worst 档下，这个实验的核心问题是 surface-vs-full gap 太小。3.2 pp 差距在审稿人看来
      不足以证明 reference features 提供了 qualitatively different signal。entropy_std 的
      R²=0.41 处于 drifting/stationary 之间的灰色地带，破坏了 DDR 作为 clean bimodal phenomenon
      的叙事。审稿人会写："The authors' distinction between 'drifting' and 'stationary' features
      appears to be a gradient rather than a dichotomy, and the surface features alone capture
      the vast majority of the signal, suggesting this is vocabulary impoverishment measured
      differently rather than a novel phenomenon."

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      Expand to 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B).
      Leave-one-generator-out (LOGO) CV. 1000 seeds × 5 generators × 5 depths ≈ 23K chains.
    expected_results:
      total_records: 22800
      logo_avg_macro_f1: 0.762
      logo_avg_binary_f1: 0.680
      logo_binary_ci: [0.672, 0.688]
      logo_per_gen_binary:
        pythia_2_8b: 0.711
        pythia_1b: 0.724
        olmo_2_1b: 0.643
        qwen3_1_7b: 0.668
        qwen3_0_6b: 0.655
      logo_per_gen_range_pp: 8.1
      lofo_binary_f1: 0.665
      lofo_pythia_out_f1: 0.621
      lofo_qwen_out_f1: 0.648
      pythia_within_family_inflation: 0.038
    result_rationale: >
      LOGO binary F1 = 0.680，低于论文 framing 中的 0.694（后者是 8-gen 版本，但这里只有 5-gen，
      训练数据更少）。更关键的是 per-generator variance 很大：Pythia-1B 在 hold-out 时最好
      （0.724），因为 Pythia-2.8B 在训练集中提供了 same-family signal。OLMo-2-1B 最差（0.643），
      因为它是唯一的 non-Pythia/non-Qwen family。LOFO 进一步降到 0.665，Pythia held-out
      降到 0.621 —— 这说明跨 family 泛化比 LOGO 差很多。审稿人会 argue Pythia family overlap
      inflates LOGO by ~3.8 pp，真实 cross-family performance 只有 0.62–0.65，远不够 practical。
      8.1 pp per-gen range 被视为 high variance = unreliable。
    tables:
      - caption: "Leave-one-generator-out binary F1 (gen-1 vs gen-2+)"
        rows:
          - ["Held-out Generator", "Family", "Binary F1", "95% CI"]
          - ["Pythia-2.8B", "Pythia", "0.711", "[0.693, 0.729]"]
          - ["Pythia-1B", "Pythia", "0.724", "[0.707, 0.741]"]
          - ["OLMo-2-1B", "OLMo", "0.643", "[0.621, 0.665]"]
          - ["Qwen3-1.7B", "Qwen", "0.668", "[0.648, 0.688]"]
          - ["Qwen3-0.6B", "Qwen", "0.655", "[0.634, 0.676]"]
          - ["**Average**", "—", "**0.680**", "[0.672, 0.688]"]
      - caption: "Leave-one-family-out binary F1"
        rows:
          - ["Held-out Family", "Binary F1", "Δ vs LOGO avg"]
          - ["Pythia (both)", "0.621", "−5.9 pp"]
          - ["Qwen (both)", "0.648", "−3.2 pp"]
          - ["OLMo", "0.726", "+4.6 pp"]
          - ["**Average**", "**0.665**", "**−1.5 pp**"]
    figures_description:
      - "Confusion matrix heatmap (5 panels, one per held-out generator) showing gen-0/gen-1/gen-2+ predictions. All 5 panels show gen-1 vs gen-2+ confusion as the dominant error — gen-1 frequently misclassified as gen-2+ (FN rate 78–89% of binary errors). OLMo panel visually the worst with near-uniform gen-1/gen-2+ confusion."
    analysis: >
      Cross-generator generalization 是论文核心卖点，但 worst 档下 LOFO binary F1 = 0.665
      被审稿人视为 near-chance for practical use。Pythia family inflation 是 concrete evidence
      that LOGO overestimates generalization。审稿人会写："The authors report LOGO F1=0.680,
      but the more honest LOFO evaluation yields 0.665, and even this is inflated by including
      two Qwen variants. Single-family holdout F1 ranges from 0.621 (Pythia) to 0.726 (OLMo),
      suggesting the method's cross-family generalization is highly variable and may not be
      robust enough for deployment."

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      Test OLMo-2-1B and Qwen3-0.6B as alternative reference models (replacing Pythia-410M).
      Verify DDR drift persists with non-Pythia reference. Key falsification test for Claim 2.
    expected_results:
      logo_f1_pythia_ref: 0.680
      logo_f1_olmo_ref: 0.672
      logo_f1_qwen_ref: 0.689
      entropy_mean_drift_pythia: -1.19
      entropy_mean_drift_olmo: -0.61
      entropy_mean_drift_qwen: -0.95
      olmo_ref_hapax_rho: -0.58
      olmo_ref_entropy_mean_rho: -0.42
      olmo_ref_tail_decay_rho: 0.09
      drift_magnitude_ratio_olmo_vs_pythia: 0.51
      drift_direction_consistent: true
      shape_stationary_all_refs: true
    result_rationale: >
      DDR 方向一致（所有 reference model 下 drifting features 都 negative drift），shape features
      都 stationary —— 但 drift magnitude 高度依赖 reference model。OLMo reference 的
      entropy_mean drift 只有 Pythia 的 51%（-0.61 vs -1.19），Spearman ρ 从 -0.60 降到 -0.42。
      审稿人会 accept "direction is consistent" 但 argue "magnitude is reference-dependent,
      meaning DDR is partially a function of reference-generator mismatch rather than an intrinsic
      property of recursive generation." 这不会 kill Claim 2 但会 weaken 它 —— 审稿人 scores
      -0.5 pp on Claim 2 credibility。LOGO F1 across references 的差异很小（0.672–0.689），
      说明分类性能 robust，但 DDR phenomenon characterization 的 precision 被削弱。
    tables:
      - caption: "Cross-reference-model DDR comparison"
        rows:
          - ["Reference Model", "LOGO F1", "entropy_mean ρ", "hapax ρ", "tail_decay ρ", "Drift magnitude (avg)"]
          - ["Pythia-410M", "0.680", "−0.60", "−0.63", "+0.04", "1.19"]
          - ["OLMo-2-1B", "0.672", "−0.42", "−0.58", "+0.09", "0.61"]
          - ["Qwen3-0.6B", "0.689", "−0.55", "−0.61", "+0.06", "0.95"]
    figures_description:
      - "3-panel overlay plot showing entropy_mean drift curves (depth 0–4) under each reference model. All three curves decline monotonically, but OLMo reference curve is visibly shallower. Reviewer will annotate the magnitude discrepancy as evidence of reference-model dependence."
    analysis: >
      Falsification test 通过了（drift direction consistent），但 worst 档审稿人会 reframe 结果：
      "While the direction of entropy drift is consistent across reference models, the magnitude
      varies by 2×, undermining the claim that DDR is an intrinsic property of recursive generation.
      A more parsimonious explanation is that DDR magnitude reflects the degree of mismatch between
      the reference model and the generator, not the depth of generation per se." 这是 worst 档
      最 subtle 的攻击 —— 技术上实验通过了，但 interpretive framing 被挑战。

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune OLMo-1B on depth-stratified subsets. 3 random seeds with bootstrap CIs.
      Compare depth-aware filtering vs binary baselines. Sample-count-matched comparison.
    expected_results:
      all_data_ppl: 2.335
      all_data_ppl_ci: [2.330, 2.340]
      size_matched_ppl: 2.367
      size_matched_ppl_ci: [2.362, 2.372]
      depth01_ppl: 2.387
      depth01_ppl_ci: [2.381, 2.393]
      binary_filtered_ppl: 2.389
      binary_filtered_ppl_ci: [2.384, 2.394]
      depth0_only_ppl: 2.681
      depth0_only_ppl_ci: [2.671, 2.691]
      tost_p_2pct: 1.1e-4
      tost_p_1pct: 0.087
      cross_seed_ppl_std: 0.001
      ranking: "all < size_matched < depth01 ≈ binary_filtered << depth0_only"
      depth_filtering_vs_random_delta_ppl: +0.020
    result_rationale: >
      Negative finding 非常 clean：depth-aware filtering 不优于 random subsampling，TOST 在 ±2%
      margin 确认 equivalence。这在 worst 档下被 weaponize 为对整个工作 motivation 的质疑。
      审稿人会写："The authors' own Claim 3 demonstrates that generation depth has no downstream
      utility, raising the fundamental question: if knowing the depth of generation doesn't help
      improve model training, what is the practical value of distinguishing gen-1 from gen-2+?"
      Cross-seed variance 极小（std < 0.002）意味着结果 robust —— 但这 robustness 是 negative
      finding 的 robustness，对论文不利。depth0_only 显著差（2.681）只是说明真实人类文本 vs
      纯合成文本有区别 —— 这是 binary detection 已经解决的问题。
      TOST 在 ±1% margin 不显著（p=0.087）被审稿人注意到但不 weaponize（论文已选 ±2%）。
    tables:
      - caption: "Downstream CLM perplexity by training data depth composition (3 seeds)"
        rows:
          - ["Variant", "Train Size", "PPL (mean ± std)", "Δ vs All", "TOST ±2% p"]
          - ["All depths", "12,299", "2.335 ± 0.001", "—", "—"]
          - ["Size-matched random", "3,951", "2.367 ± 0.001", "+0.032", "ref"]
          - ["Depth 0+1 only", "3,951", "2.387 ± 0.001", "+0.052", "1.1×10⁻⁴"]
          - ["Binary filtered", "3,951", "2.389 ± 0.001", "+0.054", "8.7×10⁻⁵"]
          - ["Depth 0 only", "797", "2.681 ± 0.001", "+0.346", "—"]
    figures_description:
      - "Bar chart with error bars showing perplexity across 5 variants. The three middle bars (size-matched, depth01, binary) are visually indistinguishable within error bars. depth0_only stands out as an outlier. Reviewer annotation: 'The only meaningful distinction is between human text and machine text — precisely the binary detection problem.'"
    analysis: >
      Negative finding 本身是诚实的科学贡献，但在 worst 档下被 R2/R3 weaponize 成 "if depth
      doesn't matter for the most obvious downstream task, the burden of proof is on the authors
      to show ANY downstream task where depth matters." 论文的 framing 是 "diagnostic tool" 但
      审稿人认为 diagnostic without therapeutic value = limited impact。

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Compare continuation vs elaboration vs inspired_rewriting chains.
      1000 seeds × Pythia-2.8B × 3 prompt types.
    expected_results:
      cv_f1_continuation: 0.781
      cv_f1_elaboration: 0.730
      cv_f1_rewriting: 0.737
      lopto_avg_f1: 0.752
      lopto_held_out_continuation_f1: 0.762
      lopto_held_out_elaboration_f1: 0.733
      lopto_held_out_rewriting_f1: 0.762
      depth_retention_d4d0_cont: 0.831
      depth_retention_d4d0_elab: 0.986
      depth_retention_d4d0_rewrite: 0.939
      drift_entropy_mean_cont: -0.557
      drift_entropy_mean_elab: -0.471
      drift_entropy_mean_rewrite: -0.477
      cross_prompt_type_range_pp: 5.1
    result_rationale: >
      Continuation chains 明显优于 elaboration（5.1 pp gap），but elaboration/rewriting 的
      depth retention 更高（0.986/0.939 vs 0.831）。审稿人 worst 档解读：depth signal 只在
      continuation（最简单、最 artificial 的 chain type）中强，而更 realistic 的 elaboration/
      rewriting 中信号明显弱。"The method works best on the least realistic generation scenario
      (verbatim continuation) and degrades on more naturalistic prompt types, suggesting the depth
      signal is an artifact of the continuation paradigm rather than a general property of
      recursive generation." Elaboration 的 entropy_mean drift 比 continuation 弱 15%
      （-0.471 vs -0.557），但 hapax drift 反而更强 —— 这种 inconsistency 进一步削弱
      DDR 作为 unified phenomenon 的叙事。
    tables:
      - caption: "Per-prompt-type classification performance and drift statistics"
        rows:
          - ["Prompt Type", "CV F1", "LOPTO F1", "Depth Retention", "entropy_mean ρ", "hapax ρ"]
          - ["Continuation", "0.781", "0.762", "0.831", "−0.557", "−0.651"]
          - ["Elaboration", "0.730", "0.733", "0.986", "−0.471", "−0.674"]
          - ["Inspired Rewriting", "0.737", "0.762", "0.939", "−0.477", "−0.670"]
    figures_description:
      - "3×7 heatmap showing per-feature Spearman ρ across prompt types. Reveals that feature ranking is not stable across prompt types — entropy_mean is strongest for continuation but hapax_ratio is strongest for elaboration/rewriting. This inconsistency undermines the 'universal DDR' narrative."
    analysis: >
      Prompt-type dependence 在 worst 档下被视为 generalizability concern 而非 nuanced finding。
      审稿人会 argue："The 5 pp gap between continuation and elaboration means the method's
      performance is highly sensitive to the (unknowable in practice) generation prompt."

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      Construct parallel paraphrasing chains for comparison with continuation chains.
      Tests attractor convergence theory.
    expected_results:
      paraphrastic_cv_f1: 0.723
      continuation_cv_f1: 0.781
      paraphrastic_binary_f1: 0.665
      continuation_binary_f1: 0.694
      paraphrastic_drift_entropy_mean: -0.38
      paraphrastic_depth_retention_d4d0: 0.995
      attractor_convergence_observed: true
      effective_classes_paraphrastic: 2
      delta_para_vs_cont_pp: 2.9
    result_rationale: >
      Paraphrastic chains 显示 attractor convergence（depth retention 0.995 ≈ 1.0，即几乎
      不丢 chain），但 depth signal 弱于 non-paraphrastic（binary F1 0.665 vs 0.694）。
      差距只有 2.9 pp —— 审稿人 argue 这太小了，不足以证明 non-paraphrastic chains 有
      qualitatively different behavior。"Both paraphrastic and non-paraphrastic chains show
      similar (weak) depth signal, contradicting the authors' claim that non-paraphrastic
      chains exhibit a fundamentally different depth dynamics." Attractor convergence 被确认
      但反而成为 negative evidence："if paraphrastic chains converge to attractors within
      ~3 iterations, and non-paraphrastic chains show comparable depth signal, the phenomenon
      is better explained by generic generation drift than by the proposed DDR framework."
    tables:
      - caption: "Paraphrastic vs non-paraphrastic chain comparison"
        rows:
          - ["Chain Type", "CV F1", "Binary F1", "Depth Retention", "entropy_mean ρ", "Effective Classes"]
          - ["Non-paraphrastic (continuation)", "0.781", "0.694", "0.831", "−0.557", "3"]
          - ["Paraphrastic", "0.723", "0.665", "0.995", "−0.380", "~2"]
          - ["Δ", "+5.8 pp", "+2.9 pp", "−0.164", "−0.177", "+1"]
    figures_description:
      - "Dual-panel: left shows feature drift curves for paraphrastic vs continuation chains (both decline, paraphrastic shallower but similar shape). Right shows confusion matrices side-by-side. The visual similarity between the two panels undermines the 'qualitatively different' claim."
    analysis: >
      在 worst 档下，this experiment backfires。审稿人预期 non-paraphrastic chains would show
      dramatically different behavior，但 2.9 pp delta 不够 dramatic。反而证明 depth signal
      is a general (and weak) generation phenomenon，不是 non-paraphrastic chains 的 unique
      property。论文需要 reframe 为 "depth signal exists across chain types" 而非
      "non-paraphrastic chains are special."

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains (different generator per depth step) vs single-model chains.
      More realistic web contamination scenario.
    expected_results:
      cross_model_binary_f1: 0.764
      cross_model_3class_f1: 0.789
      single_model_binary_f1: 0.694
      single_model_3class_f1: 0.762
      delta_binary_pp: +7.0
      delta_3class_pp: +2.7
      cross_model_logo_binary_f1: 0.830
      cross_model_easier_reason: "generator heterogeneity amplifies distributional shift"
    result_rationale: >
      Cross-model chains 的 binary F1 大幅高于 single-model（0.764 vs 0.694, +7 pp），
      LOGO 甚至达到 0.830。审稿人在 worst 档下会 reframe 这个结果为 negative evidence：
      "The substantially higher F1 on cross-model chains (0.830) suggests the method is primarily
      detecting generator switching rather than generation depth. In single-model chains (the
      harder and more interesting case), F1 drops to 0.694." 这个 gap 被视为证明 depth signal
      在 single-model case 中 weak —— 真正的 depth classification 应该在 same-generator
      chains 上 work，而 cross-model improvement 是 "trivially explained by OOD detection
      of different model fingerprints at each depth."
    tables:
      - caption: "Cross-model vs single-model chain classification"
        rows:
          - ["Setting", "Binary F1", "3-class F1", "LOGO Binary F1"]
          - ["Single-model chains", "0.694", "0.762", "0.694"]
          - ["Cross-model chains", "0.764", "0.789", "0.830"]
          - ["Δ", "+7.0 pp", "+2.7 pp", "+13.6 pp"]
    figures_description:
      - "Scatter plot of per-sample prediction confidence (single-model x-axis vs cross-model y-axis). Points cluster above the diagonal, showing cross-model chains are systematically easier. Reviewer annotation: 'This gap suggests the method detects model switching, not depth.'"
    analysis: >
      Cross-model improvement 是 double-edged sword。在 worst 档下它证明了 "easy case 更好"
      但被 reinterpreted 为 the method doesn't truly measure depth —— 而是 measures generator
      heterogeneity。审稿人会 demand "same-generator transfer" 作为 real benchmark，where
      0.694 is the relevant number。

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      Expand to 4 domains: Wikipedia, news, scientific, creative writing.
      500 seeds per domain × 5 depths.
    expected_results:
      wikipedia_binary_f1: 0.724
      news_binary_f1: 0.667
      scientific_binary_f1: 0.631
      creative_binary_f1: 0.658
      cross_domain_logo_binary_f1: 0.652
      max_gap_vs_wiki_pp: 9.3
      worst_domain: scientific
      best_domain: wikipedia
      domain_variance_std: 0.034
    result_rationale: >
      Wikipedia（训练数据的主 domain）表现最好（0.724），scientific 最差（0.631）—— 9.3 pp gap。
      审稿人在 worst 档下 argue："The method's performance is domain-dependent, with scientific
      text yielding near-chance binary F1 (0.631). Since depth classification is most needed
      for scientific text (where AI contamination is a growing concern per the authors' own
      motivation), this domain sensitivity is a critical practical limitation." Cross-domain
      LOGO（training on 3 domains, test on 1）进一步降到 0.652。Domain dependence + generator
      dependence + temperature dependence + instruct dependence = cumulative scope narrowing
      that makes the method seem increasingly specialized.
    tables:
      - caption: "Per-domain binary F1 (LOGO across generators, within-domain)"
        rows:
          - ["Domain", "Seeds", "Binary F1", "95% CI", "Δ vs Wiki"]
          - ["Wikipedia", "500", "0.724", "[0.704, 0.744]", "—"]
          - ["News", "500", "0.667", "[0.645, 0.689]", "−5.7 pp"]
          - ["Creative", "500", "0.658", "[0.635, 0.681]", "−6.6 pp"]
          - ["Scientific", "500", "0.631", "[0.607, 0.655]", "−9.3 pp"]
          - ["**Cross-domain LOGO**", "2000", "**0.652**", "[0.638, 0.666]", "—"]
    figures_description:
      - "Radar chart showing binary F1 across 4 domains × 3 prompt types. The shape is asymmetric (Wikipedia+continuation = best corner, scientific+elaboration = worst corner), making the fragility visually apparent."
    analysis: >
      Domain dependence 在 worst 档下被叠加到 existing scope limitations 上。审稿人列出
      cumulative conditions："base models only, temperature ∈ [0.5, 0.9], continuation chains,
      Wikipedia-domain seeds" —— 这是 increasingly narrow niche that undermines any practical
      framing of the work.

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4).
      Test if depth signal extends beyond 3-class resolution.
    expected_results:
      five_class_macro_f1: 0.468
      five_class_ci: [0.451, 0.485]
      three_class_macro_f1: 0.762
      ordinal_coral_f1: 0.472
      ordinal_frank_hall_f1: 0.465
      gen1_vs_gen2_confusion_rate: 0.43
      gen2_vs_gen3_confusion_rate: 0.51
      gen3_vs_gen4_confusion_rate: 0.48
      mean_absolute_depth_error: 0.89
    result_rationale: >
      5-class F1 降到 0.468，接近 5-class random baseline（0.20）但仍显著高于 chance。
      Ordinal methods（CORAL, Frank-Hall）无改善（0.472, 0.465）。Gen-2/gen-3/gen-4 之间
      几乎无法区分（confusion rate 43–51%）。审稿人在 worst 档下 argue："The 5-class F1
      of 0.468 confirms that depth signal is extremely shallow — the method can roughly distinguish
      'early' (gen-0/1) from 'late' (gen-2+) but cannot meaningfully estimate depth. The 3-class
      formulation is not a principled choice but a ceiling imposed by signal weakness." 这直接
      打击了 "depth classification" 作为 task formulation 的 novelty —— 如果实际上只有
      binary-ish signal，那 task formulation 的贡献 = trivially extending binary detection
      by one class。
    tables:
      - caption: "Ordinal classification resolution comparison"
        rows:
          - ["Granularity", "Method", "Macro F1", "Ordinal Improvement"]
          - ["3-class", "XGBoost", "0.762", "—"]
          - ["5-class", "XGBoost", "0.468", "—"]
          - ["5-class", "CORAL", "0.472", "+0.4 pp"]
          - ["5-class", "Frank-Hall", "0.465", "−0.3 pp"]
    figures_description:
      - "5×5 confusion matrix heatmap. Gen-0 is cleanly classified (>0.90 recall), gen-1 shows moderate confusion with gen-2, and gen-2/3/4 form a near-uniform block — visually a 'binary-plus-noise' pattern rather than ordinal resolution."
    analysis: >
      5-class collapse 是 worst 档最有力的 evidence against task formulation novelty。
      审稿人会 argue 这证明 depth signal 本质上是 binary（human vs machine）加上一点
      gen-1 distinctiveness，而非 true ordinal depth estimation。"The authors frame a 3-class
      problem, but the data supports at most 2.5 classes."

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Robustness to simulated human edits: (A) random word replacement 5/10/20%,
      (B) LLM-simulated light rephrasing.
    expected_results:
      baseline_binary_f1: 0.694
      random_5pct_f1: 0.648
      random_10pct_f1: 0.611
      random_20pct_f1: 0.583
      llm_rephrase_f1: 0.641
      llm_rephrase_edit_distance: 0.51
      degradation_5pct_pp: -4.6
      degradation_10pct_pp: -8.3
      degradation_20pct_pp: -11.1
      degradation_llm_pp: -5.3
    result_rationale: >
      Even 5% random replacement 造成 4.6 pp drop（0.694 → 0.648），LLM rephrasing 造成
      5.3 pp drop（→ 0.641）。审稿人在 worst 档下 argue："In practice, AI-generated text is
      almost always edited before publication. The method loses 5+ pp F1 from light editing
      (51% edit distance), and this is on top of the already-modest 0.694 baseline. After
      realistic editing, depth classification falls to ~0.64, making it effectively useless."
      20% replacement 降到 0.583 —— 接近 chance for binary task。这与 instruct degradation、
      temperature sensitivity、domain dependence 一起构成 cumulative fragility picture。
    tables:
      - caption: "Robustness to simulated human edits"
        rows:
          - ["Perturbation", "Binary F1", "Δ vs Baseline", "Edit Distance"]
          - ["None (baseline)", "0.694", "—", "0.0"]
          - ["Random 5%", "0.648", "−4.6 pp", "~0.05"]
          - ["Random 10%", "0.611", "−8.3 pp", "~0.10"]
          - ["Random 20%", "0.583", "−11.1 pp", "~0.20"]
          - ["LLM rephrase", "0.641", "−5.3 pp", "0.51"]
    figures_description:
      - "Line chart: binary F1 vs edit intensity (0%, 5%, 10%, 20%, LLM). Near-linear degradation. LLM rephrase point sits between 5% and 10% random. Shaded area shows 95% CI widening at higher edit levels."
    analysis: >
      Robustness 实验在 worst 档下是 lose-lose：如果 robust，审稿人 say "shallow features
      aren't capturing anything generation-specific"; 如果 fragile（as here），审稿人 say
      "not practical." 这里是 fragile，confirm 审稿人 prior that depth signal is surface-level
      and easily disrupted.

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      Add LD-Score (character-distribution signature) as 8th feature.
      Test character-level complementarity to word/entropy features.
    expected_results:
      seven_feature_f1: 0.773
      eight_feature_with_ld_f1: 0.779
      ld_score_alone_f1: 0.623
      ld_score_spearman_depth: -0.31
      marginal_improvement_pp: 0.6
      feature_importance_ld: 0.028
    result_rationale: >
      LD-Score 作为单独 feature 只有 0.623 F1，加入后 marginal improvement 仅 0.6 pp
      （0.773 → 0.779），feature importance 排最后（0.028）。审稿人在 worst 档不会 attack
      这个实验本身（它是 minor addition），但会 note："Adding LD-Score provides negligible
      improvement, suggesting the character-level depth signal is largely subsumed by the
      existing word-level features — further evidence that all these features measure the same
      underlying vocabulary impoverishment." 这 reinforces RC1（repackaging）。
    tables:
      - caption: "LD-Score feature addition"
        rows:
          - ["Feature Set", "Macro F1", "Δ"]
          - ["7 features (baseline)", "0.773", "—"]
          - ["7 + LD-Score", "0.779", "+0.6 pp"]
          - ["LD-Score only", "0.623", "—"]
    figures_description:
      - "Feature importance bar chart (8 features). LD-Score is the shortest bar, visually insignificant compared to hapax_ratio, TTR, entropy_mean."
    analysis: >
      Minor experiment, minor result. 在 worst 档下被用作 supporting evidence for "all signals
      are the same signal" narrative，但不是 primary attack vector。

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned end-to-end depth classifier.
      Compares learned representations vs handcrafted 7-feature ensemble.
    expected_results:
      qlora_3class_f1: 0.891
      qlora_3class_ci: [0.878, 0.904]
      qlora_binary_f1: 0.842
      qlora_binary_ci: [0.826, 0.858]
      qlora_5class_f1: 0.571
      seven_feature_3class_f1: 0.762
      seven_feature_binary_f1: 0.694
      delta_3class_pp: +12.9
      delta_binary_pp: +14.8
      qlora_logo_3class_f1: 0.743
      qlora_logo_binary_f1: 0.712
      qlora_inference_cost_ratio: 47.0
    result_rationale: >
      QLoRA within-distribution 大幅碾压 7-feature（3-class 0.891 vs 0.762, +12.9 pp），
      但 LOGO 下差距缩小（0.743 vs 0.762，7-feature 反而更好 for 3-class）。Binary LOGO
      QLoRA 仍然更好（0.712 vs 0.694）。审稿人在 worst 档下会 cherry-pick within-distribution
      numbers："A simple QLoRA classifier achieves 0.842 binary F1, dwarfing the proposed
      method's 0.694. While the authors may argue their method is more lightweight, the 14.8 pp
      gap suggests the handcrafted features miss substantial depth signal that end-to-end
      learning captures." 论文的 efficiency argument（7-feature 用 410M reference 而 QLoRA
      用 full model）在 worst 档下被 dismiss："inference cost is not a compelling argument
      when the method is 15 pp worse." LOGO 下 QLoRA 的 cross-generator generalization
      差（3-class 0.743 < 0.762）可以作为 rebuttal point，但审稿人 already scored low
      before seeing this nuance。
    tables:
      - caption: "End-to-end (QLoRA) vs handcrafted 7-feature ensemble"
        rows:
          - ["Method", "3-class F1", "Binary F1", "LOGO 3-class", "LOGO Binary", "Cost Ratio"]
          - ["7-feature XGBoost", "0.762", "0.694", "0.762", "0.694", "1×"]
          - ["QLoRA (OLMo-1B)", "0.891", "0.842", "0.743", "0.712", "47×"]
          - ["Δ", "+12.9 pp", "+14.8 pp", "−1.9 pp", "+1.8 pp", "—"]
    figures_description:
      - "Grouped bar chart: within-distribution vs LOGO for both methods. Within-distribution shows QLoRA dominating; LOGO shows convergence. The within-distribution gap is visually dramatic and is what the reviewer will focus on."
    analysis: >
      End-to-end comparison 在 worst 档下是 devastating。审稿人会 focus on within-distribution
      gap (14.8 pp) and dismiss the LOGO nuance as "an artifact of limited training generators."
      论文需要 pre-empt 这个 attack by leading with LOGO numbers and framing within-distribution
      as oracle-access upper bound。

  - name: text_length_control
    plan_id: plan_013
    description: >
      Address text length confound: length distribution analysis, length-normalized features,
      length-matched subsampling.
    expected_results:
      length_depth_spearman: 0.12
      length_depth_p: 0.001
      length_matched_binary_f1: 0.724
      unmatched_binary_f1: 0.770
      delta_pp: -4.6
      normalized_ttr_trend_preserved: true
      normalized_hapax_trend_preserved: true
      length_is_primary_confound: false
      length_contributes_to_signal: true
      short_text_dropout_bias: true
    result_rationale: >
      Length-matched F1 降 4.6 pp（0.770 → 0.724）—— 意味着 text length 贡献了约 6% 的
      总 signal。审稿人在 worst 档下会 magnify 这个 finding："After controlling for text length,
      the already-modest F1 drops further to 0.724 (unmatched) → this suggests that part of the
      'depth signal' is simply a length artifact." 但 normalized features 的 trend 保持说明
      depth signal 不完全来自 length。这是 worst 档中一个 mixed result —— 不会 kill the paper
      但会 reduce credibility of the headline number by ≤5 pp。Short text dropout bias 的
      发现（deeper depths 有更多短文本被过滤掉）adds confound complexity that makes the
      narrative harder to follow。
    tables:
      - caption: "Length control analysis"
        rows:
          - ["Condition", "Binary F1", "Δ"]
          - ["Unmatched (original)", "0.770", "—"]
          - ["Length-matched subsample", "0.724", "−4.6 pp"]
          - ["Length-normalized features", "0.748", "−2.2 pp"]
    figures_description:
      - "Left: text length distribution violin plots by depth (showing subtle rightward shift at depth 0, leftward at depth 4). Right: before/after length matching classification boundary plots."
    analysis: >
      Length confound 是 necessary experiment 但在 worst 档下 result = "yes, some of the signal
      was length." 4.6 pp drop 不是 catastrophic 但会 erode reviewer trust in all other
      reported numbers ("were these also length-confounded?").

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      Add Qwen3-8B-Base to test depth signal at 7B+ scale.
      1000 seeds × 5 depths.
    expected_results:
      qwen3_8b_logo_binary_f1: 0.637
      qwen3_8b_logo_3class_f1: 0.683
      qwen3_8b_within_cv_f1: 0.711
      six_gen_logo_avg_f1: 0.789
      delta_vs_avg_pp: -10.6
      hapax_rho_8b: -0.41
      ttr_rho_8b: -0.39
      entropy_mean_rho_8b: -0.33
      feature_margin_compression: 0.58
    result_rationale: >
      Qwen3-8B 的 LOGO binary F1 = 0.637，比 6-gen average 低 10.6 pp。Feature drift
      magnitudes 全面压缩（hapax ρ 从 avg −0.63 降到 −0.41，compression ratio 0.58）。
      这与 paper_framing 中的 scale effect 一致，但 worst 档审稿人会 extrapolate："At 8B
      the signal is already substantially degraded (−10.6 pp). Frontier models (70B+) and API
      models (GPT-4, Claude) — which generate the vast majority of real-world AI text — would
      presumably show even weaker signal, making the method irrelevant for the contamination
      problem the paper claims to address." 这是 worst 档中 most damaging extrapolation —— 
      审稿人不需要实验数据就可以 argue 方法在 practical scale 上 doesn't work。Within-CV
      F1 = 0.711 还可以（说明 8B 自身的 depth signal 存在），但 cross-generator transfer 到
      8B 很弱（0.637），meaning smaller models 的 training data 不 transfer 到大模型。
    tables:
      - caption: "Scale effect: Qwen3-8B vs smaller generators"
        rows:
          - ["Generator", "Size", "LOGO Binary F1", "hapax ρ", "entropy_mean ρ"]
          - ["Pythia-1B", "1.0B", "0.724", "−0.65", "−0.60"]
          - ["OLMo-2-1B", "1.5B", "0.643", "−0.58", "−0.55"]
          - ["Pythia-2.8B", "2.8B", "0.711", "−0.63", "−0.60"]
          - ["Qwen3-8B", "8.0B", "0.637", "−0.41", "−0.33"]
          - ["**Trend**", "—", "**Declining**", "**Compressing**", "**Compressing**"]
    figures_description:
      - "Log-scale x-axis (model size) vs binary F1 y-axis, with feature drift magnitude as bubble size. Clear downward trend from 1B to 8B. Extrapolation dotted line to 70B crosses 0.50 (chance) at ~30B, visually devastating for scale argument."
    analysis: >
      Scale degradation 是 worst 档的 structural problem —— 审稿人不需要 70B 实验就可以
      argue via extrapolation。Paper 的 honest reporting of this limitation ("defines scope
      boundary") 在 worst 档下被 reframed 为 "the scope boundary excludes all models people
      actually care about."

  - name: ordinal_baseline_comparison
    plan_id: plan_015
    description: >
      Compare existing detector continuous scores (FastDetectGPT, Binoculars, LD-Score)
      as ordinal depth predictors vs our 7-feature ensemble.
    expected_results:
      seven_feature_logo_f1: 0.680
      avg_logprob_logo_f1: 0.653
      ld_score_logo_f1: 0.641
      fastdetectgpt_logo_f1: 0.612
      binoculars_logo_f1: 0.571
      seven_feature_vs_avglogprob_delta_pp: 2.7
      seven_feature_vs_ld_delta_pp: 3.9
      bootstrap_p_7feat_vs_avglogprob: 0.038
      multi_detector_ensemble_f1: 0.708
      multi_det_vs_7feat_delta_pp: +2.8
    result_rationale: >
      7-feature ensemble (0.680) 优于所有 single detectors，但 margin 很小 —— vs Avg-LogProb
      只有 2.7 pp (p=0.038, barely significant)。更关键的是 multi-detector ensemble（4 detectors
      + surface）达到 0.708，反过来超过 7-feature 2.8 pp。审稿人在 worst 档下会 argue："A
      simple average of existing detector scores (Avg-LogProb: 0.653) achieves 96% of the
      proposed method's F1, raising the question of whether depth-specific features are necessary.
      Moreover, a multi-detector ensemble outperforms the proposed features by 2.8 pp, suggesting
      that the optimal approach is to repurpose existing detectors rather than design depth-specific
      features." 这直接 undermines Claim 1 的 contribution：if existing tools + trivial ensembling
      works comparably or better，新 feature set 的 value proposition collapses。
      
      Bootstrap test 的 p=0.038 是 borderline significant —— worst 档审稿人会 note
      "barely significant and not corrected for multiple comparisons." 如果 Bonferroni correct
      for 4 comparisons，p=0.152 → not significant。
    tables:
      - caption: "Ordinal depth classification: 7-feature vs existing detector baselines"
        rows:
          - ["Method", "LOGO Binary F1", "95% CI", "Δ vs 7-feat", "Bootstrap p"]
          - ["**7-feature ensemble**", "**0.680**", "[0.672, 0.688]", "—", "—"]
          - ["Avg-LogProb (single)", "0.653", "[0.612, 0.694]", "−2.7 pp", "0.038"]
          - ["LD-Score (single)", "0.641", "[0.598, 0.684]", "−3.9 pp", "0.011"]
          - ["FastDetectGPT (single)", "0.612", "[0.571, 0.653]", "−6.8 pp", "0.002"]
          - ["Binoculars (single)", "0.571", "[0.528, 0.614]", "−10.9 pp", "<0.001"]
          - ["4-det + surface ensemble", "0.708", "[0.694, 0.722]", "+2.8 pp", "0.024"]
    figures_description:
      - "Forest plot showing each method's LOGO F1 with 95% CI. CIs overlap heavily between 7-feature and Avg-LogProb/LD-Score. Multi-detector ensemble CI sits above 7-feature point estimate. Visually, the 7-feature method is 'in the pack' rather than clearly superior."
    analysis: >
      Baseline comparison 在 worst 档下是 most dangerous experiment。7-feature 的 advantage
      over best single detector (2.7 pp) 太小，且被 multi-detector ensemble surpassed。
      审稿人会 conclude："The proposed features provide marginal, statistically borderline
      improvement over simply using existing detector scores for depth estimation. Given the
      complexity of the feature engineering and the need for a reference model, this represents
      insufficient contribution for even Findings-level publication." 这直接 targets the paper's
      reason to exist。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "559b7cee-285e-4e00-ba36-9cab97d3f42f",
  "isSidechain": false,
  "requestId": "req_011CbDexFrbTUoXi9mLjYwcs",
  "type": "assistant",
  "uuid": "899faa7d-5fbc-4add-9d61-b9f8ca8e4f98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLrNvUQpACi95Efq2KCBpc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8830,
      "cache_read_input_tokens": 39435,
      "output_tokens": 15286,
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
          "output_tokens": 15286,
          "cache_read_input_tokens": 39435,
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：2.5-3.0 Below Threshold — 核心假设被挑战，至少一个 reviewer 给出 reject，需要 substantial reframing 但仍冲 EMNLP Findings（不降级到 workshop） 核心假设：[\"DDR 被认为是 vocabulary impoverish…",
  "leafUuid": "899faa7d-5fbc-4add-9d61-b9f8ca8e4f98",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe gen-depth-fingerprint from worst to borderline acceptance",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：2.5-3.0 Below Threshold — 核心假设被挑战，至少一个 reviewer 给出 reject，需要 substantial reframing 但仍冲 EMNLP Findings（不降级到 workshop） 核心假设：[\"DDR 被认为是 vocabulary impoverish…",
  "leafUuid": "899faa7d-5fbc-4add-9d61-b9f8ca8e4f98",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe gen-depth-fingerprint from worst to borderline acceptance",
  "sessionId": "8c952852-52ac-4fcb-8bac-8129aa8ac532"
}
```

---
