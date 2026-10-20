# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Reference-model features carry dominant independent depth signal; cross-gene

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-1/33650369-a049-4c64-8301-8fd18bc00ef8.jsonl`
- **Structured JSON:** [`e21402b52b463cd3e122.json`](../../sessions/e2/e21402b52b463cd3e122.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T18:13:11.079Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T18:13:11.079Z",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Reference-model features carry dominant independent depth signal; cross-generator generalization holds; all three claims verified cleanly\n核心假设：['Claim 2 fully validated: ref-only features significantly outperform surface-only features in ablation', 'hapax_ratio dominance in MVP was an artifact of small feature set / single-generator setting; adding generators dilutes surface shortcut', 'Cross-generator leave-one-out retains strong performance (generator-invariant distributional drift pattern exists)', 'gen-1 vs gen-2+ boundary is cleanly discriminable, not just gen-0 vs rest', 'Downstream fine-tuning quality degrades monotonically with depth, and depth-aware filtering shows clear win over binary baselines']\n关键指标范围：{'plan_001_ref_only_macro_f1': [0.76, 0.84], 'plan_001_surface_only_macro_f1': [0.58, 0.68], 'plan_001_full_macro_f1': [0.84, 0.9], 'plan_001_ref_minus_surface_delta': [0.1, 0.25], 'plan_002_cross_gen_leave_one_out_macro_f1': [0.74, 0.82], 'plan_002_cross_gen_gen1_f1': [0.68, 0.78], 'plan_002_cross_gen_gen2plus_f1': [0.7, 0.8], 'plan_003_cross_family_ref_macro_f1': [0.7, 0.8], 'plan_004_depth_quality_spearman_rho': [0.6, 0.85], 'plan_004_depth_filter_vs_binary_perf_gap_pct': [3.0, 8.0]}\n叙事方向：Original framing fully intact. Story: non-paraphrastic chains exhibit monotonic distributional divergence (H₂ confirmed), detectable via reference-model entropy features that capture drift beyond surface vocabulary impoverishment. Headline: \"distributional fingerprints enable risk-stratified data curation,\" with clean ablation separating signal from shortcut. All three claims stated at full strength. AAAI submission with no scope reduction.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-fingerprint\nvenue: AAAI 2027\nfocus: Key uncertainties: (1) whether reference-model features carry independent signal vs surface vocabulary stats (Claim 2 ablation), (2) cross-generator generalization with leave-one-out, (3) gen-1 vs gen-2+ boundary discrimination strength. MVP showed macro-F1=0.84 single-generator but hapax_ratio dominated feature importance.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains (continuation, elaboration) operate in an unbounded semantic state space — unlike paraphrasing chains that converge to attractor cycles (ACL 2025). This means distributional drift accumulates monotonically with generation depth, leaving detectable \"fingerprints\" in token-level statistics under a reference model. These fingerprints enable ordinal depth estimation, unlocking risk-stratified data curation beyond binary real/synthetic filtering.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Distributional Fingerprint Independence**: Reference-model-derived features (entropy statistics, tail-distribution decay) carry independent depth signal beyond surface vocabulary statistics (TTR, hapax ratio). Ablation: reference-only features achieve significantly higher F1 than surface-only features, or at minimum provide significant complementary signal.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation as an empirical phenomenon with practical implications for data governance. We formalize two competing hypotheses — H₁ (convergence: recursive generation tends toward a distributional fixed point even for non-paraphrastic chains) vs H₂ (divergence: non-paraphrastic chains accumulate monotonic drift) — and test them via depth-dependent distributional features under a reference model. Regardless of which hypothesis prevails, the characterization itself provides actionable insight: if H₂, depth estimation enables risk-stratified curation; if H₁, we establish the theoretical ceiling for depth-based approaches.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: If surface features (TTR, hapax) alone match full-feature performance, the \"distributional fingerprint\" framing is overclaimed. → Ablation experiment (Claim 2) directly addresses this.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n## Venue Fit\n- AAAI 2027: Strong fit — data governance + ML methodology. The H₁/H₂ hypothesis-testing framing positions it as empirical science, not just a classifier paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 2\n  name: feature_ablation\n  description: 'Ablation: (A) reference-model-only features (entropy_mean/std/min/max\n    + tail_decay) vs (B) surface-only features (TTR + hapax_ratio) vs (C) full feature\n    set. Tests whether distributional fingerprint carries independent signal beyond\n    vocabulary impoverishment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-001\n  notes: Uses existing MVP data. No new generation needed. Critical for Claim 2.\n  status: planned\n- id: plan_002\n  claim: 1\n  name: cross_generator_evaluation\n  description: 'Expand to 5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B,\n    Pythia-1B). Leave-one-generator-out CV to test cross-generator generalization.\n    1000 seeds × 5 generators × 5 depths = 25K chains.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: Only proceed if plan_001 confirms reference features have independent value.\n  status: planned\n- id: plan_003\n  claim: 1\n  name: cross_family_reference_model\n  description: 'Test non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B) for feature\n    extraction. Addresses RC2 — verifies signal isn''t architecture-specific artifact.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  status: planned\n- id: plan_004\n  claim: 3\n  name: downstream_utility\n  description: 'RQ4: Fine-tune a small LM (Pythia-410M or OLMo-1B) on depth-stratified\n    data subsets. Measure perplexity degradation on held-out test set as function\n    of training data depth. Compare depth-aware filtering vs binary baselines (FastDetectGPT,\n    LD-Score threshold).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_005\n  claim: 1\n  name: prompt_type_comparison\n  description: 'RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting\n    chains. Tests whether semantic divergence from source correlates with depth signal\n    preservation. Same 1000 seeds, Pythia-2.8B, 3 prompt types.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_006\n  claim: 1\n  name: paraphrastic_comparison\n  description: 'RQ2 full: Construct parallel paraphrasing chains for direct comparison\n    with continuation chains. Tests attractor convergence theory — do non-paraphrastic\n    chains preserve more depth signal?\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_005\n  status: planned\n- id: plan_007\n  claim: 1\n  name: cross_model_chains\n  description: 'RQ3: Cross-model chains (different generator per depth step) vs single-model\n    chains. More realistic scenario — web contamination involves diverse generators.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  name: multi_domain_seeds\n  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific\n    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5\n    depths.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_009\n  claim: 1\n  name: finer_grained_ordinal\n  description: 'Secondary analysis: 5-class ordinal classification (gen-0 through\n    gen-4) on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.\n\n    '\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  name: human_edit_robustness\n  description: 'RC5: Robustness to simulated human edits. (A) Random word replacement\n    (5%, 10%, 20%) as lower-bound. (B) LLM-simulated editing (light rephrasing of\n    random sentences).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 2\n  name: ld_score_feature\n  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)\n    as additional feature. Tests whether character-level features provide complementary\n    depth signal.\n\n    '\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  status: planned\n- id: plan_012\n  claim: 1\n  name: end_to_end_classifier\n  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.\n    Compares learned representations vs handcrafted distributional features.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.8408\n    binary_f1_gen0_vs_gen2plus: 0.8653\n    cv_macro_f1: 0.806\n    cv_std: 0.013\n    gen0_f1: 0.9517\n    gen1_f1: 0.7759\n    gen2plus_f1: 0.7947\n    total_records: 4609\n    seeds_used: 995\n    skipped: 173\n- exp_id: mvp-001-gen-s0\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-001-gen-s1\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-001-gen-s3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T18:13:11.082Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T18:13:11.082Z",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8"
}
```

---

## Round 1

15 recorded events

### User

_source line 3 · 2026-05-14T18:13:11.097Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Reference-model features carry dominant independent depth signal; cross-generator generalization holds; all three claims verified cleanly
核心假设：['Claim 2 fully validated: ref-only features significantly outperform surface-only features in ablation', 'hapax_ratio dominance in MVP was an artifact of small feature set / single-generator setting; adding generators dilutes surface shortcut', 'Cross-generator leave-one-out retains strong performance (generator-invariant distributional drift pattern exists)', 'gen-1 vs gen-2+ boundary is cleanly discriminable, not just gen-0 vs rest', 'Downstream fine-tuning quality degrades monotonically with depth, and depth-aware filtering shows clear win over binary baselines']
关键指标范围：{'plan_001_ref_only_macro_f1': [0.76, 0.84], 'plan_001_surface_only_macro_f1': [0.58, 0.68], 'plan_001_full_macro_f1': [0.84, 0.9], 'plan_001_ref_minus_surface_delta': [0.1, 0.25], 'plan_002_cross_gen_leave_one_out_macro_f1': [0.74, 0.82], 'plan_002_cross_gen_gen1_f1': [0.68, 0.78], 'plan_002_cross_gen_gen2plus_f1': [0.7, 0.8], 'plan_003_cross_family_ref_macro_f1': [0.7, 0.8], 'plan_004_depth_quality_spearman_rho': [0.6, 0.85], 'plan_004_depth_filter_vs_binary_perf_gap_pct': [3.0, 8.0]}
叙事方向：Original framing fully intact. Story: non-paraphrastic chains exhibit monotonic distributional divergence (H₂ confirmed), detectable via reference-model entropy features that capture drift beyond surface vocabulary impoverishment. Headline: "distributional fingerprints enable risk-stratified data curation," with clean ablation separating signal from shortcut. All three claims stated at full strength. AAAI submission with no scope reduction.


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
  "promptId": "0a119b01-1009-40b6-92ce-4a59605973e6",
  "type": "user",
  "uuid": "db01f50f-1d59-4f40-989d-7759a17b7303",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T18:13:11.096Z_

```json
{
  "parentUuid": "db01f50f-1d59-4f40-989d-7759a17b7303",
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
  "uuid": "19178ad3-1219-44b3-9d21-5ce59cd62ca4",
  "timestamp": "2026-05-14T18:13:11.096Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T18:13:11.096Z_

```json
{
  "parentUuid": "19178ad3-1219-44b3-9d21-5ce59cd62ca4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4d8f0f59-1a03-4382-8790-125494f0fc27",
  "timestamp": "2026-05-14T18:13:11.096Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate distributional fingerprints for generation depth estimation",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8"
}
```

---

### Assistant

_source line 7 · 2026-05-14T18:13:15.133Z_

我先查看项目现有的数据和实验细节，确保预测建立在实际基础上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d8f0f59-1a03-4382-8790-125494f0fc27",
  "isSidechain": false,
  "requestId": "req_011Cb2uzwc2J9ecCGd59Gaz7",
  "type": "assistant",
  "uuid": "ef82f2c5-664d-4b95-a945-6911af3ea2ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRTjGukUgkk8Cm4va18J11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 11841,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 324,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9401
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

_source line 8 · 2026-05-14T18:13:22.418Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VfrTAzii3WXfF8AALyz8QQ`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore project structure and MVP details",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_3, I need to understand:\n1. The overall file structure (what directories and key files exist)\n2. The MVP experiment details — especially feature importance results from mvp-001, the feature set used, the classifier used, and any existing analysis\n3. Any existing prediction or tier files\n\nSearch broadly: look at the top-level directory, any data/, results/, experiments/, analysis/ directories, and any YAML/JSON/MD files that contain experiment results or feature importance info. Read the most relevant files. Report back with specific details about:\n- Feature importance rankings from MVP (especially hapax_ratio dominance)\n- Exact feature list used\n- Classifier type and hyperparameters\n- Data generation details (models, seeds, depths, domains)\n- Any existing imagined_experiments or tier prediction files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef82f2c5-664d-4b95-a945-6911af3ea2ab",
  "isSidechain": false,
  "requestId": "req_011Cb2uzwc2J9ecCGd59Gaz7",
  "type": "assistant",
  "uuid": "0043e714-5fcd-444d-ac22-7866d37aa796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRTjGukUgkk8Cm4va18J11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 11841,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 324,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9401
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

_source line 9_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reference-model features carry dominant independent depth signal; cross-generator generalization holds; all three claims verified cleanly 核心假设：['Claim 2 fu…",
  "leafUuid": "0043e714-5fcd-444d-ac22-7866d37aa796",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate distributional fingerprints for generation depth estimation",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8"
}
```

---

### Tool result

_source line 11 · 2026-05-14T18:14:38.101Z_

<details><summary>↩ Tool result · `toolu_01VfrTAzii3WXfF8AALyz8QQ`</summary>

```text
Perfect! I've found the dream output. Let me now compile all the information I've gathered.

## Summary Report: MVP Experiment & Project Overview

### 1. **Project Structure**

**Top-level directory**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`

Key subdirectories:
- `artifacts/` - output artifacts (MVP scripts, results pointers, dream reports)
- `logs/workers/` - worker execution logs and results
- `checkpoints/` - experiment state checkpoints
- `.claude/sessions/` - agent conversation sessions
- `docs/IDEA_BRIEF.md` - complete project proposal
- Configuration files: `experiment_plan.yaml`, `registry.yaml`, `memory.md`, `paper_framing.md`, `decisions.yaml`, `ROADMAP.md`

---

### 2. **MVP-001 Experiment Details** (Completed: 2026-05-14)

#### **Core Hypothesis**
Pythia-410M reference model distributional features (entropy stats, tail-decay, TTR, hapax) can discriminate Pythia-2.8B continuation chains into three depth classes (gen-0/gen-1/gen-2+) with macro-F1 ≥ 0.45.

#### **Feature Set (7 features)**
1. **hapax_ratio** - proportion of hapax legomena (words appearing once) — dominance importance: 0.3004
2. **entropy_mean** - mean of next-token log-probability distribution — importance: 0.2202
3. **ttr** (type-token ratio) — importance: 0.1651
4. **entropy_std** - variance of next-token distribution — importance: 0.1340
5. **entropy_max** - maximum of distribution — importance: 0.0650
6. **entropy_min** - minimum of distribution — importance: 0.0585
7. **tail_decay** - probability mass beyond 90th/95th percentiles — importance: 0.0569

All features statistically significant (Kruskal-Wallis + Bonferroni correction, p < 0.001).

#### **Data Generation**
- **Generator model**: EleutherAI/Pythia-2.8B (FP16)
- **Reference model**: EleutherAI/Pythia-410M
- **Dataset**: Wikipedia (1000 seeds, local JSONL: `wiki_seed_1000.jsonl`)
- **Generation type**: Continuation (non-paraphrastic)
- **Generation parameters**: temperature=0.7, top_p=0.9, max_new_tokens=256, seed=42
- **Depths**: gen-0 through gen-4
- **Parallelization**: 4 shards across RTX 5090 GPUs

#### **Dataset Statistics**
- **Total generated records**: 4,609 (from 995 seeds initially, 5 filtered out)
- **Depth distribution**:
  - Depth 0: 995 records (21.6%) — human (seed)
  - Depth 1: 989 records (21.5%) — first generation
  - Depth 2: 924 records (20.0%)
  - Depth 3: 879 records (19.1%)
  - Depth 4: 822 records (17.8%)
  - Depth attrition: 17.4% (due to "empty input" text generation failures)

#### **Classifier**
- **Type**: XGBoost (gradient boosted trees)
- **Task**: 3-class classification (gen-0/gen-1/gen-2+)
- **Cross-validation**: 5-fold stratified CV on balanced dataset (1:1:1 downsampled)

#### **Key Results**

| Metric | Value | Threshold |
|--------|-------|-----------|
| **Macro-F1** | 0.8408 | ≥ 0.45 ✓ |
| **Binary F1 (gen-0 vs gen-2+)** | 0.8653 | ≥ 0.65 ✓ |
| **CV Macro-F1** | 0.806 ± 0.013 | — |

**Per-class metrics**:
- gen-0: Precision=0.9590, Recall=0.9444, F1=0.9517 (near-perfect separation)
- gen-1: Precision=0.7419, Recall=0.8131, F1=0.7759
- gen-2+: Precision=0.8297, Recall=0.7626, F1=0.7947

**Confusion matrix**: 45 gen-2+ examples misclassified as gen-1 (expected for adjacent classes)

#### **Verdict**: PASS — Both metrics far exceed thresholds

---

### 3. **Feature Importance Findings**

**Critical observation**: hapax_ratio (0.30) and ttr (0.17) dominate feature importance. Combined with entropy_mean (0.22), these three features account for ~69% of total importance.

**Remaining distributional features** (entropy_std, entropy_max, entropy_min, tail_decay) contribute ~31%, with tail_decay being weakest (0.057).

**Key concern identified** (noted in memory.md and decisions.yaml):
- Surface features (hapax_ratio, ttr) are extremely dominant
- **Risk**: These may be masking distributional fingerprint signal OR surface vocabulary impoverishment might be the true depth signal
- This drives the need for **Claim 2 ablation** (plan_001) to test whether reference-model features carry independent signal

---

### 4. **Data Generation Parameters**

From `generate_chain.py`:
- Model cache: `/root/autodl-tmp/models/pythia-2.8b` (local, FP16)
- Tokenizer: Standard transformers AutoTokenizer
- Generation prompt strategy: Takes last 128 tokens of input as prompt, generates 256 new tokens
- Seed reproducibility: torch.manual_seed(42) + torch.cuda.manual_seed(42)
- Input processing: Filtered to min 64 tokens per seed, max 256 tokens
- Fallback dataset: wikitext-103 if Wikipedia streaming fails

---

### 5. **Existing Experiment Plan (experiment_plan.yaml)**

All experiments keyed to three core claims:

**P0 (Priority 0) — Must-run**: 44 GPU·hours total
- **plan_001**: Feature ablation (1h) — (A) reference-only vs (B) surface-only vs (C) full feature set
- **plan_002**: Cross-generator evaluation (20h) — 5 generators × 1000 seeds × 5 depths, leave-one-out CV
- **plan_003**: Cross-family reference models (8h) — OLMo-2-1B, Qwen3.5-0.8B references
- **plan_004**: Downstream utility (15h) — Fine-tune small LM on depth-stratified data, measure perplexity

**P1 (Priority 1) — Story completeness**: 40 GPU·hours
- **plan_005**: Prompt type comparison (10h) — continuation vs elaboration vs inspired rewriting
- **plan_006**: Paraphrastic comparison (8h) — parallel paraphrasing chains vs continuation
- **plan_007**: Cross-model chains (12h) — different generator per depth step
- **plan_008**: Multi-domain seeds (10h) — Wikipedia, news, scientific, creative writing

**P2 (Priority 2) — Nice-to-have**: 23 GPU·hours
- **plan_009-012**: Finer-grained ordinal, human edit robustness, LD-Score feature, end-to-end fine-tuned classifier

**Total budget**: ~107 GPU·hours (within 200 H100-hour limit)

---

### 6. **Dream Simulation Output** (dream_20260514T181213)

A sophisticated imagined-experiments simulation was generated with three tiers characterizing possible outcomes:

**BEST CASE** (Favorable results):
- ref_only macro-F1: 0.76-0.84
- surface_only macro-F1: 0.58-0.68
- cross_gen leave-one-out: 0.74-0.82
- downstream Spearman ρ: 0.60-0.85
- Narrative: Original framing intact, all claims verified, AAAI submission with full scope

**MEDIAN CASE** (Mixed results):
- ref_only macro-F1: 0.66-0.75
- surface_only macro-F1: 0.66-0.76
- cross_gen leave-one-out: 0.62-0.73
- downstream Spearman ρ: 0.35-0.55
- Narrative: Reframe Claim 2 as "complementary signal" not "independent signal," focus on per-generator analysis

**WORST CASE** (Unfavorable results):
- ref_only macro-F1: 0.40-0.55
- surface_only macro-F1: 0.75-0.84
- cross_gen leave-one-out: 0.42-0.58
- downstream Spearman ρ: 0.10-0.30
- Narrative: Surface features explain nearly all variance; reframe as empirical characterization of depth estimation limits; extend attractor cycle theory to non-paraphrastic settings

---

### 7. **Key Files & Artifacts**

**Code**:
- `artifacts/_project/data/generate_chain.py` - data generation script (1000 seeds, Pythia-2.8B, 5 depths)
- Feature extraction and classification scripts referenced in worker logs (not stored locally; executed on AutoDL server)

**Results**:
- `artifacts/mvp-001/data/mvp_results_pointer.txt` - pointer to `/root/gen-depth-fingerprint/results/mvp_results.json` on server
- Worker result JSONs in `logs/workers/` with detailed metrics and confusion matrices

**No existing tier prediction or imagined_experiments files stored locally** — the dream simulation is live in `dream_registry.yaml` (status: imagining)

---

### 8. **Current Status & Next Steps**

**MVP Status**: PASS (2026-05-14 18:08 UTC)

**Immediate priorities** (from ROADMAP.md):
1. Wait for Dream callback → analyze reviewer feedback
2. If Dream approved: activate plan_001 (feature ablation) — uses existing MVP data, no new generation
3. If plan_001 confirms Claim 2: activate plan_002 (cross-generator, requires 4 new models)

**GPU allocation**: 3 GPU·h used (MVP), ~197 GPU·h remaining on autodl-5090

**Venue targets**: AAAI 2027 (primary, Aug 2 deadline) / EMNLP 2026 ARR (stretch, May 25 deadline)

---

This is a well-structured, high-stakes empirical research project with clear hypothesis-testing framing, comprehensive experimental planning, and sophisticated risk characterization through the dream simulation framework.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0043e714-5fcd-444d-ac22-7866d37aa796",
  "isSidechain": false,
  "promptId": "0a119b01-1009-40b6-92ce-4a59605973e6",
  "type": "user",
  "uuid": "7df14a6a-0c2e-4046-a59e-fec90e31dc0d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_3, I need to understand:\n1. The overall file structure (what directories and key files exist)\n2. The MVP experiment details — especially feature importance results from mvp-001, the feature set used, the classifier used, and any existing analysis\n3. Any existing prediction or tier files\n\nSearch broadly: look at the top-level directory, any data/, results/, experiments/, analysis/ directories, and any YAML/JSON/MD files that contain experiment results or feature importance info. Read the most relevant files. Report back with specific details about:\n- Feature importance rankings from MVP (especially hapax_ratio dominance)\n- Exact feature list used\n- Classifier type and hyperparameters\n- Data generation details (models, seeds, depths, domains)\n- Any existing imagined_experiments or tier prediction files",
    "agentId": "aa31f1d2a00bc278f",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I've found the dream output. Let me now compile all the information I've gathered.\n\n## Summary Report: MVP Experiment & Project Overview\n\n### 1. **Project Structure**\n\n**Top-level directory**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`\n\nKey subdirectories:\n- `artifacts/` - output artifacts (MVP scripts, results pointers, dream reports)\n- `logs/workers/` - worker execution logs and results\n- `checkpoints/` - experiment state checkpoints\n- `.claude/sessions/` - agent conversation sessions\n- `docs/IDEA_BRIEF.md` - complete project proposal\n- Configuration files: `experiment_plan.yaml`, `registry.yaml`, `memory.md`, `paper_framing.md`, `decisions.yaml`, `ROADMAP.md`\n\n---\n\n### 2. **MVP-001 Experiment Details** (Completed: 2026-05-14)\n\n#### **Core Hypothesis**\nPythia-410M reference model distributional features (entropy stats, tail-decay, TTR, hapax) can discriminate Pythia-2.8B continuation chains into three depth classes (gen-0/gen-1/gen-2+) with macro-F1 ≥ 0.45.\n\n#### **Feature Set (7 features)**\n1. **hapax_ratio** - proportion of hapax legomena (words appearing once) — dominance importance: 0.3004\n2. **entropy_mean** - mean of next-token log-probability distribution — importance: 0.2202\n3. **ttr** (type-token ratio) — importance: 0.1651\n4. **entropy_std** - variance of next-token distribution — importance: 0.1340\n5. **entropy_max** - maximum of distribution — importance: 0.0650\n6. **entropy_min** - minimum of distribution — importance: 0.0585\n7. **tail_decay** - probability mass beyond 90th/95th percentiles — importance: 0.0569\n\nAll features statistically significant (Kruskal-Wallis + Bonferroni correction, p < 0.001).\n\n#### **Data Generation**\n- **Generator model**: EleutherAI/Pythia-2.8B (FP16)\n- **Reference model**: EleutherAI/Pythia-410M\n- **Dataset**: Wikipedia (1000 seeds, local JSONL: `wiki_seed_1000.jsonl`)\n- **Generation type**: Continuation (non-paraphrastic)\n- **Generation parameters**: temperature=0.7, top_p=0.9, max_new_tokens=256, seed=42\n- **Depths**: gen-0 through gen-4\n- **Parallelization**: 4 shards across RTX 5090 GPUs\n\n#### **Dataset Statistics**\n- **Total generated records**: 4,609 (from 995 seeds initially, 5 filtered out)\n- **Depth distribution**:\n  - Depth 0: 995 records (21.6%) — human (seed)\n  - Depth 1: 989 records (21.5%) — first generation\n  - Depth 2: 924 records (20.0%)\n  - Depth 3: 879 records (19.1%)\n  - Depth 4: 822 records (17.8%)\n  - Depth attrition: 17.4% (due to \"empty input\" text generation failures)\n\n#### **Classifier**\n- **Type**: XGBoost (gradient boosted trees)\n- **Task**: 3-class classification (gen-0/gen-1/gen-2+)\n- **Cross-validation**: 5-fold stratified CV on balanced dataset (1:1:1 downsampled)\n\n#### **Key Results**\n\n| Metric | Value | Threshold |\n|--------|-------|-----------|\n| **Macro-F1** | 0.8408 | ≥ 0.45 ✓ |\n| **Binary F1 (gen-0 vs gen-2+)** | 0.8653 | ≥ 0.65 ✓ |\n| **CV Macro-F1** | 0.806 ± 0.013 | — |\n\n**Per-class metrics**:\n- gen-0: Precision=0.9590, Recall=0.9444, F1=0.9517 (near-perfect separation)\n- gen-1: Precision=0.7419, Recall=0.8131, F1=0.7759\n- gen-2+: Precision=0.8297, Recall=0.7626, F1=0.7947\n\n**Confusion matrix**: 45 gen-2+ examples misclassified as gen-1 (expected for adjacent classes)\n\n#### **Verdict**: PASS — Both metrics far exceed thresholds\n\n---\n\n### 3. **Feature Importance Findings**\n\n**Critical observation**: hapax_ratio (0.30) and ttr (0.17) dominate feature importance. Combined with entropy_mean (0.22), these three features account for ~69% of total importance.\n\n**Remaining distributional features** (entropy_std, entropy_max, entropy_min, tail_decay) contribute ~31%, with tail_decay being weakest (0.057).\n\n**Key concern identified** (noted in memory.md and decisions.yaml):\n- Surface features (hapax_ratio, ttr) are extremely dominant\n- **Risk**: These may be masking distributional fingerprint signal OR surface vocabulary impoverishment might be the true depth signal\n- This drives the need for **Claim 2 ablation** (plan_001) to test whether reference-model features carry independent signal\n\n---\n\n### 4. **Data Generation Parameters**\n\nFrom `generate_chain.py`:\n- Model cache: `/root/autodl-tmp/models/pythia-2.8b` (local, FP16)\n- Tokenizer: Standard transformers AutoTokenizer\n- Generation prompt strategy: Takes last 128 tokens of input as prompt, generates 256 new tokens\n- Seed reproducibility: torch.manual_seed(42) + torch.cuda.manual_seed(42)\n- Input processing: Filtered to min 64 tokens per seed, max 256 tokens\n- Fallback dataset: wikitext-103 if Wikipedia streaming fails\n\n---\n\n### 5. **Existing Experiment Plan (experiment_plan.yaml)**\n\nAll experiments keyed to three core claims:\n\n**P0 (Priority 0) — Must-run**: 44 GPU·hours total\n- **plan_001**: Feature ablation (1h) — (A) reference-only vs (B) surface-only vs (C) full feature set\n- **plan_002**: Cross-generator evaluation (20h) — 5 generators × 1000 seeds × 5 depths, leave-one-out CV\n- **plan_003**: Cross-family reference models (8h) — OLMo-2-1B, Qwen3.5-0.8B references\n- **plan_004**: Downstream utility (15h) — Fine-tune small LM on depth-stratified data, measure perplexity\n\n**P1 (Priority 1) — Story completeness**: 40 GPU·hours\n- **plan_005**: Prompt type comparison (10h) — continuation vs elaboration vs inspired rewriting\n- **plan_006**: Paraphrastic comparison (8h) — parallel paraphrasing chains vs continuation\n- **plan_007**: Cross-model chains (12h) — different generator per depth step\n- **plan_008**: Multi-domain seeds (10h) — Wikipedia, news, scientific, creative writing\n\n**P2 (Priority 2) — Nice-to-have**: 23 GPU·hours\n- **plan_009-012**: Finer-grained ordinal, human edit robustness, LD-Score feature, end-to-end fine-tuned classifier\n\n**Total budget**: ~107 GPU·hours (within 200 H100-hour limit)\n\n---\n\n### 6. **Dream Simulation Output** (dream_20260514T181213)\n\nA sophisticated imagined-experiments simulation was generated with three tiers characterizing possible outcomes:\n\n**BEST CASE** (Favorable results):\n- ref_only macro-F1: 0.76-0.84\n- surface_only macro-F1: 0.58-0.68\n- cross_gen leave-one-out: 0.74-0.82\n- downstream Spearman ρ: 0.60-0.85\n- Narrative: Original framing intact, all claims verified, AAAI submission with full scope\n\n**MEDIAN CASE** (Mixed results):\n- ref_only macro-F1: 0.66-0.75\n- surface_only macro-F1: 0.66-0.76\n- cross_gen leave-one-out: 0.62-0.73\n- downstream Spearman ρ: 0.35-0.55\n- Narrative: Reframe Claim 2 as \"complementary signal\" not \"independent signal,\" focus on per-generator analysis\n\n**WORST CASE** (Unfavorable results):\n- ref_only macro-F1: 0.40-0.55\n- surface_only macro-F1: 0.75-0.84\n- cross_gen leave-one-out: 0.42-0.58\n- downstream Spearman ρ: 0.10-0.30\n- Narrative: Surface features explain nearly all variance; reframe as empirical characterization of depth estimation limits; extend attractor cycle theory to non-paraphrastic settings\n\n---\n\n### 7. **Key Files & Artifacts**\n\n**Code**:\n- `artifacts/_project/data/generate_chain.py` - data generation script (1000 seeds, Pythia-2.8B, 5 depths)\n- Feature extraction and classification scripts referenced in worker logs (not stored locally; executed on AutoDL server)\n\n**Results**:\n- `artifacts/mvp-001/data/mvp_results_pointer.txt` - pointer to `/root/gen-depth-fingerprint/results/mvp_results.json` on server\n- Worker result JSONs in `logs/workers/` with detailed metrics and confusion matrices\n\n**No existing tier prediction or imagined_experiments files stored locally** — the dream simulation is live in `dream_registry.yaml` (status: imagining)\n\n---\n\n### 8. **Current Status & Next Steps**\n\n**MVP Status**: PASS (2026-05-14 18:08 UTC)\n\n**Immediate priorities** (from ROADMAP.md):\n1. Wait for Dream callback → analyze reviewer feedback\n2. If Dream approved: activate plan_001 (feature ablation) — uses existing MVP data, no new generation\n3. If plan_001 confirms Claim 2: activate plan_002 (cross-generator, requires 4 new models)\n\n**GPU allocation**: 3 GPU·h used (MVP), ~197 GPU·h remaining on autodl-5090\n\n**Venue targets**: AAAI 2027 (primary, Aug 2 deadline) / EMNLP 2026 ARR (stretch, May 25 deadline)\n\n---\n\nThis is a well-structured, high-stakes empirical research project with clear hypothesis-testing framing, comprehensive experimental planning, and sophisticated risk characterization through the dream simulation framework."
      }
    ],
    "totalDurationMs": 75677,
    "totalTokens": 67316,
    "totalToolUseCount": 36,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 8924,
      "cache_read_input_tokens": 55661,
      "output_tokens": 2727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8924
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 2727,
          "cache_read_input_tokens": 55661,
          "cache_creation_input_tokens": 8924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8924,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 15,
      "searchCount": 1,
      "bashCount": 20,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "0043e714-5fcd-444d-ac22-7866d37aa796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T18:15:14.347Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the project. Let me construct the detailed best-tier imagined experiments YAML. I need to:

1. Go through each of the 12 planned experiments
2. For each, generate detailed expected results with specific metric values within the "best" tier ranges
3. Provide result_rationale explaining WHY these results would occur under the best-case scenario
4. Include tables, figures descriptions, and analysis

Let me be precise and grounded in the MVP results and the theoretical framing.

Key MVP baselines to anchor predictions:
- MVP macro-F1: 0.8408 (single generator, all features)


- Feature importance shows hapax_ratio dominates at 0.30, with entropy_mean at 0.22 and ttr at 0.17 providing secondary signals
- Per-class performance varies significantly: gen-0 achieves 0.95 F1 while gen-1 and gen-2+ cluster around 0.78-0.79
- Cross-validation stability at 0.806 ± 0.013 suggests robust generalization

For the best-tier scenario, I'm anchoring on the assumption that reference-model features carry dominant independent depth signal, cross-generator generalization holds cleanly, and all three core claims verify without complications.

Now I'm looking at the performance ranges across different experimental plans: reference-only models hit 0.76-0.84 macro F1, surface-only drops to 0.58-0.68, and the full model reaches 0.84-0.9. The reference-minus-surface delta spans 0.1-0.25, confirming the substantial contribution from reference features. Cross-generator leave-one-out maintains 0.74-0.82 macro F1 with individual generator classes ranging 0.68-0.80, while cross-family reference performance sits at 0.7-0.8.

For the depth quality analysis, I'm seeing spearman correlation between 0.6-0.85 and a performance gap of 3-8% when comparing depth filtering versus binary classification. Now I need to construct the full YAML specification across all 12 experiments, starting with plan_001 as the critical feature ablation test for Claim 2—where reference-only features achieve roughly 0.79 macro F1, surface-only around 0.63, the full set reaches 0.87, and the delta between them is approximately 0.16.

The key insight here is that hapax_ratio's dominance in the original MVP was partly an artifact of XGBoost's preference for features with granular splits; the 7-feature model let surface features proxy some distributional signal. When I ablate down to just the reference-model entropy features, they capture the monotonic drift pattern directly since they measure how the generator deviates from the reference distribution's expectations.

For plan_002 with cross-generator validation using leave-one-out across 5 generators, I'm expecting macro F1 around 0.78, with individual generator performance ranging from 0.73 to 0.75—suggesting the distributional drift pattern generalizes across different generators.

The reason this works is that all generators deviate from human text in similar ways as generation depth increases, and since the signal is measured by the reference model rather than generator-specific properties, it's invariant across different generators.

For plan_003, I'm testing whether the phenomenon holds with non-Pythia reference models, expecting macro F1 around 0.75. The underlying distributional drift is a property of the generated text itself, not the reference model architecture—any well-trained language model will assign lower probability to deeper-generation text since they all model human text distribution.

For plan_004, I'm looking at downstream utility with a Spearman correlation around 0.72 and roughly a 5.5-point gap between filter and binary classification approaches.

The key insight for plan_005 is that different prompt types show varying strength of the depth signal—continuation chains preserve it best, elaboration somewhat less, and inspired rewriting the least, though all three should maintain usable signal. For plan_006, I'm checking whether paraphrastic chains exhibit convergence as predicted by attractor theory.

Now looking at the remaining plans: non-paraphrastic chains should show divergence with clear separation between the two modalities. Cross-model chains in plan_007 might be slightly harder to discriminate but still distinguishable. The signal should hold across all four domains in plan_008, degrade monotonically but remain usable with five ordinal classes in plan_009, and show graceful degradation up to 10% edits with steeper decline at 20% in plan_010. LD-Score should provide complementary signal in plan_011, and the fine-tuned model should match or slightly outperform the handcrafted features in plan_012.

Now I'm organizing all these expectations into a comprehensive YAML structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7df14a6a-0c2e-4046-a59e-fec90e31dc0d",
  "isSidechain": false,
  "requestId": "req_011Cb2v7MVNgaeEh4bxvfuxq",
  "type": "assistant",
  "uuid": "10b0be21-deb3-44c6-9863-5aafa47700f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJtZSTU2dZxZyxNDkrusGT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3060,
      "cache_read_input_tokens": 21242,
      "output_tokens": 14856,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14856,
          "cache_read_input_tokens": 21242,
          "cache_creation_input_tokens": 3060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3060
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

_source line 13 · 2026-05-14T18:19:15.435Z_

```yaml
tier: best
narrative_guidance: >
  Original framing fully intact. Story: non-paraphrastic chains exhibit monotonic
  distributional divergence (H₂ confirmed), detectable via reference-model entropy
  features that capture drift beyond surface vocabulary impoverishment. Headline:
  "distributional fingerprints enable risk-stratified data curation," with clean
  ablation separating signal from shortcut. All three claims stated at full strength.
  AAAI submission with no scope reduction.

imagined_experiments:
  - name: feature_ablation
    plan_id: plan_001
    description: >
      Ablation on existing MVP data (4609 records, Pythia-2.8B generator, Pythia-410M
      reference, Wikipedia seeds). Three conditions: (A) reference-only features
      (entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay), (B) surface-only
      features (ttr, hapax_ratio), (C) full 7-feature set. Same XGBoost classifier,
      5-fold stratified CV, 3-class (gen-0/gen-1/gen-2+).
    expected_results:
      ref_only_macro_f1: 0.79
      ref_only_cv_std: 0.018
      ref_only_gen0_f1: 0.91
      ref_only_gen1_f1: 0.71
      ref_only_gen2plus_f1: 0.74
      surface_only_macro_f1: 0.63
      surface_only_cv_std: 0.022
      surface_only_gen0_f1: 0.82
      surface_only_gen1_f1: 0.52
      surface_only_gen2plus_f1: 0.55
      full_macro_f1: 0.87
      full_cv_std: 0.012
      full_gen0_f1: 0.96
      full_gen1_f1: 0.81
      full_gen2plus_f1: 0.83
      ref_minus_surface_delta: 0.16
      mcnemar_p_ref_vs_surface: 0.00003
      permutation_importance_entropy_mean: 0.28
      permutation_importance_entropy_std: 0.19
      permutation_importance_hapax_ratio: 0.14
      permutation_importance_ttr: 0.09
    result_rationale: >
      MVP feature importance (hapax_ratio=0.30) was inflated by XGBoost's split-gain
      metric, which overweights high-cardinality continuous features with many useful
      split points. When surface features are ablated, the 5 reference-model features
      retain macro-F1=0.79 because they directly measure the generator's deviation
      from the reference model's next-token distribution — a signal that accumulates
      monotonically with depth as the generator's output drifts further from human
      text. Entropy_mean captures the average surprise under the reference model
      (increases with depth as generated text occupies lower-probability regions),
      while entropy_std captures the increasing variance of surprise (deeper text
      alternates between familiar patterns and novel drift). Surface features alone
      (F1=0.63) capture only vocabulary impoverishment — TTR and hapax_ratio decline
      with depth as generators recycle high-frequency tokens — but this is a weaker,
      noisier proxy. The 0.16 delta and significant McNemar test confirm reference
      features carry independent, dominant signal. The full set achieves F1=0.87
      (up from MVP's 0.84) because retuned hyperparameters on the same data with
      proper ablation awareness extract slightly more complementary value. Permutation
      importance (which avoids split-gain bias) reranks entropy_mean as the top feature.
    tables:
      - name: "Table 1: Feature Ablation Results (3-class depth classification)"
        columns: ["Feature Set", "Features", "Macro-F1", "gen-0 F1", "gen-1 F1", "gen-2+ F1", "CV std"]
        rows:
          - ["Reference-only", "entropy_{mean,std,min,max}, tail_decay", 0.79, 0.91, 0.71, 0.74, 0.018]
          - ["Surface-only", "ttr, hapax_ratio", 0.63, 0.82, 0.52, 0.55, 0.022]
          - ["Full", "All 7 features", 0.87, 0.96, 0.81, 0.83, 0.012]
          - ["Δ (ref − surface)", "—", "+0.16", "+0.09", "+0.19", "+0.19", "—"]
      - name: "Table 2: Permutation Importance (Full model, 5-fold mean)"
        columns: ["Feature", "Permutation Importance", "XGBoost Gain (MVP)"]
        rows:
          - ["entropy_mean", 0.28, 0.22]
          - ["entropy_std", 0.19, 0.13]
          - ["hapax_ratio", 0.14, 0.30]
          - ["tail_decay", 0.13, 0.06]
          - ["ttr", 0.09, 0.17]
          - ["entropy_max", 0.09, 0.07]
          - ["entropy_min", 0.08, 0.06]
    figures_description:
      - "Fig 1a: Grouped bar chart — Macro-F1 for ref-only / surface-only / full, with 95% CI error bars from CV. Clear visual gap between ref-only and surface-only."
      - "Fig 1b: Per-class F1 heatmap (3 feature sets × 3 classes). Shows that the surface→ref gap is largest for gen-1 and gen-2+ (the harder classes), confirming reference features add discriminability precisely where surface shortcuts fail."
      - "Fig 1c: Permutation importance bar chart (full model) vs XGBoost gain bar chart (MVP). Side-by-side comparison reveals hapax_ratio's gain was inflated; entropy_mean is the true top feature under permutation."
    analysis: >
      The ablation cleanly validates Claim 2. The ref-only advantage is strongest
      on gen-1 (Δ=+0.19) and gen-2+ (Δ=+0.19), the classes where surface features
      struggle most — TTR/hapax can separate human text from any synthetic text
      but cannot distinguish depth levels within synthetic text, because vocabulary
      impoverishment saturates quickly (mostly between gen-0→gen-1). Reference-model
      entropy features, by contrast, capture cumulative distributional drift that
      continues to grow between gen-1 and gen-2+. The reranking of feature importance
      under permutation (entropy_mean rises to 0.28, hapax_ratio drops to 0.14)
      directly addresses RC1 ("Is this just vocabulary impoverishment?") — it is not.
      The full model's improvement to 0.87 suggests the two feature families capture
      partially orthogonal information: surface features provide a cheap gen-0 vs
      rest shortcut, while reference features provide the finer gen-1 vs gen-2+ signal.

  - name: cross_generator_evaluation
    plan_id: plan_002
    description: >
      Generate 25K chains: 1000 Wikipedia seeds × 5 generators (Pythia-2.8B, OLMo-2-1B,
      Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B) × 5 depths. Feature extraction with
      Pythia-410M reference model. Leave-one-generator-out CV (train on 4 generators,
      test on held-out generator). Also report per-generator in-distribution results
      and per-class breakdowns.
    expected_results:
      leave_one_out_macro_f1_mean: 0.78
      leave_one_out_macro_f1_std: 0.03
      leave_one_out_gen1_f1_mean: 0.73
      leave_one_out_gen2plus_f1_mean: 0.75
      leave_one_out_gen0_f1_mean: 0.88
      in_distribution_5fold_macro_f1: 0.86
      per_generator_held_out:
        pythia_2_8b: 0.81
        olmo_2_1b: 0.77
        qwen3_5_2b: 0.76
        qwen3_5_0_8b: 0.74
        pythia_1b: 0.82
      total_chains_generated: 24200
      attrition_rate_pct: 3.2
      generation_gpu_hours: 18.5
    result_rationale: >
      Cross-generator generalization holds (mean leave-one-out F1=0.78) because
      distributional drift is measured from the reference model's perspective, not
      the generator's. All generators produce text that progressively deviates from
      human text distribution as measured by Pythia-410M; the drift trajectory differs
      in magnitude but shares the same directional pattern (entropy increases,
      tail probability mass shifts). Pythia-family generators (2.8B, 1B) transfer
      best to each other (F1=0.81–0.82) due to shared pretraining distribution.
      Qwen3.5-0.8B is the hardest held-out case (F1=0.74) because its smaller
      capacity produces qualitatively different text that drifts faster at early
      depths — the classifier trained on larger models underestimates Qwen-0.8B's
      depth. The gen-1 vs gen-2+ boundary remains the bottleneck (gen-1 F1=0.73)
      because gen-1 text from some generators overlaps with gen-2+ text from others
      in feature space. In-distribution pooled performance (0.86) is close to MVP
      (0.84) despite mixing generators, confirming that generator diversity adds
      training signal rather than noise. Attrition (~3.2%) is lower than MVP (3.7%)
      due to improved generation pipeline with retry logic.
    tables:
      - name: "Table 3: Leave-One-Generator-Out Cross-Validation"
        columns: ["Held-out Generator", "Macro-F1", "gen-0 F1", "gen-1 F1", "gen-2+ F1"]
        rows:
          - ["Pythia-2.8B", 0.81, 0.91, 0.75, 0.77]
          - ["OLMo-2-1B", 0.77, 0.87, 0.72, 0.73]
          - ["Qwen3.5-2B", 0.76, 0.86, 0.71, 0.72]
          - ["Qwen3.5-0.8B", 0.74, 0.84, 0.68, 0.70]
          - ["Pythia-1B", 0.82, 0.92, 0.76, 0.78]
          - ["Mean ± std", "0.78 ± 0.03", "0.88 ± 0.03", "0.73 ± 0.03", "0.75 ± 0.03"]
      - name: "Table 4: Per-Generator In-Distribution 5-Fold CV"
        columns: ["Generator", "Macro-F1", "CV std"]
        rows:
          - ["Pythia-2.8B", 0.85, 0.014]
          - ["OLMo-2-1B", 0.84, 0.016]
          - ["Qwen3.5-2B", 0.86, 0.013]
          - ["Qwen3.5-0.8B", 0.83, 0.019]
          - ["Pythia-1B", 0.84, 0.015]
          - ["Pooled (all 5)", 0.86, 0.011]
    figures_description:
      - "Fig 2a: Leave-one-out macro-F1 bar chart with error bars, generators ordered by held-out performance. Horizontal dashed line at 0.78 (mean). Shows Pythia-family clusters above mean, Qwen-0.8B below."
      - "Fig 2b: Confusion matrix heatmaps (5 panels, one per held-out generator). Highlights that gen-1↔gen-2+ confusion is the primary failure mode across all generators."
      - "Fig 2c: t-SNE of reference-model features colored by depth, faceted by generator. Shows that depth clusters are geometrically similar across generators despite generator-specific offsets in feature space."
    analysis: >
      The 0.78 mean leave-one-out F1 with narrow std (0.03) strongly supports
      Claim 1's cross-generator generalization. The pattern is consistent: gen-0
      is always well-separated (F1≥0.84), while gen-1 and gen-2+ form a harder
      boundary. Pythia-family transfer is strongest, suggesting some same-family
      distributional similarity, but even cross-family transfer (Pythia→Qwen)
      maintains F1≥0.74. This confirms the distributional fingerprint is a property
      of the generation process, not a generator-specific artifact. The pooled
      in-distribution result (0.86) exceeding any single-generator result suggests
      that multi-generator training improves robustness. For the paper, this table
      is the centerpiece of Claim 1 and directly addresses RC2.

  - name: cross_family_reference_model
    plan_id: plan_003
    description: >
      Re-extract features using non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B)
      on the plan_002 dataset (25K chains). Compare classification performance across
      3 reference model families. Tests whether the fingerprint is reference-model-agnostic.
    expected_results:
      pythia_410m_ref_macro_f1: 0.86
      olmo_2_1b_ref_macro_f1: 0.76
      qwen3_5_0_8b_ref_macro_f1: 0.74
      ensemble_3refs_macro_f1: 0.88
      cross_ref_leave_one_out_macro_f1: 0.75
      feature_correlation_pythia_olmo_entropy_mean: 0.82
      feature_correlation_pythia_qwen_entropy_mean: 0.78
    result_rationale: >
      All three reference models detect depth signal (F1≥0.74) because any well-trained
      LM assigns progressively lower probability to deeper-generation text — the
      drift is a property of the text, not the measuring instrument. Pythia-410M
      performs best (0.86) because it was the reference model used during pipeline
      development and its capacity is calibrated for sensitivity to distributional
      shifts (small enough to be "surprised" by drift, large enough to model human
      text well). OLMo-2-1B (0.76) and Qwen3.5-0.8B (0.74) are slightly weaker
      because their different pretraining distributions create different baselines
      for "expected" text, adding noise to depth features. High cross-reference
      entropy_mean correlations (0.78–0.82) confirm that all three models agree on
      the direction of drift even if magnitudes differ. The 3-reference ensemble
      (0.88) exceeds any single reference, indicating that diverse reference models
      capture complementary aspects of distributional drift. This decisively addresses
      RC2 — the signal is not a Pythia-specific artifact.
    tables:
      - name: "Table 5: Reference Model Comparison (pooled 5-generator data)"
        columns: ["Reference Model", "Family", "Params", "Macro-F1", "gen-0 F1", "gen-1 F1", "gen-2+ F1"]
        rows:
          - ["Pythia-410M", "Pythia", "410M", 0.86, 0.95, 0.80, 0.82]
          - ["OLMo-2-1B", "OLMo", "1B", 0.76, 0.88, 0.69, 0.72]
          - ["Qwen3.5-0.8B", "Qwen", "0.8B", 0.74, 0.86, 0.66, 0.70]
          - ["Ensemble (3 refs)", "Mixed", "—", 0.88, 0.96, 0.83, 0.85]
      - name: "Table 6: Pairwise Feature Correlation (Spearman ρ) Across Reference Models"
        columns: ["Feature", "Pythia↔OLMo", "Pythia↔Qwen", "OLMo↔Qwen"]
        rows:
          - ["entropy_mean", 0.82, 0.78, 0.80]
          - ["entropy_std", 0.79, 0.74, 0.76]
          - ["tail_decay", 0.71, 0.66, 0.69]
    figures_description:
      - "Fig 3a: Parallel coordinates plot showing entropy_mean distributions by depth, one panel per reference model. Monotonic increase with depth visible in all three, confirming H₂ across reference architectures."
      - "Fig 3b: Scatter matrix of entropy_mean values across reference model pairs, colored by depth. Strong positive correlation with depth-dependent clustering confirms cross-reference consistency."
    analysis: >
      The cross-family validation eliminates the concern that Pythia-410M has some
      idiosyncratic sensitivity to synthetic text. All three reference architectures
      detect monotonic distributional drift. The ensemble's improvement to 0.88
      provides an optional "best-effort" configuration for practitioners, though
      the single-reference Pythia-410M result (0.86) is sufficient for the paper's
      claims. The correlation analysis (Table 6) is particularly informative: high
      but imperfect correlations indicate that reference models measure the same
      underlying phenomenon through slightly different lenses, explaining why
      ensembling helps. For the paper, this experiment transforms a potential weakness
      (Pythia-only evaluation) into a strength (reference-model-agnostic signal).

  - name: downstream_utility
    plan_id: plan_004
    description: >
      Fine-tune Pythia-410M on depth-stratified subsets of the plan_002 data. Measure
      perplexity on held-out human test set as function of training data depth
      composition. Compare depth-aware filtering (keep gen-0 + gen-1, discard gen-2+)
      vs binary baselines (FastDetectGPT threshold, LD-Score threshold) for preserving
      downstream model quality.
    expected_results:
      depth_quality_spearman_rho: 0.72
      ppl_gen0_only: 28.3
      ppl_gen1_only: 30.1
      ppl_gen2_only: 34.7
      ppl_gen3_only: 38.9
      ppl_gen4_only: 43.2
      ppl_mixed_uniform: 35.8
      ppl_depth_filtered_gen01: 29.0
      ppl_binary_fastdetectgpt: 31.8
      ppl_binary_ldscore: 32.1
      ppl_human_baseline: 27.5
      depth_filter_vs_binary_gap_pct: 5.2
      training_samples_kept_depth_filter: 0.42
      training_samples_kept_binary: 0.28
    result_rationale: >
      Perplexity increases monotonically with training data depth (28.3→43.2 from
      gen-0→gen-4) because deeper-generation text has compounded distributional
      drift from human text — fine-tuning on it shifts the model's learned distribution
      away from the human test set. The Spearman ρ=0.72 between depth and perplexity
      is strong but not perfect because individual samples vary in drift magnitude
      (some gen-3 texts are less drifted than some gen-2 texts). Depth-aware filtering
      (keep gen-0+gen-1, perplexity=29.0) outperforms binary baselines (~31.8–32.1)
      by 5.2% because binary detectors discard all synthetic text including useful
      gen-1 content that is distributionally close to human text. Binary filtering
      retains only 28% of data (mostly gen-0) while depth filtering retains 42%
      (gen-0 + gen-1), providing more training data of acceptable quality. The gap
      between gen-0-only (28.3) and depth-filtered (29.0) is small, confirming that
      gen-1 text is nearly as good as human text for training — the key practical
      insight for data curation.
    tables:
      - name: "Table 7: Fine-tuning Perplexity by Training Data Depth"
        columns: ["Training Data", "Depth Composition", "PPL (↓)", "Samples Used"]
        rows:
          - ["Human-only", "gen-0", 28.3, "~4800"]
          - ["gen-1 only", "gen-1", 30.1, "~4750"]
          - ["gen-2 only", "gen-2", 34.7, "~4500"]
          - ["gen-3 only", "gen-3", 38.9, "~4200"]
          - ["gen-4 only", "gen-4", 43.2, "~3900"]
          - ["Uniform mix", "gen-0–4 equal", 35.8, "~22000"]
          - ["Depth-filtered (ours)", "gen-0 + gen-1", 29.0, "~9500"]
          - ["FastDetectGPT filter", "binary threshold", 31.8, "~6300"]
          - ["LD-Score filter", "binary threshold", 32.1, "~6100"]
          - ["Human test baseline", "—", 27.5, "—"]
      - name: "Table 8: Depth-Aware vs Binary Filtering Comparison"
        columns: ["Method", "PPL", "Data Retained (%)", "PPL Gap to Human-Only"]
        rows:
          - ["Depth-filtered (gen-0+1)", 29.0, "42%", "+0.7"]
          - ["FastDetectGPT binary", 31.8, "28%", "+3.5"]
          - ["LD-Score binary", 32.1, "26%", "+3.8"]
          - ["No filtering (all data)", 35.8, "100%", "+7.5"]
    figures_description:
      - "Fig 4a: Line plot — perplexity vs generation depth (gen-0 through gen-4). Monotonic increase with 95% CI bands from 3 random seeds. Confirms H₂'s downstream consequence."
      - "Fig 4b: Bar chart comparing filtering strategies (depth-aware, FastDetectGPT, LD-Score, no filter) on perplexity and data retention. Dual y-axis: bars for perplexity, overlaid line for % data retained."
      - "Fig 4c: Scatter plot — predicted depth score vs actual fine-tuning perplexity contribution per sample, with Spearman ρ annotation. Shows the sample-level correlation between depth estimate and quality impact."
    analysis: >
      This experiment validates Claim 3 and provides the practical punchline of the
      paper. The monotonic perplexity curve (Fig 4a) is the most intuitive
      visualization of H₂ — it translates distributional drift into a metric
      practitioners care about. The 5.2% gap between depth-aware and binary filtering
      is meaningful because it comes with MORE data retained (42% vs 28%), resolving
      the precision-recall tradeoff that plagues binary detection. The key insight
      is that gen-1 text is "good enough" for training (PPL=30.1 vs human 28.3),
      but gen-2+ is not (PPL≥34.7). Binary detectors cannot make this distinction.
      For AAAI reviewers, this experiment connects the theoretical contribution
      (distributional drift characterization) to a practical application (data
      curation), which is important for venue fit.

  - name: prompt_type_comparison
    plan_id: plan_005
    description: >
      Generate chains with 3 prompt types (continuation, elaboration, inspired_rewriting)
      using Pythia-2.8B on 1000 Wikipedia seeds × 5 depths. Compare depth signal
      preservation across prompt types. Tests whether semantic divergence from source
      correlates with depth signal.
    expected_results:
      continuation_macro_f1: 0.85
      elaboration_macro_f1: 0.80
      inspired_rewriting_macro_f1: 0.72
      continuation_entropy_drift_per_depth: 0.18
      elaboration_entropy_drift_per_depth: 0.14
      inspired_rewriting_entropy_drift_per_depth: 0.10
      cross_prompt_train_test_macro_f1: 0.74
      prompt_type_drift_rate_spearman: 0.91
    result_rationale: >
      Continuation preserves the strongest depth signal (F1=0.85) because each
      generation step continues directly from the previous output, maximizing the
      accumulation of distributional drift. Elaboration (F1=0.80) injects some
      new semantic direction via the prompt instruction, which partially resets
      the drift trajectory at each step — drift still accumulates but at a slower
      rate. Inspired rewriting (F1=0.72) has the most semantic freedom: the model
      is instructed to produce text "inspired by" the input, allowing it to diverge
      from the drift trajectory and partially re-anchor to its pretraining
      distribution. The strong correlation between per-depth entropy drift rate
      and classification F1 (Spearman ρ=0.91) confirms the theoretical prediction:
      more constrained generation → faster drift accumulation → stronger depth
      signal. Cross-prompt-type transfer (F1=0.74) is moderate, indicating that
      the drift signature is partially shared across prompt types but the rate
      differences create distribution shift in feature space.
    tables:
      - name: "Table 9: Depth Classification by Prompt Type"
        columns: ["Prompt Type", "Macro-F1", "gen-0 F1", "gen-1 F1", "gen-2+ F1", "Entropy Drift Rate"]
        rows:
          - ["Continuation", 0.85, 0.95, 0.79, 0.81, "0.18 nats/depth"]
          - ["Elaboration", 0.80, 0.92, 0.73, 0.75, "0.14 nats/depth"]
          - ["Inspired rewriting", 0.72, 0.86, 0.64, 0.67, "0.10 nats/depth"]
    figures_description:
      - "Fig 5a: Line plots — entropy_mean vs depth for each prompt type, showing different drift rates. Continuation has steepest slope."
      - "Fig 5b: Scatter plot — prompt type drift rate vs macro-F1, confirming linear relationship. Three points with regression line and ρ annotation."
    analysis: >
      This experiment decomposes the depth signal by generation modality. The ordering
      (continuation > elaboration > inspired rewriting) aligns with the theoretical
      framework: the more the generation task constrains the output to build on
      previous text, the more drift accumulates. Inspired rewriting's lower F1
      is not a failure — it confirms the mechanism. For the paper, this comparison
      strengthens the theoretical story by showing that depth signal is graded,
      not binary, and correlates with the degree of semantic coupling between
      successive generation steps.

  - name: paraphrastic_comparison
    plan_id: plan_006
    description: >
      Construct parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B, 5 depths)
      alongside continuation chains. Measure whether paraphrastic chains converge
      (per attractor theory) while continuation chains diverge (our H₂). Direct
      empirical test of H₁ vs H₂.
    expected_results:
      paraphrase_macro_f1_3class: 0.58
      paraphrase_gen0_f1: 0.81
      paraphrase_gen1_f1: 0.46
      paraphrase_gen2plus_f1: 0.47
      continuation_macro_f1_3class: 0.85
      paraphrase_entropy_drift_depth3: 0.06
      continuation_entropy_drift_depth3: 0.52
      paraphrase_cycle_detection_pct: 68.0
      divergence_test_ks_statistic: 0.41
      divergence_test_p_value: 0.00001
    result_rationale: >
      Paraphrastic chains show weak depth signal (F1=0.58) because the semantic
      preservation constraint of paraphrasing creates attractor dynamics — the text
      oscillates around a fixed semantic point, and distributional features converge
      after ~2 steps (confirming ACL 2025 attractor cycle theory). By depth 3,
      paraphrastic entropy drift has nearly plateaued (0.06 nats) while continuation
      drift continues growing (0.52 nats). The 68% cycle detection rate in
      paraphrastic chains (text at depth d is more similar to depth d-2 than d-1)
      directly corroborates the 2-period attractor cycle prediction. Continuation
      chains show no such periodicity — drift is monotonic. The KS test between
      depth-3 entropy distributions of paraphrastic vs continuation chains (D=0.41,
      p<0.001) provides the statistical test of H₁ vs H₂. This is the most
      theoretically clean result in the paper: H₂ (divergence) holds for
      non-paraphrastic chains, H₁ (convergence) holds for paraphrastic chains,
      exactly as predicted by the semantic constraint difference.
    tables:
      - name: "Table 10: Paraphrastic vs Continuation Chain Comparison"
        columns: ["Chain Type", "Macro-F1", "Entropy Drift @depth3", "Cycle Detection %"]
        rows:
          - ["Continuation", 0.85, "0.52 nats", "< 5%"]
          - ["Paraphrasing", 0.58, "0.06 nats", "68%"]
          - ["Δ", "+0.27", "+0.46 nats", "—"]
    figures_description:
      - "Fig 6a: Dual-panel line plot — entropy_mean vs depth for continuation (diverging) and paraphrasing (converging). The visual contrast is the paper's most compelling figure."
      - "Fig 6b: Autocorrelation plot of entropy_mean sequence across depths for paraphrastic chains, showing the period-2 oscillation pattern predicted by attractor theory."
    analysis: >
      This is the experiment that elevates the paper from "a depth classifier" to
      "an empirical test of distributional dynamics in recursive generation." The
      clean separation between convergent (paraphrastic) and divergent (non-paraphrastic)
      chains validates the core theoretical insight and connects our work to the
      ACL 2025 attractor cycle literature. H₂ is confirmed for non-paraphrastic
      chains: drift accumulates monotonically, enabling depth estimation. H₁ is
      confirmed for paraphrastic chains: convergence limits depth signal to ~2 classes.
      This dual result explains WHY our approach works and WHY prior work on
      paraphrasing chains found limited depth discriminability.

  - name: cross_model_chains
    plan_id: plan_007
    description: >
      Generate cross-model chains where each depth step uses a different generator
      (randomly sampled from the 5 generators). 1000 seeds × 5 depths. Compares
      cross-model chain depth classification to single-model chains. More realistic
      scenario — real web contamination involves diverse generators.
    expected_results:
      cross_model_chain_macro_f1: 0.75
      single_model_chain_macro_f1_mean: 0.85
      cross_model_gen0_f1: 0.90
      cross_model_gen1_f1: 0.68
      cross_model_gen2plus_f1: 0.67
      cross_model_entropy_drift_per_depth: 0.13
      cross_vs_single_model_delta: -0.10
    result_rationale: >
      Cross-model chains are harder to classify (F1=0.75 vs single-model 0.85)
      because generator switching introduces distributional discontinuities — each
      new generator has its own distributional signature that partially masks the
      monotonic drift signal. However, F1=0.75 is still well above chance (0.33)
      and practically useful, because the underlying drift phenomenon persists: even
      when generators change, the cumulative deviation from human text distribution
      still increases with depth. The gen-1 and gen-2+ classes are most affected
      (F1=0.68, 0.67) because generator-switching noise is most confusing for the
      middle classes. Gen-0 remains well-separated (F1=0.90) because human text is
      fundamentally different from any generator's output. The 10-point drop from
      single-model is a known cost that should be reported transparently — it
      bounds the method's real-world applicability but does not invalidate the
      approach. Entropy drift rate (0.13 nats/depth) is lower than single-model
      continuation (0.18) because generator transitions partially reset drift.
    tables:
      - name: "Table 11: Single-Model vs Cross-Model Chain Comparison"
        columns: ["Chain Type", "Macro-F1", "gen-0 F1", "gen-1 F1", "gen-2+ F1"]
        rows:
          - ["Single-model (mean of 5)", 0.85, 0.95, 0.79, 0.81]
          - ["Cross-model (random switch)", 0.75, 0.90, 0.68, 0.67]
          - ["Δ", "-0.10", "-0.05", "-0.11", "-0.14"]
    figures_description:
      - "Fig 7: Box plot of entropy_mean by depth for cross-model chains. Wider boxes than single-model chains reflect generator-switching variance, but median still increases monotonically."
    analysis: >
      The 10-point F1 drop is the honest cost of ecological validity. Reviewers
      (RC4) will ask about this — reporting it transparently strengthens the paper.
      The key takeaway is that depth signal survives cross-model chains despite
      generator-switching noise, maintaining F1=0.75. For practical data curation,
      this means depth-aware filtering still provides value even when contamination
      sources are diverse. The fact that gen-0 F1 remains at 0.90 means the method's
      primary utility (separating human from any-depth synthetic) is robust; the
      finer-grained depth estimation within synthetic text is where accuracy degrades.

  - name: multi_domain_seeds
    plan_id: plan_008
    description: >
      Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC
      abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5
      generators × 5 depths. Tests domain generalization of depth signal.
    expected_results:
      wikipedia_macro_f1: 0.86
      news_macro_f1: 0.83
      scientific_macro_f1: 0.81
      creative_macro_f1: 0.78
      cross_domain_leave_one_out_f1: 0.77
      pooled_all_domains_f1: 0.84
      domain_variance_of_f1: 0.0009
    result_rationale: >
      Wikipedia performs best (0.86) because it matches the MVP setting and has the
      most structured, information-dense text that generators struggle to faithfully
      continue. News is close (0.83) due to similar factual density. Scientific
      text (0.81) has domain-specific vocabulary that somewhat masks depth drift
      in surface features, but reference-model features still capture the signal.
      Creative writing is hardest (0.78) because generators produce more fluent,
      human-like creative text — the distributional gap between human and generated
      creative writing is smaller than for factual domains, reducing the overall
      drift magnitude. Cross-domain leave-one-out (0.77) confirms that the depth
      signal generalizes across domains, though some domain-specific calibration
      is lost. The low variance (0.0009) across domains indicates that depth signal
      is a robust, domain-general phenomenon. Pooled performance (0.84) suggests
      that multi-domain training is beneficial — diverse training data helps the
      classifier learn domain-invariant depth features.
    tables:
      - name: "Table 12: Multi-Domain Depth Classification"
        columns: ["Domain", "Seeds", "Macro-F1", "gen-0 F1", "gen-1 F1", "gen-2+ F1"]
        rows:
          - ["Wikipedia", 500, 0.86, 0.95, 0.80, 0.82]
          - ["News", 500, 0.83, 0.93, 0.77, 0.79]
          - ["Scientific", 500, 0.81, 0.91, 0.74, 0.77]
          - ["Creative", 500, 0.78, 0.88, 0.71, 0.74]
          - ["Pooled (all)", 2000, 0.84, 0.93, 0.78, 0.80]
          - ["Leave-one-domain-out", "—", 0.77, 0.88, 0.70, 0.73]
    figures_description:
      - "Fig 8: Faceted violin plot of entropy_mean by depth, one panel per domain. All domains show monotonic drift but with different baseline offsets and drift rates."
    analysis: >
      Domain generalization confirms that distributional drift is not an artifact of
      Wikipedia-style text. The ordering (factual > creative) is interpretable and
      provides nuance for practitioners: depth estimation is most reliable for
      factual domains where generators have clear distributional signatures. The
      cross-domain leave-one-out result (0.77) is strong enough to claim domain
      generalization in the paper. For AAAI, including 4 domains in the evaluation
      addresses RC6 and demonstrates ecological validity.

  - name: finer_grained_ordinal
    plan_id: plan_009
    description: >
      5-class ordinal classification (gen-0 through gen-4) on the plan_002 data.
      Tests whether non-paraphrastic chains support finer-grained depth estimation
      beyond the 3-class setup.
    expected_results:
      ordinal_5class_macro_f1: 0.62
      ordinal_5class_gen0_f1: 0.92
      ordinal_5class_gen1_f1: 0.68
      ordinal_5class_gen2_f1: 0.52
      ordinal_5class_gen3_f1: 0.48
      ordinal_5class_gen4_f1: 0.51
      ordinal_mae: 0.58
      ordinal_spearman_rho: 0.83
      adjacent_class_confusion_pct: 72.0
    result_rationale: >
      5-class F1 (0.62) is lower than 3-class (0.86) because deeper classes
      (gen-2/gen-3/gen-4) have progressively overlapping feature distributions —
      drift accumulates but with diminishing marginal signal per step. Gen-0 remains
      easy (F1=0.92), gen-1 is moderate (F1=0.68), and gen-2/3/4 are difficult
      (F1≈0.48–0.52) because the distributional differences between adjacent deep
      classes are small. However, the high Spearman ρ (0.83) and low MAE (0.58)
      indicate that the classifier's errors are ordinal — when it misclassifies,
      it predicts an adjacent class (72% of errors are off-by-one), not a distant
      one. This supports ordinal regression as a natural formulation and suggests
      that while exact depth prediction is noisy for deep classes, the relative
      ordering is preserved. For the paper, this result supports the claim that
      drift is monotonic (H₂) while honestly reporting the practical ceiling on
      depth resolution.
    tables:
      - name: "Table 13: 5-Class Ordinal Depth Classification"
        columns: ["Class", "Precision", "Recall", "F1"]
        rows:
          - ["gen-0", 0.93, 0.91, 0.92]
          - ["gen-1", 0.66, 0.70, 0.68]
          - ["gen-2", 0.50, 0.54, 0.52]
          - ["gen-3", 0.47, 0.49, 0.48]
          - ["gen-4", 0.53, 0.50, 0.51]
          - ["Macro", "—", "—", 0.62]
      - name: "Table 13b: Ordinal Error Analysis"
        columns: ["Metric", "Value"]
        rows:
          - ["MAE", 0.58]
          - ["Spearman ρ (pred vs true depth)", 0.83]
          - ["Adjacent-class confusion (%)", "72%"]
    figures_description:
      - "Fig 9a: 5×5 confusion matrix heatmap. Diagonal + adjacent-diagonal cells are dark, confirming ordinal error structure."
      - "Fig 9b: Predicted depth (box plot) vs true depth. Boxes overlap for gen-2/3/4 but medians increase monotonically."
    analysis: >
      The 5-class result characterizes the resolution ceiling of distributional
      fingerprints. While exact depth-4 vs depth-3 discrimination is weak, the
      ordinal structure is strong (ρ=0.83). This has practical implications: for
      data curation, coarse depth buckets (gen-0 / gen-1 / gen-2+) are more useful
      than exact depth anyway — the key decision boundary is "how much drift is
      tolerable." The result also differentiates our work from attractor theory:
      paraphrastic chains converge to ~2 distinguishable classes, while our
      non-paraphrastic chains support at least 3 clean classes and 5 ordinal classes.
      This directly addresses RC3.

  - name: human_edit_robustness
    plan_id: plan_010
    description: >
      Robustness test on plan_002 data with simulated edits: (A) random word
      replacement at 5%, 10%, 20% rates, (B) LLM-simulated light editing (rephrase
      random sentences). Tests depth signal persistence under post-generation editing.
    expected_results:
      no_edit_macro_f1: 0.86
      random_5pct_macro_f1: 0.83
      random_10pct_macro_f1: 0.78
      random_20pct_macro_f1: 0.67
      llm_light_edit_macro_f1: 0.76
      degradation_slope_per_10pct: -0.095
    result_rationale: >
      Random word replacement at 5% has minimal impact (F1=0.83, Δ=-0.03) because
      replacing 5% of tokens introduces noise uniformly across all depth classes,
      preserving the relative distributional differences. At 10% (F1=0.78), the
      noise begins to mask depth-specific features — entropy statistics become
      noisier as random words inject unpredictable surprise values. At 20% (F1=0.67),
      substantial text corruption disrupts the distributional fingerprint significantly
      but performance remains above chance (0.33). LLM-simulated editing (F1=0.76)
      is comparable to 10% random replacement because light rephrasing changes
      surface statistics but largely preserves the underlying distributional
      structure — the edited text still occupies the same region of reference-model
      feature space. The degradation is approximately linear (-0.095 F1 per 10%
      edit rate), providing a simple model for practitioners to assess signal
      reliability given estimated editing rates. These results address RC5 while
      honestly reporting the method's sensitivity to post-generation modification.
    tables:
      - name: "Table 14: Robustness to Simulated Edits"
        columns: ["Edit Type", "Edit Rate", "Macro-F1", "Δ from No-Edit"]
        rows:
          - ["None (baseline)", "0%", 0.86, "—"]
          - ["Random word replacement", "5%", 0.83, "-0.03"]
          - ["Random word replacement", "10%", 0.78, "-0.08"]
          - ["Random word replacement", "20%", 0.67, "-0.19"]
          - ["LLM light editing", "~8–12%", 0.76, "-0.10"]
    figures_description:
      - "Fig 10: Line plot — macro-F1 vs edit rate. Linear degradation with 95% CI band. Horizontal dashed line at chance level (0.33). Annotation at 10% edit rate: 'typical human editing range.'"
    analysis: >
      The robustness profile is realistic for practical deployment. Light editing
      (5–10%) typical of human post-processing preserves most of the depth signal.
      Heavy editing (20%) degrades performance significantly but remains above
      chance, suggesting that even heavily edited text retains some distributional
      fingerprint. For the paper, this experiment provides the necessary caveat
      about real-world applicability while showing that the method is viable for
      the most common use case (lightly edited or unedited synthetic text in
      web-scraped data).

  - name: ld_score_feature
    plan_id: plan_011
    description: >
      Add LD-Score (character-distribution signature from arXiv:2605.01647) as an
      additional feature to the plan_001 ablation framework. Tests whether character-level
      features provide complementary depth signal beyond token-level distributional
      features.
    expected_results:
      full_plus_ld_macro_f1: 0.88
      ld_score_only_macro_f1: 0.59
      ld_score_permutation_importance: 0.06
      full_plus_ld_vs_full_delta: 0.01
    result_rationale: >
      LD-Score alone achieves modest depth discrimination (F1=0.59) because
      character-level distributional signatures capture some depth-dependent
      patterns — deeper generation text has slightly more uniform character
      distributions as vocabulary impoverishment affects character-level statistics.
      However, adding LD-Score to the full feature set provides only marginal
      improvement (Δ=+0.01) because LD-Score's signal is largely redundant with
      existing surface features (TTR, hapax_ratio) — both measure vocabulary
      impoverishment, just at different granularities (character vs word level).
      The low permutation importance (0.06) confirms that LD-Score is not providing
      new information. This is a useful negative-ish result: it shows that
      character-level features do not add a fundamentally new signal modality,
      reinforcing that the key complementary feature families are surface
      vocabulary statistics and reference-model distributional features.
    tables:
      - name: "Table 15: LD-Score Feature Integration"
        columns: ["Feature Set", "Macro-F1", "Δ from Full"]
        rows:
          - ["Full (7 features)", 0.87, "—"]
          - ["Full + LD-Score (8 features)", 0.88, "+0.01"]
          - ["LD-Score only", 0.59, "-0.28"]
    figures_description:
      - "Fig S1 (supplementary): Feature importance bar chart with LD-Score included. LD-Score ranks below all reference-model features."
    analysis: >
      A clean but unexciting result that belongs in the supplementary material.
      It confirms the two-modality structure of depth signal (reference-model
      entropy + surface vocabulary) and shows that adding more surface-level
      features (even at a different granularity) does not expand the signal envelope.
      For the paper, this addresses potential questions about "what about other
      feature types" and justifies the focus on reference-model features as the
      novel contribution.

  - name: end_to_end_classifier
    plan_id: plan_012
    description: >
      QLoRA fine-tune Qwen3.5-0.8B for end-to-end depth classification (directly
      from text, no handcrafted features). Compares learned representations vs
      handcrafted distributional features on the plan_002 dataset.
    expected_results:
      qwen_qlora_macro_f1: 0.83
      qwen_qlora_gen0_f1: 0.94
      qwen_qlora_gen1_f1: 0.77
      qwen_qlora_gen2plus_f1: 0.79
      handcrafted_features_macro_f1: 0.86
      qwen_qlora_cross_gen_leave_one_out_f1: 0.71
      handcrafted_cross_gen_leave_one_out_f1: 0.78
      qwen_qlora_training_gpu_hours: 12.0
      handcrafted_training_time_minutes: 3.0
    result_rationale: >
      The QLoRA fine-tuned model achieves competitive in-distribution performance
      (F1=0.83 vs handcrafted 0.86) because the transformer can implicitly learn
      distributional features from raw text. However, it underperforms the
      handcrafted approach for two reasons: (1) the handcrafted features distill
      the reference model's perspective into compact statistics that directly
      measure what matters (distributional drift from human text), while the
      fine-tuned model must learn this implicitly from text patterns; (2) the
      XGBoost classifier on 7 features is harder to overfit than a 0.8B parameter
      model on ~25K training examples. The larger gap in cross-generator
      leave-one-out (0.71 vs 0.78) reveals that the fine-tuned model memorizes
      generator-specific artifacts more than the handcrafted features, which are
      designed to be generator-invariant. The 4000× training time difference
      (12 GPU-hours vs 3 minutes) makes the handcrafted approach clearly preferable
      for practical deployment. This result validates the feature engineering
      approach over brute-force fine-tuning and justifies the paper's focus on
      interpretable distributional features.
    tables:
      - name: "Table 16: End-to-End vs Feature-Based Comparison"
        columns: ["Method", "In-Dist F1", "Cross-Gen F1", "Training Cost"]
        rows:
          - ["XGBoost + handcrafted features", 0.86, 0.78, "3 min"]
          - ["QLoRA Qwen3.5-0.8B", 0.83, 0.71, "12 GPU·h"]
          - ["Δ (handcrafted − QLoRA)", "+0.03", "+0.07", "—"]
    figures_description:
      - "Fig S2 (supplementary): Paired bar chart — in-distribution vs cross-generator F1 for both methods. Handcrafted features show smaller generalization gap."
    analysis: >
      This is a strategically important result. Reviewers might ask "why not just
      fine-tune a model?" — this experiment shows that handcrafted features
      outperform, generalize better, are 4000× cheaper to train, and are
      interpretable (you can point to specific features and explain why they work).
      The fine-tuned model's worse cross-generator generalization is the most
      telling result: it confirms that the handcrafted features capture the
      right abstraction (distributional drift as measured by a reference model)
      while the fine-tuned model takes shortcuts via generator-specific patterns.
      This result belongs in the supplementary material and reinforces the paper's
      methodological choice.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10b0be21-deb3-44c6-9863-5aafa47700f5",
  "isSidechain": false,
  "requestId": "req_011Cb2v7MVNgaeEh4bxvfuxq",
  "type": "assistant",
  "uuid": "a2a57b72-7eb4-4681-bca1-1c6e15f51e46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJtZSTU2dZxZyxNDkrusGT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3060,
      "cache_read_input_tokens": 21242,
      "output_tokens": 14856,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14856,
          "cache_read_input_tokens": 21242,
          "cache_creation_input_tokens": 3060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3060
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

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reference-model features carry dominant independent depth signal; cross-generator generalization holds; all three claims verified cleanly 核心假设：['Claim 2 fu…",
  "leafUuid": "a2a57b72-7eb4-4681-bca1-1c6e15f51e46",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate distributional fingerprints for generation depth estimation",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reference-model features carry dominant independent depth signal; cross-generator generalization holds; all three claims verified cleanly 核心假设：['Claim 2 fu…",
  "leafUuid": "a2a57b72-7eb4-4681-bca1-1c6e15f51e46",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate distributional fingerprints for generation depth estimation",
  "sessionId": "33650369-a049-4c64-8301-8fd18bc00ef8"
}
```

---
