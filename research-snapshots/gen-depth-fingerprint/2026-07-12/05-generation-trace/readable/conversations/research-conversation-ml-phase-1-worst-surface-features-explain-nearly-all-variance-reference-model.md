# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Surface features explain nearly all variance; reference-model features add 

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/72ba5d00-5964-499d-ab17-ffb22355be24.jsonl`
- **Structured JSON:** [`c35199ba9027072ce17d.json`](../../sessions/c3/c35199ba9027072ce17d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T18:25:10.222Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T18:25:10.222Z",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Surface features explain nearly all variance; reference-model features add negligible signal; cross-generator generalization is weak; 'distributional fingerprint' framing collapses\n核心假设：['Claim 2 falsified: surface-only ≈ full, ref-only features at or near chance; hapax_ratio + TTR are doing all the work', 'Depth signal is primarily vocabulary impoverishment, not distributional drift under reference model', 'Cross-generator generalization is poor — surface statistics are generator-specific, not universal', 'gen-1 vs gen-2+ boundary is near chance; only gen-0 vs synthetic is reliably detected', 'Downstream utility is not significantly better than binary baselines', 'H₁ (convergence) may hold: non-paraphrastic chains also stabilize quickly, limiting depth signal to ~2 classes']\n关键指标范围：{'plan_001_ref_only_macro_f1': [0.4, 0.55], 'plan_001_surface_only_macro_f1': [0.75, 0.84], 'plan_001_full_macro_f1': [0.76, 0.85], 'plan_001_ref_minus_surface_delta': [-0.35, -0.15], 'plan_002_cross_gen_leave_one_out_macro_f1': [0.42, 0.58], 'plan_002_cross_gen_gen1_f1': [0.35, 0.5], 'plan_002_cross_gen_gen2plus_f1': [0.38, 0.52], 'plan_003_cross_family_ref_macro_f1': [0.4, 0.55], 'plan_004_depth_quality_spearman_rho': [0.1, 0.3], 'plan_004_depth_filter_vs_binary_perf_gap_pct': [-1.0, 0.5]}\n叙事方向：Abandon \"distributional fingerprint\" as primary contribution. Reframe paper around the empirical characterization of recursive generation dynamics itself: \"We tested H₁ vs H₂ and found evidence that non-paraphrastic chains also converge (or that drift manifests primarily as vocabulary impoverishment rather than deeper distributional shift).\" This is a negative-but-informative result that extends the attractor cycle theory (ACL 2025) to non-paraphrastic settings. New angle: \"Vocabulary impoverishment as a universal fingerprint of synthetic text depth\" — reposition surface features not as a shortcut but as the primary mechanism, with theoretical explanation of why reference-model features fail (generation entropy converges even if vocabulary depletes). The paper becomes an empirical study characterizing the limits of depth estimation, contributing boundary conditions for future work. Supplement with analysis of *why* reference features fail (convergence speed analysis, per-depth feature trajectory plots). Still targets AAAI as an empirical science contribution with clear hypothesis-testing framing.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nvenue: AAAI 2027\nfocus: Key uncertainties: (1) whether reference-model features carry independent signal vs surface vocabulary stats (Claim 2 ablation), (2) cross-generator generalization with leave-one-out, (3) gen-1 vs gen-2+ boundary discrimination strength. MVP showed macro-F1=0.84 single-generator but hapax_ratio dominated feature importance.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains (continuation, elaboration) operate in an unbounded semantic state space — unlike paraphrasing chains that converge to attractor cycles (ACL 2025). This means distributional drift accumulates monotonically with generation depth, leaving detectable \"fingerprints\" in token-level statistics under a reference model. These fingerprints enable ordinal depth estimation, unlocking risk-stratified data curation beyond binary real/synthetic filtering.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Distributional Fingerprint Independence**: Reference-model-derived features (entropy statistics, tail-distribution decay) carry independent depth signal beyond surface vocabulary statistics (TTR, hapax ratio). Ablation: reference-only features achieve significantly higher F1 than surface-only features, or at minimum provide significant complementary signal.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation as an empirical phenomenon with practical implications for data governance. We formalize two competing hypotheses — H₁ (convergence: recursive generation tends toward a distributional fixed point even for non-paraphrastic chains) vs H₂ (divergence: non-paraphrastic chains accumulate monotonic drift) — and test them via depth-dependent distributional features under a reference model. Regardless of which hypothesis prevails, the characterization itself provides actionable insight: if H₂, depth estimation enables risk-stratified curation; if H₁, we establish the theoretical ceiling for depth-based approaches.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: If surface features (TTR, hapax) alone match full-feature performance, the \"distributional fingerprint\" framing is overclaimed. → Ablation experiment (Claim 2) directly addresses this.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n## Venue Fit\n- AAAI 2027: Strong fit — data governance + ML methodology. The H₁/H₂ hypothesis-testing framing positions it as empirical science, not just a classifier paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation\n  description: 'Ablation: (A) reference-model-only features (entropy_mean/std/min/max\n    + tail_decay) vs (B) surface-only features (TTR + hapax_ratio) vs (C) full feature\n    set. Tests whether distributional fingerprint carries independent signal beyond\n    vocabulary impoverishment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: Uses existing MVP data. No new generation needed. Critical for Claim 2.\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B,\n    Pythia-1B). Leave-one-generator-out CV to test cross-generator generalization.\n    1000 seeds × 5 generators × 5 depths = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: Only proceed if plan_001 confirms reference features have independent value.\n  status: planned\n- id: plan_003\n  claim: 1\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B) for feature\n    extraction. Addresses RC2 — verifies signal isn''t architecture-specific artifact.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune a small LM (Pythia-410M or OLMo-1B) on depth-stratified\n    data subsets. Measure perplexity degradation on held-out test set as function\n    of training data depth. Compare depth-aware filtering vs binary baselines (FastDetectGPT,\n    LD-Score threshold).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T18:25:10.225Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T18:25:10.225Z",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T18:25:10.241Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Surface features explain nearly all variance; reference-model features add negligible signal; cross-generator generalization is weak; 'distributional fingerprint' framing collapses
核心假设：['Claim 2 falsified: surface-only ≈ full, ref-only features at or near chance; hapax_ratio + TTR are doing all the work', 'Depth signal is primarily vocabulary impoverishment, not distributional drift under reference model', 'Cross-generator generalization is poor — surface statistics are generator-specific, not universal', 'gen-1 vs gen-2+ boundary is near chance; only gen-0 vs synthetic is reliably detected', 'Downstream utility is not significantly better than binary baselines', 'H₁ (convergence) may hold: non-paraphrastic chains also stabilize quickly, limiting depth signal to ~2 classes']
关键指标范围：{'plan_001_ref_only_macro_f1': [0.4, 0.55], 'plan_001_surface_only_macro_f1': [0.75, 0.84], 'plan_001_full_macro_f1': [0.76, 0.85], 'plan_001_ref_minus_surface_delta': [-0.35, -0.15], 'plan_002_cross_gen_leave_one_out_macro_f1': [0.42, 0.58], 'plan_002_cross_gen_gen1_f1': [0.35, 0.5], 'plan_002_cross_gen_gen2plus_f1': [0.38, 0.52], 'plan_003_cross_family_ref_macro_f1': [0.4, 0.55], 'plan_004_depth_quality_spearman_rho': [0.1, 0.3], 'plan_004_depth_filter_vs_binary_perf_gap_pct': [-1.0, 0.5]}
叙事方向：Abandon "distributional fingerprint" as primary contribution. Reframe paper around the empirical characterization of recursive generation dynamics itself: "We tested H₁ vs H₂ and found evidence that non-paraphrastic chains also converge (or that drift manifests primarily as vocabulary impoverishment rather than deeper distributional shift)." This is a negative-but-informative result that extends the attractor cycle theory (ACL 2025) to non-paraphrastic settings. New angle: "Vocabulary impoverishment as a universal fingerprint of synthetic text depth" — reposition surface features not as a shortcut but as the primary mechanism, with theoretical explanation of why reference-model features fail (generation entropy converges even if vocabulary depletes). The paper becomes an empirical study characterizing the limits of depth estimation, contributing boundary conditions for future work. Supplement with analysis of *why* reference features fail (convergence speed analysis, per-depth feature trajectory plots). Still targets AAAI as an empirical science contribution with clear hypothesis-testing framing.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-fingerprint
venue: AAAI 2027
focus: Key uncertainties: (1) whether reference-model features carry independent signal vs surface vocabulary stats (Claim 2 ablation), (2) cross-generator generalization with leave-one-out, (3) gen-1 vs gen-2+ boundary discrimination strength. MVP showed macro-F1=0.84 single-generator but hapax_ratio dominated feature importance.

## paper_framing.md

# Paper Framing — gen-depth-fingerprint

## Target Venue
- Primary: AAAI 2027 (deadline: August 2, 2026)
- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4
- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)

## Core Insight
Non-paraphrastic LLM generation chains (continuation, elaboration) operate in an unbounded semantic state space — unlike paraphrasing chains that converge to attractor cycles (ACL 2025). This means distributional drift accumulates monotonically with generation depth, leaving detectable "fingerprints" in token-level statistics under a reference model. These fingerprints enable ordinal depth estimation, unlocking risk-stratified data curation beyond binary real/synthetic filtering.

## Core Claims (3 条，均可证伪)

**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).

**Claim 2 — Distributional Fingerprint Independence**: Reference-model-derived features (entropy statistics, tail-distribution decay) carry independent depth signal beyond surface vocabulary statistics (TTR, hapax ratio). Ablation: reference-only features achieve significantly higher F1 than surface-only features, or at minimum provide significant complementary signal.

**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.

## Story Spine

**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).

**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.

**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation as an empirical phenomenon with practical implications for data governance. We formalize two competing hypotheses — H₁ (convergence: recursive generation tends toward a distributional fixed point even for non-paraphrastic chains) vs H₂ (divergence: non-paraphrastic chains accumulate monotonic drift) — and test them via depth-dependent distributional features under a reference model. Regardless of which hypothesis prevails, the characterization itself provides actionable insight: if H₂, depth estimation enables risk-stratified curation; if H₁, we establish the theoretical ceiling for depth-based approaches.

**Headline result template**: "On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines."

## Anticipated Reviewer Concerns

**RC1 — "Is this just vocabulary impoverishment?"**: If surface features (TTR, hapax) alone match full-feature performance, the "distributional fingerprint" framing is overclaimed. → Ablation experiment (Claim 2) directly addresses this.

**RC2 — "Does this generalize beyond Pythia?"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).

**RC3 — "Is 3-class sufficient? Why not finer-grained?"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.

**RC4 — "How realistic are single-model chains?"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).

**RC5 — "What about human editing / post-processing?"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).

**RC6 — "Ecological validity — continuation vs real web content"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).

## Venue Fit
- AAAI 2027: Strong fit — data governance + ML methodology. The H₁/H₂ hypothesis-testing framing positions it as empirical science, not just a classifier paper.
- EMNLP 2026: Excellent fit — directly addresses special theme "New Missions for NLP Research" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work.


## experiment_plan (with registry status)

- id: plan_001
  claim: 2
  name: feature_ablation
  description: 'Ablation: (A) reference-model-only features (entropy_mean/std/min/max
    + tail_decay) vs (B) surface-only features (TTR + hapax_ratio) vs (C) full feature
    set. Tests whether distributional fingerprint carries independent signal beyond
    vocabulary impoverishment.

    '
  priority: P0
  gpu_budget_hours: 1
  deps:
  - mvp-001
  notes: Uses existing MVP data. No new generation needed. Critical for Claim 2.
  status: planned
- id: plan_002
  claim: 1
  name: cross_generator_evaluation
  description: 'Expand to 5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B,
    Pythia-1B). Leave-one-generator-out CV to test cross-generator generalization.
    1000 seeds × 5 generators × 5 depths = 25K chains.

    '
  priority: P0
  gpu_budget_hours: 20
  deps:
  - plan_001
  notes: Only proceed if plan_001 confirms reference features have independent value.
  status: planned
- id: plan_003
  claim: 1
  name: cross_family_reference_model
  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B) for feature
    extraction. Addresses RC2 — verifies signal isn''t architecture-specific artifact.

    '
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_002
  status: planned
- id: plan_004
  claim: 3
  name: downstream_utility
  description: 'RQ4: Fine-tune a small LM (Pythia-410M or OLMo-1B) on depth-stratified
    data subsets. Measure perplexity degradation on held-out test set as function
    of training data depth. Compare depth-aware filtering vs binary baselines (FastDetectGPT,
    LD-Score threshold).

    '
  priority: P0
  gpu_budget_hours: 15
  deps:
  - plan_002
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
  "promptId": "0f762ddb-6afa-4880-975d-e64e5d13476d",
  "type": "user",
  "uuid": "cb471561-fa9d-4674-84f9-f488ed10df8e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T18:25:10.240Z_

```json
{
  "parentUuid": "cb471561-fa9d-4674-84f9-f488ed10df8e",
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
  "uuid": "a90244d8-1f41-4d06-92bd-273e98ff5fc0",
  "timestamp": "2026-05-14T18:25:10.240Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T18:25:10.240Z_

```json
{
  "parentUuid": "a90244d8-1f41-4d06-92bd-273e98ff5fc0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c36dd9ce-1e89-4959-a175-187ae32bfbe3",
  "timestamp": "2026-05-14T18:25:10.240Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Surface features explain nearly all variance; reference-model features add negligible signal; cross-generator generalization is weak; 'distributional fing…",
  "leafUuid": "c36dd9ce-1e89-4959-a175-187ae32bfbe3",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize worst-case depth estimation under vocabulary impoverishment",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24"
}
```

---

### Assistant

_source line 8 · 2026-05-14T18:25:19.706Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for the "worst" tier across all planned experiments in the experiment plan. I need to produce predicted results that align with the worst-case scenario defined in Phase 1, where surface features explain nearly all variance, reference-model features add negligible signal, and cross-generator generalization is weak.

Let me carefully go through each planned experiment and generate realistic worst-case predictions with rationales.

Key constraints from worst tier:
- plan_001_ref_only_macro_f1: [0.4, 0.55]
- plan_001_surface_only_macro_f1: [0.75, 0.84]


- plan_001_full_macro_f1: [0.76, 0.85]
- plan_001_ref_minus_surface_delta: [-0.35, -0.15]
- plan_002_cross_gen_leave_one_out_macro_f1: [0.42, 0.58]
- plan_002_cross_gen_gen1_f1: [0.35, 0.5]
- plan_002_cross_gen_gen2plus_f1: [0.38, 0.52]
- plan_003_cross_family_ref_macro_f1: [0.4, 0.55]
- plan_004_depth_quality_spearman_rho: [0.1, 0.3]
- plan_004_depth_filter_vs_binary_perf_gap_pct: [-1.0, 0.5]

Now I need to fill in the remaining experiments through plan_012 and structure everything as YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c36dd9ce-1e89-4959-a175-187ae32bfbe3",
  "isSidechain": false,
  "requestId": "req_011Cb2vuxDxdbxLktzUyj2g9",
  "type": "assistant",
  "uuid": "2093c78b-8ff5-4935-acd9-bcb9d6968c3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLkdyWc6EMG14tKWzj1F3g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9567,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11347,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9567
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

_source line 9 · 2026-05-14T18:28:38.465Z_

```yaml
tier: worst
narrative_guidance: >
  Abandon "distributional fingerprint" as primary contribution. Surface features (TTR, hapax_ratio)
  explain nearly all classifier variance; reference-model entropy statistics add negligible independent
  signal. Cross-generator generalization collapses because surface vocabulary statistics are
  generator-specific artifacts, not universal depth markers. Reframe paper as an empirical
  characterization of recursive generation dynamics: "We tested H₁ vs H₂ and found that
  non-paraphrastic chains also converge rapidly in distributional space, with detectable
  differences confined primarily to vocabulary impoverishment." Reposition as negative-but-informative
  result extending attractor cycle theory to non-paraphrastic settings. New angle: vocabulary
  impoverishment as a universal but shallow fingerprint — theoretically motivated by generation
  entropy convergence under autoregressive sampling. Target AAAI as empirical science contribution
  with clear hypothesis-testing framing and boundary conditions for future work.

imagined_experiments:
  - name: feature_ablation
    plan_id: plan_001
    description: >
      Ablation of reference-only, surface-only, and full feature sets on MVP data (Pythia-2.8B
      generator, Pythia-410M reference, 3-class depth). Ordinal logistic regression + random
      forest, 5-fold CV.
    expected_results:
      surface_only_macro_f1: 0.82
      surface_only_cv_std: 0.015
      ref_only_macro_f1: 0.47
      ref_only_cv_std: 0.032
      full_macro_f1: 0.83
      full_cv_std: 0.014
      ref_minus_surface_delta: -0.35
      full_minus_surface_delta: 0.01
      permutation_importance_hapax_ratio: 0.31
      permutation_importance_ttr: 0.24
      permutation_importance_entropy_mean: 0.04
      permutation_importance_entropy_std: 0.03
      permutation_importance_tail_decay: 0.02
      ref_features_added_significance_p: 0.18
    result_rationale: >
      Surface features alone recover 97.6% of full-model performance (0.82 vs 0.84 MVP).
      hapax_ratio and TTR dominate because recursive generation progressively depletes rare
      vocabulary — a mechanical consequence of autoregressive sampling from a fixed
      distribution. Reference-model entropy statistics show near-chance 3-class performance
      (0.47) because the entropy distribution under the reference model converges rapidly
      across generation depths: by gen-1, the token-level surprise distribution is already
      close to its stationary form. Adding reference features to surface features yields
      only +0.01 F1 (not statistically significant, p=0.18 on paired bootstrap), confirming
      that entropy_mean/std/min/max carry redundant information already captured by vocabulary
      depletion proxies. The "distributional fingerprint" framing collapses — what we detect
      is vocabulary impoverishment, not a deeper distributional shift.
    tables:
      - name: "Table 2: Feature Ablation Results (3-class, MVP data)"
        columns: [Feature_Set, Macro_F1, Gen0_F1, Gen1_F1, Gen2plus_F1, CV_Std]
        rows:
          - [surface_only, 0.82, 0.94, 0.75, 0.77, 0.015]
          - [ref_only, 0.47, 0.58, 0.38, 0.44, 0.032]
          - [full, 0.83, 0.95, 0.76, 0.78, 0.014]
          - [chance, 0.33, 0.33, 0.33, 0.33, "-"]
      - name: "Table 3: Permutation Feature Importance (Full Model)"
        columns: [Feature, Importance, Std]
        rows:
          - [hapax_ratio, 0.31, 0.04]
          - [ttr, 0.24, 0.03]
          - [entropy_mean, 0.04, 0.02]
          - [entropy_std, 0.03, 0.01]
          - [entropy_min, 0.02, 0.01]
          - [entropy_max, 0.01, 0.01]
          - [tail_decay, 0.02, 0.01]
    figures_description:
      - "Fig 2a: Violin plot of per-depth feature distributions. hapax_ratio shows clear monotonic decrease (gen-0 median ~0.42, gen-1 ~0.31, gen-2+ ~0.27). entropy_mean shows overlapping distributions with only gen-0 slightly separated."
      - "Fig 2b: ROC curves for each feature set. Surface-only and full curves nearly overlap (AUC 0.91 vs 0.92). Ref-only curve barely above diagonal for gen-1 vs gen-2+ (AUC 0.56)."
      - "Fig 2c: Confusion matrices side-by-side. Ref-only model conflates gen-1 and gen-2+ heavily (off-diagonal mass ~55%). Surface-only cleanly separates gen-0 but confuses gen-1/gen-2+ at ~25% rate."
    analysis: >
      Claim 2 is falsified. The ablation decisively shows that reference-model features carry
      no independent signal. The full model's marginal +0.01 over surface-only is within noise.
      This result is consistent with the hypothesis that autoregressive generation entropy
      converges to a near-stationary distribution by gen-1, while vocabulary depletion
      (a surface-level phenomenon) continues to accumulate. The practical implication: a
      $0 feature (hapax_ratio) matches the expensive reference-model inference pipeline.

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B).
      1000 seeds × 5 generators × 5 depths = 25K chains. Leave-one-generator-out CV
      for cross-generator generalization. 3-class depth classification.
    expected_results:
      within_generator_avg_macro_f1: 0.81
      leave_one_out_avg_macro_f1: 0.48
      leave_one_out_std: 0.07
      leave_one_out_gen0_f1: 0.68
      leave_one_out_gen1_f1: 0.38
      leave_one_out_gen2plus_f1: 0.42
      loo_held_out_pythia28b_f1: 0.52
      loo_held_out_olmo_f1: 0.44
      loo_held_out_qwen2b_f1: 0.43
      loo_held_out_qwen08b_f1: 0.50
      loo_held_out_pythia1b_f1: 0.53
      gen1_vs_gen2plus_binary_loo_f1: 0.54
      pooled_all_generators_macro_f1: 0.62
    result_rationale: >
      Within-generator performance remains strong (~0.81) because each generator has a
      characteristic vocabulary depletion rate that surface features learn. But leave-one-out
      drops catastrophically to 0.48 because the absolute levels of hapax_ratio and TTR
      are generator-specific: Qwen models produce systematically different type-token ratios
      than Pythia models at every depth. The classifier learns generator-specific thresholds,
      not universal depth signatures. Gen-0 identification is partially salvaged (0.68)
      because human-written text has a consistently distinct surface profile regardless of
      which generator produces the synthetic continuations. Gen-1 vs gen-2+ discrimination
      is near chance (0.38/0.42) in the cross-generator setting because the vocabulary
      depletion curves of different generators at depth 1 overlap with other generators at
      depth 2+. Pythia-family held-out sets perform slightly better (0.52-0.53) due to
      Pythia-1B sharing vocabulary statistics with Pythia-2.8B in the training fold. Cross-
      family transfer (Qwen held out) is worst (0.43-0.44). This confirms that surface
      features are generator-specific, not universal depth markers.
    tables:
      - name: "Table 4: Cross-Generator Generalization (Leave-One-Out)"
        columns: [Held_Out_Generator, Macro_F1, Gen0_F1, Gen1_F1, Gen2plus_F1]
        rows:
          - [Pythia-2.8B, 0.52, 0.71, 0.40, 0.45]
          - [OLMo-2-1B, 0.44, 0.65, 0.34, 0.38]
          - [Qwen3.5-2B, 0.43, 0.64, 0.35, 0.39]
          - [Qwen3.5-0.8B, 0.50, 0.70, 0.38, 0.43]
          - [Pythia-1B, 0.53, 0.72, 0.42, 0.46]
          - ["**Average**", "**0.48**", "**0.68**", "**0.38**", "**0.42**"]
      - name: "Table 5: Within- vs Cross-Generator Comparison"
        columns: [Setting, Macro_F1, Δ_vs_Within]
        rows:
          - [within_generator_avg, 0.81, "-"]
          - [leave_one_out_avg, 0.48, -0.33]
          - [pooled_all_generators, 0.62, -0.19]
    figures_description:
      - "Fig 3a: Per-generator hapax_ratio distributions at each depth. Each generator occupies a distinct band — Qwen3.5-2B gen-0 median overlaps with Pythia-2.8B gen-1 median, explaining cross-generator confusion."
      - "Fig 3b: Heatmap of leave-one-out F1 (held-out generator × depth class). Clear gradient: gen-0 row is yellow (decent), gen-1 and gen-2+ rows are dark red (near-chance)."
      - "Fig 3c: t-SNE of feature space colored by generator. Points cluster by generator first, depth second — generator identity dominates the feature space geometry."
    analysis: >
      Claim 1 fails in its generalization requirement. Cross-generator macro-F1 of 0.48 is
      barely above chance (0.33). The fundamental problem: surface vocabulary statistics
      are generator-specific calibration artifacts. A model that learns "hapax_ratio < 0.30
      means gen-2+" from Pythia data will misclassify Qwen gen-0 text (which may have
      hapax_ratio ~0.35 vs Pythia gen-0 ~0.45). Without independent reference-model signal
      (which plan_001 showed is absent), there is no generator-invariant depth feature.
      The pooled setting (0.62) is inflated by within-generator signal bleeding through
      the non-held-out generators in training.

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      Test OLMo-2-1B and Qwen3.5-0.8B as reference models (replacing Pythia-410M) for
      feature extraction. Full cross of 3 reference models × 5 generators.
    expected_results:
      pythia_ref_cross_gen_macro_f1: 0.48
      olmo_ref_cross_gen_macro_f1: 0.45
      qwen_ref_cross_gen_macro_f1: 0.44
      best_ref_model: pythia_410m
      ref_model_variance_std: 0.02
      ensemble_3ref_cross_gen_macro_f1: 0.50
      ref_only_olmo_macro_f1: 0.43
      ref_only_qwen_macro_f1: 0.41
    result_rationale: >
      Changing the reference model does not rescue cross-generator performance because the
      bottleneck is not reference model choice — it is the absence of depth-discriminative
      signal in the entropy statistics themselves. All three reference models produce
      similarly uninformative entropy distributions because the phenomenon is fundamental:
      autoregressive generation entropy converges to near-stationary levels by gen-1
      regardless of which model measures it. The slight advantage of Pythia-410M (0.48 vs
      0.44-0.45) is a minor architectural compatibility effect with the Pythia generators
      in the training set, not genuine signal. Ensembling three reference models yields
      only +0.02 over the best single model, confirming the features are redundant across
      reference architectures. This rules out RC2 concerns as irrelevant — the problem is
      not architecture-specific artifacts but rather the fundamental convergence of generation
      entropy.
    tables:
      - name: "Table 6: Reference Model Comparison (Leave-One-Generator-Out)"
        columns: [Reference_Model, LOO_Macro_F1, Ref_Only_F1, Surface_Only_F1]
        rows:
          - [Pythia-410M, 0.48, 0.47, 0.82]
          - [OLMo-2-1B, 0.45, 0.43, 0.82]
          - [Qwen3.5-0.8B, 0.44, 0.41, 0.82]
          - [Ensemble (3 refs), 0.50, 0.49, 0.82]
    figures_description:
      - "Fig 4: Entropy-mean distributions per depth, faceted by reference model. All three reference models show nearly identical overlapping distributions across depths — the convergence phenomenon is reference-model-invariant."
    analysis: >
      Reference model choice is irrelevant because the underlying signal is absent. Surface
      features remain constant at 0.82 regardless of reference model (they don't use it),
      confirming surface features as the sole discriminative mechanism. The experiment
      conclusively addresses RC2 but in a way that undermines the paper: the signal isn't
      architecture-specific because there is no reference-model signal to be architecture-
      specific about.

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune Pythia-410M on depth-stratified data subsets. Measure perplexity degradation
      as function of training data depth. Compare depth-aware filtering vs binary baselines
      (FastDetectGPT, LD-Score threshold).
    expected_results:
      depth_quality_spearman_rho: 0.19
      depth_quality_spearman_p: 0.04
      ppl_gen0_only: 18.2
      ppl_gen1_mixed: 19.1
      ppl_gen2plus_mixed: 19.8
      ppl_unfiltered: 19.5
      depth_filter_top1_ppl: 18.5
      binary_filter_fastdetect_ppl: 18.4
      binary_filter_ldscore_ppl: 18.6
      depth_filter_vs_binary_perf_gap_pct: -0.3
      depth_filter_data_retained_pct: 38
      binary_filter_data_retained_pct: 42
    result_rationale: >
      A weak positive correlation (ρ=0.19) exists between predicted depth and quality
      degradation, but it is barely significant and practically meaningless. The perplexity
      difference between gen-0-only and gen-2+-mixed training is modest (~1.6 points)
      because vocabulary impoverishment in synthetic text creates a noisy but not catastrophic
      training signal — the model still learns reasonable language statistics from synthetic
      text, just with slightly depleted rare-word coverage. Depth-aware filtering performs
      equivalently to binary baselines (-0.3% gap, within noise) because the depth classifier's
      cross-generator errors (from plan_002) introduce enough noise to eliminate any advantage
      over simple binary filtering. FastDetectGPT actually edges out depth-aware filtering
      by 0.1 ppl because it makes fewer classification errors on the binary task than our
      system makes on the harder ordinal task. Claim 3 effectively fails — depth-aware
      filtering provides no practical advantage over binary baselines.
    tables:
      - name: "Table 7: Downstream Fine-tuning Perplexity"
        columns: [Training_Data, Perplexity, Data_Size_pct]
        rows:
          - [gen-0 only, 18.2, 33]
          - [gen-0 + gen-1, 18.8, 67]
          - [all depths unfiltered, 19.5, 100]
          - [depth-aware filter (≤gen-1), 18.5, 38]
          - [FastDetectGPT binary filter, 18.4, 42]
          - [LD-Score binary filter, 18.6, 40]
      - name: "Table 8: Depth-Quality Correlation"
        columns: [Metric, Value]
        rows:
          - [Spearman ρ (depth vs ppl_degradation), 0.19]
          - [p-value, 0.04]
          - [depth_filter vs best_binary gap, "-0.3%"]
    figures_description:
      - "Fig 5a: Scatter plot of predicted depth vs perplexity degradation. Weak positive trend with large variance. R² ≈ 0.04. Points heavily overlapping at gen-1/gen-2+ boundary."
      - "Fig 5b: Bar chart comparing filtering strategies. Error bars overlap completely between depth-aware and binary baselines. The differences are not practically significant."
    analysis: >
      Claim 3 fails. While a statistically significant correlation exists (p=0.04), the
      effect size is negligible (ρ=0.19) and depth-aware filtering underperforms binary
      baselines by 0.3%. The ordinal depth information adds no practical value over binary
      classification for data curation. This is the expected consequence of plan_001 and
      plan_002 results: if depth estimation relies on generator-specific surface features
      and cross-generator transfer is poor, the depth predictions are too noisy to provide
      downstream utility beyond what binary detection already offers.

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Compare continuation vs elaboration vs inspired_rewriting chains. 1000 seeds,
      Pythia-2.8B, 3 prompt types, 5 depths each.
    expected_results:
      continuation_within_gen_f1: 0.82
      elaboration_within_gen_f1: 0.78
      inspired_rewriting_within_gen_f1: 0.69
      continuation_cross_prompt_f1: 0.61
      elaboration_cross_prompt_f1: 0.58
      inspired_rewriting_cross_prompt_f1: 0.52
      convergence_speed_continuation_depth: 2
      convergence_speed_elaboration_depth: 2
      convergence_speed_rewriting_depth: 1
    result_rationale: >
      Continuation chains show the highest within-generator F1 (0.82) because they preserve
      the most topic continuity, making vocabulary depletion the dominant signal. Elaboration
      is slightly lower (0.78) due to topic drift introducing vocabulary variance that
      partially masks depletion. Inspired rewriting shows the weakest signal (0.69) because
      each generation step introduces substantially new vocabulary, partially resetting the
      depletion signal. Cross-prompt transfer is poor across the board because each prompt
      type induces a different vocabulary depletion rate — the classifier learns prompt-
      type-specific thresholds. Convergence analysis shows all three types stabilize by
      depth 2 (rewriting by depth 1), supporting H₁: even non-paraphrastic chains converge
      rapidly. The rewriting chains converge fastest because the larger semantic jumps
      quickly exhaust the generator's preferred vocabulary, reaching a "vocabulary floor"
      by gen-1.
    tables:
      - name: "Table 9: Prompt Type Comparison"
        columns: [Prompt_Type, Within_Gen_F1, Cross_Prompt_F1, Convergence_Depth]
        rows:
          - [continuation, 0.82, 0.61, 2]
          - [elaboration, 0.78, 0.58, 2]
          - [inspired_rewriting, 0.69, 0.52, 1]
    figures_description:
      - "Fig 6a: Per-depth hapax_ratio trajectories for each prompt type. All three converge but at different rates and to different asymptotes. Rewriting flattens by gen-1; continuation shows a gradual decline through gen-2 then plateaus."
      - "Fig 6b: Feature distribution overlap (KL divergence between consecutive depths) per prompt type. All types show rapid KL collapse, with gen-2→gen-3 KL < 0.05 nats for all types."
    analysis: >
      All prompt types show rapid convergence, supporting H₁. The depth signal ceiling is
      approximately 2 effective classes (gen-0 vs synthetic) for rewriting and 3 classes
      (gen-0/gen-1/gen-2+) for continuation — but only within-generator. The prompt type
      comparison reveals an additional confound: not only is the signal generator-specific,
      it is prompt-type-specific. This further narrows the practical applicability of depth
      estimation.

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      Construct parallel paraphrasing chains for direct comparison with continuation chains.
      Test attractor convergence theory — H₁ vs H₂.
    expected_results:
      paraphrase_within_gen_f1: 0.64
      continuation_within_gen_f1: 0.82
      paraphrase_convergence_depth: 1
      continuation_convergence_depth: 2
      paraphrase_gen1_vs_gen2plus_f1: 0.41
      continuation_gen1_vs_gen2plus_f1: 0.58
      kl_depth2_vs_depth3_paraphrase: 0.008
      kl_depth2_vs_depth3_continuation: 0.031
    result_rationale: >
      Paraphrasing chains converge faster than continuation chains (by depth 1 vs depth 2),
      consistent with attractor cycle theory from ACL 2025. Paraphrasing F1 is lower (0.64)
      because the semantic-preservation constraint limits vocabulary variation — paraphrases
      reuse similar word types, so hapax_ratio depletion is less pronounced. But crucially,
      continuation chains also converge by depth 2, meaning non-paraphrastic generation
      does NOT produce the unbounded divergence hypothesized in H₂. Both chain types reach
      near-stationary distributions within 2-3 steps. The KL divergence between depth-2 and
      depth-3 is negligible for both types (<0.04 nats). This is the key finding for the
      worst-case narrative: H₁ (convergence) holds even for non-paraphrastic chains, limiting
      depth signal to a maximum of ~2-3 discriminable classes and undermining the premise
      that non-paraphrastic chains produce monotonic divergence.
    tables:
      - name: "Table 10: Paraphrastic vs Non-Paraphrastic Chains"
        columns: [Chain_Type, Macro_F1_3class, Gen1_vs_Gen2plus_F1, Convergence_Depth, KL_d2_d3]
        rows:
          - [paraphrasing, 0.64, 0.41, 1, 0.008]
          - [continuation, 0.82, 0.58, 2, 0.031]
          - [elaboration, 0.78, 0.52, 2, 0.024]
          - [inspired_rewriting, 0.69, 0.44, 1, 0.012]
    figures_description:
      - "Fig 7: Feature trajectory plots (hapax_ratio, entropy_mean) across depths 0-4, paraphrastic vs continuation. Both converge but continuation has a slightly longer transient. Shaded regions show ±1σ across seeds. Both curves flatten by depth 2-3."
    analysis: >
      H₁ is confirmed: non-paraphrastic chains also converge, just 1 step slower than
      paraphrastic chains. This extends the ACL 2025 attractor theory to non-paraphrastic
      settings — arguably the most publishable finding in the worst case. The convergence
      is driven by autoregressive sampling from a fixed model concentrating probability mass
      on preferred tokens regardless of prompt type, creating a universal vocabulary
      attractor. Depth signal is fundamentally bounded at ~2-3 classes.

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Cross-model chains (different generator per depth step) vs single-model chains.
      5 generators randomly assigned per step. 1000 seeds × 5 depths.
    expected_results:
      single_model_within_gen_f1: 0.81
      cross_model_chain_f1: 0.42
      cross_model_gen0_f1: 0.65
      cross_model_gen1_f1: 0.32
      cross_model_gen2plus_f1: 0.35
      cross_model_binary_gen0_vs_rest_f1: 0.67
    result_rationale: >
      Cross-model chains are devastating for depth estimation (0.42 macro-F1). When different
      generators produce each depth step, the vocabulary statistics at any given depth
      reflect the current-step generator's preferences more than the cumulative depth of the
      chain. A text generated by Qwen at depth-2 in a chain may have higher hapax_ratio
      than text generated by Pythia-1B at depth-1, because Qwen has a richer base vocabulary.
      The generator-switching effectively randomizes the surface features that the classifier
      depends on. Gen-0 identification survives partially (0.65) because human text is still
      distinct from any generator, but gen-1/gen-2+ classification is near-chance. This
      is the most realistic contamination scenario and the most damning result for practical
      applicability.
    tables:
      - name: "Table 11: Single-Model vs Cross-Model Chains"
        columns: [Setting, Macro_F1, Gen0_F1, Gen1_F1, Gen2plus_F1]
        rows:
          - [single_model_chains, 0.81, 0.94, 0.75, 0.77]
          - [cross_model_chains, 0.42, 0.65, 0.32, 0.35]
          - [chance, 0.33, 0.33, 0.33, 0.33]
    figures_description:
      - "Fig 8: Paired bar chart showing collapse from single-model to cross-model setting. Gen-1 and gen-2+ bars drop to near-chance. Annotation: 'generator identity dominates depth signal.'"
    analysis: >
      The most ecologically valid setting (cross-model chains) produces near-chance depth
      estimation. This confirms that the MVP result (0.84) was an artifact of single-model
      evaluation: the classifier learned Pythia-2.8B's specific vocabulary depletion curve,
      not a universal depth signature. In realistic web contamination scenarios with diverse
      generators, depth estimation beyond binary (human vs synthetic) is not feasible with
      current features.

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      Expand to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC), creative
      writing (WritingPrompts). 500 seeds per domain × 5 depths, Pythia-2.8B generator.
    expected_results:
      wikipedia_within_domain_f1: 0.83
      news_within_domain_f1: 0.80
      scientific_within_domain_f1: 0.76
      creative_within_domain_f1: 0.72
      cross_domain_avg_f1: 0.59
      pooled_all_domains_f1: 0.74
      scientific_hapax_ratio_gen0_median: 0.52
      creative_hapax_ratio_gen0_median: 0.38
    result_rationale: >
      Within-domain performance is reasonable but varies by domain. Wikipedia/news are
      easiest because their seed texts have high hapax_ratio (specialized proper nouns,
      rare terms) that generation rapidly depletes. Scientific text starts with high
      rare-word density (technical terms) but the generator sometimes preserves or
      regenerates these, creating noise. Creative writing is hardest because its base
      vocabulary is less specialized — the hapax_ratio gap between gen-0 and gen-1 is
      smaller. Cross-domain transfer drops to 0.59 because each domain has different
      baseline vocabulary statistics: scientific gen-0 text (hapax_ratio ~0.52) overlaps
      with creative gen-0 (~0.38), confounding domain and depth. This adds another axis
      of non-generalization beyond generator and prompt type.
    tables:
      - name: "Table 12: Multi-Domain Results"
        columns: [Domain, Within_Domain_F1, Gen0_hapax_median, Gen2plus_hapax_median, Δ_hapax]
        rows:
          - [Wikipedia, 0.83, 0.47, 0.26, 0.21]
          - [News, 0.80, 0.44, 0.27, 0.17]
          - [Scientific, 0.76, 0.52, 0.35, 0.17]
          - [Creative, 0.72, 0.38, 0.28, 0.10]
          - [Cross-domain avg, 0.59, "-", "-", "-"]
    figures_description:
      - "Fig 9: Per-domain hapax_ratio trajectories across depths. All four domains show monotonic decrease but with different baselines and slopes. Scientific and creative curves overlap substantially."
    analysis: >
      Domain is yet another confound. The depth signal is domain-specific because the
      magnitude of vocabulary depletion depends on the seed text's lexical richness.
      Combined with generator-specificity and prompt-type-specificity, this creates a
      three-way interaction that makes general-purpose depth estimation impractical.
      A classifier trained on Wikipedia+news will overestimate depth for creative writing
      (lower base hapax) and underestimate it for scientific text (higher base hapax).

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic continuation
      chains. Tests if more than 3-class depth signal exists.
    expected_results:
      ordinal_5class_macro_f1: 0.52
      ordinal_5class_gen0_f1: 0.91
      ordinal_5class_gen1_f1: 0.58
      ordinal_5class_gen2_f1: 0.38
      ordinal_5class_gen3_f1: 0.31
      ordinal_5class_gen4_f1: 0.33
      ordinal_3class_macro_f1: 0.82
      adjacent_class_confusion_rate: 0.44
      mae_ordinal: 0.72
    result_rationale: >
      5-class performance drops sharply to 0.52 macro-F1 (from 0.82 for 3-class), with
      gen-2 through gen-4 collapsing into near-chance mutual confusion. This is the direct
      consequence of H₁ convergence: by depth 2, the feature distributions have already
      converged, so gen-2/gen-3/gen-4 are statistically indistinguishable. The confusion
      is concentrated in adjacent classes (44% of errors are off-by-one), consistent with
      a smooth convergence rather than discrete depth categories. Gen-0 remains easily
      identified (0.91) and gen-1 partially (0.58), but beyond gen-1 the signal is gone.
      This confirms the practical ceiling is 2-3 discriminable depth classes, not finer-
      grained ordinal estimation.
    tables:
      - name: "Table 13: 5-Class Ordinal Classification"
        columns: [Class, Precision, Recall, F1]
        rows:
          - [gen-0, 0.93, 0.90, 0.91]
          - [gen-1, 0.54, 0.62, 0.58]
          - [gen-2, 0.36, 0.40, 0.38]
          - [gen-3, 0.29, 0.33, 0.31]
          - [gen-4, 0.31, 0.35, 0.33]
      - name: "Table 14: 5-Class Confusion Matrix"
        columns: [Predicted→, gen-0, gen-1, gen-2, gen-3, gen-4]
        rows:
          - [gen-0, 0.90, 0.07, 0.02, 0.01, 0.00]
          - [gen-1, 0.09, 0.62, 0.18, 0.07, 0.04]
          - [gen-2, 0.03, 0.21, 0.40, 0.22, 0.14]
          - [gen-3, 0.02, 0.10, 0.24, 0.33, 0.31]
          - [gen-4, 0.01, 0.07, 0.16, 0.28, 0.48]
    figures_description:
      - "Fig 10: Per-class F1 as function of number of ordinal classes (2, 3, 4, 5). Sharp elbow at 3 classes — adding a 4th or 5th class produces near-chance F1 for the new classes without improving existing ones."
    analysis: >
      Finer-grained estimation is not feasible. The depth signal has a hard ceiling at
      ~3 discriminable classes, consistent with convergence by depth 2. The confusion
      matrix shows a clear diagonal-plus-adjacent pattern typical of ordinal features
      with limited dynamic range. Gen-3 and gen-4 are essentially exchangeable. This
      further limits the practical scope of depth estimation.

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Robustness to simulated human edits. (A) Random word replacement at 5%, 10%, 20%.
      (B) LLM-simulated editing (light rephrasing of random sentences).
    expected_results:
      baseline_no_edit_f1: 0.82
      random_replace_5pct_f1: 0.77
      random_replace_10pct_f1: 0.70
      random_replace_20pct_f1: 0.58
      llm_edit_light_f1: 0.63
      llm_edit_light_gen0_f1: 0.82
      llm_edit_light_gen1_f1: 0.51
      llm_edit_light_gen2plus_f1: 0.48
    result_rationale: >
      Editing disrupts the surface features that carry all the signal. Even 5% random word
      replacement drops F1 by 0.05 because replaced words tend to be common words replaced
      with less-common alternatives, artificially inflating hapax_ratio and masking
      vocabulary depletion. At 20%, the editing noise dominates the depth signal. LLM-
      simulated editing (light rephrasing) is particularly damaging (0.63) because the
      editing LLM introduces its own vocabulary preferences, adding a second generator's
      fingerprint on top of the original. Since the classifier relies on vocabulary
      statistics, any post-hoc vocabulary injection confounds depth estimation. This
      confirms the fragility of surface-feature-based depth estimation in realistic
      scenarios where synthetic text is edited before publication.
    tables:
      - name: "Table 15: Robustness to Human Edits"
        columns: [Edit_Type, Edit_Rate, Macro_F1, Δ_vs_Baseline]
        rows:
          - [none, 0%, 0.82, "-"]
          - [random_replace, 5%, 0.77, -0.05]
          - [random_replace, 10%, 0.70, -0.12]
          - [random_replace, 20%, 0.58, -0.24]
          - [llm_simulated, light, 0.63, -0.19]
    figures_description:
      - "Fig 11: F1 degradation curve as function of edit rate. Approximately linear decline. Dashed line marks the point where depth estimation drops below binary baseline performance (~12% edit rate)."
    analysis: >
      Surface features are fragile under editing. The crossover point where depth estimation
      becomes worse than binary detection occurs at approximately 12% word replacement rate.
      Real-world synthetic text is routinely edited at this level or above, further limiting
      practical applicability.

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      Add LD-Score (character-distribution signature) as additional feature. Tests whether
      character-level features provide complementary depth signal.
    expected_results:
      surface_plus_ld_macro_f1: 0.83
      ld_only_macro_f1: 0.61
      full_plus_ld_macro_f1: 0.83
      ld_cross_gen_loo_f1: 0.46
      ld_feature_importance: 0.05
    result_rationale: >
      LD-Score as a standalone feature performs moderately (0.61) — better than reference-
      model features (0.47) but worse than surface features (0.82). This is because
      character-level distributions partially capture vocabulary depletion through character
      frequency shifts, providing a smoothed proxy for hapax_ratio. However, adding LD-Score
      to surface features yields negligible improvement (+0.01) because the character-level
      signal is redundant with word-level surface statistics. Cross-generator transfer with
      LD-Score (0.46) is no better than without, confirming that character-level features
      also suffer from generator-specificity. LD-Score does not rescue the fundamental
      problem.
    tables:
      - name: "Table 16: LD-Score Feature Analysis"
        columns: [Feature_Set, Macro_F1, LOO_Cross_Gen_F1]
        rows:
          - [surface_only, 0.82, 0.48]
          - [ld_only, 0.61, 0.46]
          - [surface + ld, 0.83, 0.49]
          - [full + ld, 0.83, 0.50]
    figures_description:
      - "Fig S1 (appendix): LD-Score distribution per depth. Moderate separation between gen-0 and gen-2+ but heavy overlap at gen-1, similar to ref-model entropy features."
    analysis: >
      LD-Score is a character-level echo of word-level vocabulary depletion — correlated
      but not complementary. It does not provide a new axis of depth information. Including
      it in the paper is optional; it addresses a potential reviewer question but doesn't
      change conclusions.

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification. Compares learned
      representations vs handcrafted features.
    expected_results:
      e2e_within_gen_macro_f1: 0.87
      e2e_cross_gen_loo_macro_f1: 0.53
      e2e_cross_gen_gen0_f1: 0.74
      e2e_cross_gen_gen1_f1: 0.42
      e2e_cross_gen_gen2plus_f1: 0.45
      e2e_vs_handcrafted_within_delta: 0.05
      e2e_vs_handcrafted_cross_delta: 0.05
      e2e_attention_analysis_top_tokens: ["the", "of", "is", ".", ","]
    result_rationale: >
      The end-to-end model achieves marginally higher within-generator F1 (0.87 vs 0.82)
      by learning soft vocabulary depletion features beyond hapax_ratio and TTR — it
      implicitly captures the full vocabulary distribution shift through its representations.
      However, cross-generator transfer shows only modest improvement (0.53 vs 0.48),
      meaning the learned representations are also predominantly generator-specific.
      Attention analysis reveals the model focuses on high-frequency function words and
      punctuation — exactly the tokens whose usage patterns shift under vocabulary
      impoverishment. The learned model does not discover hidden distributional structure
      beyond surface statistics; it simply learns a richer encoding of the same surface
      phenomenon. The 0.05 cross-gen improvement over handcrafted features is the only
      hint that some generator-invariant signal might exist in deeper representations,
      but it is not large enough to be practically useful.
    tables:
      - name: "Table 17: End-to-End vs Handcrafted Features"
        columns: [Model, Within_Gen_F1, Cross_Gen_LOO_F1, Δ_Cross_Gen]
        rows:
          - [handcrafted (surface + ref), 0.83, 0.48, "-"]
          - [QLoRA Qwen3.5-0.8B, 0.87, 0.53, +0.05]
          - [handcrafted surface_only, 0.82, 0.48, "-"]
    figures_description:
      - "Fig S2 (appendix): Attention heatmaps from fine-tuned model on gen-0 vs gen-2+ examples. Model attends heavily to function words and sentence boundaries — consistent with vocabulary impoverishment detection rather than deeper distributional analysis."
      - "Fig S3 (appendix): t-SNE of learned representations. Slight improvement in depth separation vs handcrafted features, but generator clusters still dominate the embedding space."
    analysis: >
      The end-to-end model confirms the ceiling: even with 0.8B parameters and full
      sequence access, cross-generator depth estimation barely exceeds chance for gen-1
      and gen-2+. The model learns vocabulary impoverishment more efficiently than
      handcrafted features (+0.05 within-gen) but cannot overcome the fundamental
      generator-specificity of the signal (+0.05 cross-gen, still at 0.53). This closes
      the "maybe a bigger model could find it" escape hatch — the signal genuinely isn't
      there for cross-generator depth estimation.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2093c78b-8ff5-4935-acd9-bcb9d6968c3b",
  "isSidechain": false,
  "requestId": "req_011Cb2vuxDxdbxLktzUyj2g9",
  "type": "assistant",
  "uuid": "4f7d295e-57fd-4c85-bd85-8878056966c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLkdyWc6EMG14tKWzj1F3g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9567,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11347,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9567
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Surface features explain nearly all variance; reference-model features add negligible signal; cross-generator generalization is weak; 'distributional fing…",
  "leafUuid": "4f7d295e-57fd-4c85-bd85-8878056966c5",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize worst-case depth estimation under vocabulary impoverishment",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Surface features explain nearly all variance; reference-model features add negligible signal; cross-generator generalization is weak; 'distributional fing…",
  "leafUuid": "4f7d295e-57fd-4c85-bd85-8878056966c5",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize worst-case depth estimation under vocabulary impoverishment",
  "sessionId": "72ba5d00-5964-499d-ab17-ffb22355be24"
}
```

---
