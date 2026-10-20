# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：DDR decoding-agnostic 被承认但 reviewer 认为 scope 限制削弱了 generalizability claim，

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/6ac56804-240b-4d40-94ad-f71e723ec9d0.jsonl`
- **Structured JSON:** [`b798dce438a17462007c.json`](../../sessions/b7/b798dce438a17462007c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T21:40:53.211Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T21:40:53.211Z",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：DDR decoding-agnostic 被承认但 reviewer 认为 scope 限制削弱了 generalizability claim，需 rebuttal 或小幅调整后 borderline accept\n核心假设：[\"Decoding-agnostic DDR 被认可为有意义的 robustness check，但 reviewer 认为仅 greedy + top-k 两种策略不足以 claim 'decoding-agnostic'——要求补 nucleus sampling 或 beam search（无法在 72h 内做）\", \"至少一位 reviewer 质疑 base-model-only scope 的实际价值：'in practice people use instruct models, so what's the use case?'\", \"0.694 binary F1 被认为 'moderate'——不足以支撑 practical utility claim，但足以支撑 'proof of concept' 级别\", 'Claim 3 negative finding 被接受但 reviewer 认为实验设计有限（3 seeds, single perplexity metric），要求更多 downstream task', '72h 写作修复完成 70-85%：核心 section 到位但 related work 或 appendix 仍有粗糙处']\n关键指标范围：{'avg_reviewer_overall': [3.0, 3.5], 'avg_soundness': [3.0, 3.5], 'findings_accept_prob': [0.4, 0.65], 'writing_fix_completion': [0.7, 0.85], 'effective_claim_strength_delta': ['+0.1', '+0.2'], 'reviewer_scope_concern_severity': [3, 4]}\n叙事方向：Claim 2 措辞从 'decoding-agnostic property' 软化为 'robust across tested decoding strategies (greedy, top-k)'，留出 hedging 空间。Claim 1 的 0.694 F1 重新定位为 'first baseline for a novel task' 而非 'practical tool'。需在 rebuttal 中强调：(1) base model scope 是 intentional contribution boundary 而非 oversight，(2) instruct 退化本身是 finding，(3) 0.694 是 LOGO leak-free 的 conservative estimate。可能需要加一段 'Practical Implications' 明确说明 use case 是 training data auditing 而非 deployment-time detection。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nvenue: emnlp-2026\nfocus: exp_062 decoding strategy 实验已全部完成（16/16），DDR 被确认为 decoding-agnostic。Reviewer 建议不做新 GPU 实验，72 小时全投写作修复。评估当前论文在 EMNLP 2026 Findings 的竞争力，重点关注：(1) decoding-agnostic DDR 是否能升级 claim 强度 (2) 写作修复的优先级 (3) 论文整体分数预期\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. **DDR is decoding-agnostic**: greedy decoding confirms shape stability across all 8 generators (mean |d|=0.05), establishing DDR as an autoregressive property independent of sampling truncation; top-k sampling preserves full DDR for non-Pythia/OLMo generators while model-intrinsic boundary effects account for remaining violations. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust across decoding strategies, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Greedy shape stability | mean |d|=0.05, max 0.14 | 8/8 generators PASS |\n| Top-k DDR preservation | 5/8 full DDR | 4/4 non-Pythia/OLMo PASS; failures model-intrinsic |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_logo_f1: 0.7879\n    overall_ci95:\n    - 0.783\n    - 0.7929\n    spearman_entropy_max: 0.0503\n    spearman_entropy_min: -0.4061\n    spearman_hapax: -0.6467\n    spearman_ttr: -0.6302\n    spearman_entropy_mean: -0.6098\n    spearman_entropy_std: -0.1996\n    spearman_tail_decay: -0.0403\n- exp_id: plan-010-robustness\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_binary_f1: 0.695\n    5pct_binary_f1: 0.65\n    10pct_binary_f1: 0.614\n    20pct_binary_f1: 0.591\n    5pct_drop: -0.046\n    10pct_drop: -0.081\n    20pct_drop: -0.104\n- exp_id: plan-010-llm-rephrase\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_binary_f1: 0.6918\n    original_binary_ci:\n    - 0.6749\n    - 0.7067\n    original_multiclass_f1: 0.7385\n    original_multiclass_ci:\n    - 0.7269\n    - 0.7496\n    rephrased_binary_f1: 0.6471\n    rephrased_binary_ci:\n    - 0.6308\n    - 0.6619\n    rephrased_multiclass_f1: 0.6672\n    rephrased_multiclass_ci:\n    - 0.6548\n    - 0.6796\n    binary_drop: -0.0447\n    multiclass_drop: -0.0713\n    edit_distance_ratio: 0.5071\n    avg_sentences_replaced: 1.69\n    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\n    bugs_fixed:\n    - binary_task_gen1_vs_gen2+\n    - 3class_mapping\n    - tail_decay_rank100-1000\n- exp_id: plan-008-seed-stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_complexity_binary: 0.685\n    medium_binary: 0.695\n    high_complexity_binary: 0.695\n    low_complexity_multi: 0.772\n    medium_multi: 0.778\n    high_complexity_multi: 0.779\n    max_diff_binary_pp: 1.06\n    max_diff_multiclass_pp: 0.68\n    conclusion_label: seed_independent\n- exp_id: multi-domain-seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7459\n    news_binary_ci:\n    - 0.726\n    - 0.764\n    news_multiclass_f1: 0.6516\n    academic_binary_f1: 0.7386\n    academic_binary_ci:\n    - 0.72\n    - 0.757\n    academic_multiclass_f1: 0.6223\n    code_binary_f1: 0.7535\n    code_binary_ci:\n    - 0.737\n    - 0.77\n    code_multiclass_f1: 0.6344\n    wikipedia_baseline_binary_f1: 0.8148\n    wikipedia_baseline_multiclass_f1: 0.8632\n    max_gap_vs_wiki_pp: 7.62\n    worst_domain: academic\n    best_domain: code\n    conclusion_label: domain_independent\n- exp_id: exp_047_multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7119\n    news_binary_ci:\n    - 0.6898\n    - 0.7332\n    news_3class_f1: 0.7149\n    academic_binary_f1: 0.6279\n    academic_binary_ci:\n    - 0.6027\n    - 0.6515\n    academic_3class_f1: 0.6564\n    code_binary_f1: 0.6872\n    code_binary_ci:\n    - 0.6641\n    - 0.71\n    code_3class_f1: 0.6729\n    overall_binary_f1: 0.6757\n    overall_3class_f1: 0.6814\n    delta_vs_t10_news: -0.034\n    delta_vs_t10_academic: -0.1107\n    delta_vs_t10_code: -0.0663\n- exp_id: multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_048_cross_temp_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    6gen_logo:\n      within_0.7_binary: 0.9471\n      within_0.7_3class: 0.7888\n      cross_0.7to1.0_binary: 0.9001\n      cross_0.7to1.0_3class: 0.7225\n      within_1.0_binary: 0.9107\n      within_1.0_3class: 0.7257\n      cross_1.0to0.7_binary: 0.9581\n      cross_1.0to0.7_3class: 0.7913\n      caveat: Only Qwen3-1.7B differs between conditions; 5/6 generators share data\n    qwen_only:\n      within_0.7_binary: 0.9262\n      within_0.7_binary_ci:\n      - 0.916\n      - 0.935\n      within_0.7_3class: 0.769\n      within_0.7_3class_ci:\n      - 0.756\n      - 0.781\n      cross_0.7to1.0_binary: 0.7574\n      cross_0.7to1.0_binary_ci:\n      - 0.745\n      - 0.77\n      cross_0.7to1.0_3class: 0.4581\n      cross_0.7to1.0_3class_ci:\n      - 0.445\n      - 0.472\n      within_1.0_binary: 0.8248\n      within_1.0_binary_ci:\n      - 0.81\n      - 0.838\n      within_1.0_3class: 0.5738\n      within_1.0_3class_ci:\n      - 0.56\n      - 0.588\n      cross_1.0to0.7_binary: 0.9443\n      cross_1.0to0.7_binary_ci:\n      - 0.936\n      - 0.953\n      cross_1.0to0.7_3class: 0.6014\n      cross_1.0to0.7_3class_ci:\n      - 0.593\n      - 0.611\n      delta_0.7train_binary_pp: -16.9\n      delta_0.7train_3class_pp: -31.1\n      delta_1.0train_binary_pp: 12\n      delta_1.0train_3class_pp: 2.8\n      asymmetric_transfer: true\n- exp_id: exp_049_temp_curve_t05\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 4708\n    skipped: 113\n    seeds: 995\n    model: pythia-2.8b\n    temperature: 0.5\n    top_p: 0.9\n    within_cv_binary_f1: 0.8432\n    within_cv_binary_ci:\n    - 0.8301\n    - 0.8558\n    logo_binary_f1: 0.8136\n    logo_binary_ci:\n    - 0.7984\n    - 0.8282\n    entropy_mean_rho: -0.5844\n- exp_id: exp_050_temp_curve_t09\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    records: 4536\n    model: pythia-2.8b\n    temperature: 0.9\n    top_p: 0.9\n    within_cv_binary_f1: 0.5821\n    within_cv_binary_ci:\n    - 0.5655\n    - 0.5985\n    logo_binary_f1: 0.4804\n    logo_binary_ci:\n    - 0.4645\n    - 0.4976\n    entropy_mean_rho: -0.3016\n    delta_vs_t07_cv: -0.157\n    delta_vs_t07_logo: -0.259\n- exp_id: exp_051_independent_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_to_olmo_binary_f1: 0.6945\n    pythia_to_olmo_ci:\n    - 0.6727\n    - 0.7167\n    olmo_to_pythia_binary_f1: 0.666\n    olmo_to_pythia_ci:\n    - 0.6429\n    - 0.6893\n    avg_binary_f1: 0.6803\n    shared_seed_logo_ref: 0.694\n    delta_vs_shared: -0.014\n- exp_id: exp_052_instruct_qwen3_1_7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8753\n    within_binary_ci:\n    - 0.8667\n    - 0.8837\n    within_3class_f1: 0.7324\n    within_3class_ci:\n    - 0.7195\n    - 0.745\n    base_binary_f1: 0.8614\n    base_3class_f1: 0.769\n    logo_instruct_binary: 0.658\n    logo_instruct_3class: 0.543\n    logo_base_binary: 0.821\n    logo_base_3class: 0.802\n    gen1_f1_instruct: 0.438\n    gen1_f1_base: 0.579\n    spearman_direction: reversed (instruct ρ>0, base ρ<0)\n    delta_within_binary: 0.014\n    delta_within_3class: -0.037\n    delta_logo_binary: -0.163\n- exp_id: exp_053_instruct_olmo2_1b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8131\n    within_binary_ci:\n    - 0.8012\n    - 0.8251\n    within_3class_f1: 0.5748\n    within_3class_ci:\n    - 0.5605\n    - 0.5897\n    base_binary_f1: 0.8454\n    base_3class_f1: 0.7538\n    gen1_f1_instruct: 0.256\n    gen1_f1_base: 0.523\n    delta_within_binary: -0.032\n    delta_within_3class: -0.179\n    spearman_instruct:\n      entropy_mean: 0.482\n      entropy_std: 0.296\n      entropy_min: 0.08\n      entropy_max: 0.306\n      tail_decay: 0.228\n      ttr: 0.006\n      hapax_ratio: 0.025\n    spearman_base:\n      entropy_mean: -0.639\n      entropy_std: -0.296\n      entropy_min: -0.387\n      entropy_max: 0.067\n      tail_decay: -0.141\n      ttr: -0.7\n      hapax_ratio: -0.712\n    features_reversed: 6/7\n    model_used: allenai/OLMo-2-0425-1B-Instruct\n- exp_id: exp_054_instruct_llama3_2_3b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    instruct_binary_f1: 0.8381\n    instruct_binary_ci:\n    - 0.828\n    - 0.847\n    instruct_3class_f1: 0.5437\n    instruct_3class_ci:\n    - 0.53\n    - 0.558\n    base_binary_f1: 0.8488\n    base_3class_f1: 0.7424\n    rho_instruct_entropy_mean: 0.2299\n    rho_instruct_entropy_std: 0.2623\n    rho_instruct_entropy_min: -0.0027\n    rho_instruct_entropy_max: 0.2036\n    rho_instruct_tail_decay: 0.1198\n    rho_instruct_ttr: -0.1411\n    rho_instruct_hapax_ratio: -0.1157\n    rho_base_entropy_mean: -0.627\n    rho_base_ttr: -0.6856\n    rho_base_hapax_ratio: -0.6975\n    direction_reversals: 3\n    reversed_features:\n    - entropy_mean\n    - entropy_std\n    - tail_decay\n    data_count: 4974\n- exp_id: exp_055_qlora_olmo_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8881\n    macro_f1_3class_std: 0.0071\n    macro_f1_5class: 0.5976\n    macro_f1_5class_std: 0.0046\n    binary_f1: 0.8363\n    binary_f1_std: 0.0096\n    n_samples: 4429\n    runtime_seconds: 1689.7\n- exp_id: exp_056_qlora_qwen_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.9066\n    macro_f1_3class_std: 0.0082\n    macro_f1_5class: 0.5514\n    macro_f1_5class_std: 0.0031\n    binary_f1: 0.8672\n    binary_f1_std: 0.0137\n    n_samples: 4963\n    runtime_seconds: 1880.5\n- exp_id: exp_055b_qlora_olmo_base\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8588\n    macro_f1_3class_std: 0.0036\n    macro_f1_5class: 0.5398\n    macro_f1_5class_std: 0.015\n    binary_f1: 0.7925\n    binary_f1_std: 0.0097\n    n_samples: 2379\n    runtime_seconds: 911.7\n    note: completed before kill signal\n- exp_id: exp_056b_qlora_qwen_base\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.904\n    macro_f1_3class_std: 0.0094\n    macro_f1_5class: 0.5544\n    macro_f1_5class_std: 0.0068\n    binary_f1: 0.8597\n    binary_f1_std: 0.0123\n    n_samples: 2291\n    runtime_seconds: 880.9\n    note: completed before kill signal\n- exp_id: exp_057_scale_9gen_logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: superseded by exp_057 (rerun with fixed Gemma data)\n    first_run_3class_f1: 0.7516\n    first_run_binary_f1: 0.6842\n    see_exp_057_for_final: true\n- exp_id: exp_058_ddr_causality\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    permutation_baseline_f1: 0.7714\n    drifting_avg_importance: 0.1578\n    stationary_avg_importance: 0.0297\n    drifting_stationary_ratio: 5.31\n    granger_significant_features: 6/7\n    granger_max_delta_r2: 0.031\n    granger_max_delta_r2_feature: entropy_std\n    granger_nonsig_feature: entropy_min\n    granger_panel_n: 29095\n    intervention_max_f1_drop: 0.0203\n    intervention_max_feature: entropy_max\n    intervention_min_f1_drop: 0.0061\n- exp_id: exp_059_tost_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_bootstrap: 1000\n    seed: 42\n    margin_d: 0.2\n    entropy_max:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.062\n      d_ci:\n      - 0.037\n      - 0.088\n    entropy_min:\n      median_p: 0\n      rejection_rate: 1\n      median_d: -0.016\n      d_ci:\n      - -0.042\n      - 0.011\n    tail_decay:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.088\n      d_ci:\n      - 0.065\n      - 0.111\n    entropy_std:\n      median_p: 1\n      rejection_rate: 0\n      median_d: 0.458\n      d_ci:\n      - 0.435\n      - 0.479\n    stationary_features_robust: true\n- exp_id: exp_057\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    9gen_logo_3class_f1: 0.751\n    9gen_logo_binary_f1: 0.6661\n    8gen_baseline_3class_f1: 0.7698\n    delta_9gen_vs_8gen: -0.0188\n    n_total_rows: 42015\n    n_generators: 9\n    qwen3_8b_3class_f1: 0.6955\n    qwen3_8b_binary_f1: 0.6468\n    gemma_2_2b_3class_f1: 0.6279\n    gemma_2_2b_binary_f1: 0.4402\n    per_gen_3class_f1:\n      pythia-1b: 0.8571\n      qwen3-0.6b: 0.8185\n      pythia-2.8b: 0.8117\n      qwen3-1.7b: 0.8114\n      olmo-2-1b: 0.7732\n      llama-3.2-3b: 0.7591\n      qwen3-8b: 0.6955\n      gemma-2-2b: 0.6279\n      mistral-7b-v0.3: 0.6045\n    tail_decay_consistency: VERIFIED_all_9gen_logprob_slope\n    data_source: features_9gen.csv (42015 rows, Gemma fixed)\n- exp_id: exp_060_14b_ddr_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 2229\n    n_seeds: 498\n    depth_distribution:\n      '0': 498\n      '1': 488\n      '2': 466\n      '3': 414\n      '4': 363\n    entropy_mean:\n      rho: -0.3877\n      d: 0.7765\n      group: drifting\n    entropy_std:\n      rho: -0.0557\n      d: -0.0223\n      group: stationary\n    entropy_max:\n      rho: 0.0791\n      d: -0.1717\n      group: stationary\n    entropy_min:\n      rho: -0.2471\n      d: -0.1365\n      group: stationary\n    ttr:\n      rho: -0.4916\n      d: 1.0913\n      group: drifting\n    hapax_ratio:\n      rho: -0.5065\n      d: 1.1245\n      group: drifting\n    tail_decay:\n      rho: -0.0637\n      d: 0.1356\n      group: stationary\n    ddr_pattern_match: true\n- exp_id: exp_061_instruct_ref_ddr\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwen_instruct:\n      base_ref_rho_entropy_mean: 0.478\n      instruct_ref_rho_entropy_mean: 0.221\n      base_ref_d_entropy_mean: 1.981\n      instruct_ref_d_entropy_mean: 1.022\n    olmo_instruct:\n      base_ref_rho_entropy_mean: 0.482\n      instruct_ref_rho_entropy_mean: -0.113\n      base_ref_d_entropy_mean: 1.33\n      instruct_ref_d_entropy_mean: 0.017\n- exp_id: decoding_strategy_shape\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_062_decoding_strategy_shape\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T21:40:53.214Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T21:40:53.214Z",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-21T21:40:53.232Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：DDR decoding-agnostic 被承认但 reviewer 认为 scope 限制削弱了 generalizability claim，需 rebuttal 或小幅调整后 borderline accept
核心假设：["Decoding-agnostic DDR 被认可为有意义的 robustness check，但 reviewer 认为仅 greedy + top-k 两种策略不足以 claim 'decoding-agnostic'——要求补 nucleus sampling 或 beam search（无法在 72h 内做）", "至少一位 reviewer 质疑 base-model-only scope 的实际价值：'in practice people use instruct models, so what's the use case?'", "0.694 binary F1 被认为 'moderate'——不足以支撑 practical utility claim，但足以支撑 'proof of concept' 级别", 'Claim 3 negative finding 被接受但 reviewer 认为实验设计有限（3 seeds, single perplexity metric），要求更多 downstream task', '72h 写作修复完成 70-85%：核心 section 到位但 related work 或 appendix 仍有粗糙处']
关键指标范围：{'avg_reviewer_overall': [3.0, 3.5], 'avg_soundness': [3.0, 3.5], 'findings_accept_prob': [0.4, 0.65], 'writing_fix_completion': [0.7, 0.85], 'effective_claim_strength_delta': ['+0.1', '+0.2'], 'reviewer_scope_concern_severity': [3, 4]}
叙事方向：Claim 2 措辞从 'decoding-agnostic property' 软化为 'robust across tested decoding strategies (greedy, top-k)'，留出 hedging 空间。Claim 1 的 0.694 F1 重新定位为 'first baseline for a novel task' 而非 'practical tool'。需在 rebuttal 中强调：(1) base model scope 是 intentional contribution boundary 而非 oversight，(2) instruct 退化本身是 finding，(3) 0.694 是 LOGO leak-free 的 conservative estimate。可能需要加一段 'Practical Implications' 明确说明 use case 是 training data auditing 而非 deployment-time detection。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-fingerprint
venue: emnlp-2026
focus: exp_062 decoding strategy 实验已全部完成（16/16），DDR 被确认为 decoding-agnostic。Reviewer 建议不做新 GPU 实验，72 小时全投写作修复。评估当前论文在 EMNLP 2026 Findings 的竞争力，重点关注：(1) decoding-agnostic DDR 是否能升级 claim 强度 (2) 写作修复的优先级 (3) 论文整体分数预期

## paper_framing.md

# Paper Framing — gen-depth-fingerprint

## Target Venue
- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标
- Positioning: **Findings paper**（非 main conference long paper）
- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)

## Core Insight
Non-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. **DDR is decoding-agnostic**: greedy decoding confirms shape stability across all 8 generators (mean |d|=0.05), establishing DDR as an autoregressive property independent of sampling truncation; top-k sampling preserves full DDR for non-Pythia/OLMo generators while model-intrinsic boundary effects account for remaining violations. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust across decoding strategies, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.

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
| Greedy shape stability | mean |d|=0.05, max 0.14 | 8/8 generators PASS |
| Top-k DDR preservation | 5/8 full DDR | 4/4 non-Pythia/OLMo PASS; failures model-intrinsic |
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
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp-001-gen-s1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp-001-gen-s2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp-001-gen-s3
  name: ''
  status: DONE
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
  status: DONE
  conclusion: killed
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
  status: DONE
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
  conclusion: killed
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
  status: DONE
  conclusion: killed
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
  status: DONE
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
  status: DONE
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
  status: DONE
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
  status: DONE
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
  status: DONE
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
  status: DONE
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
  status: DONE
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
- exp_id: decoding_strategy_shape
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_062_decoding_strategy_shape
  name: ''
  status: DONE
  conclusion: success
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
  "promptId": "8cd44039-612b-4058-80a1-4cde6e090ba1",
  "type": "user",
  "uuid": "f85f5cbd-9212-4a62-95a4-83d795ed4d11",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T21:40:53.230Z_

```json
{
  "parentUuid": "f85f5cbd-9212-4a62-95a4-83d795ed4d11",
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
  "uuid": "f9c710bd-3a0f-4aab-9710-7a1724bd8fde",
  "timestamp": "2026-05-21T21:40:53.230Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T21:40:53.230Z_

```json
{
  "parentUuid": "f9c710bd-3a0f-4aab-9710-7a1724bd8fde",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "19436b61-c9c6-457b-a3cc-fcaa013c6a8d",
  "timestamp": "2026-05-21T21:40:53.230Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DDR decoding-agnostic 被承认但 reviewer 认为 scope 限制削弱了 generalizability claim，需 rebuttal 或小幅调整后 borderline accept 核心假设：[\"Decoding-agnostic DDR 被认可为有意义的 robus…",
  "leafUuid": "19436b61-c9c6-457b-a3cc-fcaa013c6a8d",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "DDR decoding-agnostic validation and writing-focused revision",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

### Assistant

_source line 8 · 2026-05-21T21:40:57.259Z_

I'll review the experiment plan and the completed registry data to generate detailed predicted results for each planned experiment under the median tier.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19436b61-c9c6-457b-a3cc-fcaa013c6a8d",
  "isSidechain": false,
  "requestId": "req_011CbGSVzNpDAVtoeyWiBqmg",
  "type": "assistant",
  "uuid": "dda5fdc5-c96d-4924-8370-bde128f972be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c3SAd114MsJkz5gJGjagA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25012,
      "cache_read_input_tokens": 11841,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 271,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25012
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

_source line 9 · 2026-05-21T21:41:01.841Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LKedaHfd14QEY8jkc5D4n2`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan and registry",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_3, I need to find:\n1. The experiment_plan file (could be YAML, JSON, or markdown) that lists planned experiments (plan_001 through plan_015)\n2. The registry file that tracks completed experiments\n3. Any file related to exp_062 decoding strategy results (the most recent experiment)\n4. Any file with paper_framing or median tier definitions\n\nSearch broadly - check for files like experiment_plan.yaml, registry.yaml, exp_062*, paper_framing.md, and any YAML/JSON files in the project root or subdirectories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dda5fdc5-c96d-4924-8370-bde128f972be",
  "isSidechain": false,
  "requestId": "req_011CbGSVzNpDAVtoeyWiBqmg",
  "type": "assistant",
  "uuid": "47ea6c8e-5cf7-49e2-972d-4801331d5faf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c3SAd114MsJkz5gJGjagA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25012,
      "cache_read_input_tokens": 11841,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 271,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25012
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

_source line 10 · 2026-05-21T21:41:26.449Z_

<details><summary>↩ Tool result · `toolu_01LKedaHfd14QEY8jkc5D4n2`</summary>

```text
Perfect! Now I have all the information I need. Let me compile my findings:

## Summary of Files Found

I've successfully located all the key files you requested in the project. Here's what I found:

### 1. **Experiment Plan File**
**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`

This YAML file contains the complete planned experiment roadmap with all 15 plans (plan_001 through plan_015):
- **P0 (Must-run):** plan_001 through plan_004, plan_013, plan_015 - 45.5 GPU hours
- **P1 (Important for story):** plan_005 through plan_008, plan_014 - 48 GPU hours  
- **P2 (Nice-to-have):** plan_009 through plan_012 - 23 GPU hours
- **Total budget:** ~116.5 GPU hours (within 200 H100-hour budget)

Each plan includes: id, claim number(s), name, description, priority, GPU budget, dependencies, and notes.

### 2. **Registry File** (Completed Experiments)
**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml`

This YAML file tracks 68 completed experiment runs including:
- **mvp-001:** MVP baseline (DONE) - macro_f1: 0.8408
- **plan-001 / plan-001-fix:** Feature ablation analysis (DONE)
- **plan-002 through plan-015:** Various experiments in progress or completed
- **exp_047, exp_058, exp_059, exp_062:** Recent experiments with detailed specs and metrics

### 3. **exp_062 Decoding Strategy Results**
**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/checkpoints/exp_062_decoding_strategy_shape_DONE_20260521T212603.json`

This checkpoint file (DONE status) contains:
- **Hypothesis:** Testing DDR (Differential Depth Response) shape stability across greedy and top-k decoding strategies
- **Spec:** 3 generators (pythia-2.8b, olmo-2-1b, qwen3-1.7b), 2 decoding strategies (greedy, topk)
- **Conclusion:** success
- **Completed:** 2026-05-21T21:26:03.841Z

Also related checkpoints at:
- `exp_062_decoding_strategy_shape_RUNNING_20260521T212559.json`
- `exp_062_decoding_strategy_shape_QUEUED_20260521T064414.json`

### 4. **Paper Framing Files**
**Main location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md`

**Also in dream reports (best/median/worst tiers):**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_*/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_*/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_*/worst/paper_framing.md`

The main paper_framing.md includes:
- **Core insight:** Differential Depth Response (DDR) showing feature drift vs stationarity across generation depths
- **3 core claims** (all falsifiable)
- **Primary venue:** EMNLP 2026 Findings (ARR deadline: May 25, 2026)
- **Headline metric:** Leak-free binary F1 = 0.694 [0.688, 0.700] under 8-gen LOGO
- **Scope limitations:** Base models only, temperature sensitivity, 7-feature ensemble trade-offs
- **Contribution positioning:** Findings-level empirical characterization + negative finding on downstream utility

### Median Tier Definitions
The "median tier" appears throughout the dream_reports directory structure (dated 2026-05-14 through 2026-05-21), representing a severity/quality assessment level used in review processes:
- **best/** tier
- **median/** tier  
- **worst/** tier

Each contains paper framings, review reports, imagined experiments, and phase logs.

All files are located in the project directory at `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47ea6c8e-5cf7-49e2-972d-4801331d5faf",
  "isSidechain": false,
  "promptId": "8cd44039-612b-4058-80a1-4cde6e090ba1",
  "type": "user",
  "uuid": "c67045bf-9b0e-49ef-9f60-5609b689d775",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_3, I need to find:\n1. The experiment_plan file (could be YAML, JSON, or markdown) that lists planned experiments (plan_001 through plan_015)\n2. The registry file that tracks completed experiments\n3. Any file related to exp_062 decoding strategy results (the most recent experiment)\n4. Any file with paper_framing or median tier definitions\n\nSearch broadly - check for files like experiment_plan.yaml, registry.yaml, exp_062*, paper_framing.md, and any YAML/JSON files in the project root or subdirectories.",
    "agentId": "a8f35210033e88542",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information I need. Let me compile my findings:\n\n## Summary of Files Found\n\nI've successfully located all the key files you requested in the project. Here's what I found:\n\n### 1. **Experiment Plan File**\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml`\n\nThis YAML file contains the complete planned experiment roadmap with all 15 plans (plan_001 through plan_015):\n- **P0 (Must-run):** plan_001 through plan_004, plan_013, plan_015 - 45.5 GPU hours\n- **P1 (Important for story):** plan_005 through plan_008, plan_014 - 48 GPU hours  \n- **P2 (Nice-to-have):** plan_009 through plan_012 - 23 GPU hours\n- **Total budget:** ~116.5 GPU hours (within 200 H100-hour budget)\n\nEach plan includes: id, claim number(s), name, description, priority, GPU budget, dependencies, and notes.\n\n### 2. **Registry File** (Completed Experiments)\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml`\n\nThis YAML file tracks 68 completed experiment runs including:\n- **mvp-001:** MVP baseline (DONE) - macro_f1: 0.8408\n- **plan-001 / plan-001-fix:** Feature ablation analysis (DONE)\n- **plan-002 through plan-015:** Various experiments in progress or completed\n- **exp_047, exp_058, exp_059, exp_062:** Recent experiments with detailed specs and metrics\n\n### 3. **exp_062 Decoding Strategy Results**\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/checkpoints/exp_062_decoding_strategy_shape_DONE_20260521T212603.json`\n\nThis checkpoint file (DONE status) contains:\n- **Hypothesis:** Testing DDR (Differential Depth Response) shape stability across greedy and top-k decoding strategies\n- **Spec:** 3 generators (pythia-2.8b, olmo-2-1b, qwen3-1.7b), 2 decoding strategies (greedy, topk)\n- **Conclusion:** success\n- **Completed:** 2026-05-21T21:26:03.841Z\n\nAlso related checkpoints at:\n- `exp_062_decoding_strategy_shape_RUNNING_20260521T212559.json`\n- `exp_062_decoding_strategy_shape_QUEUED_20260521T064414.json`\n\n### 4. **Paper Framing Files**\n**Main location:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md`\n\n**Also in dream reports (best/median/worst tiers):**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_*/best/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_*/median/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_*/worst/paper_framing.md`\n\nThe main paper_framing.md includes:\n- **Core insight:** Differential Depth Response (DDR) showing feature drift vs stationarity across generation depths\n- **3 core claims** (all falsifiable)\n- **Primary venue:** EMNLP 2026 Findings (ARR deadline: May 25, 2026)\n- **Headline metric:** Leak-free binary F1 = 0.694 [0.688, 0.700] under 8-gen LOGO\n- **Scope limitations:** Base models only, temperature sensitivity, 7-feature ensemble trade-offs\n- **Contribution positioning:** Findings-level empirical characterization + negative finding on downstream utility\n\n### Median Tier Definitions\nThe \"median tier\" appears throughout the dream_reports directory structure (dated 2026-05-14 through 2026-05-21), representing a severity/quality assessment level used in review processes:\n- **best/** tier\n- **median/** tier  \n- **worst/** tier\n\nEach contains paper framings, review reports, imagined experiments, and phase logs.\n\nAll files are located in the project directory at `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`"
      }
    ],
    "totalDurationMs": 24603,
    "totalTokens": 45957,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 44624,
      "output_tokens": 1188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 140
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1188,
          "cache_read_input_tokens": 44624,
          "cache_creation_input_tokens": 140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 140,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 4,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "47ea6c8e-5cf7-49e2-972d-4801331d5faf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T21:41:29.462Z_

<details open><summary>🔧 Tool call — Read · `toolu_019LKfJLaMTuJaLiZgKQsVS3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/checkpoints/exp_062_decoding_strategy_shape_DONE_20260521T212603.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c67045bf-9b0e-49ef-9f60-5609b689d775",
  "isSidechain": false,
  "requestId": "req_011CbGSYSGMo34PHEk8iqoGi",
  "type": "assistant",
  "uuid": "539e3847-11f8-468c-a6a9-3582946d4377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139n9ppGCBamax9VH64tJtb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 36853,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 36853,
          "cache_creation_input_tokens": 1468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1468
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

_source line 12 · 2026-05-21T21:41:29.467Z_

<details><summary>↩ Tool result · `toolu_019LKfJLaMTuJaLiZgKQsVS3`</summary>

```text
1	{
2	  "exp_id": "exp_062_decoding_strategy_shape",
3	  "project": "gen-depth-fingerprint",
4	  "state": "DONE",
5	  "previous_state": "RUNNING",
6	  "experiment_data": {
7	    "status": "DONE",
8	    "retry_count": 0,
9	    "created_at": "2026-05-21T06:44:08.944Z",
10	    "updated_at": "2026-05-21T21:26:03.841Z",
11	    "hypothesis": "DDR shape stability (entropy_max, entropy_min, tail_decay near-stationary with d<0.15) holds under greedy (temperature=0) and top-k (k=50, τ=0.7) decoding, not just nucleus sampling — verifying the DDR decomposition is decoding-strategy-agnostic",
12	    "spec": {
13	      "command": "python generate_chain_decoding.py --model {pythia-2.8b,olmo-2-1b,qwen3-1.7b} --decoding {greedy,topk}",
14	      "server": "bjb2-18868",
15	      "data_path": "/root/gen-depth-fingerprint/data/seeds_1000.txt",
16	      "data_count": 1000,
17	      "model_name": "pythia-2.8b, olmo-2-1b, qwen3-1.7b",
18	      "seed": 42,
19	      "gpu": "cuda:0,1",
20	      "script_path": "/root/gen-depth-fingerprint/generate_chain_decoding.py",
21	      "checkpoint_path": "/root/gen-depth-fingerprint/data/features_qwen3-8b-topk.csv",
22	      "log_path": "/tmp/gen_qwen8b_topk.log"
23	    },
24	    "conclusion": "success",
25	    "completed_at": "2026-05-21T21:26:03.841Z"
26	  },
27	  "timestamp": "2026-05-21T21:26:03.951790+00:00",
28	  "trigger": "update_registry"
29	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "539e3847-11f8-468c-a6a9-3582946d4377",
  "isSidechain": false,
  "promptId": "8cd44039-612b-4058-80a1-4cde6e090ba1",
  "type": "user",
  "uuid": "a99885d2-e757-460c-bae1-db1fbf6e029d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/checkpoints/exp_062_decoding_strategy_shape_DONE_20260521T212603.json",
      "content": "{\n  \"exp_id\": \"exp_062_decoding_strategy_shape\",\n  \"project\": \"gen-depth-fingerprint\",\n  \"state\": \"DONE\",\n  \"previous_state\": \"RUNNING\",\n  \"experiment_data\": {\n    \"status\": \"DONE\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-21T06:44:08.944Z\",\n    \"updated_at\": \"2026-05-21T21:26:03.841Z\",\n    \"hypothesis\": \"DDR shape stability (entropy_max, entropy_min, tail_decay near-stationary with d<0.15) holds under greedy (temperature=0) and top-k (k=50, τ=0.7) decoding, not just nucleus sampling — verifying the DDR decomposition is decoding-strategy-agnostic\",\n    \"spec\": {\n      \"command\": \"python generate_chain_decoding.py --model {pythia-2.8b,olmo-2-1b,qwen3-1.7b} --decoding {greedy,topk}\",\n      \"server\": \"bjb2-18868\",\n      \"data_path\": \"/root/gen-depth-fingerprint/data/seeds_1000.txt\",\n      \"data_count\": 1000,\n      \"model_name\": \"pythia-2.8b, olmo-2-1b, qwen3-1.7b\",\n      \"seed\": 42,\n      \"gpu\": \"cuda:0,1\",\n      \"script_path\": \"/root/gen-depth-fingerprint/generate_chain_decoding.py\",\n      \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/features_qwen3-8b-topk.csv\",\n      \"log_path\": \"/tmp/gen_qwen8b_topk.log\"\n    },\n    \"conclusion\": \"success\",\n    \"completed_at\": \"2026-05-21T21:26:03.841Z\"\n  },\n  \"timestamp\": \"2026-05-21T21:26:03.951790+00:00\",\n  \"trigger\": \"update_registry\"\n}",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  },
  "sourceToolAssistantUUID": "539e3847-11f8-468c-a6a9-3582946d4377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T21:41:30.220Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018MwqkgF3JrsFPuuaCL22Jn`</summary>

```json
{
  "pattern": "projects/gen-depth-fingerprint/artifacts/dream_reports/**/median/imagined_experiments*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a99885d2-e757-460c-bae1-db1fbf6e029d",
  "isSidechain": false,
  "requestId": "req_011CbGSYSGMo34PHEk8iqoGi",
  "type": "assistant",
  "uuid": "27af6a6c-3e6c-40c0-9cf4-6c1df8163e7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139n9ppGCBamax9VH64tJtb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 36853,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 36853,
          "cache_creation_input_tokens": 1468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1468
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

_source line 14 · 2026-05-21T21:41:30.253Z_

<details><summary>↩ Tool result · `toolu_018MwqkgF3JrsFPuuaCL22Jn`</summary>

```text
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260516T105241/median/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260516T155725/median/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/imagined_experiments.yaml
projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/median/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27af6a6c-3e6c-40c0-9cf4-6c1df8163e7d",
  "isSidechain": false,
  "promptId": "8cd44039-612b-4058-80a1-4cde6e090ba1",
  "type": "user",
  "uuid": "d0f7437d-45d0-4fb6-b30f-f2af02081ddb",
  "toolUseResult": {
    "filenames": [
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260516T105241/median/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260516T155725/median/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/median/imagined_experiments.yaml",
      "projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/median/imagined_experiments.yaml"
    ],
    "durationMs": 30,
    "numFiles": 6,
    "truncated": false
  },
  "sourceToolAssistantUUID": "27af6a6c-3e6c-40c0-9cf4-6c1df8163e7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-21T21:41:30.553Z_

````json
{
  "parentUuid": "d0f7437d-45d0-4fb6-b30f-f2af02081ddb",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**gen-depth-fingerprint**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"gen-depth-fingerprint\")` 或 `load_project_config(\"gen-depth-fingerprint\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[项目]** overall framework参考已发表EMNLP论文的风格，图中的信息密度要高，视觉美观，高度浓缩method部分信息\n- **[项目]** 参考已发表同类文章（如本文是empirical）的写作风格，如用词，写作逻辑，架构，语气，改善本篇的写作，要将整个story讲的高级一些，体现技术深度同时有创新性\n- **[项目]** 附录中的可视化图要嵌入在文字中，出现在论文中需要用到图的附近位置，同时注意latex排版，避免大量空白的存在\n- **[项目]** 图表不要默认在页面的居中位置，前面有留白要及时补齐，动态调整文字和配图（全宽/半宽），同时要注意图片和文字位置的匹配程度\n- **[项目]** 图片要放在文中出现的地方附近，当文中出现大量留白时，调整后面的文字和图片及时向上补齐\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n- **AI Text Detection & Generation Depth — Research Patterns** — Distilled experimental conventions, baselines, metrics, and gaps from 25 papers on AI text detection, model collapse, and content diversity (2019-2026).  →  `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/skills/projects/gen-depth-fingerprint/distilled-research.skill.md`\n- **AI Text Detection & Generation Depth — Writing Patterns** — Distilled narrative strategies, figure/table conventions from 8 deep-read papers on AI text detection and model collapse (ICLR/ICML/ACL 2024-2025).  →  `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/skills/projects/gen-depth-fingerprint/distilled-writing.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/gen-depth-fingerprint/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "5da55bb0-bde0-4a6b-b158-7f00c841e815",
  "timestamp": "2026-05-21T21:41:30.553Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DDR decoding-agnostic 被承认但 reviewer 认为 scope 限制削弱了 generalizability claim，需 rebuttal 或小幅调整后 borderline accept 核心假设：[\"Decoding-agnostic DDR 被认可为有意义的 robus…",
  "leafUuid": "5da55bb0-bde0-4a6b-b158-7f00c841e815",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "DDR decoding-agnostic validation and writing-focused revision",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

### Tool call

_source line 18 · 2026-05-21T21:41:34.601Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K7BSZobSyjpvaA13jpCpZt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5da55bb0-bde0-4a6b-b158-7f00c841e815",
  "isSidechain": false,
  "requestId": "req_011CbGSYjuVwChhCXxjNJMYY",
  "type": "assistant",
  "uuid": "9eb5b586-b43d-4a6a-b37a-76d89c7c0e55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019p2gffXFFpsrRnTHSfLujz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7101,
      "cache_read_input_tokens": 38321,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 38321,
          "cache_creation_input_tokens": 7101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7101
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

_source line 19 · 2026-05-21T21:41:35.281Z_

<details><summary>↩ Tool result · `toolu_01K7BSZobSyjpvaA13jpCpZt`</summary>

```text
1	tier: median
2	narrative_guidance: '深度信号存在但边界模糊。DDR 需从 drifting/stationary 二分法调整为三梯度描述： strong drift
3	  (hapax, TTR)、moderate drift (entropy_mean, entropy_std, entropy_min)、 near-stationary
4	  (tail_decay, entropy_max)。7-feature 优势缩窄至 1.5–3pp， bootstrap 显著但 practical significance
5	  边界化。entropy_mean 在 8B+ 模型上 |ρ| 降至 0.30–0.40，surface features 成为主要信号源。Cross-model
6	  chains 信号温和， 不足以支撑 heterogeneity amplification 叙事。t=0.9 崩溃确认，温度范围需收窄至 [0.5,0.7]。
7	  论文仍适合 Findings 但需补充 architecture-dependent DDR 分析和 scale 衰减曲线。
8	
9	  '
10	imagined_experiments:
11	- name: feature_ablation_and_trend
12	  plan_id: plan_001
13	  description: '三部分分析：(A) Feature ablation：full vs surface-only vs reference-only,
14	    (B) DDR trend analysis per feature, (C) Perplexity pre-validation for Claim 3.
15	
16	    '
17	  expected_results:
18	    full_macro_f1: 0.808
19	    surface_only_f1: 0.757
20	    reference_only_f1: 0.712
21	    ref_vs_surf_bootstrap_ci: '[0.698,0.726] vs [0.742,0.772]'
22	    hapax_ratio_slope: -0.072
23	    hapax_ratio_rho: -0.61
24	    ttr_slope: -0.048
25	    ttr_rho: -0.58
26	    entropy_mean_slope: -0.38
27	    entropy_mean_rho: -0.52
28	    entropy_std_rho: -0.18
29	    entropy_min_rho: -0.31
30	    entropy_max_rho: 0.08
31	    tail_decay_rho: 0.05
32	    median_ppl_by_depth: 13.2, 5.1, 3.1, 2.2, 1.8
33	  result_rationale: 'Median 档下 surface features 仍是主力信号源（hapax, TTR 的 strong drift
34	    使 surface-only 达到 0.757），但 reference features 提供互补信号（full > surface +5.1pp）。 Reference-only
35	    低于 surface-only 约 4.5pp，因为 entropy_mean 的 drift 从 best-case |ρ|>0.60 退化到 moderate
36	    水平（~0.52），entropy_std 和 entropy_min 漂移温和 （|ρ| 0.18–0.31），不再清晰归类为 drifting。三梯度格局成型：strong
37	    drift (hapax -0.61, TTR -0.58) > moderate drift (entropy_mean -0.52, entropy_min
38	    -0.31, entropy_std -0.18) > near-stationary (entropy_max 0.08, tail_decay 0.05)。
39	    Perplexity 按深度单调下降，验证 Claim 3 前提。
40	
41	    '
42	  tables:
43	  - name: 'Table: Feature Ablation (5-fold CV)'
44	    columns:
45	    - Feature Set
46	    - Macro F1
47	    - 95% CI
48	    rows:
49	    - - Full (7 features)
50	      - 0.808
51	      - '[0.795, 0.821]'
52	    - - Surface-only (TTR + hapax)
53	      - 0.757
54	      - '[0.742, 0.772]'
55	    - - Reference-only (5 entropy + tail)
56	      - 0.712
57	      - '[0.698, 0.726]'
58	  - name: 'Table: DDR Gradient Classification'
59	    columns:
60	    - Feature
61	    - Spearman ρ
62	    - Gradient Group
63	    rows:
64	    - - hapax_ratio
65	      - -0.61
66	      - strong drift
67	    - - TTR
68	      - -0.58
69	      - strong drift
70	    - - entropy_mean
71	      - -0.52
72	      - moderate drift
73	    - - entropy_min
74	      - -0.31
75	      - moderate drift
76	    - - entropy_std
77	      - -0.18
78	      - moderate drift
79	    - - entropy_max
80	      - 0.08
81	      - near-stationary
82	    - - tail_decay
83	      - 0.05
84	      - near-stationary
85	  figures_description:
86	  - 7-panel feature trend plot (mean ± std across depth 0–4)：hapax 和 TTR 展示 陡峭单调下降，entropy_mean
87	    展示中等下降但 std 较大，entropy_std/min 呈平缓下降， entropy_max 和 tail_decay 近似水平线。三梯度视觉上清晰可辨。
88	  - Perplexity by depth bar chart：depth 0→4 的 Pythia-410M ppl 单调下降 (13.2→1.8)，支持 location
89	    shift 假说。
90	  analysis: 'McNemar 检验 full vs surface p ≈ 0，full vs reference p ≈ 0，确认互补性。 但 surface-only
91	    已高于 reference-only 4.5pp，表明 vocabulary impoverishment 是主导信号。原始 drifting/stationary
92	    二分法需修改：entropy_std 的 |ρ|=0.18 落在灰色地带（既非清晰 drifting 也非 stationary），需引入 moderate
93	    drift 类别。 论文 Claim 2 的叙事从 "dual dynamics" 调整为 "gradient of depth sensitivity"。
94	
95	    '
96	- name: cross_generator_evaluation
97	  plan_id: plan_002
98	  description: '扩展至 5 generators（Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B），
99	    LOGO 和 LOFO 评估。
100	
101	    '
102	  expected_results:
103	    total_records: 22800
104	    logo_avg_macro_f1: 0.788
105	    logo_avg_binary_f1: 0.675
106	    logo_binary_ci: '[0.662, 0.688]'
107	    lofo_binary_f1: 0.652
108	    per_gen_binary_f1:
109	      pythia_2_8b: 0.71
110	      pythia_1b: 0.715
111	      olmo_2_1b: 0.66
112	      qwen3_1_7b: 0.668
113	      qwen3_0_6b: 0.62
114	    per_gen_binary_f1_range_pp: 9.5
115	    family_out_delta: 0.023
116	  result_rationale: 'Median 档下 LOGO binary F1 落在 [0.66, 0.69] 范围中部（0.675）。Pythia 家族
117	    两个模型（2.8B, 1B）因与 Pythia-410M reference 同源而获得轻微优势（0.710–0.715）， OLMo 和 Qwen 因 architecture
118	    差异表现更低。per-gen 方差约 9.5pp，符合 median 档 10–15pp 预期的下界。LOFO binary F1（0.652）低于 LOGO
119	    约 2.3pp，因为 leave-one-family-out 移除整个 Pythia 家族（两个模型）时训练集覆盖度下降。Qwen3-0.6B 最低因为
120	    模型容量小导致生成文本多样性本身受限，depth drift 信号被压缩。
121	
122	    '
123	  tables:
124	  - name: 'Table: LOGO Per-Generator Binary F1'
125	    columns:
126	    - Generator
127	    - Binary F1
128	    - 95% CI
129	    - Family
130	    rows:
131	    - - Pythia-2.8B
132	      - 0.71
133	      - '[0.692, 0.728]'
134	      - Pythia
135	    - - Pythia-1B
136	      - 0.715
137	      - '[0.697, 0.733]'
138	      - Pythia
139	    - - OLMo-2-1B
140	      - 0.66
141	      - '[0.641, 0.679]'
142	      - OLMo
143	    - - Qwen3-1.7B
144	      - 0.668
145	      - '[0.649, 0.687]'
146	      - Qwen
147	    - - Qwen3-0.6B
148	      - 0.62
149	      - '[0.600, 0.640]'
150	      - Qwen
151	  figures_description:
152	  - Per-generator LOGO binary F1 bar chart with CI whiskers，按 family 着色。 Pythia 家族明显高于其他
153	    family，展示 reference model bias。
154	  - LOFO confusion matrix heatmap：leave-Pythia-out 条件下 gen-1 vs gen-2+ 混淆 集中，leave-Qwen-out
155	    条件下性能最高。
156	  analysis: 'Per-gen F1 range 9.5pp 处于 median 预期下界，reviewers 可能质疑 generalizability。
157	    需逐 generator 报告并承认 Pythia-as-reference 的 family bias。LOFO 下降 2.3pp 表明 cross-family
158	    transfer 存在但有衰减。论文需将 headline metric 从单一 F1 改为 range 报告（0.620–0.715）。
159	
160	    '
161	- name: cross_family_reference_model
162	  plan_id: plan_003
163	  description: '测试 OLMo-2-1B 和 Qwen3-0.6B 作为 reference model 时 DDR 是否持续。
164	
165	    '
166	  expected_results:
167	    logo_f1_pythia_ref: 0.788
168	    logo_f1_olmo_ref: 0.78
169	    logo_f1_qwen_ref: 0.795
170	    entropy_drift_all_refs_negative: true
171	    pythia_ref_entropy_mean_rho: -0.52
172	    olmo_ref_entropy_mean_rho: -0.44
173	    qwen_ref_entropy_mean_rho: -0.48
174	    olmo_ref_drift_range:
175	    - -0.44
176	    - -0.78
177	    qwen_ref_drift_range:
178	    - -0.48
179	    - -0.85
180	    pythia_ref_drift_range:
181	    - -0.52
182	    - -0.92
183	    dual_dynamics_is_pythia_artifact: false
184	    tail_decay_rho_all_refs_abs_max: 0.09
185	  result_rationale: 'Median 档下 DDR 不是 Pythia 特有现象（drift 方向一致），但 entropy_mean |ρ| 跨
186	    reference model 有明显波动（0.44–0.52），不再稳定超过 0.55。三个 ref 的 LOGO F1 差异 <1.5pp，说明 classifier
187	    性能对 reference 选择不敏感，但 DDR 分析的具体数值（ρ magnitude）取决于 reference-generator 对。Qwen ref
188	    略高 因为 Qwen 家族的 entropy 分布与多数 generator 有更好的判别力。tail_decay 和 entropy_max 在所有 ref
189	    下保持 near-stationary（|ρ| < 0.10），确认 shape features 的稳健性是跨 reference 的。DDR 三梯度结构跨
190	    reference 稳定，但 moderate drift 组的具体 ρ 值波动 ±0.08。
191	
192	    '
193	  tables:
194	  - name: 'Table: Reference Model Comparison'
195	    columns:
196	    - Reference Model
197	    - LOGO F1
198	    - entropy_mean ρ
199	    - tail_decay ρ
200	    rows:
201	    - - Pythia-410M
202	      - 0.788
203	      - -0.52
204	      - 0.05
205	    - - OLMo-2-1B
206	      - 0.78
207	      - -0.44
208	      - 0.07
209	    - - Qwen3-0.6B
210	      - 0.795
211	      - -0.48
212	      - 0.04
213	  figures_description:
214	  - 3×7 heatmap：每个 reference model 下 7 个 feature 的 Spearman ρ。颜色编码 三梯度（deep red =
215	    strong drift, orange = moderate, gray = stationary）。 跨行模式一致但 moderate drift 列色调有波动。
216	  analysis: 'DDR 非 Pythia artifact——方向一致、三梯度结构跨 ref 稳定。但 entropy_mean 的 |ρ| 在 non-Pythia
217	    ref 下降至 0.44，接近 drifting/moderate 边界。论文应报告 所有三个 ref 的 ρ range 而非挑选最佳值。这支持将 entropy_mean
218	    归入 moderate drift 而非 strong drift，进一步支持三梯度叙事。
219	
220	    '
221	- name: downstream_utility
222	  plan_id: plan_004
223	  description: 'OLMo-1B fine-tune on depth-stratified data，3 seeds，bootstrap CIs，
224	    sample-count-matched control。
225	
226	    '
227	  expected_results:
228	    all_ppl_mean: 2.34
229	    all_ppl_ci: '[2.336, 2.344]'
230	    size_matched_ppl_mean: 2.37
231	    size_matched_ppl_ci: '[2.366, 2.374]'
232	    depth01_ppl_mean: 2.39
233	    depth01_ppl_ci: '[2.386, 2.394]'
234	    binary_filtered_ppl_mean: 2.393
235	    binary_filtered_ppl_ci: '[2.389, 2.397]'
236	    depth0_only_ppl_mean: 2.685
237	    depth0_only_ppl_ci: '[2.680, 2.690]'
238	    ranking: all < size_matched < depth01 ≈ binary_filtered << depth0_only
239	    tost_2pct_p: 0.00012
240	    tost_1pct_p: 0.087
241	    seed_variance: <0.003 within variant
242	    cohens_d_depth01_vs_matched: 0.42
243	  result_rationale: 'Median 档下 Claim 3 的 negative finding 完全成立。depth-aware filtering
244	    不优于 random subsampling（size_matched 2.370 vs depth01 2.390），因为 depth filtering
245	    移除的深层文本虽然 perplexity 更低，但其信息内容仍有训练价值。TOST 在 ±2% margin 下显著（p=0.00012），但 ±1% margin
246	    下不显著（p=0.087），说明等价性 在实际层面成立但统计精度受限于 3 seeds。seed 间方差极小（<0.003），印证 OLMo-1B fine-tune
247	    的稳定性。depth0_only 显著差因为纯人工文本量不足（仅 ~800 训练样本），这是数据量效应而非深度质量效应。Cohen''s d=0.42 中等偏小，
248	    TOST 是更合适的检验。
249	
250	    '
251	  tables:
252	  - name: 'Table: Downstream CLM Quality by Training Data Composition'
253	    columns:
254	    - Variant
255	    - Train Size
256	    - Ppl (mean ± std)
257	    - TOST p (±2%)
258	    rows:
259	    - - All depths
260	      - 12299
261	      - 2.340 ± 0.003
262	      - —
263	    - - Size-matched random
264	      - 3951
265	      - 2.370 ± 0.003
266	      - ref
267	    - - Depth 0+1 only
268	      - 3951
269	      - 2.390 ± 0.003
270	      - 0.00012
271	    - - Binary-filtered
272	      - 3951
273	      - 2.393 ± 0.003
274	      - 9.0e-05
275	    - - Depth 0 only
276	      - 797
277	      - 2.685 ± 0.004
278	      - <0.001 (reject eq.)
279	  figures_description:
280	  - Bar chart with ppl per variant，3 seeds 显示为抖动点。all 和 size_matched 之间的 gap 归因于数据量，depth01
281	    和 binary_filtered 几乎重叠。
282	  - TOST margin sensitivity plot：x 轴 margin (±1%–5%)，y 轴 rejection p-value。 ±2% 处
283	    p 跌破 0.05 临界线。
284	  analysis: 'Negative finding 稳健。Depth-aware curation 不改善下游 CLM 质量，depth fingerprinting
285	    定位为 diagnostic 而非 curative 工具。论文 Claim 3 在 median 档下无需修改措辞， 是最稳定的 claim。
286	
287	    '
288	- name: prompt_type_comparison
289	  plan_id: plan_005
290	  description: 'Continuation vs elaboration vs inspired_rewriting chains，Pythia-2.8B，1000
291	    seeds。
292	
293	    '
294	  expected_results:
295	    cv_f1_continuation: 0.773
296	    cv_f1_elaboration: 0.723
297	    cv_f1_rewriting: 0.733
298	    lopto_avg_f1: 0.748
299	    lopto_held_out_cont: 0.758
300	    lopto_held_out_elab: 0.755
301	    lopto_held_out_rewrite: 0.728
302	    depth_retention_d4_d0:
303	      continuation: 0.835
304	      elaboration: 0.984
305	      rewriting: 0.938
306	    drift_hapax_continuation: -0.72
307	    drift_hapax_elaboration: -0.81
308	    drift_hapax_rewriting: -0.78
309	    drift_entropy_mean_continuation: -0.5
310	    drift_entropy_mean_elaboration: -0.43
311	    drift_entropy_mean_rewriting: -0.45
312	  result_rationale: 'Median 档下 continuation 信号最强（0.773）因为每步生成从前文直接续写， 累积的 lexical
313	    diversity 压缩最显著。Elaboration 最弱（0.723）因为 elaboration prompt 给模型更多自由度，保留了更多词汇多样性。但三种
314	    prompt 类型的差距 仅 ~5pp（而非 best-case 下的 7pp），因为在 median 档下 entropy_mean 的 drift magnitude
315	    已整体缩小，各 prompt 类型间的 drift 差异也随之缩小。Elaboration 的 depth retention 极高（0.984）意味着几乎不丢失链条，但深度信号更弱——
316	    这是 semantic divergence 与 depth discriminability 的 tradeoff。LOPTO (leave-one-prompt-type-out)
317	    显示 cross-prompt transfer 合理（avg 0.748）， 但 held-out rewriting 略低因其 drift 特征介于两端。
318	
319	    '
320	  tables:
321	  - name: 'Table: Prompt-Type CV F1 Comparison'
322	    columns:
323	    - Prompt Type
324	    - CV F1
325	    - Depth Retention (d4/d0)
326	    - hapax ρ
327	    - entropy_mean ρ
328	    rows:
329	    - - Continuation
330	      - 0.773
331	      - 0.835
332	      - -0.72
333	      - -0.5
334	    - - Inspired Rewriting
335	      - 0.733
336	      - 0.938
337	      - -0.78
338	      - -0.45
339	    - - Elaboration
340	      - 0.723
341	      - 0.984
342	      - -0.81
343	      - -0.43
344	  figures_description:
345	  - 3-panel feature drift plot（每行一种 prompt 类型）：continuation 的 hapax/TTR 斜率最陡，elaboration
346	    的 entropy_mean 斜率最平。可视化 semantic freedom 与 depth signal 的反向关系。
347	  analysis: 'Continuation 最适合 depth fingerprinting，elaboration 最弱。论文报告 continuation
348	    0.773 vs elaboration 0.723（+5.0pp），prompt-type 依赖性存在 但可控。Median 档下差异缩小意味着论文措辞应用
349	    "moderate prompt-type dependence" 而非 "strong"。
350	
351	    '
352	- name: paraphrastic_comparison
353	  plan_id: plan_006
354	  description: '构建 paraphrasing chains（语义保持的改写链）与 continuation chains 直接对比， 测试 attractor
355	    convergence theory。
356	
357	    '
358	  expected_results:
359	    paraphrastic_cv_binary_f1: 0.585
360	    paraphrastic_ci: '[0.565, 0.605]'
361	    continuation_cv_binary_f1: 0.682
362	    continuation_ci: '[0.665, 0.699]'
363	    delta_pp: 9.7
364	    paraphrastic_hapax_rho: -0.28
365	    paraphrastic_entropy_mean_rho: -0.15
366	    paraphrastic_attractor_convergence_depth: 2.8
367	    continuation_attractor_convergence_depth: '>4'
368	    paraphrastic_depth_retention_d4_d0: 0.96
369	  result_rationale: 'Paraphrastic chains 因 semantic preservation 约束而快速收敛到 attractor
370	    state， 深度信号在 depth 2–3 后基本消失（|ρ| 从 depth 0-1 的 0.28 降至 depth 3-4 的 < 0.10）。这与
371	    ACL 2025 "LLM as Broken Telephone" 的 attractor cycle theory 一致： paraphrasing 约束将分布锁定在
372	    ~3-class 分辨率上界。Continuation chains 因无 semantic 约束，diversity 持续压缩，depth signal
373	    延伸到 depth 4+。二者差距 9.7pp （median 档，best-case 可能更大）确认了 non-paraphrastic chains 是更有前途的
374	    depth estimation 场景。但 median 档下 continuation 本身也只有 0.682（LOGO）， 所以 paraphrastic
375	    的 0.585 已接近 chance-level 对于 binary classification。
376	
377	    '
378	  tables:
379	  - name: 'Table: Paraphrastic vs Continuation Chains'
380	    columns:
381	    - Chain Type
382	    - Binary F1
383	    - hapax ρ
384	    - entropy_mean ρ
385	    - Attractor Convergence
386	    rows:
387	    - - Continuation
388	      - 0.682
389	      - -0.61
390	      - -0.5
391	      - '>depth 4'
392	    - - Paraphrastic
393	      - 0.585
394	      - -0.28
395	      - -0.15
396	      - ~depth 2.8
397	  figures_description:
398	  - Feature drift trajectory comparison：两条线（continuation vs paraphrastic） 叠加，x 轴 depth
399	    0–4，y 轴 normalized feature value。Paraphrastic 线在 depth 2–3 趋平，continuation 线持续下降。
400	  analysis: 'Paraphrastic chains 的 attractor convergence 确认我们的 contribution scope：
401	    non-paraphrastic chains 是 DDR 的核心场景。论文 Related Work 需与 ACL 2025 attractor theory
402	    对话。Median 档下 paraphrastic F1 仍显著高于 random（0.50）， 说明即使在 attractor 约束下 depth 1 vs
403	    depth 2+ 仍有微弱信号。
404	
405	    '
406	- name: cross_model_chains
407	  plan_id: plan_007
408	  description: 'Cross-model chains（每步不同 generator），与 single-model chains 对比。
409	
410	    '
411	  expected_results:
412	    cross_model_binary_f1: 0.73
413	    cross_model_binary_ci: '[0.71, 0.75]'
414	    cross_model_3class_f1: 0.72
415	    single_model_logo_binary_f1: 0.675
416	    delta_cross_vs_single_pp: 5.5
417	    cross_model_hapax_rho: -0.54
418	    cross_model_entropy_mean_rho: -0.4
419	    per_chain_composition_variance: 0.03
420	  result_rationale: 'Median 档下 cross-model chains 的 binary F1 为 0.73，落在指定区间 [0.70,
421	    0.76] 中部。Cross-model chains 的 F1 高于 single-model LOGO（0.675）约 5.5pp， 原因是不同 generator
422	    间的 architecture 差异引入额外的 distributional shift， 叠加在 depth-intrinsic drift 之上。但这个
423	    amplification 是温和的（+5.5pp 而非 best-case 的 +13.6pp），因为 median 档下 architecture-dependent
424	    DDR 意味着部分 generator 组合（如两个 Qwen 模型相邻）的 architecture shift 很小。 entropy_mean ρ 在
425	    cross-model 链中降至 -0.40（单模型下 -0.52），因为 reference model 对不同 architecture 的 entropy
426	    估计不一致。hapax/TTR 的 surface features 受 architecture shift 影响更小（-0.54 vs -0.61），再次确认
427	    surface features 在 median 档下的相对优势。
428	
429	    '
430	  tables:
431	  - name: 'Table: Cross-Model vs Single-Model Chains'
432	    columns:
433	    - Chain Type
434	    - Binary F1
435	    - 3-class F1
436	    - hapax ρ
437	    - entropy_mean ρ
438	    rows:
439	    - - Cross-model (5-gen mix)
440	      - 0.73
441	      - 0.72
442	      - -0.54
443	      - -0.4
444	    - - Single-model (LOGO avg)
445	      - 0.675
446	      - 0.788
447	      - -0.61
448	      - -0.52
449	  figures_description:
450	  - Cross-model chain construction diagram：展示 5 generators 如何在不同 depth 层被随机分配。附 per-composition
451	    binary F1 violin plot。
452	  analysis: 'Cross-model 信号温和（0.73），不足以支撑 "heterogeneity amplification" 的强叙事。 论文需将
453	    framing 从 "heterogeneity amplifies depth signal" 改为 "heterogeneous chains remain
454	    detectable, with moderate amplification from architecture mixing"。 Median 档下这是一个稳健但不戏剧化的
455	    finding。
456	
457	    '
458	- name: multi_domain_seeds
459	  plan_id: plan_008
460	  description: '扩展至 4 domains：Wikipedia, news, scientific, creative writing。
461	
462	    '
463	  expected_results:
464	    wikipedia_binary_f1: 0.692
465	    news_binary_f1: 0.675
466	    news_ci: '[0.655, 0.695]'
467	    academic_binary_f1: 0.648
468	    academic_ci: '[0.628, 0.668]'
469	    creative_binary_f1: 0.66
470	    creative_ci: '[0.640, 0.680]'
471	    max_gap_vs_wiki_pp: 4.4
472	    cross_domain_logo_binary_f1: 0.665
473	    worst_domain: academic
474	  result_rationale: 'Median 档下各 domain 的 binary F1 落在 0.648–0.692，max gap 约 4.4pp。
475	    Wikipedia 最高因为 Wikipedia 文本结构相对均匀，depth drift 信号最 consistent。 Academic 最低因为科学文本的
476	    vocabulary 本身 specialized 且 diversity 较低（高频 术语复用），depth-induced vocabulary compression
477	    与 domain-intrinsic low diversity 混淆。Creative writing 和 news 居中。Cross-domain LOGO（train
478	    on 3 domains, test on held-out domain）为 0.665，接近 overall LOGO，说明 depth signal
479	    是 domain-robust 的。差异 <5pp 足以在论文中 claim "domain independence"， 但需逐 domain 报告并讨论
480	    academic domain 的特殊性。
481	
482	    '
483	  tables:
484	  - name: 'Table: Multi-Domain Binary F1'
485	    columns:
486	    - Domain
487	    - Binary F1
488	    - 95% CI
489	    - Seed Count
490	    rows:
491	    - - Wikipedia
492	      - 0.692
493	      - '[0.672, 0.712]'
494	      - 500
495	    - - News
496	      - 0.675
497	      - '[0.655, 0.695]'
498	      - 500
499	    - - Creative
500	      - 0.66
501	      - '[0.640, 0.680]'
502	      - 500
503	    - - Academic
504	      - 0.648
505	      - '[0.628, 0.668]'
506	      - 500
507	  figures_description:
508	  - Per-domain feature drift comparison：4 个 domain 的 hapax_ratio drift 线 基本平行（slope
509	    相近），但 academic domain 的 intercept 更低（初始 diversity 就低），解释其 F1 略低。
510	  analysis: 'Depth signal 跨 domain 稳健，最大差距 4.4pp。论文可 claim domain independence 但需报告
511	    academic domain 的 ceiling 效应。Median 档下 creative writing 没有 出现特殊行为，消除了 "creative
512	    writing harder" 的担忧。
513	
514	    '
515	- name: finer_grained_ordinal
516	  plan_id: plan_009
517	  description: '5-class ordinal classification（gen-0 through gen-4），CORAL 和 Frank-Hall
518	    ordinal methods vs standard XGBoost。
519	
520	    '
521	  expected_results:
522	    xgboost_5class_f1: 0.495
523	    coral_5class_f1: 0.498
524	    frank_hall_5class_f1: 0.492
525	    xgboost_3class_f1: 0.788
526	    gen1_vs_gen2_confusion_rate: 0.43
527	    gen2_vs_gen3_confusion_rate: 0.52
528	    gen3_vs_gen4_confusion_rate: 0.58
529	    binary_fn_concentration: 0.85
530	  result_rationale: 'Median 档下 5-class F1 降至 ~0.495，ordinal methods 无改善（±0.3pp）。 Gen-1/gen-2
531	    边界是 bottleneck（43% confusion），gen-2/gen-3 和 gen-3/gen-4 更差（52% 和 58%）。原因是 DDR
532	    在 median 档下的 moderate drift features （entropy_mean, entropy_std, entropy_min）在深度
533	    2+ 后的 marginal change 很小， feature space 中 gen-2/3/4 高度重叠。Surface features (hapax,
534	    TTR) 虽 drift 更强但也在 depth 3+ 趋于饱和。Ordinal methods 理论上应利用深度顺序性，但 因为 feature space
535	    本身在 depth 2+ 后分辨力不足，ordinal constraint 无法提供 额外信号。3-class 是 practical ceiling，5-class
536	    只在 gen-0 identification 上有效（gen-0 F1 ~0.95），deeper classes 全部混淆。86% 的 binary errors
537	    集中在 FN（gen-2+ 被误判为 gen-1），说明模型在 depth boundary 上的主要失败 是 miss 而非 false alarm。
538	
539	    '
540	  tables:
541	  - name: 'Table: Ordinal Granularity Comparison'
542	    columns:
543	    - Method
544	    - 5-class F1
545	    - 3-class F1
546	    - ΔF1
547	    rows:
548	    - - XGBoost (standard)
549	      - 0.495
550	      - 0.788
551	      - -0.293
552	    - - CORAL
553	      - 0.498
554	      - —
555	      - —
556	    - - Frank-Hall
557	      - 0.492
558	      - —
559	      - —
560	  figures_description:
561	  - 5-class confusion matrix heatmap：gen-0 几乎完美分类（对角线深色），gen-1 有中等混淆，gen-2/3/4 的三行几乎互相混淆（off-diagonal
562	    色块密集）。
563	  analysis: '3-class 是 resolution ceiling，ordinal methods 无额外增益。论文应明确报告 这个负面结果，定位
564	    3-class 为 "practical resolution limit"。这其实加强了 论文叙事：gen-1 vs gen-2+ 的二分法在 median
565	    档下仍有意义，更细粒度不现实。
566	
567	    '
568	- name: human_edit_robustness
569	  plan_id: plan_010
570	  description: '模拟人工编辑鲁棒性：(A) Random word replacement，(B) LLM-simulated rephrasing。
571	
572	    '
573	  expected_results:
574	    baseline_binary_f1: 0.68
575	    random_5pct_f1: 0.636
576	    random_5pct_drop: -0.044
577	    random_10pct_f1: 0.602
578	    random_10pct_drop: -0.078
579	    random_20pct_f1: 0.575
580	    random_20pct_drop: -0.105
581	    llm_rephrase_f1: 0.632
582	    llm_rephrase_drop: -0.048
583	    llm_rephrase_ci: '[0.612, 0.652]'
584	    edit_distance_ratio: 0.5
585	  result_rationale: 'Median 档下 LLM rephrase drop 为 4.8pp，落在指定区间 [4.0, 7.0] 的下半部。 Random
586	    replacement 5% 与 LLM rephrase 的 drop 相近（~4.4–4.8pp），因为 5% 随机替换对 vocabulary diversity
587	    features（hapax, TTR）的扰动与 LLM 对 ~1.7 句的 rephrasing 对 diversity 的影响量级相当。10% 和 20%
588	    replacement 的更大 drop 主要来自 surface features 的破坏：随机插入的词汇增加了 hapax count， 部分抵消了 depth-induced
589	    diversity compression 信号。LLM rephrase 的影响 更 "intelligent"——它倾向于同义替换而非随机词，所以保留了更多
590	    distributional structure。20% replacement 后仍有 0.575（>0.50 random），说明 depth signal
591	    在重度编辑下仍有微弱残留。论文需在附录中报告，承认 moderate robustness。
592	
593	    '
594	  tables:
595	  - name: 'Table: Robustness to Simulated Editing'
596	    columns:
597	    - Edit Type
598	    - Binary F1
599	    - Drop (pp)
600	    - 95% CI
601	    rows:
602	    - - None (baseline)
603	      - 0.68
604	      - —
605	      - '[0.663, 0.697]'
606	    - - Random 5%
607	      - 0.636
608	      - -4.4
609	      - '[0.618, 0.654]'
610	    - - Random 10%
611	      - 0.602
612	      - -7.8
613	      - '[0.583, 0.621]'
614	    - - Random 20%
615	      - 0.575
616	      - -10.5
617	      - '[0.556, 0.594]'
618	    - - LLM rephrase
619	      - 0.632
620	      - -4.8
621	      - '[0.612, 0.652]'
622	  figures_description:
623	  - Robustness degradation curve：x 轴 edit intensity（0%, 5%, 10%, 20%, LLM）， y 轴 binary
624	    F1。LLM rephrase 标注为菱形点，与 random 5% 高度接近。
625	  analysis: 'Signal 在 moderate editing 下尚存但降解显著。论文定位为 "robust to light editing, degrades
626	    gracefully under heavier perturbation"。LLM rephrase drop 4.8pp 在 median 档预期内，reviewers
627	    不太会以此否定方法但会要求讨论 ecological validity。
628	
629	    '
630	- name: ld_score_feature
631	  plan_id: plan_011
632	  description: '添加 LD-Score（character-level distribution signature）作为第 8 个 feature。
633	
634	    '
635	  expected_results:
636	    eight_feat_cv_f1: 0.798
637	    seven_feat_cv_f1: 0.788
638	    delta_pp: 1.0
639	    ld_score_alone_rho: -0.42
640	    ld_score_xgb_importance: 0.045
641	    ld_score_spearman_with_hapax: 0.72
642	  result_rationale: 'Median 档下 LD-Score 提供了 +1.0pp 的 marginal gain，统计显著但实际增益微小。 LD-Score
643	    与 hapax_ratio 的 Spearman 相关高达 0.72——两者都捕获 lexical diversity 的不同侧面（word-level vs
644	    character-level），信号高度冗余。LD-Score 单独的 ordinal ρ 为 -0.42，介于 moderate drift 组。在 XGBoost
645	    importance 中仅排第 6 位（0.045），被 hapax, TTR, entropy_mean 远远压过。增加 LD-Score 不改变论文叙事，
646	    但可作为 "character-level signal also exhibits depth drift" 的补充证据。 论文选择保持 7-feature
647	    设计并在附录报告 LD-Score，避免增加模型复杂度。
648	
649	    '
650	  tables:
651	  - name: 'Table: LD-Score as Additional Feature'
652	    columns:
653	    - Feature Set
654	    - CV F1
655	    - Δ vs 7-feat
656	    rows:
657	    - - 7 features
658	      - 0.788
659	      - —
660	    - - 7 features + LD-Score
661	      - 0.798
662	      - +1.0pp
663	    - - LD-Score alone
664	      - 0.682
665	      - -10.6pp
666	  figures_description:
667	  - Feature correlation heatmap including LD-Score：LD-Score 与 hapax_ratio 的 色块最深（r=0.72），视觉上解释冗余性。
668	  analysis: 'LD-Score 的 marginal value 有限（+1pp），不值得增加 feature set 复杂度。 但 character-level
669	    depth drift 的存在本身有学术价值，作为 DDR 跨 granularity 的佐证。论文附录报告。
670	
671	    '
672	- name: end_to_end_classifier
673	  plan_id: plan_012
674	  description: 'QLoRA fine-tuned end-to-end classifier vs handcrafted 7-feature model。
675	
676	    '
677	  expected_results:
678	    qlora_3class_cv_f1: 0.882
679	    qlora_3class_ci: '[0.870, 0.894]'
680	    qlora_binary_cv_f1: 0.84
681	    qlora_binary_ci: '[0.825, 0.855]'
682	    qlora_5class_cv_f1: 0.565
683	    seven_feat_3class_cv_f1: 0.788
684	    seven_feat_binary_cv_f1: 0.68
685	    delta_3class_pp: 9.4
686	    delta_binary_pp: 16.0
687	    qlora_logo_binary_f1: 0.62
688	    qlora_gpu_memory_gb: 8.5
689	    qlora_inference_time_ratio: 12.4
690	  result_rationale: 'QLoRA within-distribution performance 显著高于 7-feature（3-class
691	    +9.4pp， binary +16pp），因为 end-to-end model 可以学到 handcrafted features 未捕获的 fine-grained
692	    distributional patterns（如 specific n-gram frequency shifts， positional entropy
693	    patterns）。但 LOGO generalization（0.62）大幅低于 within-distribution（0.840），暴露了 end-to-end
694	    model 对 generator-specific artifacts 的过拟合。7-feature model 的 LOGO vs CV drop 更小（~10pp
695	    vs ~22pp）， 因为 handcrafted features 是 generator-agnostic 的 distributional statistics。
696	    5-class QLoRA（0.565）仍低，确认 resolution ceiling 非 feature engineering 问题 而是 task
697	    intrinsic。推理成本 12.4× 和 8.5GB GPU memory 使 QLoRA 在实际部署中 不 competitive。论文定位 7-feature
698	    的优势为 "efficiency + generalization"。
699	
700	    '
701	  tables:
702	  - name: 'Table: End-to-End vs Handcrafted Features'
703	    columns:
704	    - Method
705	    - CV 3-class
706	    - CV Binary
707	    - LOGO Binary
708	    - Inference Cost
709	    rows:
710	    - - 7-feature XGBoost
711	      - 0.788
712	      - 0.68
713	      - 0.675
714	      - 1×
715	    - - QLoRA Qwen3-0.6B
716	      - 0.882
717	      - 0.84
718	      - 0.62
719	      - 12.4×
720	  figures_description:
721	  - Radar chart：4 维比较（CV F1, LOGO F1, inference cost, memory usage）， 7-feature 在 LOGO
722	    和效率维度占优，QLoRA 在 within-dist 占优。
723	  analysis: 'QLoRA 的 within-dist 优势不能 transfer 到 unseen generators，而这恰好是 depth fingerprinting
724	    的核心应用场景。7-feature model 的 LOGO 优势（0.675 vs 0.62）在 median 档下并不巨大（+5.5pp），但加上 12.4×
725	    的成本差异，efficiency argument 成立。论文可用 QLoRA 作为 upper bound reference，强调 7-feature
726	    的 "right tradeoff"。
727	
728	    '
729	- name: text_length_control
730	  plan_id: plan_013
731	  description: 'Text length confound analysis：长度相关性、length-normalized features、 length-matched
732	    re-evaluation。
733	
734	    '
735	  expected_results:
736	    spearman_length_depth: 0.11
737	    spearman_ci: '[-0.06, 0.14]'
738	    length_is_confound: false
739	    normalized_ttr_trend_preserved: true
740	    normalized_hapax_trend_preserved: true
741	    normalized_rho_stronger: true
742	    length_matched_binary_f1: 0.652
743	    unmatched_binary_f1: 0.68
744	    delta_pp: -2.8
745	    dropout_short_text_bias: true
746	  result_rationale: 'Median 档下 length-depth Spearman ρ 仅 0.11，text length 不是 depth
747	    signal 的主要驱动因素。Length normalization 后 TTR 和 hapax 的 depth drift 反而更强 （normalized
748	    ρ stronger），因为去除了 length variation 带来的噪声。 Length-matched subsampling 导致 F1 下降
749	    2.8pp（0.680→0.652），但这主要来自 样本量减少（matching 丢弃了 ~30% 的数据）而非 length confound 移除。 Random
750	    subsample control 可验证这一点。Depth-driven dropout 偏向短文本 （deeper generation 产生更多空/短输出被
751	    skipped），但这是 generation process 的 intrinsic 特性而非统计 confound。论文可自信地排除 length confound。
752	
753	    '
754	  tables:
755	  - name: 'Table: Length Confound Analysis'
756	    columns:
757	    - Metric
758	    - Value
759	    - Conclusion
760	    rows:
761	    - - Spearman ρ(length, depth)
762	      - 0.11
763	      - Weak (|ρ|<0.15)
764	    - - Length-matched binary F1
765	      - 0.652
766	      - −2.8pp from unmatched
767	    - - Random subsample F1 (same n)
768	      - 0.656
769	      - Similar drop → sample size effect
770	    - - Normalized TTR drift preserved?
771	      - 'Yes'
772	      - Depth signal independent of length
773	  figures_description:
774	  - Length distribution violin plot by depth (0–4)：各 depth 的 length 分布 高度重叠，仅 depth
775	    4 有轻微 left shift（shorter texts）。
776	  analysis: 'Length confound 排除。这是 paper credibility 的关键支撑。Median 档下 结论清晰，无需 hedge。
777	
778	    '
779	- name: large_scale_generator
780	  plan_id: plan_014
781	  description: '添加 Qwen3-8B-Base 测试 scale effect on depth signal。
782	
783	    '
784	  expected_results:
785	    total_records: 4500
786	    logo_6gen_avg_f1: 0.672
787	    logo_qwen3_8b_held_out_binary_f1: 0.615
788	    logo_qwen3_8b_ci: '[0.595, 0.635]'
789	    logo_5gen_baseline_f1: 0.675
790	    spearman_hapax: -0.5
791	    spearman_ttr: -0.49
792	    spearman_entropy_mean: -0.36
793	    spearman_entropy_std: -0.08
794	    spearman_entropy_max: 0.07
795	    spearman_tail_decay: -0.06
796	    feature_importance_hapax: 0.28
797	    feature_importance_ttr: 0.17
798	    feature_importance_entropy_mean: 0.14
799	  result_rationale: 'Median 档下 Qwen3-8B held-out binary F1 为 0.615，落在指定区间 [0.58, 0.65]
800	    中部。大模型生成的文本更 fluent、vocabulary 更 diverse、perplexity 更 uniform， 压缩了 depth drift
801	    的 margin。entropy_mean |ρ| 从 5-gen avg 的 ~0.52 降至 0.36， 因为 8B 模型的 next-token entropy
802	    分布更窄、depth-induced shift 更小。 Surface features（hapax -0.50, TTR -0.49）的衰减幅度小于 entropy
803	    features， 因为 vocabulary diversity compression 是 depth-intrinsic 的物理过程，不受 model
804	    capacity 影响——更大的模型仍然会在 recursive generation 中累积 lexical convergence。这进一步支持 median
805	    档的核心主题：surface features 在 scale 增大时成为更重要的信号源。6-gen LOGO（含 8B）avg F1 0.672 vs 5-gen
806	    baseline 0.675，8B 的加入仅轻微拉低整体。
807	
808	    '
809	  tables:
810	  - name: 'Table: Scale Effect — DDR by Model Size'
811	    columns:
812	    - Generator
813	    - Size
814	    - Binary F1
815	    - hapax ρ
816	    - entropy_mean ρ
817	    rows:
818	    - - Qwen3-0.6B
819	      - 0.6B
820	      - 0.62
821	      - -0.58
822	      - -0.52
823	    - - Pythia-1B
824	      - 1B
825	      - 0.715
826	      - -0.63
827	      - -0.54
828	    - - OLMo-2-1B
829	      - 1.5B
830	      - 0.66
831	      - -0.6
832	      - -0.5
833	    - - Qwen3-1.7B
834	      - 1.7B
835	      - 0.668
836	      - -0.59
837	      - -0.49
838	    - - Pythia-2.8B
839	      - 2.8B
840	      - 0.71
841	      - -0.61
842	      - -0.52
843	    - - Qwen3-8B
844	      - 8B
845	      - 0.615
846	      - -0.5
847	      - -0.36
848	  figures_description:
849	  - Scale-DDR scatter plot：x 轴 log(model size)，y 轴 |ρ|。两条线： hapax（红，平缓下降）和 entropy_mean（蓝，陡峭下降）。8B
850	    处两线明显分叉。 灰色 band 标注 stationary features 始终在 |ρ|<0.10 区域。
851	  analysis: 'Scale effect 确认：entropy_mean drift 在 8B 处显著衰减（|ρ| 0.36 vs avg 0.52），
852	    但 surface features 保持相对稳定（|ρ| 0.50 vs avg 0.60）。这意味着更大模型 的 DDR 三梯度中，entropy_mean
853	    可能从 moderate drift 退化为 near-stationary， DDR 叙事在 frontier scale 上需要更多 nuance。论文应将此作为
854	    honest limitation 报告，并建议 future work 在 >14B 模型上验证。
855	
856	    '
857	- name: ordinal_baseline_comparison
858	  plan_id: plan_015
859	  description: '对比 existing detector scores（FastDetectGPT, Binoculars, LD-Score, avg_logprob）
860	    作为 ordinal depth features vs 7-feature model。
861	
862	    '
863	  expected_results:
864	    seven_feature_logo_f1: 0.68
865	    seven_feature_ci: '[0.665, 0.695]'
866	    avg_logprob_logo_f1: 0.658
867	    avg_logprob_ci: '[0.540, 0.740]'
868	    ld_score_logo_f1: 0.632
869	    ld_score_ci: '[0.520, 0.710]'
870	    fastdetectgpt_logo_f1: 0.595
871	    fastdetectgpt_ci: '[0.480, 0.690]'
872	    binoculars_logo_f1: 0.558
873	    binoculars_ci: '[0.400, 0.650]'
874	    bootstrap_delta_7feat_vs_avglogprob:
875	      delta: 0.022
876	      p: 0.008
877	      significant: true
878	    seven_feat_advantage_pp: 2.2
879	    avg_logprob_spearman: -0.52
880	    ld_score_spearman: -0.48
881	  result_rationale: 'Median 档下 7-feature vs best single detector (avg_logprob) 优势缩窄至
882	    2.2pp， 落在指定区间 [1.5, 3.0] 中部。avg_logprob 本身是一个强 ordinal baseline （ρ = -0.52），因为它直接度量了
883	    generation 的 "surprise" 级别，与 depth 有天然 负相关。7-feature 的优势来自两方面：(1) surface features
884	    捕获 vocabulary diversity 维度的独立信号，(2) 多特征组合提供了更 robust 的 decision boundary。 但在 median
885	    档下这些优势被 moderate drift 削弱——entropy features 的 marginal contribution 缩小，使 7-feature
886	    相对于 avg_logprob 的增量主要来自 hapax 和 TTR（实质上是 surface features + avg_logprob 的近似）。Bootstrap
887	    仍显著 (p=0.008) 但 CI overlap 大，Binoculars 和 FastDetectGPT 的高方差 CI （跨 generator 方差大）使得它们不是可靠的
888	    ordinal predictors。论文保持 "7-feature model outperforms single detectors" 但措辞需降低断言强度，
889	    强调 "statistical significance with modest practical improvement"。
890	
891	    '
892	  tables:
893	  - name: 'Table: Ordinal Baseline Comparison (LOGO Binary F1)'
894	    columns:
895	    - Method
896	    - LOGO F1
897	    - 95% CI
898	    - Spearman ρ
899	    rows:
900	    - - 7-feature ensemble
901	      - 0.68
902	      - '[0.665, 0.695]'
903	      - —
904	    - - Avg-LogProb (single)
905	      - 0.658
906	      - '[0.540, 0.740]'
907	      - -0.52
908	    - - LD-Score (single)
909	      - 0.632
910	      - '[0.520, 0.710]'
911	      - -0.48
912	    - - FastDetectGPT (single)
913	      - 0.595
914	      - '[0.480, 0.690]'
915	      - -0.38
916	    - - Binoculars (single)
917	      - 0.558
918	      - '[0.400, 0.650]'
919	      - -0.2
920	  figures_description:
921	  - Bootstrap Δ distribution plot：7-feature minus avg_logprob 的 1000-sample bootstrap
922	    Δ 分布，mean=+2.2pp，95% 区间不含零但左尾接近零。视觉上 传达 'significant but narrow' 的信息。
923	  analysis: 7-feature 优势在 median 档下边界化（2.2pp），论文需诚实定位：contribution 不在于 performance
924	    gap 的大小，而在于 (a) task formulation 的新颖性（ordinal depth estimation），(b) DDR 现象的实证发现，(c)
925	    7-feature 的 interpretability 和 efficiency 优势。若 reviewers 挑战 2.2pp 的 practical
926	    significance，回应 strategy 是强调 feature-level DDR 分析本身的 diagnostic value。
927	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9eb5b586-b43d-4a6a-b37a-76d89c7c0e55",
  "isSidechain": false,
  "promptId": "8cd44039-612b-4058-80a1-4cde6e090ba1",
  "type": "user",
  "uuid": "00bb365f-526b-4816-9c4d-fd6e42846f4a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/median/imagined_experiments.yaml",
      "content": "tier: median\nnarrative_guidance: '深度信号存在但边界模糊。DDR 需从 drifting/stationary 二分法调整为三梯度描述： strong drift\n  (hapax, TTR)、moderate drift (entropy_mean, entropy_std, entropy_min)、 near-stationary\n  (tail_decay, entropy_max)。7-feature 优势缩窄至 1.5–3pp， bootstrap 显著但 practical significance\n  边界化。entropy_mean 在 8B+ 模型上 |ρ| 降至 0.30–0.40，surface features 成为主要信号源。Cross-model\n  chains 信号温和， 不足以支撑 heterogeneity amplification 叙事。t=0.9 崩溃确认，温度范围需收窄至 [0.5,0.7]。\n  论文仍适合 Findings 但需补充 architecture-dependent DDR 分析和 scale 衰减曲线。\n\n  '\nimagined_experiments:\n- name: feature_ablation_and_trend\n  plan_id: plan_001\n  description: '三部分分析：(A) Feature ablation：full vs surface-only vs reference-only,\n    (B) DDR trend analysis per feature, (C) Perplexity pre-validation for Claim 3.\n\n    '\n  expected_results:\n    full_macro_f1: 0.808\n    surface_only_f1: 0.757\n    reference_only_f1: 0.712\n    ref_vs_surf_bootstrap_ci: '[0.698,0.726] vs [0.742,0.772]'\n    hapax_ratio_slope: -0.072\n    hapax_ratio_rho: -0.61\n    ttr_slope: -0.048\n    ttr_rho: -0.58\n    entropy_mean_slope: -0.38\n    entropy_mean_rho: -0.52\n    entropy_std_rho: -0.18\n    entropy_min_rho: -0.31\n    entropy_max_rho: 0.08\n    tail_decay_rho: 0.05\n    median_ppl_by_depth: 13.2, 5.1, 3.1, 2.2, 1.8\n  result_rationale: 'Median 档下 surface features 仍是主力信号源（hapax, TTR 的 strong drift\n    使 surface-only 达到 0.757），但 reference features 提供互补信号（full > surface +5.1pp）。 Reference-only\n    低于 surface-only 约 4.5pp，因为 entropy_mean 的 drift 从 best-case |ρ|>0.60 退化到 moderate\n    水平（~0.52），entropy_std 和 entropy_min 漂移温和 （|ρ| 0.18–0.31），不再清晰归类为 drifting。三梯度格局成型：strong\n    drift (hapax -0.61, TTR -0.58) > moderate drift (entropy_mean -0.52, entropy_min\n    -0.31, entropy_std -0.18) > near-stationary (entropy_max 0.08, tail_decay 0.05)。\n    Perplexity 按深度单调下降，验证 Claim 3 前提。\n\n    '\n  tables:\n  - name: 'Table: Feature Ablation (5-fold CV)'\n    columns:\n    - Feature Set\n    - Macro F1\n    - 95% CI\n    rows:\n    - - Full (7 features)\n      - 0.808\n      - '[0.795, 0.821]'\n    - - Surface-only (TTR + hapax)\n      - 0.757\n      - '[0.742, 0.772]'\n    - - Reference-only (5 entropy + tail)\n      - 0.712\n      - '[0.698, 0.726]'\n  - name: 'Table: DDR Gradient Classification'\n    columns:\n    - Feature\n    - Spearman ρ\n    - Gradient Group\n    rows:\n    - - hapax_ratio\n      - -0.61\n      - strong drift\n    - - TTR\n      - -0.58\n      - strong drift\n    - - entropy_mean\n      - -0.52\n      - moderate drift\n    - - entropy_min\n      - -0.31\n      - moderate drift\n    - - entropy_std\n      - -0.18\n      - moderate drift\n    - - entropy_max\n      - 0.08\n      - near-stationary\n    - - tail_decay\n      - 0.05\n      - near-stationary\n  figures_description:\n  - 7-panel feature trend plot (mean ± std across depth 0–4)：hapax 和 TTR 展示 陡峭单调下降，entropy_mean\n    展示中等下降但 std 较大，entropy_std/min 呈平缓下降， entropy_max 和 tail_decay 近似水平线。三梯度视觉上清晰可辨。\n  - Perplexity by depth bar chart：depth 0→4 的 Pythia-410M ppl 单调下降 (13.2→1.8)，支持 location\n    shift 假说。\n  analysis: 'McNemar 检验 full vs surface p ≈ 0，full vs reference p ≈ 0，确认互补性。 但 surface-only\n    已高于 reference-only 4.5pp，表明 vocabulary impoverishment 是主导信号。原始 drifting/stationary\n    二分法需修改：entropy_std 的 |ρ|=0.18 落在灰色地带（既非清晰 drifting 也非 stationary），需引入 moderate\n    drift 类别。 论文 Claim 2 的叙事从 \"dual dynamics\" 调整为 \"gradient of depth sensitivity\"。\n\n    '\n- name: cross_generator_evaluation\n  plan_id: plan_002\n  description: '扩展至 5 generators（Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B），\n    LOGO 和 LOFO 评估。\n\n    '\n  expected_results:\n    total_records: 22800\n    logo_avg_macro_f1: 0.788\n    logo_avg_binary_f1: 0.675\n    logo_binary_ci: '[0.662, 0.688]'\n    lofo_binary_f1: 0.652\n    per_gen_binary_f1:\n      pythia_2_8b: 0.71\n      pythia_1b: 0.715\n      olmo_2_1b: 0.66\n      qwen3_1_7b: 0.668\n      qwen3_0_6b: 0.62\n    per_gen_binary_f1_range_pp: 9.5\n    family_out_delta: 0.023\n  result_rationale: 'Median 档下 LOGO binary F1 落在 [0.66, 0.69] 范围中部（0.675）。Pythia 家族\n    两个模型（2.8B, 1B）因与 Pythia-410M reference 同源而获得轻微优势（0.710–0.715）， OLMo 和 Qwen 因 architecture\n    差异表现更低。per-gen 方差约 9.5pp，符合 median 档 10–15pp 预期的下界。LOFO binary F1（0.652）低于 LOGO\n    约 2.3pp，因为 leave-one-family-out 移除整个 Pythia 家族（两个模型）时训练集覆盖度下降。Qwen3-0.6B 最低因为\n    模型容量小导致生成文本多样性本身受限，depth drift 信号被压缩。\n\n    '\n  tables:\n  - name: 'Table: LOGO Per-Generator Binary F1'\n    columns:\n    - Generator\n    - Binary F1\n    - 95% CI\n    - Family\n    rows:\n    - - Pythia-2.8B\n      - 0.71\n      - '[0.692, 0.728]'\n      - Pythia\n    - - Pythia-1B\n      - 0.715\n      - '[0.697, 0.733]'\n      - Pythia\n    - - OLMo-2-1B\n      - 0.66\n      - '[0.641, 0.679]'\n      - OLMo\n    - - Qwen3-1.7B\n      - 0.668\n      - '[0.649, 0.687]'\n      - Qwen\n    - - Qwen3-0.6B\n      - 0.62\n      - '[0.600, 0.640]'\n      - Qwen\n  figures_description:\n  - Per-generator LOGO binary F1 bar chart with CI whiskers，按 family 着色。 Pythia 家族明显高于其他\n    family，展示 reference model bias。\n  - LOFO confusion matrix heatmap：leave-Pythia-out 条件下 gen-1 vs gen-2+ 混淆 集中，leave-Qwen-out\n    条件下性能最高。\n  analysis: 'Per-gen F1 range 9.5pp 处于 median 预期下界，reviewers 可能质疑 generalizability。\n    需逐 generator 报告并承认 Pythia-as-reference 的 family bias。LOFO 下降 2.3pp 表明 cross-family\n    transfer 存在但有衰减。论文需将 headline metric 从单一 F1 改为 range 报告（0.620–0.715）。\n\n    '\n- name: cross_family_reference_model\n  plan_id: plan_003\n  description: '测试 OLMo-2-1B 和 Qwen3-0.6B 作为 reference model 时 DDR 是否持续。\n\n    '\n  expected_results:\n    logo_f1_pythia_ref: 0.788\n    logo_f1_olmo_ref: 0.78\n    logo_f1_qwen_ref: 0.795\n    entropy_drift_all_refs_negative: true\n    pythia_ref_entropy_mean_rho: -0.52\n    olmo_ref_entropy_mean_rho: -0.44\n    qwen_ref_entropy_mean_rho: -0.48\n    olmo_ref_drift_range:\n    - -0.44\n    - -0.78\n    qwen_ref_drift_range:\n    - -0.48\n    - -0.85\n    pythia_ref_drift_range:\n    - -0.52\n    - -0.92\n    dual_dynamics_is_pythia_artifact: false\n    tail_decay_rho_all_refs_abs_max: 0.09\n  result_rationale: 'Median 档下 DDR 不是 Pythia 特有现象（drift 方向一致），但 entropy_mean |ρ| 跨\n    reference model 有明显波动（0.44–0.52），不再稳定超过 0.55。三个 ref 的 LOGO F1 差异 <1.5pp，说明 classifier\n    性能对 reference 选择不敏感，但 DDR 分析的具体数值（ρ magnitude）取决于 reference-generator 对。Qwen ref\n    略高 因为 Qwen 家族的 entropy 分布与多数 generator 有更好的判别力。tail_decay 和 entropy_max 在所有 ref\n    下保持 near-stationary（|ρ| < 0.10），确认 shape features 的稳健性是跨 reference 的。DDR 三梯度结构跨\n    reference 稳定，但 moderate drift 组的具体 ρ 值波动 ±0.08。\n\n    '\n  tables:\n  - name: 'Table: Reference Model Comparison'\n    columns:\n    - Reference Model\n    - LOGO F1\n    - entropy_mean ρ\n    - tail_decay ρ\n    rows:\n    - - Pythia-410M\n      - 0.788\n      - -0.52\n      - 0.05\n    - - OLMo-2-1B\n      - 0.78\n      - -0.44\n      - 0.07\n    - - Qwen3-0.6B\n      - 0.795\n      - -0.48\n      - 0.04\n  figures_description:\n  - 3×7 heatmap：每个 reference model 下 7 个 feature 的 Spearman ρ。颜色编码 三梯度（deep red =\n    strong drift, orange = moderate, gray = stationary）。 跨行模式一致但 moderate drift 列色调有波动。\n  analysis: 'DDR 非 Pythia artifact——方向一致、三梯度结构跨 ref 稳定。但 entropy_mean 的 |ρ| 在 non-Pythia\n    ref 下降至 0.44，接近 drifting/moderate 边界。论文应报告 所有三个 ref 的 ρ range 而非挑选最佳值。这支持将 entropy_mean\n    归入 moderate drift 而非 strong drift，进一步支持三梯度叙事。\n\n    '\n- name: downstream_utility\n  plan_id: plan_004\n  description: 'OLMo-1B fine-tune on depth-stratified data，3 seeds，bootstrap CIs，\n    sample-count-matched control。\n\n    '\n  expected_results:\n    all_ppl_mean: 2.34\n    all_ppl_ci: '[2.336, 2.344]'\n    size_matched_ppl_mean: 2.37\n    size_matched_ppl_ci: '[2.366, 2.374]'\n    depth01_ppl_mean: 2.39\n    depth01_ppl_ci: '[2.386, 2.394]'\n    binary_filtered_ppl_mean: 2.393\n    binary_filtered_ppl_ci: '[2.389, 2.397]'\n    depth0_only_ppl_mean: 2.685\n    depth0_only_ppl_ci: '[2.680, 2.690]'\n    ranking: all < size_matched < depth01 ≈ binary_filtered << depth0_only\n    tost_2pct_p: 0.00012\n    tost_1pct_p: 0.087\n    seed_variance: <0.003 within variant\n    cohens_d_depth01_vs_matched: 0.42\n  result_rationale: 'Median 档下 Claim 3 的 negative finding 完全成立。depth-aware filtering\n    不优于 random subsampling（size_matched 2.370 vs depth01 2.390），因为 depth filtering\n    移除的深层文本虽然 perplexity 更低，但其信息内容仍有训练价值。TOST 在 ±2% margin 下显著（p=0.00012），但 ±1% margin\n    下不显著（p=0.087），说明等价性 在实际层面成立但统计精度受限于 3 seeds。seed 间方差极小（<0.003），印证 OLMo-1B fine-tune\n    的稳定性。depth0_only 显著差因为纯人工文本量不足（仅 ~800 训练样本），这是数据量效应而非深度质量效应。Cohen''s d=0.42 中等偏小，\n    TOST 是更合适的检验。\n\n    '\n  tables:\n  - name: 'Table: Downstream CLM Quality by Training Data Composition'\n    columns:\n    - Variant\n    - Train Size\n    - Ppl (mean ± std)\n    - TOST p (±2%)\n    rows:\n    - - All depths\n      - 12299\n      - 2.340 ± 0.003\n      - —\n    - - Size-matched random\n      - 3951\n      - 2.370 ± 0.003\n      - ref\n    - - Depth 0+1 only\n      - 3951\n      - 2.390 ± 0.003\n      - 0.00012\n    - - Binary-filtered\n      - 3951\n      - 2.393 ± 0.003\n      - 9.0e-05\n    - - Depth 0 only\n      - 797\n      - 2.685 ± 0.004\n      - <0.001 (reject eq.)\n  figures_description:\n  - Bar chart with ppl per variant，3 seeds 显示为抖动点。all 和 size_matched 之间的 gap 归因于数据量，depth01\n    和 binary_filtered 几乎重叠。\n  - TOST margin sensitivity plot：x 轴 margin (±1%–5%)，y 轴 rejection p-value。 ±2% 处\n    p 跌破 0.05 临界线。\n  analysis: 'Negative finding 稳健。Depth-aware curation 不改善下游 CLM 质量，depth fingerprinting\n    定位为 diagnostic 而非 curative 工具。论文 Claim 3 在 median 档下无需修改措辞， 是最稳定的 claim。\n\n    '\n- name: prompt_type_comparison\n  plan_id: plan_005\n  description: 'Continuation vs elaboration vs inspired_rewriting chains，Pythia-2.8B，1000\n    seeds。\n\n    '\n  expected_results:\n    cv_f1_continuation: 0.773\n    cv_f1_elaboration: 0.723\n    cv_f1_rewriting: 0.733\n    lopto_avg_f1: 0.748\n    lopto_held_out_cont: 0.758\n    lopto_held_out_elab: 0.755\n    lopto_held_out_rewrite: 0.728\n    depth_retention_d4_d0:\n      continuation: 0.835\n      elaboration: 0.984\n      rewriting: 0.938\n    drift_hapax_continuation: -0.72\n    drift_hapax_elaboration: -0.81\n    drift_hapax_rewriting: -0.78\n    drift_entropy_mean_continuation: -0.5\n    drift_entropy_mean_elaboration: -0.43\n    drift_entropy_mean_rewriting: -0.45\n  result_rationale: 'Median 档下 continuation 信号最强（0.773）因为每步生成从前文直接续写， 累积的 lexical\n    diversity 压缩最显著。Elaboration 最弱（0.723）因为 elaboration prompt 给模型更多自由度，保留了更多词汇多样性。但三种\n    prompt 类型的差距 仅 ~5pp（而非 best-case 下的 7pp），因为在 median 档下 entropy_mean 的 drift magnitude\n    已整体缩小，各 prompt 类型间的 drift 差异也随之缩小。Elaboration 的 depth retention 极高（0.984）意味着几乎不丢失链条，但深度信号更弱——\n    这是 semantic divergence 与 depth discriminability 的 tradeoff。LOPTO (leave-one-prompt-type-out)\n    显示 cross-prompt transfer 合理（avg 0.748）， 但 held-out rewriting 略低因其 drift 特征介于两端。\n\n    '\n  tables:\n  - name: 'Table: Prompt-Type CV F1 Comparison'\n    columns:\n    - Prompt Type\n    - CV F1\n    - Depth Retention (d4/d0)\n    - hapax ρ\n    - entropy_mean ρ\n    rows:\n    - - Continuation\n      - 0.773\n      - 0.835\n      - -0.72\n      - -0.5\n    - - Inspired Rewriting\n      - 0.733\n      - 0.938\n      - -0.78\n      - -0.45\n    - - Elaboration\n      - 0.723\n      - 0.984\n      - -0.81\n      - -0.43\n  figures_description:\n  - 3-panel feature drift plot（每行一种 prompt 类型）：continuation 的 hapax/TTR 斜率最陡，elaboration\n    的 entropy_mean 斜率最平。可视化 semantic freedom 与 depth signal 的反向关系。\n  analysis: 'Continuation 最适合 depth fingerprinting，elaboration 最弱。论文报告 continuation\n    0.773 vs elaboration 0.723（+5.0pp），prompt-type 依赖性存在 但可控。Median 档下差异缩小意味着论文措辞应用\n    \"moderate prompt-type dependence\" 而非 \"strong\"。\n\n    '\n- name: paraphrastic_comparison\n  plan_id: plan_006\n  description: '构建 paraphrasing chains（语义保持的改写链）与 continuation chains 直接对比， 测试 attractor\n    convergence theory。\n\n    '\n  expected_results:\n    paraphrastic_cv_binary_f1: 0.585\n    paraphrastic_ci: '[0.565, 0.605]'\n    continuation_cv_binary_f1: 0.682\n    continuation_ci: '[0.665, 0.699]'\n    delta_pp: 9.7\n    paraphrastic_hapax_rho: -0.28\n    paraphrastic_entropy_mean_rho: -0.15\n    paraphrastic_attractor_convergence_depth: 2.8\n    continuation_attractor_convergence_depth: '>4'\n    paraphrastic_depth_retention_d4_d0: 0.96\n  result_rationale: 'Paraphrastic chains 因 semantic preservation 约束而快速收敛到 attractor\n    state， 深度信号在 depth 2–3 后基本消失（|ρ| 从 depth 0-1 的 0.28 降至 depth 3-4 的 < 0.10）。这与\n    ACL 2025 \"LLM as Broken Telephone\" 的 attractor cycle theory 一致： paraphrasing 约束将分布锁定在\n    ~3-class 分辨率上界。Continuation chains 因无 semantic 约束，diversity 持续压缩，depth signal\n    延伸到 depth 4+。二者差距 9.7pp （median 档，best-case 可能更大）确认了 non-paraphrastic chains 是更有前途的\n    depth estimation 场景。但 median 档下 continuation 本身也只有 0.682（LOGO）， 所以 paraphrastic\n    的 0.585 已接近 chance-level 对于 binary classification。\n\n    '\n  tables:\n  - name: 'Table: Paraphrastic vs Continuation Chains'\n    columns:\n    - Chain Type\n    - Binary F1\n    - hapax ρ\n    - entropy_mean ρ\n    - Attractor Convergence\n    rows:\n    - - Continuation\n      - 0.682\n      - -0.61\n      - -0.5\n      - '>depth 4'\n    - - Paraphrastic\n      - 0.585\n      - -0.28\n      - -0.15\n      - ~depth 2.8\n  figures_description:\n  - Feature drift trajectory comparison：两条线（continuation vs paraphrastic） 叠加，x 轴 depth\n    0–4，y 轴 normalized feature value。Paraphrastic 线在 depth 2–3 趋平，continuation 线持续下降。\n  analysis: 'Paraphrastic chains 的 attractor convergence 确认我们的 contribution scope：\n    non-paraphrastic chains 是 DDR 的核心场景。论文 Related Work 需与 ACL 2025 attractor theory\n    对话。Median 档下 paraphrastic F1 仍显著高于 random（0.50）， 说明即使在 attractor 约束下 depth 1 vs\n    depth 2+ 仍有微弱信号。\n\n    '\n- name: cross_model_chains\n  plan_id: plan_007\n  description: 'Cross-model chains（每步不同 generator），与 single-model chains 对比。\n\n    '\n  expected_results:\n    cross_model_binary_f1: 0.73\n    cross_model_binary_ci: '[0.71, 0.75]'\n    cross_model_3class_f1: 0.72\n    single_model_logo_binary_f1: 0.675\n    delta_cross_vs_single_pp: 5.5\n    cross_model_hapax_rho: -0.54\n    cross_model_entropy_mean_rho: -0.4\n    per_chain_composition_variance: 0.03\n  result_rationale: 'Median 档下 cross-model chains 的 binary F1 为 0.73，落在指定区间 [0.70,\n    0.76] 中部。Cross-model chains 的 F1 高于 single-model LOGO（0.675）约 5.5pp， 原因是不同 generator\n    间的 architecture 差异引入额外的 distributional shift， 叠加在 depth-intrinsic drift 之上。但这个\n    amplification 是温和的（+5.5pp 而非 best-case 的 +13.6pp），因为 median 档下 architecture-dependent\n    DDR 意味着部分 generator 组合（如两个 Qwen 模型相邻）的 architecture shift 很小。 entropy_mean ρ 在\n    cross-model 链中降至 -0.40（单模型下 -0.52），因为 reference model 对不同 architecture 的 entropy\n    估计不一致。hapax/TTR 的 surface features 受 architecture shift 影响更小（-0.54 vs -0.61），再次确认\n    surface features 在 median 档下的相对优势。\n\n    '\n  tables:\n  - name: 'Table: Cross-Model vs Single-Model Chains'\n    columns:\n    - Chain Type\n    - Binary F1\n    - 3-class F1\n    - hapax ρ\n    - entropy_mean ρ\n    rows:\n    - - Cross-model (5-gen mix)\n      - 0.73\n      - 0.72\n      - -0.54\n      - -0.4\n    - - Single-model (LOGO avg)\n      - 0.675\n      - 0.788\n      - -0.61\n      - -0.52\n  figures_description:\n  - Cross-model chain construction diagram：展示 5 generators 如何在不同 depth 层被随机分配。附 per-composition\n    binary F1 violin plot。\n  analysis: 'Cross-model 信号温和（0.73），不足以支撑 \"heterogeneity amplification\" 的强叙事。 论文需将\n    framing 从 \"heterogeneity amplifies depth signal\" 改为 \"heterogeneous chains remain\n    detectable, with moderate amplification from architecture mixing\"。 Median 档下这是一个稳健但不戏剧化的\n    finding。\n\n    '\n- name: multi_domain_seeds\n  plan_id: plan_008\n  description: '扩展至 4 domains：Wikipedia, news, scientific, creative writing。\n\n    '\n  expected_results:\n    wikipedia_binary_f1: 0.692\n    news_binary_f1: 0.675\n    news_ci: '[0.655, 0.695]'\n    academic_binary_f1: 0.648\n    academic_ci: '[0.628, 0.668]'\n    creative_binary_f1: 0.66\n    creative_ci: '[0.640, 0.680]'\n    max_gap_vs_wiki_pp: 4.4\n    cross_domain_logo_binary_f1: 0.665\n    worst_domain: academic\n  result_rationale: 'Median 档下各 domain 的 binary F1 落在 0.648–0.692，max gap 约 4.4pp。\n    Wikipedia 最高因为 Wikipedia 文本结构相对均匀，depth drift 信号最 consistent。 Academic 最低因为科学文本的\n    vocabulary 本身 specialized 且 diversity 较低（高频 术语复用），depth-induced vocabulary compression\n    与 domain-intrinsic low diversity 混淆。Creative writing 和 news 居中。Cross-domain LOGO（train\n    on 3 domains, test on held-out domain）为 0.665，接近 overall LOGO，说明 depth signal\n    是 domain-robust 的。差异 <5pp 足以在论文中 claim \"domain independence\"， 但需逐 domain 报告并讨论\n    academic domain 的特殊性。\n\n    '\n  tables:\n  - name: 'Table: Multi-Domain Binary F1'\n    columns:\n    - Domain\n    - Binary F1\n    - 95% CI\n    - Seed Count\n    rows:\n    - - Wikipedia\n      - 0.692\n      - '[0.672, 0.712]'\n      - 500\n    - - News\n      - 0.675\n      - '[0.655, 0.695]'\n      - 500\n    - - Creative\n      - 0.66\n      - '[0.640, 0.680]'\n      - 500\n    - - Academic\n      - 0.648\n      - '[0.628, 0.668]'\n      - 500\n  figures_description:\n  - Per-domain feature drift comparison：4 个 domain 的 hapax_ratio drift 线 基本平行（slope\n    相近），但 academic domain 的 intercept 更低（初始 diversity 就低），解释其 F1 略低。\n  analysis: 'Depth signal 跨 domain 稳健，最大差距 4.4pp。论文可 claim domain independence 但需报告\n    academic domain 的 ceiling 效应。Median 档下 creative writing 没有 出现特殊行为，消除了 \"creative\n    writing harder\" 的担忧。\n\n    '\n- name: finer_grained_ordinal\n  plan_id: plan_009\n  description: '5-class ordinal classification（gen-0 through gen-4），CORAL 和 Frank-Hall\n    ordinal methods vs standard XGBoost。\n\n    '\n  expected_results:\n    xgboost_5class_f1: 0.495\n    coral_5class_f1: 0.498\n    frank_hall_5class_f1: 0.492\n    xgboost_3class_f1: 0.788\n    gen1_vs_gen2_confusion_rate: 0.43\n    gen2_vs_gen3_confusion_rate: 0.52\n    gen3_vs_gen4_confusion_rate: 0.58\n    binary_fn_concentration: 0.85\n  result_rationale: 'Median 档下 5-class F1 降至 ~0.495，ordinal methods 无改善（±0.3pp）。 Gen-1/gen-2\n    边界是 bottleneck（43% confusion），gen-2/gen-3 和 gen-3/gen-4 更差（52% 和 58%）。原因是 DDR\n    在 median 档下的 moderate drift features （entropy_mean, entropy_std, entropy_min）在深度\n    2+ 后的 marginal change 很小， feature space 中 gen-2/3/4 高度重叠。Surface features (hapax,\n    TTR) 虽 drift 更强但也在 depth 3+ 趋于饱和。Ordinal methods 理论上应利用深度顺序性，但 因为 feature space\n    本身在 depth 2+ 后分辨力不足，ordinal constraint 无法提供 额外信号。3-class 是 practical ceiling，5-class\n    只在 gen-0 identification 上有效（gen-0 F1 ~0.95），deeper classes 全部混淆。86% 的 binary errors\n    集中在 FN（gen-2+ 被误判为 gen-1），说明模型在 depth boundary 上的主要失败 是 miss 而非 false alarm。\n\n    '\n  tables:\n  - name: 'Table: Ordinal Granularity Comparison'\n    columns:\n    - Method\n    - 5-class F1\n    - 3-class F1\n    - ΔF1\n    rows:\n    - - XGBoost (standard)\n      - 0.495\n      - 0.788\n      - -0.293\n    - - CORAL\n      - 0.498\n      - —\n      - —\n    - - Frank-Hall\n      - 0.492\n      - —\n      - —\n  figures_description:\n  - 5-class confusion matrix heatmap：gen-0 几乎完美分类（对角线深色），gen-1 有中等混淆，gen-2/3/4 的三行几乎互相混淆（off-diagonal\n    色块密集）。\n  analysis: '3-class 是 resolution ceiling，ordinal methods 无额外增益。论文应明确报告 这个负面结果，定位\n    3-class 为 \"practical resolution limit\"。这其实加强了 论文叙事：gen-1 vs gen-2+ 的二分法在 median\n    档下仍有意义，更细粒度不现实。\n\n    '\n- name: human_edit_robustness\n  plan_id: plan_010\n  description: '模拟人工编辑鲁棒性：(A) Random word replacement，(B) LLM-simulated rephrasing。\n\n    '\n  expected_results:\n    baseline_binary_f1: 0.68\n    random_5pct_f1: 0.636\n    random_5pct_drop: -0.044\n    random_10pct_f1: 0.602\n    random_10pct_drop: -0.078\n    random_20pct_f1: 0.575\n    random_20pct_drop: -0.105\n    llm_rephrase_f1: 0.632\n    llm_rephrase_drop: -0.048\n    llm_rephrase_ci: '[0.612, 0.652]'\n    edit_distance_ratio: 0.5\n  result_rationale: 'Median 档下 LLM rephrase drop 为 4.8pp，落在指定区间 [4.0, 7.0] 的下半部。 Random\n    replacement 5% 与 LLM rephrase 的 drop 相近（~4.4–4.8pp），因为 5% 随机替换对 vocabulary diversity\n    features（hapax, TTR）的扰动与 LLM 对 ~1.7 句的 rephrasing 对 diversity 的影响量级相当。10% 和 20%\n    replacement 的更大 drop 主要来自 surface features 的破坏：随机插入的词汇增加了 hapax count， 部分抵消了 depth-induced\n    diversity compression 信号。LLM rephrase 的影响 更 \"intelligent\"——它倾向于同义替换而非随机词，所以保留了更多\n    distributional structure。20% replacement 后仍有 0.575（>0.50 random），说明 depth signal\n    在重度编辑下仍有微弱残留。论文需在附录中报告，承认 moderate robustness。\n\n    '\n  tables:\n  - name: 'Table: Robustness to Simulated Editing'\n    columns:\n    - Edit Type\n    - Binary F1\n    - Drop (pp)\n    - 95% CI\n    rows:\n    - - None (baseline)\n      - 0.68\n      - —\n      - '[0.663, 0.697]'\n    - - Random 5%\n      - 0.636\n      - -4.4\n      - '[0.618, 0.654]'\n    - - Random 10%\n      - 0.602\n      - -7.8\n      - '[0.583, 0.621]'\n    - - Random 20%\n      - 0.575\n      - -10.5\n      - '[0.556, 0.594]'\n    - - LLM rephrase\n      - 0.632\n      - -4.8\n      - '[0.612, 0.652]'\n  figures_description:\n  - Robustness degradation curve：x 轴 edit intensity（0%, 5%, 10%, 20%, LLM）， y 轴 binary\n    F1。LLM rephrase 标注为菱形点，与 random 5% 高度接近。\n  analysis: 'Signal 在 moderate editing 下尚存但降解显著。论文定位为 \"robust to light editing, degrades\n    gracefully under heavier perturbation\"。LLM rephrase drop 4.8pp 在 median 档预期内，reviewers\n    不太会以此否定方法但会要求讨论 ecological validity。\n\n    '\n- name: ld_score_feature\n  plan_id: plan_011\n  description: '添加 LD-Score（character-level distribution signature）作为第 8 个 feature。\n\n    '\n  expected_results:\n    eight_feat_cv_f1: 0.798\n    seven_feat_cv_f1: 0.788\n    delta_pp: 1.0\n    ld_score_alone_rho: -0.42\n    ld_score_xgb_importance: 0.045\n    ld_score_spearman_with_hapax: 0.72\n  result_rationale: 'Median 档下 LD-Score 提供了 +1.0pp 的 marginal gain，统计显著但实际增益微小。 LD-Score\n    与 hapax_ratio 的 Spearman 相关高达 0.72——两者都捕获 lexical diversity 的不同侧面（word-level vs\n    character-level），信号高度冗余。LD-Score 单独的 ordinal ρ 为 -0.42，介于 moderate drift 组。在 XGBoost\n    importance 中仅排第 6 位（0.045），被 hapax, TTR, entropy_mean 远远压过。增加 LD-Score 不改变论文叙事，\n    但可作为 \"character-level signal also exhibits depth drift\" 的补充证据。 论文选择保持 7-feature\n    设计并在附录报告 LD-Score，避免增加模型复杂度。\n\n    '\n  tables:\n  - name: 'Table: LD-Score as Additional Feature'\n    columns:\n    - Feature Set\n    - CV F1\n    - Δ vs 7-feat\n    rows:\n    - - 7 features\n      - 0.788\n      - —\n    - - 7 features + LD-Score\n      - 0.798\n      - +1.0pp\n    - - LD-Score alone\n      - 0.682\n      - -10.6pp\n  figures_description:\n  - Feature correlation heatmap including LD-Score：LD-Score 与 hapax_ratio 的 色块最深（r=0.72），视觉上解释冗余性。\n  analysis: 'LD-Score 的 marginal value 有限（+1pp），不值得增加 feature set 复杂度。 但 character-level\n    depth drift 的存在本身有学术价值，作为 DDR 跨 granularity 的佐证。论文附录报告。\n\n    '\n- name: end_to_end_classifier\n  plan_id: plan_012\n  description: 'QLoRA fine-tuned end-to-end classifier vs handcrafted 7-feature model。\n\n    '\n  expected_results:\n    qlora_3class_cv_f1: 0.882\n    qlora_3class_ci: '[0.870, 0.894]'\n    qlora_binary_cv_f1: 0.84\n    qlora_binary_ci: '[0.825, 0.855]'\n    qlora_5class_cv_f1: 0.565\n    seven_feat_3class_cv_f1: 0.788\n    seven_feat_binary_cv_f1: 0.68\n    delta_3class_pp: 9.4\n    delta_binary_pp: 16.0\n    qlora_logo_binary_f1: 0.62\n    qlora_gpu_memory_gb: 8.5\n    qlora_inference_time_ratio: 12.4\n  result_rationale: 'QLoRA within-distribution performance 显著高于 7-feature（3-class\n    +9.4pp， binary +16pp），因为 end-to-end model 可以学到 handcrafted features 未捕获的 fine-grained\n    distributional patterns（如 specific n-gram frequency shifts， positional entropy\n    patterns）。但 LOGO generalization（0.62）大幅低于 within-distribution（0.840），暴露了 end-to-end\n    model 对 generator-specific artifacts 的过拟合。7-feature model 的 LOGO vs CV drop 更小（~10pp\n    vs ~22pp）， 因为 handcrafted features 是 generator-agnostic 的 distributional statistics。\n    5-class QLoRA（0.565）仍低，确认 resolution ceiling 非 feature engineering 问题 而是 task\n    intrinsic。推理成本 12.4× 和 8.5GB GPU memory 使 QLoRA 在实际部署中 不 competitive。论文定位 7-feature\n    的优势为 \"efficiency + generalization\"。\n\n    '\n  tables:\n  - name: 'Table: End-to-End vs Handcrafted Features'\n    columns:\n    - Method\n    - CV 3-class\n    - CV Binary\n    - LOGO Binary\n    - Inference Cost\n    rows:\n    - - 7-feature XGBoost\n      - 0.788\n      - 0.68\n      - 0.675\n      - 1×\n    - - QLoRA Qwen3-0.6B\n      - 0.882\n      - 0.84\n      - 0.62\n      - 12.4×\n  figures_description:\n  - Radar chart：4 维比较（CV F1, LOGO F1, inference cost, memory usage）， 7-feature 在 LOGO\n    和效率维度占优，QLoRA 在 within-dist 占优。\n  analysis: 'QLoRA 的 within-dist 优势不能 transfer 到 unseen generators，而这恰好是 depth fingerprinting\n    的核心应用场景。7-feature model 的 LOGO 优势（0.675 vs 0.62）在 median 档下并不巨大（+5.5pp），但加上 12.4×\n    的成本差异，efficiency argument 成立。论文可用 QLoRA 作为 upper bound reference，强调 7-feature\n    的 \"right tradeoff\"。\n\n    '\n- name: text_length_control\n  plan_id: plan_013\n  description: 'Text length confound analysis：长度相关性、length-normalized features、 length-matched\n    re-evaluation。\n\n    '\n  expected_results:\n    spearman_length_depth: 0.11\n    spearman_ci: '[-0.06, 0.14]'\n    length_is_confound: false\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_binary_f1: 0.652\n    unmatched_binary_f1: 0.68\n    delta_pp: -2.8\n    dropout_short_text_bias: true\n  result_rationale: 'Median 档下 length-depth Spearman ρ 仅 0.11，text length 不是 depth\n    signal 的主要驱动因素。Length normalization 后 TTR 和 hapax 的 depth drift 反而更强 （normalized\n    ρ stronger），因为去除了 length variation 带来的噪声。 Length-matched subsampling 导致 F1 下降\n    2.8pp（0.680→0.652），但这主要来自 样本量减少（matching 丢弃了 ~30% 的数据）而非 length confound 移除。 Random\n    subsample control 可验证这一点。Depth-driven dropout 偏向短文本 （deeper generation 产生更多空/短输出被\n    skipped），但这是 generation process 的 intrinsic 特性而非统计 confound。论文可自信地排除 length confound。\n\n    '\n  tables:\n  - name: 'Table: Length Confound Analysis'\n    columns:\n    - Metric\n    - Value\n    - Conclusion\n    rows:\n    - - Spearman ρ(length, depth)\n      - 0.11\n      - Weak (|ρ|<0.15)\n    - - Length-matched binary F1\n      - 0.652\n      - −2.8pp from unmatched\n    - - Random subsample F1 (same n)\n      - 0.656\n      - Similar drop → sample size effect\n    - - Normalized TTR drift preserved?\n      - 'Yes'\n      - Depth signal independent of length\n  figures_description:\n  - Length distribution violin plot by depth (0–4)：各 depth 的 length 分布 高度重叠，仅 depth\n    4 有轻微 left shift（shorter texts）。\n  analysis: 'Length confound 排除。这是 paper credibility 的关键支撑。Median 档下 结论清晰，无需 hedge。\n\n    '\n- name: large_scale_generator\n  plan_id: plan_014\n  description: '添加 Qwen3-8B-Base 测试 scale effect on depth signal。\n\n    '\n  expected_results:\n    total_records: 4500\n    logo_6gen_avg_f1: 0.672\n    logo_qwen3_8b_held_out_binary_f1: 0.615\n    logo_qwen3_8b_ci: '[0.595, 0.635]'\n    logo_5gen_baseline_f1: 0.675\n    spearman_hapax: -0.5\n    spearman_ttr: -0.49\n    spearman_entropy_mean: -0.36\n    spearman_entropy_std: -0.08\n    spearman_entropy_max: 0.07\n    spearman_tail_decay: -0.06\n    feature_importance_hapax: 0.28\n    feature_importance_ttr: 0.17\n    feature_importance_entropy_mean: 0.14\n  result_rationale: 'Median 档下 Qwen3-8B held-out binary F1 为 0.615，落在指定区间 [0.58, 0.65]\n    中部。大模型生成的文本更 fluent、vocabulary 更 diverse、perplexity 更 uniform， 压缩了 depth drift\n    的 margin。entropy_mean |ρ| 从 5-gen avg 的 ~0.52 降至 0.36， 因为 8B 模型的 next-token entropy\n    分布更窄、depth-induced shift 更小。 Surface features（hapax -0.50, TTR -0.49）的衰减幅度小于 entropy\n    features， 因为 vocabulary diversity compression 是 depth-intrinsic 的物理过程，不受 model\n    capacity 影响——更大的模型仍然会在 recursive generation 中累积 lexical convergence。这进一步支持 median\n    档的核心主题：surface features 在 scale 增大时成为更重要的信号源。6-gen LOGO（含 8B）avg F1 0.672 vs 5-gen\n    baseline 0.675，8B 的加入仅轻微拉低整体。\n\n    '\n  tables:\n  - name: 'Table: Scale Effect — DDR by Model Size'\n    columns:\n    - Generator\n    - Size\n    - Binary F1\n    - hapax ρ\n    - entropy_mean ρ\n    rows:\n    - - Qwen3-0.6B\n      - 0.6B\n      - 0.62\n      - -0.58\n      - -0.52\n    - - Pythia-1B\n      - 1B\n      - 0.715\n      - -0.63\n      - -0.54\n    - - OLMo-2-1B\n      - 1.5B\n      - 0.66\n      - -0.6\n      - -0.5\n    - - Qwen3-1.7B\n      - 1.7B\n      - 0.668\n      - -0.59\n      - -0.49\n    - - Pythia-2.8B\n      - 2.8B\n      - 0.71\n      - -0.61\n      - -0.52\n    - - Qwen3-8B\n      - 8B\n      - 0.615\n      - -0.5\n      - -0.36\n  figures_description:\n  - Scale-DDR scatter plot：x 轴 log(model size)，y 轴 |ρ|。两条线： hapax（红，平缓下降）和 entropy_mean（蓝，陡峭下降）。8B\n    处两线明显分叉。 灰色 band 标注 stationary features 始终在 |ρ|<0.10 区域。\n  analysis: 'Scale effect 确认：entropy_mean drift 在 8B 处显著衰减（|ρ| 0.36 vs avg 0.52），\n    但 surface features 保持相对稳定（|ρ| 0.50 vs avg 0.60）。这意味着更大模型 的 DDR 三梯度中，entropy_mean\n    可能从 moderate drift 退化为 near-stationary， DDR 叙事在 frontier scale 上需要更多 nuance。论文应将此作为\n    honest limitation 报告，并建议 future work 在 >14B 模型上验证。\n\n    '\n- name: ordinal_baseline_comparison\n  plan_id: plan_015\n  description: '对比 existing detector scores（FastDetectGPT, Binoculars, LD-Score, avg_logprob）\n    作为 ordinal depth features vs 7-feature model。\n\n    '\n  expected_results:\n    seven_feature_logo_f1: 0.68\n    seven_feature_ci: '[0.665, 0.695]'\n    avg_logprob_logo_f1: 0.658\n    avg_logprob_ci: '[0.540, 0.740]'\n    ld_score_logo_f1: 0.632\n    ld_score_ci: '[0.520, 0.710]'\n    fastdetectgpt_logo_f1: 0.595\n    fastdetectgpt_ci: '[0.480, 0.690]'\n    binoculars_logo_f1: 0.558\n    binoculars_ci: '[0.400, 0.650]'\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.022\n      p: 0.008\n      significant: true\n    seven_feat_advantage_pp: 2.2\n    avg_logprob_spearman: -0.52\n    ld_score_spearman: -0.48\n  result_rationale: 'Median 档下 7-feature vs best single detector (avg_logprob) 优势缩窄至\n    2.2pp， 落在指定区间 [1.5, 3.0] 中部。avg_logprob 本身是一个强 ordinal baseline （ρ = -0.52），因为它直接度量了\n    generation 的 \"surprise\" 级别，与 depth 有天然 负相关。7-feature 的优势来自两方面：(1) surface features\n    捕获 vocabulary diversity 维度的独立信号，(2) 多特征组合提供了更 robust 的 decision boundary。 但在 median\n    档下这些优势被 moderate drift 削弱——entropy features 的 marginal contribution 缩小，使 7-feature\n    相对于 avg_logprob 的增量主要来自 hapax 和 TTR（实质上是 surface features + avg_logprob 的近似）。Bootstrap\n    仍显著 (p=0.008) 但 CI overlap 大，Binoculars 和 FastDetectGPT 的高方差 CI （跨 generator 方差大）使得它们不是可靠的\n    ordinal predictors。论文保持 \"7-feature model outperforms single detectors\" 但措辞需降低断言强度，\n    强调 \"statistical significance with modest practical improvement\"。\n\n    '\n  tables:\n  - name: 'Table: Ordinal Baseline Comparison (LOGO Binary F1)'\n    columns:\n    - Method\n    - LOGO F1\n    - 95% CI\n    - Spearman ρ\n    rows:\n    - - 7-feature ensemble\n      - 0.68\n      - '[0.665, 0.695]'\n      - —\n    - - Avg-LogProb (single)\n      - 0.658\n      - '[0.540, 0.740]'\n      - -0.52\n    - - LD-Score (single)\n      - 0.632\n      - '[0.520, 0.710]'\n      - -0.48\n    - - FastDetectGPT (single)\n      - 0.595\n      - '[0.480, 0.690]'\n      - -0.38\n    - - Binoculars (single)\n      - 0.558\n      - '[0.400, 0.650]'\n      - -0.2\n  figures_description:\n  - Bootstrap Δ distribution plot：7-feature minus avg_logprob 的 1000-sample bootstrap\n    Δ 分布，mean=+2.2pp，95% 区间不含零但左尾接近零。视觉上 传达 'significant but narrow' 的信息。\n  analysis: 7-feature 优势在 median 档下边界化（2.2pp），论文需诚实定位：contribution 不在于 performance\n    gap 的大小，而在于 (a) task formulation 的新颖性（ordinal depth estimation），(b) DDR 现象的实证发现，(c)\n    7-feature 的 interpretability 和 efficiency 优势。若 reviewers 挑战 2.2pp 的 practical\n    significance，回应 strategy 是强调 feature-level DDR 分析本身的 diagnostic value。\n",
      "numLines": 927,
      "startLine": 1,
      "totalLines": 927
    }
  },
  "sourceToolAssistantUUID": "9eb5b586-b43d-4a6a-b37a-76d89c7c0e55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DDR decoding-agnostic 被承认但 reviewer 认为 scope 限制削弱了 generalizability claim，需 rebuttal 或小幅调整后 borderline accept 核心假设：[\"Decoding-agnostic DDR 被认可为有意义的 robus…",
  "leafUuid": "00bb365f-526b-4816-9c4d-fd6e42846f4a",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "DDR decoding-agnostic validation and writing-focused revision",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

### Assistant

_source line 22 · 2026-05-21T21:43:58.238Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the previous median-tier imagined experiments from the last dream report. I need to generate an updated version based on:

1. The actual completed experiment results in the registry
2. The median tier definition provided by the user
3. The experiment_plan entries that are still "planned"

Let me check which experiments are already completed and which are still planned. From the registry, I can see that many experiments are already done. The user wants me to generate predicted data for each "planned" experiment in the experiment_plan.

Wait, looking more carefully at the experiment_plan, ALL entries have `status: planned`. But many of these have corresponding completed experiments in the registry. Let me reconcile:


- Most of the early plans (001-005, 008) have actual completed results in the registry
- Plans 006 and 007 are genuinely unfinished, though 007 has some cross-model data mentioned in the paper framing
- Plan 009 appears incomplete but has some 5-class information scattered in the paper framing and QLoRA experiments
- Plans 010, 013-015 are all completed with their respective experiment runs
- Plan 011 was planned but the LD-Score metric ended up being used in plan 015 instead
- Plan 012 is partially done with some QLoRA experiments in exp_055/056

The user is asking me to generate detailed predicted data for every planned experiment in the plan, since they're all marked as planned status. Let me re-read their request more carefully to understand exactly what data format and scope they want.

They want me to generate median-tier predicted results for all experiments, and crucially, every prediction needs to include a result_rationale. For experiments that already have actual completed results, I need to project what the median scenario would look like from a reviewer's perspective.

The median tier parameters are fairly consistent: reviewer scores around 3.0-3.5 for overall and soundness, acceptance probability between 40-65%, writing completion around 70-85%, modest claim strength improvements of +0.1 to +0.2, and reviewer scope concerns at severity level 3-4. The key insight is that DDR's decoding-agnostic approach is recognized as a meaningful robustness check, though with some limitations.

Looking at the specific concerns: greedy and top-k decoding alone don't fully support the "decoding-agnostic" claim, at least one reviewer will question the base-model-only scope, the 0.694 binary F1 is viewed as moderate performance rather than practically useful, Claim 3's negative finding is accepted but the experimental design is limited with only 3 seeds and a single metric, and the writing revisions would be about 70-85% complete in 72 hours. The narrative shifts Claim 2 from "decoding-agnostic property" to "robust across tested decoding strategies" and repositions Claim 1 as "first baseline for novel task," with rebuttals emphasizing the intentional scope boundaries.

Now I'm reconciling the actual results with this median-tier narrative to understand how the paper would be framed under this reviewer scenario. I need to ground the median-tier predictions in the actual experimental data where it exists, using real results as anchors while reframing the interpretation to match the median reviewer narrative. For experiments still pending, I'll project what would plausibly occur under median-tier assumptions.

Now I'm compiling the YAML output with all 15 experiments, anchoring the numeric results to what was actually observed while adjusting the rationales to reflect the median tier's concerns about scope limitations and insufficient evidence for the stronger claims. Looking at the cross-generator evaluation results, pythia-1b performed best at 0.8507 while olmo-2-1b was weakest at 0.7519, with ablation tests showing the full model substantially outperforming reference-only and surface-only variants. The cross-family reference model experiments confirm the pattern holds across different model families, with qwen showing the strongest leave-one-out performance at 0.8158, and crucially, entropy drift is consistently negative across all reference models while the effect isn't specific to pythia. Finally, the downstream utility experiments came back negative—both the full dataset and size-matched subsets show similar perplexity around 2.3-2.4, indicating the learned features don't transfer to language modeling tasks. Looking at the results across additional domains, code achieves 0.7535 at temperature 1.0 dropping to 0.6872 at 0.7, while Wikipedia establishes a strong baseline at 0.8148. The finer-grained ordinal classification shows 5-class performance degrading to around 0.50 with no gains from ordinal methods, and human edits reveal robustness issues with performance declining from 0.695 to 0.591 as perturbation increases. LD-Score as a standalone detector reaches 0.7212, though it was previously explored differently in another experiment.

The end-to-end classifier experiments show strong performance across model variants, with Qwen instruct achieving 0.9066 on 3-class and 0.8672 on binary, while text length appears to be a weak confound with minimal impact on classification despite a modest 0.041 improvement when length-matched.

For the large-scale generator evaluation, the 6-generator average F1 drops to 0.7893 compared to the 5-generator baseline of 0.8, and the ordinal baseline comparison shows the 7-feature approach outperforming alternatives like fastdetectgpt and binoculars by 3.3 percentage points. Now I'm reconciling the LOGO metrics across different evaluation setups—the binary F1 is 0.694 while the 3-class reaches 0.762, though the plan-002-eval shows a macro F1 of 0.8037 on the 5-generator set, which I need to align with the median tier framing.

Since the user's instructions ask me to expand each planned experiment with detailed data, and all experiments in the plan are marked as planned status, I should use actual results where they exist and project outcomes for the incomplete ones through the median tier lens.

The decoding-agnostic claim needs softening too — exp_062 shows robustness across greedy and top-k strategies, but reviewers at the median tier would argue that two decoding methods aren't enough to claim full decoding-agnosticism, so I'll frame it as "robust across tested strategies" instead.

Now I'll generate the full YAML output using actual experimental results as predicted values.

I'm noticing the paper distinguishes between two F1 metrics: the binary F1 (gen-1 vs gen-2+) at 0.694, which is the headline metric, versus the 3-class macro F1 at 0.8037, which inflates due to gen-0 seed sharing. I need to make sure I'm using the right metric for the median-tier framing. Looking at the 9-gen results, I can see the binary F1 dropped to 0.6661, which is lower than the 8-gen baseline of 0.694. The paper reports that 8-gen LOGO binary F1 value, and I have the per-generator range from 0.633 to 0.724 to work with. Now I need to organize all the median tier experiments into a structured output and think through how the decoding-agnostic framing fits into the overall narrative.

The decoding robustness across greedy and top-k strategies does show some stability, but calling it truly "decoding-agnostic" oversells the evidence with just two approaches tested. The 0.694 binary F1 is respectable but not strong enough to claim this is a production-ready tool—it's more of a solid first baseline. The scope limitation to base models only is intentional and defensible as a contribution boundary, even if it raises questions about broader applicability. The negative finding about claim 3 is legitimate but rests on limited evidence: only three seeds and a single metric. I'm at about 70-85% completion on the writing—the core sections are solid but related work and appendix still need refinement. The decoding experiment adds a modest +0.1 to +0.2 boost to overall claim strength, which is meaningful but not transformative.

Now I'm checking which experiments actually have results versus which are still planned. I need to distinguish between what's been run and what I'm projecting, especially for the YAML predictions. Looking through the registry and paper framing to see which experiments have concrete numbers versus which ones I'll need to estimate based on median-tier outcomes. The experiments in the plan (plan_001 through plan_015) are what I need to focus on, while exp_062 on decoding strategy serves as supporting context that shapes the narrative around plans like plan_001 and plan_003. Now I'm working through the metric definitions—the 3-class macro F1 scores look reasonable on the surface (~0.76-0.80) but are artificially inflated by generator-0 seed overlap, whereas the binary F1 (~0.694) gives a more honest assessment of model performance and is what the paper emphasizes.

I'm mapping each plan to its corresponding results: plan_001 through plan_005 and plan_008 and plan_010 have actual experimental data I can pull from, while plan_006, plan_007, plan_009, and plan_011 require projections based on the paper's framing and related findings. Writing the comprehensive YAML output now... For the completed experiments, I should stick with the actual measured values since those are fixed facts—the "median tier" framing only changes how I interpret and present these results, not the numbers themselves. The earlier dream report was indeed a prediction made before experiments ran, which is why those values differed from actuals, but now that I have real data, I need to use it.

For experiments still pending, I'll project outcomes that align with a median-tier assessment, then explain in each result_rationale why those particular numbers would lead reviewers to that tier conclusion. The overall narrative_guidance will tie together how this mixed picture—solid actual results plus reasonable projections—supports a median-tier story.

I should also reconsider how exp_062 on decoding strategy shifts the interpretation compared to the earlier dream report.

Looking at the median tier definition, the decoding-agnostic finding carries specific weight: reviewers acknowledge it as a meaningful robustness check but view two strategies (greedy and top-k) as insufficient to fully claim decoding-agnostic status. This translates to a modest +0.1 to +0.2 boost in effective claim strength. I need to reflect this uplift across the relevant experiments—particularly in Plan_001 where the feature ablation now incorporates the decoding strategy dimension, and in Plan_003 where the reference model cross-validation is further reinforced by this finding.

Now I'm pulling together the final output structure. The imagined_experiments section needs to be comprehensive but proportional—around 920 lines like the previous report. Since exp_062 feeds directly into both the DDR characterization and claim 2 validation, I need to integrate those decoding strategy results into the relevant experiment data. The checkpoint shows exp_062 concluded successfully but the metrics are empty, so I'll need to work from the paper_framing notes about greedy shape stability and construct the output accordingly. Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00bb365f-526b-4816-9c4d-fd6e42846f4a",
  "isSidechain": false,
  "requestId": "req_011CbGSZ6ZDUHoy1fJHZJTGs",
  "type": "assistant",
  "uuid": "7a783c07-0f80-44e5-94d9-ee0ca0c95145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbESnEZhBtTcsCNq5Yar9j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16740,
      "cache_read_input_tokens": 45422,
      "output_tokens": 26042,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16740,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26042,
          "cache_read_input_tokens": 45422,
          "cache_creation_input_tokens": 16740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16740
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

_source line 23 · 2026-05-21T21:50:07.198Z_

Now I have the actual experimental data and the previous dream report format. Let me construct the comprehensive median-tier prediction grounded in actual results.

```yaml
tier: median
narrative_guidance: >
  Decoding-agnostic DDR（greedy mean |d|=0.05, top-k 5/8 full preservation）被 reviewer 认可为有价值的
  robustness check，将 Claim 2 从纯 DDR 现象观察升级为包含 decoding-robustness 的 dual contribution——但
  仅 greedy + top-k 两种策略不足以 claim "decoding-agnostic property"，reviewer 要求至少补 nucleus sampling
  或 beam search。Claim 2 措辞从 "decoding-agnostic DDR" 软化为 "DDR robust across tested decoding
  strategies (greedy, top-k)"，保留 hedging 空间。0.694 binary F1 被定位为 "first baseline for a novel task"
  而非 practical tool，reviewer 认可 task formulation 贡献但质疑 practical utility。Base-model-only scope
  被至少一位 reviewer 标记为 major concern（"in practice people use instruct models"），需在 rebuttal 中
  强调 intentional contribution boundary + instruct 退化本身是 finding（OLMo-Instruct LOGO 0.338 vs 0.763 base）。
  Claim 3 negative finding 最稳固但 3 seeds + single perplexity metric 被认为 evidence 有限。
  72h 写作修复完成约 75-80%：核心 Results/Method 到位，但 Related Work 的 OOD detection 和 model collapse 文献
  覆盖不完整，Appendix 可视化粗糙。Overall 3.0-3.5，Findings borderline accept。

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      三部分分析：(A) Feature ablation: full vs surface-only vs reference-only,
      (B) DDR trend analysis per feature (Spearman ρ, KS statistics),
      (C) Perplexity pre-validation for Claim 3.
    expected_results:
      full_macro_f1: 0.820
      full_macro_ci: "[0.807, 0.833]"
      surface_only_f1: 0.763
      surface_only_ci: "[0.747, 0.774]"
      reference_only_f1: 0.719
      reference_only_ci: "[0.706, 0.733]"
      mcnemar_full_vs_surface_p: 0.0
      mcnemar_full_vs_reference_p: 0.0
      hapax_ratio_rho: -0.63
      ttr_rho: -0.61
      entropy_mean_rho: -0.60
      entropy_std_rho: -0.12
      entropy_min_rho: -0.35
      entropy_max_rho: 0.06
      tail_decay_rho: 0.04
      ks_drifting_range: "[0.516, 0.537]"
      ks_stationary_range: "[0.043, 0.052]"
      ks_gap_ratio: "~10x"
      median_ppl_by_depth: "13.50, 4.96, 3.00, 2.07, 1.72"
    result_rationale: >
      Median 档下 surface features（hapax -0.63, TTR -0.61）仍是最强 drift 信号源，surface-only
      达到 0.763，高于 reference-only 约 4.4pp。这意味着 vocabulary impoverishment 是 depth signal
      的主导机制。但 full 超过 surface +5.7pp（McNemar p≈0）确认 reference features 提供独立互补信号——
      entropy_mean 的 |ρ|=0.60 处于 drifting/moderate 边界，在 median 档的 reviewer 看来足以支撑
      "complementary" 但不足以 claim "independent dual dynamics"。DDR 呈现三梯度结构：strong drift
      (hapax, TTR, entropy_mean 的 |ρ|>0.60) vs moderate drift (entropy_min -0.35, entropy_std -0.12)
      vs near-stationary (entropy_max 0.06, tail_decay 0.04)。KS statistics 的 ~10x gap 为 DDR 提供
      非参数佐证，但 reviewer 可能指出 entropy_std 的 |ρ|=0.12 模糊了 drifting/stationary 分界——
      需在论文中明确将其归入 moderate drift 而非硬性二分。Perplexity 按深度单调递减（13.50→1.72）验证
      location shift 假说，为 Claim 3 pre-validation 成功。Decoding-agnostic 结果（greedy mean |d|=0.05
      for shape features）进一步强化了 DDR 的三梯度分类：shape features 在 greedy 和 top-k 下均
      保持 near-stationary，但 reviewer 认为仅两种策略不构成充分的 "agnostic" 证据。
    tables:
      - name: "Table: Feature Ablation (5-fold CV, Pythia-2.8B single generator)"
        columns: [Feature Set, Macro F1, 95% CI]
        rows:
          - [Full (7 features), 0.820, "[0.807, 0.833]"]
          - [Surface-only (TTR + hapax), 0.763, "[0.747, 0.774]"]
          - [Reference-only (5 entropy + tail_decay), 0.719, "[0.706, 0.733]"]
      - name: "Table: DDR Feature Classification"
        columns: [Feature, Spearman ρ, KS Statistic, DDR Group]
        rows:
          - [hapax_ratio, -0.63, 0.537, drifting]
          - [TTR, -0.61, 0.516, drifting]
          - [entropy_mean, -0.60, 0.528, drifting]
          - [entropy_min, -0.35, 0.052, moderate]
          - [entropy_std, -0.12, 0.043, moderate]
          - [entropy_max, 0.06, 0.048, near-stationary]
          - [tail_decay, 0.04, 0.045, near-stationary]
    figures_description:
      - >
        7-panel feature trend plot (mean ± std across depth 0-4)：hapax/TTR/entropy_mean 展示
        单调递减，entropy_min/std 平缓下降，entropy_max/tail_decay 近似水平线。
        三梯度视觉清晰。新增 greedy vs nucleus 对比子面板，shape features 两条线几乎重叠。
      - >
        Perplexity by depth bar chart：Pythia-410M ppl 单调下降 (13.50→1.72)，
        支持 NLL location shift 假说。
    analysis: >
      McNemar 确认 full > surface > reference，互补性成立。Surface 主导（+4.4pp over reference）
      意味着 reviewer 可能评价 reference features 的 marginal contribution 有限——这是 median 档的
      核心张力：DDR 作为概念有价值（drifting vs stationary 的 10x KS gap），但 practical 层面
      surface features 已捕获大部分信号。论文 Claim 2 需聚焦 DDR 的 interpretability 和
      diagnostic 价值而非 classification performance 增益。

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      扩展至 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)，
      LOGO 和 LOFO 评估跨 generator 和跨 family 泛化能力。
    expected_results:
      total_records: 18423
      generators: 5
      logo_avg_macro_f1: 0.804
      logo_avg_binary_f1: 0.694
      logo_binary_ci: "[0.688, 0.700]"
      lofo_binary_f1: 0.686
      per_gen_binary_f1:
        pythia_2_8b: 0.724
        pythia_1b: 0.721
        olmo_2_1b: 0.662
        qwen3_1_7b: 0.688
        qwen3_0_6b: 0.656
      per_gen_binary_f1_range: "0.656-0.724 (6.8pp spread)"
      family_out_delta: 0.008
      best_held_out_3class: "pythia-1b (0.851)"
      worst_held_out_3class: "olmo-2-1b (0.752)"
      ablation_full_f1: 0.804
      ablation_reference_only_f1: 0.754
      ablation_surface_only_f1: 0.747
      mcnemar_p: 0.0
      top_features: [hapax_ratio (0.289), ttr (0.168), entropy_mean (0.160)]
    result_rationale: >
      Median 档下 8-gen LOGO binary F1 = 0.694 [0.688, 0.700]，落在指定 findings_accept_prob
      区间的 "moderate" 位置。Reviewer 会认可 cross-generator generalization 的 effort（5 families,
      8 generators），但 0.694 不足以 claim practical utility——定位为 "first baseline establishing
      task feasibility"。Per-gen F1 range 6.8pp（0.656-0.724）在 median 档下是 acceptable variance，
      但 reviewer 会注意 Pythia 家族一致性偏高（2.8B: 0.724, 1B: 0.721），追问是否因为 Pythia-410M
      reference 与同家族 generator 有 architecture 亲和性。LOFO binary F1 = 0.686（vs LOGO 0.694，
      delta 仅 0.8pp）是强有力的 cross-family transfer 证据，但 reviewer 可能指出仅 3 families
      (Pythia, OLMo, Qwen) 的 LOFO 样本量不足以 fully claim family independence。3-class macro F1
      (0.804) 看起来更好但 inflated by gen-0 seed sharing——论文必须将 binary F1 作为 primary metric
      以避免 reviewer 质疑 evaluation integrity。Feature importance 排序（hapax > ttr > entropy_mean）
      跨 5 generators 稳定，确认 surface features 主导地位。
    tables:
      - name: "Table: LOGO Per-Generator Results (5 generators)"
        columns: [Generator, Family, Size, Binary F1, 3-class F1]
        rows:
          - [Pythia-2.8B, Pythia, 2.8B, 0.724, 0.812]
          - [Pythia-1B, Pythia, 1B, 0.721, 0.851]
          - [Qwen3-1.7B, Qwen, 1.7B, 0.688, 0.811]
          - [OLMo-2-1B, OLMo, 1.5B, 0.662, 0.752]
          - [Qwen3-0.6B, Qwen, 0.6B, 0.656, 0.819]
      - name: "Table: LOFO Cross-Family Transfer"
        columns: [Held-out Family, Binary F1, Delta vs LOGO]
        rows:
          - [Pythia, 0.678, -0.016]
          - [OLMo, 0.691, -0.003]
          - [Qwen, 0.689, -0.005]
          - [Average, 0.686, -0.008]
    figures_description:
      - >
        Per-generator LOGO binary F1 bar chart with CI whiskers，按 family 着色。
        Pythia 家族两个 bar 并列偏高，OLMo 和小 Qwen 偏低。水平线标注 LOGO average (0.694)。
      - >
        Feature importance stacked bar chart by generator：跨 5 generators hapax/ttr 始终
        占据 top-2，entropy_mean 稳定第三。视觉传达 feature ranking 的 cross-generator consistency。
    analysis: >
      0.694 binary F1 在 reviewer 眼中是 "moderate"——充分证明 task feasibility 但不足以
      支撑 deployment-ready tool 的 framing。LOFO delta 仅 0.8pp 是 cross-family 的强证据，
      但 median 档 reviewer 会追问 base-model-only 的限制。论文 headline 应报告
      "binary F1 = 0.694 [0.688, 0.700], ranging 0.656-0.724 across generators"。

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      测试 OLMo-2-1B 和 Qwen3-0.6B 作为 reference model 时 DDR 是否持续，
      验证 DDR 非 Pythia-specific artifact。
    expected_results:
      logo_f1_pythia_ref: 0.803
      logo_f1_olmo_ref: 0.807
      logo_f1_qwen_ref: 0.816
      logo_f1_range: "[0.803, 0.816] (1.3pp spread)"
      entropy_drift_all_refs_negative: true
      pythia_ref_drift_range: [-1.187, -1.402]
      olmo_ref_drift_range: [-0.608, -0.909]
      qwen_ref_drift_range: [-0.956, -1.346]
      tail_decay_rho_all_refs_abs_max: 0.07
      dual_dynamics_is_pythia_artifact: false
      greedy_shape_stability_all_refs: true
      greedy_mean_d_pythia: 0.05
      greedy_mean_d_olmo: 0.06
      greedy_mean_d_qwen: 0.05
    result_rationale: >
      Median 档下 DDR 确认非 Pythia 特有现象——三个 reference model 下 entropy drift 方向一致（均为
      负），LOGO F1 跨 ref 仅差 1.3pp (0.803-0.816)，说明 classifier 性能对 reference 选择不敏感。
      Qwen ref 略高（0.816），可能因其较小容量使 entropy 估计对 depth variation 更敏感。DDR 的
      drifting/stationary 分类在所有 ref 下保持：tail_decay 在三个 ref 下 |ρ| 均 <0.07，
      entropy_mean 始终为 drifting。Drift magnitude 跨 ref 有波动（Pythia ref 的 entropy_mean
      drift 最强 -1.187 to -1.402，OLMo 最弱 -0.608 to -0.909），但方向一致。Decoding-agnostic 维度
      进一步加强：greedy decoding 下三个 ref 的 shape stability 均成立（mean |d| 0.05-0.06），
      意味着 DDR 的 ref-independent + decoding-robust 双重验证成功。但 median 档 reviewer 的关切在于：
      (1) 三个 ref 全是 1B-scale base models，未测试更大或更小 ref；(2) greedy + top-k 仍只是两种
      decoding 策略；(3) ref 选择对 ρ 具体值影响明显（OLMo ref drift 约为 Pythia ref 的一半），
      虽然不影响分类方向但影响 DDR 的 quantitative characterization。论文应报告所有三个 ref 的
      range 而非挑最佳，承认 ρ magnitude 的 ref-dependence。
    tables:
      - name: "Table: Reference Model Comparison"
        columns: [Reference Model, Size, LOGO 3-class F1, entropy_mean drift, tail_decay |ρ|]
        rows:
          - [Pythia-410M, 410M, 0.803, "[-1.187, -1.402]", 0.05]
          - [OLMo-2-1B, 1.5B, 0.807, "[-0.608, -0.909]", 0.07]
          - [Qwen3-0.6B, 0.6B, 0.816, "[-0.956, -1.346]", 0.04]
      - name: "Table: Greedy Shape Stability Across References"
        columns: [Reference, Mean |d| (shape), Max |d| (shape), PASS]
        rows:
          - [Pythia-410M, 0.05, 0.14, "Yes"]
          - [OLMo-2-1B, 0.06, 0.15, "Yes"]
          - [Qwen3-0.6B, 0.05, 0.13, "Yes"]
    figures_description:
      - >
        3×7 heatmap：每个 reference model 下 7 个 feature 的 Spearman ρ。颜色编码 DDR 三梯度
        （deep red = strong drift, orange = moderate, gray = stationary）。跨行模式一致。
      - >
        Greedy vs top-k shape stability comparison 按 reference model 分面：shape features 的
        Cohen's d 值在两种 decoding + 三种 ref 下均 <0.15，视觉传达 decoding-robust + ref-robust。
    analysis: >
      DDR 非 artifact——方向一致、三梯度跨 ref 稳定、decoding-robust 双重验证。但 drift magnitude
      的 ref-dependence（OLMo ref drift 仅 Pythia ref 的 ~50%）提醒论文不应过度量化 DDR 的具体
      数值。Median 档 reviewer 接受 qualitative DDR pattern 但可能要求更多 ref 和 decoding 策略
      的消融，这在 72h 内不可行——rebuttal 中承认并建议 future work。

  - name: downstream_utility
    plan_id: plan_004
    description: >
      OLMo-1B fine-tune on depth-stratified data，3 seeds，bootstrap CIs，
      sample-count-matched control。验证 Claim 3 negative finding。
    expected_results:
      total_runs: 15
      all_ppl_mean: 2.335
      all_ppl_seeds: {seed_42: 2.335, seed_123: 2.335, seed_456: 2.335}
      size_matched_ppl_mean: 2.367
      size_matched_ppl_seeds: {seed_42: 2.367, seed_123: 2.367, seed_456: 2.367}
      depth01_ppl_mean: 2.387
      depth01_ppl_seeds: {seed_42: 2.388, seed_123: 2.387, seed_456: 2.387}
      binary_filtered_ppl_mean: 2.389
      binary_filtered_ppl_seeds: {seed_42: 2.389, seed_123: 2.389, seed_456: 2.389}
      depth0_only_ppl_mean: 2.681
      depth0_only_ppl_seeds: {seed_42: 2.682, seed_123: 2.680, seed_456: 2.682}
      ranking: "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)"
      tost_2pct_p: 1.1e-04
      tost_1pct_p: 0.09
      seed_variance: "<0.002 within variant"
      cohens_d_depth01_vs_matched: 0.45
    result_rationale: >
      Median 档下 Claim 3 negative finding 完全成立且是三个 claims 中最稳固的。Depth-aware curation
      不优于 random subsampling：size_matched (2.367) vs depth01 (2.387)，差异仅 0.020 perplexity
      points。TOST 在 ±2% margin 下显著（p = 1.1×10⁻⁴），确认统计等价性。但 ±1% margin 下不显著
      (p≈0.09)，reviewer 可指出精度受限于 3 seeds。Seed 间方差极小（<0.002）——这在 reviewer 看来
      既是 stability 证据也是 concern："3 seeds with near-zero variance suggests the outcome is
      deterministic, but doesn't test robustness to different data splits or hyperparameters"。
      depth0_only (2.681) 显著差归因于训练数据量不足（仅 797 样本），这是 data size effect 而非
      depth quality effect。Median 档 reviewer 接受 negative finding 但要求更多 downstream tasks
      （如 text classification, QA）以确认 "diagnostic not curative" 结论的 generality——
      72h 内无法补充，需 rebuttal 中承认为 limitation。Cohen's d = 0.45 中等，TOST 是更合适的检验。
    tables:
      - name: "Table: Downstream CLM Quality by Training Data Composition"
        columns: [Variant, Train Size, Perplexity (mean ± std), TOST p (±2%)]
        rows:
          - [All depths, 12299, "2.335 ± 0.0002", "—"]
          - [Size-matched random, 3951, "2.367 ± 0.0002", "ref"]
          - ["Depth 0+1 only", 3951, "2.387 ± 0.0005", "1.1×10⁻⁴"]
          - [Binary-filtered, 3951, "2.389 ± 0.0005", "~10⁻⁴"]
          - [Depth 0 only, 797, "2.681 ± 0.001", "reject equivalence"]
    figures_description:
      - >
        Bar chart with perplexity per variant，3 seed jitter points overlaid。
        all 和 size_matched 之间的 gap 归因于数据量（水平注释 "data size effect"），
        depth01 和 binary_filtered 几乎重叠，depth0_only 独立偏高。
      - >
        TOST margin sensitivity plot：x 轴 margin (±1%-5%)，y 轴 rejection p-value，
        ±2% 处 p 跌破 0.05 临界线，±1% 处 p 在 0.05 上方。
    analysis: >
      Negative finding 稳健。Depth fingerprinting 定位为 diagnostic tool。Reviewer concern
      集中在 "only perplexity metric, only CLM task"——rebuttal 承认 limitation 并强调
      depth-stratified evaluation 本身是 methodological contribution。

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Continuation vs elaboration vs inspired_rewriting chains，Pythia-2.8B，
      1000 seeds，leave-one-prompt-type-out evaluation。
    expected_results:
      cv_f1:
        continuation: 0.781
        inspired_rewriting: 0.737
        elaboration: 0.730
      lopto_f1:
        held_out_cont: 0.762
        held_out_elab: 0.762
        held_out_rewrite: 0.733
        avg: 0.753
      depth_retention_d4_d0:
        continuation: 0.831
        elaboration: 0.986
        rewriting: 0.939
      drift_hapax:
        continuation: -0.740
        elaboration: -0.828
        rewriting: -0.800
      drift_ttr:
        continuation: -0.607
        elaboration: -0.641
        rewriting: -0.618
      drift_entropy_mean:
        continuation: -0.557
        elaboration: -0.471
        rewriting: -0.477
    result_rationale: >
      Median 档下 continuation 信号最强（CV F1 0.781）因为直接续写累积 lexical diversity 压缩最显著；
      elaboration 最弱（0.730）因为 elaboration prompt 给模型更多 lexical 自由度。但三者差距仅 5.1pp
      （0.781 vs 0.730），reviewer 会视为 "moderate prompt-type dependence"。反直觉的是 elaboration
      的 hapax drift 最强（-0.828 vs continuation -0.740），但 entropy_mean drift 最弱（-0.471 vs
      -0.557）——这是因为 elaboration 保留了更多 semantic content 但 vocabulary 复用更 aggressive。
      CV F1 低于 hapax drift 所暗示的水平，因为 entropy features 在 elaboration 下退化。
      Depth retention 差异显著：continuation 仅保留 83.1% 的 chains 到 depth 4（更多
      degenerate outputs），而 elaboration 保留 98.6%。LOPTO cross-prompt transfer 合理
      (avg 0.753)，held-out rewriting 最低因其 drift profile 介于两端。
      Decoding-agnostic 维度未在此实验中独立测试，但 continuation chains 是 exp_062 decoding
      实验的主要 chain type，其结果（shape stability across greedy/top-k）可外推至 elaboration/rewriting。
    tables:
      - name: "Table: Prompt-Type Comparison"
        columns: [Prompt Type, CV F1, Depth Retention (d4/d0), hapax ρ, entropy_mean ρ]
        rows:
          - [Continuation, 0.781, 0.831, -0.740, -0.557]
          - [Inspired Rewriting, 0.737, 0.939, -0.800, -0.477]
          - [Elaboration, 0.730, 0.986, -0.828, -0.471]
      - name: "Table: LOPTO Cross-Prompt Transfer"
        columns: [Held-out Prompt, F1, Delta vs within-type CV]
        rows:
          - [Continuation, 0.762, -0.019]
          - [Elaboration, 0.762, +0.032]
          - [Rewriting, 0.733, -0.004]
    figures_description:
      - >
        3-panel feature drift plot by prompt type：continuation 的 entropy_mean 斜率最陡，
        elaboration 的 hapax 斜率最陡但 entropy_mean 最平。可视化 semantic freedom 与
        feature-level drift 的非一致性。
    analysis: >
      Prompt-type 依赖性存在但可控（max gap 5.1pp）。论文报告 "continuation F1 = 0.781 vs
      elaboration 0.730"，措辞用 "moderate prompt-type dependence"。Median 档 reviewer
      接受这个分析但可能要求 mixed-prompt-type evaluation（将三种 prompt 混合训练）——
      LOPTO 结果（0.753 avg）部分回答了这个问题。

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      构建 paraphrasing chains（语义保持的改写链）与 continuation chains 直接对比，
      测试 attractor convergence theory (ACL 2025 "LLM as Broken Telephone")。
    expected_results:
      paraphrastic_cv_binary_f1: 0.572
      paraphrastic_ci: "[0.552, 0.592]"
      continuation_cv_binary_f1: 0.695
      continuation_ci: "[0.678, 0.712]"
      delta_pp: 12.3
      paraphrastic_hapax_rho: -0.24
      paraphrastic_entropy_mean_rho: -0.12
      paraphrastic_ttr_rho: -0.20
      paraphrastic_attractor_convergence_depth: "~2.5"
      continuation_attractor_convergence_depth: ">4"
      paraphrastic_depth_retention_d4_d0: 0.97
      paraphrastic_3class_f1: 0.58
    result_rationale: >
      Median 档下 paraphrastic chains 的 binary F1 仅 0.572——显著高于 random (0.50) 但远低于
      continuation (0.695)，delta 12.3pp。Paraphrastic chains 因 semantic preservation 约束
      快速收敛到 attractor state：hapax_ratio |ρ| 仅 0.24（continuation 下 0.63），entropy_mean
      |ρ| 仅 0.12（continuation 下 0.60）。Attractor convergence 约在 depth 2.5 处——depth 3+
      的 paraphrastic text 在 feature space 中几乎不可区分。这与 ACL 2025 attractor cycle theory
      高度一致：paraphrasing 约束将分布锁定在有限的 attractor manifold 上，深度信号在 ~3 代后耗散。
      Continuation chains 无此约束，vocabulary diversity 持续压缩至 depth 4+。
      Median 档下 paraphrastic 的 0.572 已接近 binary classification 的 practical noise floor，
      reviewer 会视为 "minimal residual signal" 而非 "meaningful detection capability"。
      但差距本身（12.3pp）是有价值的 finding：它量化了 semantic constraint 对 depth signal 的
      抑制程度，连接了我们的 non-paraphrastic DDR 与 attractor theory 的理论框架。
      Decoding 维度：paraphrastic chains 的 shape stability 预期更强（因 attractor convergence
      压缩了所有维度的 variation），但这一点未独立验证。
    tables:
      - name: "Table: Paraphrastic vs Continuation Chains"
        columns: [Chain Type, Binary F1, 3-class F1, hapax ρ, entropy_mean ρ, Attractor Convergence]
        rows:
          - [Continuation, 0.695, 0.762, -0.63, -0.60, ">depth 4"]
          - [Paraphrastic, 0.572, 0.580, -0.24, -0.12, "~depth 2.5"]
    figures_description:
      - >
        Feature drift trajectory comparison：两条线 (continuation vs paraphrastic) 叠加，
        x 轴 depth 0-4，y 轴 normalized feature value。Paraphrastic 线在 depth 2-3 趋平，
        continuation 线持续下降。灰色 band 标注 "attractor region"。
      - >
        Per-depth binary F1 breakdown：continuation 在 depth 1-2 和 2-3 边界均有信号，
        paraphrastic 仅在 depth 1-2 边界有弱信号，depth 3+ pairs 接近 chance。
    analysis: >
      Paraphrastic comparison 确认 contribution scope：non-paraphrastic chains 是 DDR 的
      核心场景。Delta 12.3pp 是 Related Work 中与 ACL 2025 对话的关键数据点。Median 档 reviewer
      可能要求更 rigorous 的 paraphrasing protocol（当前用 LLM paraphrase，可能不完全保留语义），
      但这是 P1 实验，appendix 报告即可。

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains（每个 depth step 使用不同 generator）vs single-model chains，
      模拟真实 web contamination 中多 generator 混合场景。
    expected_results:
      cross_model_binary_f1: 0.830
      cross_model_binary_ci: "[0.815, 0.845]"
      cross_model_3class_f1: 0.789
      single_model_logo_binary_f1: 0.694
      delta_cross_vs_single_pp: 13.6
      cross_model_logo_5gen_binary_f1: 0.764
      cross_model_hapax_rho: -0.68
      cross_model_entropy_mean_rho: -0.55
      generator_level_logo_binary_f1: 0.830
    result_rationale: >
      Median 档下 cross-model chains 的 binary F1 = 0.830，显著高于 single-model LOGO (0.694)，
      delta 13.6pp。Architecture 差异在每个 depth step 引入额外 distributional shift，叠加在
      depth-intrinsic drift 上，使 depth signal 被放大。hapax ρ = -0.68（vs single-model -0.63）
      确认 cross-model 的 vocabulary diversity 压缩更 aggressive。但这个 amplification 在 median
      档的 reviewer 看来是 double-edged：(1) 高 F1 展示了 realistic scenario 下的 detection
      capability，支持 practical relevance；(2) 但 amplification 可能 confound depth signal
      与 architecture-switching signal——reviewer 会问 "are you detecting depth or just
      detecting model switches?"。Generator-level LOGO (5-gen subset) 的 0.830 binary F1
      说明即使在 leave-one-generator-out 条件下 cross-model signal 仍强。Cross-model LOGO
      (全 chain composition 泛化) 为 0.764，下降说明特定 generator 组合的 signal 不完全 transfer。
      Median 档的论文措辞应为 "heterogeneous chains show amplified depth signal (0.830),
      partly attributable to architecture-mixing effects" 而非 overclaim 为 "robust to any
      generator combination"。Decoding 维度未在 cross-model chains 上独立验证。
    tables:
      - name: "Table: Cross-Model vs Single-Model Chains"
        columns: [Evaluation, Binary F1, 95% CI, hapax ρ, entropy_mean ρ]
        rows:
          - ["Cross-model (generator-level LOGO, 5-gen)", 0.830, "[0.815, 0.845]", -0.68, -0.55]
          - ["Cross-model (composition LOGO)", 0.764, "[0.745, 0.783]", -0.65, -0.50]
          - ["Single-model (8-gen LOGO)", 0.694, "[0.688, 0.700]", -0.63, -0.60]
    figures_description:
      - >
        Paired bar chart: single-model LOGO vs cross-model F1 per evaluation setup，
        with CI whiskers。Cross-model 显著高出，视觉传达 amplification effect。
      - >
        Feature space PCA scatter：cross-model chains 的 depth clusters 更分离，
        single-model clusters 更重叠。
    analysis: >
      Cross-model amplification 是有价值的 finding 但需 careful framing。Reviewer 可能要求
      控制 architecture switch 效应——需在 rebuttal 中指出 LOGO evaluation 已部分控制
      （held-out generator 的 chain 包含 unseen architecture）。Median 档下 0.830 是 paper
      中最高的 headline-worthy binary F1，但不能替代 single-model LOGO (0.694) 作为 primary
      metric，因为 single-model 更 conservative。

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      扩展至 4 domains：Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts),
      code (programming)。500 seeds per domain × 5 depths。
    expected_results:
      wikipedia_baseline_binary_f1: 0.815
      wikipedia_baseline_ci: "[0.798, 0.832]"
      news_binary_f1: 0.746
      news_ci: "[0.726, 0.764]"
      academic_binary_f1: 0.739
      academic_ci: "[0.720, 0.757]"
      code_binary_f1: 0.754
      code_ci: "[0.737, 0.770]"
      max_gap_vs_wiki_pp: 7.6
      worst_domain: academic
      best_non_wiki_domain: code
      cross_domain_logo_binary_f1: 0.700
    result_rationale: >
      Median 档下各 domain 的 binary F1 落在 0.739-0.815 范围，max gap vs Wikipedia 约 7.6pp。
      Wikipedia 最高（0.815）因为 Wikipedia 是训练数据中的 primary domain（seeds 和 reference model
      的 training data 均含大量 Wikipedia），distributional match 最好。Academic 最低（0.739）
      因为科学文本 vocabulary 本身 specialized 且 diversity 较低——domain-intrinsic low diversity
      与 depth-induced diversity compression 方向一致，压缩了 feature margin。Code 略高于 academic
      （0.754）因为 code 的 structural patterns（indentation, function names）提供了额外
      distributional signal。News 居中（0.746）。Cross-domain LOGO 为 0.700，接近 overall LOGO
      (0.694)，说明 depth signal 是 domain-robust 的。
      Median 档 reviewer 注意到 Wikipedia baseline 显著偏高，可能追问 "is the method just
      fitting Wikipedia distribution?" —— cross-domain LOGO 回答了这个问题（0.700 on unseen domain）。
      差异 <8pp 足以 claim "moderate domain independence"，但需逐 domain 报告。
      Code domain 的表现有趣——LLM 对 code 的 recursive generation 保留了更多 structural regularity，
      使 entropy features 有更强的 discrimination power。
    tables:
      - name: "Table: Multi-Domain Binary F1"
        columns: [Domain, Binary F1, 95% CI, Seed Count]
        rows:
          - [Wikipedia, 0.815, "[0.798, 0.832]", 1000]
          - [Code, 0.754, "[0.737, 0.770]", 500]
          - [News, 0.746, "[0.726, 0.764]", 500]
          - [Academic, 0.739, "[0.720, 0.757]", 500]
    figures_description:
      - >
        Per-domain feature drift comparison：4 个 domain 的 hapax_ratio drift 线基本平行
        （slope 相近），但 academic domain 的 intercept 更低（初始 diversity 就低）。
        Code domain 的 entropy features 斜率更陡。
    analysis: >
      Depth signal 跨 domain 稳健，max gap 7.6pp。论文可 claim "domain-robust" 但需报告
      academic domain 的 ceiling 效应和 Wikipedia 的 distributional advantage。Median 档
      reviewer 接受 domain independence 但可能要求 creative writing domain（当前用 code 替代）。

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4)，测试 CORAL 和 Frank-Hall
      ordinal methods vs standard XGBoost。
    expected_results:
      xgboost_5class_f1: 0.50
      xgboost_5class_ci: "[0.48, 0.52]"
      coral_5class_f1: 0.50
      frank_hall_5class_f1: 0.49
      xgboost_3class_f1: 0.762
      gen1_vs_gen2_confusion_rate: 0.44
      gen2_vs_gen3_confusion_rate: 0.53
      gen3_vs_gen4_confusion_rate: 0.59
      gen0_5class_f1: 0.95
      gen4_5class_f1: 0.28
      binary_fn_concentration: 0.86
    result_rationale: >
      Median 档下 5-class F1 降至 ~0.50，ordinal methods (CORAL, Frank-Hall) 无改善（±1pp），
      确认 resolution ceiling。Gen-1/gen-2 边界是 bottleneck（44% confusion），gen-2/3 和
      gen-3/4 更差（53% 和 59%）。原因是 DDR 的 drifting features 在 depth 2+ 后 marginal
      change 递减——hapax/TTR 的 drift slope 在 depth 2-3 后趋平（lexical diversity 接近
      floor），entropy_mean 的 depth-wise change 在 depth 3+ 仅为 depth 0-1 change 的 ~25%。
      Feature space 中 gen-2/3/4 高度重叠，ordinal constraint 无法提供额外信号因为 features 本身
      已无法区分相邻深度。Gen-0 F1 ~0.95 因为 seed sharing 使 gen-0 独特可识别。
      86% 的 binary errors 集中在 FN（gen-2+ 被误判为 gen-1），说明 classifier 的主要失败模式
      是 miss deeper generations 而非 false alarm。这是 depth signal 的 intrinsic ceiling，
      不是 method limitation——即使 QLoRA end-to-end classifier 的 5-class F1 也仅 ~0.55。
      Median 档 reviewer 接受 3-class 为 practical resolution limit，这实际上加强了论文叙事：
      gen-0/gen-1/gen-2+ 三分法有 principled boundary（与 feature discriminability 对齐）。
    tables:
      - name: "Table: Ordinal Granularity Comparison"
        columns: [Method, 5-class F1, 3-class F1, Delta]
        rows:
          - [XGBoost (standard), 0.50, 0.762, -0.262]
          - [CORAL (ordinal), 0.50, "—", "—"]
          - [Frank-Hall (ordinal), 0.49, "—", "—"]
      - name: "Table: 5-Class Per-Depth F1"
        columns: [Depth, F1, Primary Confusion]
        rows:
          - [gen-0, 0.95, "—"]
          - [gen-1, 0.52, "→ gen-2"]
          - [gen-2, 0.35, "→ gen-1, gen-3"]
          - [gen-3, 0.30, "→ gen-2, gen-4"]
          - [gen-4, 0.28, "→ gen-3"]
    figures_description:
      - >
        5-class confusion matrix heatmap：gen-0 对角线深色（近完美），gen-1 有中等混淆，
        gen-2/3/4 的三行几乎互相混淆（off-diagonal 色块密集）。
      - >
        Per-depth feature separation violin plots：depth 0-1 gap 明显，depth 2-3-4 的
        feature distributions 高度重叠。
    analysis: >
      3-class resolution ceiling 确认。Ordinal methods 无额外增益——问题在 feature resolution
      而非 classifier architecture。论文明确报告 5-class 负面结果，定位 3-class 为
      "practical resolution limit aligned with feature discriminability boundary"。

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      模拟人工编辑鲁棒性：(A) Random word replacement (5%, 10%, 20%)，
      (B) LLM-simulated rephrasing (~1.7 sentences replaced per document)。
    expected_results:
      baseline_binary_f1: 0.695
      random_5pct_f1: 0.650
      random_5pct_drop_pp: -4.5
      random_10pct_f1: 0.614
      random_10pct_drop_pp: -8.1
      random_20pct_f1: 0.591
      random_20pct_drop_pp: -10.4
      llm_rephrase_binary_f1: 0.647
      llm_rephrase_binary_ci: "[0.631, 0.662]"
      llm_rephrase_drop_pp: -4.5
      llm_rephrase_multiclass_f1: 0.667
      llm_rephrase_multiclass_ci: "[0.655, 0.680]"
      edit_distance_ratio: 0.507
      avg_sentences_replaced: 1.69
    result_rationale: >
      Median 档下 LLM rephrase drop 为 4.5pp（0.695→0.647），与 random 5% replacement (4.5pp)
      几乎相同。这是因为 ~1.7 句 LLM rephrasing 对 vocabulary diversity features 的扰动量级
      与 5% random word replacement 相当——LLM rephrase 替换的是 coherent phrases（保留语法但
      改变用词），random replacement 破坏的是 individual tokens，两者对 hapax/TTR 的影响相似。
      10% (8.1pp drop) 和 20% (10.4pp drop) 展示 graceful degradation：20% replacement 后
      F1 仍为 0.591（显著高于 random baseline 0.50），说明 depth signal 在重度编辑下仍有微弱
      残留。Surface features (hapax, TTR) 是 most vulnerable 因为 random word insertion
      直接增加了 vocabulary diversity，部分抵消 depth-induced compression。Reference features
      (entropy) 对 word-level editing 更 robust 因为 sentence-level perplexity 对少量词替换
      不敏感。Median 档 reviewer 接受 "graceful degradation" 叙事但可能指出 LLM rephrase
      protocol 过于简单——real human editing 更 targeted 且 context-dependent。
    tables:
      - name: "Table: Robustness to Simulated Editing"
        columns: [Edit Type, Binary F1, Drop (pp), 95% CI]
        rows:
          - [None (baseline), 0.695, "—", "[0.679, 0.711]"]
          - [Random 5%, 0.650, -4.5, "[0.633, 0.667]"]
          - [Random 10%, 0.614, -8.1, "[0.596, 0.632]"]
          - [Random 20%, 0.591, -10.4, "[0.573, 0.609]"]
          - [LLM rephrase, 0.647, -4.5, "[0.631, 0.662]"]
    figures_description:
      - >
        Robustness degradation curve：x 轴 edit intensity (0%, 5%, 10%, 20%, LLM)，
        y 轴 binary F1。LLM rephrase 标注为菱形点，与 random 5% 高度接近。
        灰色虚线标注 random baseline (0.50)。
    analysis: >
      Signal 在 moderate editing 下 degrades gracefully。论文定位为 "robust to light editing
      (≤5pp drop at 5% or LLM rephrase), degrades under heavier perturbation"。
      Appendix 报告即可。Median 档下这不是 make-or-break experiment。

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      添加 LD-Score (character-level distribution signature) 作为第 8 个 feature，
      测试 character-level features 是否提供互补 depth signal。
    expected_results:
      eight_feat_logo_f1: 0.700
      seven_feat_logo_f1: 0.694
      delta_pp: 0.6
      ld_score_alone_logo_f1: 0.721
      ld_score_alone_cv_f1: 0.793
      ld_score_spearman_depth: -0.79
      ld_score_correlation_with_hapax: 0.75
      ld_score_xgb_importance: 0.042
    result_rationale: >
      Median 档下 LD-Score 作为第 8 个 feature 仅提供 +0.6pp marginal gain (0.694→0.700)，
      统计上 borderline significant。LD-Score 与 hapax_ratio 的相关高达 0.75——两者都捕获
      lexical diversity 的不同侧面（character-level vs word-level），信号高度冗余。
      LD-Score 单独的 ordinal Spearman ρ = -0.79（强），LOGO F1 = 0.721（高于 FastDetectGPT
      的 0.627 但低于 7-feature 的 0.694——因为 single feature 缺乏 multi-dimensional
      decision boundary）。实际上 LD-Score 在 plan-015 中作为 standalone baseline 已表现优异，
      但作为 8th feature 加入 ensemble 时与 hapax/TTR 的冗余使 marginal gain 微小。
      XGBoost importance 仅 0.042，排在所有 7 个原始 features 之后。
      Median 档论文选择保持 7-feature 设计并在 appendix/plan-015 comparison 中报告 LD-Score，
      避免增加模型复杂度。Character-level depth drift 的存在本身有学术价值（DDR 跨 granularity
      的佐证），但不改变核心叙事。
    tables:
      - name: "Table: LD-Score as Additional Feature"
        columns: [Feature Set, LOGO Binary F1, Delta vs 7-feat]
        rows:
          - [7 features, 0.694, "—"]
          - [7 features + LD-Score, 0.700, "+0.6pp"]
          - [LD-Score alone, 0.721, "+2.7pp*"]
      - name: "Note"
        columns: [Note]
        rows:
          - ["*LD-Score alone > 7-feat because it captures strong ordinal signal (ρ=-0.79), but single-feature variance is high across generators (CI [0.588, 0.770])"]
    figures_description:
      - >
        Feature correlation heatmap including LD-Score：LD-Score 与 hapax_ratio 色块最深
        (r=0.75)，与 ttr 次深 (r=0.68)。视觉解释冗余性。
    analysis: >
      LD-Score marginal value 有限（+0.6pp），不值得增加 feature set 复杂度。
      论文在 baseline comparison (plan-015) 中已充分利用 LD-Score 作为 standalone competitor。

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned end-to-end depth classifier (OLMo-2-1B, Qwen3-1.7B) vs
      handcrafted 7-feature XGBoost model。Base 和 Instruct 版本均测试。
    expected_results:
      qlora_olmo_instruct_3class_f1: 0.888
      qlora_olmo_instruct_3class_std: 0.007
      qlora_olmo_instruct_binary_f1: 0.836
      qlora_olmo_instruct_binary_std: 0.010
      qlora_qwen_instruct_3class_f1: 0.907
      qlora_qwen_instruct_3class_std: 0.008
      qlora_qwen_instruct_binary_f1: 0.867
      qlora_qwen_instruct_binary_std: 0.014
      qlora_olmo_base_3class_f1: 0.859
      qlora_olmo_base_binary_f1: 0.793
      qlora_qwen_base_3class_f1: 0.904
      qlora_qwen_base_binary_f1: 0.860
      qlora_5class_f1_range: "[0.540, 0.598]"
      seven_feat_3class_logo_f1: 0.762
      seven_feat_binary_logo_f1: 0.694
      delta_3class_best_qlora_vs_7feat: "+14.5pp"
      delta_binary_best_qlora_vs_7feat: "+17.3pp"
      qlora_logo_generalization: "not tested (single-generator within-CV only)"
      qlora_gpu_memory_gb: 8.5
      qlora_inference_time_ratio: "~12x"
    result_rationale: >
      Median 档下 QLoRA within-distribution performance 显著高于 7-feature（best QLoRA 3-class
      0.907 vs 7-feat LOGO 0.762, +14.5pp）。End-to-end model 可以学到 handcrafted features
      未捕获的 fine-grained distributional patterns——specific n-gram frequency shifts,
      positional entropy patterns, syntactic depth indicators。Qwen instruct > OLMo instruct
      (0.907 vs 0.888) 因为 Qwen 的 instruction following 更精准，分类 prompt 效果更好。
      但关键 caveat：QLoRA 仅在 within-generator CV 下评估（非 LOGO），不测试 cross-generator
      generalization。7-feature 的 LOGO evaluation 是 fundamentally harder setting——
      QLoRA 在 LOGO 下的表现预期大幅下降（~15-20pp），因为 end-to-end model 对 generator-specific
      artifacts 过拟合。5-class QLoRA（0.540-0.598）仍低，再次确认 resolution ceiling 非
      feature engineering 问题。Inference cost 12x + 8.5GB GPU memory 使 QLoRA 在
      practical deployment 中不 competitive。
      Median 档的论文定位：7-feature 的优势在于 "efficiency + cross-generator generalization +
      interpretability"，QLoRA 作为 within-distribution upper bound reference。Reviewer 可能
      要求 QLoRA LOGO evaluation 来公平比较——72h 内可能来不及，rebuttal 承认。
    tables:
      - name: "Table: End-to-End (QLoRA) vs Handcrafted Features"
        columns: [Method, Evaluation, 3-class F1, Binary F1, Cost]
        rows:
          - [7-feature XGBoost, "8-gen LOGO", 0.762, 0.694, "1× (CPU)"]
          - [QLoRA Qwen-Instruct, "within-gen CV", 0.907, 0.867, "~12× (GPU)"]
          - [QLoRA OLMo-Instruct, "within-gen CV", 0.888, 0.836, "~12× (GPU)"]
          - [QLoRA Qwen-Base, "within-gen CV", 0.904, 0.860, "~12× (GPU)"]
          - [QLoRA OLMo-Base, "within-gen CV", 0.859, 0.793, "~12× (GPU)"]
    figures_description:
      - >
        Radar chart：4 维比较 (CV F1, generalization, inference cost, memory)，
        7-feature 在 generalization 和 efficiency 维度占优，QLoRA 在 within-dist accuracy 占优。
        标注 "QLoRA LOGO not evaluated" 在 generalization 轴。
    analysis: >
      QLoRA 的 within-dist 优势不能直接与 7-feature LOGO 相比（evaluation setting 不同）。
      论文需明确标注 evaluation 差异，避免 misleading comparison。Median 档 reviewer 会
      质疑 fairness——rebuttal 中说明 LOGO 是 our contribution 的核心 evaluation protocol，
      QLoRA 仅作为 "what-if" upper bound。

  - name: text_length_control
    plan_id: plan_013
    description: >
      Text length confound analysis：(A) 长度-深度相关性分析，(B) length-normalized features，
      (C) length-matched classifier re-evaluation。
    expected_results:
      spearman_length_depth_range: "[-0.066, +0.134]"
      length_depth_correlation: "weak (|ρ|<0.14)"
      normalized_ttr_trend_preserved: true
      normalized_hapax_trend_preserved: true
      normalized_rho_stronger: true
      length_matched_binary_f1: 0.724
      unmatched_binary_f1: 0.770
      length_matched_f1_delta: "-4.6pp (but +4.1pp vs random subsample control)"
      length_is_confound: false
      dropout_short_text_bias: true
    result_rationale: >
      Median 档下 length-depth Spearman ρ 范围 [-0.066, +0.134]，|ρ| 均 <0.14，text length
      不是 depth signal 的驱动因素。Length normalization 后 TTR 和 hapax 的 depth drift 反而更强
      （normalized ρ stronger），因为去除了 length variation 带来的噪声——这是 strong deconfounding
      evidence。Length-matched subsampling 导致 binary F1 从 0.770 降至 0.724 (-4.6pp)，但
      random subsample control（相同 n）也从 0.770 降至约 0.730——说明 drop 主要来自样本量减少
      而非 length confound 移除。Net effect of length matching: +4.1pp vs 同等 sample size，
      实际上 length matching 略微提升了 F1 因为去除了 length-related noise。
      Depth-driven dropout 偏向短文本（深层 generation 更多 degenerate/short outputs 被 skip），
      但这是 generation process 的 intrinsic 特性而非统计 confound。
      Median 档 reviewer 满意于 length confound 排除——这是 paper credibility 的关键支撑，
      且 evidence 清晰无争议。
    tables:
      - name: "Table: Length Confound Analysis"
        columns: [Analysis, Result, Conclusion]
        rows:
          - ["Spearman ρ(length, depth)", "[-0.066, +0.134]", "Weak (|ρ|<0.14)"]
          - [Length-normalized feature drift, "preserved and stronger", "Depth signal independent of length"]
          - [Length-matched binary F1, "0.724 (vs 0.770 unmatched)", "Drop from sample size, not confound"]
          - [Random subsample control F1, "~0.730 (same n)", "Confirms sample size effect"]
    figures_description:
      - >
        Length distribution violin plot by depth (0-4)：各 depth 的 length 分布高度重叠，
        仅 depth 4 有轻微 left shift (shorter texts due to dropout)。
    analysis: >
      Length confound 清晰排除。Median 档下无争议——结论确定，evidence robust。

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      添加 Qwen3-8B-Base generator 测试 scale effect on depth signal。
      1000 seeds × 5 depths。
    expected_results:
      total_records: 4497
      unique_seeds: 995
      depth_dist: {gen0: 995, gen1: 979, gen2: 937, gen3: 831, gen4: 755}
      logo_6gen_avg_f1: 0.789
      logo_qwen3_8b_held_out_binary_f1: 0.683
      logo_qwen3_8b_ci: "[0.665, 0.701]"
      logo_5gen_baseline_f1: 0.800
      spearman:
        hapax_ratio: -0.558
        ttr: -0.542
        entropy_mean: -0.475
        entropy_min: -0.303
        entropy_max: 0.095
        tail_decay: -0.089
        entropy_std: -0.076
      feature_importance:
        hapax_ratio: 0.269
        entropy_mean: 0.164
        ttr: 0.159
    result_rationale: >
      Median 档下 Qwen3-8B held-out binary F1 = 0.683，落在合理的 scale degradation 范围。
      8B 模型在 6-gen LOGO 中表现最低（0.683），因为：(1) 大模型生成的文本更 fluent、vocabulary
      更 diverse、perplexity distribution 更 uniform，压缩了 depth drift margin；(2) 8B 的
      generation quality 使 gen-1 和 gen-2+ 之间的 distributional gap 更小。
      但 DDR 三梯度结构在 8B 上仍然成立：hapax (-0.558) 和 ttr (-0.542) 仍为 strong drift,
      entropy_mean (-0.475) moderate drift, tail_decay (-0.089) near-stationary。
      Scale effect 的量化：entropy_mean |ρ| 从 5-gen avg ~0.60 降至 0.475（-20%），但 hapax
      仅从 ~0.63 降至 0.558（-11%），确认 surface features 在 scale 增大时相对更 robust。
      6-gen LOGO avg F1 (0.789) vs 5-gen baseline (0.800)，8B 的加入仅拉低 1.1pp——整体
      影响温和。Depth retention: 755/995 (75.9%) 到 depth 4，低于 smaller models (~83-85%)，
      因为 8B 模型更容易在深层产生 degenerate outputs。
      Median 档的 reviewer 会注意 8B 的 moderate degradation 并追问 "what about 14B+?"——
      论文在 Limitations 中承认并建议 future work。Decoding-agnostic 在 8B 上的验证
      是通过 exp_062 完成的（8B greedy shape stability confirmed）。
    tables:
      - name: "Table: Scale Effect — DDR by Model Size (6 generators)"
        columns: [Generator, Size, Held-out Binary F1, hapax ρ, entropy_mean ρ]
        rows:
          - [Pythia-1B, 1B, 0.856, -0.63, -0.60]
          - [Qwen3-0.6B, 0.6B, 0.824, -0.58, -0.56]
          - [Pythia-2.8B, 2.8B, 0.804, -0.61, -0.60]
          - [Qwen3-1.7B, 1.7B, 0.805, -0.59, -0.55]
          - [OLMo-2-1B, 1.5B, 0.764, -0.60, -0.50]
          - [Qwen3-8B, 8B, 0.683, -0.558, -0.475]
    figures_description:
      - >
        Scale-DDR scatter plot：x 轴 log(model size)，y 轴 |ρ|。三条线：hapax（红，平缓下降），
        entropy_mean（蓝，陡峭下降），tail_decay（灰，始终 <0.10）。8B 处 hapax 和 entropy_mean
        分叉明显。趋势线附 R² 值。
    analysis: >
      Scale effect 确认但非 catastrophic：8B 仍可检测（0.683 >> random 0.50）。DDR 三梯度
      在 8B 上 qualitatively preserved。论文报告 scale degradation 为 honest limitation，
      强调 surface features 的 relative robustness to scale。Median 档下这是 acceptable—
      reviewer 认可 "studied up to 8B" 但会标注 ">14B frontier models" 为 gap。

  - name: ordinal_baseline_comparison
    plan_id: plan_015
    description: >
      对比 existing detector continuous scores (avg_logprob, LD-Score, FastDetectGPT,
      Binoculars) 作为 ordinal depth features vs 7-feature ensemble。
    expected_results:
      seven_feature_logo_f1: 0.798
      seven_feature_ci: "[0.786, 0.799]"
      avg_logprob_logo_f1: 0.765
      avg_logprob_ci: "[0.616, 0.820]"
      avg_logprob_spearman: -0.788
      ld_score_logo_f1: 0.721
      ld_score_ci: "[0.588, 0.770]"
      ld_score_spearman: -0.794
      fastdetectgpt_logo_f1: 0.627
      fastdetectgpt_ci: "[0.511, 0.762]"
      fastdetectgpt_spearman: -0.433
      binoculars_logo_f1: 0.579
      binoculars_ci: "[0.405, 0.664]"
      binoculars_spearman: -0.199
      bootstrap_delta_7feat_vs_avglogprob:
        delta: 0.033
        p: 0.0
        significant: true
      bootstrap_delta_7feat_vs_fdgpt:
        delta: 0.067
        p: 0.0
        significant: true
      seven_feat_advantage_pp: 3.3
    result_rationale: >
      Median 档下 7-feature vs best single detector (avg_logprob) 优势为 3.3pp (0.798 vs 0.765)，
      bootstrap 显著 (p<0.001)。但 avg_logprob 的 CI 极宽 [0.616, 0.820]——跨 generator
      方差大（部分 generators 上 avg_logprob 可达 ~0.82，其他降至 ~0.62），说明 single detector
      的 performance 对 generator identity 高度敏感。7-feature ensemble 的 CI [0.786, 0.799]
      显著更窄，体现了 multi-feature 组合的 robustness advantage。
      LD-Score (0.721) 作为 character-level feature 表现出色（Spearman -0.794），强于
      FastDetectGPT (0.627) 和 Binoculars (0.579)。LD-Score 的高 ordinal ρ (-0.794)
      与 avg_logprob (-0.788) 接近，说明 character-level 和 token-level depth signal
      强度相当——但两者与 7-feature ensemble 的差距证明 multi-dimensional features 的互补价值。
      FastDetectGPT 和 Binoculars 原为 binary detection 设计，repurpose 为 ordinal depth
      predictor 时 performance 大幅下降——depth 不等于 "real vs synthetic" 的 continuous
      extension，binary detection features 的 ordinal utility 有限。
      Median 档 reviewer 的关切：3.3pp advantage 是 "statistically significant but practically
      modest"。Rebuttal 策略：(1) contribution 不在 performance gap 而在 task formulation + DDR
      discovery，(2) 7-feature 的 narrow CI 展示 robustness 优势，(3) feature-level DDR 分析
      本身有 diagnostic value beyond classification。
      Decoding-agnostic 维度增强了 7-feature 的叙事：DDR 在 greedy/top-k 下稳定，意味着
      7-feature ensemble 在不同 decoding 设置下的 signal basis 不变——single detectors 未经
      decoding-robustness 验证。
    tables:
      - name: "Table: Ordinal Baseline Comparison (LOGO 3-class F1)"
        columns: [Method, LOGO F1, 95% CI, Spearman ρ, Type]
        rows:
          - [7-feature ensemble, 0.798, "[0.786, 0.799]", "—", multi-feature]
          - [Avg-LogProb, 0.765, "[0.616, 0.820]", -0.788, single-feature]
          - [LD-Score, 0.721, "[0.588, 0.770]", -0.794, single-feature]
          - [FastDetectGPT, 0.627, "[0.511, 0.762]", -0.433, single-detector]
          - [Binoculars, 0.579, "[0.405, 0.664]", -0.199, single-detector]
      - name: "Table: Bootstrap Pairwise Comparison (n=1000)"
        columns: [Comparison, Delta (pp), p-value, Significant]
        rows:
          - [7-feat vs Avg-LogProb, "+3.3", "<0.001", "Yes"]
          - [7-feat vs LD-Score, "+7.7", "<0.001", "Yes"]
          - [7-feat vs FastDetectGPT, "+17.1", "<0.001", "Yes"]
          - [7-feat vs Binoculars, "+21.9", "<0.001", "Yes"]
    figures_description:
      - >
        LOGO F1 bar chart with bootstrap CI whiskers：7-feature 的 narrow bar + tight CI 与
        single detectors 的 wider CI 形成对比。水平线标注 random baseline。
      - >
        Per-generator LOGO F1 parallel coordinates：7-feature 线相对平坦（cross-gen robust），
        avg_logprob 线波动大（某些 generators 高、某些低）。
    analysis: >
      7-feature 优势 3.3pp，statistically significant but practically modest。论文核心
      contribution 不在 classification performance 的绝对优势，而在 (a) 首次提出 ordinal
      depth estimation task，(b) DDR 的 empirical characterization（drifting vs stationary
      的 10x KS gap），(c) decoding-robustness 验证，(d) 7-feature 的 interpretability +
      narrow cross-generator variance。Median 档 reviewer 可能给 soundness 3.0-3.5，
      认为 contribution 足够 Findings 但 margin 偏紧。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a783c07-0f80-44e5-94d9-ee0ca0c95145",
  "isSidechain": false,
  "requestId": "req_011CbGSZ6ZDUHoy1fJHZJTGs",
  "type": "assistant",
  "uuid": "9d945ac3-5b92-48fe-a601-687f7b2a06c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbESnEZhBtTcsCNq5Yar9j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16740,
      "cache_read_input_tokens": 45422,
      "output_tokens": 26042,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16740,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26042,
          "cache_read_input_tokens": 45422,
          "cache_creation_input_tokens": 16740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16740
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DDR decoding-agnostic 被承认但 reviewer 认为 scope 限制削弱了 generalizability claim，需 rebuttal 或小幅调整后 borderline accept 核心假设：[\"Decoding-agnostic DDR 被认可为有意义的 robus…",
  "leafUuid": "9d945ac3-5b92-48fe-a601-687f7b2a06c2",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "DDR decoding-agnostic validation and writing-focused revision",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DDR decoding-agnostic 被承认但 reviewer 认为 scope 限制削弱了 generalizability claim，需 rebuttal 或小幅调整后 borderline accept 核心假设：[\"Decoding-agnostic DDR 被认可为有意义的 robus…",
  "leafUuid": "9d945ac3-5b92-48fe-a601-687f7b2a06c2",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "DDR decoding-agnostic validation and writing-focused revision",
  "sessionId": "6ac56804-240b-4d40-94ad-f71e723ec9d0"
}
```

---
