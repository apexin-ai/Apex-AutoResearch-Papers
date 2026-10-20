# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Dataflow negatives produce statistically significant retrieval gains over ra

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/97a6a919-58e0-4df7-9f4a-3465cf395004.jsonl`
- **Structured JSON:** [`247ca4621559a79359d1.json`](../../sessions/24/247ca4621559a79359d1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T20:44:41.392Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T20:44:41.392Z",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Dataflow negatives produce statistically significant retrieval gains over random; all 3 claims hold; EMNLP Main viable\n核心假设：['Z% at 5K-repo scale ≥ 35%, confirming sufficient connected≠gold signal for meaningful negative mining', 'Dataflow-aware training converges to different optimum than random (val_loss gap > 0.02)', 'CodeQL timeout < 8% at 5K scale, extraction remains practical', 'Embedding-distance harm replicates at full scale (Δ_emb < -2pp R@5)', 'Gain transfers to end-to-end SWE-bench Lite resolve rate']\n关键指标范围：{'Z_pct_5K': [35, 50], 'codeql_timeout_pct_5K': [3, 8], 'retrieval_R5_dataflow': [0.82, 0.9], 'retrieval_R5_random': [0.74, 0.82], 'retrieval_R5_emb_dist': [0.7, 0.78], 'delta_dataflow_vs_random_R5': [0.04, 0.1], 'delta_emb_vs_random_R5': [-0.08, -0.02], 'swebench_lite_resolve_delta_pp': [1.5, 4.0], 'repobench_R_improvement_pp': [2.0, 6.0]}\n叙事方向：Original framing holds: \"structure-grounded hard negatives outperform both random and embedding-distance.\" Dual-pillar motivation intact — complementary signal + drift immunity both contribute. Headline: dataflow +Xpp over random, embedding actively harms, method scales to 5K repos. Cross-domain generalization discussion is aspirational but credible given strong empirical results. Target: EMNLP Main.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\nfocus: Key risk: dataflow negatives showed connected⊆gold at MVP scale (8 repos) but Z=40.8% at 50-repo scale. Full-scale training may reveal the effect is weaker than hypothesized. Also: embedding-distance negatives actively harm (-3.7pp R@1), which is a strong negative result supporting the dual-pillar motivation. Reviewers should stress-test whether the connected≠gold signal at scale (40.8%) is sufficient to produce meaningful training differentiation, and whether the improvement magnitude will be large enough for EMNLP acceptance.\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Structure-grounded hard negatives outperform embedding-distance and random negatives for contrastive code retrieval training.** Inter-procedural data-flow connectivity provides a complementary signal dimension that textual similarity cannot recover — files that are lexically similar but structurally disconnected force the model to internalize structural relevance beyond surface features.\n\n2. **Embedding-distance hard negatives actively harm code retrieval compared to random negatives.** The gradient signal from embedding-distance negatives is partially redundant with the encoder's learned similarity, leading to degraded retrieval quality. (MVP evidence: -3.7pp recall@1 at pool=50, -27pp at pool=26, 3 seeds consistent.)\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** With 2-hop call-graph bounding, timeout <5%, and >40% of instances have connected-but-not-gold structural signals at scale.\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers conflate lexical similarity with structural relevance — a file sharing function names with the buggy code may be structurally unrelated, while a data-flow-connected file may contain the actual fix dependency.\n\n- **Existing approaches & gaps**:\n  - Text-based (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no data-flow edges, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: hard negatives improve code search, but embedding-distance negatives are redundant with encoder similarity\n\n- **Our framing**: The key gap is using structural connectivity for **training signal**, not just inference-time navigation. Structure-grounded hard negatives — lexically similar but data-flow disconnected files — provide a complementary learning signal. This is a general paradigm: any domain with external structural knowledge (molecular networks, circuit topology, KG retrieval) can use drift-immune structure-grounded negative mining. Code is the ideal testbed due to formal semantic guarantees.\n\n- **Headline result template**: \"On SWE-bench Lite, StructFuse with data-flow-aware hard negatives achieves X% recall@5 while embedding-distance negatives achieve Y% and random negatives Z%, demonstrating that structure-grounded negative mining provides training signal that text-based methods cannot recover.\"\n\n## Dual-Pillar Motivation (per Human Review)\n\n1. **Primary — Complementary signal dimension**: Structural connectivity encodes a relevance dimension entirely absent from textual signals. No amount of text-based training can recover inter-procedural data-flow relationships from token sequences alone.\n2. **Secondary — Selection drift immunity**: Structural graph is externally fixed; negative set does not drift with encoder updates (unlike embedding-distance negatives which shift every epoch).\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder.\n\n## Title\n\n\"StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval\"\n(Per Human Review: emphasize methodology, de-emphasize SE-specific framing)\n\n## Venue Fit Risks\n\n1. **EMNLP vs SE**: Frame as contrastive learning methodology with code as instantiation\n2. **Domain-specific concern**: Cross-domain generalization in Discussion (molecular networks, circuit topology, KG retrieval)\n3. **Incremental contribution**: Novelty is in WHAT generates negatives (program analysis), not the objective itself\n4. **CodeQL dependency**: CodeQL is one instantiation; any structural analysis producing a connectivity graph works\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Too domain-specific | Cross-domain generalization + formal definition is domain-agnostic | Discussion section |\n| Why not ARISE? | Intra-procedural only + inference-time only; we cross call boundaries + train | Direct comparison in ablation |\n| CodeQL scalability | 0% timeout at pilot, 4% at 50-repo scale; scope-bounded 2-hop | P1 + scale check |\n| Small improvement | Training methodology contribution, not benchmark chasing; improvement ceiling analysis | Failure analysis |\n| connected⊆gold? | Scale effect: 40.8% instances have connected≠gold at 50-repo scale | M1 full statistics |\n\n## MVP Evidence Summary\n\n- P1: CodeQL feasible (timeout 0%, Fisher p=1.54e-7, instance recall 75%)\n- P2a: DataFlow feature AUC=0.78, BM25 coefficient negative (-1.80)\n- P2b: random >> embedding_distance (-3.7pp R@1 at pool=50); dataflow untestable at MVP scale but viable at full scale (Z=40.8%)\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: QUEUED\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-12T20:44:41.396Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T20:44:41.396Z",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-12T20:44:41.418Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Dataflow negatives produce statistically significant retrieval gains over random; all 3 claims hold; EMNLP Main viable
核心假设：['Z% at 5K-repo scale ≥ 35%, confirming sufficient connected≠gold signal for meaningful negative mining', 'Dataflow-aware training converges to different optimum than random (val_loss gap > 0.02)', 'CodeQL timeout < 8% at 5K scale, extraction remains practical', 'Embedding-distance harm replicates at full scale (Δ_emb < -2pp R@5)', 'Gain transfers to end-to-end SWE-bench Lite resolve rate']
关键指标范围：{'Z_pct_5K': [35, 50], 'codeql_timeout_pct_5K': [3, 8], 'retrieval_R5_dataflow': [0.82, 0.9], 'retrieval_R5_random': [0.74, 0.82], 'retrieval_R5_emb_dist': [0.7, 0.78], 'delta_dataflow_vs_random_R5': [0.04, 0.1], 'delta_emb_vs_random_R5': [-0.08, -0.02], 'swebench_lite_resolve_delta_pp': [1.5, 4.0], 'repobench_R_improvement_pp': [2.0, 6.0]}
叙事方向：Original framing holds: "structure-grounded hard negatives outperform both random and embedding-distance." Dual-pillar motivation intact — complementary signal + drift immunity both contribute. Headline: dataflow +Xpp over random, embedding actively harms, method scales to 5K repos. Cross-domain generalization discussion is aspirational but credible given strong empirical results. Target: EMNLP Main.


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
  "promptId": "497a2f21-d461-40b1-96cf-3b144c0ef2c8",
  "type": "user",
  "uuid": "644ea626-200f-4a65-893a-4021916f4f9a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T20:44:41.417Z_

```json
{
  "parentUuid": "644ea626-200f-4a65-893a-4021916f4f9a",
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
  "uuid": "101bbcef-c490-4932-9619-4e01747528e3",
  "timestamp": "2026-05-12T20:44:41.417Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T20:44:41.417Z_

```json
{
  "parentUuid": "101bbcef-c490-4932-9619-4e01747528e3",
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
  "uuid": "dd8e812c-003d-4e21-8287-990d07ddd1bc",
  "timestamp": "2026-05-12T20:44:41.417Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-12T20:44:41.417Z_

```json
{
  "parentUuid": "dd8e812c-003d-4e21-8287-990d07ddd1bc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8928be79-7944-4ace-983f-75afdb9001a5",
  "timestamp": "2026-05-12T20:44:41.417Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Dataflow negatives produce statistically significant retrieval gains over random; all 3 claims hold; EMNLP Main viable 核心假设：['Z% at 5K-repo scale ≥ 35%, co…",
  "leafUuid": "8928be79-7944-4ace-983f-75afdb9001a5",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Scale dataflow negatives to 5K repos and validate EMNLP claims",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004"
}
```

---

### Assistant

_source line 9 · 2026-05-12T20:44:58.635Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, based on the "best" tier definition. Let me carefully analyze:

1. The best tier means: Dataflow negatives produce statistically significant retrieval gains over random; all 3 claims hold; EMNLP Main viable
2. Key metric ranges are given
3. I need to provide result_rationale for each prediction

Let me go through each planned experiment and generate detailed predictions.

Let me re-read the experiment plan and registry data carefully.

Key existing evidence:
- MVP scale (8 repos): CodeQL timeout 0%, gold_in_connected_ratio=1.0


- At 50-repo scale, CodeQL timeout rises to 4% and Z-score reaches 40.8%
- Training baselines show random achieving R@1=0.987 on MVP but dropping to 0.525 at Pool50 scale, while embedding distance performs worse in both settings
- Validation loss indicates random models are better calibrated than embedding distance models
- Dataflow training had implementation issues that need resolving before I can use those results

For the "best" tier predictions, I need to account for how performance typically degrades at larger scales while ensuring dataflow negatives still show statistically significant gains.

Plan 001 should see CodeQL extraction complete across 5K repos with Z-score around 42% and timeout rates near 5%. For Plan 002, I'm predicting dataflow will achieve R@5 between 0.82-0.9 with a validation loss gap exceeding 0.02 compared to random, while embedding distance should underperform both. Plan 003 involves running the full SWE-bench Lite evaluation pipeline end-to-end.

Now I'm laying out the remaining experiments: Plan 004 tests RepoBench-R with expected improvement between 2.0-6.0 percentage points, then Plans 005 through 012 cover embedding depth analysis, scalability statistics, and various ablations on hop count, training data size, fusion heads, and distance weighting, plus failure analysis and qualitative examples. Let me structure all of this into the final YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8928be79-7944-4ace-983f-75afdb9001a5",
  "isSidechain": false,
  "requestId": "req_011CayKwCSAvD6H6kzcnzj3f",
  "type": "assistant",
  "uuid": "a11462eb-9d8a-4c4e-b352-d6e0e82bffab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxBaDUM2CF4WEQnGkjXPbX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10873,
      "cache_read_input_tokens": 11447,
      "output_tokens": 10315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10315,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 10873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10873
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

_source line 10 · 2026-05-12T20:48:00.681Z_

```yaml
tier: best
narrative_guidance: >
  All three claims hold with statistical significance. Dataflow-aware negatives produce the largest
  retrieval gains; embedding-distance negatives actively harm; CodeQL scales to 5K repos with acceptable
  timeout. The story is clean: structure-grounded hard negatives provide a complementary signal dimension
  that text similarity cannot recover. EMNLP Main submission with strong empirical backing.

imagined_experiments:
  - name: "M1 全量 CodeQL 提取"
    plan_id: "plan_001"
    description: "5K SWE-smith repos data-flow extraction + connected vs gold statistics"
    expected_results:
      repos_attempted: 5000
      repos_success: 4720
      repos_skipped_no_python: 180
      repos_timeout: 100
      codeql_timeout_pct: 5.2
      total_instances: ~24000
      instances_with_extra_connected: ~10100
      Z_pct: 42.1
      avg_connected_minus_gold: 5.8
      median_extraction_time_s: 38.2
      p95_extraction_time_s: 210
      by_repo_size:
        small_lt50: { Z_pct: 39.5, avg_extra: 2.8 }
        medium_50_200: { Z_pct: 54.2, avg_extra: 10.5 }
        large_gt200: { Z_pct: 18.3, avg_extra: 9.2 }
    result_rationale: >
      50-repo pilot showed Z=40.8%, timeout=4%. At 5K scale, repo size distribution shifts slightly
      toward medium repos in SWE-smith, pushing Z marginally higher to ~42%. Timeout increases modestly
      to ~5% because the long tail of large repos grows — large repos have deeper call graphs that hit
      the 2-hop bound more often, but scope-bounding keeps it under 8%. The medium-repo Z dominance
      (~54%) persists because medium repos have enough inter-module structure to produce connected≠gold
      files but aren't so large that the gold set already covers most connected files. Small repos stay
      ~40% because their shallow call graphs limit reachability. The 42% Z means ~10K instances have
      structurally meaningful hard negatives available — sufficient training signal for contrastive
      learning.
    tables:
      - name: "Table 2: CodeQL Extraction Statistics at Scale"
        columns: ["Repo Size Bucket", "N Repos", "Z%", "Avg Extra Connected", "Timeout %", "Median Time (s)"]
        rows:
          - ["< 50 files", "~2800", "39.5%", "2.8", "2.1%", "18.5"]
          - ["50–200 files", "~1500", "54.2%", "10.5", "6.8%", "52.3"]
          - ["> 200 files", "~420", "18.3%", "9.2", "14.1%", "142.7"]
          - ["All", "~4720", "42.1%", "5.8", "5.2%", "38.2"]
    figures_description:
      - "Fig 2a: Histogram of Z% by repo size bucket, showing medium repos dominate signal availability"
      - "Fig 2b: CDF of extraction time per repo, with vertical line at 300s timeout threshold"
    analysis: >
      Z=42% at 5K scale confirms the 50-repo pilot was representative. The connected≠gold signal is
      robust and not an artifact of small-sample selection. Medium repos are the sweet spot for structural
      negative mining. Timeout at 5.2% is within budget and concentrated in large repos (>200 files),
      which are a minority of the dataset. This validates Claim 3 (scalability) and provides the
      foundation for training experiments.

  - name: "M2 全量 3-strategy 对比训练"
    plan_id: "plan_002"
    description: "random vs embedding_distance vs dataflow_aware, 3 seeds each, Qwen2.5-Coder-3B LoRA"
    expected_results:
      training_instances: ~12000
      epochs: 3
      batch_size: 32
      dataflow_s42: { val_loss: 0.0215, recall@5: 0.862 }
      dataflow_s123: { val_loss: 0.0248, recall@5: 0.849 }
      dataflow_s456: { val_loss: 0.0198, recall@5: 0.871 }
      dataflow_mean: { val_loss: 0.0220, recall@5: 0.861 }
      random_s42: { val_loss: 0.0312, recall@5: 0.792 }
      random_s123: { val_loss: 0.0358, recall@5: 0.778 }
      random_s456: { val_loss: 0.0289, recall@5: 0.801 }
      random_mean: { val_loss: 0.0320, recall@5: 0.790 }
      emb_dist_s42: { val_loss: 0.0485, recall@5: 0.738 }
      emb_dist_s123: { val_loss: 0.0512, recall@5: 0.721 }
      emb_dist_s456: { val_loss: 0.0468, recall@5: 0.745 }
      emb_dist_mean: { val_loss: 0.0488, recall@5: 0.735 }
      delta_dataflow_vs_random_R5: 0.071
      delta_emb_vs_random_R5: -0.055
      val_loss_gap_dataflow_vs_random: 0.010
      paired_t_test_dataflow_vs_random_p: 0.008
      paired_t_test_emb_vs_random_p: 0.012
    result_rationale: >
      At full scale with ~10K instances having valid dataflow negatives, the model receives structurally
      informative contrastive signal that random negatives cannot provide. Random negatives are mostly
      easy (unrelated files) so the model converges quickly to a shallow optimum — val_loss ~0.032.
      Dataflow negatives force the model to distinguish between lexically similar but structurally
      disconnected files, pushing it past the random optimum to val_loss ~0.022. The 0.01 val_loss gap
      is smaller than the 0.02 threshold for "different optimum" but the R@5 gap of +7.1pp is the
      meaningful signal. Embedding-distance negatives are partially redundant with the encoder's own
      similarity — the gradient signal reinforces existing biases rather than correcting them, leading to
      a higher val_loss (~0.049) and lower R@5 (0.735). The MVP evidence already showed this pattern:
      emb_dist val_loss was 5x higher than random. At scale the gap narrows because more training data
      helps all strategies, but the ordering is preserved. Three seeds show low variance (std ~0.01 R@5)
      because the dataset is large enough to stabilize training. Statistical significance at p<0.01
      because the effect is consistent across seeds and the evaluation set is ~2K+ instances.
    tables:
      - name: "Table 3: Main Results — 3-Strategy Contrastive Training"
        columns: ["Strategy", "Val Loss", "R@1", "R@5", "R@10", "Δ vs Random R@5"]
        rows:
          - ["Random (3 seeds)", "0.032 ± 0.004", "0.683 ± 0.018", "0.790 ± 0.012", "0.861 ± 0.009", "—"]
          - ["Embedding-Dist (3 seeds)", "0.049 ± 0.002", "0.621 ± 0.015", "0.735 ± 0.012", "0.808 ± 0.011", "-5.5pp"]
          - ["Dataflow-Aware (3 seeds)", "0.022 ± 0.003", "0.752 ± 0.016", "0.861 ± 0.011", "0.918 ± 0.008", "+7.1pp"]
    figures_description:
      - "Fig 3a: Training loss curves for 3 strategies × 3 seeds, showing dataflow converges to distinct lower optimum"
      - "Fig 3b: R@5 bar chart with error bars (±1 std), showing clear ordering: dataflow > random > emb_dist"
      - "Fig 3c: Per-seed scatter plot of R@5 vs val_loss, 3 strategies color-coded — no overlap between dataflow and random clusters"
    analysis: >
      The 7.1pp R@5 gain is the headline result. Dataflow negatives produce a statistically significant
      improvement (p=0.008) over random, and the ordering dataflow > random > emb_dist is consistent
      across all 9 runs. Embedding-distance negatives harm by 5.5pp, consistent with MVP evidence but
      attenuated by larger training set. The val_loss convergence pattern confirms that dataflow training
      reaches a qualitatively different optimum — the loss curves diverge after epoch 1 and never
      reconverge. This is the core evidence for Claim 1.

  - name: "M3a SWE-bench Lite End-to-End Evaluation"
    plan_id: "plan_003"
    description: "3 strategies × best checkpoint, Qwen3.6-27B agent, 300 SWE-bench Lite instances"
    expected_results:
      n_instances: 300
      agent_model: "Qwen3.6-27B"
      baseline_swerank_resolve_rate: 0.312
      dataflow_retriever_resolve_rate: 0.338
      random_retriever_resolve_rate: 0.318
      emb_dist_retriever_resolve_rate: 0.305
      delta_dataflow_vs_random_pp: 2.0
      delta_dataflow_vs_swerank_pp: 2.6
      delta_emb_vs_random_pp: -1.3
      swebench_lite_resolve_delta_pp: 2.0
      instances_where_retrieval_changed_outcome: 18
      instances_where_dataflow_uniquely_solved: 9
      instances_where_emb_dist_uniquely_failed: 5
    result_rationale: >
      End-to-end resolve rate amplification is inherently noisy — retrieval is one component in a
      multi-step pipeline (retrieval → context selection → patch generation → validation). A 7.1pp R@5
      gain in retrieval translates to ~2pp resolve rate gain because: (1) many instances are solvable
      regardless of retrieval quality (easy fixes in obvious files), (2) some instances fail at patch
      generation regardless of correct retrieval, (3) the agent's own exploration partially compensates
      for retrieval misses. The 2.0pp gain is at the lower end of the best-tier range [1.5, 4.0] but
      is meaningful because SWE-bench Lite has high variance — 2pp on 300 instances is ~6 additional
      solves, which is detectable but not overwhelming. Embedding-distance retriever slightly harms
      resolve rate (-1.3pp) consistent with the retrieval-level findings but attenuated by agent
      compensation. The 18 instances where retrieval changed the outcome are the qualitative gold mine
      for the paper — they demonstrate that structural retrieval surfaces fix-relevant files the agent
      couldn't find on its own.
    tables:
      - name: "Table 4: SWE-bench Lite End-to-End Results"
        columns: ["Retriever", "Resolve Rate", "Δ vs Random", "Δ vs SweRank"]
        rows:
          - ["SweRank (baseline)", "31.2%", "-0.6pp", "—"]
          - ["Random negatives", "31.8%", "—", "+0.6pp"]
          - ["Embedding-Dist negatives", "30.5%", "-1.3pp", "-0.7pp"]
          - ["Dataflow-Aware negatives", "33.8%", "+2.0pp", "+2.6pp"]
    figures_description:
      - "Fig 4: Resolve rate bar chart with 95% bootstrap CI, showing dataflow > random > emb_dist ordering preserved end-to-end"
      - "Fig 5: Venn diagram of solved instances by retriever strategy — highlighting 9 uniquely solved by dataflow"
    analysis: >
      The 2.0pp end-to-end gain confirms Claim 1 transfers from retrieval metrics to downstream task
      performance. The gain is modest but expected given pipeline noise. The 9 uniquely solved instances
      provide strong qualitative evidence — in each case, the dataflow retriever surfaced a fix-relevant
      file that was structurally connected (2-hop reachable) but lexically dissimilar to the bug report.
      This is exactly the complementary signal dimension the paper claims.

  - name: "M3b RepoBench-R Cross-File Retrieval"
    plan_id: "plan_004"
    description: "Retrieval-only evaluation on RepoBench-R, no LLM agent"
    expected_results:
      n_eval_instances: ~5000
      dataflow_R5: 0.724
      random_R5: 0.688
      emb_dist_R5: 0.671
      swerank_baseline_R5: 0.695
      delta_dataflow_vs_random_pp: 3.6
      delta_dataflow_vs_swerank_pp: 2.9
      repobench_R_improvement_pp: 3.6
      MRR_dataflow: 0.618
      MRR_random: 0.582
      MRR_emb_dist: 0.561
    result_rationale: >
      RepoBench-R is a cross-file code completion benchmark where structural dependencies (imports,
      function calls) are central to relevance. Dataflow-trained retrievers have learned to internalize
      structural connectivity signals, so they naturally excel on tasks where the gold reference depends
      on inter-file relationships. The 3.6pp R@5 gain is smaller than the 7.1pp on our own eval set
      because RepoBench-R uses a different gold definition (next-line completion context) that doesn't
      perfectly align with our training objective (bug-fix relevance). The improvement is still in the
      best-tier range [2.0, 6.0] and demonstrates cross-task generalization — the structural signal
      learned from bug-fix training transfers to completion retrieval. Embedding-distance negatives
      again underperform random, though by a smaller margin (1.7pp) because RepoBench-R's distribution
      is less adversarial than SWE-bench.
    tables:
      - name: "Table 5: RepoBench-R Cross-File Retrieval"
        columns: ["Model", "R@1", "R@5", "R@10", "MRR"]
        rows:
          - ["SweRank", "0.582", "0.695", "0.761", "0.591"]
          - ["Ours (Random neg)", "0.576", "0.688", "0.752", "0.582"]
          - ["Ours (Emb-Dist neg)", "0.551", "0.671", "0.738", "0.561"]
          - ["Ours (Dataflow neg)", "0.612", "0.724", "0.789", "0.618"]
    figures_description:
      - "Fig 6: RepoBench-R R@k curves (k=1..20) for 4 models, showing dataflow advantage grows with k"
    analysis: >
      Cross-benchmark generalization validates that the structural signal is not overfit to SWE-bench
      distribution. The R@5 gain of 3.6pp on RepoBench-R, combined with 7.1pp on our eval set and 2.0pp
      end-to-end on SWE-bench Lite, provides a consistent picture across three evaluation settings.
      Notably, dataflow beats SweRank by 2.9pp despite SweRank being trained on a much larger corpus —
      quality of negatives matters more than quantity of training data.

  - name: "Embedding vs Random 深度分析"
    plan_id: "plan_005"
    description: "按 repo size/complexity 分层, 分析 embedding negatives 何时最有害"
    expected_results:
      strata:
        small_repos_lt50:
          emb_vs_random_delta_R5: -0.032
          n_instances: ~4800
        medium_repos_50_200:
          emb_vs_random_delta_R5: -0.071
          n_instances: ~1800
        large_repos_gt200:
          emb_vs_random_delta_R5: -0.089
          n_instances: ~400
      by_query_difficulty:
        easy_bm25_gt08:
          emb_vs_random_delta_R5: -0.018
        hard_bm25_lt04:
          emb_vs_random_delta_R5: -0.092
      correlation_emb_harm_vs_repo_complexity: 0.61
      gradient_redundancy_metric: 0.74
    result_rationale: >
      Embedding-distance negatives are most harmful in larger repos and harder queries because: (1) in
      large repos, lexically similar files are more abundant, so embedding-distance selects negatives
      that are close in the encoder's existing feature space — this creates gradient signal that
      reinforces the encoder's current biases rather than teaching new discriminations. (2) For hard
      queries where BM25 already fails, the encoder's similarity surface is poorly calibrated, and
      embedding-distance negatives compound this miscalibration. In small repos with easy queries, the
      harm is muted because the retrieval task is simple enough that any reasonable negative strategy
      works. The gradient redundancy metric (0.74) quantifies that 74% of the gradient direction from
      embedding-distance negatives overlaps with the gradient from the current encoder's top-ranked
      non-gold files — confirming the "redundant signal" hypothesis from Claim 2.
    tables:
      - name: "Table 6: Embedding-Distance Harm by Repo Complexity"
        columns: ["Stratum", "N", "Emb Δ R@5 vs Random", "Gradient Redundancy"]
        rows:
          - ["Small (< 50 files)", "~4800", "-3.2pp", "0.68"]
          - ["Medium (50–200)", "~1800", "-7.1pp", "0.76"]
          - ["Large (> 200)", "~400", "-8.9pp", "0.82"]
      - name: "Table 7: Embedding-Distance Harm by Query Difficulty"
        columns: ["Difficulty", "N", "Emb Δ R@5 vs Random"]
        rows:
          - ["Easy (BM25 R@5 > 0.8)", "~3500", "-1.8pp"]
          - ["Medium (0.4–0.8)", "~2500", "-5.6pp"]
          - ["Hard (< 0.4)", "~1000", "-9.2pp"]
    figures_description:
      - "Fig 7a: Heatmap of emb_dist harm (Δ R@5 vs random) by repo size × query difficulty"
      - "Fig 7b: Scatter plot of gradient redundancy vs emb harm, showing strong positive correlation"
    analysis: >
      The stratified analysis provides the mechanistic explanation for Claim 2. Embedding-distance
      negatives harm most when the task is hard and the repo is large — precisely the setting where
      structural negatives provide the most value. The gradient redundancy metric is a novel diagnostic
      that could be useful for the community beyond this paper. This analysis strengthens the
      "complementary signal" narrative: embedding negatives fail because they operate in the same
      feature space the encoder already occupies; structural negatives succeed because they introduce
      an orthogonal signal dimension.

  - name: "M1 Scalability Statistics"
    plan_id: "plan_006"
    description: "timeout rate, extraction time, coverage, connected-but-not-gold ratio by repo size"
    expected_results:
      total_repos: 5000
      timeout_rate_pct: 5.2
      mean_extraction_time_s: 41.8
      median_extraction_time_s: 28.5
      p95_extraction_time_s: 198
      p99_extraction_time_s: 285
      coverage_has_cg: 0.96
      coverage_has_df: 0.91
      Z_pct_overall: 42.1
      Z_by_language:
        python: 43.8
        javascript: 38.2
        typescript: 41.5
      extraction_cost_total_cpu_hours: 82
    result_rationale: >
      These are the same extraction as plan_001, reported from a scalability/engineering perspective.
      Timeout at 5.2% is driven almost entirely by repos with >200 files where the 2-hop call graph
      traversal explores a combinatorial number of paths. The scope-bounding (2-hop limit) keeps this
      manageable — without it, timeout would be >20%. Coverage is high (96% call-graph, 91% dataflow)
      because CodeQL's Python/JS/TS extractors are mature. The 5% coverage gap for dataflow is due to
      repos using dynamic features (eval, metaprogramming) that CodeQL cannot resolve statically.
      Total CPU cost of 82 hours for 5K repos means the method is practical for academic labs — a
      single 32-core machine processes the full dataset in ~3 hours wall time.
    tables:
      - name: "Table 8: CodeQL Scalability at 5K Repos"
        columns: ["Metric", "Value"]
        rows:
          - ["Repos processed", "4720 / 5000 (94.4%)"]
          - ["Timeout rate", "5.2%"]
          - ["Median extraction time", "28.5s"]
          - ["P95 extraction time", "198s"]
          - ["Call-graph coverage", "96%"]
          - ["Dataflow coverage", "91%"]
          - ["Z% (connected ≠ gold)", "42.1%"]
          - ["Total CPU cost", "82 hours"]
    figures_description:
      - "Fig 8: Log-scale extraction time distribution by repo size, with timeout threshold marked"
    analysis: >
      Validates Claim 3. CodeQL is practical at academic scale: 82 CPU-hours for 5K repos, <6% timeout,
      >90% coverage. The method is not specific to CodeQL — any static analysis producing a call-graph
      + dataflow graph would work. Cost is dominated by large repos, suggesting a simple repo-size
      filter could reduce timeout to <2% with minimal coverage loss.

  - name: "Ablation: Hop Count (1 vs 2 vs 3)"
    plan_id: "plan_007"
    description: "1-hop vs 2-hop vs 3-hop call-graph bounding"
    expected_results:
      hop_1:
        Z_pct: 28.5
        timeout_pct: 1.2
        R5_dataflow: 0.831
        connected_set_size_mean: 3.2
      hop_2:
        Z_pct: 42.1
        timeout_pct: 5.2
        R5_dataflow: 0.861
        connected_set_size_mean: 8.7
      hop_3:
        Z_pct: 51.8
        timeout_pct: 18.5
        R5_dataflow: 0.852
        connected_set_size_mean: 24.1
    result_rationale: >
      1-hop is too conservative — only direct callers/callees are connected, so Z% drops to 28.5% and
      the connected set is too small (3.2 files avg) to provide diverse negative mining. The retrieval
      gain is real but smaller (R@5=0.831) because the training signal has less structural diversity.
      2-hop is the sweet spot — Z=42%, timeout=5.2%, and the connected set (8.7 files avg) is large
      enough for meaningful negatives without being so large that most files are "connected" (which would
      dilute the negative signal). 3-hop expands the connected set to 24 files on average, which improves
      Z to 52% but the larger connected set means many weakly-connected files are now excluded from the
      negative pool — some of these are genuinely good hard negatives. Additionally, timeout triples to
      18.5% because 3-hop traversal is combinatorially expensive. The R@5 at 3-hop (0.852) is slightly
      worse than 2-hop (0.861) because the structural signal becomes noisier — too many files are
      "connected" and the negative/positive boundary becomes less informative.
    tables:
      - name: "Table 9: Hop Count Ablation"
        columns: ["Hops", "Z%", "Timeout %", "Connected Set Size", "R@5", "Δ vs Random R@5"]
        rows:
          - ["1-hop", "28.5%", "1.2%", "3.2", "0.831", "+4.1pp"]
          - ["2-hop (ours)", "42.1%", "5.2%", "8.7", "0.861", "+7.1pp"]
          - ["3-hop", "51.8%", "18.5%", "24.1", "0.852", "+6.2pp"]
    figures_description:
      - "Fig 9: Line plot of R@5, Z%, and timeout rate vs hop count, showing 2-hop as Pareto-optimal"
    analysis: >
      2-hop is the clear sweet spot. This is an important ablation because it justifies a design choice
      that would otherwise seem arbitrary. The diminishing returns from 2→3 hop (while timeout triples)
      show that the method is not sensitive to the exact hop count — any reasonable scope-bounding works.

  - name: "Ablation: Training Data Size Scaling"
    plan_id: "plan_008"
    description: "1K vs 3K vs 5K training instances"
    expected_results:
      size_1K:
        dataflow_R5: 0.821
        random_R5: 0.768
        delta_pp: 5.3
      size_3K:
        dataflow_R5: 0.848
        random_R5: 0.782
        delta_pp: 6.6
      size_5K:
        dataflow_R5: 0.861
        random_R5: 0.790
        delta_pp: 7.1
      log_linear_fit_r2: 0.97
    result_rationale: >
      Both strategies benefit from more data, but the dataflow advantage grows because more data means
      more instances with valid structural negatives (Z~42% of instances have usable signal). At 1K
      instances, only ~420 have dataflow negatives, which limits the structural signal. At 5K, ~2100
      instances contribute structural negatives, and the model has enough examples to learn the structural
      discrimination pattern. Random negatives also improve with scale but plateau faster because the
      signal from random negatives is less informative — more random negatives are just more easy
      negatives. The dataflow advantage scales roughly log-linearly with data size, suggesting that even
      more data (10K+) would continue to help but with diminishing returns. The delta grows from 5.3pp
      at 1K to 7.1pp at 5K, showing that the structural signal is data-efficient but benefits from scale.
    tables:
      - name: "Table 10: Data Size Scaling"
        columns: ["Training Size", "Dataflow R@5", "Random R@5", "Δ (pp)", "Instances w/ Structural Neg"]
        rows:
          - ["1K", "0.821", "0.768", "+5.3", "~420"]
          - ["3K", "0.848", "0.782", "+6.6", "~1260"]
          - ["5K", "0.861", "0.790", "+7.1", "~2100"]
    figures_description:
      - "Fig 10: Data scaling curves for 3 strategies, log-x axis, showing dataflow scales better"
    analysis: >
      The log-linear scaling confirms that the method is not data-hungry — even 1K instances produce a
      meaningful 5.3pp gain. But the improvement from 1K→5K (+1.8pp) suggests that collecting more
      structural data is worthwhile. This analysis also serves as a practical guide for applying the
      method to new domains where structural data may be expensive to obtain.

  - name: "Ablation: Fusion Head"
    plan_id: "plan_009"
    description: "embedding-only vs structural-features-only vs combined fusion head"
    expected_results:
      embedding_only:
        R5: 0.790
        note: "Equivalent to random-trained baseline"
      structural_only:
        R5: 0.712
        note: "Data-flow features alone, no embedding"
      combined:
        R5: 0.861
        note: "Full model"
      delta_combined_vs_embedding_pp: 7.1
      delta_combined_vs_structural_pp: 14.9
    result_rationale: >
      Structural features alone (is_connected, hop_distance, shared_callees) produce a weak retriever
      (R@5=0.712) because they are sparse and binary — a file is either connected or not, and the
      structural graph doesn't capture all relevance dimensions (e.g., a file can be relevant because
      it defines an error type mentioned in the bug, not because of dataflow). Embedding-only is the
      random baseline (R@5=0.790). The combined model achieves 0.861 because the structural features
      act as a complementary signal that helps the embedding focus on the right region of the file space
      — the structural features filter candidate files, and the embedding ranks within that filtered set.
      The 14.9pp gap between combined and structural-only confirms that embeddings remain essential;
      structure augments but doesn't replace text similarity. The 7.1pp gap between combined and
      embedding-only is the value of the structural signal — exactly matching the main result.
    tables:
      - name: "Table 11: Fusion Head Ablation"
        columns: ["Configuration", "R@1", "R@5", "R@10"]
        rows:
          - ["Embedding only", "0.683", "0.790", "0.861"]
          - ["Structural features only", "0.598", "0.712", "0.778"]
          - ["Combined (ours)", "0.752", "0.861", "0.918"]
    figures_description:
      - "Fig 11: Radar chart comparing 3 configurations across R@1, R@5, R@10, MRR"
    analysis: >
      This ablation decomposes the contribution of each signal source. The structural signal is
      complementary (7.1pp gain when added to embedding) but not sufficient alone (7.8pp below
      embedding-only). This supports the "complementary signal dimension" pillar of the paper's
      motivation and shows that the method enhances rather than replaces existing retrieval.

  - name: "Ablation: Distance-Weighted vs Binary"
    plan_id: "plan_010"
    description: "dataflow-distance weighted negatives vs binary connected/disconnected"
    expected_results:
      binary:
        R5: 0.861
      weighted_linear:
        R5: 0.858
      weighted_inverse:
        R5: 0.864
      delta_weighted_vs_binary_pp: 0.3
      p_value: 0.42
    result_rationale: >
      The binary connected/disconnected distinction captures most of the signal. Weighted variants
      (using hop-distance as a continuous feature) provide negligible additional gain because: (1) the
      structural graph is already scope-bounded to 2 hops, so the distance range is {0, 1, 2, ∞} —
      too coarse for meaningful weighting; (2) the key discrimination is between connected (any hop
      distance) and disconnected (∞), not between 1-hop and 2-hop connected files. The inverse-weighted
      variant marginally helps (+0.3pp) by upweighting negatives that are close to the connectivity
      boundary, but the effect is not statistically significant (p=0.42). This is a useful negative
      result — it shows the method's simplicity (binary signal) is a feature, not a limitation.
    tables:
      - name: "Table 12: Distance Weighting Ablation"
        columns: ["Weighting", "R@5", "Δ vs Binary"]
        rows:
          - ["Binary (ours)", "0.861", "—"]
          - ["Linear distance", "0.858", "-0.3pp"]
          - ["Inverse distance", "0.864", "+0.3pp (n.s.)"]
    figures_description: []
    analysis: >
      Simplicity validated — binary connected/disconnected is sufficient. This removes a potential
      reviewer concern about hyperparameter sensitivity in the distance weighting scheme.

  - name: "Failure Analysis"
    plan_id: "plan_011"
    description: "50 SweRank/BM25 failures, categorize by whether data-flow helps"
    expected_results:
      failures_analyzed: 50
      categories:
        dataflow_helps_directly: 14
        dataflow_helps_partially: 8
        structural_irrelevant: 18
        gold_unreachable_by_any: 10
      dataflow_help_rate: 0.44
      common_failure_patterns:
        - pattern: "Gold file is utility/helper imported transitively"
          count: 11
          dataflow_helps: true
        - pattern: "Gold file is test file with no structural connection"
          count: 9
          dataflow_helps: false
        - pattern: "Bug is in configuration/data file not in call graph"
          count: 8
          dataflow_helps: false
        - pattern: "Gold file shares API contract but no direct dataflow"
          count: 7
          dataflow_helps: true
        - pattern: "Multiple valid fix locations, gold is one of several"
          count: 6
          dataflow_helps: partial
    result_rationale: >
      44% of baseline failures are helped by dataflow because the most common retrieval failure mode
      is missing transitively-imported utility files — these are structurally connected but lexically
      dissimilar to the bug context. The 18 structurally-irrelevant failures (36%) are cases where the
      gold file is a test, config, or data file that has no call-graph relationship to the bug — these
      represent the ceiling of structural methods. The 10 unreachable-by-any cases (20%) are instances
      where the gold patch touches files that no retrieval method could reasonably surface (e.g.,
      documentation files, or files added in the fix that don't exist yet). The 44% help rate is
      consistent with Z=42% — roughly the same fraction of instances where structural signal exists.
    tables:
      - name: "Table 13: Failure Analysis Categories"
        columns: ["Category", "Count", "% of Failures", "Example"]
        rows:
          - ["Dataflow helps directly", "14", "28%", "Transitively imported utility"]
          - ["Dataflow helps partially", "8", "16%", "API contract without direct flow"]
          - ["Structural signal irrelevant", "18", "36%", "Test/config/data files"]
          - ["Unreachable by any method", "10", "20%", "New files in fix"]
    figures_description:
      - "Fig 12: Sunburst chart of failure categories with representative examples annotated"
    analysis: >
      The failure analysis honestly characterizes the method's scope. Structural negatives help in 44%
      of failure cases — substantial but not universal. The ceiling analysis (20% unreachable) is
      important for reviewer expectations and frames future work: combining structural with other
      signals (test dependencies, git co-change history) could address the remaining 36%.

  - name: "Qualitative Examples"
    plan_id: "plan_012"
    description: "5-10 cases where structural negatives changed retrieval outcome"
    expected_results:
      examples_selected: 8
      categories:
        transitively_connected_utility: 3
        shared_data_pipeline: 2
        cross_module_error_handler: 2
        api_contract_dependency: 1
      format: "Each example includes: bug description, gold file, baseline retrieval rank, dataflow retrieval rank, structural path (call chain), and explanation of why lexical similarity fails"
    result_rationale: >
      The 8 examples are selected to cover the major categories where structural negatives help. Each
      demonstrates the same pattern: the gold file is reachable via 1-2 hop call/dataflow edges but
      shares few lexical tokens with the bug context. Transitively-connected utilities are the most
      common (3 examples) because Python projects heavily use utility modules that are imported through
      intermediate files — BM25 and embedding-based methods miss these because the utility file's
      vocabulary is generic (e.g., "parse", "validate", "convert") while the bug context uses
      domain-specific terms. Cross-module error handlers (2 examples) illustrate a different pattern:
      the error handling code is structurally connected via exception propagation paths that only
      inter-procedural dataflow analysis captures.
    tables: []
    figures_description:
      - "Fig 13: 4 selected examples as 2×2 grid, each showing: call-graph subgraph with gold file highlighted, retrieval rank comparison (baseline vs dataflow), and key code snippets"
    analysis: >
      Qualitative examples make the abstract "complementary signal" claim concrete and intuitive for
      reviewers. The diversity of categories (utilities, pipelines, error handlers, API contracts)
      demonstrates that the structural signal is not limited to one pattern. These examples are
      selected for pedagogical value, not cherry-picked for maximum effect — the failure analysis
      (plan_011) provides the honest aggregate picture.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a11462eb-9d8a-4c4e-b352-d6e0e82bffab",
  "isSidechain": false,
  "requestId": "req_011CayKwCSAvD6H6kzcnzj3f",
  "type": "assistant",
  "uuid": "4b65801d-413e-4e6a-8d59-e0864991e1ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxBaDUM2CF4WEQnGkjXPbX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10873,
      "cache_read_input_tokens": 11447,
      "output_tokens": 10315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10315,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 10873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10873
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Dataflow negatives produce statistically significant retrieval gains over random; all 3 claims hold; EMNLP Main viable 核心假设：['Z% at 5K-repo scale ≥ 35%, co…",
  "leafUuid": "4b65801d-413e-4e6a-8d59-e0864991e1ca",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Scale dataflow negatives to 5K repos and validate EMNLP claims",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Dataflow negatives produce statistically significant retrieval gains over random; all 3 claims hold; EMNLP Main viable 核心假设：['Z% at 5K-repo scale ≥ 35%, co…",
  "leafUuid": "4b65801d-413e-4e6a-8d59-e0864991e1ca",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Scale dataflow negatives to 5K repos and validate EMNLP claims",
  "sessionId": "97a6a919-58e0-4df7-9f4a-3465cf395004"
}
```

---
