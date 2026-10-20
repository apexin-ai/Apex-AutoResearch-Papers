# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Dataflow negatives hurt or are indistinguishable from embedding-distance; Z

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/b5eda8b7-2eb3-4589-ae68-d539d1f9e440.jsonl`
- **Structured JSON:** [`e75cab7c98b2d1af0133.json`](../../sessions/e7/e75cab7c98b2d1af0133.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T20:53:59.724Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T20:53:59.724Z",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Dataflow negatives hurt or are indistinguishable from embedding-distance; Z% collapses at scale or timeout spikes; only negative results survive; restructure as analysis paper\n核心假设：['Z% at 5K scale < 20% or CodeQL timeout > 15%, undermining scalability claim', 'Dataflow negatives perform similarly to embedding-distance (both worse than random), suggesting structural features as used here add noise rather than signal', \"The connected≠gold signal at 40.8% was inflated by medium-repo bias (55.7%) that doesn't generalize\", 'End-to-end SWE-bench shows no improvement or regression from any hard negative strategy', 'Embedding-distance harm effect may shrink at full-scale training (more data dilutes the redundancy problem)']\n关键指标范围：{'Z_pct_5K': [8, 20], 'codeql_timeout_pct_5K': [12, 25], 'retrieval_R5_dataflow': [0.7, 0.79], 'retrieval_R5_random': [0.74, 0.83], 'retrieval_R5_emb_dist': [0.71, 0.8], 'delta_dataflow_vs_random_R5': [-0.06, -0.01], 'delta_emb_vs_random_R5': [-0.04, -0.01], 'swebench_lite_resolve_delta_pp': [-2.0, 0.5], 'repobench_R_improvement_pp': [-3.0, 0.5]}\n叙事方向：Restructure as analysis/negative-result paper: \"Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet).\" Core contribution becomes empirical analysis of three negative mining strategies with deep failure taxonomy. Key findings: (1) all hard negatives underperform random when pool diversity is sufficient — random sampling from large repos already provides implicit structural diversity; (2) CodeQL reachability is too coarse (2-hop call-graph) to capture fine-grained repair relevance; (3) the connected≠gold signal is necessary but not sufficient — connectivity does not imply repair-relevance. Salvageable pieces: the formal framework for structure-grounded negatives (future work with finer-grained analysis), the empirical methodology, and the embedding-harm finding if it partially replicates. Target: workshop paper (NLP4SE, ML4Code) or analysis track. Consider whether the formal definition + negative results are sufficient for a short/Findings paper with honest framing.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\nfocus: Key risk: dataflow negatives showed connected⊆gold at MVP scale (8 repos) but Z=40.8% at 50-repo scale. Full-scale training may reveal the effect is weaker than hypothesized. Also: embedding-distance negatives actively harm (-3.7pp R@1), which is a strong negative result supporting the dual-pillar motivation. Reviewers should stress-test whether the connected≠gold signal at scale (40.8%) is sufficient to produce meaningful training differentiation, and whether the improvement magnitude will be large enough for EMNLP acceptance.\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Structure-grounded hard negatives outperform embedding-distance and random negatives for contrastive code retrieval training.** Inter-procedural data-flow connectivity provides a complementary signal dimension that textual similarity cannot recover — files that are lexically similar but structurally disconnected force the model to internalize structural relevance beyond surface features.\n\n2. **Embedding-distance hard negatives actively harm code retrieval compared to random negatives.** The gradient signal from embedding-distance negatives is partially redundant with the encoder's learned similarity, leading to degraded retrieval quality. (MVP evidence: -3.7pp recall@1 at pool=50, -27pp at pool=26, 3 seeds consistent.)\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** With 2-hop call-graph bounding, timeout <5%, and >40% of instances have connected-but-not-gold structural signals at scale.\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers conflate lexical similarity with structural relevance — a file sharing function names with the buggy code may be structurally unrelated, while a data-flow-connected file may contain the actual fix dependency.\n\n- **Existing approaches & gaps**:\n  - Text-based (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no data-flow edges, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: hard negatives improve code search, but embedding-distance negatives are redundant with encoder similarity\n\n- **Our framing**: The key gap is using structural connectivity for **training signal**, not just inference-time navigation. Structure-grounded hard negatives — lexically similar but data-flow disconnected files — provide a complementary learning signal. This is a general paradigm: any domain with external structural knowledge (molecular networks, circuit topology, KG retrieval) can use drift-immune structure-grounded negative mining. Code is the ideal testbed due to formal semantic guarantees.\n\n- **Headline result template**: \"On SWE-bench Lite, StructFuse with data-flow-aware hard negatives achieves X% recall@5 while embedding-distance negatives achieve Y% and random negatives Z%, demonstrating that structure-grounded negative mining provides training signal that text-based methods cannot recover.\"\n\n## Dual-Pillar Motivation (per Human Review)\n\n1. **Primary — Complementary signal dimension**: Structural connectivity encodes a relevance dimension entirely absent from textual signals. No amount of text-based training can recover inter-procedural data-flow relationships from token sequences alone.\n2. **Secondary — Selection drift immunity**: Structural graph is externally fixed; negative set does not drift with encoder updates (unlike embedding-distance negatives which shift every epoch).\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder.\n\n## Title\n\n\"StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval\"\n(Per Human Review: emphasize methodology, de-emphasize SE-specific framing)\n\n## Venue Fit Risks\n\n1. **EMNLP vs SE**: Frame as contrastive learning methodology with code as instantiation\n2. **Domain-specific concern**: Cross-domain generalization in Discussion (molecular networks, circuit topology, KG retrieval)\n3. **Incremental contribution**: Novelty is in WHAT generates negatives (program analysis), not the objective itself\n4. **CodeQL dependency**: CodeQL is one instantiation; any structural analysis producing a connectivity graph works\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Too domain-specific | Cross-domain generalization + formal definition is domain-agnostic | Discussion section |\n| Why not ARISE? | Intra-procedural only + inference-time only; we cross call boundaries + train | Direct comparison in ablation |\n| CodeQL scalability | 0% timeout at pilot, 4% at 50-repo scale; scope-bounded 2-hop | P1 + scale check |\n| Small improvement | Training methodology contribution, not benchmark chasing; improvement ceiling analysis | Failure analysis |\n| connected⊆gold? | Scale effect: 40.8% instances have connected≠gold at 50-repo scale | M1 full statistics |\n\n## MVP Evidence Summary\n\n- P1: CodeQL feasible (timeout 0%, Fisher p=1.54e-7, instance recall 75%)\n- P2a: DataFlow feature AUC=0.78, BM25 coefficient negative (-1.80)\n- P2b: random >> embedding_distance (-3.7pp R@1 at pool=50); dataflow untestable at MVP scale but viable at full scale (Z=40.8%)\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: QUEUED\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-12T20:53:59.728Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T20:53:59.728Z",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-12T20:53:59.750Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Dataflow negatives hurt or are indistinguishable from embedding-distance; Z% collapses at scale or timeout spikes; only negative results survive; restructure as analysis paper
核心假设：['Z% at 5K scale < 20% or CodeQL timeout > 15%, undermining scalability claim', 'Dataflow negatives perform similarly to embedding-distance (both worse than random), suggesting structural features as used here add noise rather than signal', "The connected≠gold signal at 40.8% was inflated by medium-repo bias (55.7%) that doesn't generalize", 'End-to-end SWE-bench shows no improvement or regression from any hard negative strategy', 'Embedding-distance harm effect may shrink at full-scale training (more data dilutes the redundancy problem)']
关键指标范围：{'Z_pct_5K': [8, 20], 'codeql_timeout_pct_5K': [12, 25], 'retrieval_R5_dataflow': [0.7, 0.79], 'retrieval_R5_random': [0.74, 0.83], 'retrieval_R5_emb_dist': [0.71, 0.8], 'delta_dataflow_vs_random_R5': [-0.06, -0.01], 'delta_emb_vs_random_R5': [-0.04, -0.01], 'swebench_lite_resolve_delta_pp': [-2.0, 0.5], 'repobench_R_improvement_pp': [-3.0, 0.5]}
叙事方向：Restructure as analysis/negative-result paper: "Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet)." Core contribution becomes empirical analysis of three negative mining strategies with deep failure taxonomy. Key findings: (1) all hard negatives underperform random when pool diversity is sufficient — random sampling from large repos already provides implicit structural diversity; (2) CodeQL reachability is too coarse (2-hop call-graph) to capture fine-grained repair relevance; (3) the connected≠gold signal is necessary but not sufficient — connectivity does not imply repair-relevance. Salvageable pieces: the formal framework for structure-grounded negatives (future work with finer-grained analysis), the empirical methodology, and the embedding-harm finding if it partially replicates. Target: workshop paper (NLP4SE, ML4Code) or analysis track. Consider whether the formal definition + negative results are sufficient for a short/Findings paper with honest framing.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: faith-evidence-ie
focus: Key risk: dataflow negatives showed connected⊆gold at MVP scale (8 repos) but Z=40.8% at 50-repo scale. Full-scale training may reveal the effect is weaker than hypothesized. Also: embedding-distance negatives actively harm (-3.7pp R@1), which is a strong negative result supporting the dual-pillar motivation. Reviewers should stress-test whether the connected≠gold signal at scale (40.8%) is sufficient to produce meaningful training differentiation, and whether the improvement magnitude will be large enough for EMNLP acceptance.

## paper_framing.md

# Paper Framing — StructFuse

## Target Venue
- Primary: EMNLP 2026 Main
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026

## Core Claims (3)

1. **Structure-grounded hard negatives outperform embedding-distance and random negatives for contrastive code retrieval training.** Inter-procedural data-flow connectivity provides a complementary signal dimension that textual similarity cannot recover — files that are lexically similar but structurally disconnected force the model to internalize structural relevance beyond surface features.

2. **Embedding-distance hard negatives actively harm code retrieval compared to random negatives.** The gradient signal from embedding-distance negatives is partially redundant with the encoder's learned similarity, leading to degraded retrieval quality. (MVP evidence: -3.7pp recall@1 at pool=50, -27pp at pool=26, 3 seeds consistent.)

3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** With 2-hop call-graph bounding, timeout <5%, and >40% of instances have connected-but-not-gold structural signals at scale.

## Story Spine

- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers conflate lexical similarity with structural relevance — a file sharing function names with the buggy code may be structurally unrelated, while a data-flow-connected file may contain the actual fix dependency.

- **Existing approaches & gaps**:
  - Text-based (SweRank, SWE-Fixer): blind to structural dependencies
  - Graph-guided (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no data-flow edges, no training signal
  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
  - CoCoHaNeRe: hard negatives improve code search, but embedding-distance negatives are redundant with encoder similarity

- **Our framing**: The key gap is using structural connectivity for **training signal**, not just inference-time navigation. Structure-grounded hard negatives — lexically similar but data-flow disconnected files — provide a complementary learning signal. This is a general paradigm: any domain with external structural knowledge (molecular networks, circuit topology, KG retrieval) can use drift-immune structure-grounded negative mining. Code is the ideal testbed due to formal semantic guarantees.

- **Headline result template**: "On SWE-bench Lite, StructFuse with data-flow-aware hard negatives achieves X% recall@5 while embedding-distance negatives achieve Y% and random negatives Z%, demonstrating that structure-grounded negative mining provides training signal that text-based methods cannot recover."

## Dual-Pillar Motivation (per Human Review)

1. **Primary — Complementary signal dimension**: Structural connectivity encodes a relevance dimension entirely absent from textual signals. No amount of text-based training can recover inter-procedural data-flow relationships from token sequences alone.
2. **Secondary — Selection drift immunity**: Structural graph is externally fixed; negative set does not drift with encoder updates (unlike embedding-distance negatives which shift every epoch).

## Formal Definition

Given retrieval domain D, structural graph G, similarity function s, query q:
**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)

The structural graph is externally fixed and does not update with the encoder.

## Title

"StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval"
(Per Human Review: emphasize methodology, de-emphasize SE-specific framing)

## Venue Fit Risks

1. **EMNLP vs SE**: Frame as contrastive learning methodology with code as instantiation
2. **Domain-specific concern**: Cross-domain generalization in Discussion (molecular networks, circuit topology, KG retrieval)
3. **Incremental contribution**: Novelty is in WHAT generates negatives (program analysis), not the objective itself
4. **CodeQL dependency**: CodeQL is one instantiation; any structural analysis producing a connectivity graph works

## Anticipated Reviewer Concerns

| Concern | Response | Evidence |
|---------|----------|----------|
| Too domain-specific | Cross-domain generalization + formal definition is domain-agnostic | Discussion section |
| Why not ARISE? | Intra-procedural only + inference-time only; we cross call boundaries + train | Direct comparison in ablation |
| CodeQL scalability | 0% timeout at pilot, 4% at 50-repo scale; scope-bounded 2-hop | P1 + scale check |
| Small improvement | Training methodology contribution, not benchmark chasing; improvement ceiling analysis | Failure analysis |
| connected⊆gold? | Scale effect: 40.8% instances have connected≠gold at 50-repo scale | M1 full statistics |

## MVP Evidence Summary

- P1: CodeQL feasible (timeout 0%, Fisher p=1.54e-7, instance recall 75%)
- P2a: DataFlow feature AUC=0.78, BM25 coefficient negative (-1.80)
- P2b: random >> embedding_distance (-3.7pp R@1 at pool=50); dataflow untestable at MVP scale but viable at full scale (Z=40.8%)


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected
    vs gold statistics'
  priority: P0
  gpu_budget_hours: 0
  deps: []
  status: planned
- id: plan_002
  claim: 1
  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,
    3 seeds each, Qwen2.5-Coder-3B LoRA'
  priority: P0
  gpu_budget_hours: 30
  deps:
  - plan_001
  status: planned
- id: plan_003
  claim: 1
  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best
    checkpoint, Qwen3.6-27B agent'
  priority: P0
  gpu_budget_hours: 40
  deps:
  - plan_002
  status: planned
- id: plan_004
  claim: 1
  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no
    LLM agent'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - plan_002
  status: planned
- id: plan_005
  claim: 2
  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding
    negatives 何时最有害'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_002
  status: planned
- id: plan_006
  claim: 3
  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,
    connected-but-not-gold ratio by repo size'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  status: planned
- id: plan_007
  claim: 1
  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'
  priority: P1
  gpu_budget_hours: 20
  deps:
  - plan_001
  status: planned
- id: plan_008
  claim: 1
  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - plan_001
  status: planned
- id: plan_009
  claim: 1
  description: 'Ablation: fusion head (embedding-only vs structural-features-only
    vs combined)'
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_002
  status: planned
- id: plan_010
  claim: 1
  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'
  priority: P2
  gpu_budget_hours: 10
  deps:
  - plan_001
  status: planned
- id: plan_011
  claim: 1
  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether
    data-flow helps'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_003
  status: planned
- id: plan_012
  claim: 1
  description: 'Qualitative examples: 5-10 cases where structural negatives changed
    retrieval outcome'
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_003
  status: planned


## registry (completed experiments)

- exp_id: mvp_p1_codeql_feasibility
  name: ''
  status: DONE
  conclusion: success
  metrics:
    timeout_rate: 0
    repos_processed: 8
    repos_skipped: 2
    cg_mean_s: 29.6
    cg_max_s: 119.8
    df_mean_s: 43.4
    df_max_s: 167.1
    h2_connected_coverage: 0.014815
    h2_disconnected_coverage: 0
    h2_fisher_p: 6.5e-09
    h2_gold_in_connected_ratio: 1
    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'
- exp_id: mvp_p2a_linear_proxy
  name: ''
  status: DONE
  conclusion: success
  metrics:
    df_bm25_auc: 0.78
    bm25_only_auc: 0.476
    auc_delta: 0.304
    df_bm25_mrr: 0.556
    bm25_only_mrr: 0.115
    mrr_delta: 0.441
    df_bm25_f1: 0.143
    bm25_only_f1: 0.039
    top_feature: is_connected (+2.82)
    repos_evaluated: 3
    note: 3 repos / 3 positive samples, directional evidence
- exp_id: p2b-smoke-test
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke4
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke5
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke6
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke7
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke8
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-all-9runs
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_p2b_contrastive_training
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics:
    random_s42_recall1: 0.984
    random_s123_recall1: 0.984
    random_s456_recall1: 0.992
    embedding_s42_recall1: 0.874
    random_mean_recall1: 0.987
    runs_completed: 4
    runs_failed: 5
    failure_type: disk_full_torch_save
- exp_id: mvp_p2b_contrastive_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b_eval_all
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: p2b_eval_4runs_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    random_seed42:
      recall@1: 0.9449
      recall@5: 0.9843
      recall@10: 0.9843
    random_seed123:
      recall@1: 0.9449
      recall@5: 0.9921
      recall@10: 0.9921
    random_seed456:
      recall@1: 0.9291
      recall@5: 0.9921
      recall@10: 0.9921
    emb_dist_seed42:
      recall@1: 0.6693
      recall@5: 0.8898
      recall@10: 0.9291
    pool_size: 26
    n_samples: 127
- exp_id: p2b_5reruns
  name: ''
  status: DONE
  conclusion: success
  metrics:
    random_s42:
      val_loss: 0.0347
      recall@1: 0.9843
    random_s123:
      val_loss: 0.0446
      recall@1: 0.9843
    random_s456:
      val_loss: 0.0188
      recall@1: 0.9921
    emb_dist_s42:
      val_loss: 0.1876
      recall@1: 0.874
    emb_dist_s123:
      val_loss: 0.1461
      recall@1: 0.874
    emb_dist_s456:
      val_loss: 0.1281
      recall@1: 0.8819
    dataflow_s42:
      val_loss: 0.1878
      recall@1: 0.874
    dataflow_s123:
      val_loss: 0.146
      recall@1: 0.874
    dataflow_s456:
      val_loss: 0.1278
      recall@1: 0.8819
    runs_completed: 9
    runs_failed: 0
    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds
      — likely code bug in negative sampling
- exp_id: p2b_dataflow_retrain
  name: ''
  status: QUEUED
  conclusion: negative
  metrics: {}
- exp_id: p2b_eval_4runs_pool50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pool_size: 50
    n_samples: 127
    random_s42:
      recall@1: 0.496
      recall@5: 0.843
      recall@10: 0.945
    random_s123:
      recall@1: 0.535
      recall@5: 0.85
      recall@10: 0.921
    random_s456:
      recall@1: 0.543
      recall@5: 0.843
      recall@10: 0.953
    emb_dist_s42:
      recall@1: 0.488
      recall@5: 0.835
      recall@10: 0.874
    random_mean:
      recall@1: 0.525
      recall@5: 0.845
      recall@10: 0.94
    emb_dist_vs_random_delta:
      recall@1: -0.037
      recall@5: -0.01
      recall@10: -0.066
- exp_id: d007_50repo_overlap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_instances: 240
    instances_with_extra_connected: 98
    Z_pct: 40.8
    avg_connected_minus_gold: 6
    codeql_timeout_rate_pct: 4
    by_repo_size:
      small_lt50:
        Z_pct: 38.6
        avg_extra: 2.5
      medium_50_200:
        Z_pct: 55.7
        avg_extra: 11.8
      large_gt200:
        Z_pct: 16.7
        avg_extra: 8.8
    decision: Z=40.8% >= 20% -> original method viable, proceed to M1

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
  "promptId": "c78a1f63-fa37-4273-a264-35dc8b1f198b",
  "type": "user",
  "uuid": "1a197106-a0f0-4b7d-8ff7-7b789588010e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T20:53:59.749Z_

```json
{
  "parentUuid": "1a197106-a0f0-4b7d-8ff7-7b789588010e",
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
  "uuid": "b7bf9f92-3592-4e86-a3cd-20f55ee7dc62",
  "timestamp": "2026-05-12T20:53:59.749Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T20:53:59.749Z_

```json
{
  "parentUuid": "b7bf9f92-3592-4e86-a3cd-20f55ee7dc62",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "1ac82d88-468a-4d0a-9ff0-4544d4048ad4",
  "timestamp": "2026-05-12T20:53:59.749Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-12T20:53:59.749Z_

```json
{
  "parentUuid": "1ac82d88-468a-4d0a-9ff0-4544d4048ad4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0c8de905-8793-4a8e-8fea-c95e39b5906e",
  "timestamp": "2026-05-12T20:53:59.749Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Dataflow negatives hurt or are indistinguishable from embedding-distance; Z% collapses at scale or timeout spikes; only negative results survive; restruct…",
  "leafUuid": "0c8de905-8793-4a8e-8fea-c95e39b5906e",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze worst-case scenario for structure-grounded hard negatives",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440"
}
```

---

### Assistant

_source line 9 · 2026-05-12T20:54:21.461Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment under the "worst" tier scenario. Let me review all the planned experiments and the worst-tier definition carefully.

The worst tier means:
- Z% at 5K scale < 20% or CodeQL timeout > 15%
- Dataflow negatives perform similarly to embedding-distance (both worse than random)
- The connected≠gold signal at 40.8% was inflated by medium-repo bias (55.7%)
- End-to-end SWE-bench shows no improvement or regression
- Embedding-distance harm effect may shrink at full-scale training


Now I'm mapping out the specific metric ranges I'll use for the worst-case predictions: Z_pct_5K between 8-20%, CodeQL timeouts between 12-25%, retrieval metrics showing dataflow and embedding-distance both underperforming random baseline, and negative deltas indicating no improvement over the baseline approach.

Looking at the planned experiments, I need to work through each one systematically—starting with the full CodeQL extraction on 5K repos, then the three-strategy comparison training with different retrieval approaches, followed by the end-to-end evaluations on SWE-bench Lite and RepoBench-R, and finally a deeper analysis of how embedding-based retrieval compares to random selection.

Now I'm laying out the remaining ablation studies to isolate key components: testing different hop distances in the dataflow graph, scaling the training data to understand sample efficiency, evaluating the fusion head's contribution, and examining how weighting negatives by dataflow distance affects performance. I'll also need to analyze failure cases and pull out qualitative examples to understand where the approach succeeds and struggles.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c8de905-8793-4a8e-8fea-c95e39b5906e",
  "isSidechain": false,
  "requestId": "req_011CayLeMhRgnjHzV2axk52E",
  "type": "assistant",
  "uuid": "2e18135d-cf85-4195-b3b1-78a01f997f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DufZA24RYVTnpqm2DoDbPL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11026,
      "cache_read_input_tokens": 11447,
      "output_tokens": 11159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11159,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11026
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

_source line 10 · 2026-05-12T20:57:39.167Z_

```yaml
tier: worst
narrative_guidance: >
  Restructure as analysis/negative-result paper: "Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet)."
  Core contribution becomes empirical analysis of three negative mining strategies with deep failure taxonomy.
  Key findings: (1) all hard negatives underperform random when pool diversity is sufficient;
  (2) CodeQL 2-hop reachability is too coarse to capture fine-grained repair relevance;
  (3) connected≠gold signal is necessary but not sufficient.
  Target: workshop paper (NLP4SE, ML4Code) or analysis/Findings track.

imagined_experiments:
  - name: "M1 全量 CodeQL 提取"
    plan_id: "plan_001"
    description: "5K SWE-smith repos data-flow extraction + connected vs gold statistics"
    expected_results:
      repos_attempted: 5000
      repos_successful: 3850
      repos_skipped_no_python: 420
      repos_failed_codeql_error: 310
      repos_timeout: 420
      total_instances: 18200
      instances_with_extra_connected: 2550
      Z_pct_overall: 14.0
      Z_pct_small_lt50: 9.2
      Z_pct_medium_50_200: 24.8
      Z_pct_large_gt200: 5.1
      gold_in_connected_ratio: 0.72
      avg_connected_minus_gold_small: 1.1
      avg_connected_minus_gold_medium: 5.3
      avg_connected_minus_gold_large: 2.8
      cg_mean_s: 48.7
      cg_median_s: 22.1
      cg_p95_s: 210.5
      df_mean_s: 71.3
      df_median_s: 35.8
      df_p95_s: 340.2
    result_rationale: >
      50-repo Z=40.8% 被 medium-repo 偏差严重膨胀（medium 占比 55.7%，Z=55.7%）。
      5K 规模下 repo size 分布回归自然分布：small 占 ~60%，medium ~25%，large ~15%。
      small repos 文件少，call-graph 稀疏，connected set 几乎等于 gold set，Z 降至 ~9%。
      large repos CodeQL 分析超时率高且 2-hop 边界内可达文件爆炸，但大多数可达文件与 bug 无关，
      gold_in_connected_ratio 下降到 0.72（pilot 时为 1.0），说明 path normalization 在
      大规模异构 repo 中不够鲁棒。整体 Z=14% < 20% 阈值，核心 scalability claim 失败。
    tables:
      - name: "Table 1: CodeQL Extraction Statistics by Repo Size"
        columns: ["Repo Size", "N repos", "N instances", "Z%", "Avg Extra Connected", "Timeout%"]
        rows:
          - ["Small (<50 files)", 2310, 10920, 9.2, 1.1, 5.8]
          - ["Medium (50-200)", 963, 4550, 24.8, 5.3, 8.2]
          - ["Large (>200)", 577, 2730, 5.1, 2.8, 22.1]
          - ["Overall", 3850, 18200, 14.0, 2.4, 10.9]
    figures_description:
      - "Fig 1: Z% vs repo file count scatter plot, showing strong medium-repo clustering and near-zero Z for small/large repos. Includes 50-repo pilot point (Z=40.8) highlighted as outlier."
      - "Fig 2: CDF of CodeQL extraction time by repo size, showing heavy tail for large repos with 22% exceeding 300s timeout."
    analysis: >
      Z=14% 低于 20% 阈值，意味着 86% 的训练实例中 dataflow negatives 退化为与 random 等价
      （connected set = gold set，无额外结构信号）。medium-repo 偏差假设得到验证：50-repo pilot
      中 medium 占 55.7% 且 Z=55.7%，但 5K 自然分布下 medium 仅占 25%。large repos 的 Z 仅 5.1%
      因为 2-hop 可达集过大（数百文件），反而无法提供有区分度的负例。scalability claim 需要根本性修改。

  - name: "M2 全量 3-strategy 对比训练"
    plan_id: "plan_002"
    description: "random vs embedding_distance vs dataflow_aware, 3 seeds each, Qwen2.5-Coder-3B LoRA, ~15K training instances"
    expected_results:
      training_instances: 15400
      random_s42:
        val_loss: 0.082
        retrieval_R1: 0.412
        retrieval_R5: 0.783
        retrieval_R10: 0.871
      random_s123:
        val_loss: 0.079
        retrieval_R1: 0.425
        retrieval_R5: 0.791
        retrieval_R10: 0.878
      random_s456:
        val_loss: 0.085
        retrieval_R1: 0.408
        retrieval_R5: 0.776
        retrieval_R10: 0.865
      random_mean:
        retrieval_R1: 0.415
        retrieval_R5: 0.783
        retrieval_R10: 0.871
      emb_dist_s42:
        val_loss: 0.121
        retrieval_R1: 0.378
        retrieval_R5: 0.748
        retrieval_R10: 0.842
      emb_dist_s123:
        val_loss: 0.118
        retrieval_R1: 0.385
        retrieval_R5: 0.755
        retrieval_R10: 0.849
      emb_dist_s456:
        val_loss: 0.125
        retrieval_R1: 0.371
        retrieval_R5: 0.741
        retrieval_R10: 0.836
      emb_dist_mean:
        retrieval_R1: 0.378
        retrieval_R5: 0.748
        retrieval_R10: 0.842
      dataflow_s42:
        val_loss: 0.115
        retrieval_R1: 0.382
        retrieval_R5: 0.752
        retrieval_R10: 0.845
      dataflow_s123:
        val_loss: 0.112
        retrieval_R1: 0.390
        retrieval_R5: 0.758
        retrieval_R10: 0.851
      dataflow_s456:
        val_loss: 0.119
        retrieval_R1: 0.375
        retrieval_R5: 0.745
        retrieval_R10: 0.838
      dataflow_mean:
        retrieval_R1: 0.382
        retrieval_R5: 0.752
        retrieval_R10: 0.845
      delta_dataflow_vs_random_R5: -0.031
      delta_emb_vs_random_R5: -0.035
      delta_dataflow_vs_emb_R5: 0.004
      eval_pool_size: 200
      eval_n_samples: 2400
    result_rationale: >
      Z=14% 意味着 86% 的 dataflow training instances 实际上选取的负例与 random 无异
      （connected=gold，disconnected set 就是全集减 gold）。仅 14% 的实例提供了真正的
      structure-grounded signal，这不足以让模型学到结构特征。同时 dataflow negatives
      在这 14% 的实例上选取的是"lexically similar but disconnected"文件，但 2-hop
      call-graph 的 disconnected 判定过于粗糙——很多被标记为 disconnected 的文件实际上
      通过 3-hop 或间接数据流相连，导致假阴性噪声。embedding-distance negatives 的
      harm effect 从 MVP 的 -3.7pp R@1 (pool=50) 缩小到 -3.7pp R@1 (pool=200)，
      但因训练数据量增大（15K vs 127），redundancy 问题被更多样化的数据部分稀释。
      dataflow 与 embedding_distance 的差异仅 0.4pp R@5，统计不显著（p>0.3），
      两者都不如 random。
    tables:
      - name: "Table 2: Retrieval Performance by Negative Mining Strategy (pool=200)"
        columns: ["Strategy", "R@1", "R@5", "R@10", "Δ vs Random R@5"]
        rows:
          - ["Random (3 seeds)", "0.415±0.009", "0.783±0.008", "0.871±0.007", "—"]
          - ["Embedding-distance", "0.378±0.007", "0.748±0.007", "0.842±0.007", "-0.035"]
          - ["Dataflow-aware", "0.382±0.008", "0.752±0.007", "0.845±0.007", "-0.031"]
    figures_description:
      - "Fig 3: Bar chart with error bars for R@1/R@5/R@10 across 3 strategies. Random clearly dominates; dataflow and embedding-distance are statistically indistinguishable."
      - "Fig 4: Training loss curves for all 9 runs. Random converges fastest; dataflow and embedding-distance show similar slower convergence patterns, suggesting both impose similarly noisy gradient signals."
    analysis: >
      Dataflow negatives 表现与 embedding-distance 几乎不可区分，两者都劣于 random。
      这支持核心假设：当 Z% 过低时，structure-grounded signal 被淹没在无差别负例中。
      Random negatives 在大池中自然采样到足够多样性的负例，隐式包含了结构多样性。
      这是论文的核心负面发现，也是 restructure 的关键证据。

  - name: "M3a SWE-bench Lite end-to-end evaluation"
    plan_id: "plan_003"
    description: "3 strategies x best checkpoint, SWE-bench Lite 300 instances, Qwen3.6-27B agent"
    expected_results:
      n_instances: 300
      random_best:
        resolve_rate: 0.243
        recall_R5_file: 0.68
        avg_patches_generated: 2.1
      emb_dist_best:
        resolve_rate: 0.233
        recall_R5_file: 0.66
        avg_patches_generated: 2.0
      dataflow_best:
        resolve_rate: 0.237
        recall_R5_file: 0.67
        avg_patches_generated: 2.0
      baseline_swerank:
        resolve_rate: 0.247
        recall_R5_file: 0.71
      delta_dataflow_vs_random_resolve_pp: -0.6
      delta_dataflow_vs_swerank_resolve_pp: -1.0
      delta_emb_vs_random_resolve_pp: -1.0
      confidence_interval_95_resolve: 0.025
    result_rationale: >
      Retrieval 阶段 dataflow 已经落后 random 3.1pp R@5，这个差距在 end-to-end pipeline 中
      被 agent 的修复能力部分缓冲（agent 能通过多轮交互弥补检索遗漏），但无法反转。
      resolve rate 差异在 confidence interval 内（±2.5pp），统计上三者不可区分。
      SweRank baseline 因为在更大语料上预训练，甚至略优于我们所有策略，进一步削弱
      structure-grounded training 的增量价值叙事。这意味着 end-to-end 结果无法支撑
      任何正面 claim——最多只能说 "no improvement or regression"。
    tables:
      - name: "Table 3: SWE-bench Lite End-to-End Results"
        columns: ["Retriever", "Resolve%", "File R@5", "Δ Resolve vs Random"]
        rows:
          - ["Random negatives", 24.3, 0.68, "—"]
          - ["Embedding-distance", 23.3, 0.66, "-1.0pp"]
          - ["Dataflow-aware", 23.7, 0.67, "-0.6pp"]
          - ["SweRank (baseline)", 24.7, 0.71, "+0.4pp"]
    figures_description:
      - "Fig 5: Resolve rate with 95% bootstrap CI bars. All four methods' CIs heavily overlap, no significant differences."
    analysis: >
      End-to-end 结果是决定性的负面证据：structure-grounded negatives 在下游任务中
      没有产生任何可测量的改进。SweRank baseline 的轻微优势表明，更多预训练数据
      比更精巧的负例选择更有效——这本身是一个值得在分析论文中讨论的发现。

  - name: "M3b RepoBench-R cross-file retrieval evaluation"
    plan_id: "plan_004"
    description: "RepoBench-R retrieval-only evaluation, no LLM agent, 3 strategies x best checkpoint"
    expected_results:
      n_samples: 1200
      random_best:
        MRR: 0.534
        recall_R5: 0.712
        recall_R10: 0.801
      emb_dist_best:
        MRR: 0.498
        recall_R5: 0.683
        recall_R10: 0.775
      dataflow_best:
        MRR: 0.507
        recall_R5: 0.691
        recall_R10: 0.782
      delta_dataflow_vs_random_R5_pp: -2.1
      delta_emb_vs_random_R5_pp: -2.9
      repobench_R_improvement_pp: -2.1
    result_rationale: >
      RepoBench-R 评估的是 cross-file code completion retrieval，与 SWE-bench 的 bug-fix
      retrieval 不同但相关。Random negatives 在此任务上也优于两种 hard negative 策略，
      原因相同：大规模训练集中 random negatives 已经提供了足够的负例多样性。
      Dataflow negatives 略优于 embedding-distance（delta 0.8pp），但仍显著低于 random。
      在 RepoBench 的 cross-repo 设置下，我们训练时使用的 repo-internal dataflow
      信号完全不可用，暴露了方法的 generalization 局限性。
    tables:
      - name: "Table 4: RepoBench-R Retrieval Results"
        columns: ["Strategy", "MRR", "R@5", "R@10", "Δ R@5 vs Random"]
        rows:
          - ["Random", 0.534, 0.712, 0.801, "—"]
          - ["Embedding-distance", 0.498, 0.683, 0.775, "-2.9pp"]
          - ["Dataflow-aware", 0.507, 0.691, 0.782, "-2.1pp"]
    figures_description:
      - "Fig 6: RepoBench-R MRR comparison bar chart. Pattern mirrors SWE-bench retrieval results — random dominates."
    analysis: >
      RepoBench-R 证实了 M2 的结论在 out-of-distribution 设置下也成立。
      Dataflow training signal 不仅在 in-distribution 上无效，在 cross-repo transfer
      上更差，因为 structural connectivity 是 repo-specific 的，不迁移到新 repo。
      这是分析论文中 "generalization failure" 章节的关键证据。

  - name: "Embedding vs random 深度分析"
    plan_id: "plan_005"
    description: "按 repo size/complexity 分层分析 embedding negatives 何时最有害"
    expected_results:
      stratified_by_repo_size:
        small_lt50_files:
          n_instances: 920
          emb_delta_R5: -0.018
          random_R5: 0.812
        medium_50_200:
          n_instances: 580
          emb_delta_R5: -0.042
          random_R5: 0.761
        large_gt200:
          n_instances: 340
          emb_delta_R5: -0.051
          random_R5: 0.698
      stratified_by_code_similarity:
        high_similarity_repos:
          emb_delta_R5: -0.067
          note: "repos with mean pairwise cosine > 0.7"
        low_similarity_repos:
          emb_delta_R5: -0.008
          note: "repos with mean pairwise cosine < 0.4"
      embedding_harm_partially_replicates: true
      harm_magnitude_shrinks_at_scale: true
      mvp_delta_R1_pool50: -0.037
      fullscale_delta_R5_pool200: -0.035
    result_rationale: >
      Embedding-distance harm effect 在全量训练下部分复现但程度减弱。MVP 时 pool=50
      的 -3.7pp R@1 在 full-scale pool=200 上变为 -3.5pp R@5（不同指标不完全可比，
      但量级相近）。关键发现：harm 在 high-similarity repos 中最严重（-6.7pp），
      因为这些 repo 中 embedding-distance negatives 几乎全是 near-duplicates，
      梯度信号高度冗余。在 low-similarity repos 中 harm 几乎消失（-0.8pp），
      因为 embedding-distance 选出的负例已经足够多样。这是可以salvage 的发现——
      embedding harm 与 repo 内部代码相似度高度相关，提供了关于何时避免
      embedding-distance negatives 的实用指导。
    tables:
      - name: "Table 5: Embedding-Distance Harm by Repo Characteristics"
        columns: ["Stratum", "N", "Random R@5", "Emb Δ R@5", "p-value"]
        rows:
          - ["Small repos", 920, 0.812, -0.018, 0.21]
          - ["Medium repos", 580, 0.761, -0.042, 0.04]
          - ["Large repos", 340, 0.698, -0.051, 0.03]
          - ["High intra-sim", 410, 0.745, -0.067, 0.008]
          - ["Low intra-sim", 390, 0.798, -0.008, 0.68]
    figures_description:
      - "Fig 7: Heatmap of embedding harm (Δ R@5) vs repo size and intra-repo cosine similarity. Clear gradient from bottom-left (no harm) to top-right (maximum harm)."
    analysis: >
      Embedding harm finding 部分 salvageable：在 high-similarity repos 中效应稳健，
      可以作为 "when NOT to use embedding-distance negatives" 的实用指南。
      这支持 dual-pillar motivation 中的 selection drift 论点，但仅在特定条件下成立。
      分析论文可以将此作为核心正面贡献之一。

  - name: "M1 scalability statistics"
    plan_id: "plan_006"
    description: "CodeQL timeout rate, extraction time, coverage, connected-but-not-gold ratio by repo size"
    expected_results:
      overall_timeout_pct: 14.2
      timeout_by_size:
        small_lt50: 5.8
        medium_50_200: 8.2
        large_gt200: 42.1
      extraction_time_mean_s: 61.4
      extraction_time_median_s: 28.7
      extraction_time_p95_s: 285.3
      extraction_time_p99_s: 520.1
      coverage_pct: 77.0
      codeql_db_creation_failure_pct: 8.7
      memory_oom_pct: 3.1
      connected_but_not_gold_by_size:
        small: 0.092
        medium: 0.248
        large: 0.051
    result_rationale: >
      CodeQL 的 2-hop call-graph 分析在 large repos 上严重超时（42.1%），因为
      大型 Python 项目的 call-graph 在 2-hop 内可达节点数呈指数增长。overall timeout
      14.2% 超过 15% 阈值（接近边界），这破坏了 "scalable method" 的 claim。
      pilot 时 0% timeout 是因为只有 8 个精选 repo，50-repo 时 4% 是因为刻意
      过滤了过大的 repo。5K 自然分布下大 repo 占比增加，暴露了真实的 scalability 瓶颈。
      coverage 77% 意味着 23% 的 repo 无法成功提取，进一步限制了方法的实用性。
    tables:
      - name: "Table 6: CodeQL Scalability at 5K Repos"
        columns: ["Metric", "Small", "Medium", "Large", "Overall"]
        rows:
          - ["Timeout %", 5.8, 8.2, 42.1, 14.2]
          - ["Mean extraction (s)", 18.3, 52.7, 185.4, 61.4]
          - ["Z%", 9.2, 24.8, 5.1, 14.0]
          - ["DB creation fail %", 3.1, 7.5, 19.8, 8.7]
    figures_description:
      - "Fig 8: Extraction time vs repo file count (log-log), with timeout threshold at 300s. Clear super-linear scaling."
      - "Fig 9: Stacked bar of repo outcomes: success / timeout / OOM / DB-fail, by size bucket."
    analysis: >
      Scalability claim 彻底失败。14.2% overall timeout + 8.7% DB creation failure
      意味着 ~23% 的 repos 无法处理。即使限制在 <200 files 的 repo 上，timeout 仍有 6-8%。
      这表明 CodeQL 的 2-hop bounding 不足以控制分析复杂度——需要更激进的 scope limiting
      或转向更轻量级的静态分析工具。分析论文应诚实报告这些数字并讨论替代方案。

  - name: "Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding"
    plan_id: "plan_007"
    description: "Compare 1-hop, 2-hop, 3-hop bounding on extraction feasibility and Z%"
    expected_results:
      hop_1:
        Z_pct: 6.3
        timeout_pct: 4.8
        gold_in_connected_ratio: 0.51
        mean_connected_set_size: 3.2
      hop_2:
        Z_pct: 14.0
        timeout_pct: 14.2
        gold_in_connected_ratio: 0.72
        mean_connected_set_size: 18.7
      hop_3:
        Z_pct: 22.5
        timeout_pct: 38.6
        gold_in_connected_ratio: 0.84
        mean_connected_set_size: 67.3
      retrieval_R5_hop1: 0.771
      retrieval_R5_hop2: 0.752
      retrieval_R5_hop3: 0.738
    result_rationale: >
      存在不可调和的 trade-off：更多 hops 提高 Z% 和 gold coverage，但 timeout 率
      急剧上升且 connected set 过大导致负例选择区分度下降。1-hop Z% 仅 6.3%，
      几乎无结构信号；3-hop Z% 达到 22.5%（超过 20% 阈值）但 timeout 38.6% 不可接受。
      2-hop 是折中但仍然不够好（Z=14%, timeout=14.2%）。关键问题是 Python 的 call-graph
      天然稀疏（动态调度），1-hop 太少，但一旦增加 hops，组合爆炸导致超时。
      这是方法层面的根本限制，不是工程问题。
    tables:
      - name: "Table 7: Hop Bounding Trade-off"
        columns: ["Hops", "Z%", "Timeout%", "Gold Coverage", "Mean Connected Set", "Retrieval R@5"]
        rows:
          - [1, 6.3, 4.8, 0.51, 3.2, 0.771]
          - [2, 14.0, 14.2, 0.72, 18.7, 0.752]
          - [3, 22.5, 38.6, 0.84, 67.3, 0.738]
    figures_description:
      - "Fig 10: Pareto frontier of Z% vs timeout% for 1/2/3-hop. No operating point achieves Z>20% with timeout<10%."
    analysis: >
      Hop-bounding ablation 揭示了方法的根本困境：Z% 和 feasibility 互相矛盾。
      没有一个 hop 设置同时满足 Z>20% 和 timeout<10%。这是分析论文的核心技术发现，
      解释了为什么 2-hop call-graph 作为 structural graph 不适合大规模负例挖掘。
      Future work 应考虑基于 import graph 或 type hierarchy 的更粗粒度但更 scalable 的替代方案。

  - name: "Ablation: training data size scaling"
    plan_id: "plan_008"
    description: "1K vs 3K vs 5K training instances, dataflow strategy"
    expected_results:
      scale_1K:
        dataflow_R5: 0.721
        random_R5: 0.742
        delta: -0.021
      scale_3K:
        dataflow_R5: 0.743
        random_R5: 0.768
        delta: -0.025
      scale_5K:
        dataflow_R5: 0.752
        random_R5: 0.783
        delta: -0.031
      scaling_trend: "gap widens with more data"
    result_rationale: >
      增加训练数据同时提升 random 和 dataflow 的绝对性能，但两者的差距不缩小反而略微扩大
      （-2.1pp → -2.5pp → -3.1pp）。原因：更多数据意味着 random negatives 获得更多
      隐式结构多样性（大池中自然包含更多 disconnected 负例），而 dataflow 的有效信号
      比例（Z=14%）不随数据量增加而改善——每个新 repo 依然是 ~86% 无差别负例。
      数据量扩展反而凸显了 Z% 过低的问题。这否定了 "more data will help" 的可能救赎路径。
    tables:
      - name: "Table 8: Data Scaling Ablation"
        columns: ["Scale", "Random R@5", "Dataflow R@5", "Δ R@5"]
        rows:
          - ["1K", 0.742, 0.721, -0.021]
          - ["3K", 0.768, 0.743, -0.025]
          - ["5K", 0.783, 0.752, -0.031]
    figures_description:
      - "Fig 11: Scaling curves for random vs dataflow R@5. Lines diverge rather than converge, suggesting the gap is structural not statistical."
    analysis: >
      Scaling 趋势是 worst tier 最致命的证据之一：更多数据不能弥补信号质量问题。
      如果 gap 随数据量缩小，还有希望通过更多数据或更好的 Z% 来挽回。但 gap 扩大
      说明 random negatives 在大数据regime 下有内在优势——它们的多样性与数据量正相关，
      而 dataflow 的结构信号密度（Z%）是 repo 分布的固有属性。

  - name: "Ablation: fusion head variants"
    plan_id: "plan_009"
    description: "Embedding-only vs structural-features-only vs combined fusion head"
    expected_results:
      embedding_only:
        R5: 0.779
        R10: 0.868
      structural_only:
        R5: 0.612
        R10: 0.734
      combined:
        R5: 0.752
        R10: 0.845
      combined_vs_embedding_delta_R5: -0.027
    result_rationale: >
      Structural features alone（is_connected, dataflow_distance 等）作为唯一检索信号
      极差（R@5=0.612），因为 connectivity 是必要非充分条件，且 Z=14% 意味着大多数
      instance 的 structural feature 为零或缺失。Combined fusion 反而比 embedding-only
      更差（-2.7pp），说明在 Z% 过低时加入 structural features 是添加噪声而非信号。
      Structural features 在 86% 的 instances 上没有区分度（connected=gold），
      在这些 case 上 fusion head 学到的权重是噪声，反过来干扰了 embedding 信号。
    tables:
      - name: "Table 9: Fusion Head Ablation"
        columns: ["Variant", "R@5", "R@10", "Δ R@5 vs Emb-only"]
        rows:
          - ["Embedding-only", 0.779, 0.868, "—"]
          - ["Structural-only", 0.612, 0.734, "-0.167"]
          - ["Combined", 0.752, 0.845, "-0.027"]
    figures_description:
      - "Fig 12: Attention weight distribution in combined fusion head. Structural features receive near-zero attention on 85% of instances, confirming sparsity problem."
    analysis: >
      Fusion head ablation 是 "structural features as used here add noise rather than signal"
      假设的直接验证。Combined < embedding-only 说明即使模型可以学习 ignore structural
      features，fusion layer 仍引入了优化难度。这支持分析论文的论点：2-hop call-graph
      connectivity 粒度不足以作为有用的训练特征。

  - name: "Ablation: dataflow-distance weighted negatives"
    plan_id: "plan_010"
    description: "Binary connected/disconnected vs distance-weighted negative sampling"
    expected_results:
      binary:
        R5: 0.752
      distance_weighted:
        R5: 0.747
      delta: -0.005
      distance_distribution_analysis:
        pct_distance_1: 62.3
        pct_distance_2: 37.7
        pct_distance_gt2: 0.0
    result_rationale: >
      2-hop bounding 下距离只有 1 和 2 两个值，weighted sampling 退化为对 distance=1
      的轻微偏好。距离分布极度集中（62.3% 在 distance=1），根本无法提供有意义的
      gradient weighting。distance-weighted 略差于 binary 因为过度偏向 distance=2 的
      负例（更远=更难），但这些负例往往是边界 case，标注噪声更大。
      这个 ablation 技术上有效但无实际意义——问题在上游（Z% 太低），不在下游（采样策略）。
    tables:
      - name: "Table 10: Distance Weighting Ablation"
        columns: ["Sampling", "R@5", "Unique Negatives", "Δ vs Binary"]
        rows:
          - ["Binary", 0.752, 2840, "—"]
          - ["Distance-weighted", 0.747, 2840, "-0.005"]
    figures_description:
      - "Fig 13: Histogram of dataflow distances in training negatives. Bimodal at d=1 and d=2, no long-tail."
    analysis: >
      证实了 2-hop bounding 导致距离空间退化的问题。要让 distance weighting 有意义，
      需要至少 3-hop 的分析深度，但 3-hop 的 timeout 率（38.6%）不可接受。
      又一个 scalability-quality trade-off 的体现。

  - name: "Failure analysis"
    plan_id: "plan_011"
    description: "50 SweRank/BM25 failures, categorize by whether data-flow helps"
    expected_results:
      total_analyzed: 50
      category_breakdown:
        multi_file_cross_module: 12
        single_file_edit: 18
        test_file_related: 8
        config_or_setup: 7
        documentation_adjacent: 5
      dataflow_would_help: 4
      dataflow_would_help_pct: 8.0
      dataflow_neutral: 28
      dataflow_would_hurt: 18
      dataflow_hurt_reasons:
        connected_set_too_large: 9
        gold_not_in_connected: 6
        false_connected_due_to_dynamic_dispatch: 3
    result_rationale: >
      手动分析 50 个 failure cases 发现 dataflow 仅在 8%（4/50）的案例中能提供帮助
      （需要跨模块数据流追踪的多文件编辑）。36%（18/50）的案例中 dataflow 反而有害，
      主要因为：(1) connected set 过大淹没真正相关文件（9例）；(2) gold file 不在
      connected set 中，因为修复不涉及 call-graph 上的数据流（6例，如配置文件修改）；
      (3) Python 动态调度导致 false connection（3例）。56%（28/50）中 dataflow 中性，
      因为这些是单文件编辑或 test 文件问题，structural connectivity 本身不 applicable。
      这个 8% vs 36% 的比率是分析论文中最有说服力的细粒度证据。
    tables:
      - name: "Table 11: Failure Analysis Taxonomy"
        columns: ["Category", "Count", "Dataflow Helpful?", "Reason"]
        rows:
          - ["Cross-module multi-file", 12, "4 yes / 8 no", "Yes when call-chain aligns; no when transitive"]
          - ["Single-file edit", 18, "Neutral", "Structural signal not applicable"]
          - ["Test-related", 8, "Neutral", "Test→source graph is inverted"]
          - ["Config/setup", 7, "0 yes / 5 hurt", "Config not in call-graph"]
          - ["Doc-adjacent", 5, "0 yes / 2 hurt", "Docs not in call-graph"]
    figures_description:
      - "Fig 14: Sankey diagram from failure category → dataflow impact (helps/neutral/hurts). Shows narrow 'helps' flow and wide 'hurts' flow."
    analysis: >
      Failure analysis 揭示了方法的根本适用性问题：2-hop call-graph connectivity
      只能捕捉一种特定的文件间依赖（函数调用链上的数据流），但 SWE-bench 的修复
      涉及多种依赖类型（配置、测试、文档、类型继承），call-graph 对这些完全无效。
      8% helpful rate 说明即使 Z% 足够高，dataflow negatives 的理论上限也很有限。
      这是分析论文 "Why Structure-Grounded Hard Negatives Don't Help (Yet)" 的核心论证。

  - name: "Qualitative examples"
    plan_id: "plan_012"
    description: "5-10 cases where structural negatives changed retrieval outcome"
    expected_results:
      total_examples_found: 7
      positive_change: 2
      negative_change: 4
      ambiguous: 1
      example_themes:
        positive_1: "Cross-module utility function correctly retrieved via 2-hop data-flow"
        positive_2: "Disconnected near-duplicate correctly rejected as negative"
        negative_1: "Config file missed because not in call-graph"
        negative_2: "Test helper connected but irrelevant, displacing correct file"
        negative_3: "Dynamic dispatch false-positive connection"
        negative_4: "Overly large connected set (47 files) diluting signal"
    result_rationale: >
      定性分析反映定量结果：正面案例存在但稀少（2/7），且仅限于 "clean" 的函数调用链场景。
      负面案例更多样且更有教育意义。每个负面案例都指向方法的一个具体局限性：
      call-graph 不覆盖非代码依赖、connected 不等于 relevant、动态语言的静态分析不完整、
      以及 2-hop 在大 repo 中的组合爆炸。这些案例可以构成分析论文的精彩 case study 部分，
      用具体例子说明为什么 "structure-grounded" 的直觉在实践中被诸多噪声源打败。
    tables: []
    figures_description:
      - "Fig 15: Side-by-side retrieval rankings for 2 positive and 4 negative qualitative examples, showing file connectivity graph and retrieval position changes."
    analysis: >
      Qualitative examples 为分析论文提供了必要的叙事深度。读者需要看到具体案例
      才能理解为什么看似合理的直觉（"structurally connected = relevant for repair"）
      在实践中不成立。这些案例也暗示了 future work 方向：需要更丰富的 structural graph
      （包含 import graph、type hierarchy、test-source mapping），而不仅仅是 call-graph data-flow。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e18135d-cf85-4195-b3b1-78a01f997f50",
  "isSidechain": false,
  "requestId": "req_011CayLeMhRgnjHzV2axk52E",
  "type": "assistant",
  "uuid": "9f2b5144-329b-4db5-a912-f13f5911f7a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DufZA24RYVTnpqm2DoDbPL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11026,
      "cache_read_input_tokens": 11447,
      "output_tokens": 11159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11159,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11026
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Dataflow negatives hurt or are indistinguishable from embedding-distance; Z% collapses at scale or timeout spikes; only negative results survive; restruct…",
  "leafUuid": "9f2b5144-329b-4db5-a912-f13f5911f7a6",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze worst-case scenario for structure-grounded hard negatives",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Dataflow negatives hurt or are indistinguishable from embedding-distance; Z% collapses at scale or timeout spikes; only negative results survive; restruct…",
  "leafUuid": "9f2b5144-329b-4db5-a912-f13f5911f7a6",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze worst-case scenario for structure-grounded hard negatives",
  "sessionId": "b5eda8b7-2eb3-4589-ae68-d539d1f9e440"
}
```

---
