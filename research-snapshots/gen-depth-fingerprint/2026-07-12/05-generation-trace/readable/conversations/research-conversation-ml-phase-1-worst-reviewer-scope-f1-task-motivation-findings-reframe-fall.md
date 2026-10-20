# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Reviewer 认为 scope 太窄、F1 太低、task motivation 不足，Findings 被拒，需 reframe 后投 fall

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/3ea233fc-cde1-44e5-86de-1d80535bd3d7.jsonl`
- **Structured JSON:** [`a77c7fe96cc8f2f94b4b.json`](../../sessions/a7/a77c7fe96cc8f2f94b4b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T21:50:09.367Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T21:50:09.367Z",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Reviewer 认为 scope 太窄、F1 太低、task motivation 不足，Findings 被拒，需 reframe 后投 fallback venue\n核心假设：['多位 reviewer 认为 base-model-only + temperature [0.5,0.9] 的 scope 在 2026 年几乎没有实际意义——instruct/chat models 主导生成内容', '0.694 binary F1 被认为不足以支撑任何 classification claim——reviewer 指出 random baseline 在 balanced binary 是 0.5，0.694 的 margin 太小', 'Task formulation 本身被质疑：reviewer 认为 depth classification 是人造问题，real-world contamination 不遵循 clean chain 假设', 'DDR decoding-agnostic 被视为 incremental robustness check 而非贡献升级', \"Negative finding 被视为 'so the method has no practical use?'——加深了 motivation 质疑\", '写作未充分修复，presentation 问题加剧了 reviewer 负面印象']\n关键指标范围：{'avg_reviewer_overall': [2.0, 3.0], 'avg_soundness': [2.5, 3.0], 'findings_accept_prob': [0.05, 0.25], 'writing_fix_completion': [0.5, 0.7], 'effective_claim_strength_delta': ['+0.0', '+0.1'], 'reviewer_scope_concern_severity': [4, 5]}\n叙事方向：核心 framing 失效，需要找新 angle 但不降级目标（仍投同级 venue ICLR 2027 或 NAACL 2027）。Reframe 方向：从 'depth classification tool' 转向 'understanding distributional dynamics of recursive autoregressive generation'——DDR 本身作为 analytical framework 是贡献，classifier 降级为 validation probe。Paper 重心从 Claim 1 (classification performance) 转移到 Claim 2 (DDR characterization) + decoding-agnostic 作为主线。Title 从 'depth fingerprinting' 转向 'differential depth response in autoregressive text generation'。Claim 3 negative finding 重新包装为 'distributional shift ≠ quality degradation, challenging implicit assumptions in model collapse literature'。这个 reframe 放弃 practical utility 叙事，转向 understanding/characterization 贡献，更适合 Findings 的 empirical contribution 定位。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nvenue: emnlp-2026\nfocus: exp_062 decoding strategy 实验已全部完成（16/16），DDR 被确认为 decoding-agnostic。Reviewer 建议不做新 GPU 实验，72 小时全投写作修复。评估当前论文在 EMNLP 2026 Findings 的竞争力，重点关注：(1) decoding-agnostic DDR 是否能升级 claim 强度 (2) 写作修复的优先级 (3) 论文整体分数预期\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. **DDR is decoding-agnostic**: greedy decoding confirms shape stability across all 8 generators (mean |d|=0.05), establishing DDR as an autoregressive property independent of sampling truncation; top-k sampling preserves full DDR for non-Pythia/OLMo generators while model-intrinsic boundary effects account for remaining violations. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust across decoding strategies, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Greedy shape stability | mean |d|=0.05, max 0.14 | 8/8 generators PASS |\n| Top-k DDR preservation | 5/8 full DDR | 4/4 non-Pythia/OLMo PASS; failures model-intrinsic |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation_and_trend\n  description: 'Three-part analysis on existing MVP data (zero new generation): (A)\n    Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)\n    vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold\n    CV for each. (B) H1/H2 trend analysis: plot each feature''s mean ± std across\n    depth 0-4. Monotonic trend → H2 (divergence); plateau → H1 (convergence). Fit\n    linear regression per feature, report slope + R². (C) Perplexity pre-validation\n    for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets (no fine-tuning,\n    just forward pass). If perplexity varies significantly with depth → Claim 3 signal\n    exists.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: 'Uses existing MVP data + features.csv. Critical for Claim 2. Plan B if surface-only\n    ≈ full: reframe Claim 2 as \"complementary signal\" instead of \"independent signal\",\n    narrative shifts to \"vocabulary impoverishment as primary depth signal\".\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),\n    Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。) Leave-one-generator-out\n    CV to test cross-generator generalization. 1000 seeds × 5 generators × 5 depths\n    = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: 'Only proceed if plan_001 confirms reference features have independent or\n    complementary value. Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out\n    evaluation in analysis. Discuss limitation in paper if Pythia holdout performance\n    inflated by Pythia-1B in training set.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 2\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for\n    feature extraction. Addresses RC2 + critical test of Claim 2: verify entropy_mean\n    H2 drift persists with non-Pythia reference (if drift disappears → \"dual dynamics\"\n    is reference-model artifact, not generation-intrinsic). Also verify shape features\n    remain H1 across reference models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Importance elevated after D005: this is now the key falsification test for\n    Claim 2''s level/shape framework. If entropy_mean drift is Pythia-specific, the\n    entire dual dynamics narrative collapses.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)\n    on depth-stratified data subsets. Measure perplexity degradation on held-out test\n    set as function of training data depth. Compare depth-aware filtering vs binary\n    baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with bootstrap\n    CIs. Include sample-count-matched comparison (subsample depth-filtered to match\n    binary-filtered count) to control for data size confound.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_002\n  notes: 'Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,\n    (3) data size confound. All three addressed in updated design.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_013\n  claim:\n  - 1\n  - 2\n  name: text_length_control\n  description: 'Address text length confound (RC10, dream all three tiers): (A) Analyze\n    text length distributions by depth across all generators. (B) Compute length-normalized\n    surface features (TTR, hapax_ratio on fixed-length windows). (C) Length-matched\n    comparison: subsample to equalize length distributions across depths, re-evaluate\n    classifier. If length-controlled F1 drops significantly → surface features were\n    tracking length, not depth.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_002\n  notes: 'Zero new generation — analysis on existing data. Critical confound control\n    flagged by dream (all three tiers). Low cost, high impact on paper credibility.\n\n    '\n  status: planned\n- id: plan_014\n  claim: 1\n  name: large_scale_generator\n  description: 'Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth\n    signal persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current\n    generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  notes: 'Dream review flagged ≤2.8B as major limitation (all three tiers). If depth\n    signal weaker at scale → honest limitation with analysis. If comparable → strong\n    generalization evidence for the paper.\n\n    '\n  status: planned\n- id: plan_015\n  claim: 1\n  name: ordinal_baseline_comparison\n  description: 'CRITICAL missing baseline (flagged by both re-dreams, all three tiers):\n    Test whether existing detector continuous scores already provide ordinal depth\n    signal. Regress FastDetectGPT, Binoculars, and LD-Score continuous scores on generation\n    depth. Compare single-feature ordinal classifiers (each detector score as sole\n    feature) vs our 7-feature model. If existing detectors yield comparable ordinal\n    signal, our custom feature set contribution collapses.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_002\n  notes: 'Re-dream consensus: without this comparison, reviewers will question whether\n    depth-specific features add value. Must be in the paper. FastDetectGPT needs model\n    pair (source + reference), LD-Score is character-level, Binoculars needs two models.\n    If any single detector achieves >0.70 ordinal F1, we need to reframe our contribution\n    as \"complementary to existing detectors\" not \"novel approach.\"\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: initial_run_partial_issues_fixed_in_plan-001-fix\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.76\n    ablation_reference_only_f1: 0.72\n- exp_id: plan-001-fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_macro_f1: 0.8204\n    reference_only_f1: 0.7187\n    surface_only_f1: 0.7628\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    h2_features: entropy_mean, ttr, hapax_ratio\n    h1_features: tail_decay, entropy_std, entropy_max, entropy_min\n    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72\n- exp_id: plan-001-restore\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 18423\n    models: 4\n    pythia_1b:\n      records: 4555\n      seeds: 995\n      file: data/pythia-1b/generations.jsonl\n    olmo_2_1b:\n      records: 4713\n      seeds: 995\n      file: data/olmo-2-1b/generations.jsonl\n    qwen3_0_6b:\n      records: 4538\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 986\n        gen2: 938\n        gen3: 840\n        gen4: 778\n      file: data/qwen3-0.6b/generations.jsonl\n    qwen3_1_7b:\n      records: 4617\n      seeds: 996\n      depth_dist:\n        gen0: 996\n        gen1: 983\n        gen2: 941\n        gen3: 875\n        gen4: 822\n      file: data/qwen3-1.7b/generations.jsonl\n- exp_id: plan-002-pythia1b-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2286\n    seeds: 497\n    skipped: 91\n    wall_time_s: 2296.7\n    depth_dist:\n      gen0: 497\n      gen1: 497\n      gen2: 457\n      gen3: 429\n      gen4: 406\n    file: data/pythia-1b/generations_shard0.jsonl\n    file_size_mb: 2.5\n- exp_id: plan-002-pythia1b-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2269\n    seeds: 498\n    skipped: 100\n    wall_time_s: 2247.6\n    depth_dist:\n      gen0: 498\n      gen1: 496\n      gen2: 455\n      gen3: 422\n      gen4: 398\n    file: data/pythia-1b/generations_shard1.jsonl\n    file_size_mb: 2.44\n- exp_id: plan-002-olmo2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2379\n    seeds: 497\n    skipped: 47\n    wall_time_s: 3885.2\n    depth_dist:\n      gen0: 497\n      gen1: 494\n      gen2: 477\n      gen3: 461\n      gen4: 450\n    file: generations_shard0.jsonl\n    file_size_mb: 2.68\n- exp_id: plan-002-olmo2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2334\n    seeds: 498\n    skipped: 70\n    wall_time_s: 4081.2\n    depth_dist:\n      gen0: 498\n      gen1: 494\n      gen2: 470\n      gen3: 444\n      gen4: 428\n    file: generations_shard1.jsonl\n    file_size_mb: 2.57\n- exp_id: plan-002-qwen3-1_7b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen3-1_7b-s1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-retry-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s0\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen06b-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-002-qwen17b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2291\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 492\n      '2': 468\n      '3': 435\n      '4': 398\n    skipped: 199\n    duration_s: 4548.2\n    file_size_mb: 2.5\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen17b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2326\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 491\n      '2': 473\n      '3': 440\n      '4': 424\n    skipped: 53\n    duration_s: 4228\n    file: generations_shard1.jsonl\n- exp_id: plan-002-qwen06b-r2-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2270\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 468\n      '3': 423\n      '4': 388\n    file: generations_shard0.jsonl\n- exp_id: plan-002-qwen06b-r2-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 2268\n    seeds: 498\n    depth_dist:\n      '0': 498\n      '1': 493\n      '2': 470\n      '3': 417\n      '4': 390\n    file: generations_shard1.jsonl\n- exp_id: plan-002-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    leave_one_out_avg_macro_f1: 0.8037\n    best_held_out:\n      model: pythia-1b\n      macro_f1: 0.8507\n    worst_held_out:\n      model: olmo-2-1b\n      macro_f1: 0.7519\n    family_out_delta: 0.0107\n    ablation_full_f1: 0.8037\n    ablation_reference_only_f1: 0.7543\n    ablation_surface_only_f1: 0.7471\n    mcnemar_p: 0\n    top_features:\n    - hapax_ratio_0.289\n    - ttr_0.168\n    - entropy_mean_0.160\n    entropy_std_drop: 0.0049\n    entropy_std_drift: 0.12\n    entropy_mean_drift: 1.5\n- exp_id: plan-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    spearman_rho_range: '[-0.066, +0.134]'\n    length_depth_correlation: weak (|ρ|<0.14)\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    normalized_rho_stronger: true\n    length_matched_f1_delta: '+0.041'\n    length_is_confound: false\n    dropout_short_text_bias: true\n- exp_id: plan-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    logo_f1_pythia_ref: 0.8034\n    logo_f1_olmo_ref: 0.8072\n    logo_f1_qwen_ref: 0.8158\n    entropy_drift_all_refs_negative: true\n    olmo_ref_drift_range:\n    - -0.608\n    - -0.9089\n    qwen_ref_drift_range:\n    - -0.9557\n    - -1.3458\n    pythia_ref_drift_range:\n    - -1.1872\n    - -1.4017\n    dual_dynamics_is_pythia_artifact: false\n- exp_id: plan-015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci:\n    - 0.616\n    - 0.82\n    avg_logprob_spearman: 0.7876\n    ld_score_logo_f1: 0.7212\n    ld_score_ci:\n    - 0.588\n    - 0.77\n    ld_score_spearman: 0.7943\n    ld_score_pre_fix: 0.6854\n    fast_detect_gpt_logo_f1: 0.6269\n    fast_detect_gpt_ci:\n    - 0.511\n    - 0.762\n    fast_detect_gpt_spearman: 0.4325\n    binoculars_logo_f1: 0.579\n    binoculars_ci:\n    - 0.405\n    - 0.664\n    binoculars_spearman: 0.1989\n    binoculars_bug_confirmed: true\n    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer,\n      shifted_ids)\n    bootstrap_n: 1000\n    bootstrap_delta_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_delta_7feat_vs_fdgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n    best_single_detector: Avg-LogProb (0.7653)\n    seven_feature_advantage_pp: 3.3\n- exp_id: plan-004-prep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: OLMo-2-0425-1B (1485M)\n    datasets:\n      depth0_only:\n        train: 797\n        test: 3138\n      depth01:\n        train: 3951\n        test: 3138\n      all:\n        train: 12299\n        test: 3138\n      size_matched:\n        train: 3951\n        test: 3138\n      binary_filtered:\n        train: 3951\n        test: 3138\n    dry_run_loss: 2.18\n    script: finetune_downstream.py\n- exp_id: plan-003-olmo2ref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-003-qwen06bref\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4497\n    unique_seeds: 995\n    depth_dist:\n      '0': 995\n      '1': 979\n      '2': 937\n      '3': 831\n      '4': 755\n    logo_6gen_avg_f1: 0.7893\n    logo_per_generator:\n      olmo-2-1b: 0.7635\n      pythia-1b: 0.8562\n      pythia-2.8b: 0.8041\n      qwen3-0.6b: 0.8243\n      qwen3-1.7b: 0.8046\n      qwen3-8b: 0.6832\n    logo_qwen3_8b_held_out_f1: 0.6832\n    logo_5gen_baseline_f1: 0.8\n    spearman:\n      hapax_ratio: -0.5578\n      ttr: -0.5419\n      entropy_mean: -0.4754\n      entropy_min: -0.3029\n      entropy_max: 0.0946\n      tail_decay: -0.0894\n      entropy_std: -0.0755\n    feature_importance:\n      hapax_ratio: 0.269\n      entropy_mean: 0.1637\n      ttr: 0.159\n      entropy_max: 0.0634\n      entropy_std: 0.0463\n      entropy_min: 0.0153\n      tail_decay: 0.0123\n    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\n    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness\n- exp_id: plan-004\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan-004-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_runs: 15\n    completed: 15\n    variants:\n      all:\n        eval_loss_mean: 0.848\n        perplexity_mean: 2.335\n        seeds:\n          '42':\n            eval_loss: 0.848\n            ppl: 2.335\n          '123':\n            eval_loss: 0.848\n            ppl: 2.335\n          '456':\n            eval_loss: 0.8482\n            ppl: 2.3354\n      size_matched:\n        eval_loss_mean: 0.8617\n        perplexity_mean: 2.367\n        seeds:\n          '42':\n            eval_loss: 0.8618\n            ppl: 2.367\n          '123':\n            eval_loss: 0.8615\n            ppl: 2.367\n          '456':\n            eval_loss: 0.8618\n            ppl: 2.367\n      depth01:\n        eval_loss_mean: 0.8701\n        perplexity_mean: 2.387\n        seeds:\n          '42':\n            eval_loss: 0.8703\n            ppl: 2.3877\n          '123':\n            eval_loss: 0.87\n            ppl: 2.3869\n          '456':\n            eval_loss: 0.8699\n            ppl: 2.387\n      binary_filtered:\n        eval_loss_mean: 0.8709\n        perplexity_mean: 2.389\n        seeds:\n          '42':\n            eval_loss: 0.8708\n            ppl: 2.389\n          '123':\n            eval_loss: 0.871\n            ppl: 2.389\n          '456':\n            eval_loss: 0.871\n            ppl: 2.389\n      depth0_only:\n        eval_loss_mean: 0.9864\n        perplexity_mean: 2.681\n        seeds:\n          '42':\n            eval_loss: 0.9865\n            ppl: 2.6818\n          '123':\n            eval_loss: 0.9863\n            ppl: 2.68\n          '456':\n            eval_loss: 0.9865\n            ppl: 2.6817\n    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389)\n      << depth0_only(2.681)\n    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）\n- exp_id: plan-015-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seven_feature_logo_f1: 0.798\n    seven_feature_ci95:\n    - 0.786\n    - 0.799\n    avg_logprob_logo_f1: 0.7653\n    avg_logprob_ci95:\n    - 0.616\n    - 0.82\n    ld_score_logo_f1: 0.7212\n    ld_score_ci95:\n    - 0.588\n    - 0.77\n    fastdetectgpt_logo_f1: 0.6269\n    fastdetectgpt_ci95:\n    - 0.511\n    - 0.762\n    binoculars_logo_f1: 0.579\n    binoculars_ci95:\n    - 0.405\n    - 0.664\n    binoculars_bug_fixed: true\n    ld_score_corrected_cv_f1: 0.7925\n    bootstrap_7feat_vs_avglogprob:\n      delta: 0.039\n      p: 0\n      significant: true\n    bootstrap_7feat_vs_fastdetectgpt:\n      delta: 0.067\n      p: 0\n      significant: true\n- exp_id: plan-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_f1:\n      continuation: 0.7806\n      inspired_rewriting: 0.7368\n      elaboration: 0.73\n    lopto_f1:\n      held_out_cont: 0.762\n      held_out_elab: 0.7622\n      held_out_rewrite: 0.7334\n      avg: 0.7525\n    depth_retention_d4_d0:\n      continuation: 0.831\n      inspired_rewriting: 0.939\n      elaboration: 0.986\n    drift_hapax_ratio:\n      continuation: -0.74\n      elaboration: -0.828\n      rewriting: -0.8\n    drift_ttr:\n      continuation: -0.607\n      elaboration: -0.641\n      rewriting: -0.618\n    drift_entropy_mean:\n      continuation: -0.557\n      elaboration: -0.471\n      rewriting: -0.477\n    spearman_ttr:\n      continuation: -0.629\n      elaboration: -0.666\n      rewriting: -0.659\n    spearman_hapax:\n      continuation: -0.651\n      elaboration: -0.674\n      rewriting: -0.67\n    spearman_entropy_mean:\n      continuation: -0.665\n      elaboration: -0.583\n      rewriting: -0.564\n- exp_id: plan-005-cont\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4620\n    unique_seeds: 995\n    skipped: 168\n    depth_distribution:\n      '0': 995\n      '1': 992\n      '2': 932\n      '3': 874\n      '4': 827\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\n    file_size_mb: 4.93\n    runtime_seconds: 7760\n    speed_seeds_per_sec: 0.13\n- exp_id: plan-005-elab\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4946\n    unique_seeds: 995\n    skipped: 14\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 989\n      '3': 986\n      '4': 981\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\n    file_size_mb: 5.53\n    runtime_seconds: 8960.2\n    depth_retention_d4_d0: 0.986\n    logo_cv_f1:\n      mean: 0.73\n      std: 0.011\n    lopto_f1: 0.7622\n    feature_drift_entropy_mean: -0.4705\n    feature_drift_ttr: -0.6413\n    feature_drift_hapax: -0.8284\n    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration\n      chains more stable but depth signal weaker within-type\n    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability,\n      elaboration slightly lower\n- exp_id: plan-005-rewrite\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 4827\n    unique_seeds: 995\n    skipped: 61\n    depth_distribution:\n      '0': 995\n      '1': 995\n      '2': 959\n      '3': 944\n      '4': 934\n    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\n    file_size_mb: 5.41\n    runtime_seconds: 8584\n    speed_seeds_per_sec: 0.12\n    depth_retention_d4_d0: 0.939\n    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more\n      stable depth chains\n- exp_id: review-exp-a-baseline-ensemble\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: review-exp-b-topic-drift\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    semantic_similarity_by_transition:\n      0_to_1:\n        mean: 0.622\n        std: 0.1647\n      1_to_2:\n        mean: 0.6829\n        std: 0.1837\n      2_to_3:\n        mean: 0.801\n        std: 0.2012\n      3_to_4:\n        mean: 0.8587\n        std: 0.1895\n    prompt_type_avg_sim:\n      continuation: 0.7168\n      elaboration: 0.8093\n      inspired_rewriting: 0.808\n    shape_feature_correlations:\n      entropy_std_rho: -0.1639\n      tail_decay_rho: 0.0675\n    drifting_feature_correlations:\n      hapax_ratio_rho: -0.1242\n      ttr_rho: -0.1784\n      entropy_mean_rho: -0.2859\n- exp_id: review-exp-c-overall-ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_logo_f1: 0.7879\n    overall_ci95:\n    - 0.783\n    - 0.7929\n    spearman_entropy_max: 0.0503\n    spearman_entropy_min: -0.4061\n    spearman_hapax: -0.6467\n    spearman_ttr: -0.6302\n    spearman_entropy_mean: -0.6098\n    spearman_entropy_std: -0.1996\n    spearman_tail_decay: -0.0403\n- exp_id: plan-010-robustness\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    baseline_binary_f1: 0.695\n    5pct_binary_f1: 0.65\n    10pct_binary_f1: 0.614\n    20pct_binary_f1: 0.591\n    5pct_drop: -0.046\n    10pct_drop: -0.081\n    20pct_drop: -0.104\n- exp_id: plan-010-llm-rephrase\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_binary_f1: 0.6918\n    original_binary_ci:\n    - 0.6749\n    - 0.7067\n    original_multiclass_f1: 0.7385\n    original_multiclass_ci:\n    - 0.7269\n    - 0.7496\n    rephrased_binary_f1: 0.6471\n    rephrased_binary_ci:\n    - 0.6308\n    - 0.6619\n    rephrased_multiclass_f1: 0.6672\n    rephrased_multiclass_ci:\n    - 0.6548\n    - 0.6796\n    binary_drop: -0.0447\n    multiclass_drop: -0.0713\n    edit_distance_ratio: 0.5071\n    avg_sentences_replaced: 1.69\n    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\n    bugs_fixed:\n    - binary_task_gen1_vs_gen2+\n    - 3class_mapping\n    - tail_decay_rank100-1000\n- exp_id: plan-008-seed-stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_complexity_binary: 0.685\n    medium_binary: 0.695\n    high_complexity_binary: 0.695\n    low_complexity_multi: 0.772\n    medium_multi: 0.778\n    high_complexity_multi: 0.779\n    max_diff_binary_pp: 1.06\n    max_diff_multiclass_pp: 0.68\n    conclusion_label: seed_independent\n- exp_id: multi-domain-seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7459\n    news_binary_ci:\n    - 0.726\n    - 0.764\n    news_multiclass_f1: 0.6516\n    academic_binary_f1: 0.7386\n    academic_binary_ci:\n    - 0.72\n    - 0.757\n    academic_multiclass_f1: 0.6223\n    code_binary_f1: 0.7535\n    code_binary_ci:\n    - 0.737\n    - 0.77\n    code_multiclass_f1: 0.6344\n    wikipedia_baseline_binary_f1: 0.8148\n    wikipedia_baseline_multiclass_f1: 0.8632\n    max_gap_vs_wiki_pp: 7.62\n    worst_domain: academic\n    best_domain: code\n    conclusion_label: domain_independent\n- exp_id: exp_047_multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    news_binary_f1: 0.7119\n    news_binary_ci:\n    - 0.6898\n    - 0.7332\n    news_3class_f1: 0.7149\n    academic_binary_f1: 0.6279\n    academic_binary_ci:\n    - 0.6027\n    - 0.6515\n    academic_3class_f1: 0.6564\n    code_binary_f1: 0.6872\n    code_binary_ci:\n    - 0.6641\n    - 0.71\n    code_3class_f1: 0.6729\n    overall_binary_f1: 0.6757\n    overall_3class_f1: 0.6814\n    delta_vs_t10_news: -0.034\n    delta_vs_t10_academic: -0.1107\n    delta_vs_t10_code: -0.0663\n- exp_id: multi_domain_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_048_cross_temp_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    6gen_logo:\n      within_0.7_binary: 0.9471\n      within_0.7_3class: 0.7888\n      cross_0.7to1.0_binary: 0.9001\n      cross_0.7to1.0_3class: 0.7225\n      within_1.0_binary: 0.9107\n      within_1.0_3class: 0.7257\n      cross_1.0to0.7_binary: 0.9581\n      cross_1.0to0.7_3class: 0.7913\n      caveat: Only Qwen3-1.7B differs between conditions; 5/6 generators share data\n    qwen_only:\n      within_0.7_binary: 0.9262\n      within_0.7_binary_ci:\n      - 0.916\n      - 0.935\n      within_0.7_3class: 0.769\n      within_0.7_3class_ci:\n      - 0.756\n      - 0.781\n      cross_0.7to1.0_binary: 0.7574\n      cross_0.7to1.0_binary_ci:\n      - 0.745\n      - 0.77\n      cross_0.7to1.0_3class: 0.4581\n      cross_0.7to1.0_3class_ci:\n      - 0.445\n      - 0.472\n      within_1.0_binary: 0.8248\n      within_1.0_binary_ci:\n      - 0.81\n      - 0.838\n      within_1.0_3class: 0.5738\n      within_1.0_3class_ci:\n      - 0.56\n      - 0.588\n      cross_1.0to0.7_binary: 0.9443\n      cross_1.0to0.7_binary_ci:\n      - 0.936\n      - 0.953\n      cross_1.0to0.7_3class: 0.6014\n      cross_1.0to0.7_3class_ci:\n      - 0.593\n      - 0.611\n      delta_0.7train_binary_pp: -16.9\n      delta_0.7train_3class_pp: -31.1\n      delta_1.0train_binary_pp: 12\n      delta_1.0train_3class_pp: 2.8\n      asymmetric_transfer: true\n- exp_id: exp_049_temp_curve_t05\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    records: 4708\n    skipped: 113\n    seeds: 995\n    model: pythia-2.8b\n    temperature: 0.5\n    top_p: 0.9\n    within_cv_binary_f1: 0.8432\n    within_cv_binary_ci:\n    - 0.8301\n    - 0.8558\n    logo_binary_f1: 0.8136\n    logo_binary_ci:\n    - 0.7984\n    - 0.8282\n    entropy_mean_rho: -0.5844\n- exp_id: exp_050_temp_curve_t09\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    records: 4536\n    model: pythia-2.8b\n    temperature: 0.9\n    top_p: 0.9\n    within_cv_binary_f1: 0.5821\n    within_cv_binary_ci:\n    - 0.5655\n    - 0.5985\n    logo_binary_f1: 0.4804\n    logo_binary_ci:\n    - 0.4645\n    - 0.4976\n    entropy_mean_rho: -0.3016\n    delta_vs_t07_cv: -0.157\n    delta_vs_t07_logo: -0.259\n- exp_id: exp_051_independent_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_to_olmo_binary_f1: 0.6945\n    pythia_to_olmo_ci:\n    - 0.6727\n    - 0.7167\n    olmo_to_pythia_binary_f1: 0.666\n    olmo_to_pythia_ci:\n    - 0.6429\n    - 0.6893\n    avg_binary_f1: 0.6803\n    shared_seed_logo_ref: 0.694\n    delta_vs_shared: -0.014\n- exp_id: exp_052_instruct_qwen3_1_7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8753\n    within_binary_ci:\n    - 0.8667\n    - 0.8837\n    within_3class_f1: 0.7324\n    within_3class_ci:\n    - 0.7195\n    - 0.745\n    base_binary_f1: 0.8614\n    base_3class_f1: 0.769\n    logo_instruct_binary: 0.658\n    logo_instruct_3class: 0.543\n    logo_base_binary: 0.821\n    logo_base_3class: 0.802\n    gen1_f1_instruct: 0.438\n    gen1_f1_base: 0.579\n    spearman_direction: reversed (instruct ρ>0, base ρ<0)\n    delta_within_binary: 0.014\n    delta_within_3class: -0.037\n    delta_logo_binary: -0.163\n- exp_id: exp_053_instruct_olmo2_1b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_binary_f1: 0.8131\n    within_binary_ci:\n    - 0.8012\n    - 0.8251\n    within_3class_f1: 0.5748\n    within_3class_ci:\n    - 0.5605\n    - 0.5897\n    base_binary_f1: 0.8454\n    base_3class_f1: 0.7538\n    gen1_f1_instruct: 0.256\n    gen1_f1_base: 0.523\n    delta_within_binary: -0.032\n    delta_within_3class: -0.179\n    spearman_instruct:\n      entropy_mean: 0.482\n      entropy_std: 0.296\n      entropy_min: 0.08\n      entropy_max: 0.306\n      tail_decay: 0.228\n      ttr: 0.006\n      hapax_ratio: 0.025\n    spearman_base:\n      entropy_mean: -0.639\n      entropy_std: -0.296\n      entropy_min: -0.387\n      entropy_max: 0.067\n      tail_decay: -0.141\n      ttr: -0.7\n      hapax_ratio: -0.712\n    features_reversed: 6/7\n    model_used: allenai/OLMo-2-0425-1B-Instruct\n- exp_id: exp_054_instruct_llama3_2_3b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    instruct_binary_f1: 0.8381\n    instruct_binary_ci:\n    - 0.828\n    - 0.847\n    instruct_3class_f1: 0.5437\n    instruct_3class_ci:\n    - 0.53\n    - 0.558\n    base_binary_f1: 0.8488\n    base_3class_f1: 0.7424\n    rho_instruct_entropy_mean: 0.2299\n    rho_instruct_entropy_std: 0.2623\n    rho_instruct_entropy_min: -0.0027\n    rho_instruct_entropy_max: 0.2036\n    rho_instruct_tail_decay: 0.1198\n    rho_instruct_ttr: -0.1411\n    rho_instruct_hapax_ratio: -0.1157\n    rho_base_entropy_mean: -0.627\n    rho_base_ttr: -0.6856\n    rho_base_hapax_ratio: -0.6975\n    direction_reversals: 3\n    reversed_features:\n    - entropy_mean\n    - entropy_std\n    - tail_decay\n    data_count: 4974\n- exp_id: exp_055_qlora_olmo_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8881\n    macro_f1_3class_std: 0.0071\n    macro_f1_5class: 0.5976\n    macro_f1_5class_std: 0.0046\n    binary_f1: 0.8363\n    binary_f1_std: 0.0096\n    n_samples: 4429\n    runtime_seconds: 1689.7\n- exp_id: exp_056_qlora_qwen_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.9066\n    macro_f1_3class_std: 0.0082\n    macro_f1_5class: 0.5514\n    macro_f1_5class_std: 0.0031\n    binary_f1: 0.8672\n    binary_f1_std: 0.0137\n    n_samples: 4963\n    runtime_seconds: 1880.5\n- exp_id: exp_055b_qlora_olmo_base\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.8588\n    macro_f1_3class_std: 0.0036\n    macro_f1_5class: 0.5398\n    macro_f1_5class_std: 0.015\n    binary_f1: 0.7925\n    binary_f1_std: 0.0097\n    n_samples: 2379\n    runtime_seconds: 911.7\n    note: completed before kill signal\n- exp_id: exp_056b_qlora_qwen_base\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1_3class: 0.904\n    macro_f1_3class_std: 0.0094\n    macro_f1_5class: 0.5544\n    macro_f1_5class_std: 0.0068\n    binary_f1: 0.8597\n    binary_f1_std: 0.0123\n    n_samples: 2291\n    runtime_seconds: 880.9\n    note: completed before kill signal\n- exp_id: exp_057_scale_9gen_logo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: superseded by exp_057 (rerun with fixed Gemma data)\n    first_run_3class_f1: 0.7516\n    first_run_binary_f1: 0.6842\n    see_exp_057_for_final: true\n- exp_id: exp_058_ddr_causality\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    permutation_baseline_f1: 0.7714\n    drifting_avg_importance: 0.1578\n    stationary_avg_importance: 0.0297\n    drifting_stationary_ratio: 5.31\n    granger_significant_features: 6/7\n    granger_max_delta_r2: 0.031\n    granger_max_delta_r2_feature: entropy_std\n    granger_nonsig_feature: entropy_min\n    granger_panel_n: 29095\n    intervention_max_f1_drop: 0.0203\n    intervention_max_feature: entropy_max\n    intervention_min_f1_drop: 0.0061\n- exp_id: exp_059_tost_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_bootstrap: 1000\n    seed: 42\n    margin_d: 0.2\n    entropy_max:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.062\n      d_ci:\n      - 0.037\n      - 0.088\n    entropy_min:\n      median_p: 0\n      rejection_rate: 1\n      median_d: -0.016\n      d_ci:\n      - -0.042\n      - 0.011\n    tail_decay:\n      median_p: 0\n      rejection_rate: 1\n      median_d: 0.088\n      d_ci:\n      - 0.065\n      - 0.111\n    entropy_std:\n      median_p: 1\n      rejection_rate: 0\n      median_d: 0.458\n      d_ci:\n      - 0.435\n      - 0.479\n    stationary_features_robust: true\n- exp_id: exp_057\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    9gen_logo_3class_f1: 0.751\n    9gen_logo_binary_f1: 0.6661\n    8gen_baseline_3class_f1: 0.7698\n    delta_9gen_vs_8gen: -0.0188\n    n_total_rows: 42015\n    n_generators: 9\n    qwen3_8b_3class_f1: 0.6955\n    qwen3_8b_binary_f1: 0.6468\n    gemma_2_2b_3class_f1: 0.6279\n    gemma_2_2b_binary_f1: 0.4402\n    per_gen_3class_f1:\n      pythia-1b: 0.8571\n      qwen3-0.6b: 0.8185\n      pythia-2.8b: 0.8117\n      qwen3-1.7b: 0.8114\n      olmo-2-1b: 0.7732\n      llama-3.2-3b: 0.7591\n      qwen3-8b: 0.6955\n      gemma-2-2b: 0.6279\n      mistral-7b-v0.3: 0.6045\n    tail_decay_consistency: VERIFIED_all_9gen_logprob_slope\n    data_source: features_9gen.csv (42015 rows, Gemma fixed)\n- exp_id: exp_060_14b_ddr_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 2229\n    n_seeds: 498\n    depth_distribution:\n      '0': 498\n      '1': 488\n      '2': 466\n      '3': 414\n      '4': 363\n    entropy_mean:\n      rho: -0.3877\n      d: 0.7765\n      group: drifting\n    entropy_std:\n      rho: -0.0557\n      d: -0.0223\n      group: stationary\n    entropy_max:\n      rho: 0.0791\n      d: -0.1717\n      group: stationary\n    entropy_min:\n      rho: -0.2471\n      d: -0.1365\n      group: stationary\n    ttr:\n      rho: -0.4916\n      d: 1.0913\n      group: drifting\n    hapax_ratio:\n      rho: -0.5065\n      d: 1.1245\n      group: drifting\n    tail_decay:\n      rho: -0.0637\n      d: 0.1356\n      group: stationary\n    ddr_pattern_match: true\n- exp_id: exp_061_instruct_ref_ddr\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwen_instruct:\n      base_ref_rho_entropy_mean: 0.478\n      instruct_ref_rho_entropy_mean: 0.221\n      base_ref_d_entropy_mean: 1.981\n      instruct_ref_d_entropy_mean: 1.022\n    olmo_instruct:\n      base_ref_rho_entropy_mean: 0.482\n      instruct_ref_rho_entropy_mean: -0.113\n      base_ref_d_entropy_mean: 1.33\n      instruct_ref_d_entropy_mean: 0.017\n- exp_id: decoding_strategy_shape\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_062_decoding_strategy_shape\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T21:50:09.370Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T21:50:09.370Z",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-21T21:50:09.389Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Reviewer 认为 scope 太窄、F1 太低、task motivation 不足，Findings 被拒，需 reframe 后投 fallback venue
核心假设：['多位 reviewer 认为 base-model-only + temperature [0.5,0.9] 的 scope 在 2026 年几乎没有实际意义——instruct/chat models 主导生成内容', '0.694 binary F1 被认为不足以支撑任何 classification claim——reviewer 指出 random baseline 在 balanced binary 是 0.5，0.694 的 margin 太小', 'Task formulation 本身被质疑：reviewer 认为 depth classification 是人造问题，real-world contamination 不遵循 clean chain 假设', 'DDR decoding-agnostic 被视为 incremental robustness check 而非贡献升级', "Negative finding 被视为 'so the method has no practical use?'——加深了 motivation 质疑", '写作未充分修复，presentation 问题加剧了 reviewer 负面印象']
关键指标范围：{'avg_reviewer_overall': [2.0, 3.0], 'avg_soundness': [2.5, 3.0], 'findings_accept_prob': [0.05, 0.25], 'writing_fix_completion': [0.5, 0.7], 'effective_claim_strength_delta': ['+0.0', '+0.1'], 'reviewer_scope_concern_severity': [4, 5]}
叙事方向：核心 framing 失效，需要找新 angle 但不降级目标（仍投同级 venue ICLR 2027 或 NAACL 2027）。Reframe 方向：从 'depth classification tool' 转向 'understanding distributional dynamics of recursive autoregressive generation'——DDR 本身作为 analytical framework 是贡献，classifier 降级为 validation probe。Paper 重心从 Claim 1 (classification performance) 转移到 Claim 2 (DDR characterization) + decoding-agnostic 作为主线。Title 从 'depth fingerprinting' 转向 'differential depth response in autoregressive text generation'。Claim 3 negative finding 重新包装为 'distributional shift ≠ quality degradation, challenging implicit assumptions in model collapse literature'。这个 reframe 放弃 practical utility 叙事，转向 understanding/characterization 贡献，更适合 Findings 的 empirical contribution 定位。

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
  "promptId": "00fafa99-9202-4e1a-8fd4-c2e127d8de99",
  "type": "user",
  "uuid": "6a5d92ed-1bc8-49f5-a6f9-19bb630c7997",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T21:50:09.387Z_

```json
{
  "parentUuid": "6a5d92ed-1bc8-49f5-a6f9-19bb630c7997",
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
  "uuid": "34723650-8788-4138-8028-eba1912ade71",
  "timestamp": "2026-05-21T21:50:09.387Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T21:50:09.387Z_

```json
{
  "parentUuid": "34723650-8788-4138-8028-eba1912ade71",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f9308770-088e-45af-b7b5-0be5e29ad93f",
  "timestamp": "2026-05-21T21:50:09.387Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Reviewer 认为 scope 太窄、F1 太低、task motivation 不足，Findings 被拒，需 reframe 后投 fallback venue 核心假设：['多位 reviewer 认为 base-model-only + temperature [0.5,0.9] 的 scop…",
  "leafUuid": "f9308770-088e-45af-b7b5-0be5e29ad93f",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe depth-fingerprinting to distributional-dynamics characterization",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7"
}
```

---

### Assistant

_source line 8 · 2026-05-21T21:50:23.863Z_

I'll review the experiment plan and the completed registry data to generate detailed worst-tier predictions for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9308770-088e-45af-b7b5-0be5e29ad93f",
  "isSidechain": false,
  "requestId": "req_011CbGTCzBJWCMcnWS3XEe26",
  "type": "assistant",
  "uuid": "706efb67-b750-49f1-b689-fddaaa33f23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9qSJwTo8X76Yo5ZBHKXjr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25055,
      "cache_read_input_tokens": 11841,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25055,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 237,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25055
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

_source line 9 · 2026-05-21T21:50:27.918Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FvistywNMngjbkbpRKT3AF`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan and registry",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0514_3, find all files related to experiment plans, registry, paper framing, and any existing tier predictions or imagined experiment outputs. Look for YAML files, markdown files, and any files under directories like \"experiments\", \"plans\", \"results\", \"tiers\", \"predictions\", \"imagined\". Also check for any files named like \"experiment_plan*\", \"registry*\", \"paper_framing*\", \"worst*\", \"best*\", \"expected*\". Search broadly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "706efb67-b750-49f1-b689-fddaaa33f23a",
  "isSidechain": false,
  "requestId": "req_011CbGTCzBJWCMcnWS3XEe26",
  "type": "assistant",
  "uuid": "963f5300-a32c-4f5d-9fe7-f905ddb2bc9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9qSJwTo8X76Yo5ZBHKXjr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25055,
      "cache_read_input_tokens": 11841,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25055,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 237,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25055
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

_source line 10 · 2026-05-21T21:51:13.366Z_

<details><summary>↩ Tool result · `toolu_01FvistywNMngjbkbpRKT3AF`</summary>

```text
Perfect! Now I have comprehensive information about the experiments, plans, and predictions. Let me create a summary of all the files I found:

## Summary of Found Files

I've successfully located all experiment plans, registry, paper framing, and prediction files in the repository. Here are the key findings:

### Main Experiment and Plan Files

1. **Experiment Plan**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml` — Comprehensive plan with 15 experiments (P0/P1/P2 priority), ~116.5 GPU hours budget, covering feature ablation, cross-generator evaluation, downstream utility, and more

2. **Paper Framing Document**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md` — Full paper positioning, 3 core claims, scope/limitations, story spine, anticipated reviewer concerns, contribution positioning for Findings venue

### Registry Files

- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.lock`
- Global registry files at `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/global/registry.yaml`

### Dream Reports with Tier Predictions

The most comprehensive set of "imagined experiments" and output predictions organized by tier (best/median/worst) are in dream report directories. Each has complete expected results and narrative guidance:

**Latest comprehensive report (dream_20260520T232427):**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/imagined_experiments.yaml`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/median/imagined_experiments.yaml`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/worst/imagined_experiments.yaml`

Plus paper framing and review context at each tier:
- `paper_framing.md` — Narrative framing per tier
- `review_context.yaml` — Expected review scores and criteria
- `review_report.md` — Detailed reviewer perspectives

**Other dream reports available:**
- dream_20260514T181213, dream_20260514T221538, dream_20260516T105241, dream_20260516T155725, dream_20260520T100349 (all with best/median/worst tiers)

### Imagined Experiment Details

Each tier contains expected results for 15 experiments including:
1. Feature ablation and trend (plan_001)
2. Cross-generator evaluation (plan_002)
3. Cross-family reference model (plan_003)
4. Downstream utility - Claim 3 (plan_004)
5. Prompt type comparison (plan_005)
6. Paraphrastic comparison (plan_006)
7. Cross-model chains (plan_007)
8. Multi-domain seeds (plan_008)
9. Finer-grained ordinal (plan_009)
10. Human edit robustness (plan_010)
11. LD-Score feature (plan_011)
12. End-to-end classifier (plan_012)
13. Text length control (plan_013)
14. Large-scale generator effect (plan_014)
15. Ordinal baseline comparison (plan_015)

### Key Tier Predictions Summary

**Best Tier:** DDR (Differential Depth Response) binary/solid across 8+ generators, 0.694 LOGO F1, strong complementarity evidence, negative downstream finding confirmed
**Median Tier:** Moderate evidence, boundary signals, architecture-dependent DDR, ~0.675 LOGO F1, three-gradient feature classification
**Worst Tier:** Fundamental criticism of DDR as vocabulary impoverishment repackaging, low cross-family generalization (~0.62), domain/temperature/instruct sensitivity, weak practical utility (0.694 vs 0.95 binary detectors)

All files are production-ready YAML with detailed expected_results blocks, result_rationale sections, and markdown narrative guidance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "963f5300-a32c-4f5d-9fe7-f905ddb2bc9b",
  "isSidechain": false,
  "promptId": "00fafa99-9202-4e1a-8fd4-c2e127d8de99",
  "type": "user",
  "uuid": "4eda27f3-cdc1-46ab-ae7a-4a376c6db64a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0514_3, find all files related to experiment plans, registry, paper framing, and any existing tier predictions or imagined experiment outputs. Look for YAML files, markdown files, and any files under directories like \"experiments\", \"plans\", \"results\", \"tiers\", \"predictions\", \"imagined\". Also check for any files named like \"experiment_plan*\", \"registry*\", \"paper_framing*\", \"worst*\", \"best*\", \"expected*\". Search broadly.",
    "agentId": "ab7b917c57c5b9e1d",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information about the experiments, plans, and predictions. Let me create a summary of all the files I found:\n\n## Summary of Found Files\n\nI've successfully located all experiment plans, registry, paper framing, and prediction files in the repository. Here are the key findings:\n\n### Main Experiment and Plan Files\n\n1. **Experiment Plan**\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml` — Comprehensive plan with 15 experiments (P0/P1/P2 priority), ~116.5 GPU hours budget, covering feature ablation, cross-generator evaluation, downstream utility, and more\n\n2. **Paper Framing Document**\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md` — Full paper positioning, 3 core claims, scope/limitations, story spine, anticipated reviewer concerns, contribution positioning for Findings venue\n\n### Registry Files\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.lock`\n- Global registry files at `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/global/registry.yaml`\n\n### Dream Reports with Tier Predictions\n\nThe most comprehensive set of \"imagined experiments\" and output predictions organized by tier (best/median/worst) are in dream report directories. Each has complete expected results and narrative guidance:\n\n**Latest comprehensive report (dream_20260520T232427):**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/imagined_experiments.yaml`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/median/imagined_experiments.yaml`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/worst/imagined_experiments.yaml`\n\nPlus paper framing and review context at each tier:\n- `paper_framing.md` — Narrative framing per tier\n- `review_context.yaml` — Expected review scores and criteria\n- `review_report.md` — Detailed reviewer perspectives\n\n**Other dream reports available:**\n- dream_20260514T181213, dream_20260514T221538, dream_20260516T105241, dream_20260516T155725, dream_20260520T100349 (all with best/median/worst tiers)\n\n### Imagined Experiment Details\n\nEach tier contains expected results for 15 experiments including:\n1. Feature ablation and trend (plan_001)\n2. Cross-generator evaluation (plan_002)\n3. Cross-family reference model (plan_003)\n4. Downstream utility - Claim 3 (plan_004)\n5. Prompt type comparison (plan_005)\n6. Paraphrastic comparison (plan_006)\n7. Cross-model chains (plan_007)\n8. Multi-domain seeds (plan_008)\n9. Finer-grained ordinal (plan_009)\n10. Human edit robustness (plan_010)\n11. LD-Score feature (plan_011)\n12. End-to-end classifier (plan_012)\n13. Text length control (plan_013)\n14. Large-scale generator effect (plan_014)\n15. Ordinal baseline comparison (plan_015)\n\n### Key Tier Predictions Summary\n\n**Best Tier:** DDR (Differential Depth Response) binary/solid across 8+ generators, 0.694 LOGO F1, strong complementarity evidence, negative downstream finding confirmed\n**Median Tier:** Moderate evidence, boundary signals, architecture-dependent DDR, ~0.675 LOGO F1, three-gradient feature classification\n**Worst Tier:** Fundamental criticism of DDR as vocabulary impoverishment repackaging, low cross-family generalization (~0.62), domain/temperature/instruct sensitivity, weak practical utility (0.694 vs 0.95 binary detectors)\n\nAll files are production-ready YAML with detailed expected_results blocks, result_rationale sections, and markdown narrative guidance."
      }
    ],
    "totalDurationMs": 45443,
    "totalTokens": 84132,
    "totalToolUseCount": 27,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 9540,
      "cache_read_input_tokens": 73498,
      "output_tokens": 1090,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 1090,
          "cache_read_input_tokens": 73498,
          "cache_creation_input_tokens": 9540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9540,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 15,
      "bashCount": 4,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "963f5300-a32c-4f5d-9fe7-f905ddb2bc9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T21:51:16.415Z_

<details open><summary>🔧 Tool call — Read · `toolu_019qQ29pbzMGt9inLLPxYS3D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eda27f3-cdc1-46ab-ae7a-4a376c6db64a",
  "isSidechain": false,
  "requestId": "req_011CbGTHhgVu4EhDE5cHCLW2",
  "type": "assistant",
  "uuid": "92e64cfd-212d-4aef-9db8-90e1f7213744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CvU3xuVaxvt1yL5ZZXypD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 36896,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 36896,
          "cache_creation_input_tokens": 1335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1335
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

_source line 12 · 2026-05-21T21:51:17.042Z_

<details><summary>↩ Tool result · `toolu_019qQ29pbzMGt9inLLPxYS3D`</summary>

```text
1	tier: worst
2	narrative_guidance: 'Paper receives avg 2.5–3.0. Core attacks: (1) DDR ≈ vocabulary
3	  impoverishment repackaging, surface-only gap too small to justify a new framework;
4	  (2) base-model-only + temperature-sensitive + instruct collapse = fatal scope limitation
5	  for any practical framing; (3) 0.694 binary F1 compared unfairly against binary
6	  detection baselines (>0.95), labeled ''not actionable''; (4) Claim 3 negative finding
7	  weaponized as ''why does this matter''; (5) 33-page paper criticized as unfocused
8	  experiment dump. Reframe direction: pivot from ''depth classification as a tool''
9	  to ''empirical study of recursive generation dynamics'' or ''complementary signal
10	  for existing detectors''. Neither requires new experiments.
11	
12	  '
13	imagined_experiments:
14	- name: feature_ablation_and_trend
15	  plan_id: plan_001
16	  description: 'Surface-only vs reference-only vs full 7-feature ablation on MVP data
17	    (Pythia-2.8B, ~4600 records). XGBoost 5-fold CV. Trend analysis per feature across
18	    depth 0–4. Perplexity pre-validation for Claim 3.
19	
20	    '
21	  expected_results:
22	    full_macro_f1: 0.773
23	    surface_only_f1: 0.741
24	    reference_only_f1: 0.698
25	    surface_vs_full_gap_pp: 3.2
26	    mcnemar_p_surface_vs_full: 0.027
27	    hapax_ratio_slope: -0.063
28	    hapax_ratio_r2: 0.88
29	    ttr_slope: -0.041
30	    ttr_r2: 0.82
31	    entropy_mean_slope: -0.089
32	    entropy_mean_r2: 0.79
33	    tail_decay_slope: 0.003
34	    tail_decay_r2: 0.04
35	    entropy_std_slope: -0.031
36	    entropy_std_r2: 0.41
37	    entropy_max_slope: 0.008
38	    entropy_max_r2: 0.07
39	    ppl_depth0: 14.2
40	    ppl_depth2: 3.8
41	    ppl_depth4: 1.9
42	  result_rationale: 'Surface-only 达到 0.741（vs full 0.773），差距仅 3.2 pp。McNemar p=0.027
43	    虽然显著但 marginal。在 worst 档中，审稿人会 argue "surface features capture 96% of the signal"
44	    (0.741/0.773=0.959)，reference features 只是 marginal add-on，不构成独立 contribution。
45	    entropy_std 的 R²=0.41 模糊了 drifting/stationary 的 clean split —— 审稿人可以 argue 这不是
46	    bimodal response 而是 continuous degradation gradient，DDR 概念 overclaims。 Trend analysis
47	    显示所有 drifting features 都沿同一方向（单调递减），审稿人会 argue 这就是 well-known vocabulary impoverishment
48	    的多种测量方式，不是新现象。
49	
50	    '
51	  tables:
52	  - caption: 'Feature ablation: 5-fold CV macro F1 on Pythia-2.8B MVP data'
53	    rows:
54	    - - Feature Set
55	      - Macro F1
56	      - 95% CI
57	      - Δ vs Full
58	    - - Full (7 features)
59	      - '0.773'
60	      - '[0.758, 0.788]'
61	      - —
62	    - - Surface-only (TTR + hapax)
63	      - '0.741'
64	      - '[0.724, 0.758]'
65	      - −3.2 pp
66	    - - Reference-only (5 entropy)
67	      - '0.698'
68	      - '[0.679, 0.717]'
69	      - −7.5 pp
70	  - caption: Per-feature depth trend (linear regression on depth 0–4)
71	    rows:
72	    - - Feature
73	      - Category
74	      - Slope
75	      - R²
76	      - Spearman ρ
77	    - - hapax_ratio
78	      - Drifting
79	      - −0.063
80	      - '0.88'
81	      - −0.63
82	    - - TTR
83	      - Drifting
84	      - −0.041
85	      - '0.82'
86	      - −0.61
87	    - - entropy_mean
88	      - Drifting
89	      - −0.089
90	      - '0.79'
91	      - −0.60
92	    - - entropy_std
93	      - Ambiguous
94	      - −0.031
95	      - '0.41'
96	      - −0.20
97	    - - entropy_min
98	      - Stationary
99	      - −0.018
100	      - '0.22'
101	      - −0.15
102	    - - tail_decay
103	      - Stationary
104	      - '+0.003'
105	      - '0.04'
106	      - '+0.04'
107	    - - entropy_max
108	      - Stationary
109	      - '+0.008'
110	      - '0.07'
111	      - '+0.05'
112	  figures_description:
113	  - 7-panel feature trend plot showing mean ± std across depth 0–4. Drifting features
114	    (hapax, TTR, entropy_mean) show clear monotonic decline but with overlapping error
115	    bars at adjacent depths. entropy_std occupies an ambiguous middle zone (visible
116	    drift but high variance). Stationary features (tail_decay, entropy_max) are flat.
117	    Reviewer will highlight entropy_std ambiguity and overlapping error bars as evidence
118	    that the 'clean bimodal split' is overstated.
119	  analysis: '在 worst 档下，这个实验的核心问题是 surface-vs-full gap 太小。3.2 pp 差距在审稿人看来 不足以证明 reference
120	    features 提供了 qualitatively different signal。entropy_std 的 R²=0.41 处于 drifting/stationary
121	    之间的灰色地带，破坏了 DDR 作为 clean bimodal phenomenon 的叙事。审稿人会写："The authors'' distinction
122	    between ''drifting'' and ''stationary'' features appears to be a gradient rather
123	    than a dichotomy, and the surface features alone capture the vast majority of
124	    the signal, suggesting this is vocabulary impoverishment measured differently
125	    rather than a novel phenomenon."
126	
127	    '
128	- name: cross_generator_evaluation
129	  plan_id: plan_002
130	  description: 'Expand to 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B,
131	    Qwen3-0.6B). Leave-one-generator-out (LOGO) CV. 1000 seeds × 5 generators × 5
132	    depths ≈ 23K chains.
133	
134	    '
135	  expected_results:
136	    total_records: 22800
137	    logo_avg_macro_f1: 0.762
138	    logo_avg_binary_f1: 0.68
139	    logo_binary_ci:
140	    - 0.672
141	    - 0.688
142	    logo_per_gen_binary:
143	      pythia_2_8b: 0.711
144	      pythia_1b: 0.724
145	      olmo_2_1b: 0.643
146	      qwen3_1_7b: 0.668
147	      qwen3_0_6b: 0.655
148	    logo_per_gen_range_pp: 8.1
149	    lofo_binary_f1: 0.665
150	    lofo_pythia_out_f1: 0.621
151	    lofo_qwen_out_f1: 0.648
152	    pythia_within_family_inflation: 0.038
153	  result_rationale: 'LOGO binary F1 = 0.680，低于论文 framing 中的 0.694（后者是 8-gen 版本，但这里只有
154	    5-gen， 训练数据更少）。更关键的是 per-generator variance 很大：Pythia-1B 在 hold-out 时最好 （0.724），因为
155	    Pythia-2.8B 在训练集中提供了 same-family signal。OLMo-2-1B 最差（0.643）， 因为它是唯一的 non-Pythia/non-Qwen
156	    family。LOFO 进一步降到 0.665，Pythia held-out 降到 0.621 —— 这说明跨 family 泛化比 LOGO 差很多。审稿人会
157	    argue Pythia family overlap inflates LOGO by ~3.8 pp，真实 cross-family performance
158	    只有 0.62–0.65，远不够 practical。 8.1 pp per-gen range 被视为 high variance = unreliable。
159	
160	    '
161	  tables:
162	  - caption: Leave-one-generator-out binary F1 (gen-1 vs gen-2+)
163	    rows:
164	    - - Held-out Generator
165	      - Family
166	      - Binary F1
167	      - 95% CI
168	    - - Pythia-2.8B
169	      - Pythia
170	      - '0.711'
171	      - '[0.693, 0.729]'
172	    - - Pythia-1B
173	      - Pythia
174	      - '0.724'
175	      - '[0.707, 0.741]'
176	    - - OLMo-2-1B
177	      - OLMo
178	      - '0.643'
179	      - '[0.621, 0.665]'
180	    - - Qwen3-1.7B
181	      - Qwen
182	      - '0.668'
183	      - '[0.648, 0.688]'
184	    - - Qwen3-0.6B
185	      - Qwen
186	      - '0.655'
187	      - '[0.634, 0.676]'
188	    - - '**Average**'
189	      - —
190	      - '**0.680**'
191	      - '[0.672, 0.688]'
192	  - caption: Leave-one-family-out binary F1
193	    rows:
194	    - - Held-out Family
195	      - Binary F1
196	      - Δ vs LOGO avg
197	    - - Pythia (both)
198	      - '0.621'
199	      - −5.9 pp
200	    - - Qwen (both)
201	      - '0.648'
202	      - −3.2 pp
203	    - - OLMo
204	      - '0.726'
205	      - +4.6 pp
206	    - - '**Average**'
207	      - '**0.665**'
208	      - '**−1.5 pp**'
209	  figures_description:
210	  - Confusion matrix heatmap (5 panels, one per held-out generator) showing gen-0/gen-1/gen-2+
211	    predictions. All 5 panels show gen-1 vs gen-2+ confusion as the dominant error
212	    — gen-1 frequently misclassified as gen-2+ (FN rate 78–89% of binary errors).
213	    OLMo panel visually the worst with near-uniform gen-1/gen-2+ confusion.
214	  analysis: 'Cross-generator generalization 是论文核心卖点，但 worst 档下 LOFO binary F1 = 0.665
215	    被审稿人视为 near-chance for practical use。Pythia family inflation 是 concrete evidence
216	    that LOGO overestimates generalization。审稿人会写："The authors report LOGO F1=0.680,
217	    but the more honest LOFO evaluation yields 0.665, and even this is inflated by
218	    including two Qwen variants. Single-family holdout F1 ranges from 0.621 (Pythia)
219	    to 0.726 (OLMo), suggesting the method''s cross-family generalization is highly
220	    variable and may not be robust enough for deployment."
221	
222	    '
223	- name: cross_family_reference_model
224	  plan_id: plan_003
225	  description: 'Test OLMo-2-1B and Qwen3-0.6B as alternative reference models (replacing
226	    Pythia-410M). Verify DDR drift persists with non-Pythia reference. Key falsification
227	    test for Claim 2.
228	
229	    '
230	  expected_results:
231	    logo_f1_pythia_ref: 0.68
232	    logo_f1_olmo_ref: 0.672
233	    logo_f1_qwen_ref: 0.689
234	    entropy_mean_drift_pythia: -1.19
235	    entropy_mean_drift_olmo: -0.61
236	    entropy_mean_drift_qwen: -0.95
237	    olmo_ref_hapax_rho: -0.58
238	    olmo_ref_entropy_mean_rho: -0.42
239	    olmo_ref_tail_decay_rho: 0.09
240	    drift_magnitude_ratio_olmo_vs_pythia: 0.51
241	    drift_direction_consistent: true
242	    shape_stationary_all_refs: true
243	  result_rationale: 'DDR 方向一致（所有 reference model 下 drifting features 都 negative drift），shape
244	    features 都 stationary —— 但 drift magnitude 高度依赖 reference model。OLMo reference
245	    的 entropy_mean drift 只有 Pythia 的 51%（-0.61 vs -1.19），Spearman ρ 从 -0.60 降到 -0.42。
246	    审稿人会 accept "direction is consistent" 但 argue "magnitude is reference-dependent,
247	    meaning DDR is partially a function of reference-generator mismatch rather than
248	    an intrinsic property of recursive generation." 这不会 kill Claim 2 但会 weaken 它 ——
249	    审稿人 scores -0.5 pp on Claim 2 credibility。LOGO F1 across references 的差异很小（0.672–0.689），
250	    说明分类性能 robust，但 DDR phenomenon characterization 的 precision 被削弱。
251	
252	    '
253	  tables:
254	  - caption: Cross-reference-model DDR comparison
255	    rows:
256	    - - Reference Model
257	      - LOGO F1
258	      - entropy_mean ρ
259	      - hapax ρ
260	      - tail_decay ρ
261	      - Drift magnitude (avg)
262	    - - Pythia-410M
263	      - '0.680'
264	      - −0.60
265	      - −0.63
266	      - '+0.04'
267	      - '1.19'
268	    - - OLMo-2-1B
269	      - '0.672'
270	      - −0.42
271	      - −0.58
272	      - '+0.09'
273	      - '0.61'
274	    - - Qwen3-0.6B
275	      - '0.689'
276	      - −0.55
277	      - −0.61
278	      - '+0.06'
279	      - '0.95'
280	  figures_description:
281	  - 3-panel overlay plot showing entropy_mean drift curves (depth 0–4) under each
282	    reference model. All three curves decline monotonically, but OLMo reference curve
283	    is visibly shallower. Reviewer will annotate the magnitude discrepancy as evidence
284	    of reference-model dependence.
285	  analysis: 'Falsification test 通过了（drift direction consistent），但 worst 档审稿人会 reframe
286	    结果： "While the direction of entropy drift is consistent across reference models,
287	    the magnitude varies by 2×, undermining the claim that DDR is an intrinsic property
288	    of recursive generation. A more parsimonious explanation is that DDR magnitude
289	    reflects the degree of mismatch between the reference model and the generator,
290	    not the depth of generation per se." 这是 worst 档 最 subtle 的攻击 —— 技术上实验通过了，但 interpretive
291	    framing 被挑战。
292	
293	    '
294	- name: downstream_utility
295	  plan_id: plan_004
296	  description: 'Fine-tune OLMo-1B on depth-stratified subsets. 3 random seeds with
297	    bootstrap CIs. Compare depth-aware filtering vs binary baselines. Sample-count-matched
298	    comparison.
299	
300	    '
301	  expected_results:
302	    all_data_ppl: 2.335
303	    all_data_ppl_ci:
304	    - 2.33
305	    - 2.34
306	    size_matched_ppl: 2.367
307	    size_matched_ppl_ci:
308	    - 2.362
309	    - 2.372
310	    depth01_ppl: 2.387
311	    depth01_ppl_ci:
312	    - 2.381
313	    - 2.393
314	    binary_filtered_ppl: 2.389
315	    binary_filtered_ppl_ci:
316	    - 2.384
317	    - 2.394
318	    depth0_only_ppl: 2.681
319	    depth0_only_ppl_ci:
320	    - 2.671
321	    - 2.691
322	    tost_p_2pct: 0.00011
323	    tost_p_1pct: 0.087
324	    cross_seed_ppl_std: 0.001
325	    ranking: all < size_matched < depth01 ≈ binary_filtered << depth0_only
326	    depth_filtering_vs_random_delta_ppl: 0.02
327	  result_rationale: 'Negative finding 非常 clean：depth-aware filtering 不优于 random subsampling，TOST
328	    在 ±2% margin 确认 equivalence。这在 worst 档下被 weaponize 为对整个工作 motivation 的质疑。 审稿人会写："The
329	    authors'' own Claim 3 demonstrates that generation depth has no downstream utility,
330	    raising the fundamental question: if knowing the depth of generation doesn''t
331	    help improve model training, what is the practical value of distinguishing gen-1
332	    from gen-2+?" Cross-seed variance 极小（std < 0.002）意味着结果 robust —— 但这 robustness
333	    是 negative finding 的 robustness，对论文不利。depth0_only 显著差（2.681）只是说明真实人类文本 vs 纯合成文本有区别
334	    —— 这是 binary detection 已经解决的问题。 TOST 在 ±1% margin 不显著（p=0.087）被审稿人注意到但不 weaponize（论文已选
335	    ±2%）。
336	
337	    '
338	  tables:
339	  - caption: Downstream CLM perplexity by training data depth composition (3 seeds)
340	    rows:
341	    - - Variant
342	      - Train Size
343	      - PPL (mean ± std)
344	      - Δ vs All
345	      - TOST ±2% p
346	    - - All depths
347	      - 12,299
348	      - 2.335 ± 0.001
349	      - —
350	      - —
351	    - - Size-matched random
352	      - 3,951
353	      - 2.367 ± 0.001
354	      - '+0.032'
355	      - ref
356	    - - Depth 0+1 only
357	      - 3,951
358	      - 2.387 ± 0.001
359	      - '+0.052'
360	      - 1.1×10⁻⁴
361	    - - Binary filtered
362	      - 3,951
363	      - 2.389 ± 0.001
364	      - '+0.054'
365	      - 8.7×10⁻⁵
366	    - - Depth 0 only
367	      - '797'
368	      - 2.681 ± 0.001
369	      - '+0.346'
370	      - —
371	  figures_description:
372	  - 'Bar chart with error bars showing perplexity across 5 variants. The three middle
373	    bars (size-matched, depth01, binary) are visually indistinguishable within error
374	    bars. depth0_only stands out as an outlier. Reviewer annotation: ''The only meaningful
375	    distinction is between human text and machine text — precisely the binary detection
376	    problem.'''
377	  analysis: 'Negative finding 本身是诚实的科学贡献，但在 worst 档下被 R2/R3 weaponize 成 "if depth
378	    doesn''t matter for the most obvious downstream task, the burden of proof is on
379	    the authors to show ANY downstream task where depth matters." 论文的 framing 是 "diagnostic
380	    tool" 但 审稿人认为 diagnostic without therapeutic value = limited impact。
381	
382	    '
383	- name: prompt_type_comparison
384	  plan_id: plan_005
385	  description: 'Compare continuation vs elaboration vs inspired_rewriting chains.
386	    1000 seeds × Pythia-2.8B × 3 prompt types.
387	
388	    '
389	  expected_results:
390	    cv_f1_continuation: 0.781
391	    cv_f1_elaboration: 0.73
392	    cv_f1_rewriting: 0.737
393	    lopto_avg_f1: 0.752
394	    lopto_held_out_continuation_f1: 0.762
395	    lopto_held_out_elaboration_f1: 0.733
396	    lopto_held_out_rewriting_f1: 0.762
397	    depth_retention_d4d0_cont: 0.831
398	    depth_retention_d4d0_elab: 0.986
399	    depth_retention_d4d0_rewrite: 0.939
400	    drift_entropy_mean_cont: -0.557
401	    drift_entropy_mean_elab: -0.471
402	    drift_entropy_mean_rewrite: -0.477
403	    cross_prompt_type_range_pp: 5.1
404	  result_rationale: 'Continuation chains 明显优于 elaboration（5.1 pp gap），but elaboration/rewriting
405	    的 depth retention 更高（0.986/0.939 vs 0.831）。审稿人 worst 档解读：depth signal 只在 continuation（最简单、最
406	    artificial 的 chain type）中强，而更 realistic 的 elaboration/ rewriting 中信号明显弱。"The method
407	    works best on the least realistic generation scenario (verbatim continuation)
408	    and degrades on more naturalistic prompt types, suggesting the depth signal is
409	    an artifact of the continuation paradigm rather than a general property of recursive
410	    generation." Elaboration 的 entropy_mean drift 比 continuation 弱 15% （-0.471 vs
411	    -0.557），但 hapax drift 反而更强 —— 这种 inconsistency 进一步削弱 DDR 作为 unified phenomenon
412	    的叙事。
413	
414	    '
415	  tables:
416	  - caption: Per-prompt-type classification performance and drift statistics
417	    rows:
418	    - - Prompt Type
419	      - CV F1
420	      - LOPTO F1
421	      - Depth Retention
422	      - entropy_mean ρ
423	      - hapax ρ
424	    - - Continuation
425	      - '0.781'
426	      - '0.762'
427	      - '0.831'
428	      - −0.557
429	      - −0.651
430	    - - Elaboration
431	      - '0.730'
432	      - '0.733'
433	      - '0.986'
434	      - −0.471
435	      - −0.674
436	    - - Inspired Rewriting
437	      - '0.737'
438	      - '0.762'
439	      - '0.939'
440	      - −0.477
441	      - −0.670
442	  figures_description:
443	  - 3×7 heatmap showing per-feature Spearman ρ across prompt types. Reveals that feature
444	    ranking is not stable across prompt types — entropy_mean is strongest for continuation
445	    but hapax_ratio is strongest for elaboration/rewriting. This inconsistency undermines
446	    the 'universal DDR' narrative.
447	  analysis: 'Prompt-type dependence 在 worst 档下被视为 generalizability concern 而非 nuanced
448	    finding。 审稿人会 argue："The 5 pp gap between continuation and elaboration means the
449	    method''s performance is highly sensitive to the (unknowable in practice) generation
450	    prompt."
451	
452	    '
453	- name: paraphrastic_comparison
454	  plan_id: plan_006
455	  description: 'Construct parallel paraphrasing chains for comparison with continuation
456	    chains. Tests attractor convergence theory.
457	
458	    '
459	  expected_results:
460	    paraphrastic_cv_f1: 0.723
461	    continuation_cv_f1: 0.781
462	    paraphrastic_binary_f1: 0.665
463	    continuation_binary_f1: 0.694
464	    paraphrastic_drift_entropy_mean: -0.38
465	    paraphrastic_depth_retention_d4d0: 0.995
466	    attractor_convergence_observed: true
467	    effective_classes_paraphrastic: 2
468	    delta_para_vs_cont_pp: 2.9
469	  result_rationale: 'Paraphrastic chains 显示 attractor convergence（depth retention
470	    0.995 ≈ 1.0，即几乎 不丢 chain），但 depth signal 弱于 non-paraphrastic（binary F1 0.665 vs
471	    0.694）。 差距只有 2.9 pp —— 审稿人 argue 这太小了，不足以证明 non-paraphrastic chains 有 qualitatively
472	    different behavior。"Both paraphrastic and non-paraphrastic chains show similar
473	    (weak) depth signal, contradicting the authors'' claim that non-paraphrastic chains
474	    exhibit a fundamentally different depth dynamics." Attractor convergence 被确认 但反而成为
475	    negative evidence："if paraphrastic chains converge to attractors within ~3 iterations,
476	    and non-paraphrastic chains show comparable depth signal, the phenomenon is better
477	    explained by generic generation drift than by the proposed DDR framework."
478	
479	    '
480	  tables:
481	  - caption: Paraphrastic vs non-paraphrastic chain comparison
482	    rows:
483	    - - Chain Type
484	      - CV F1
485	      - Binary F1
486	      - Depth Retention
487	      - entropy_mean ρ
488	      - Effective Classes
489	    - - Non-paraphrastic (continuation)
490	      - '0.781'
491	      - '0.694'
492	      - '0.831'
493	      - −0.557
494	      - '3'
495	    - - Paraphrastic
496	      - '0.723'
497	      - '0.665'
498	      - '0.995'
499	      - −0.380
500	      - ~2
501	    - - Δ
502	      - +5.8 pp
503	      - +2.9 pp
504	      - −0.164
505	      - −0.177
506	      - '+1'
507	  figures_description:
508	  - 'Dual-panel: left shows feature drift curves for paraphrastic vs continuation
509	    chains (both decline, paraphrastic shallower but similar shape). Right shows confusion
510	    matrices side-by-side. The visual similarity between the two panels undermines
511	    the ''qualitatively different'' claim.'
512	  analysis: '在 worst 档下，this experiment backfires。审稿人预期 non-paraphrastic chains would
513	    show dramatically different behavior，但 2.9 pp delta 不够 dramatic。反而证明 depth signal
514	    is a general (and weak) generation phenomenon，不是 non-paraphrastic chains 的 unique
515	    property。论文需要 reframe 为 "depth signal exists across chain types" 而非 "non-paraphrastic
516	    chains are special."
517	
518	    '
519	- name: cross_model_chains
520	  plan_id: plan_007
521	  description: 'Cross-model chains (different generator per depth step) vs single-model
522	    chains. More realistic web contamination scenario.
523	
524	    '
525	  expected_results:
526	    cross_model_binary_f1: 0.764
527	    cross_model_3class_f1: 0.789
528	    single_model_binary_f1: 0.694
529	    single_model_3class_f1: 0.762
530	    delta_binary_pp: 7.0
531	    delta_3class_pp: 2.7
532	    cross_model_logo_binary_f1: 0.83
533	    cross_model_easier_reason: generator heterogeneity amplifies distributional shift
534	  result_rationale: 'Cross-model chains 的 binary F1 大幅高于 single-model（0.764 vs 0.694,
535	    +7 pp）， LOGO 甚至达到 0.830。审稿人在 worst 档下会 reframe 这个结果为 negative evidence： "The substantially
536	    higher F1 on cross-model chains (0.830) suggests the method is primarily detecting
537	    generator switching rather than generation depth. In single-model chains (the
538	    harder and more interesting case), F1 drops to 0.694." 这个 gap 被视为证明 depth signal
539	    在 single-model case 中 weak —— 真正的 depth classification 应该在 same-generator chains
540	    上 work，而 cross-model improvement 是 "trivially explained by OOD detection of different
541	    model fingerprints at each depth."
542	
543	    '
544	  tables:
545	  - caption: Cross-model vs single-model chain classification
546	    rows:
547	    - - Setting
548	      - Binary F1
549	      - 3-class F1
550	      - LOGO Binary F1
551	    - - Single-model chains
552	      - '0.694'
553	      - '0.762'
554	      - '0.694'
555	    - - Cross-model chains
556	      - '0.764'
557	      - '0.789'
558	      - '0.830'
559	    - - Δ
560	      - +7.0 pp
561	      - +2.7 pp
562	      - +13.6 pp
563	  figures_description:
564	  - 'Scatter plot of per-sample prediction confidence (single-model x-axis vs cross-model
565	    y-axis). Points cluster above the diagonal, showing cross-model chains are systematically
566	    easier. Reviewer annotation: ''This gap suggests the method detects model switching,
567	    not depth.'''
568	  analysis: 'Cross-model improvement 是 double-edged sword。在 worst 档下它证明了 "easy case
569	    更好" 但被 reinterpreted 为 the method doesn''t truly measure depth —— 而是 measures
570	    generator heterogeneity。审稿人会 demand "same-generator transfer" 作为 real benchmark，where
571	    0.694 is the relevant number。
572	
573	    '
574	- name: multi_domain_seeds
575	  plan_id: plan_008
576	  description: 'Expand to 4 domains: Wikipedia, news, scientific, creative writing.
577	    500 seeds per domain × 5 depths.
578	
579	    '
580	  expected_results:
581	    wikipedia_binary_f1: 0.724
582	    news_binary_f1: 0.667
583	    scientific_binary_f1: 0.631
584	    creative_binary_f1: 0.658
585	    cross_domain_logo_binary_f1: 0.652
586	    max_gap_vs_wiki_pp: 9.3
587	    worst_domain: scientific
588	    best_domain: wikipedia
589	    domain_variance_std: 0.034
590	  result_rationale: 'Wikipedia（训练数据的主 domain）表现最好（0.724），scientific 最差（0.631）—— 9.3
591	    pp gap。 审稿人在 worst 档下 argue："The method''s performance is domain-dependent, with
592	    scientific text yielding near-chance binary F1 (0.631). Since depth classification
593	    is most needed for scientific text (where AI contamination is a growing concern
594	    per the authors'' own motivation), this domain sensitivity is a critical practical
595	    limitation." Cross-domain LOGO（training on 3 domains, test on 1）进一步降到 0.652。Domain
596	    dependence + generator dependence + temperature dependence + instruct dependence
597	    = cumulative scope narrowing that makes the method seem increasingly specialized.
598	
599	    '
600	  tables:
601	  - caption: Per-domain binary F1 (LOGO across generators, within-domain)
602	    rows:
603	    - - Domain
604	      - Seeds
605	      - Binary F1
606	      - 95% CI
607	      - Δ vs Wiki
608	    - - Wikipedia
609	      - '500'
610	      - '0.724'
611	      - '[0.704, 0.744]'
612	      - —
613	    - - News
614	      - '500'
615	      - '0.667'
616	      - '[0.645, 0.689]'
617	      - −5.7 pp
618	    - - Creative
619	      - '500'
620	      - '0.658'
621	      - '[0.635, 0.681]'
622	      - −6.6 pp
623	    - - Scientific
624	      - '500'
625	      - '0.631'
626	      - '[0.607, 0.655]'
627	      - −9.3 pp
628	    - - '**Cross-domain LOGO**'
629	      - '2000'
630	      - '**0.652**'
631	      - '[0.638, 0.666]'
632	      - —
633	  figures_description:
634	  - Radar chart showing binary F1 across 4 domains × 3 prompt types. The shape is
635	    asymmetric (Wikipedia+continuation = best corner, scientific+elaboration = worst
636	    corner), making the fragility visually apparent.
637	  analysis: 'Domain dependence 在 worst 档下被叠加到 existing scope limitations 上。审稿人列出 cumulative
638	    conditions："base models only, temperature ∈ [0.5, 0.9], continuation chains, Wikipedia-domain
639	    seeds" —— 这是 increasingly narrow niche that undermines any practical framing of
640	    the work.
641	
642	    '
643	- name: finer_grained_ordinal
644	  plan_id: plan_009
645	  description: '5-class ordinal classification (gen-0 through gen-4). Test if depth
646	    signal extends beyond 3-class resolution.
647	
648	    '
649	  expected_results:
650	    five_class_macro_f1: 0.468
651	    five_class_ci:
652	    - 0.451
653	    - 0.485
654	    three_class_macro_f1: 0.762
655	    ordinal_coral_f1: 0.472
656	    ordinal_frank_hall_f1: 0.465
657	    gen1_vs_gen2_confusion_rate: 0.43
658	    gen2_vs_gen3_confusion_rate: 0.51
659	    gen3_vs_gen4_confusion_rate: 0.48
660	    mean_absolute_depth_error: 0.89
661	  result_rationale: '5-class F1 降到 0.468，接近 5-class random baseline（0.20）但仍显著高于 chance。
662	    Ordinal methods（CORAL, Frank-Hall）无改善（0.472, 0.465）。Gen-2/gen-3/gen-4 之间 几乎无法区分（confusion
663	    rate 43–51%）。审稿人在 worst 档下 argue："The 5-class F1 of 0.468 confirms that depth
664	    signal is extremely shallow — the method can roughly distinguish ''early'' (gen-0/1)
665	    from ''late'' (gen-2+) but cannot meaningfully estimate depth. The 3-class formulation
666	    is not a principled choice but a ceiling imposed by signal weakness." 这直接 打击了
667	    "depth classification" 作为 task formulation 的 novelty —— 如果实际上只有 binary-ish signal，那
668	    task formulation 的贡献 = trivially extending binary detection by one class。
669	
670	    '
671	  tables:
672	  - caption: Ordinal classification resolution comparison
673	    rows:
674	    - - Granularity
675	      - Method
676	      - Macro F1
677	      - Ordinal Improvement
678	    - - 3-class
679	      - XGBoost
680	      - '0.762'
681	      - —
682	    - - 5-class
683	      - XGBoost
684	      - '0.468'
685	      - —
686	    - - 5-class
687	      - CORAL
688	      - '0.472'
689	      - +0.4 pp
690	    - - 5-class
691	      - Frank-Hall
692	      - '0.465'
693	      - −0.3 pp
694	  figures_description:
695	  - 5×5 confusion matrix heatmap. Gen-0 is cleanly classified (>0.90 recall), gen-1
696	    shows moderate confusion with gen-2, and gen-2/3/4 form a near-uniform block —
697	    visually a 'binary-plus-noise' pattern rather than ordinal resolution.
698	  analysis: '5-class collapse 是 worst 档最有力的 evidence against task formulation novelty。
699	    审稿人会 argue 这证明 depth signal 本质上是 binary（human vs machine）加上一点 gen-1 distinctiveness，而非
700	    true ordinal depth estimation。"The authors frame a 3-class problem, but the data
701	    supports at most 2.5 classes."
702	
703	    '
704	- name: human_edit_robustness
705	  plan_id: plan_010
706	  description: 'Robustness to simulated human edits: (A) random word replacement 5/10/20%,
707	    (B) LLM-simulated light rephrasing.
708	
709	    '
710	  expected_results:
711	    baseline_binary_f1: 0.694
712	    random_5pct_f1: 0.648
713	    random_10pct_f1: 0.611
714	    random_20pct_f1: 0.583
715	    llm_rephrase_f1: 0.641
716	    llm_rephrase_edit_distance: 0.51
717	    degradation_5pct_pp: -4.6
718	    degradation_10pct_pp: -8.3
719	    degradation_20pct_pp: -11.1
720	    degradation_llm_pp: -5.3
721	  result_rationale: 'Even 5% random replacement 造成 4.6 pp drop（0.694 → 0.648），LLM
722	    rephrasing 造成 5.3 pp drop（→ 0.641）。审稿人在 worst 档下 argue："In practice, AI-generated
723	    text is almost always edited before publication. The method loses 5+ pp F1 from
724	    light editing (51% edit distance), and this is on top of the already-modest 0.694
725	    baseline. After realistic editing, depth classification falls to ~0.64, making
726	    it effectively useless." 20% replacement 降到 0.583 —— 接近 chance for binary task。这与
727	    instruct degradation、 temperature sensitivity、domain dependence 一起构成 cumulative
728	    fragility picture。
729	
730	    '
731	  tables:
732	  - caption: Robustness to simulated human edits
733	    rows:
734	    - - Perturbation
735	      - Binary F1
736	      - Δ vs Baseline
737	      - Edit Distance
738	    - - None (baseline)
739	      - '0.694'
740	      - —
741	      - '0.0'
742	    - - Random 5%
743	      - '0.648'
744	      - −4.6 pp
745	      - ~0.05
746	    - - Random 10%
747	      - '0.611'
748	      - −8.3 pp
749	      - ~0.10
750	    - - Random 20%
751	      - '0.583'
752	      - −11.1 pp
753	      - ~0.20
754	    - - LLM rephrase
755	      - '0.641'
756	      - −5.3 pp
757	      - '0.51'
758	  figures_description:
759	  - 'Line chart: binary F1 vs edit intensity (0%, 5%, 10%, 20%, LLM). Near-linear
760	    degradation. LLM rephrase point sits between 5% and 10% random. Shaded area shows
761	    95% CI widening at higher edit levels.'
762	  analysis: 'Robustness 实验在 worst 档下是 lose-lose：如果 robust，审稿人 say "shallow features
763	    aren''t capturing anything generation-specific"; 如果 fragile（as here），审稿人 say "not
764	    practical." 这里是 fragile，confirm 审稿人 prior that depth signal is surface-level and
765	    easily disrupted.
766	
767	    '
768	- name: ld_score_feature
769	  plan_id: plan_011
770	  description: 'Add LD-Score (character-distribution signature) as 8th feature. Test
771	    character-level complementarity to word/entropy features.
772	
773	    '
774	  expected_results:
775	    seven_feature_f1: 0.773
776	    eight_feature_with_ld_f1: 0.779
777	    ld_score_alone_f1: 0.623
778	    ld_score_spearman_depth: -0.31
779	    marginal_improvement_pp: 0.6
780	    feature_importance_ld: 0.028
781	  result_rationale: 'LD-Score 作为单独 feature 只有 0.623 F1，加入后 marginal improvement 仅
782	    0.6 pp （0.773 → 0.779），feature importance 排最后（0.028）。审稿人在 worst 档不会 attack 这个实验本身（它是
783	    minor addition），但会 note："Adding LD-Score provides negligible improvement, suggesting
784	    the character-level depth signal is largely subsumed by the existing word-level
785	    features — further evidence that all these features measure the same underlying
786	    vocabulary impoverishment." 这 reinforces RC1（repackaging）。
787	
788	    '
789	  tables:
790	  - caption: LD-Score feature addition
791	    rows:
792	    - - Feature Set
793	      - Macro F1
794	      - Δ
795	    - - 7 features (baseline)
796	      - '0.773'
797	      - —
798	    - - 7 + LD-Score
799	      - '0.779'
800	      - +0.6 pp
801	    - - LD-Score only
802	      - '0.623'
803	      - —
804	  figures_description:
805	  - Feature importance bar chart (8 features). LD-Score is the shortest bar, visually
806	    insignificant compared to hapax_ratio, TTR, entropy_mean.
807	  analysis: 'Minor experiment, minor result. 在 worst 档下被用作 supporting evidence for
808	    "all signals are the same signal" narrative，但不是 primary attack vector。
809	
810	    '
811	- name: end_to_end_classifier
812	  plan_id: plan_012
813	  description: 'QLoRA fine-tuned end-to-end depth classifier. Compares learned representations
814	    vs handcrafted 7-feature ensemble.
815	
816	    '
817	  expected_results:
818	    qlora_3class_f1: 0.891
819	    qlora_3class_ci:
820	    - 0.878
821	    - 0.904
822	    qlora_binary_f1: 0.842
823	    qlora_binary_ci:
824	    - 0.826
825	    - 0.858
826	    qlora_5class_f1: 0.571
827	    seven_feature_3class_f1: 0.762
828	    seven_feature_binary_f1: 0.694
829	    delta_3class_pp: 12.9
830	    delta_binary_pp: 14.8
831	    qlora_logo_3class_f1: 0.743
832	    qlora_logo_binary_f1: 0.712
833	    qlora_inference_cost_ratio: 47.0
834	  result_rationale: 'QLoRA within-distribution 大幅碾压 7-feature（3-class 0.891 vs 0.762,
835	    +12.9 pp）， 但 LOGO 下差距缩小（0.743 vs 0.762，7-feature 反而更好 for 3-class）。Binary LOGO
836	    QLoRA 仍然更好（0.712 vs 0.694）。审稿人在 worst 档下会 cherry-pick within-distribution numbers："A
837	    simple QLoRA classifier achieves 0.842 binary F1, dwarfing the proposed method''s
838	    0.694. While the authors may argue their method is more lightweight, the 14.8
839	    pp gap suggests the handcrafted features miss substantial depth signal that end-to-end
840	    learning captures." 论文的 efficiency argument（7-feature 用 410M reference 而 QLoRA
841	    用 full model）在 worst 档下被 dismiss："inference cost is not a compelling argument
842	    when the method is 15 pp worse." LOGO 下 QLoRA 的 cross-generator generalization
843	    差（3-class 0.743 < 0.762）可以作为 rebuttal point，但审稿人 already scored low before seeing
844	    this nuance。
845	
846	    '
847	  tables:
848	  - caption: End-to-end (QLoRA) vs handcrafted 7-feature ensemble
849	    rows:
850	    - - Method
851	      - 3-class F1
852	      - Binary F1
853	      - LOGO 3-class
854	      - LOGO Binary
855	      - Cost Ratio
856	    - - 7-feature XGBoost
857	      - '0.762'
858	      - '0.694'
859	      - '0.762'
860	      - '0.694'
861	      - 1×
862	    - - QLoRA (OLMo-1B)
863	      - '0.891'
864	      - '0.842'
865	      - '0.743'
866	      - '0.712'
867	      - 47×
868	    - - Δ
869	      - +12.9 pp
870	      - +14.8 pp
871	      - −1.9 pp
872	      - +1.8 pp
873	      - —
874	  figures_description:
875	  - 'Grouped bar chart: within-distribution vs LOGO for both methods. Within-distribution
876	    shows QLoRA dominating; LOGO shows convergence. The within-distribution gap is
877	    visually dramatic and is what the reviewer will focus on.'
878	  analysis: 'End-to-end comparison 在 worst 档下是 devastating。审稿人会 focus on within-distribution
879	    gap (14.8 pp) and dismiss the LOGO nuance as "an artifact of limited training
880	    generators." 论文需要 pre-empt 这个 attack by leading with LOGO numbers and framing
881	    within-distribution as oracle-access upper bound。
882	
883	    '
884	- name: text_length_control
885	  plan_id: plan_013
886	  description: 'Address text length confound: length distribution analysis, length-normalized
887	    features, length-matched subsampling.
888	
889	    '
890	  expected_results:
891	    length_depth_spearman: 0.12
892	    length_depth_p: 0.001
893	    length_matched_binary_f1: 0.724
894	    unmatched_binary_f1: 0.77
895	    delta_pp: -4.6
896	    normalized_ttr_trend_preserved: true
897	    normalized_hapax_trend_preserved: true
898	    length_is_primary_confound: false
899	    length_contributes_to_signal: true
900	    short_text_dropout_bias: true
901	  result_rationale: 'Length-matched F1 降 4.6 pp（0.770 → 0.724）—— 意味着 text length 贡献了约
902	    6% 的 总 signal。审稿人在 worst 档下会 magnify 这个 finding："After controlling for text length,
903	    the already-modest F1 drops further to 0.724 (unmatched) → this suggests that
904	    part of the ''depth signal'' is simply a length artifact." 但 normalized features
905	    的 trend 保持说明 depth signal 不完全来自 length。这是 worst 档中一个 mixed result —— 不会 kill the
906	    paper 但会 reduce credibility of the headline number by ≤5 pp。Short text dropout
907	    bias 的 发现（deeper depths 有更多短文本被过滤掉）adds confound complexity that makes the narrative
908	    harder to follow。
909	
910	    '
911	  tables:
912	  - caption: Length control analysis
913	    rows:
914	    - - Condition
915	      - Binary F1
916	      - Δ
917	    - - Unmatched (original)
918	      - '0.770'
919	      - —
920	    - - Length-matched subsample
921	      - '0.724'
922	      - −4.6 pp
923	    - - Length-normalized features
924	      - '0.748'
925	      - −2.2 pp
926	  figures_description:
927	  - 'Left: text length distribution violin plots by depth (showing subtle rightward
928	    shift at depth 0, leftward at depth 4). Right: before/after length matching classification
929	    boundary plots.'
930	  analysis: 'Length confound 是 necessary experiment 但在 worst 档下 result = "yes, some
931	    of the signal was length." 4.6 pp drop 不是 catastrophic 但会 erode reviewer trust
932	    in all other reported numbers ("were these also length-confounded?").
933	
934	    '
935	- name: large_scale_generator
936	  plan_id: plan_014
937	  description: 'Add Qwen3-8B-Base to test depth signal at 7B+ scale. 1000 seeds ×
938	    5 depths.
939	
940	    '
941	  expected_results:
942	    qwen3_8b_logo_binary_f1: 0.637
943	    qwen3_8b_logo_3class_f1: 0.683
944	    qwen3_8b_within_cv_f1: 0.711
945	    six_gen_logo_avg_f1: 0.789
946	    delta_vs_avg_pp: -10.6
947	    hapax_rho_8b: -0.41
948	    ttr_rho_8b: -0.39
949	    entropy_mean_rho_8b: -0.33
950	    feature_margin_compression: 0.58
951	  result_rationale: 'Qwen3-8B 的 LOGO binary F1 = 0.637，比 6-gen average 低 10.6 pp。Feature
952	    drift magnitudes 全面压缩（hapax ρ 从 avg −0.63 降到 −0.41，compression ratio 0.58）。 这与
953	    paper_framing 中的 scale effect 一致，但 worst 档审稿人会 extrapolate："At 8B the signal is
954	    already substantially degraded (−10.6 pp). Frontier models (70B+) and API models
955	    (GPT-4, Claude) — which generate the vast majority of real-world AI text — would
956	    presumably show even weaker signal, making the method irrelevant for the contamination
957	    problem the paper claims to address." 这是 worst 档中 most damaging extrapolation
958	    ——  审稿人不需要实验数据就可以 argue 方法在 practical scale 上 doesn''t work。Within-CV F1 = 0.711
959	    还可以（说明 8B 自身的 depth signal 存在），但 cross-generator transfer 到 8B 很弱（0.637），meaning
960	    smaller models 的 training data 不 transfer 到大模型。
961	
962	    '
963	  tables:
964	  - caption: 'Scale effect: Qwen3-8B vs smaller generators'
965	    rows:
966	    - - Generator
967	      - Size
968	      - LOGO Binary F1
969	      - hapax ρ
970	      - entropy_mean ρ
971	    - - Pythia-1B
972	      - 1.0B
973	      - '0.724'
974	      - −0.65
975	      - −0.60
976	    - - OLMo-2-1B
977	      - 1.5B
978	      - '0.643'
979	      - −0.58
980	      - −0.55
981	    - - Pythia-2.8B
982	      - 2.8B
983	      - '0.711'
984	      - −0.63
985	      - −0.60
986	    - - Qwen3-8B
987	      - 8.0B
988	      - '0.637'
989	      - −0.41
990	      - −0.33
991	    - - '**Trend**'
992	      - —
993	      - '**Declining**'
994	      - '**Compressing**'
995	      - '**Compressing**'
996	  figures_description:
997	  - Log-scale x-axis (model size) vs binary F1 y-axis, with feature drift magnitude
998	    as bubble size. Clear downward trend from 1B to 8B. Extrapolation dotted line
999	    to 70B crosses 0.50 (chance) at ~30B, visually devastating for scale argument.
1000	  analysis: 'Scale degradation 是 worst 档的 structural problem —— 审稿人不需要 70B 实验就可以 argue
1001	    via extrapolation。Paper 的 honest reporting of this limitation ("defines scope
1002	    boundary") 在 worst 档下被 reframed 为 "the scope boundary excludes all models people
1003	    actually care about."
1004	
1005	    '
1006	- name: ordinal_baseline_comparison
1007	  plan_id: plan_015
1008	  description: 'Compare existing detector continuous scores (FastDetectGPT, Binoculars,
1009	    LD-Score) as ordinal depth predictors vs our 7-feature ensemble.
1010	
1011	    '
1012	  expected_results:
1013	    seven_feature_logo_f1: 0.68
1014	    avg_logprob_logo_f1: 0.653
1015	    ld_score_logo_f1: 0.641
1016	    fastdetectgpt_logo_f1: 0.612
1017	    binoculars_logo_f1: 0.571
1018	    seven_feature_vs_avglogprob_delta_pp: 2.7
1019	    seven_feature_vs_ld_delta_pp: 3.9
1020	    bootstrap_p_7feat_vs_avglogprob: 0.038
1021	    multi_detector_ensemble_f1: 0.708
1022	    multi_det_vs_7feat_delta_pp: 2.8
1023	  result_rationale: '7-feature ensemble (0.680) 优于所有 single detectors，但 margin 很小
1024	    —— vs Avg-LogProb 只有 2.7 pp (p=0.038, barely significant)。更关键的是 multi-detector
1025	    ensemble（4 detectors + surface）达到 0.708，反过来超过 7-feature 2.8 pp。审稿人在 worst 档下会
1026	    argue："A simple average of existing detector scores (Avg-LogProb: 0.653) achieves
1027	    96% of the proposed method''s F1, raising the question of whether depth-specific
1028	    features are necessary. Moreover, a multi-detector ensemble outperforms the proposed
1029	    features by 2.8 pp, suggesting that the optimal approach is to repurpose existing
1030	    detectors rather than design depth-specific features." 这直接 undermines Claim 1
1031	    的 contribution：if existing tools + trivial ensembling works comparably or better，新
1032	    feature set 的 value proposition collapses。
1033	
1034	    Bootstrap test 的 p=0.038 是 borderline significant —— worst 档审稿人会 note "barely
1035	    significant and not corrected for multiple comparisons." 如果 Bonferroni correct
1036	    for 4 comparisons，p=0.152 → not significant。
1037	
1038	    '
1039	  tables:
1040	  - caption: 'Ordinal depth classification: 7-feature vs existing detector baselines'
1041	    rows:
1042	    - - Method
1043	      - LOGO Binary F1
1044	      - 95% CI
1045	      - Δ vs 7-feat
1046	      - Bootstrap p
1047	    - - '**7-feature ensemble**'
1048	      - '**0.680**'
1049	      - '[0.672, 0.688]'
1050	      - —
1051	      - —
1052	    - - Avg-LogProb (single)
1053	      - '0.653'
1054	      - '[0.612, 0.694]'
1055	      - −2.7 pp
1056	      - '0.038'
1057	    - - LD-Score (single)
1058	      - '0.641'
1059	      - '[0.598, 0.684]'
1060	      - −3.9 pp
1061	      - '0.011'
1062	    - - FastDetectGPT (single)
1063	      - '0.612'
1064	      - '[0.571, 0.653]'
1065	      - −6.8 pp
1066	      - '0.002'
1067	    - - Binoculars (single)
1068	      - '0.571'
1069	      - '[0.528, 0.614]'
1070	      - −10.9 pp
1071	      - <0.001
1072	    - - 4-det + surface ensemble
1073	      - '0.708'
1074	      - '[0.694, 0.722]'
1075	      - +2.8 pp
1076	      - '0.024'
1077	  figures_description:
1078	  - Forest plot showing each method's LOGO F1 with 95% CI. CIs overlap heavily between
1079	    7-feature and Avg-LogProb/LD-Score. Multi-detector ensemble CI sits above 7-feature
1080	    point estimate. Visually, the 7-feature method is 'in the pack' rather than clearly
1081	    superior.
1082	  analysis: Baseline comparison 在 worst 档下是 most dangerous experiment。7-feature 的
1083	    advantage over best single detector (2.7 pp) 太小，且被 multi-detector ensemble surpassed。
1084	    审稿人会 conclude："The proposed features provide marginal, statistically borderline
1085	    improvement over simply using existing detector scores for depth estimation. Given
1086	    the complexity of the feature engineering and the need for a reference model,
1087	    this represents insufficient contribution for even Findings-level publication."
1088	    这直接 targets the paper's reason to exist。
1089	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92e64cfd-212d-4aef-9db8-90e1f7213744",
  "isSidechain": false,
  "promptId": "00fafa99-9202-4e1a-8fd4-c2e127d8de99",
  "type": "user",
  "uuid": "a8f2349c-3a55-4c78-920a-c96a9918c9ed",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/worst/imagined_experiments.yaml",
      "content": "tier: worst\nnarrative_guidance: 'Paper receives avg 2.5–3.0. Core attacks: (1) DDR ≈ vocabulary\n  impoverishment repackaging, surface-only gap too small to justify a new framework;\n  (2) base-model-only + temperature-sensitive + instruct collapse = fatal scope limitation\n  for any practical framing; (3) 0.694 binary F1 compared unfairly against binary\n  detection baselines (>0.95), labeled ''not actionable''; (4) Claim 3 negative finding\n  weaponized as ''why does this matter''; (5) 33-page paper criticized as unfocused\n  experiment dump. Reframe direction: pivot from ''depth classification as a tool''\n  to ''empirical study of recursive generation dynamics'' or ''complementary signal\n  for existing detectors''. Neither requires new experiments.\n\n  '\nimagined_experiments:\n- name: feature_ablation_and_trend\n  plan_id: plan_001\n  description: 'Surface-only vs reference-only vs full 7-feature ablation on MVP data\n    (Pythia-2.8B, ~4600 records). XGBoost 5-fold CV. Trend analysis per feature across\n    depth 0–4. Perplexity pre-validation for Claim 3.\n\n    '\n  expected_results:\n    full_macro_f1: 0.773\n    surface_only_f1: 0.741\n    reference_only_f1: 0.698\n    surface_vs_full_gap_pp: 3.2\n    mcnemar_p_surface_vs_full: 0.027\n    hapax_ratio_slope: -0.063\n    hapax_ratio_r2: 0.88\n    ttr_slope: -0.041\n    ttr_r2: 0.82\n    entropy_mean_slope: -0.089\n    entropy_mean_r2: 0.79\n    tail_decay_slope: 0.003\n    tail_decay_r2: 0.04\n    entropy_std_slope: -0.031\n    entropy_std_r2: 0.41\n    entropy_max_slope: 0.008\n    entropy_max_r2: 0.07\n    ppl_depth0: 14.2\n    ppl_depth2: 3.8\n    ppl_depth4: 1.9\n  result_rationale: 'Surface-only 达到 0.741（vs full 0.773），差距仅 3.2 pp。McNemar p=0.027\n    虽然显著但 marginal。在 worst 档中，审稿人会 argue \"surface features capture 96% of the signal\"\n    (0.741/0.773=0.959)，reference features 只是 marginal add-on，不构成独立 contribution。\n    entropy_std 的 R²=0.41 模糊了 drifting/stationary 的 clean split —— 审稿人可以 argue 这不是\n    bimodal response 而是 continuous degradation gradient，DDR 概念 overclaims。 Trend analysis\n    显示所有 drifting features 都沿同一方向（单调递减），审稿人会 argue 这就是 well-known vocabulary impoverishment\n    的多种测量方式，不是新现象。\n\n    '\n  tables:\n  - caption: 'Feature ablation: 5-fold CV macro F1 on Pythia-2.8B MVP data'\n    rows:\n    - - Feature Set\n      - Macro F1\n      - 95% CI\n      - Δ vs Full\n    - - Full (7 features)\n      - '0.773'\n      - '[0.758, 0.788]'\n      - —\n    - - Surface-only (TTR + hapax)\n      - '0.741'\n      - '[0.724, 0.758]'\n      - −3.2 pp\n    - - Reference-only (5 entropy)\n      - '0.698'\n      - '[0.679, 0.717]'\n      - −7.5 pp\n  - caption: Per-feature depth trend (linear regression on depth 0–4)\n    rows:\n    - - Feature\n      - Category\n      - Slope\n      - R²\n      - Spearman ρ\n    - - hapax_ratio\n      - Drifting\n      - −0.063\n      - '0.88'\n      - −0.63\n    - - TTR\n      - Drifting\n      - −0.041\n      - '0.82'\n      - −0.61\n    - - entropy_mean\n      - Drifting\n      - −0.089\n      - '0.79'\n      - −0.60\n    - - entropy_std\n      - Ambiguous\n      - −0.031\n      - '0.41'\n      - −0.20\n    - - entropy_min\n      - Stationary\n      - −0.018\n      - '0.22'\n      - −0.15\n    - - tail_decay\n      - Stationary\n      - '+0.003'\n      - '0.04'\n      - '+0.04'\n    - - entropy_max\n      - Stationary\n      - '+0.008'\n      - '0.07'\n      - '+0.05'\n  figures_description:\n  - 7-panel feature trend plot showing mean ± std across depth 0–4. Drifting features\n    (hapax, TTR, entropy_mean) show clear monotonic decline but with overlapping error\n    bars at adjacent depths. entropy_std occupies an ambiguous middle zone (visible\n    drift but high variance). Stationary features (tail_decay, entropy_max) are flat.\n    Reviewer will highlight entropy_std ambiguity and overlapping error bars as evidence\n    that the 'clean bimodal split' is overstated.\n  analysis: '在 worst 档下，这个实验的核心问题是 surface-vs-full gap 太小。3.2 pp 差距在审稿人看来 不足以证明 reference\n    features 提供了 qualitatively different signal。entropy_std 的 R²=0.41 处于 drifting/stationary\n    之间的灰色地带，破坏了 DDR 作为 clean bimodal phenomenon 的叙事。审稿人会写：\"The authors'' distinction\n    between ''drifting'' and ''stationary'' features appears to be a gradient rather\n    than a dichotomy, and the surface features alone capture the vast majority of\n    the signal, suggesting this is vocabulary impoverishment measured differently\n    rather than a novel phenomenon.\"\n\n    '\n- name: cross_generator_evaluation\n  plan_id: plan_002\n  description: 'Expand to 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B,\n    Qwen3-0.6B). Leave-one-generator-out (LOGO) CV. 1000 seeds × 5 generators × 5\n    depths ≈ 23K chains.\n\n    '\n  expected_results:\n    total_records: 22800\n    logo_avg_macro_f1: 0.762\n    logo_avg_binary_f1: 0.68\n    logo_binary_ci:\n    - 0.672\n    - 0.688\n    logo_per_gen_binary:\n      pythia_2_8b: 0.711\n      pythia_1b: 0.724\n      olmo_2_1b: 0.643\n      qwen3_1_7b: 0.668\n      qwen3_0_6b: 0.655\n    logo_per_gen_range_pp: 8.1\n    lofo_binary_f1: 0.665\n    lofo_pythia_out_f1: 0.621\n    lofo_qwen_out_f1: 0.648\n    pythia_within_family_inflation: 0.038\n  result_rationale: 'LOGO binary F1 = 0.680，低于论文 framing 中的 0.694（后者是 8-gen 版本，但这里只有\n    5-gen， 训练数据更少）。更关键的是 per-generator variance 很大：Pythia-1B 在 hold-out 时最好 （0.724），因为\n    Pythia-2.8B 在训练集中提供了 same-family signal。OLMo-2-1B 最差（0.643）， 因为它是唯一的 non-Pythia/non-Qwen\n    family。LOFO 进一步降到 0.665，Pythia held-out 降到 0.621 —— 这说明跨 family 泛化比 LOGO 差很多。审稿人会\n    argue Pythia family overlap inflates LOGO by ~3.8 pp，真实 cross-family performance\n    只有 0.62–0.65，远不够 practical。 8.1 pp per-gen range 被视为 high variance = unreliable。\n\n    '\n  tables:\n  - caption: Leave-one-generator-out binary F1 (gen-1 vs gen-2+)\n    rows:\n    - - Held-out Generator\n      - Family\n      - Binary F1\n      - 95% CI\n    - - Pythia-2.8B\n      - Pythia\n      - '0.711'\n      - '[0.693, 0.729]'\n    - - Pythia-1B\n      - Pythia\n      - '0.724'\n      - '[0.707, 0.741]'\n    - - OLMo-2-1B\n      - OLMo\n      - '0.643'\n      - '[0.621, 0.665]'\n    - - Qwen3-1.7B\n      - Qwen\n      - '0.668'\n      - '[0.648, 0.688]'\n    - - Qwen3-0.6B\n      - Qwen\n      - '0.655'\n      - '[0.634, 0.676]'\n    - - '**Average**'\n      - —\n      - '**0.680**'\n      - '[0.672, 0.688]'\n  - caption: Leave-one-family-out binary F1\n    rows:\n    - - Held-out Family\n      - Binary F1\n      - Δ vs LOGO avg\n    - - Pythia (both)\n      - '0.621'\n      - −5.9 pp\n    - - Qwen (both)\n      - '0.648'\n      - −3.2 pp\n    - - OLMo\n      - '0.726'\n      - +4.6 pp\n    - - '**Average**'\n      - '**0.665**'\n      - '**−1.5 pp**'\n  figures_description:\n  - Confusion matrix heatmap (5 panels, one per held-out generator) showing gen-0/gen-1/gen-2+\n    predictions. All 5 panels show gen-1 vs gen-2+ confusion as the dominant error\n    — gen-1 frequently misclassified as gen-2+ (FN rate 78–89% of binary errors).\n    OLMo panel visually the worst with near-uniform gen-1/gen-2+ confusion.\n  analysis: 'Cross-generator generalization 是论文核心卖点，但 worst 档下 LOFO binary F1 = 0.665\n    被审稿人视为 near-chance for practical use。Pythia family inflation 是 concrete evidence\n    that LOGO overestimates generalization。审稿人会写：\"The authors report LOGO F1=0.680,\n    but the more honest LOFO evaluation yields 0.665, and even this is inflated by\n    including two Qwen variants. Single-family holdout F1 ranges from 0.621 (Pythia)\n    to 0.726 (OLMo), suggesting the method''s cross-family generalization is highly\n    variable and may not be robust enough for deployment.\"\n\n    '\n- name: cross_family_reference_model\n  plan_id: plan_003\n  description: 'Test OLMo-2-1B and Qwen3-0.6B as alternative reference models (replacing\n    Pythia-410M). Verify DDR drift persists with non-Pythia reference. Key falsification\n    test for Claim 2.\n\n    '\n  expected_results:\n    logo_f1_pythia_ref: 0.68\n    logo_f1_olmo_ref: 0.672\n    logo_f1_qwen_ref: 0.689\n    entropy_mean_drift_pythia: -1.19\n    entropy_mean_drift_olmo: -0.61\n    entropy_mean_drift_qwen: -0.95\n    olmo_ref_hapax_rho: -0.58\n    olmo_ref_entropy_mean_rho: -0.42\n    olmo_ref_tail_decay_rho: 0.09\n    drift_magnitude_ratio_olmo_vs_pythia: 0.51\n    drift_direction_consistent: true\n    shape_stationary_all_refs: true\n  result_rationale: 'DDR 方向一致（所有 reference model 下 drifting features 都 negative drift），shape\n    features 都 stationary —— 但 drift magnitude 高度依赖 reference model。OLMo reference\n    的 entropy_mean drift 只有 Pythia 的 51%（-0.61 vs -1.19），Spearman ρ 从 -0.60 降到 -0.42。\n    审稿人会 accept \"direction is consistent\" 但 argue \"magnitude is reference-dependent,\n    meaning DDR is partially a function of reference-generator mismatch rather than\n    an intrinsic property of recursive generation.\" 这不会 kill Claim 2 但会 weaken 它 ——\n    审稿人 scores -0.5 pp on Claim 2 credibility。LOGO F1 across references 的差异很小（0.672–0.689），\n    说明分类性能 robust，但 DDR phenomenon characterization 的 precision 被削弱。\n\n    '\n  tables:\n  - caption: Cross-reference-model DDR comparison\n    rows:\n    - - Reference Model\n      - LOGO F1\n      - entropy_mean ρ\n      - hapax ρ\n      - tail_decay ρ\n      - Drift magnitude (avg)\n    - - Pythia-410M\n      - '0.680'\n      - −0.60\n      - −0.63\n      - '+0.04'\n      - '1.19'\n    - - OLMo-2-1B\n      - '0.672'\n      - −0.42\n      - −0.58\n      - '+0.09'\n      - '0.61'\n    - - Qwen3-0.6B\n      - '0.689'\n      - −0.55\n      - −0.61\n      - '+0.06'\n      - '0.95'\n  figures_description:\n  - 3-panel overlay plot showing entropy_mean drift curves (depth 0–4) under each\n    reference model. All three curves decline monotonically, but OLMo reference curve\n    is visibly shallower. Reviewer will annotate the magnitude discrepancy as evidence\n    of reference-model dependence.\n  analysis: 'Falsification test 通过了（drift direction consistent），但 worst 档审稿人会 reframe\n    结果： \"While the direction of entropy drift is consistent across reference models,\n    the magnitude varies by 2×, undermining the claim that DDR is an intrinsic property\n    of recursive generation. A more parsimonious explanation is that DDR magnitude\n    reflects the degree of mismatch between the reference model and the generator,\n    not the depth of generation per se.\" 这是 worst 档 最 subtle 的攻击 —— 技术上实验通过了，但 interpretive\n    framing 被挑战。\n\n    '\n- name: downstream_utility\n  plan_id: plan_004\n  description: 'Fine-tune OLMo-1B on depth-stratified subsets. 3 random seeds with\n    bootstrap CIs. Compare depth-aware filtering vs binary baselines. Sample-count-matched\n    comparison.\n\n    '\n  expected_results:\n    all_data_ppl: 2.335\n    all_data_ppl_ci:\n    - 2.33\n    - 2.34\n    size_matched_ppl: 2.367\n    size_matched_ppl_ci:\n    - 2.362\n    - 2.372\n    depth01_ppl: 2.387\n    depth01_ppl_ci:\n    - 2.381\n    - 2.393\n    binary_filtered_ppl: 2.389\n    binary_filtered_ppl_ci:\n    - 2.384\n    - 2.394\n    depth0_only_ppl: 2.681\n    depth0_only_ppl_ci:\n    - 2.671\n    - 2.691\n    tost_p_2pct: 0.00011\n    tost_p_1pct: 0.087\n    cross_seed_ppl_std: 0.001\n    ranking: all < size_matched < depth01 ≈ binary_filtered << depth0_only\n    depth_filtering_vs_random_delta_ppl: 0.02\n  result_rationale: 'Negative finding 非常 clean：depth-aware filtering 不优于 random subsampling，TOST\n    在 ±2% margin 确认 equivalence。这在 worst 档下被 weaponize 为对整个工作 motivation 的质疑。 审稿人会写：\"The\n    authors'' own Claim 3 demonstrates that generation depth has no downstream utility,\n    raising the fundamental question: if knowing the depth of generation doesn''t\n    help improve model training, what is the practical value of distinguishing gen-1\n    from gen-2+?\" Cross-seed variance 极小（std < 0.002）意味着结果 robust —— 但这 robustness\n    是 negative finding 的 robustness，对论文不利。depth0_only 显著差（2.681）只是说明真实人类文本 vs 纯合成文本有区别\n    —— 这是 binary detection 已经解决的问题。 TOST 在 ±1% margin 不显著（p=0.087）被审稿人注意到但不 weaponize（论文已选\n    ±2%）。\n\n    '\n  tables:\n  - caption: Downstream CLM perplexity by training data depth composition (3 seeds)\n    rows:\n    - - Variant\n      - Train Size\n      - PPL (mean ± std)\n      - Δ vs All\n      - TOST ±2% p\n    - - All depths\n      - 12,299\n      - 2.335 ± 0.001\n      - —\n      - —\n    - - Size-matched random\n      - 3,951\n      - 2.367 ± 0.001\n      - '+0.032'\n      - ref\n    - - Depth 0+1 only\n      - 3,951\n      - 2.387 ± 0.001\n      - '+0.052'\n      - 1.1×10⁻⁴\n    - - Binary filtered\n      - 3,951\n      - 2.389 ± 0.001\n      - '+0.054'\n      - 8.7×10⁻⁵\n    - - Depth 0 only\n      - '797'\n      - 2.681 ± 0.001\n      - '+0.346'\n      - —\n  figures_description:\n  - 'Bar chart with error bars showing perplexity across 5 variants. The three middle\n    bars (size-matched, depth01, binary) are visually indistinguishable within error\n    bars. depth0_only stands out as an outlier. Reviewer annotation: ''The only meaningful\n    distinction is between human text and machine text — precisely the binary detection\n    problem.'''\n  analysis: 'Negative finding 本身是诚实的科学贡献，但在 worst 档下被 R2/R3 weaponize 成 \"if depth\n    doesn''t matter for the most obvious downstream task, the burden of proof is on\n    the authors to show ANY downstream task where depth matters.\" 论文的 framing 是 \"diagnostic\n    tool\" 但 审稿人认为 diagnostic without therapeutic value = limited impact。\n\n    '\n- name: prompt_type_comparison\n  plan_id: plan_005\n  description: 'Compare continuation vs elaboration vs inspired_rewriting chains.\n    1000 seeds × Pythia-2.8B × 3 prompt types.\n\n    '\n  expected_results:\n    cv_f1_continuation: 0.781\n    cv_f1_elaboration: 0.73\n    cv_f1_rewriting: 0.737\n    lopto_avg_f1: 0.752\n    lopto_held_out_continuation_f1: 0.762\n    lopto_held_out_elaboration_f1: 0.733\n    lopto_held_out_rewriting_f1: 0.762\n    depth_retention_d4d0_cont: 0.831\n    depth_retention_d4d0_elab: 0.986\n    depth_retention_d4d0_rewrite: 0.939\n    drift_entropy_mean_cont: -0.557\n    drift_entropy_mean_elab: -0.471\n    drift_entropy_mean_rewrite: -0.477\n    cross_prompt_type_range_pp: 5.1\n  result_rationale: 'Continuation chains 明显优于 elaboration（5.1 pp gap），but elaboration/rewriting\n    的 depth retention 更高（0.986/0.939 vs 0.831）。审稿人 worst 档解读：depth signal 只在 continuation（最简单、最\n    artificial 的 chain type）中强，而更 realistic 的 elaboration/ rewriting 中信号明显弱。\"The method\n    works best on the least realistic generation scenario (verbatim continuation)\n    and degrades on more naturalistic prompt types, suggesting the depth signal is\n    an artifact of the continuation paradigm rather than a general property of recursive\n    generation.\" Elaboration 的 entropy_mean drift 比 continuation 弱 15% （-0.471 vs\n    -0.557），但 hapax drift 反而更强 —— 这种 inconsistency 进一步削弱 DDR 作为 unified phenomenon\n    的叙事。\n\n    '\n  tables:\n  - caption: Per-prompt-type classification performance and drift statistics\n    rows:\n    - - Prompt Type\n      - CV F1\n      - LOPTO F1\n      - Depth Retention\n      - entropy_mean ρ\n      - hapax ρ\n    - - Continuation\n      - '0.781'\n      - '0.762'\n      - '0.831'\n      - −0.557\n      - −0.651\n    - - Elaboration\n      - '0.730'\n      - '0.733'\n      - '0.986'\n      - −0.471\n      - −0.674\n    - - Inspired Rewriting\n      - '0.737'\n      - '0.762'\n      - '0.939'\n      - −0.477\n      - −0.670\n  figures_description:\n  - 3×7 heatmap showing per-feature Spearman ρ across prompt types. Reveals that feature\n    ranking is not stable across prompt types — entropy_mean is strongest for continuation\n    but hapax_ratio is strongest for elaboration/rewriting. This inconsistency undermines\n    the 'universal DDR' narrative.\n  analysis: 'Prompt-type dependence 在 worst 档下被视为 generalizability concern 而非 nuanced\n    finding。 审稿人会 argue：\"The 5 pp gap between continuation and elaboration means the\n    method''s performance is highly sensitive to the (unknowable in practice) generation\n    prompt.\"\n\n    '\n- name: paraphrastic_comparison\n  plan_id: plan_006\n  description: 'Construct parallel paraphrasing chains for comparison with continuation\n    chains. Tests attractor convergence theory.\n\n    '\n  expected_results:\n    paraphrastic_cv_f1: 0.723\n    continuation_cv_f1: 0.781\n    paraphrastic_binary_f1: 0.665\n    continuation_binary_f1: 0.694\n    paraphrastic_drift_entropy_mean: -0.38\n    paraphrastic_depth_retention_d4d0: 0.995\n    attractor_convergence_observed: true\n    effective_classes_paraphrastic: 2\n    delta_para_vs_cont_pp: 2.9\n  result_rationale: 'Paraphrastic chains 显示 attractor convergence（depth retention\n    0.995 ≈ 1.0，即几乎 不丢 chain），但 depth signal 弱于 non-paraphrastic（binary F1 0.665 vs\n    0.694）。 差距只有 2.9 pp —— 审稿人 argue 这太小了，不足以证明 non-paraphrastic chains 有 qualitatively\n    different behavior。\"Both paraphrastic and non-paraphrastic chains show similar\n    (weak) depth signal, contradicting the authors'' claim that non-paraphrastic chains\n    exhibit a fundamentally different depth dynamics.\" Attractor convergence 被确认 但反而成为\n    negative evidence：\"if paraphrastic chains converge to attractors within ~3 iterations,\n    and non-paraphrastic chains show comparable depth signal, the phenomenon is better\n    explained by generic generation drift than by the proposed DDR framework.\"\n\n    '\n  tables:\n  - caption: Paraphrastic vs non-paraphrastic chain comparison\n    rows:\n    - - Chain Type\n      - CV F1\n      - Binary F1\n      - Depth Retention\n      - entropy_mean ρ\n      - Effective Classes\n    - - Non-paraphrastic (continuation)\n      - '0.781'\n      - '0.694'\n      - '0.831'\n      - −0.557\n      - '3'\n    - - Paraphrastic\n      - '0.723'\n      - '0.665'\n      - '0.995'\n      - −0.380\n      - ~2\n    - - Δ\n      - +5.8 pp\n      - +2.9 pp\n      - −0.164\n      - −0.177\n      - '+1'\n  figures_description:\n  - 'Dual-panel: left shows feature drift curves for paraphrastic vs continuation\n    chains (both decline, paraphrastic shallower but similar shape). Right shows confusion\n    matrices side-by-side. The visual similarity between the two panels undermines\n    the ''qualitatively different'' claim.'\n  analysis: '在 worst 档下，this experiment backfires。审稿人预期 non-paraphrastic chains would\n    show dramatically different behavior，但 2.9 pp delta 不够 dramatic。反而证明 depth signal\n    is a general (and weak) generation phenomenon，不是 non-paraphrastic chains 的 unique\n    property。论文需要 reframe 为 \"depth signal exists across chain types\" 而非 \"non-paraphrastic\n    chains are special.\"\n\n    '\n- name: cross_model_chains\n  plan_id: plan_007\n  description: 'Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic web contamination scenario.\n\n    '\n  expected_results:\n    cross_model_binary_f1: 0.764\n    cross_model_3class_f1: 0.789\n    single_model_binary_f1: 0.694\n    single_model_3class_f1: 0.762\n    delta_binary_pp: 7.0\n    delta_3class_pp: 2.7\n    cross_model_logo_binary_f1: 0.83\n    cross_model_easier_reason: generator heterogeneity amplifies distributional shift\n  result_rationale: 'Cross-model chains 的 binary F1 大幅高于 single-model（0.764 vs 0.694,\n    +7 pp）， LOGO 甚至达到 0.830。审稿人在 worst 档下会 reframe 这个结果为 negative evidence： \"The substantially\n    higher F1 on cross-model chains (0.830) suggests the method is primarily detecting\n    generator switching rather than generation depth. In single-model chains (the\n    harder and more interesting case), F1 drops to 0.694.\" 这个 gap 被视为证明 depth signal\n    在 single-model case 中 weak —— 真正的 depth classification 应该在 same-generator chains\n    上 work，而 cross-model improvement 是 \"trivially explained by OOD detection of different\n    model fingerprints at each depth.\"\n\n    '\n  tables:\n  - caption: Cross-model vs single-model chain classification\n    rows:\n    - - Setting\n      - Binary F1\n      - 3-class F1\n      - LOGO Binary F1\n    - - Single-model chains\n      - '0.694'\n      - '0.762'\n      - '0.694'\n    - - Cross-model chains\n      - '0.764'\n      - '0.789'\n      - '0.830'\n    - - Δ\n      - +7.0 pp\n      - +2.7 pp\n      - +13.6 pp\n  figures_description:\n  - 'Scatter plot of per-sample prediction confidence (single-model x-axis vs cross-model\n    y-axis). Points cluster above the diagonal, showing cross-model chains are systematically\n    easier. Reviewer annotation: ''This gap suggests the method detects model switching,\n    not depth.'''\n  analysis: 'Cross-model improvement 是 double-edged sword。在 worst 档下它证明了 \"easy case\n    更好\" 但被 reinterpreted 为 the method doesn''t truly measure depth —— 而是 measures\n    generator heterogeneity。审稿人会 demand \"same-generator transfer\" 作为 real benchmark，where\n    0.694 is the relevant number。\n\n    '\n- name: multi_domain_seeds\n  plan_id: plan_008\n  description: 'Expand to 4 domains: Wikipedia, news, scientific, creative writing.\n    500 seeds per domain × 5 depths.\n\n    '\n  expected_results:\n    wikipedia_binary_f1: 0.724\n    news_binary_f1: 0.667\n    scientific_binary_f1: 0.631\n    creative_binary_f1: 0.658\n    cross_domain_logo_binary_f1: 0.652\n    max_gap_vs_wiki_pp: 9.3\n    worst_domain: scientific\n    best_domain: wikipedia\n    domain_variance_std: 0.034\n  result_rationale: 'Wikipedia（训练数据的主 domain）表现最好（0.724），scientific 最差（0.631）—— 9.3\n    pp gap。 审稿人在 worst 档下 argue：\"The method''s performance is domain-dependent, with\n    scientific text yielding near-chance binary F1 (0.631). Since depth classification\n    is most needed for scientific text (where AI contamination is a growing concern\n    per the authors'' own motivation), this domain sensitivity is a critical practical\n    limitation.\" Cross-domain LOGO（training on 3 domains, test on 1）进一步降到 0.652。Domain\n    dependence + generator dependence + temperature dependence + instruct dependence\n    = cumulative scope narrowing that makes the method seem increasingly specialized.\n\n    '\n  tables:\n  - caption: Per-domain binary F1 (LOGO across generators, within-domain)\n    rows:\n    - - Domain\n      - Seeds\n      - Binary F1\n      - 95% CI\n      - Δ vs Wiki\n    - - Wikipedia\n      - '500'\n      - '0.724'\n      - '[0.704, 0.744]'\n      - —\n    - - News\n      - '500'\n      - '0.667'\n      - '[0.645, 0.689]'\n      - −5.7 pp\n    - - Creative\n      - '500'\n      - '0.658'\n      - '[0.635, 0.681]'\n      - −6.6 pp\n    - - Scientific\n      - '500'\n      - '0.631'\n      - '[0.607, 0.655]'\n      - −9.3 pp\n    - - '**Cross-domain LOGO**'\n      - '2000'\n      - '**0.652**'\n      - '[0.638, 0.666]'\n      - —\n  figures_description:\n  - Radar chart showing binary F1 across 4 domains × 3 prompt types. The shape is\n    asymmetric (Wikipedia+continuation = best corner, scientific+elaboration = worst\n    corner), making the fragility visually apparent.\n  analysis: 'Domain dependence 在 worst 档下被叠加到 existing scope limitations 上。审稿人列出 cumulative\n    conditions：\"base models only, temperature ∈ [0.5, 0.9], continuation chains, Wikipedia-domain\n    seeds\" —— 这是 increasingly narrow niche that undermines any practical framing of\n    the work.\n\n    '\n- name: finer_grained_ordinal\n  plan_id: plan_009\n  description: '5-class ordinal classification (gen-0 through gen-4). Test if depth\n    signal extends beyond 3-class resolution.\n\n    '\n  expected_results:\n    five_class_macro_f1: 0.468\n    five_class_ci:\n    - 0.451\n    - 0.485\n    three_class_macro_f1: 0.762\n    ordinal_coral_f1: 0.472\n    ordinal_frank_hall_f1: 0.465\n    gen1_vs_gen2_confusion_rate: 0.43\n    gen2_vs_gen3_confusion_rate: 0.51\n    gen3_vs_gen4_confusion_rate: 0.48\n    mean_absolute_depth_error: 0.89\n  result_rationale: '5-class F1 降到 0.468，接近 5-class random baseline（0.20）但仍显著高于 chance。\n    Ordinal methods（CORAL, Frank-Hall）无改善（0.472, 0.465）。Gen-2/gen-3/gen-4 之间 几乎无法区分（confusion\n    rate 43–51%）。审稿人在 worst 档下 argue：\"The 5-class F1 of 0.468 confirms that depth\n    signal is extremely shallow — the method can roughly distinguish ''early'' (gen-0/1)\n    from ''late'' (gen-2+) but cannot meaningfully estimate depth. The 3-class formulation\n    is not a principled choice but a ceiling imposed by signal weakness.\" 这直接 打击了\n    \"depth classification\" 作为 task formulation 的 novelty —— 如果实际上只有 binary-ish signal，那\n    task formulation 的贡献 = trivially extending binary detection by one class。\n\n    '\n  tables:\n  - caption: Ordinal classification resolution comparison\n    rows:\n    - - Granularity\n      - Method\n      - Macro F1\n      - Ordinal Improvement\n    - - 3-class\n      - XGBoost\n      - '0.762'\n      - —\n    - - 5-class\n      - XGBoost\n      - '0.468'\n      - —\n    - - 5-class\n      - CORAL\n      - '0.472'\n      - +0.4 pp\n    - - 5-class\n      - Frank-Hall\n      - '0.465'\n      - −0.3 pp\n  figures_description:\n  - 5×5 confusion matrix heatmap. Gen-0 is cleanly classified (>0.90 recall), gen-1\n    shows moderate confusion with gen-2, and gen-2/3/4 form a near-uniform block —\n    visually a 'binary-plus-noise' pattern rather than ordinal resolution.\n  analysis: '5-class collapse 是 worst 档最有力的 evidence against task formulation novelty。\n    审稿人会 argue 这证明 depth signal 本质上是 binary（human vs machine）加上一点 gen-1 distinctiveness，而非\n    true ordinal depth estimation。\"The authors frame a 3-class problem, but the data\n    supports at most 2.5 classes.\"\n\n    '\n- name: human_edit_robustness\n  plan_id: plan_010\n  description: 'Robustness to simulated human edits: (A) random word replacement 5/10/20%,\n    (B) LLM-simulated light rephrasing.\n\n    '\n  expected_results:\n    baseline_binary_f1: 0.694\n    random_5pct_f1: 0.648\n    random_10pct_f1: 0.611\n    random_20pct_f1: 0.583\n    llm_rephrase_f1: 0.641\n    llm_rephrase_edit_distance: 0.51\n    degradation_5pct_pp: -4.6\n    degradation_10pct_pp: -8.3\n    degradation_20pct_pp: -11.1\n    degradation_llm_pp: -5.3\n  result_rationale: 'Even 5% random replacement 造成 4.6 pp drop（0.694 → 0.648），LLM\n    rephrasing 造成 5.3 pp drop（→ 0.641）。审稿人在 worst 档下 argue：\"In practice, AI-generated\n    text is almost always edited before publication. The method loses 5+ pp F1 from\n    light editing (51% edit distance), and this is on top of the already-modest 0.694\n    baseline. After realistic editing, depth classification falls to ~0.64, making\n    it effectively useless.\" 20% replacement 降到 0.583 —— 接近 chance for binary task。这与\n    instruct degradation、 temperature sensitivity、domain dependence 一起构成 cumulative\n    fragility picture。\n\n    '\n  tables:\n  - caption: Robustness to simulated human edits\n    rows:\n    - - Perturbation\n      - Binary F1\n      - Δ vs Baseline\n      - Edit Distance\n    - - None (baseline)\n      - '0.694'\n      - —\n      - '0.0'\n    - - Random 5%\n      - '0.648'\n      - −4.6 pp\n      - ~0.05\n    - - Random 10%\n      - '0.611'\n      - −8.3 pp\n      - ~0.10\n    - - Random 20%\n      - '0.583'\n      - −11.1 pp\n      - ~0.20\n    - - LLM rephrase\n      - '0.641'\n      - −5.3 pp\n      - '0.51'\n  figures_description:\n  - 'Line chart: binary F1 vs edit intensity (0%, 5%, 10%, 20%, LLM). Near-linear\n    degradation. LLM rephrase point sits between 5% and 10% random. Shaded area shows\n    95% CI widening at higher edit levels.'\n  analysis: 'Robustness 实验在 worst 档下是 lose-lose：如果 robust，审稿人 say \"shallow features\n    aren''t capturing anything generation-specific\"; 如果 fragile（as here），审稿人 say \"not\n    practical.\" 这里是 fragile，confirm 审稿人 prior that depth signal is surface-level and\n    easily disrupted.\n\n    '\n- name: ld_score_feature\n  plan_id: plan_011\n  description: 'Add LD-Score (character-distribution signature) as 8th feature. Test\n    character-level complementarity to word/entropy features.\n\n    '\n  expected_results:\n    seven_feature_f1: 0.773\n    eight_feature_with_ld_f1: 0.779\n    ld_score_alone_f1: 0.623\n    ld_score_spearman_depth: -0.31\n    marginal_improvement_pp: 0.6\n    feature_importance_ld: 0.028\n  result_rationale: 'LD-Score 作为单独 feature 只有 0.623 F1，加入后 marginal improvement 仅\n    0.6 pp （0.773 → 0.779），feature importance 排最后（0.028）。审稿人在 worst 档不会 attack 这个实验本身（它是\n    minor addition），但会 note：\"Adding LD-Score provides negligible improvement, suggesting\n    the character-level depth signal is largely subsumed by the existing word-level\n    features — further evidence that all these features measure the same underlying\n    vocabulary impoverishment.\" 这 reinforces RC1（repackaging）。\n\n    '\n  tables:\n  - caption: LD-Score feature addition\n    rows:\n    - - Feature Set\n      - Macro F1\n      - Δ\n    - - 7 features (baseline)\n      - '0.773'\n      - —\n    - - 7 + LD-Score\n      - '0.779'\n      - +0.6 pp\n    - - LD-Score only\n      - '0.623'\n      - —\n  figures_description:\n  - Feature importance bar chart (8 features). LD-Score is the shortest bar, visually\n    insignificant compared to hapax_ratio, TTR, entropy_mean.\n  analysis: 'Minor experiment, minor result. 在 worst 档下被用作 supporting evidence for\n    \"all signals are the same signal\" narrative，但不是 primary attack vector。\n\n    '\n- name: end_to_end_classifier\n  plan_id: plan_012\n  description: 'QLoRA fine-tuned end-to-end depth classifier. Compares learned representations\n    vs handcrafted 7-feature ensemble.\n\n    '\n  expected_results:\n    qlora_3class_f1: 0.891\n    qlora_3class_ci:\n    - 0.878\n    - 0.904\n    qlora_binary_f1: 0.842\n    qlora_binary_ci:\n    - 0.826\n    - 0.858\n    qlora_5class_f1: 0.571\n    seven_feature_3class_f1: 0.762\n    seven_feature_binary_f1: 0.694\n    delta_3class_pp: 12.9\n    delta_binary_pp: 14.8\n    qlora_logo_3class_f1: 0.743\n    qlora_logo_binary_f1: 0.712\n    qlora_inference_cost_ratio: 47.0\n  result_rationale: 'QLoRA within-distribution 大幅碾压 7-feature（3-class 0.891 vs 0.762,\n    +12.9 pp）， 但 LOGO 下差距缩小（0.743 vs 0.762，7-feature 反而更好 for 3-class）。Binary LOGO\n    QLoRA 仍然更好（0.712 vs 0.694）。审稿人在 worst 档下会 cherry-pick within-distribution numbers：\"A\n    simple QLoRA classifier achieves 0.842 binary F1, dwarfing the proposed method''s\n    0.694. While the authors may argue their method is more lightweight, the 14.8\n    pp gap suggests the handcrafted features miss substantial depth signal that end-to-end\n    learning captures.\" 论文的 efficiency argument（7-feature 用 410M reference 而 QLoRA\n    用 full model）在 worst 档下被 dismiss：\"inference cost is not a compelling argument\n    when the method is 15 pp worse.\" LOGO 下 QLoRA 的 cross-generator generalization\n    差（3-class 0.743 < 0.762）可以作为 rebuttal point，但审稿人 already scored low before seeing\n    this nuance。\n\n    '\n  tables:\n  - caption: End-to-end (QLoRA) vs handcrafted 7-feature ensemble\n    rows:\n    - - Method\n      - 3-class F1\n      - Binary F1\n      - LOGO 3-class\n      - LOGO Binary\n      - Cost Ratio\n    - - 7-feature XGBoost\n      - '0.762'\n      - '0.694'\n      - '0.762'\n      - '0.694'\n      - 1×\n    - - QLoRA (OLMo-1B)\n      - '0.891'\n      - '0.842'\n      - '0.743'\n      - '0.712'\n      - 47×\n    - - Δ\n      - +12.9 pp\n      - +14.8 pp\n      - −1.9 pp\n      - +1.8 pp\n      - —\n  figures_description:\n  - 'Grouped bar chart: within-distribution vs LOGO for both methods. Within-distribution\n    shows QLoRA dominating; LOGO shows convergence. The within-distribution gap is\n    visually dramatic and is what the reviewer will focus on.'\n  analysis: 'End-to-end comparison 在 worst 档下是 devastating。审稿人会 focus on within-distribution\n    gap (14.8 pp) and dismiss the LOGO nuance as \"an artifact of limited training\n    generators.\" 论文需要 pre-empt 这个 attack by leading with LOGO numbers and framing\n    within-distribution as oracle-access upper bound。\n\n    '\n- name: text_length_control\n  plan_id: plan_013\n  description: 'Address text length confound: length distribution analysis, length-normalized\n    features, length-matched subsampling.\n\n    '\n  expected_results:\n    length_depth_spearman: 0.12\n    length_depth_p: 0.001\n    length_matched_binary_f1: 0.724\n    unmatched_binary_f1: 0.77\n    delta_pp: -4.6\n    normalized_ttr_trend_preserved: true\n    normalized_hapax_trend_preserved: true\n    length_is_primary_confound: false\n    length_contributes_to_signal: true\n    short_text_dropout_bias: true\n  result_rationale: 'Length-matched F1 降 4.6 pp（0.770 → 0.724）—— 意味着 text length 贡献了约\n    6% 的 总 signal。审稿人在 worst 档下会 magnify 这个 finding：\"After controlling for text length,\n    the already-modest F1 drops further to 0.724 (unmatched) → this suggests that\n    part of the ''depth signal'' is simply a length artifact.\" 但 normalized features\n    的 trend 保持说明 depth signal 不完全来自 length。这是 worst 档中一个 mixed result —— 不会 kill the\n    paper 但会 reduce credibility of the headline number by ≤5 pp。Short text dropout\n    bias 的 发现（deeper depths 有更多短文本被过滤掉）adds confound complexity that makes the narrative\n    harder to follow。\n\n    '\n  tables:\n  - caption: Length control analysis\n    rows:\n    - - Condition\n      - Binary F1\n      - Δ\n    - - Unmatched (original)\n      - '0.770'\n      - —\n    - - Length-matched subsample\n      - '0.724'\n      - −4.6 pp\n    - - Length-normalized features\n      - '0.748'\n      - −2.2 pp\n  figures_description:\n  - 'Left: text length distribution violin plots by depth (showing subtle rightward\n    shift at depth 0, leftward at depth 4). Right: before/after length matching classification\n    boundary plots.'\n  analysis: 'Length confound 是 necessary experiment 但在 worst 档下 result = \"yes, some\n    of the signal was length.\" 4.6 pp drop 不是 catastrophic 但会 erode reviewer trust\n    in all other reported numbers (\"were these also length-confounded?\").\n\n    '\n- name: large_scale_generator\n  plan_id: plan_014\n  description: 'Add Qwen3-8B-Base to test depth signal at 7B+ scale. 1000 seeds ×\n    5 depths.\n\n    '\n  expected_results:\n    qwen3_8b_logo_binary_f1: 0.637\n    qwen3_8b_logo_3class_f1: 0.683\n    qwen3_8b_within_cv_f1: 0.711\n    six_gen_logo_avg_f1: 0.789\n    delta_vs_avg_pp: -10.6\n    hapax_rho_8b: -0.41\n    ttr_rho_8b: -0.39\n    entropy_mean_rho_8b: -0.33\n    feature_margin_compression: 0.58\n  result_rationale: 'Qwen3-8B 的 LOGO binary F1 = 0.637，比 6-gen average 低 10.6 pp。Feature\n    drift magnitudes 全面压缩（hapax ρ 从 avg −0.63 降到 −0.41，compression ratio 0.58）。 这与\n    paper_framing 中的 scale effect 一致，但 worst 档审稿人会 extrapolate：\"At 8B the signal is\n    already substantially degraded (−10.6 pp). Frontier models (70B+) and API models\n    (GPT-4, Claude) — which generate the vast majority of real-world AI text — would\n    presumably show even weaker signal, making the method irrelevant for the contamination\n    problem the paper claims to address.\" 这是 worst 档中 most damaging extrapolation\n    ——  审稿人不需要实验数据就可以 argue 方法在 practical scale 上 doesn''t work。Within-CV F1 = 0.711\n    还可以（说明 8B 自身的 depth signal 存在），但 cross-generator transfer 到 8B 很弱（0.637），meaning\n    smaller models 的 training data 不 transfer 到大模型。\n\n    '\n  tables:\n  - caption: 'Scale effect: Qwen3-8B vs smaller generators'\n    rows:\n    - - Generator\n      - Size\n      - LOGO Binary F1\n      - hapax ρ\n      - entropy_mean ρ\n    - - Pythia-1B\n      - 1.0B\n      - '0.724'\n      - −0.65\n      - −0.60\n    - - OLMo-2-1B\n      - 1.5B\n      - '0.643'\n      - −0.58\n      - −0.55\n    - - Pythia-2.8B\n      - 2.8B\n      - '0.711'\n      - −0.63\n      - −0.60\n    - - Qwen3-8B\n      - 8.0B\n      - '0.637'\n      - −0.41\n      - −0.33\n    - - '**Trend**'\n      - —\n      - '**Declining**'\n      - '**Compressing**'\n      - '**Compressing**'\n  figures_description:\n  - Log-scale x-axis (model size) vs binary F1 y-axis, with feature drift magnitude\n    as bubble size. Clear downward trend from 1B to 8B. Extrapolation dotted line\n    to 70B crosses 0.50 (chance) at ~30B, visually devastating for scale argument.\n  analysis: 'Scale degradation 是 worst 档的 structural problem —— 审稿人不需要 70B 实验就可以 argue\n    via extrapolation。Paper 的 honest reporting of this limitation (\"defines scope\n    boundary\") 在 worst 档下被 reframed 为 \"the scope boundary excludes all models people\n    actually care about.\"\n\n    '\n- name: ordinal_baseline_comparison\n  plan_id: plan_015\n  description: 'Compare existing detector continuous scores (FastDetectGPT, Binoculars,\n    LD-Score) as ordinal depth predictors vs our 7-feature ensemble.\n\n    '\n  expected_results:\n    seven_feature_logo_f1: 0.68\n    avg_logprob_logo_f1: 0.653\n    ld_score_logo_f1: 0.641\n    fastdetectgpt_logo_f1: 0.612\n    binoculars_logo_f1: 0.571\n    seven_feature_vs_avglogprob_delta_pp: 2.7\n    seven_feature_vs_ld_delta_pp: 3.9\n    bootstrap_p_7feat_vs_avglogprob: 0.038\n    multi_detector_ensemble_f1: 0.708\n    multi_det_vs_7feat_delta_pp: 2.8\n  result_rationale: '7-feature ensemble (0.680) 优于所有 single detectors，但 margin 很小\n    —— vs Avg-LogProb 只有 2.7 pp (p=0.038, barely significant)。更关键的是 multi-detector\n    ensemble（4 detectors + surface）达到 0.708，反过来超过 7-feature 2.8 pp。审稿人在 worst 档下会\n    argue：\"A simple average of existing detector scores (Avg-LogProb: 0.653) achieves\n    96% of the proposed method''s F1, raising the question of whether depth-specific\n    features are necessary. Moreover, a multi-detector ensemble outperforms the proposed\n    features by 2.8 pp, suggesting that the optimal approach is to repurpose existing\n    detectors rather than design depth-specific features.\" 这直接 undermines Claim 1\n    的 contribution：if existing tools + trivial ensembling works comparably or better，新\n    feature set 的 value proposition collapses。\n\n    Bootstrap test 的 p=0.038 是 borderline significant —— worst 档审稿人会 note \"barely\n    significant and not corrected for multiple comparisons.\" 如果 Bonferroni correct\n    for 4 comparisons，p=0.152 → not significant。\n\n    '\n  tables:\n  - caption: 'Ordinal depth classification: 7-feature vs existing detector baselines'\n    rows:\n    - - Method\n      - LOGO Binary F1\n      - 95% CI\n      - Δ vs 7-feat\n      - Bootstrap p\n    - - '**7-feature ensemble**'\n      - '**0.680**'\n      - '[0.672, 0.688]'\n      - —\n      - —\n    - - Avg-LogProb (single)\n      - '0.653'\n      - '[0.612, 0.694]'\n      - −2.7 pp\n      - '0.038'\n    - - LD-Score (single)\n      - '0.641'\n      - '[0.598, 0.684]'\n      - −3.9 pp\n      - '0.011'\n    - - FastDetectGPT (single)\n      - '0.612'\n      - '[0.571, 0.653]'\n      - −6.8 pp\n      - '0.002'\n    - - Binoculars (single)\n      - '0.571'\n      - '[0.528, 0.614]'\n      - −10.9 pp\n      - <0.001\n    - - 4-det + surface ensemble\n      - '0.708'\n      - '[0.694, 0.722]'\n      - +2.8 pp\n      - '0.024'\n  figures_description:\n  - Forest plot showing each method's LOGO F1 with 95% CI. CIs overlap heavily between\n    7-feature and Avg-LogProb/LD-Score. Multi-detector ensemble CI sits above 7-feature\n    point estimate. Visually, the 7-feature method is 'in the pack' rather than clearly\n    superior.\n  analysis: Baseline comparison 在 worst 档下是 most dangerous experiment。7-feature 的\n    advantage over best single detector (2.7 pp) 太小，且被 multi-detector ensemble surpassed。\n    审稿人会 conclude：\"The proposed features provide marginal, statistically borderline\n    improvement over simply using existing detector scores for depth estimation. Given\n    the complexity of the feature engineering and the need for a reference model,\n    this represents insufficient contribution for even Findings-level publication.\"\n    这直接 targets the paper's reason to exist。\n",
      "numLines": 1089,
      "startLine": 1,
      "totalLines": 1089
    }
  },
  "sourceToolAssistantUUID": "92e64cfd-212d-4aef-9db8-90e1f7213744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T21:51:17.099Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S72vMsEargZF6Hn1mWVgqg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/imagined_experiments.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8f2349c-3a55-4c78-920a-c96a9918c9ed",
  "isSidechain": false,
  "requestId": "req_011CbGTHhgVu4EhDE5cHCLW2",
  "type": "assistant",
  "uuid": "962e16d7-e2c2-49aa-b807-83cb852229dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CvU3xuVaxvt1yL5ZZXypD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 36896,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 36896,
          "cache_creation_input_tokens": 1335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1335
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

_source line 14 · 2026-05-21T21:51:17.105Z_

<details><summary>↩ Tool result · `toolu_01S72vMsEargZF6Hn1mWVgqg`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立。DDR 二分法 (drifting: hapax, TTR, entropy_mean |ρ|≥0.55;
3	  stationary: tail_decay, entropy_max |ρ|<0.10) 在 8+ generators / 5 families 上鲁棒，
4	  entropy_std 归为 weakly drifting (|ρ|≈0.20)，不破坏主叙事。 三条 claim 均有充分实验支撑：(1) LOGO binary
5	  F1=0.694 为 headline，LOFO 0.686 和 cross-model 0.830 验证泛化性；(2) DDR 跨 3 个 reference
6	  model 和 5 个 generator family 稳健， TOST 确认 shape feature stationarity；(3) negative
7	  downstream finding 以 TOST ±2% margin 确认。 Scope limitations (base-only, t≤0.7, ≤14B)
8	  诚实报告但不动摇核心 contribution。 论文按原 framing 直接提交 ARR。
9	
10	  '
11	imagined_experiments:
12	- name: feature_ablation_and_trend
13	  plan_id: plan_001
14	  description: MVP 数据上的三部分分析：(A) feature ablation (full/surface/reference), (B) H1/H2
15	    trend analysis, (C) perplexity pre-validation
16	  expected_results:
17	    ablation_full_macro_f1: 0.82
18	    ablation_surface_only_f1: 0.763
19	    ablation_reference_only_f1: 0.719
20	    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'
21	    mcnemar_full_vs_surface_p: 0.0
22	    mcnemar_full_vs_ref_p: 0.0
23	    h2_drifting_features:
24	    - entropy_mean
25	    - ttr
26	    - hapax_ratio
27	    h2_slope_entropy_mean: -0.29
28	    h2_slope_ttr: -0.034
29	    h2_slope_hapax_ratio: -0.043
30	    h2_R2_entropy_mean: 0.93
31	    h2_R2_ttr: 0.89
32	    h2_R2_hapax_ratio: 0.92
33	    h1_stationary_features:
34	    - tail_decay
35	    - entropy_std
36	    - entropy_max
37	    - entropy_min
38	    h1_slope_tail_decay: 0.002
39	    h1_R2_tail_decay: 0.03
40	    entropy_std_slope: -0.12
41	    entropy_std_R2: 0.41
42	    median_ppl_by_depth:
43	    - 13.5
44	    - 4.96
45	    - 3.0
46	    - 2.07
47	    - 1.72
48	    ppl_depth_trend: monotonic_decrease
49	  result_rationale: 'Full set 显著优于任一子集 (5.7-10.1pp)。Surface features 捕捉词汇多样性衰减 (TTR/hapax
50	    随 depth 单调递减)，reference features 捕捉 NLL 分布位移 (entropy_mean drift)，两组信号互补。McNemar
51	    p=0 确认非冗余。 H2 drifting features 呈清晰单调趋势 (R²>0.89)：递归生成导致词汇空间收缩 和 NLL 均值下降 (recursive
52	    compression)。H1 stationary features 保持平坦 (tail_decay R²=0.03)：NLL 分布的 shape 参数在
53	    location shift 下近似不变。 entropy_std 弱趋势 (R²=0.41) 远低于 drifting 组，归为 intermediate
54	    不影响主叙事。 Perplexity 单调递减：deeper text 对 reference model 更 predictable， 因为 model
55	    自身输出的 recursive compression 使 NLL 分布左移。
56	
57	    '
58	  tables:
59	  - 'Table A1: Feature Ablation 5-fold CV — Full 0.820, Surface 0.763, Ref 0.719'
60	  - 'Table A2: Per-feature linear trend (slope, R², p-value) across depths 0–4'
61	  figures_description:
62	  - 'Fig 2: 7 features mean±std across depth 0–4。drifting 三特征 (hapax, TTR, entropy_mean)
63	    显示清晰单调递减, R²>0.89；stationary 特征 (tail_decay, entropy_max) 水平。entropy_std 弱趋势 (浅灰色标注为
64	    intermediate)'
65	  - 'Fig S1: Pythia-410M perplexity by depth, 单调递减曲线 (13.50→1.72)'
66	  analysis: 'Surface 和 reference 信号互补性经 McNemar 确认 (p=0)，是论文 complementarity claim
67	    的基础。 entropy_std 的 intermediate status (|slope|=0.12, R²=0.41) 需在正文中诚实讨论， 但不破坏
68	    3-drifting / 2-stationary 的核心二分法， 因为 entropy_std 的 drift magnitude 仅为 drifting
69	    组的 1/3。 Perplexity pre-validation 确认 NLL 分布中存在 depth-dependent signal，为 Claim
70	    3 建立 baseline。
71	
72	    '
73	- name: cross_generator_evaluation
74	  plan_id: plan_002
75	  description: 5-generator LOGO 跨 generator 泛化评估 (Pythia-2.8B, Pythia-1B, OLMo-2-1B,
76	    Qwen3-1.7B, Qwen3-0.6B)
77	  expected_results:
78	    total_records: 23032
79	    generators:
80	    - pythia-2.8b
81	    - pythia-1b
82	    - olmo-2-1b
83	    - qwen3-1.7b
84	    - qwen3-0.6b
85	    families:
86	    - Pythia
87	    - OLMo
88	    - Qwen
89	    logo_macro_f1: 0.804
90	    logo_binary_f1: 0.72
91	    logo_binary_ci:
92	    - 0.708
93	    - 0.732
94	    per_gen_macro_f1:
95	      pythia-1b: 0.851
96	      pythia-2.8b: 0.804
97	      qwen3-0.6b: 0.818
98	      qwen3-1.7b: 0.805
99	      olmo-2-1b: 0.752
100	    per_gen_binary_f1:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "962e16d7-e2c2-49aa-b807-83cb852229dc",
  "isSidechain": false,
  "promptId": "00fafa99-9202-4e1a-8fd4-c2e127d8de99",
  "type": "user",
  "uuid": "6b8e70f1-20c4-4ea5-ae2e-c23505ac3211",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: '原始 framing 完全成立。DDR 二分法 (drifting: hapax, TTR, entropy_mean |ρ|≥0.55;\n  stationary: tail_decay, entropy_max |ρ|<0.10) 在 8+ generators / 5 families 上鲁棒，\n  entropy_std 归为 weakly drifting (|ρ|≈0.20)，不破坏主叙事。 三条 claim 均有充分实验支撑：(1) LOGO binary\n  F1=0.694 为 headline，LOFO 0.686 和 cross-model 0.830 验证泛化性；(2) DDR 跨 3 个 reference\n  model 和 5 个 generator family 稳健， TOST 确认 shape feature stationarity；(3) negative\n  downstream finding 以 TOST ±2% margin 确认。 Scope limitations (base-only, t≤0.7, ≤14B)\n  诚实报告但不动摇核心 contribution。 论文按原 framing 直接提交 ARR。\n\n  '\nimagined_experiments:\n- name: feature_ablation_and_trend\n  plan_id: plan_001\n  description: MVP 数据上的三部分分析：(A) feature ablation (full/surface/reference), (B) H1/H2\n    trend analysis, (C) perplexity pre-validation\n  expected_results:\n    ablation_full_macro_f1: 0.82\n    ablation_surface_only_f1: 0.763\n    ablation_reference_only_f1: 0.719\n    ref_vs_surf_bootstrap_ci: '[0.706,0.733] vs [0.747,0.774]'\n    mcnemar_full_vs_surface_p: 0.0\n    mcnemar_full_vs_ref_p: 0.0\n    h2_drifting_features:\n    - entropy_mean\n    - ttr\n    - hapax_ratio\n    h2_slope_entropy_mean: -0.29\n    h2_slope_ttr: -0.034\n    h2_slope_hapax_ratio: -0.043\n    h2_R2_entropy_mean: 0.93\n    h2_R2_ttr: 0.89\n    h2_R2_hapax_ratio: 0.92\n    h1_stationary_features:\n    - tail_decay\n    - entropy_std\n    - entropy_max\n    - entropy_min\n    h1_slope_tail_decay: 0.002\n    h1_R2_tail_decay: 0.03\n    entropy_std_slope: -0.12\n    entropy_std_R2: 0.41\n    median_ppl_by_depth:\n    - 13.5\n    - 4.96\n    - 3.0\n    - 2.07\n    - 1.72\n    ppl_depth_trend: monotonic_decrease\n  result_rationale: 'Full set 显著优于任一子集 (5.7-10.1pp)。Surface features 捕捉词汇多样性衰减 (TTR/hapax\n    随 depth 单调递减)，reference features 捕捉 NLL 分布位移 (entropy_mean drift)，两组信号互补。McNemar\n    p=0 确认非冗余。 H2 drifting features 呈清晰单调趋势 (R²>0.89)：递归生成导致词汇空间收缩 和 NLL 均值下降 (recursive\n    compression)。H1 stationary features 保持平坦 (tail_decay R²=0.03)：NLL 分布的 shape 参数在\n    location shift 下近似不变。 entropy_std 弱趋势 (R²=0.41) 远低于 drifting 组，归为 intermediate\n    不影响主叙事。 Perplexity 单调递减：deeper text 对 reference model 更 predictable， 因为 model\n    自身输出的 recursive compression 使 NLL 分布左移。\n\n    '\n  tables:\n  - 'Table A1: Feature Ablation 5-fold CV — Full 0.820, Surface 0.763, Ref 0.719'\n  - 'Table A2: Per-feature linear trend (slope, R², p-value) across depths 0–4'\n  figures_description:\n  - 'Fig 2: 7 features mean±std across depth 0–4。drifting 三特征 (hapax, TTR, entropy_mean)\n    显示清晰单调递减, R²>0.89；stationary 特征 (tail_decay, entropy_max) 水平。entropy_std 弱趋势 (浅灰色标注为\n    intermediate)'\n  - 'Fig S1: Pythia-410M perplexity by depth, 单调递减曲线 (13.50→1.72)'\n  analysis: 'Surface 和 reference 信号互补性经 McNemar 确认 (p=0)，是论文 complementarity claim\n    的基础。 entropy_std 的 intermediate status (|slope|=0.12, R²=0.41) 需在正文中诚实讨论， 但不破坏\n    3-drifting / 2-stationary 的核心二分法， 因为 entropy_std 的 drift magnitude 仅为 drifting\n    组的 1/3。 Perplexity pre-validation 确认 NLL 分布中存在 depth-dependent signal，为 Claim\n    3 建立 baseline。\n\n    '\n- name: cross_generator_evaluation\n  plan_id: plan_002\n  description: 5-generator LOGO 跨 generator 泛化评估 (Pythia-2.8B, Pythia-1B, OLMo-2-1B,\n    Qwen3-1.7B, Qwen3-0.6B)\n  expected_results:\n    total_records: 23032\n    generators:\n    - pythia-2.8b\n    - pythia-1b\n    - olmo-2-1b\n    - qwen3-1.7b\n    - qwen3-0.6b\n    families:\n    - Pythia\n    - OLMo\n    - Qwen\n    logo_macro_f1: 0.804\n    logo_binary_f1: 0.72\n    logo_binary_ci:\n    - 0.708\n    - 0.732\n    per_gen_macro_f1:\n      pythia-1b: 0.851\n      pythia-2.8b: 0.804\n      qwen3-0.6b: 0.818\n      qwen3-1.7b: 0.805\n      olmo-2-1b: 0.752\n    per_gen_binary_f1:",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 855
    }
  },
  "sourceToolAssistantUUID": "962e16d7-e2c2-49aa-b807-83cb852229dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-21T21:51:17.214Z_

````json
{
  "parentUuid": "6b8e70f1-20c4-4ea5-ae2e-c23505ac3211",
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
  "uuid": "07ac5fee-1de4-4c68-a0e5-73ebee0324fa",
  "timestamp": "2026-05-21T21:51:17.214Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Reviewer 认为 scope 太窄、F1 太低、task motivation 不足，Findings 被拒，需 reframe 后投 fallback venue 核心假设：['多位 reviewer 认为 base-model-only + temperature [0.5,0.9] 的 scop…",
  "leafUuid": "07ac5fee-1de4-4c68-a0e5-73ebee0324fa",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe depth-fingerprinting to distributional-dynamics characterization",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7"
}
```

---

### Assistant

_source line 18 · 2026-05-21T21:53:52.962Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the previous worst-tier imagined experiments and the best-tier for comparison. I also have the actual completed experiment results from the registry. The user wants me to generate detailed worst-tier predictions for each planned experiment, but now I need to update these predictions based on the actual completed experiment data.

Let me look at the actual completed experiments more carefully and compare with the worst-tier predictions to see what has actually happened. Many experiments are already completed. The user wants me to generate the worst-tier imagined experiments based on the current state, meaning I need to produce predictions that are consistent with the worst-tier definition but also informed by what experiments have actually been completed.


I'm realizing the experiment_plan lists all experiments with "planned" status, but the registry shows many are already completed. So the plan is the original blueprint while the registry captures what actually happened. For the worst-tier scenario, I should generate predictions for each planned experiment as if they haven't run yet, showing what the worst possible outcomes would be. does exactly this: it generates imagined results for all experiments as if they were to be run, even though some have already been completed. The key is that this is a "dream" exercise - imagining what would happen in the worst case.

But the user says the previous worst-tier dream was from dream_20260520T100349. Now there's a newer dream report at dream_20260520T232427 which has best/median but maybe not worst. Let me check.

Actually, looking at the data more carefully, I notice the user has provided very detailed context in the prompt including:
1. The worst tier definition (reviewer scores, scope concerns, etc.)
2. The paper framing
3. The experiment plan
4. The registry of completed experiments

The user wants me to generate new worst-tier predictions based on this context. The previous worst-tier predictions I read are from an earlier dream report, and now I need to produce updated ones.

Now I'm grounding my predictions in the actual experimental results from the registry - the fix approach achieved 0.82 on the full set versus 0.72 on the reference, the evaluation across models ranged from 0.75 to 0.85, the reference implementations showed consistent performance around 0.80-0.82, the depth filtering experiment yielded no meaningful signal, and the continuation variants performed between 0.73 and 0.78. I'll use these as anchors and then shift them toward worst-case outcomes that align with the reviewer concerns about scope and methodology. I'm realizing there's a key distinction here—the worst-tier predictions were generated before experiments ran, so they represent hypothetical worst-case scenarios rather than actual results. Now that many experiments are complete, I need to decide whether to use the real numbers or stick with the imagined worst-case interpretations that were predicted earlier.

The user wants me to generate a detailed report for the worst tier with rationales for each prediction, and since the experiments in the plan are marked as "planned," I should treat this as a hypothetical scenario. But the real insight is that worst-tier doesn't necessarily mean numerically worse results—it means reviewers interpret findings in the most pessimistic way possible, and I should ground this in actual data where available while still maintaining the worst-case interpretation lens.

Now I'm cross-referencing which experiments from the plan are actually completed in the registry versus which ones are still marked as planned, so I can decide which ones need hypothetical worst-case numbers and which ones I should base on actual results interpreted unfavorably. Writing YAML predictions... I need to anchor the worst-tier predictions to actual results where experiments have already run, then forecast plausible worst-case outcomes for the remaining ones—all filtered through a harsh reviewer's lens that questions the methodology and significance of the findings. Let me identify which experiments are complete versus pending and start building out the comprehensive YAML with all fifteen experiments. ored numbers and worst-tier interpretations. I'll be comprehensive.

Let me structure this properly: For LOGO binary F1, the paper uses 0.694 (8-gen LOGO). The actual 5-gen plan-002-eval gives LOGO avg macro 0.8037. With 8 generators (from exp_057), we get 0.7698 3-class and 0.6842 binary (wait that's 9-gen). The 8-gen baseline is 0.7698 3-class.

From the paper_framing headline metrics:
- Primary: LOGO binary F1 = 0.694 [0.688, 0.700]
- LOFO binary F1 = 0.686

So the actual LOGO binary F1 across 8 generators is 0.694. This is the key number reviewers will focus on.

Now I'm pulling together the full picture from the registry. I need to ground this in the actual experimental results: plan-001-fix shows the full model at 0.8204 with surface features at 0.7628, plan-002-eval establishes the LOGO baseline at 0.8037 with per-generator variation from 0.7519 to 0.8507, plan-003 reveals consistent negative drift across all reference conditions, plan-004-v2 confirms the ordering where negative results are worst and binary performance lags significantly behind depth variants, and plan-005 demonstrates that prompt type matters for drift patterns with continuous prompts at 0.7806 versus elaboration at 0.73.

Continuing with the remaining experiments: plan-010 shows baseline degradation starting at 5% perturbation with -0.046 drop and accelerating to -0.104 at 20%, plan-013 rules out length as a confound with a matched delta of +0.041, plan-014 reveals Qwen3-8B's LOGO performance at 0.6832 with clear scale degradation, plan-015-v2 achieves 0.798 with seven features and 0.7653 with average log probability, exp_057 shows the 9-generator LOGO at 0.751 for three-class but drops to 0.6661 for binary with Mistral performing worst at 0.6045, exp_058 confirms DDR causality with a 5.31× ratio, and exp_060 is still processing the 14B model results.

Now I'm reviewing the R analysis to confirm the underlying pattern, then checking the remaining plans: plan-006 still needs paraphrastic implementation, plan-007 references the paper's binary F1 of 0.830 at generator level, plan-008 is complete with domain-specific results across news, academic, and code, plan-009 shows five-class performance around 0.50, plan-011 isolates LD-Score at 0.7212, and plan-012's QLoRA experiments demonstrate strong three-class and binary performance. I'm now building the comprehensive worst-tier YAML configuration to ensure predictions align with or closely match the observed results.

For the worst-tier scenario, I need to set predictions that are somewhat pessimistic compared to actuals—representing a plausible low-end outcome rather than catastrophic failure—while framing the interpretation through a harsh reviewer lens. Since the actual LOGO binary F1 sits at 0.694 and the paper already anchors around this, I'm calibrating the worst-tier numbers to stay grounded in reality while emphasizing unfavorable interpretations.

The user's prompt is asking me to explain *why* results would fall at each tier level, not to invent entirely different numbers. So for completed experiments, I'll use actual results but interpret them critically; for planned experiments, I'll project pessimistic but plausible outcomes. Now I'll generate the full output with detailed rationales for each tier. worst tier predicts specific numerical outcomes AND explains why they occur in this scenario.

Given the worst tier narrative:
- Core framing fails
- Reviewers see scope as too narrow (base-model-only + temperature [0.5,0.9])
- 0.694 binary F1 margin too small above 0.5 random
- DDR seen as incremental
- Negative finding weaponized

The worst tier should predict results where:
- Numbers are at the pessimistic end of plausible ranges
- Some experiments reveal weaknesses
- Cumulative evidence doesn't strongly support claims

For experiments already done, I'll use numbers close to actuals (slightly pessimized) but with devastating interpretation. For undone experiments, I'll predict genuinely weak results.

Now I'm considering that there's a previous worst-tier dream from earlier, and the user wants an updated version reflecting the current experimental state. Since exp_062 on decoding strategy is now complete, showing that DDR remains stable across different decoding approaches with minimal drift, I need to frame this in the worst tier as merely a robustness check that doesn't strengthen the core claims. I'll generate the YAML with this updated context, treating the decoding-agnostic finding as incremental rather than validating. Now I'm working through the worst-tier grounding for each experiment. For the feature ablation test, the surface-only model captures 93% of the full model's performance, suggesting the DDR features might be largely redundant with what surface vocabulary already provides. The cross-generator evaluation shows a thin margin over baseline for the primary binary F1 metric, with high variance across generator families. And for the reference model comparison, performance drifts depending on which reference is used, indicating DDR isn't fully reference-agnostic as claimed.

Looking at downstream utility, all the ablated variants underperform the full model, but the depth variants show surprisingly little degradation—which could be weaponized as evidence that depth doesn't actually help. The prompt type analysis reveals continuation prompts (the least realistic setup) perform best, while elaboration and rewrite prompts drop off. I haven't finished the paraphrastic comparison yet, but I'm expecting it to show similar signal patterns that would undermine the claim that non-paraphrastic detection is uniquely valuable. And for the cross-model chains, the paper reports high binary F1 on a 5-generator subset, but that might just be detecting generator-level patterns rather than something more fundamental.

Now looking at the multi-domain results, performance is heavily domain-dependent—news and code do reasonably well, but academic is the worst performer, which is problematic since that's where contamination detection matters most. The finer-grained ordinal classification hits a ceiling at 3 classes with only 50% accuracy on 5-class prediction, suggesting the model isn't actually learning true depth ordering. And the human edit robustness test shows the approach is fragile across the board—even small edits degrade performance, and LLM rephrasing barely helps.

The LD-Score feature alone gets 0.72 F1, but adding six more features only pushes it to 0.798, indicating they're all measuring the same underlying signal. Meanwhile, the end-to-end QLoRA classifier dramatically outperforms everything at 0.89-0.91 for 3-class and 0.84-0.87 for binary, which undermines the whole feature engineering effort. On text length, I'm seeing conflicting signals—the delta shows +0.041 when controlling for length, but I need to reconcile that with the paper's reported 0.724 F1 for length-matched binary classification. Worst case here is that the margin over existing detectors is too narrow, and an ensemble approach combining multiple detectors would actually perform better.

Now I have enough grounding to write out the comprehensive YAML with actual numbers and worst-case reasoning. I need to be precise about which metric is which though—the paper's primary metric is LOGO binary F1 for the gen-1 vs gen-2+ comparison, so I should verify which registry values correspond to that versus the 3-class variant.

Looking at the paper's headline numbers as authoritative: LOGO binary F1 is 0.694, the 3-class version is 0.762, LOFO binary F1 is 0.686, and cross-model binary F1 reaches 0.830. I'll use these as my baseline and write the final output with precision.

For the worst-tier interpretation, I need to use numbers close to the actuals—maybe rounding pessimistically—and frame them in a way that emphasizes the concerns reviewers might raise about scope and methodology. The worst-tier framing isn't about inventing false numbers, but about how those real numbers could be interpreted unfavorably given the experimental design and limitations.

Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07ac5fee-1de4-4c68-a0e5-73ebee0324fa",
  "isSidechain": false,
  "requestId": "req_011CbGTHz5ypas3H5PU4HW6A",
  "type": "assistant",
  "uuid": "692c9b85-c22f-489b-bf9b-8c2d3e3baf79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RF2gvHyxzFbKGL4kyDyHQ1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25307,
      "cache_read_input_tokens": 38231,
      "output_tokens": 24157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 24157,
          "cache_read_input_tokens": 38231,
          "cache_creation_input_tokens": 25307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25307
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

_source line 19 · 2026-05-21T21:59:54.849Z_

Now I have the previous dream report and actual registry data. Let me cross-reference to produce worst-tier predictions grounded in actual results.

```yaml
tier: worst
narrative_guidance: >
  核心 framing 失效。Reviewer 共识：(1) base-model-only + temperature [0.5,0.9] 的 scope 在 2026 年没有实际意义——instruct/chat models
  主导生成内容，方法对 instruct models 信号反转 (ρ 从负变正)；(2) 0.694 binary F1 被认为不足以支撑 classification claim
  ——random baseline 0.5，margin 仅 0.194，per-gen 最差 Mistral-7B 只有 0.633；(3) DDR decoding-agnostic 被视为
  incremental robustness check 而非 contribution upgrade——"验证了方法在另一种 decoding 下也能产生同样 modest 的结果"；
  (4) Negative finding 被 weaponize 为 "so the method has no practical use?"——depth-aware curation ≡ random subsampling 直接
  质疑 task motivation；(5) 多位 reviewer 指出所有 drifting features 都在测量同一个 vocabulary impoverishment 现象，DDR 不是新发现
  而是 repackaging；(6) 写作修复不充分，presentation issues 加剧负面印象。
  Reframe 方向：从 'depth classification tool' 转向 'understanding distributional dynamics of recursive autoregressive generation'
  ——DDR 本身作为 analytical framework 是贡献，classifier 降级为 validation probe。Paper 重心从 Claim 1 转移到
  Claim 2 (DDR characterization) + decoding-agnostic 作为主线。Claim 3 negative finding 重新包装为
  'distributional shift ≠ quality degradation, challenging implicit assumptions in model collapse literature'。
  这个 reframe 放弃 practical utility 叙事，转向 understanding/characterization 贡献。

imagined_experiments:
  - name: feature_ablation_and_trend
    plan_id: plan_001
    description: >
      MVP 数据上三部分分析：(A) Feature ablation: reference-only vs surface-only vs full 7-feature, XGBoost 5-fold CV；
      (B) 每个 feature 的 depth trend (slope, R², Spearman ρ)；(C) Pythia-410M perplexity pre-validation for Claim 3。
    expected_results:
      full_macro_f1: 0.820
      surface_only_f1: 0.763
      reference_only_f1: 0.719
      surface_vs_full_gap_pp: 5.7
      ref_vs_surf_bootstrap_ci: "[0.706,0.733] vs [0.747,0.774]"
      mcnemar_full_vs_surface_p: 0.0
      mcnemar_full_vs_ref_p: 0.0
      h2_features: "entropy_mean, ttr, hapax_ratio"
      h1_features: "tail_decay, entropy_std, entropy_max, entropy_min"
      hapax_ratio_slope: -0.063
      hapax_ratio_r2: 0.88
      hapax_ratio_rho: -0.63
      ttr_slope: -0.041
      ttr_r2: 0.82
      ttr_rho: -0.61
      entropy_mean_slope: -0.089
      entropy_mean_r2: 0.79
      entropy_mean_rho: -0.60
      entropy_std_slope: -0.031
      entropy_std_r2: 0.41
      entropy_std_rho: -0.20
      tail_decay_slope: 0.003
      tail_decay_r2: 0.04
      tail_decay_rho: 0.04
      entropy_max_slope: 0.008
      entropy_max_r2: 0.07
      entropy_max_rho: 0.05
      median_ppl_by_depth: [13.50, 4.96, 3.00, 2.07, 1.72]
    result_rationale: >
      Surface-only (0.763) 达到 full (0.820) 的 93%——审稿人会 argue reference features 只是 marginal add-on，不构成独立
      contribution。虽然 McNemar p=0 确认显著性，但 worst-tier reviewer 会指出 5.7 pp 差距中 hapax_ratio 单个 surface 
      feature 就占据了 0.289 importance（plan-002-eval 实测），说明 reference features 被 surface features 的 vocabulary 
      impoverishment 信号 dominate。entropy_std 的 R²=0.41 处于 drifting/stationary 灰色地带，reviewer 会 argue DDR 
      不是 bimodal dichotomy 而是 continuous gradient——"the clean split between drifting and stationary is an artifact of 
      thresholding a continuous degradation spectrum." 所有 drifting features (hapax, TTR, entropy_mean) 沿同一方向单调递减，
      reviewer 会 argue 这就是 well-known vocabulary impoverishment 的多种测量维度，不是新现象。Perplexity 单调递减 
      (13.50→1.72) 只是说明 recursive generation 使 text 对 reference model 更 predictable——这是 trivial observation。
    tables:
      - caption: "Feature ablation: 5-fold CV macro F1 on MVP data (Pythia-2.8B, ~4600 records)"
        rows:
          - [Feature Set, Macro F1, 95% CI, "Δ vs Full"]
          - ["Full (7 features)", "0.820", "[0.807, 0.833]", "—"]
          - ["Surface-only (TTR + hapax)", "0.763", "[0.747, 0.774]", "−5.7 pp"]
          - ["Reference-only (5 entropy)", "0.719", "[0.706, 0.733]", "−10.1 pp"]
      - caption: "Per-feature depth trend (linear regression on depth 0–4)"
        rows:
          - [Feature, Category, Slope, R², Spearman ρ]
          - [hapax_ratio, Drifting, "−0.063", "0.88", "−0.63"]
          - [TTR, Drifting, "−0.041", "0.82", "−0.61"]
          - [entropy_mean, Drifting, "−0.089", "0.79", "−0.60"]
          - [entropy_std, Ambiguous, "−0.031", "0.41", "−0.20"]
          - [entropy_min, Stationary, "−0.018", "0.22", "−0.15"]
          - [tail_decay, Stationary, "+0.003", "0.04", "+0.04"]
          - [entropy_max, Stationary, "+0.008", "0.07", "+0.05"]
    figures_description:
      - >
        7-panel feature trend plot (mean ± std across depth 0–4)。Drifting features (hapax, TTR, entropy_mean) 单调递减但
        相邻 depth 的 error bars 大量重叠。entropy_std 占据灰色中间地带 (visible drift + high variance)。Reviewer 会
        circle entropy_std 并标注 "this feature breaks the clean dichotomy" 以及 annotate overlapping error bars 
        作为 "individual depth steps are not reliably distinguishable" 的 evidence。
    analysis: >
      在 worst 档下，ablation 的核心问题是 surface features 太强：93% signal retention 意味着 reference features 的 
      independent contribution minimal。Reviewer 会写："The proposed DDR framework adds substantial complexity (reference 
      model inference, 5 entropy features) for a 5.7 pp improvement over two simple vocabulary diversity metrics. The claim 
      of 'complementary signal' is technically supported but practically marginal." entropy_std 的 ambiguous status 
      (R²=0.41, ρ=-0.20) 破坏 DDR clean binary split 的叙事核心，reviewer 会 argue 这是 continuous degradation 
      而非 bimodal response。

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      扩展到 8 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, Llama-3.2-3B, Qwen3-8B, 
      Mistral-7B-v0.3) 的 LOGO 评估。~37K records。
    expected_results:
      total_records: 37500
      generators: 8
      families: 5
      logo_avg_3class_f1: 0.762
      logo_avg_3class_ci: [0.758, 0.766]
      logo_avg_binary_f1: 0.694
      logo_binary_ci: [0.688, 0.700]
      lofo_binary_f1: 0.686
      per_gen_binary_f1:
        pythia-1b: 0.724
        pythia-2.8b: 0.711
        qwen3-0.6b: 0.702
        qwen3-1.7b: 0.698
        olmo-2-1b: 0.679
        llama-3.2-3b: 0.688
        qwen3-8b: 0.647
        mistral-7b: 0.633
      per_gen_range_pp: 9.1
      fn_rate_of_binary_errors: 0.86
      worst_gen: mistral-7b-v0.3
      best_gen: pythia-1b
    result_rationale: >
      LOGO binary F1 = 0.694，margin over random baseline (0.50) 仅 0.194。在 balanced binary 任务中，这意味着 
      每 10 个 gen-2+ 样本中约 3 个被误判为 gen-1。Per-gen range 达 9.1 pp (Pythia-1B 0.724 vs Mistral-7B 0.633)，
      审稿人会 argue 方法 performance 高度依赖 generator identity，且最差的恰好是两个较大模型 (Mistral-7B 0.633, 
      Qwen3-8B 0.647)——暗示 scale 上升时方法失效。LOFO binary F1 = 0.686 比 LOGO 低 0.8 pp，说明跨 family 泛化
      存在但 margin 更薄。86% 的 binary errors 集中在 FN (gen-2+ 被判为 gen-1)——方法系统性地 under-detect deeper 
      generation，恰好是实际应用中最需要检出的样本。Reviewer 会写："The primary metric of 0.694 offers a margin of 
      less than 0.20 over random guessing. While statistically significant, this margin is far too thin for any 
      practical deployment, particularly given the 9 pp variance across generators and the systematic FN bias 
      toward deeper generations."
    tables:
      - caption: "Leave-one-generator-out (LOGO) binary F1 (gen-1 vs gen-2+, 8 generators)"
        rows:
          - [Held-out Generator, Family, Size, Binary F1, 95% CI]
          - [Pythia-1B, Pythia, 1.0B, "0.724", "[0.707, 0.741]"]
          - [Pythia-2.8B, Pythia, 2.8B, "0.711", "[0.693, 0.729]"]
          - [Qwen3-0.6B, Qwen, 0.6B, "0.702", "[0.682, 0.722]"]
          - [Qwen3-1.7B, Qwen, 1.7B, "0.698", "[0.678, 0.718]"]
          - [Llama-3.2-3B, Llama, 3.0B, "0.688", "[0.668, 0.708]"]
          - [OLMo-2-1B, OLMo, 1.5B, "0.679", "[0.658, 0.700]"]
          - [Qwen3-8B, Qwen, 8.0B, "0.647", "[0.624, 0.670]"]
          - [Mistral-7B-v0.3, Mistral, 7.0B, "0.633", "[0.609, 0.657]"]
          - ["**Average**", "—", "—", "**0.694**", "[0.688, 0.700]"]
      - caption: "Leave-one-family-out (LOFO) binary F1"
        rows:
          - [Held-out Family, Binary F1, "Δ vs LOGO"]
          - [Pythia, "0.668", "−2.6 pp"]
          - [Qwen, "0.672", "−2.2 pp"]
          - [OLMo, "0.714", "+2.0 pp"]
          - [Llama, "0.701", "+0.7 pp"]
          - [Mistral, "0.673", "−2.1 pp"]
          - ["**Average**", "**0.686**", "**−0.8 pp**"]
    figures_description:
      - >
        8-panel confusion matrix heatmap (one per held-out generator)。所有 panel 显示 gen-1 vs gen-2+ 是 dominant 
        confusion zone——gen-1 频繁被误判为 gen-2+ (FN rate 78–89%)。Mistral/Qwen3-8B panels 的 gen-1/gen-2+ 
        block 接近 uniform，视觉上几乎是 random guessing。Reviewer 会 annotate "these two panels show the method 
        fails on the larger models that matter most."
      - >
        Scatter plot: model size (log scale, x-axis) vs LOGO binary F1 (y-axis)。Clear negative trend。
        Regression line extrapolation 到 70B 处约 0.55——dangerously close to chance。
    analysis: >
      0.694 是论文 headline number，也是 worst 档审稿人的 primary attack target。两个结构性问题：(1) margin over 
      chance (0.194) 太薄——在 noisy real-world setting 下可能进一步缩小到 near-chance；(2) per-gen range 9.1 pp 
      说明 performance 高度 generator-dependent，最差的大模型们恰好是最重要的模型。审稿人会 write："At the models 
      that actually generate content at scale (7B+), the method achieves binary F1 of 0.633–0.647, which is 
      not meaningfully above random guessing for a balanced binary task."

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      测试 OLMo-2-1B 和 Qwen3-0.6B 作为替代 reference model (替代 Pythia-410M)。验证 DDR drift 是否在 
      非 Pythia reference 下持续存在。Claim 2 的关键 falsification test。
    expected_results:
      logo_f1_pythia_ref: 0.803
      logo_f1_olmo_ref: 0.807
      logo_f1_qwen_ref: 0.816
      entropy_mean_drift_pythia_range: [-1.19, -1.40]
      entropy_mean_drift_olmo_range: [-0.61, -0.91]
      entropy_mean_drift_qwen_range: [-0.96, -1.35]
      drift_direction_consistent: true
      shape_stationary_all_refs: true
      drift_magnitude_ratio_olmo_vs_pythia: 0.55
      qwen_ref_gives_best_logo: true
    result_rationale: >
      Falsification test 技术上通过了——drift direction 在所有 reference models 下一致 (所有 entropy_mean ρ < 0，
      所有 shape features |ρ| < 0.10)。但 drift magnitude 高度依赖 reference model：OLMo reference 的 entropy_mean 
      drift 仅为 Pythia 的 ~55% (-0.61 vs -1.19 on weakest generator)。LOGO F1 across references 差异小 
      (0.803–0.816)——但 worst-tier reviewer 会 reframe 这为："The classification performance is similar regardless 
      of reference model, but the underlying DDR characterization changes substantially. This means DDR magnitude 
      is as much a function of reference-generator mismatch as of recursive depth. The phenomenon the authors claim 
      to study is partially an artifact of their measurement instrument." 技术上不 kill Claim 2，但 interpretive 
      precision 被严重削弱。Qwen reference 给出最高 LOGO 说明 reference choice matters——在 worst 档下这被视为 
      "the method's performance depends on an engineering choice (reference model) that has no principled selection 
      criterion."
    tables:
      - caption: "Cross-reference-model DDR comparison"
        rows:
          - [Reference Model, Size, LOGO F1, "entropy_mean avg ρ", "hapax avg ρ", "tail_decay avg ρ", "Drift magnitude range"]
          - [Pythia-410M, 410M, "0.803", "−0.60", "−0.63", "+0.04", "[−1.19, −1.40]"]
          - [OLMo-2-1B, 1.5B, "0.807", "−0.50", "−0.58", "+0.07", "[−0.61, −0.91]"]
          - [Qwen3-0.6B, 0.6B, "0.816", "−0.56", "−0.61", "+0.05", "[−0.96, −1.35]"]
    figures_description:
      - >
        3-panel overlay plot: entropy_mean drift curves (depth 0–4) under each reference model。三条曲线都单调递减，
        但 OLMo reference curve 明显 shallower (slope ~55% of Pythia)。Reviewer annotation: "the claimed 'intrinsic' 
        property varies by 2× depending on measurement instrument."
    analysis: >
      这是 worst 档中最 subtle 的攻击向量。实验技术上通过了 falsification (drift direction consistent, shape 
      stationary)，但 magnitude dependence on reference model 给了审稿人一个 elegant reframe："DDR is not a 
      pure property of recursive generation but a joint function of generation and reference model. The authors' 
      claim of an 'intrinsic differential response' is overstated—it's a measurement-relative phenomenon." 
      这不会导致 reject 但会让 Claim 2 的 contribution 评估降半档。

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune OLMo-1B on depth-stratified data subsets。3 random seeds, bootstrap CIs。Compare depth-aware 
      filtering vs binary baselines vs random subsampling。Sample-count-matched comparison。
    expected_results:
      all_data_ppl_mean: 2.335
      all_data_ppl_std: 0.0003
      size_matched_ppl_mean: 2.367
      size_matched_ppl_std: 0.0003
      depth01_ppl_mean: 2.387
      depth01_ppl_std: 0.0004
      binary_filtered_ppl_mean: 2.389
      binary_filtered_ppl_std: 0.0006
      depth0_only_ppl_mean: 2.681
      depth0_only_ppl_std: 0.0006
      tost_p_2pct: 0.00011
      tost_p_1pct: 0.087
      ranking: "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)"
      seed_variance: "极小 (<0.002 within variant)"
      cohens_d_sizematched_vs_depth01: 0.42
    result_rationale: >
      Negative finding 极其 clean 且 robust：depth-aware filtering 与 random subsampling 在 ±2% margin 内 
      equivalence 被 TOST 确认 (p=1.1×10⁻⁴)。Cross-seed variance < 0.002 意味着这个 negative finding 是 
      highly reliable——不是 noisy null 而是 genuine equivalence。Ranking 显示更多数据 always better (all < 
      size_matched)，depth filtering 反而 slightly worse than random (2.387 vs 2.367)——意味着 depth-aware 
      curation 不仅没有帮助，还可能因为丢弃了 useful training signal 而 slightly hurt。
      
      审稿人在 worst 档下会 weaponize 这个结果："The authors' own Claim 3 establishes that generation depth 
      is informationally vacuous for the most obvious downstream application. If depth information provides 
      zero utility for data curation — indeed, depth-filtered data is slightly WORSE than random — then the 
      practical motivation for depth classification collapses entirely. The paper's pivot to 'diagnostic tool' 
      is an ad hoc rescue, not a designed contribution." TOST 在 ±1% margin 不显著 (p=0.087) 会被注意到但
      不 weaponize (论文已选 ±2%)。depth0_only 的高 perplexity (2.681) 只证明 human vs machine 有区别——
      这是 binary detection 已解决的问题，不支持 depth classification 的 incremental value。
    tables:
      - caption: "Downstream CLM perplexity by training data depth composition (3 seeds, OLMo-1B)"
        rows:
          - [Variant, Train Size, "PPL (mean ± std)", "Δ vs Size-matched", "TOST ±2% p"]
          - [All depths, "12,299", "2.335 ± 0.0003", "—", "—"]
          - [Size-matched random, "3,951", "2.367 ± 0.0003", "ref", "ref"]
          - ["Depth 0+1 only", "3,951", "2.387 ± 0.0004", "+0.020", "1.1×10⁻⁴"]
          - [Binary filtered, "3,951", "2.389 ± 0.0006", "+0.022", "8.7×10⁻⁵"]
          - ["Depth 0 only", "797", "2.681 ± 0.0006", "+0.314", "—"]
    figures_description:
      - >
        Bar chart with error bars: 5 variants 的 perplexity。中间三个 bar (size-matched, depth01, binary) 在 
        error bars 内 visually indistinguishable。depth0_only 作为 outlier 突出。Reviewer annotation: 
        "The only meaningful distinction is human vs machine — the binary detection problem. Depth adds nothing."
    analysis: >
      Negative finding 是 worst 档的 strategic vulnerability。论文 framing 为 "diagnostic not curative" 
      是诚实的，但 worst-tier reviewers 会 argue diagnostic value 未被证明——"where is the use case where 
      knowing depth matters?" 这与 Claim 1 的 practical motivation 形成 circular problem：如果 depth 没有
      downstream impact，为什么要分类 depth？论文需要 reframe 为 understanding contribution (DDR characterization) 
      而非 any form of utility，但这 reframe 在 worst 档下被视为 post-hoc rationalization。

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Compare continuation vs elaboration vs inspired_rewriting chains。1000 seeds × Pythia-2.8B × 3 prompt types。
    expected_results:
      cv_f1_continuation: 0.781
      cv_f1_elaboration: 0.730
      cv_f1_rewriting: 0.737
      lopto_avg_f1: 0.753
      lopto_held_out_cont: 0.762
      lopto_held_out_elab: 0.762
      lopto_held_out_rewrite: 0.734
      depth_retention_cont: 0.831
      depth_retention_elab: 0.986
      depth_retention_rewrite: 0.939
      drift_hapax_cont: -0.74
      drift_hapax_elab: -0.828
      drift_hapax_rewrite: -0.800
      drift_entropy_mean_cont: -0.557
      drift_entropy_mean_elab: -0.471
      drift_entropy_mean_rewrite: -0.477
      spearman_ttr_cont: -0.629
      spearman_ttr_elab: -0.666
      spearman_ttr_rewrite: -0.659
      cross_prompt_type_range_pp: 5.1
    result_rationale: >
      Continuation chains 优于 elaboration 5.1 pp (0.781 vs 0.730)，但 elaboration/rewriting 有更高 depth 
      retention (0.986/0.939 vs 0.831)。这是一个 paradox：elaboration 保留更多 chain completeness 但 depth 
      signal 更弱——说明 signal strength 与 chain fidelity inversely correlated。Worst-tier reviewer 会 argue 
      "the method works best on continuation chains — the simplest, least realistic generation paradigm. In more 
      naturalistic scenarios (elaboration, rewriting), where generators receive richer prompts and produce more 
      diverse output, the depth signal degrades by 5 pp." Feature drift inconsistency across prompt types 
      (entropy_mean 在 continuation 最强 -0.557 但 hapax 在 elaboration 最强 -0.828) 进一步 undermines DDR 
      作为 universal phenomenon 的叙事。LOPTO 显示 cross-prompt-type transfer 存在但不完美 (avg 0.753 vs 
      best within-type 0.781)——在实际应用中 prompt type 未知，reviewer 会 argue 应取 worst-case performance。
    tables:
      - caption: "Per-prompt-type classification and drift statistics (Pythia-2.8B)"
        rows:
          - [Prompt Type, CV F1, LOPTO F1, Depth Retention, "entropy_mean ρ", "hapax ρ", "TTR ρ"]
          - [Continuation, "0.781", "0.762", "0.831", "−0.557", "−0.740", "−0.629"]
          - [Elaboration, "0.730", "0.762", "0.986", "−0.471", "−0.828", "−0.666"]
          - [Inspired Rewriting, "0.737", "0.734", "0.939", "−0.477", "−0.800", "−0.659"]
    figures_description:
      - >
        3×7 heatmap: per-feature Spearman ρ across prompt types。Feature ranking 不 stable——entropy_mean 
        在 continuation 最强但 hapax_ratio 在 elaboration 最强。Reviewer: "if the feature dynamics vary by 
        prompt type, DDR is not a universal property but a prompt-conditional phenomenon."
    analysis: >
      Prompt-type dependence 在 worst 档下被叠加到 scope limitations 上。Reviewer list: "base models only, 
      temperature ∈ [0.5, 0.9], continuation chains preferred, Wikipedia seeds." 每增加一个条件性 qualifier，
      方法的 practical scope 进一步收窄。Feature-drift inconsistency (不同 feature 在不同 prompt type 下 
      rank 不同) 是对 DDR unified framework 的直接挑战。

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      构建 parallel paraphrasing chains 与 continuation chains 直接比较。测试 attractor convergence theory。
      1000 seeds × Pythia-2.8B × 2 chain types。
    expected_results:
      paraphrastic_cv_f1: 0.718
      continuation_cv_f1: 0.781
      paraphrastic_binary_f1: 0.661
      continuation_binary_f1: 0.694
      paraphrastic_drift_entropy_mean: -0.39
      paraphrastic_drift_hapax: -0.52
      paraphrastic_depth_retention: 0.992
      attractor_convergence_observed: true
      effective_classes_paraphrastic: 2
      delta_para_vs_cont_binary_pp: 3.3
      paraphrastic_gen2_vs_gen3_confusion: 0.62
    result_rationale: >
      Paraphrastic chains 显示 attractor convergence (depth retention 0.992 ≈ 1.0)，但 depth signal 弱于 
      non-paraphrastic (binary F1 0.661 vs 0.694, −3.3 pp)。差距只有 3.3 pp——worst-tier reviewer 会 argue 
      这太小了不足以证明 non-paraphrastic chains 有 qualitatively different depth dynamics。"Both chain types 
      show comparable (and modest) depth signal, suggesting the phenomenon is generic generation drift rather 
      than the differential depth response the authors claim." Paraphrastic chains 的 gen-2 vs gen-3 confusion 
      rate (0.62) 比 continuation (0.51) 更高，但 gen-0 vs gen-1 distinction 在两者中都 robust——说明 depth 
      signal 本质上是 binary (near-source vs deeper)，不是 true ordinal。Attractor convergence 被确认但 
      反而成为 negative evidence："if paraphrasting chains converge within ~3 iterations, and non-paraphrastic 
      chains show only 3.3 pp more depth signal, the 'novel' non-paraphrastic depth estimation adds negligible 
      value over studying convergence itself."
    tables:
      - caption: "Paraphrastic vs non-paraphrastic chain comparison (Pythia-2.8B)"
        rows:
          - [Chain Type, CV F1, Binary F1, Depth Retention, "entropy_mean ρ", Effective Classes]
          - ["Continuation (non-para)", "0.781", "0.694", "0.831", "−0.557", "3"]
          - [Paraphrastic, "0.718", "0.661", "0.992", "−0.390", "~2"]
          - ["Δ", "+6.3 pp", "+3.3 pp", "−0.161", "−0.167", "+1"]
    figures_description:
      - >
        Dual-panel: left shows feature drift curves for both chain types (both decline, paraphrastic shallower 
        but similar shape)。Right shows confusion matrices side-by-side。两者 visual similarity 强——reviewer 
        会 annotate "these look almost identical, undermining the 'qualitatively different' claim."
    analysis: >
      Paraphrastic comparison 在 worst 档下 backfires。预期 non-paraphrastic chains 会显示 dramatically 
      different behavior，但 3.3 pp binary delta 不够 dramatic。反而证明 depth signal 是 generic generation 
      phenomenon 而非 non-paraphrastic chains 的 unique property。论文需要 reframe 为 "depth signal exists 
      across chain types with moderate variation" 而非 "non-paraphrastic chains are special"。

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains (每个 depth step 使用不同 generator) vs single-model chains。5-gen subset, 
      generator-level LOGO。
    expected_results:
      cross_model_binary_f1: 0.764
      cross_model_3class_f1: 0.789
      single_model_binary_f1: 0.694
      single_model_3class_f1: 0.762
      cross_model_logo_binary_f1: 0.830
      delta_binary_pp: 7.0
      delta_logo_pp: 13.6
    result_rationale: >
      Cross-model chains binary F1 大幅高于 single-model (0.764 vs 0.694, +7 pp; LOGO 0.830 vs 0.694, +13.6 pp)。
      Worst-tier reviewer 会 reframe 这为 devastating counter-evidence："The +13.6 pp LOGO improvement on 
      cross-model chains reveals that the method is primarily detecting generator switching (different model 
      fingerprints at each depth step) rather than generation depth. In the single-model case — which is the 
      harder, more interesting, and more realistic scenario for same-generator iterative contamination — F1 drops 
      back to the modest 0.694." Cross-model improvement 被解释为 trivially explained by OOD detection of 
      different model fingerprints。"The authors' best result (0.830) is achieved on the easiest setting that 
      conflates depth with generator identity. The honest number for depth classification is 0.694, achieved 
      on single-model chains where the confound is absent." 这直接 undercuts the paper's strongest metric。
    tables:
      - caption: "Cross-model vs single-model chain classification"
        rows:
          - [Setting, Binary F1, 3-class F1, LOGO Binary F1]
          - [Single-model chains, "0.694", "0.762", "0.694"]
          - [Cross-model chains, "0.764", "0.789", "0.830"]
          - ["Δ", "+7.0 pp", "+2.7 pp", "+13.6 pp"]
    figures_description:
      - >
        Per-sample confidence scatter (single-model x, cross-model y)。Points cluster above diagonal——
        cross-model chains systematically easier。Reviewer: "this gap proves the method detects model 
        switching, not depth."
    analysis: >
      Cross-model improvement 是 double-edged sword。在 worst 档下，0.830 是 "cheating number" (conflates 
      depth with generator identity)，0.694 是 "honest number" (single-model, pure depth signal)。Paper 如果
      同时 report 两者，reviewer 会 focus on 差距作为方法不是真正测量 depth 的 evidence。如果只 report 0.694，
      reviewer 会问 "where are the cross-model results?" 无法赢。

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      扩展到 4 domains: Wikipedia, news (CNN/DailyMail), academic (S2ORC), code。500 seeds × 5 depths per domain。
      Cross-domain LOGO evaluation。
    expected_results:
      wikipedia_binary_f1: 0.815
      news_binary_f1: 0.712
      news_binary_ci: [0.690, 0.733]
      academic_binary_f1: 0.628
      academic_binary_ci: [0.603, 0.652]
      code_binary_f1: 0.687
      code_binary_ci: [0.664, 0.710]
      cross_domain_logo_binary_f1: 0.668
      max_gap_vs_wiki_pp: 18.7
      worst_domain: academic
      best_domain: wikipedia
    result_rationale: >
      Wikipedia (训练数据主 domain) 表现最好 (0.815)，academic 最差 (0.628)——gap 达 18.7 pp。在 t=0.7 下
      academic binary F1 进一步降到 ~0.628，接近 chance + 0.128 margin。Cross-domain LOGO (train on 3, test 
      on 1) 降到 0.668。Worst-tier reviewer 会 argue："The method's performance is catastrophically 
      domain-dependent. Scientific text — precisely the domain where AI contamination is a pressing concern 
      per the authors' own motivation — yields near-chance binary F1 of 0.628. This domain sensitivity, 
      combined with the base-model and temperature restrictions, makes the method's scope so narrow as to 
      be practically meaningless." Academic domain 的 weak signal 可能因为 scientific text 的 formulaic 
      structure 本身就限制了 vocabulary diversity variation，使 surface features 失效。Cross-domain LOGO 
      0.668 加上 cross-generator LOGO 0.694 = cumulative degradation when both unknowns (generator + domain) 
      are combined，reviewer 会 estimate real-world F1 < 0.65。
    tables:
      - caption: "Per-domain binary F1 (LOGO across generators)"
        rows:
          - [Domain, Seeds, Binary F1, 95% CI, "Δ vs Wiki"]
          - [Wikipedia, "500", "0.815", "[0.796, 0.834]", "—"]
          - [News, "500", "0.712", "[0.690, 0.733]", "−10.3 pp"]
          - [Code, "500", "0.687", "[0.664, 0.710]", "−12.8 pp"]
          - [Academic, "500", "0.628", "[0.603, 0.652]", "−18.7 pp"]
          - ["**Cross-domain LOGO**", "2000", "**0.668**", "[0.654, 0.682]", "—"]
    figures_description:
      - >
        Radar chart: 4 domains × 3 prompt types 的 binary F1。Shape highly asymmetric——Wiki+continuation 
        是 best corner, academic+elaboration 是 worst corner (F1 < 0.60)。视觉上方法只在 top-right quadrant 
        work。
    analysis: >
      Domain dependence 在 worst 档下与 generator/temperature/instruct/edit 依赖 叠加。Reviewer 列出 
      cumulative conditions："base models only, temperature ∈ [0.5, 0.9], continuation preferred, 
      Wikipedia domain, no human editing, single reference model." 这是 increasingly narrow niche。
      Academic domain failure 尤其 damaging 因为 paper motivation 中引用了 "7–17% of recent scientific 
      papers contain LLM text"——方法恰好在这个最相关 domain 上最弱。

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4)。测试 depth resolution 是否超过 3-class。
      Ordinal methods (CORAL, Frank-Hall) 比较。
    expected_results:
      five_class_macro_f1: 0.498
      five_class_ci: [0.480, 0.516]
      three_class_macro_f1: 0.762
      ordinal_coral_f1: 0.502
      ordinal_frank_hall_f1: 0.491
      gen0_recall: 0.92
      gen1_recall: 0.63
      gen2_recall: 0.41
      gen3_recall: 0.33
      gen4_recall: 0.29
      gen2_gen3_confusion_rate: 0.51
      gen3_gen4_confusion_rate: 0.48
      mean_absolute_depth_error: 0.89
    result_rationale: >
      5-class F1 = 0.498 (random baseline ~0.20, so margin = 0.298)。Ordinal methods 无改善 (CORAL 0.502, 
      Frank-Hall 0.491)——depth signal 不具备 ordinal structure beyond coarse binning。Gen-0 recall 高 
      (0.92) 但 gen-2/3/4 几乎无法区分 (recall 0.29–0.41, confusion 48–51%)。Gen-0 的高 recall 来自 
      seed-sharing (原始人类文本与训练 features 有 distributional gap)——这不是 depth classification 而是 
      human-vs-machine detection。
      
      Worst-tier reviewer 会 argue："5-class F1 of 0.498 confirms depth signal is essentially binary: the 
      method distinguishes 'source-adjacent' (gen-0/1) from 'deep' (gen-2+) but cannot resolve within either 
      group. The 3-class formulation is not a principled task definition but an artifact of signal weakness — 
      it happens to be the granularity at which the method achieves non-trivial performance. The gen-2/3/4 
      confusion block (48–51% confusion rate) shows the 'generation depth' framing overclaims — this is 
      at most a binary-plus-one classifier."
    tables:
      - caption: "Ordinal depth classification resolution"
        rows:
          - [Granularity, Method, Macro F1, "Ordinal vs XGBoost"]
          - [3-class, XGBoost, "0.762", "—"]
          - [5-class, XGBoost, "0.498", "—"]
          - [5-class, CORAL, "0.502", "+0.4 pp"]
          - [5-class, Frank-Hall, "0.491", "−0.7 pp"]
      - caption: "5-class per-depth recall"
        rows:
          - [Depth, Recall, Primary Confusion]
          - [gen-0, "0.92", "gen-1 (6%)"]
          - [gen-1, "0.63", "gen-2 (24%)"]
          - [gen-2, "0.41", "gen-1/gen-3 (26%/18%)"]
          - [gen-3, "0.33", "gen-2/gen-4 (31%/21%)"]
          - [gen-4, "0.29", "gen-3 (38%)"]
    figures_description:
      - >
        5×5 confusion matrix heatmap。Gen-0 bright diagonal (>0.90 recall)。Gen-1 moderate diagonal。
        Gen-2/3/4 形成 near-uniform block——视觉上是 "binary + noise" pattern。Reviewer 会 draw a 
        rectangle around gen-2/3/4 block 并标注 "effectively random within this block."
    analysis: >
      5-class collapse 是 worst 档对 task formulation novelty 最有力的 attack。如果 depth signal 本质上
      是 binary (+gen-1 略有区分)，那 "generation depth classification" 这个 task formulation 的 novelty 
      = 在 binary detection 上加了一个勉强可用的 third class。Ordinal methods 无改善进一步说明 depth 
      不是 ordinal quantity (continuous gradient)——而是 discrete jump from near-source to deep, 
      与 model collapse theory 的 gradual degradation 预测不一致。

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Robustness to simulated human edits: (A) random word replacement 5/10/20%, 
      (B) LLM-simulated light rephrasing (Qwen3-1.7B)。
    expected_results:
      baseline_binary_f1: 0.695
      random_5pct_f1: 0.650
      random_10pct_f1: 0.614
      random_20pct_f1: 0.591
      llm_rephrase_binary_f1: 0.647
      llm_rephrase_multiclass_f1: 0.667
      llm_rephrase_edit_distance: 0.507
      degradation_5pct_pp: -4.5
      degradation_10pct_pp: -8.1
      degradation_20pct_pp: -10.4
      degradation_llm_pp: -4.5
    result_rationale: >
      5% random replacement 造成 4.5 pp drop (0.695 → 0.650)。LLM rephrasing (edit distance 0.507, 
      avg 1.69 sentences replaced) 造成相同量级 drop (−4.5 pp → 0.647)。20% replacement 降到 0.591。
      
      Worst-tier reviewer 会 argue："In practice, AI-generated text is almost always edited before 
      publication — students edit LLM essays, writers revise LLM drafts, automated pipelines post-process 
      outputs. The method loses 4.5 pp F1 from light editing (50% edit distance ratio, ~1.7 sentences 
      changed), pushing the already-modest 0.695 baseline to 0.647. At this level, the method correctly 
      classifies depth for barely 65% of edited text — not actionable for any real-world application."
      
      Degradation is near-linear with perturbation intensity, suggesting the depth signal resides in 
      surface-level distributional properties easily disrupted by any text modification. This confirms 
      the "vocabulary impoverishment repackaging" critique—if the signal were capturing deeper structural 
      properties of recursive generation, it would be more robust to superficial edits.
    tables:
      - caption: "Robustness to simulated human edits"
        rows:
          - [Perturbation, Binary F1, "Δ vs Baseline", Edit Distance]
          - ["None (baseline)", "0.695", "—", "0.0"]
          - ["Random 5%", "0.650", "−4.5 pp", "~0.05"]
          - ["Random 10%", "0.614", "−8.1 pp", "~0.10"]
          - ["Random 20%", "0.591", "−10.4 pp", "~0.20"]
          - ["LLM rephrase", "0.647", "−4.5 pp", "0.507"]
    figures_description:
      - >
        Line chart: binary F1 vs perturbation intensity。Near-linear degradation。LLM rephrase point 
        sits between 5% and 10% random。Shaded 95% CI widens at higher perturbation。Reviewer: 
        "the linear degradation curve suggests the signal is purely surface-level and has no structural 
        robustness."
    analysis: >
      Robustness 实验在 worst 档下是 lose-lose。Fragile result confirms depth signal 是 surface-level 
      且 easily disrupted。Combined with instruct degradation、temperature sensitivity、domain dependence，
      the cumulative fragility makes a devastating picture for any practical deployment argument。

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      添加 LD-Score (character-distribution signature) 作为第 8 个 feature。测试 character-level 信号
      是否与 word/entropy features 互补。
    expected_results:
      seven_feature_logo_f1: 0.798
      eight_feature_with_ld_f1: 0.802
      ld_score_alone_logo_f1: 0.721
      ld_score_alone_spearman: 0.794
      marginal_improvement_pp: 0.4
      feature_importance_ld: 0.022
      ld_score_cv_corrected_f1: 0.793
    result_rationale: >
      LD-Score 单独 LOGO F1 = 0.721 (高于 FastDetectGPT 0.627 和 Binoculars 0.579，但低于 Avg-LogProb 
      0.765 和 7-feature 0.798)。加入后 marginal improvement 仅 0.4 pp (0.798 → 0.802)，feature 
      importance 排最后 (0.022)。LD-Score 的 high Spearman (0.794) 说明它有 ordinal depth signal，
      但被 existing features 高度 subsume。
      
      Worst-tier reviewer 不会直接 attack 这个实验 (minor addition)，但会用它 reinforce vocabulary 
      impoverishment narrative："Adding a character-level feature provides negligible improvement (0.4 pp), 
      confirming that character, word, and NLL features all measure the same underlying phenomenon — 
      text simplification under recursive generation. The claimed 'differential depth response' across 
      feature types is an artifact of measuring the same signal at different linguistic levels."
    tables:
      - caption: "LD-Score feature addition (3-class LOGO)"
        rows:
          - [Feature Set, LOGO F1, "Δ"]
          - ["7 features (baseline)", "0.798", "—"]
          - ["7 + LD-Score", "0.802", "+0.4 pp"]
          - ["LD-Score only", "0.721", "—"]
    figures_description:
      - >
        Feature importance bar chart (8 features)。LD-Score 是最短 bar，视觉上 negligible vs 
        hapax_ratio (0.269) 和 entropy_mean (0.164)。
    analysis: >
      Minor experiment, minor result。在 worst 档下主要作为 "all signals converge" narrative 的 
      supporting evidence。不是 primary attack vector。

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned end-to-end depth classifier (OLMo-1B-Instruct, Qwen3-1.7B-Instruct, 
      及其 base model variants)。Within-distribution CV 和 cross-generator transfer。
    expected_results:
      qlora_olmo_instruct_3class: 0.888
      qlora_olmo_instruct_3class_std: 0.007
      qlora_olmo_instruct_binary: 0.836
      qlora_olmo_instruct_binary_std: 0.010
      qlora_qwen_instruct_3class: 0.907
      qlora_qwen_instruct_binary: 0.867
      qlora_olmo_base_3class: 0.859
      qlora_olmo_base_binary: 0.793
      qlora_qwen_base_3class: 0.904
      qlora_qwen_base_binary: 0.860
      seven_feature_3class: 0.762
      seven_feature_binary: 0.694
      delta_3class_pp_olmo: 12.6
      delta_binary_pp_olmo: 14.2
      qlora_5class_f1: 0.575
      qlora_inference_cost_ratio: 47.0
    result_rationale: >
      QLoRA within-distribution 大幅碾压 7-feature：OLMo-Instruct 3-class 0.888 vs 0.762 (+12.6 pp)，
      binary 0.836 vs 0.694 (+14.2 pp)。Qwen-Instruct 更高 (3-class 0.907, binary 0.867)。Even base 
      models QLoRA (3-class 0.859/0.904) 远超 7-feature。5-class F1 = 0.575 也远超 7-feature 的 ~0.50。
      
      Worst-tier reviewer 会 cherry-pick within-distribution numbers："A straightforward QLoRA classifier 
      achieves 0.867 binary F1 (Qwen-Instruct), dwarfing the proposed method's 0.694 by 17.3 pp. Even 
      with the base model alone, QLoRA achieves 0.860 binary — a 16.6 pp advantage. The 7-feature 
      ensemble captures less than half the depth signal available in the text. The authors' efficiency 
      argument (47× cost ratio) is unconvincing: the QLoRA classifier runs on the same-sized model 
      already needed as a reference, and the 17 pp gap is too large to justify on cost grounds."
      
      论文的 rebuttal point 是 LOGO cross-generator transfer——QLoRA within-distribution 的 advantage 
      partly comes from overfitting to generator-specific patterns。但 worst-tier reviewer 已经 scored 
      low before considering this nuance。
    tables:
      - caption: "End-to-end (QLoRA) vs 7-feature ensemble"
        rows:
          - [Method, Model, "3-class F1 (±std)", "Binary F1 (±std)", Cost Ratio]
          - [7-feature XGBoost, "—", "0.762", "0.694", "1×"]
          - [QLoRA, OLMo-Instruct, "0.888 ± 0.007", "0.836 ± 0.010", "47×"]
          - [QLoRA, Qwen-Instruct, "0.907 ± 0.008", "0.867 ± 0.014", "47×"]
          - [QLoRA, OLMo-Base, "0.859 ± 0.004", "0.793 ± 0.010", "47×"]
          - [QLoRA, Qwen-Base, "0.904 ± 0.009", "0.860 ± 0.012", "47×"]
    figures_description:
      - >
        Grouped bar chart: within-distribution (left cluster) vs LOGO (right cluster, if available)。
        Within-distribution 差距 visually dramatic (all QLoRA bars tower over 7-feature)。Reviewer 会 
        focus on left cluster 并 ignore right cluster caveat。
    analysis: >
      End-to-end comparison 在 worst 档下 devastating。14-17 pp gap 说明 7-feature ensemble 遗漏了 
      substantial depth signal。论文的 positioning 是 efficiency vs absolute performance tradeoff，但 
      worst-tier reviewer 不买账："if the features miss this much signal, the contribution is not a 
      competitive method but an incomplete characterization." QLoRA instruct > base 也 undermine 
      "instruct kills depth signal" narrative——within-distribution instruct QLoRA actually works fine, 
      说明 instruct 限制的是 the specific features chosen, not the depth signal itself。

  - name: text_length_control
    plan_id: plan_013
    description: >
      Address text length confound: (A) length-depth correlation analysis, (B) length-normalized features, 
      (C) length-matched subsampling re-evaluation。
    expected_results:
      spearman_length_depth: 0.12
      spearman_p: 0.001
      length_depth_correlation: "weak (|ρ|<0.14)"
      length_matched_binary_f1: 0.724
      unmatched_binary_f1: 0.770
      delta_pp: -4.6
      normalized_ttr_trend_preserved: true
      normalized_hapax_trend_preserved: true
      normalized_rho_stronger: true
      length_is_primary_confound: false
      short_text_dropout_bias: true
      length_matched_f1_vs_logo_headline: "+3.0 pp above 0.694 LOGO"
    result_rationale: >
      Length-depth correlation weak (ρ=0.12) 但 statistically significant (p=0.001)。Length-matched 
      binary F1 降 4.6 pp (0.770 → 0.724)——意味着 ~6% of signal 来自 text length。Normalized 
      features 的 depth trend 保持说明 depth signal 不完全是 length artifact，但 worst-tier reviewer 
      会 magnify 4.6 pp drop："After controlling for the most basic confound — text length — the method 
      loses 4.6 pp. How many other confounds (topic, style, vocabulary register) remain uncontrolled? 
      The 0.694 LOGO F1 may be further inflated by confounds the authors haven't tested."
      
      Short-text dropout bias 增加了 confound complexity：deeper depths 有更多 short text 被 pipeline 
      过滤掉，导致 surviving deeper text 是 systematically longer/more complete——这是 selection bias，
      方法可能部分检测的是 "which texts survived the pipeline filter" 而非 true depth signal。
    tables:
      - caption: "Length control analysis"
        rows:
          - [Condition, Binary F1, "Δ vs Unmatched"]
          - ["Unmatched (original)", "0.770", "—"]
          - ["Length-normalized features", "0.748", "−2.2 pp"]
          - ["Length-matched subsample", "0.724", "−4.6 pp"]
    figures_description:
      - >
        Left: text length distribution violin plots by depth (subtle shift)。Right: before/after 
        length matching confusion matrix comparison。Reviewer 会 note 4.6 pp drop 并 question what 
        other confounds exist。
    analysis: >
      Length confound 不 kill paper 但 erode credibility。4.6 pp 降幅在 worst 档下被 generalize 为 
      "confound-sensitive method"——reviewer 会 question every reported number 是否被 uncontrolled 
      confounds inflate。这使 0.694 headline number 的 credibility 进一步下降。

  - name: large_scale_generator
    plan_id: plan_014
    description: >
      添加 Qwen3-8B-Base 测试 7B+ scale 的 depth signal。1000 seeds × 5 depths。与现有 6-gen 
      LOGO 集成。
    expected_results:
      qwen3_8b_records: 4497
      qwen3_8b_unique_seeds: 995
      qwen3_8b_depth_dist: {"0": 995, "1": 979, "2": 937, "3": 831, "4": 755}
      logo_6gen_avg_f1: 0.789
      qwen3_8b_logo_binary_f1: 0.647
      qwen3_8b_logo_3class_f1: 0.683
      qwen3_8b_within_cv_f1: 0.711
      delta_vs_avg_pp: -10.6
      hapax_rho_8b: -0.558
      ttr_rho_8b: -0.542
      entropy_mean_rho_8b: -0.475
      feature_margin_compression_vs_avg: 0.72
      ddr_pattern_preserved: true
    result_rationale: >
      Qwen3-8B LOGO binary F1 = 0.647——比 6-gen average 低 ~10.6 pp。Feature drift magnitudes 全面压缩 
      (hapax ρ −0.558 vs avg −0.647, compression ~0.72)。DDR pattern 仍然 preserved (drifting > stationary 
      分离 maintained)，但 magnitudes 显著 weakened。Within-CV F1 = 0.711 说明 8B 自身 depth signal 存在，
      但 cross-generator transfer 弱 (LOGO 0.647)——smaller models 的 feature distribution 不 transfer well。
      
      Worst-tier reviewer 会 extrapolate："At 8B, the method shows substantial degradation (−10.6 pp vs 
      average, LOGO binary 0.647). This model is still far from frontier: GPT-4 (>100B), Claude 3 (unknown), 
      Llama-3-70B — the models generating the vast majority of AI text in practice — are 10–100× larger. 
      The observed linear degradation in log-scale model size (from 0.6B to 8B) projects to near-chance 
      performance at frontier scales, rendering the method irrelevant for the contamination problem it claims 
      to address." 这是 worst 档中 most damaging extrapolation——审稿人不需要实验数据就可以 argue。
      
      Depth distribution (gen-4 only 755/995 = 75.9% retention) 也说明 8B models 更容易产生 degenerate 
      output at depth (higher skip rate)——selection bias adds to confound concerns。
    tables:
      - caption: "Scale effect: Qwen3-8B vs smaller generators"
        rows:
          - [Generator, Size, LOGO Binary F1, "hapax ρ", "entropy_mean ρ", "Feature compression"]
          - [Pythia-1B, 1.0B, "0.724", "−0.65", "−0.60", "—"]
          - [Qwen3-1.7B, 1.7B, "0.698", "−0.63", "−0.60", "—"]
          - [Pythia-2.8B, 2.8B, "0.711", "−0.63", "−0.60", "—"]
          - [Qwen3-8B, 8.0B, "0.647", "−0.56", "−0.48", "0.72×"]
          - ["**Trend**", "—", "**Declining**", "**Compressing**", "**Compressing**", "—"]
    figures_description:
      - >
        Log-scale x-axis (model size) vs binary F1 y-axis，with feature drift magnitude as bubble size。
        Clear downward trend from 1B to 8B。Dotted extrapolation line to 70B crosses 0.55 (near-chance) 
        at ~30B。Visually devastating for any scale-generalization argument。
    analysis: >
      Scale degradation 是 worst 档的 structural problem。论文诚实 report 这是 scope boundary，但 
      reviewer reframe："the scope boundary excludes all models that generate text at scale." 加上 
      instruct degradation (OLMo-Instruct LOGO 0.338)，方法的 applicable scope = base models ≤ 8B 
      at moderate temperature in Wikipedia-like domains without human editing。这个 niche 在 2026 年
      没有 practical relevance。

  - name: ordinal_baseline_comparison
    plan_id: plan_015
    description: >
      Compare existing detector continuous scores (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb) 
      作为 ordinal depth predictors vs 7-feature ensemble。Multi-detector ensemble 比较。
    expected_results:
      seven_feature_logo_f1: 0.798
      seven_feature_ci: [0.786, 0.799]
      avg_logprob_logo_f1: 0.765
      avg_logprob_ci: [0.616, 0.820]
      ld_score_logo_f1: 0.721
      ld_score_ci: [0.588, 0.770]
      fastdetectgpt_logo_f1: 0.627
      fastdetectgpt_ci: [0.511, 0.762]
      binoculars_logo_f1: 0.579
      binoculars_ci: [0.405, 0.664]
      bootstrap_7feat_vs_avglogprob_delta: 0.033
      bootstrap_7feat_vs_avglogprob_p: 0.0
      multi_detector_ensemble_f1: 0.708
      multi_det_4det_plus_surface_3class: 0.795
      multi_det_binary: 0.708
      seven_feature_binary: 0.705
      multi_det_vs_7feat_binary_pp: 0.3
      multi_det_inference_cost: "2.4×"
    result_rationale: >
      7-feature LOGO F1 = 0.798 (3-class) 显著优于最佳 single detector Avg-LogProb (0.765, δ=3.3 pp, 
      p < 0.001)。但 single detector CIs 极宽 (Avg-LogProb CI [0.616, 0.820] 跨越 7-feature point 
      estimate)——说明 per-generator variance 极高。Multi-detector ensemble (4-det + surface) 达到 
      3-class 0.795 和 binary 0.708 vs 7-feature binary 0.705——仅 0.3 pp 差距。
      
      Worst-tier reviewer 会 argue："The 7-feature ensemble achieves 3.3 pp over Avg-LogProb, but this 
      single number (average log probability) requires only basic LM inference — no feature engineering, 
      no reference model selection, no DDR framework. The tiny margin and overlapping confidence intervals 
      suggest the elaborate DDR characterization provides minimal practical benefit over a trivial baseline. 
      Moreover, a multi-detector ensemble matches the 7-feature binary F1 within 0.3 pp. The contribution 
      reduces to: 'a slightly different way to achieve what existing tools already achieve, with a novel 
      but unvalidated interpretive framework (DDR).'"
      
      Bootstrap p < 0.001 for 7-feat vs Avg-LogProb 在 3-class setting 是 significant。但 binary 
      setting 差距 near-zero (0.705 vs 0.708)——primary metric 下 7-feature 反而略低于 multi-detector。
    tables:
      - caption: "Ordinal depth classification: 7-feature vs existing detector baselines (LOGO)"
        rows:
          - [Method, "3-class F1", "95% CI", "Binary F1", "Δ vs 7-feat 3-class", "Bootstrap p"]
          - ["**7-feature ensemble**", "**0.798**", "[0.786, 0.799]", "**0.705**", "—", "—"]
          - ["Avg-LogProb", "0.765", "[0.616, 0.820]", "0.695", "−3.3 pp", "<0.001"]
          - ["LD-Score", "0.721", "[0.588, 0.770]", "0.672", "−7.7 pp", "<0.001"]
          - ["FastDetectGPT", "0.627", "[0.511, 0.762]", "0.601", "−17.1 pp", "<0.001"]
          - ["Binoculars", "0.579", "[0.405, 0.664]", "0.558", "−21.9 pp", "<0.001"]
          - ["4-det + surface", "0.795", "[0.781, 0.808]", "0.708", "−0.3 pp", "0.72"]
    figures_description:
      - >
        Forest plot: each method's LOGO F1 with 95% CI。CIs overlap heavily between 7-feature, 
        Avg-LogProb, 和 multi-detector ensemble。7-feature 在 pack 中而非 clearly superior。
        Multi-detector ensemble CI overlaps entirely with 7-feature。Reviewer: "the proposed method 
        is statistically indistinguishable from a simple ensemble of existing tools."
    analysis: >
      Baseline comparison 在 worst 档下是 most dangerous experiment。在 binary metric (primary) 下，
      7-feature (0.705) 和 multi-det (0.708) 几乎无差——reviewer 会 conclude 7-feature 的 contribution 
      不足以 justify publication。3-class 下 7-feature 略优 (0.798 vs 0.795)，但差距 near-zero。
      论文 contribution 被 reduce 为："a modestly different feature set that performs comparably to 
      existing detector ensembles, with an interpretive framework (DDR) that may or may not correspond 
      to a real phenomenon." 这是 worst 档下 paper's reason to exist 被直接 challenged 的实验。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "692c9b85-c22f-489b-bf9b-8c2d3e3baf79",
  "isSidechain": false,
  "requestId": "req_011CbGTHz5ypas3H5PU4HW6A",
  "type": "assistant",
  "uuid": "9c990b61-7df0-44b7-b160-1516385aaf94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RF2gvHyxzFbKGL4kyDyHQ1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25307,
      "cache_read_input_tokens": 38231,
      "output_tokens": 24157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 24157,
          "cache_read_input_tokens": 38231,
          "cache_creation_input_tokens": 25307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25307
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Reviewer 认为 scope 太窄、F1 太低、task motivation 不足，Findings 被拒，需 reframe 后投 fallback venue 核心假设：['多位 reviewer 认为 base-model-only + temperature [0.5,0.9] 的 scop…",
  "leafUuid": "9c990b61-7df0-44b7-b160-1516385aaf94",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe depth-fingerprinting to distributional-dynamics characterization",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Reviewer 认为 scope 太窄、F1 太低、task motivation 不足，Findings 被拒，需 reframe 后投 fallback venue 核心假设：['多位 reviewer 认为 base-model-only + temperature [0.5,0.9] 的 scop…",
  "leafUuid": "9c990b61-7df0-44b7-b160-1516385aaf94",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe depth-fingerprinting to distributional-dynamics characterization",
  "sessionId": "3ea233fc-cde1-44e5-86de-1d80535bd3d7"
}
```

---
