# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Dataflow negatives ≈ random (no clear win), but embedding-harm result is s

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/fcae3eab-b048-4c65-b10d-e118231f4669.jsonl`
- **Structured JSON:** [`6c9dbecb475819788fda.json`](../../sessions/6c/6c9dbecb475819788fda.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T20:48:03.077Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T20:48:03.077Z",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Dataflow negatives ≈ random (no clear win), but embedding-harm result is strong and Z% confirms structural signal exists; Claim 1 weakened, Claims 2+3 hold; reframe needed, EMNLP Findings viable\n核心假设：['Z% at 5K scale moderate (20-35%): structural signal exists but is sparser than hoped', 'Dataflow-aware training shows marginal or inconsistent improvement over random (within noise across seeds)', 'Embedding-distance harm replicates robustly at full scale', 'CodeQL scales acceptably (timeout < 12%)', 'SWE-bench Lite shows no significant resolve rate gain from retriever strategy alone']\n关键指标范围：{'Z_pct_5K': [20, 35], 'codeql_timeout_pct_5K': [4, 12], 'retrieval_R5_dataflow': [0.76, 0.84], 'retrieval_R5_random': [0.74, 0.83], 'retrieval_R5_emb_dist': [0.7, 0.79], 'delta_dataflow_vs_random_R5': [-0.01, 0.03], 'delta_emb_vs_random_R5': [-0.06, -0.02], 'swebench_lite_resolve_delta_pp': [-0.5, 1.5], 'repobench_R_improvement_pp': [-1.0, 2.0]}\n叙事方向：Pivot primary claim from \"dataflow wins\" to \"embedding-distance negatives are harmful — a cautionary result for the contrastive code retrieval community.\" Claim 2 becomes the headline; Claim 1 downgrades to \"dataflow negatives are a viable alternative that avoids the pitfalls of embedding-distance negatives without degrading performance.\" Claim 3 (scalability methodology) survives as-is. Add ceiling analysis: why doesn't structural signal help more? Hypotheses include insufficient Z% density, noise in CodeQL reachability, or random negatives already being near-optimal when pool diversity is high. Failure analysis (plan_011) becomes critical for explaining the gap. Title pivot: emphasize \"when hard negatives hurt\" angle. Target: EMNLP Findings or resubmit cycle.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: faith-evidence-ie\nfocus: Key risk: dataflow negatives showed connected⊆gold at MVP scale (8 repos) but Z=40.8% at 50-repo scale. Full-scale training may reveal the effect is weaker than hypothesized. Also: embedding-distance negatives actively harm (-3.7pp R@1), which is a strong negative result supporting the dual-pillar motivation. Reviewers should stress-test whether the connected≠gold signal at scale (40.8%) is sufficient to produce meaningful training differentiation, and whether the improvement magnitude will be large enough for EMNLP acceptance.\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Structure-grounded hard negatives outperform embedding-distance and random negatives for contrastive code retrieval training.** Inter-procedural data-flow connectivity provides a complementary signal dimension that textual similarity cannot recover — files that are lexically similar but structurally disconnected force the model to internalize structural relevance beyond surface features.\n\n2. **Embedding-distance hard negatives actively harm code retrieval compared to random negatives.** The gradient signal from embedding-distance negatives is partially redundant with the encoder's learned similarity, leading to degraded retrieval quality. (MVP evidence: -3.7pp recall@1 at pool=50, -27pp at pool=26, 3 seeds consistent.)\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** With 2-hop call-graph bounding, timeout <5%, and >40% of instances have connected-but-not-gold structural signals at scale.\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers conflate lexical similarity with structural relevance — a file sharing function names with the buggy code may be structurally unrelated, while a data-flow-connected file may contain the actual fix dependency.\n\n- **Existing approaches & gaps**:\n  - Text-based (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no data-flow edges, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: hard negatives improve code search, but embedding-distance negatives are redundant with encoder similarity\n\n- **Our framing**: The key gap is using structural connectivity for **training signal**, not just inference-time navigation. Structure-grounded hard negatives — lexically similar but data-flow disconnected files — provide a complementary learning signal. This is a general paradigm: any domain with external structural knowledge (molecular networks, circuit topology, KG retrieval) can use drift-immune structure-grounded negative mining. Code is the ideal testbed due to formal semantic guarantees.\n\n- **Headline result template**: \"On SWE-bench Lite, StructFuse with data-flow-aware hard negatives achieves X% recall@5 while embedding-distance negatives achieve Y% and random negatives Z%, demonstrating that structure-grounded negative mining provides training signal that text-based methods cannot recover.\"\n\n## Dual-Pillar Motivation (per Human Review)\n\n1. **Primary — Complementary signal dimension**: Structural connectivity encodes a relevance dimension entirely absent from textual signals. No amount of text-based training can recover inter-procedural data-flow relationships from token sequences alone.\n2. **Secondary — Selection drift immunity**: Structural graph is externally fixed; negative set does not drift with encoder updates (unlike embedding-distance negatives which shift every epoch).\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder.\n\n## Title\n\n\"StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval\"\n(Per Human Review: emphasize methodology, de-emphasize SE-specific framing)\n\n## Venue Fit Risks\n\n1. **EMNLP vs SE**: Frame as contrastive learning methodology with code as instantiation\n2. **Domain-specific concern**: Cross-domain generalization in Discussion (molecular networks, circuit topology, KG retrieval)\n3. **Incremental contribution**: Novelty is in WHAT generates negatives (program analysis), not the objective itself\n4. **CodeQL dependency**: CodeQL is one instantiation; any structural analysis producing a connectivity graph works\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Too domain-specific | Cross-domain generalization + formal definition is domain-agnostic | Discussion section |\n| Why not ARISE? | Intra-procedural only + inference-time only; we cross call boundaries + train | Direct comparison in ablation |\n| CodeQL scalability | 0% timeout at pilot, 4% at 50-repo scale; scope-bounded 2-hop | P1 + scale check |\n| Small improvement | Training methodology contribution, not benchmark chasing; improvement ceiling analysis | Failure analysis |\n| connected⊆gold? | Scale effect: 40.8% instances have connected≠gold at 50-repo scale | M1 full statistics |\n\n## MVP Evidence Summary\n\n- P1: CodeQL feasible (timeout 0%, Fisher p=1.54e-7, instance recall 75%)\n- P2a: DataFlow feature AUC=0.78, BM25 coefficient negative (-1.80)\n- P2b: random >> embedding_distance (-3.7pp R@1 at pool=50); dataflow untestable at MVP scale but viable at full scale (Z=40.8%)\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: QUEUED\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-12T20:48:03.080Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T20:48:03.080Z",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669"
}
```

---

## Round 1

20 recorded events

### User

_source line 3 · 2026-05-12T20:48:03.102Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Dataflow negatives ≈ random (no clear win), but embedding-harm result is strong and Z% confirms structural signal exists; Claim 1 weakened, Claims 2+3 hold; reframe needed, EMNLP Findings viable
核心假设：['Z% at 5K scale moderate (20-35%): structural signal exists but is sparser than hoped', 'Dataflow-aware training shows marginal or inconsistent improvement over random (within noise across seeds)', 'Embedding-distance harm replicates robustly at full scale', 'CodeQL scales acceptably (timeout < 12%)', 'SWE-bench Lite shows no significant resolve rate gain from retriever strategy alone']
关键指标范围：{'Z_pct_5K': [20, 35], 'codeql_timeout_pct_5K': [4, 12], 'retrieval_R5_dataflow': [0.76, 0.84], 'retrieval_R5_random': [0.74, 0.83], 'retrieval_R5_emb_dist': [0.7, 0.79], 'delta_dataflow_vs_random_R5': [-0.01, 0.03], 'delta_emb_vs_random_R5': [-0.06, -0.02], 'swebench_lite_resolve_delta_pp': [-0.5, 1.5], 'repobench_R_improvement_pp': [-1.0, 2.0]}
叙事方向：Pivot primary claim from "dataflow wins" to "embedding-distance negatives are harmful — a cautionary result for the contrastive code retrieval community." Claim 2 becomes the headline; Claim 1 downgrades to "dataflow negatives are a viable alternative that avoids the pitfalls of embedding-distance negatives without degrading performance." Claim 3 (scalability methodology) survives as-is. Add ceiling analysis: why doesn't structural signal help more? Hypotheses include insufficient Z% density, noise in CodeQL reachability, or random negatives already being near-optimal when pool diversity is high. Failure analysis (plan_011) becomes critical for explaining the gap. Title pivot: emphasize "when hard negatives hurt" angle. Target: EMNLP Findings or resubmit cycle.


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
  "promptId": "1919b124-0c98-4c22-a170-3a07ef4b12f7",
  "type": "user",
  "uuid": "b4c4c30b-551c-47fa-9a0b-cea59ce52d2f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T20:48:03.101Z_

```json
{
  "parentUuid": "b4c4c30b-551c-47fa-9a0b-cea59ce52d2f",
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
  "uuid": "ea10c1de-71dd-482b-8726-953503186a09",
  "timestamp": "2026-05-12T20:48:03.101Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T20:48:03.101Z_

```json
{
  "parentUuid": "ea10c1de-71dd-482b-8726-953503186a09",
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
  "uuid": "de772576-2f64-451f-a8c8-67e3533c533d",
  "timestamp": "2026-05-12T20:48:03.101Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-12T20:48:03.101Z_

```json
{
  "parentUuid": "de772576-2f64-451f-a8c8-67e3533c533d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "eed20764-d09c-43de-b1e6-9cffc7f960c0",
  "timestamp": "2026-05-12T20:48:03.101Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Dataflow negatives ≈ random (no clear win), but embedding-harm result is strong and Z% confirms structural signal exists; Claim 1 weakened, Claims 2+3 ho…",
  "leafUuid": "eed20764-d09c-43de-b1e6-9cffc7f960c0",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling structure-grounded hard negatives to 5K repos",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669"
}
```

---

### Assistant

_source line 9 · 2026-05-12T20:48:06.032Z_

I'll review the experiment plan and project context to generate detailed median-tier predictions for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eed20764-d09c-43de-b1e6-9cffc7f960c0",
  "isSidechain": false,
  "requestId": "req_011CayLC4kUfDXCyfewjZktQ",
  "type": "assistant",
  "uuid": "f79059fe-fb0c-4a31-a4e8-eb1aab48f3f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WbWtx5JU2z5G9ogbx9239Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10969,
      "cache_read_input_tokens": 11447,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 252,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 10969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10969
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

_source line 10 · 2026-05-12T20:48:16.310Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011wFoonFXTY1JfR3HBwC4pg`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment configs and data",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5, I need to understand the experiment setup details. Search for:\n1. Any training config files (hyperparameters, model configs, LoRA settings)\n2. Any evaluation scripts or configs for SWE-bench Lite and RepoBench-R\n3. The CodeQL extraction pipeline config\n4. Any existing results files or analysis notebooks\n5. The negative sampling implementation (especially dataflow-aware vs random vs embedding-distance)\n\nSearch breadth: very thorough. Report file paths and key parameter values you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f79059fe-fb0c-4a31-a4e8-eb1aab48f3f6",
  "isSidechain": false,
  "requestId": "req_011CayLC4kUfDXCyfewjZktQ",
  "type": "assistant",
  "uuid": "cb828015-c53c-46c6-be75-762966f61d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WbWtx5JU2z5G9ogbx9239Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10969,
      "cache_read_input_tokens": 11447,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 252,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 10969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10969
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

_source line 11 · 2026-05-12T20:49:35.236Z_

<details><summary>↩ Tool result · `toolu_011wFoonFXTY1JfR3HBwC4pg`</summary>

```text
Excellent! Now let me compile a comprehensive summary report:

## Comprehensive Experiment Setup Analysis

Based on my thorough search of the project, here's the complete experiment setup documentation:

### 1. TRAINING CONFIG FILES & HYPERPARAMETERS

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/training/train.py` (lines 414-442)

**Key Hyperparameters:**
- **Model**: Qwen/Qwen2.5-Coder-3B (3B parameter bi-encoder)
- **Batch Size**: 8
- **Learning Rate**: 2e-5 (AdamW optimizer with weight_decay=0.01)
- **Number of Epochs**: 3
- **Warmup Ratio**: 0.1 (linear warmup)
- **Gradient Clipping**: max_norm=1.0
- **Scheduler**: Cosine schedule with warmup
- **Max Sequence Length**: 2048 tokens
- **Seed**: 42 (default)
- **Evaluation Interval**: every 500 steps
- **Checkpoint Interval**: every 1000 steps
- **Projection Dimension**: 256 (after backbone hidden_size)
- **Learnable Temperature**: 0.07 (log-transformed, trainable parameter)
- **W&B Logging**: enabled (project name: "structfuse")

### 2. LoRA CONFIGURATION

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/training/contrastive_model.py` (lines 94-105)

**LoRA Settings (when `--use-lora` flag enabled):**
- **LoRA Rank (r)**: 16 (default, configurable via `--lora-r`)
- **LoRA Alpha**: r × 2 = 32
- **Target Modules**: ["q_proj", "v_proj"] (attention heads only)
- **LoRA Dropout**: 0.05
- **Bias**: "none"
- **Task Type**: FEATURE_EXTRACTION

**Optional Fusion Head:**
- Hidden dimension: 128 MLP layers
- Input features: embedding similarity + 5 structural features
- Output: scalar relevance score

### 3. EVALUATION SCRIPTS & CONFIGS

#### 3a. SWE-bench Lite Evaluation
**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/evaluation/eval_swebench.py`

**Key Parameters:**
- **LLM Endpoint**: http://localhost:8000/v1 (vLLM server)
- **LLM Model**: Qwen/Qwen3.6-27B
- **SWE-bench Split**: lite (default), verified, or pro
- **Max Context Tokens**: 16,000
- **Max Generation Tokens**: 4,096
- **vLLM Temperature**: 0.0 (deterministic)
- **Parallel Workers**: 4
- **Timeout per Instance**: 600 seconds
- **Retrieval Top-k**: 10 files

**Output Metrics:**
- Pass@1 (test success rate)
- Average tokens used per instance
- Average retrieval recall@10
- Per-instance results: retrieved files, generated patch, test status

#### 3b. Retrieval Evaluation (SWE-bench Lite & RepoBench-R)
**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/evaluation/eval_retrieval.py`

**Key Parameters:**
- **Batch Size**: 32 (encoding)
- **Max Sequence Length**: 2048
- **Top-k Values**: 1, 5, 10 (for Recall@k)
- **Dataset Support**: swebench_lite, repobench, custom

**Evaluation Metrics:**
- Recall@1/5/10 (gold files in top-k)
- MRR (Mean Reciprocal Rank)
- Structural Precision (fraction of retrieved files in dataflow reachability set)

**Fusion Ranker Weights (optional):**
- BM25 weight: 0.2
- Data-flow signal weight: 0.3
- StructFuse embedding weight: 0.5

**Retrieval Pipeline:**
1. BM25 coarse retrieval (top 30 candidates)
2. Optional data-flow filter (keep only reachable files if ≥3 remain)
3. StructFuse bi-encoder re-ranking
4. Optional fusion re-ranking (combines all signals)

### 4. CODEQL EXTRACTION PIPELINE CONFIG

**Files**: 
- Call Graph: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/call_graph.ql`
- Data-flow: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/bounded_dataflow.ql`

**Extraction Parameters** (`extract_dataflow.py`):
- **CodeQL Timeout**: 300 seconds per query
- **CodeQL RAM Limit**: 8192 MB
- **Min Reachable Files Threshold**: 5 (fallback to Beniget if CodeQL finds fewer)
- **Num Workers**: 4 (multiprocessing parallel)

**Call Graph Analysis:**
- **Scope**: 2-hop bidirectional call graph from buggy function
- **Direction**: both "caller" (functions calling buggy) and "callee" (functions called by buggy)
- **Hop Distances**: 0 (origin), 1 (direct), 2 (indirect)
- **Resolution Strategy**: Points-to analysis with name-based fallback

**Data-flow Analysis:**
- **Scope**: inter-procedural data-flow within 2-hop functions
- **Sources**: parameters and return values of in-scope functions
- **Sinks**: variable reads within in-scope functions
- **Bound Type**: scope-bounded (sources/sinks restricted BEFORE evaluation)

**Fallback**: Beniget (intra-file def-use chains via AST)

### 5. TRAINING DATA BUILD CONFIG

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/build_training_data.py`

**Parameters:**
- **Num Negatives**: 7 (default)
- **Hard Negative Ratio**: 0.5 (50% hard, 50% random)
- **Max Sequence Length**: 2048

**Hard Negative Sampling (dataflow-aware):**
- **Hard Strategy**: BM25-similar but structurally disconnected files
- **Random Strategy**: uniform random non-positive files
- Selection: top-k by BM25 score from files NOT in connected_files set

**Feature Vector (5 dimensions):**
1. `dataflow_distance`: min path length from buggy function (999 if disconnected)
2. `dataflow_path_count`: # of distinct data-flow paths
3. `dependency_type`: 1.0 if inter-procedural, 0.0 if intra-file
4. `bm25_score`: BM25 relevance score
5. `inter_procedural`: metadata flag

**Positive Weighting:**
- Formula: `exp(-alpha * dataflow_distance)` where alpha = 1.0
- Applied per-sample during InfoNCE loss computation

### 6. NEGATIVE SAMPLING IMPLEMENTATION

**Three Strategies** (in `hard_negative_mining.py`, lines 1-218):

#### Strategy 1: Random (`RandomMiner`)
- Uniformly random non-positive files from same repo
- **Hardness Score**: 0.0

#### Strategy 2: Embedding Distance (`EmbeddingDistanceMiner`, CoCoHaNeRe baseline)
- Top-k candidates by cosine similarity to query embedding
- Uses pre-computed .npz embeddings
- **Hardness Score**: cosine similarity value

#### Strategy 3: Data-flow-aware (`DataFlowAwareMiner`, novel)
- **Core Logic** (lines 126-154):
  1. Get top-50 similar candidates by embedding distance
  2. Filter to those NOT reachable via data-flow (contradictive to gold path)
  3. Optional BM25 re-ranking within disconnected set
  4. Fallback: pad with random if &lt;K disconnected candidates exist
- **Intuition**: Files that look related (high embedding sim) but have no data-flow path provide strongest contrastive signal
- **Hardness Score**: from embeddings (later rescored by BM25 if available)

### 7. EXPERIMENT RESULTS & ANALYSIS FILES

**Phase 1 - CodeQL Feasibility** (completed):
- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md`
- **Results**: 
  - CodeQL timeout rate: 0%
  - Call graph mean time: 29.6s, max: 119.8s
  - Data-flow mean time: 43.4s, max: 167.1s
  - Gold file coverage in connected files: 100% (8/8)
  - Fisher p-value: 6.5e-09 (highly significant difference between connected vs disconnected)

**Phase 2a - Linear Proxy Validation** (completed):
- Data-flow + BM25 Logistic Regression
- **Results**:
  - AUC: 0.78 (vs 0.476 for BM25-only, +60% improvement)
  - MRR: 0.556 (vs 0.115, +384% improvement)
  - F1: 0.143 (vs 0.039)
  - Top feature weight: `is_connected` (+2.82)

**Phase 2b - Contrastive Training** (in progress/partial):
- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md`
- Status: 1 of 9 seeds completed (Run 1, s42)
- Issue: ModelScope concurrent download caused safetensors file corruption in subsequent runs

**50-Repo Overlap Analysis** (completed):
- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/_project/report/50repo_overlap_report.md`
- **Key Results**:
  - 40.8% of instances have connected-but-not-gold files (threshold: ≥20% needed)
  - CodeQL success rate: 64.2% (154/240)
  - Average connected files: 6.0
  - Best performance on medium repos (50-200 files): 55.7%
  - Validates that structured negatives method is viable at scale

### 8. EXPERIMENT PLAN

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/experiment_plan.yaml`

**GPU Budget Summary:**
- P0 (Priority): ~70 GPU hours (training 30h + SWE-bench eval 40h)
- P1 (Medium): ~70 GPU hours (RepoBench 15h + ablations 55h)
- P2 (Low): ~10 GPU hours
- **Total**: ~150 GPU hours + ~10 CPU hours

**Key Hypotheses:**
- H1: CodeQL 2-hop analysis timeout <30%
- H2: Gold file coverage in connected files >> disconnected (confirmed: p=6.5e-09)
- Main claim: Dataflow-aware hard negatives outperform embedding distance and random

### 9. DEPENDENCIES

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/requirements.txt`

Core: torch≥2.2.0, transformers≥4.40.0, accelerate≥0.28.0, peft≥0.10.0
Data: datasets≥2.18.0, rank-bm25≥0.2.2, numpy≥1.24.0
Retrieval: faiss-cpu≥1.7.4
Analysis: beniget≥0.4.0, tree-sitter≥0.21.0
Monitoring: wandb≥0.16.0, vllm≥0.4.0

### Key Takeaways

1. **Training**: Qwen2.5-Coder-3B with LoRA (r=16), InfoNCE loss, data-flow-weighted positives, dynamic hard-negative mining
2. **Hard Negatives**: Three strategies tested—novel dataflow-aware mining selects lexically-similar but structurally-disconnected files
3. **Evaluation**: Retrieval metrics (Recall@k, MRR, Structural Precision) on SWE-bench Lite & RepoBench-R; end-to-end via vLLM Qwen3.6-27B
4. **CodeQL**: 2-phase analysis (call graph + bounded data-flow) with Beniget fallback; 4% timeout rate, strong statistical signal (p=6.5e-09)
5. **Scale Validation**: 40.8% of 240 SWE-smith instances have connected-but-not-gold files, confirming viability of method
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb828015-c53c-46c6-be75-762966f61d5b",
  "isSidechain": false,
  "promptId": "1919b124-0c98-4c22-a170-3a07ef4b12f7",
  "type": "user",
  "uuid": "461a5151-b37f-486e-9677-691ce46eaaea",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5, I need to understand the experiment setup details. Search for:\n1. Any training config files (hyperparameters, model configs, LoRA settings)\n2. Any evaluation scripts or configs for SWE-bench Lite and RepoBench-R\n3. The CodeQL extraction pipeline config\n4. Any existing results files or analysis notebooks\n5. The negative sampling implementation (especially dataflow-aware vs random vs embedding-distance)\n\nSearch breadth: very thorough. Report file paths and key parameter values you find.",
    "agentId": "a2d09ada1d480f844",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now let me compile a comprehensive summary report:\n\n## Comprehensive Experiment Setup Analysis\n\nBased on my thorough search of the project, here's the complete experiment setup documentation:\n\n### 1. TRAINING CONFIG FILES & HYPERPARAMETERS\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/training/train.py` (lines 414-442)\n\n**Key Hyperparameters:**\n- **Model**: Qwen/Qwen2.5-Coder-3B (3B parameter bi-encoder)\n- **Batch Size**: 8\n- **Learning Rate**: 2e-5 (AdamW optimizer with weight_decay=0.01)\n- **Number of Epochs**: 3\n- **Warmup Ratio**: 0.1 (linear warmup)\n- **Gradient Clipping**: max_norm=1.0\n- **Scheduler**: Cosine schedule with warmup\n- **Max Sequence Length**: 2048 tokens\n- **Seed**: 42 (default)\n- **Evaluation Interval**: every 500 steps\n- **Checkpoint Interval**: every 1000 steps\n- **Projection Dimension**: 256 (after backbone hidden_size)\n- **Learnable Temperature**: 0.07 (log-transformed, trainable parameter)\n- **W&B Logging**: enabled (project name: \"structfuse\")\n\n### 2. LoRA CONFIGURATION\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/training/contrastive_model.py` (lines 94-105)\n\n**LoRA Settings (when `--use-lora` flag enabled):**\n- **LoRA Rank (r)**: 16 (default, configurable via `--lora-r`)\n- **LoRA Alpha**: r × 2 = 32\n- **Target Modules**: [\"q_proj\", \"v_proj\"] (attention heads only)\n- **LoRA Dropout**: 0.05\n- **Bias**: \"none\"\n- **Task Type**: FEATURE_EXTRACTION\n\n**Optional Fusion Head:**\n- Hidden dimension: 128 MLP layers\n- Input features: embedding similarity + 5 structural features\n- Output: scalar relevance score\n\n### 3. EVALUATION SCRIPTS & CONFIGS\n\n#### 3a. SWE-bench Lite Evaluation\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/evaluation/eval_swebench.py`\n\n**Key Parameters:**\n- **LLM Endpoint**: http://localhost:8000/v1 (vLLM server)\n- **LLM Model**: Qwen/Qwen3.6-27B\n- **SWE-bench Split**: lite (default), verified, or pro\n- **Max Context Tokens**: 16,000\n- **Max Generation Tokens**: 4,096\n- **vLLM Temperature**: 0.0 (deterministic)\n- **Parallel Workers**: 4\n- **Timeout per Instance**: 600 seconds\n- **Retrieval Top-k**: 10 files\n\n**Output Metrics:**\n- Pass@1 (test success rate)\n- Average tokens used per instance\n- Average retrieval recall@10\n- Per-instance results: retrieved files, generated patch, test status\n\n#### 3b. Retrieval Evaluation (SWE-bench Lite & RepoBench-R)\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/evaluation/eval_retrieval.py`\n\n**Key Parameters:**\n- **Batch Size**: 32 (encoding)\n- **Max Sequence Length**: 2048\n- **Top-k Values**: 1, 5, 10 (for Recall@k)\n- **Dataset Support**: swebench_lite, repobench, custom\n\n**Evaluation Metrics:**\n- Recall@1/5/10 (gold files in top-k)\n- MRR (Mean Reciprocal Rank)\n- Structural Precision (fraction of retrieved files in dataflow reachability set)\n\n**Fusion Ranker Weights (optional):**\n- BM25 weight: 0.2\n- Data-flow signal weight: 0.3\n- StructFuse embedding weight: 0.5\n\n**Retrieval Pipeline:**\n1. BM25 coarse retrieval (top 30 candidates)\n2. Optional data-flow filter (keep only reachable files if ≥3 remain)\n3. StructFuse bi-encoder re-ranking\n4. Optional fusion re-ranking (combines all signals)\n\n### 4. CODEQL EXTRACTION PIPELINE CONFIG\n\n**Files**: \n- Call Graph: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/call_graph.ql`\n- Data-flow: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/bounded_dataflow.ql`\n\n**Extraction Parameters** (`extract_dataflow.py`):\n- **CodeQL Timeout**: 300 seconds per query\n- **CodeQL RAM Limit**: 8192 MB\n- **Min Reachable Files Threshold**: 5 (fallback to Beniget if CodeQL finds fewer)\n- **Num Workers**: 4 (multiprocessing parallel)\n\n**Call Graph Analysis:**\n- **Scope**: 2-hop bidirectional call graph from buggy function\n- **Direction**: both \"caller\" (functions calling buggy) and \"callee\" (functions called by buggy)\n- **Hop Distances**: 0 (origin), 1 (direct), 2 (indirect)\n- **Resolution Strategy**: Points-to analysis with name-based fallback\n\n**Data-flow Analysis:**\n- **Scope**: inter-procedural data-flow within 2-hop functions\n- **Sources**: parameters and return values of in-scope functions\n- **Sinks**: variable reads within in-scope functions\n- **Bound Type**: scope-bounded (sources/sinks restricted BEFORE evaluation)\n\n**Fallback**: Beniget (intra-file def-use chains via AST)\n\n### 5. TRAINING DATA BUILD CONFIG\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/build_training_data.py`\n\n**Parameters:**\n- **Num Negatives**: 7 (default)\n- **Hard Negative Ratio**: 0.5 (50% hard, 50% random)\n- **Max Sequence Length**: 2048\n\n**Hard Negative Sampling (dataflow-aware):**\n- **Hard Strategy**: BM25-similar but structurally disconnected files\n- **Random Strategy**: uniform random non-positive files\n- Selection: top-k by BM25 score from files NOT in connected_files set\n\n**Feature Vector (5 dimensions):**\n1. `dataflow_distance`: min path length from buggy function (999 if disconnected)\n2. `dataflow_path_count`: # of distinct data-flow paths\n3. `dependency_type`: 1.0 if inter-procedural, 0.0 if intra-file\n4. `bm25_score`: BM25 relevance score\n5. `inter_procedural`: metadata flag\n\n**Positive Weighting:**\n- Formula: `exp(-alpha * dataflow_distance)` where alpha = 1.0\n- Applied per-sample during InfoNCE loss computation\n\n### 6. NEGATIVE SAMPLING IMPLEMENTATION\n\n**Three Strategies** (in `hard_negative_mining.py`, lines 1-218):\n\n#### Strategy 1: Random (`RandomMiner`)\n- Uniformly random non-positive files from same repo\n- **Hardness Score**: 0.0\n\n#### Strategy 2: Embedding Distance (`EmbeddingDistanceMiner`, CoCoHaNeRe baseline)\n- Top-k candidates by cosine similarity to query embedding\n- Uses pre-computed .npz embeddings\n- **Hardness Score**: cosine similarity value\n\n#### Strategy 3: Data-flow-aware (`DataFlowAwareMiner`, novel)\n- **Core Logic** (lines 126-154):\n  1. Get top-50 similar candidates by embedding distance\n  2. Filter to those NOT reachable via data-flow (contradictive to gold path)\n  3. Optional BM25 re-ranking within disconnected set\n  4. Fallback: pad with random if &lt;K disconnected candidates exist\n- **Intuition**: Files that look related (high embedding sim) but have no data-flow path provide strongest contrastive signal\n- **Hardness Score**: from embeddings (later rescored by BM25 if available)\n\n### 7. EXPERIMENT RESULTS & ANALYSIS FILES\n\n**Phase 1 - CodeQL Feasibility** (completed):\n- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md`\n- **Results**: \n  - CodeQL timeout rate: 0%\n  - Call graph mean time: 29.6s, max: 119.8s\n  - Data-flow mean time: 43.4s, max: 167.1s\n  - Gold file coverage in connected files: 100% (8/8)\n  - Fisher p-value: 6.5e-09 (highly significant difference between connected vs disconnected)\n\n**Phase 2a - Linear Proxy Validation** (completed):\n- Data-flow + BM25 Logistic Regression\n- **Results**:\n  - AUC: 0.78 (vs 0.476 for BM25-only, +60% improvement)\n  - MRR: 0.556 (vs 0.115, +384% improvement)\n  - F1: 0.143 (vs 0.039)\n  - Top feature weight: `is_connected` (+2.82)\n\n**Phase 2b - Contrastive Training** (in progress/partial):\n- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md`\n- Status: 1 of 9 seeds completed (Run 1, s42)\n- Issue: ModelScope concurrent download caused safetensors file corruption in subsequent runs\n\n**50-Repo Overlap Analysis** (completed):\n- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/_project/report/50repo_overlap_report.md`\n- **Key Results**:\n  - 40.8% of instances have connected-but-not-gold files (threshold: ≥20% needed)\n  - CodeQL success rate: 64.2% (154/240)\n  - Average connected files: 6.0\n  - Best performance on medium repos (50-200 files): 55.7%\n  - Validates that structured negatives method is viable at scale\n\n### 8. EXPERIMENT PLAN\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/experiment_plan.yaml`\n\n**GPU Budget Summary:**\n- P0 (Priority): ~70 GPU hours (training 30h + SWE-bench eval 40h)\n- P1 (Medium): ~70 GPU hours (RepoBench 15h + ablations 55h)\n- P2 (Low): ~10 GPU hours\n- **Total**: ~150 GPU hours + ~10 CPU hours\n\n**Key Hypotheses:**\n- H1: CodeQL 2-hop analysis timeout <30%\n- H2: Gold file coverage in connected files >> disconnected (confirmed: p=6.5e-09)\n- Main claim: Dataflow-aware hard negatives outperform embedding distance and random\n\n### 9. DEPENDENCIES\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/requirements.txt`\n\nCore: torch≥2.2.0, transformers≥4.40.0, accelerate≥0.28.0, peft≥0.10.0\nData: datasets≥2.18.0, rank-bm25≥0.2.2, numpy≥1.24.0\nRetrieval: faiss-cpu≥1.7.4\nAnalysis: beniget≥0.4.0, tree-sitter≥0.21.0\nMonitoring: wandb≥0.16.0, vllm≥0.4.0\n\n### Key Takeaways\n\n1. **Training**: Qwen2.5-Coder-3B with LoRA (r=16), InfoNCE loss, data-flow-weighted positives, dynamic hard-negative mining\n2. **Hard Negatives**: Three strategies tested—novel dataflow-aware mining selects lexically-similar but structurally-disconnected files\n3. **Evaluation**: Retrieval metrics (Recall@k, MRR, Structural Precision) on SWE-bench Lite & RepoBench-R; end-to-end via vLLM Qwen3.6-27B\n4. **CodeQL**: 2-phase analysis (call graph + bounded data-flow) with Beniget fallback; 4% timeout rate, strong statistical signal (p=6.5e-09)\n5. **Scale Validation**: 40.8% of 240 SWE-smith instances have connected-but-not-gold files, confirming viability of method"
      }
    ],
    "totalDurationMs": 78918,
    "totalTokens": 89307,
    "totalToolUseCount": 36,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1518,
      "cache_read_input_tokens": 84384,
      "output_tokens": 3399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 3399,
          "cache_read_input_tokens": 84384,
          "cache_creation_input_tokens": 1518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1518,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 16,
      "searchCount": 4,
      "bashCount": 16,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "cb828015-c53c-46c6-be75-762966f61d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T20:49:38.651Z_

<details open><summary>🔧 Tool call — Read · `toolu_013hEXK8LiGjpQMa9HVHHJZj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "461a5151-b37f-486e-9677-691ce46eaaea",
  "isSidechain": false,
  "requestId": "req_011CayLJrnaxzDachUZuc2Rf",
  "type": "assistant",
  "uuid": "edc314ac-9a7f-4b59-a861-5ddf7c2edcbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCA2bivh6vT54hcwHJPM1P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3660,
      "cache_read_input_tokens": 22416,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3660,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 22416,
          "cache_creation_input_tokens": 3660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3660
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

_source line 13 · 2026-05-12T20:49:38.665Z_

<details><summary>↩ Tool result · `toolu_013hEXK8LiGjpQMa9HVHHJZj`</summary>

```text
1	experiments:
2	  # === Claim 1: Structure-grounded negatives > embedding/random ===
3	  - id: plan_001
4	    claim: 1
5	    description: "M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected vs gold statistics"
6	    priority: P0
7	    gpu_budget_hours: 0
8	    deps: []
9	
10	  - id: plan_002
11	    claim: 1
12	    description: "M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware, 3 seeds each, Qwen2.5-Coder-3B LoRA"
13	    priority: P0
14	    gpu_budget_hours: 30
15	    deps: [plan_001]
16	
17	  - id: plan_003
18	    claim: 1
19	    description: "M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best checkpoint, Qwen3.6-27B agent"
20	    priority: P0
21	    gpu_budget_hours: 40
22	    deps: [plan_002]
23	
24	  - id: plan_004
25	    claim: 1
26	    description: "M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no LLM agent"
27	    priority: P1
28	    gpu_budget_hours: 15
29	    deps: [plan_002]
30	
31	  # === Claim 2: Embedding negatives harmful ===
32	  - id: plan_005
33	    claim: 2
34	    description: "Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding negatives 何时最有害"
35	    priority: P1
36	    gpu_budget_hours: 5
37	    deps: [plan_002]
38	
39	  # === Claim 3: CodeQL scalability ===
40	  - id: plan_006
41	    claim: 3
42	    description: "M1 scalability statistics: timeout rate, extraction time, coverage, connected-but-not-gold ratio by repo size"
43	    priority: P0
44	    gpu_budget_hours: 0
45	    deps: [plan_001]
46	
47	  # === Ablations ===
48	  - id: plan_007
49	    claim: 1
50	    description: "Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding"
51	    priority: P1
52	    gpu_budget_hours: 20
53	    deps: [plan_001]
54	
55	  - id: plan_008
56	    claim: 1
57	    description: "Ablation: training data size scaling (1K vs 3K vs 5K instances)"
58	    priority: P1
59	    gpu_budget_hours: 15
60	    deps: [plan_001]
61	
62	  - id: plan_009
63	    claim: 1
64	    description: "Ablation: fusion head (embedding-only vs structural-features-only vs combined)"
65	    priority: P1
66	    gpu_budget_hours: 10
67	    deps: [plan_002]
68	
69	  - id: plan_010
70	    claim: 1
71	    description: "Ablation: dataflow-distance weighted negatives vs binary connected/disconnected"
72	    priority: P2
73	    gpu_budget_hours: 10
74	    deps: [plan_001]
75	
76	  # === Analysis ===
77	  - id: plan_011
78	    claim: 1
79	    description: "Failure analysis: 50 SweRank/BM25 failures, categorize by whether data-flow helps"
80	    priority: P1
81	    gpu_budget_hours: 5
82	    deps: [plan_003]
83	
84	  - id: plan_012
85	    claim: 1
86	    description: "Qualitative examples: 5-10 cases where structural negatives changed retrieval outcome"
87	    priority: P2
88	    gpu_budget_hours: 0
89	    deps: [plan_003]
90	
91	# GPU Budget:
92	# P0: ~70h (M2 30h + M3a 40h) + M1 CPU
93	# P1: ~70h (RepoBench 15h + emb analysis 5h + hop 20h + size 15h + fusion 10h + failure 5h)
94	# P2: ~10h (distance-weighted + qualitative)
95	# Total: ~150h GPU + ~10h CPU
96	# Hardware: 1x RTX 4090D (M2 training) + 1-2x RTX 6000 Pro 96GB (M3a: Qwen3.6-27B >32GB VRAM)
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edc314ac-9a7f-4b59-a861-5ddf7c2edcbe",
  "isSidechain": false,
  "promptId": "1919b124-0c98-4c22-a170-3a07ef4b12f7",
  "type": "user",
  "uuid": "3db5f030-5a58-4d1a-8ca9-98943e0b5dd1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/experiment_plan.yaml",
      "content": "experiments:\n  # === Claim 1: Structure-grounded negatives > embedding/random ===\n  - id: plan_001\n    claim: 1\n    description: \"M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected vs gold statistics\"\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n\n  - id: plan_002\n    claim: 1\n    description: \"M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware, 3 seeds each, Qwen2.5-Coder-3B LoRA\"\n    priority: P0\n    gpu_budget_hours: 30\n    deps: [plan_001]\n\n  - id: plan_003\n    claim: 1\n    description: \"M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best checkpoint, Qwen3.6-27B agent\"\n    priority: P0\n    gpu_budget_hours: 40\n    deps: [plan_002]\n\n  - id: plan_004\n    claim: 1\n    description: \"M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no LLM agent\"\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [plan_002]\n\n  # === Claim 2: Embedding negatives harmful ===\n  - id: plan_005\n    claim: 2\n    description: \"Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding negatives 何时最有害\"\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [plan_002]\n\n  # === Claim 3: CodeQL scalability ===\n  - id: plan_006\n    claim: 3\n    description: \"M1 scalability statistics: timeout rate, extraction time, coverage, connected-but-not-gold ratio by repo size\"\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_001]\n\n  # === Ablations ===\n  - id: plan_007\n    claim: 1\n    description: \"Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding\"\n    priority: P1\n    gpu_budget_hours: 20\n    deps: [plan_001]\n\n  - id: plan_008\n    claim: 1\n    description: \"Ablation: training data size scaling (1K vs 3K vs 5K instances)\"\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [plan_001]\n\n  - id: plan_009\n    claim: 1\n    description: \"Ablation: fusion head (embedding-only vs structural-features-only vs combined)\"\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan_002]\n\n  - id: plan_010\n    claim: 1\n    description: \"Ablation: dataflow-distance weighted negatives vs binary connected/disconnected\"\n    priority: P2\n    gpu_budget_hours: 10\n    deps: [plan_001]\n\n  # === Analysis ===\n  - id: plan_011\n    claim: 1\n    description: \"Failure analysis: 50 SweRank/BM25 failures, categorize by whether data-flow helps\"\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [plan_003]\n\n  - id: plan_012\n    claim: 1\n    description: \"Qualitative examples: 5-10 cases where structural negatives changed retrieval outcome\"\n    priority: P2\n    gpu_budget_hours: 0\n    deps: [plan_003]\n\n# GPU Budget:\n# P0: ~70h (M2 30h + M3a 40h) + M1 CPU\n# P1: ~70h (RepoBench 15h + emb analysis 5h + hop 20h + size 15h + fusion 10h + failure 5h)\n# P2: ~10h (distance-weighted + qualitative)\n# Total: ~150h GPU + ~10h CPU\n# Hardware: 1x RTX 4090D (M2 training) + 1-2x RTX 6000 Pro 96GB (M3a: Qwen3.6-27B >32GB VRAM)\n",
      "numLines": 97,
      "startLine": 1,
      "totalLines": 97
    }
  },
  "sourceToolAssistantUUID": "edc314ac-9a7f-4b59-a861-5ddf7c2edcbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-12T20:49:38.702Z_

````json
{
  "parentUuid": "3db5f030-5a58-4d1a-8ca9-98943e0b5dd1",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**faith-evidence-ie**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"faith-evidence-ie\")` 或 `load_project_config(\"faith-evidence-ie\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/faith-evidence-ie/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "41fcb042-e2a3-4198-8e60-59eae90c1757",
  "timestamp": "2026-05-12T20:49:38.702Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Dataflow negatives ≈ random (no clear win), but embedding-harm result is strong and Z% confirms structural signal exists; Claim 1 weakened, Claims 2+3 ho…",
  "leafUuid": "41fcb042-e2a3-4198-8e60-59eae90c1757",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling structure-grounded hard negatives to 5K repos",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669"
}
```

---

### Assistant

_source line 17 · 2026-05-12T20:50:06.827Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the project. Let me generate the detailed median-tier predictions for each planned experiment.

Key median-tier characteristics:
- Z% at 5K scale: 20-35% (moderate)
- Dataflow negatives ≈ random (no clear win)
- Embedding-harm result is strong
- Claim 1 weakened, Claims 2+3 hold
- Reframe needed, EMNLP Findings viable

Let me think through each experiment carefully:

**plan_001: M1 全量 CodeQL 提取 (5K repos)**
- At 50-repo scale: Z=40.8%, timeout=4%


- Scaling to 5K repos, I expect Z to drop into the 20-35% range since the larger dataset includes more diverse and smaller repositories with sparser call graphs, plus higher timeout rates of 4-12% as we hit more complex edge cases in the full distribution.

**plan_002: M2 全量 3-strategy 对比训练**
- Median tier: dataflow ≈ random, embedding clearly worse
- At MVP (pool=50): random R@1=0.525, emb R@1=0.488 (delta=-0.037)
- At full scale with 5K data, R@5 metrics show dataflow and random converging (0.76-0.84 and 0.74-0.83 respectively) while embedding lags (0.70-0.79), with deltas ranging from -0.01 to 0.03 between dataflow and random, and -0.06 to -0.02 between embedding and random.

**plan_003: M3a SWE-bench Lite evaluation**
- Expecting resolve rate delta of -0.5 to 1.5 points; retriever strategy alone shouldn't drive significant changes in resolution performance.

**plan_004: M3b RepoB

**
- Anticipating -1.0 to 2.0 point improvement on RepoBench-R metrics.

Now I'm laying out the remaining ablation studies: examining how embedding negatives impact medium-complexity repos, measuring timeout rates and extraction times across different repository sizes, comparing 1-hop versus multi-hop retrieval, scaling training data from 1K to 5K samples, testing fusion head variants, comparing distance-weighted versus binary matching strategies, analyzing failure modes, and collecting qualitative examples to understand model behavior.

Constructing the detailed YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41fcb042-e2a3-4198-8e60-59eae90c1757",
  "isSidechain": false,
  "requestId": "req_011CayLK7mz6f5u4wbRbf1n4",
  "type": "assistant",
  "uuid": "cecedec1-3450-42de-b22b-88f9857d3749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cPRKqwcqB65hs1iSv1RCQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6356,
      "cache_read_input_tokens": 26076,
      "output_tokens": 11907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6356,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11907,
          "cache_read_input_tokens": 26076,
          "cache_creation_input_tokens": 6356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6356
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

_source line 18 · 2026-05-12T20:53:57.252Z_

```yaml
tier: median
narrative_guidance: >
  Pivot primary claim from "dataflow wins" to "embedding-distance negatives are harmful — a cautionary result
  for the contrastive code retrieval community." Claim 2 becomes the headline; Claim 1 downgrades to
  "dataflow negatives are a viable alternative that avoids the pitfalls of embedding-distance negatives
  without degrading performance." Claim 3 (scalability methodology) survives as-is. Add ceiling analysis:
  why doesn't structural signal help more? Hypotheses include insufficient Z% density, noise in CodeQL
  reachability, or random negatives already being near-optimal when pool diversity is high. Failure analysis
  (plan_011) becomes critical for explaining the gap. Title pivot: emphasize "when hard negatives hurt" angle.
  Target: EMNLP Findings or resubmit cycle.

imagined_experiments:
  - name: "M1 全量 CodeQL 提取 (5K SWE-smith)"
    plan_id: "plan_001"
    description: "5K SWE-smith repos 全量 data-flow extraction，统计 connected vs gold overlap"
    expected_results:
      total_repos_attempted: 5000
      repos_successfully_extracted: 4300
      repos_failed_or_skipped: 700
      total_instances: 12800
      instances_with_extra_connected: 3200
      Z_pct_5K: 25.0
      avg_connected_minus_gold: 4.2
      codeql_timeout_rate_pct: 7.8
      codeql_mean_time_s: 38.5
      codeql_p95_time_s: 210.0
      gold_in_connected_ratio: 0.72
      repos_with_zero_connected: 2100
    result_rationale: >
      50-repo 试点 Z=40.8% 是在人工筛选的中等规模 repo 上得到的，样本偏向有丰富调用图结构的项目。
      5K 全量 SWE-smith 包含大量小型/单文件/脚本式 repo，这些 repo 缺乏跨文件调用链，CodeQL
      提取的 connected set 很小甚至为空。同时大型 monorepo 会触发更多 timeout（从 4% 升至 ~8%），
      进一步降低有效覆盖。综合效应使 Z% 从 40.8% 缩水至 ~25%，仍在 20-35% 窗口内，说明结构信号
      存在但比预期稀疏。gold_in_connected_ratio 从 1.0 降至 0.72，因为 5K 规模下更多 bug fix
      涉及 CodeQL 无法追踪的动态调用或反射模式。
    tables:
      - caption: "Table 1: CodeQL Extraction Statistics at 5K Scale"
        columns: ["Metric", "50-repo pilot", "5K full"]
        rows:
          - ["Z% (connected∖gold > 0)", "40.8%", "25.0%"]
          - ["Timeout rate", "4.0%", "7.8%"]
          - ["Gold ∈ connected ratio", "100%", "72%"]
          - ["Mean extraction time (s)", "43.4", "38.5"]
          - ["Avg |connected \\ gold|", "6.0", "4.2"]
      - caption: "Table 2: Z% by Repo Size Stratum (5K)"
        columns: ["Stratum", "# Instances", "Z%", "Avg extra connected"]
        rows:
          - ["Small (<50 files)", "7200", "15.3%", "1.8"]
          - ["Medium (50-200 files)", "3800", "38.9%", "7.5"]
          - ["Large (>200 files)", "1800", "29.1%", "6.0"]
    figures_description:
      - "Scatter plot: repo size (x) vs Z% (y), colored by timeout/success. Shows inverted-U shape peaking at medium repos."
      - "CDF of extraction time per repo, with vertical line at 300s timeout threshold."
    analysis: >
      Z=25% 满足 ≥20% 的最低门槛，证明结构信号在全量规模上确实存在，但密度显著低于 pilot。
      关键发现是 repo 规模的非单调效应：小 repo 缺乏跨文件调用链导致 Z 低，大 repo 因 timeout
      和分析复杂度也不理想，中等 repo（50-200 文件）仍然是甜点区（Z≈39%）。这为后续训练实验
      提供了一个重要预期管理：基于结构信号的训练增益将主要来自中等规模 repo 的子集，而非全局。

  - name: "M2 全量 3-strategy 对比训练"
    plan_id: "plan_002"
    description: "random vs embedding_distance vs dataflow_aware, 3 seeds each, Qwen2.5-Coder-3B LoRA, 5K 训练数据"
    expected_results:
      random_s42_recall5: 0.812
      random_s123_recall5: 0.798
      random_s456_recall5: 0.821
      random_mean_recall5: 0.810
      random_std_recall5: 0.012
      dataflow_s42_recall5: 0.818
      dataflow_s123_recall5: 0.807
      dataflow_s456_recall5: 0.826
      dataflow_mean_recall5: 0.817
      dataflow_std_recall5: 0.010
      emb_dist_s42_recall5: 0.762
      emb_dist_s123_recall5: 0.748
      emb_dist_s456_recall5: 0.771
      emb_dist_mean_recall5: 0.760
      emb_dist_std_recall5: 0.012
      delta_dataflow_vs_random_R5: 0.007
      delta_emb_vs_random_R5: -0.050
      random_mean_recall1: 0.542
      dataflow_mean_recall1: 0.553
      emb_dist_mean_recall1: 0.489
      delta_dataflow_vs_random_R1: 0.011
      delta_emb_vs_random_R1: -0.053
      training_loss_final_random: 0.028
      training_loss_final_dataflow: 0.035
      training_loss_final_emb_dist: 0.092
      training_time_hours_per_run: 3.2
    result_rationale: >
      Dataflow vs random 的 delta 仅 +0.7pp R@5，在 seed 方差范围内（std≈1.1pp），不构成
      统计显著差异。根本原因：Z=25% 意味着训练集中只有约四分之一的 instance 拥有"connected but
      not gold"的结构信号——对于其余 75% 的 instance，dataflow-aware miner 回退到 BM25-hard
      或 random padding（因为没有足够的 disconnected-but-similar candidates），使其行为退化为
      近似 random。此外，在 pool diversity 较高的全量评估中（pool=50+），random negatives 已经
      包含足够的"偶然 hard"样本（约 15-20% 的 random negatives 恰好是 BM25-similar 的），
      缩小了结构化采样的边际增益。Embedding-distance negatives 则延续 MVP 的负面趋势：在 5K
      规模上 delta=-5.0pp R@5，因为 embedding-distance mining 选出的 negatives 与 encoder
      的梯度信号高度冗余（CoCoHaNeRe 效应），导致 representation collapse 风险——val_loss
      显著高于 random（0.092 vs 0.028），说明模型在 embedding-distance negatives 上学到的
      区分信号更弱。
    tables:
      - caption: "Table 3: Retrieval Performance by Negative Mining Strategy (5K training, SWE-bench Lite eval pool=50)"
        columns: ["Strategy", "R@1", "R@5", "R@10", "Val Loss"]
        rows:
          - ["Random (3 seeds)", "0.542 ± 0.018", "0.810 ± 0.012", "0.921 ± 0.008", "0.028"]
          - ["DataFlow-aware (3 seeds)", "0.553 ± 0.015", "0.817 ± 0.010", "0.925 ± 0.007", "0.035"]
          - ["Emb-distance (3 seeds)", "0.489 ± 0.020", "0.760 ± 0.012", "0.878 ± 0.011", "0.092"]
      - caption: "Table 4: Pairwise Deltas (pp) with Paired t-test p-values"
        columns: ["Comparison", "ΔR@1", "ΔR@5", "p-value (R@5)"]
        rows:
          - ["DataFlow − Random", "+1.1", "+0.7", "0.42"]
          - ["EmbDist − Random", "−5.3", "−5.0", "0.003"]
          - ["DataFlow − EmbDist", "+6.4", "+5.7", "0.005"]
    figures_description:
      - "Bar chart with error bars: R@1, R@5, R@10 for three strategies, 3 seeds each. Random and dataflow bars nearly identical height, embedding-distance clearly lower."
      - "Training loss curves (3 strategies × 3 seeds): embedding-distance converges slower and to higher final loss."
      - "Per-seed scatter plot of R@5: shows dataflow and random seeds intermixed, embedding seeds clustered below."
    analysis: >
      核心发现是非对称的：dataflow negatives 未能显著超越 random（p=0.42），但 embedding-distance
      negatives 显著低于 random（p=0.003）。这要求叙事重心从"dataflow wins"转向"embedding
      hurts"。Dataflow 的无害性本身是一个有价值的结果——它证明结构化 negatives 不会引入噪声，
      可以作为 embedding-distance 的安全替代方案。论文 Claim 1 应降级为 viability claim。

  - name: "M3a SWE-bench Lite End-to-End Evaluation"
    plan_id: "plan_003"
    description: "3 strategies × best checkpoint, Qwen3.6-27B agent, 300 instances end-to-end patch generation + test"
    expected_results:
      random_resolve_rate_pct: 28.3
      dataflow_resolve_rate_pct: 28.7
      emb_dist_resolve_rate_pct: 27.8
      resolve_delta_dataflow_vs_random_pp: 0.4
      resolve_delta_emb_vs_random_pp: -0.5
      random_retrieval_recall5_e2e: 0.805
      dataflow_retrieval_recall5_e2e: 0.811
      emb_dist_retrieval_recall5_e2e: 0.758
      avg_tokens_per_instance: 12400
      timeout_instances: 8
      total_eval_gpu_hours: 38
    result_rationale: >
      SWE-bench Lite 的 resolve rate 主要受 LLM agent 能力约束，而非 retriever 质量。
      三种 retriever 的 R@5 差异在 5pp 以内，经过 Qwen3.6-27B 的 patch generation pipeline
      后，检索质量差异被进一步稀释——agent 会通过多轮 tool call 自行浏览代码弥补检索遗漏，
      也会因 LLM 推理错误浪费正确检索结果。因此 resolve rate delta 被压缩到 <1pp，远低于
      统计显著性门槛。这符合 median 档位"retriever strategy alone shows no significant
      resolve rate gain"的预期。值得注意的是绝对 resolve rate ~28% 与 SWE-agent 等
      baseline 在 Lite 上的表现大致可比，说明 pipeline 本身工作正常。
    tables:
      - caption: "Table 5: SWE-bench Lite End-to-End Results"
        columns: ["Retriever Strategy", "Resolve Rate (%)", "Retrieval R@5", "Avg Tokens"]
        rows:
          - ["Random", "28.3", "0.805", "12,200"]
          - ["DataFlow-aware", "28.7", "0.811", "12,400"]
          - ["Emb-distance", "27.8", "0.758", "12,600"]
          - ["No retriever (BM25 only)", "26.1", "0.720", "13,100"]
    figures_description:
      - "Grouped bar chart: resolve rate by strategy with 95% CI (bootstrap). CIs largely overlapping for all three strategies."
      - "Venn diagram: instances resolved by each strategy — high overlap (>85% shared), with small unique-to-each subsets."
    analysis: >
      End-to-end 结果确认 retriever 改进被 agent pipeline 的噪声淹没。但与 BM25-only baseline
      相比，所有 trained retrievers 都有 +2pp 的一致增益，证明对比学习训练本身有价值。关键 takeaway
      是 dataflow 和 random 都是有效的 negative 策略，而 embedding-distance 即使在 end-to-end
      也表现最差（虽然差异在统计噪声内）。论文应强调 retrieval-level 结果（Table 3）而非 resolve rate。

  - name: "M3b RepoBench-R Cross-File Retrieval Evaluation"
    plan_id: "plan_004"
    description: "retrieval-only evaluation on RepoBench-R cross-file completion benchmark, no LLM agent"
    expected_results:
      random_recall5: 0.618
      dataflow_recall5: 0.625
      emb_dist_recall5: 0.592
      random_mrr: 0.483
      dataflow_mrr: 0.490
      emb_dist_mrr: 0.461
      delta_dataflow_vs_random_R5_pp: 0.7
      delta_emb_vs_random_R5_pp: -2.6
      repobench_R_improvement_pp: 0.7
      baseline_unixcoder_recall5: 0.601
      baseline_swerank_recall5: 0.645
    result_rationale: >
      RepoBench-R 是跨文件代码补全任务，与 SWE-bench 的 bug fix 场景不同。StructFuse 的对比
      训练在 SWE-smith 数据上进行，domain shift 会削弱迁移效果。Dataflow vs random 的增益
      仍然微弱（+0.7pp），因为 RepoBench 的跨文件依赖多为 import 级别而非深层 data-flow，
      而 StructFuse 训练优化的结构信号（2-hop call graph connectivity）与 import-level
      依赖的重合度有限。Embedding-distance negatives 的伤害在 RepoBench 上反而略弱于
      SWE-bench（-2.6pp vs -5.0pp），因为 RepoBench 的 candidate pool 更小且更同质，
      embedding redundancy 的影响被缓解。与 SweRank baseline 的差距（-2.0pp）说明
      domain-specific 预训练数据量仍然是决定性因素。
    tables:
      - caption: "Table 6: RepoBench-R Retrieval Results"
        columns: ["Model", "R@1", "R@5", "R@10", "MRR"]
        rows:
          - ["StructFuse-Random", "0.385", "0.618", "0.742", "0.483"]
          - ["StructFuse-DataFlow", "0.392", "0.625", "0.748", "0.490"]
          - ["StructFuse-EmbDist", "0.360", "0.592", "0.718", "0.461"]
          - ["UniXcoder (baseline)", "0.371", "0.601", "0.730", "0.468"]
          - ["SweRank (baseline)", "0.412", "0.645", "0.771", "0.510"]
    figures_description:
      - "Radar chart comparing 5 models on R@1, R@5, R@10, MRR. Shows StructFuse variants clustered together, SweRank leading."
    analysis: >
      RepoBench-R 结果与 SWE-bench retrieval 结果一致：dataflow ≈ random > embedding-distance。
      跨 benchmark 的一致性增强了 Claim 2（embedding hurts）的可信度。与 SweRank 的差距可归因于
      预训练数据量差异（SweRank 用 >100K instances，StructFuse 用 5K），这不影响 negative
      strategy 的相对比较。论文可在 Discussion 中指出 StructFuse 的方法论贡献独立于绝对性能。

  - name: "Embedding vs Random 深度分层分析"
    plan_id: "plan_005"
    description: "按 repo size/complexity/domain 分层，分析 embedding negatives 何时最有害"
    expected_results:
      harm_by_repo_size:
        small_lt50_delta_R5_pp: -2.1
        medium_50_200_delta_R5_pp: -6.8
        large_gt200_delta_R5_pp: -5.3
      harm_by_candidate_pool_diversity:
        low_diversity_delta_R5_pp: -7.2
        high_diversity_delta_R5_pp: -2.8
      harm_by_embedding_similarity_of_negatives:
        top10pct_most_similar_delta_R5_pp: -9.1
        bottom50pct_delta_R5_pp: -1.5
      correlation_neg_similarity_vs_harm: 0.71
    result_rationale: >
      Embedding-distance negatives 的伤害机制是梯度冗余：当选中的 negatives 与 query 的 embedding
      高度相似时，对比 loss 的梯度方向与 encoder 已有的相似性判断高度对齐，导致"原地踏步"甚至
      过拟合到 surface feature。这个效应在 medium-size repo（50-200 files）最强，因为这些 repo
      的 candidate pool 大小适中（足够多的 similar files 被选为 negatives），且文件间共享
      更多命名约定和 import pattern（增加 surface similarity）。在 small repo 中，candidate
      pool 太小，embedding-distance 和 random 选到的 negatives 高度重叠（池子就那么大），
      差异被稀释。在 large repo 中，虽然有很多 similar candidates，但 pool diversity 也更高，
      部分缓解了冗余效应。关键发现是 embedding 相似度与 harm 程度的相关系数 0.71——越相似的
      negatives 越有害——这直接支持了"梯度冗余"假说。
    tables:
      - caption: "Table 7: Embedding-Distance Harm Stratified by Repo Characteristics"
        columns: ["Stratum", "N instances", "Emb R@5", "Random R@5", "Δ (pp)"]
        rows:
          - ["Small (<50 files)", "3,200", "0.782", "0.803", "−2.1"]
          - ["Medium (50-200)", "1,900", "0.698", "0.766", "−6.8"]
          - ["Large (>200)", "850", "0.732", "0.785", "−5.3"]
      - caption: "Table 8: Harm vs. Negative Embedding Similarity"
        columns: ["Neg Similarity Quartile", "Mean cosine sim", "Δ R@5 (pp)"]
        rows:
          - ["Q4 (most similar)", "0.91", "−9.1"]
          - ["Q3", "0.82", "−5.4"]
          - ["Q2", "0.73", "−3.2"]
          - ["Q1 (least similar)", "0.61", "−1.5"]
    figures_description:
      - "Heatmap: repo size (y) × negative similarity quartile (x), cell color = Δ R@5. Darkest red in medium × high-similarity corner."
      - "Scatter plot: mean negative cosine similarity (x) vs R@5 drop (y), with regression line (r=0.71, p<0.001)."
    analysis: >
      这是 Claim 2 的核心支撑实验。梯度冗余假说得到定量验证：embedding similarity 与 harm 的
      相关系数 0.71 说明 ~50% 的 harm variance 可由 negative 的 embedding 相似度解释。
      Medium repo 是"毒区"的发现对 practitioner 有直接指导意义：在这个规模的 repo 上使用
      embedding-distance hard negatives 风险最高。论文应将此分析放在 Results 的显著位置，
      作为 headline finding 的主要证据。

  - name: "M1 Scalability Statistics"
    plan_id: "plan_006"
    description: "CodeQL 5K 规模的 timeout rate, extraction time, coverage, connected-but-not-gold ratio by repo size"
    expected_results:
      overall_timeout_pct: 7.8
      overall_extraction_success_pct: 86.0
      mean_extraction_time_s: 38.5
      median_extraction_time_s: 22.1
      p95_extraction_time_s: 210.0
      p99_extraction_time_s: 285.0
      by_repo_size:
        small_lt50:
          timeout_pct: 1.2
          mean_time_s: 12.3
          Z_pct: 15.3
          coverage: 0.92
        medium_50_200:
          timeout_pct: 6.5
          mean_time_s: 45.8
          Z_pct: 38.9
          coverage: 0.85
        large_gt200:
          timeout_pct: 18.7
          mean_time_s: 98.2
          Z_pct: 29.1
          coverage: 0.71
      codeql_db_creation_failure_pct: 6.2
      beniget_fallback_usage_pct: 14.0
    result_rationale: >
      CodeQL 的 2-hop bounded analysis 在小 repo 上非常高效（<15s mean），因为 call graph 小，
      搜索空间有限。Medium repo 是 sweet spot：足够复杂以产生有意义的 connected set，但不至于
      timeout。Large repo（>200 files）的 timeout 率升至 ~19%，主要因为 Python 的 points-to
      analysis 在大型项目中的路径爆炸——即使限制了 2-hop，每个 hop 内的 callee 数量可能很大。
      总体 timeout <12% 满足 median tier 的上限。Beniget fallback 在 14% 的 instance 上
      触发，主要是 CodeQL 数据库创建失败（6.2%）或 connected files <5 的情况。Coverage 从
      pilot 的 100% 降至 86%，因为 5K 规模的 repo 质量更参差——包括 setup.py 缺失、
      非标准项目结构、混合语言等 CodeQL 难以处理的情况。
    tables:
      - caption: "Table 9: CodeQL Scalability at 5K Repos"
        columns: ["Metric", "Small", "Medium", "Large", "Overall"]
        rows:
          - ["Timeout rate (%)", "1.2", "6.5", "18.7", "7.8"]
          - ["Mean time (s)", "12.3", "45.8", "98.2", "38.5"]
          - ["Z%", "15.3", "38.9", "29.1", "25.0"]
          - ["DB creation success (%)", "96.1", "93.2", "84.5", "93.8"]
    figures_description:
      - "Box plot: extraction time distribution by repo size stratum, with jittered timeout points marked red."
      - "Stacked bar: repo count by size stratum, colored by extraction outcome (success/timeout/db-fail/beniget-fallback)."
    analysis: >
      Claim 3 的 scalability 论点成立：总体 timeout <8%，在可接受范围内。论文应诚实报告
      large repo 的 19% timeout，但指出这是 Python points-to analysis 的固有限制而非方法论
      缺陷——Java/Go 等有更精确类型系统的语言预期会更好。Beniget fallback 的存在也增强了
      方法的 robustness narrative。

  - name: "Ablation: 1-hop vs 2-hop vs 3-hop Call-Graph Bounding"
    plan_id: "plan_007"
    description: "不同 hop 数下的 connected set 大小、Z%、训练后 R@5 对比"
    expected_results:
      hop_1:
        Z_pct: 12.1
        avg_connected_files: 2.3
        timeout_pct: 2.1
        recall5_after_training: 0.808
      hop_2:
        Z_pct: 25.0
        avg_connected_files: 4.2
        timeout_pct: 7.8
        recall5_after_training: 0.817
      hop_3:
        Z_pct: 41.5
        avg_connected_files: 12.8
        timeout_pct: 22.3
        recall5_after_training: 0.811
    result_rationale: >
      1-hop 提供最精确但最稀疏的结构信号：只有直接调用者/被调用者，Z% 仅 12%，大部分 instance
      没有可用的 structural negative 信号，训练退化为 near-random。2-hop 是 pilot 验证的
      配置，平衡了覆盖率和精度。3-hop 大幅增加 connected set（avg 12.8 files），Z% 升至 42%，
      但引入了大量弱关联文件——3-hop 可达的文件可能只是通过一个公共 utility 函数间接连接，
      不真正代表 semantic relevance。结果是 3-hop 的训练信号更嘈杂（precision 下降），
      R@5 反而不如 2-hop。同时 3-hop 的 timeout 率飙升至 22%，实用性受限。这个消融验证了
      2-hop 是合理的工程选择。
    tables:
      - caption: "Table 10: Hop Distance Ablation"
        columns: ["Hops", "Z%", "Avg |connected|", "Timeout %", "R@5 (trained)"]
        rows:
          - ["1-hop", "12.1%", "2.3", "2.1%", "0.808"]
          - ["2-hop", "25.0%", "4.2", "7.8%", "0.817"]
          - ["3-hop", "41.5%", "12.8", "22.3%", "0.811"]
    figures_description:
      - "Line plot: hop count (x) vs Z%, timeout%, R@5 (three y-axes). Shows Z% monotonically increasing but R@5 peaking at 2-hop."
    analysis: >
      2-hop 的 Pareto optimality 支持论文的方法论选择。3-hop 的"更多连接 ≠ 更好信号"是一个
      有意义的发现，说明结构信号的质量比数量重要。论文可在 ablation section 简洁呈现。

  - name: "Ablation: Training Data Size Scaling (1K vs 3K vs 5K)"
    plan_id: "plan_008"
    description: "固定 negative strategy=dataflow_aware, 不同训练数据量下的性能变化"
    expected_results:
      scale_1K:
        recall5: 0.785
        recall1: 0.510
        training_time_h: 0.7
      scale_3K:
        recall5: 0.808
        recall1: 0.541
        training_time_h: 2.0
      scale_5K:
        recall5: 0.817
        recall1: 0.553
        training_time_h: 3.2
      scaling_slope_R5_per_1K: 0.008
      log_linear_fit_r2: 0.96
    result_rationale: >
      对比学习的数据效率通常遵循 log-linear scaling：从 1K 到 3K 的增益（+2.3pp R@5）
      大于 3K 到 5K 的增益（+0.9pp R@5），边际收益递减但尚未饱和。1K 已经提供 reasonable
      baseline（R@5=0.785），因为 InfoNCE loss 的学习效率主要取决于 batch 内 negative
      diversity 而非总数据量。从 3K 到 5K 的小幅增益暗示 5K 接近当前 model capacity
      和 negative strategy 下的 performance ceiling——进一步 scaling 需要更好的 negative
      mining 或更大的 model。log-linear fit R²=0.96 说明 scaling 行为规则可预测。
    tables:
      - caption: "Table 11: Training Data Scaling (DataFlow strategy)"
        columns: ["Scale", "R@1", "R@5", "R@10", "Train time (h)"]
        rows:
          - ["1K", "0.510", "0.785", "0.905", "0.7"]
          - ["3K", "0.541", "0.808", "0.918", "2.0"]
          - ["5K", "0.553", "0.817", "0.925", "3.2"]
    figures_description:
      - "Log-linear plot: training instances (x, log scale) vs R@5 (y). Near-linear trend with slight saturation at 5K."
    analysis: >
      Scaling 曲线支持 5K 作为"enough but not saturated"的选择。论文可引用此消融回应
      reviewer 关于"数据量不够"的潜在质疑——trend line 外推到 10K 预计仅额外 +0.5pp，
      不改变 strategy 之间的相对排序。

  - name: "Ablation: Fusion Head (Embedding-only vs Structural-features-only vs Combined)"
    plan_id: "plan_009"
    description: "评估 fusion head 的三种配置：纯 embedding、纯结构特征、和组合"
    expected_results:
      embedding_only_recall5: 0.817
      structural_only_recall5: 0.628
      combined_recall5: 0.822
      combined_vs_embedding_delta_pp: 0.5
      structural_features_auc: 0.71
    result_rationale: >
      纯结构特征（5 维：dataflow_distance, path_count, dependency_type, bm25_score,
      inter_procedural）在 retrieval 上表现差（R@5=0.628），因为它们是 sparse binary/integer
      features，信息量远不如 dense embedding。组合 fusion head 仅比 embedding-only 高 0.5pp，
      因为 MLP fusion head 难以从已经被 embedding 学习过的信号中提取额外增益——结构特征与
      embedding 学到的相似性有部分重叠（bm25_score 尤其如此），且 5 维 sparse features 对
      128 维 MLP 来说信息密度太低。这个结果说明"结构信号的价值主要在训练阶段（negative
      selection）而非推理阶段（feature fusion）"——一个重要的方法论 insight。
    tables:
      - caption: "Table 12: Fusion Head Ablation"
        columns: ["Configuration", "R@1", "R@5", "MRR"]
        rows:
          - ["Embedding-only", "0.553", "0.817", "0.652"]
          - ["Structural-features-only", "0.398", "0.628", "0.485"]
          - ["Combined (MLP fusion)", "0.558", "0.822", "0.658"]
    figures_description:
      - "Bar chart comparing three fusion configurations. Shows structural-only much lower, combined marginally higher than embedding-only."
    analysis: >
      Fusion head 的边际增益不支持在 pipeline 中保留结构特征用于推理。论文应将此作为 negative
      result 报告：structure helps training, not inference。这强化了方法论的核心 message——
      结构信号的价值在于 mining better training data，不在于作为 inference-time feature。
      Simplifies deployment: 推理时只需标准 bi-encoder，无需 CodeQL。

  - name: "Ablation: Dataflow-Distance Weighted vs Binary Connected/Disconnected"
    plan_id: "plan_010"
    description: "比较 exp(-α·d) 加权 vs 简单 binary connected/disconnected 的负样本选择"
    expected_results:
      binary_recall5: 0.815
      weighted_alpha1_recall5: 0.817
      weighted_alpha05_recall5: 0.814
      weighted_alpha2_recall5: 0.812
      delta_weighted_vs_binary_pp: 0.2
    result_rationale: >
      在 Z=25% 的 median 场景下，大多数 instance 的 connected files 数量很少（avg 4.2），
      dataflow distance 的粒度有限（大部分是 distance=1 或 2）。当信号本身就是 sparse binary
      时，连续加权的额外信息量极小。Alpha=1 略优于 binary（+0.2pp）在噪声范围内。Alpha=2
      过度惩罚远距离连接导致有效 connected set 更小，反而轻微下降。这个消融确认 binary
      connected/disconnected 足够，不需要复杂的距离加权——simplifies the method。
    tables:
      - caption: "Table 13: Distance Weighting Ablation"
        columns: ["Weighting", "α", "R@5", "Δ vs Binary"]
        rows:
          - ["Binary (0/1)", "—", "0.815", "—"]
          - ["exp(−αd)", "0.5", "0.814", "−0.1"]
          - ["exp(−αd)", "1.0", "0.817", "+0.2"]
          - ["exp(−αd)", "2.0", "0.812", "−0.3"]
    figures_description:
      - "Line plot: α values (x) vs R@5 (y), with horizontal dashed line for binary baseline. Nearly flat curve."
    analysis: >
      Negative result 支持 Occam's razor：binary classification 足够。论文可在 appendix
      简洁报告，减少方法复杂度。

  - name: "Failure Analysis: 50 SweRank/BM25 Failures"
    plan_id: "plan_011"
    description: "抽样 50 个 SweRank/BM25 检索失败的 instance，人工标注 data-flow 是否有帮助"
    expected_results:
      total_analyzed: 50
      category_counts:
        dataflow_would_help: 11
        dataflow_irrelevant_lexical_gap: 18
        dataflow_irrelevant_logic_only: 9
        gold_not_in_repo_scope: 5
        multi_file_edit_needed: 7
      dataflow_help_rate_pct: 22.0
      ceiling_if_perfect_structural_signal_pct: 32.0
    result_rationale: >
      50 个失败 case 中只有 ~22% 是 data-flow 理论上可以帮助的——这些是 gold file 与 buggy
      file 存在调用链关系但 BM25/embedding 因命名差异未能 rank 高的情况。更多的失败（36%）
      属于"lexical gap"类型：gold file 和 query 在词汇上完全无关（例如 config file vs
      source code），data-flow 也到达不了。逻辑修复（18%）需要理解程序语义而非结构关系。
      这个分析解释了 dataflow negatives 为什么没有大幅超越 random：即使 perfect structural
      signal，ceiling improvement 也只有 ~32%×当前 failure rate ≈ 3-4pp，而在 Z=25% 的
      实际信号密度下，可实现的增益更小。这是 median tier 的核心 ceiling analysis。
    tables:
      - caption: "Table 14: Failure Category Breakdown (N=50)"
        columns: ["Category", "Count", "%", "DataFlow Helps?"]
        rows:
          - ["Lexical gap (no name overlap)", "18", "36%", "Possible but sparse"]
          - ["DataFlow reachable but missed", "11", "22%", "Yes"]
          - ["Logic-only fix (no structural dep)", "9", "18%", "No"]
          - ["Multi-file coordinated edit", "7", "14%", "Partial"]
          - ["Gold out of analysis scope", "5", "10%", "No"]
    figures_description:
      - "Pie chart of failure categories, with 'DataFlow helps' slice highlighted."
      - "Three example failure cases with repo structure, call graph, and annotated explanation of why dataflow did/didn't help."
    analysis: >
      这是 median tier 论文最关键的分析。Ceiling analysis 回答了"为什么结构信号没有帮更多"
      的核心 reviewer 问题：(1) 大量失败与结构无关（lexical gap, logic-only），
      (2) 即使结构信号完美，可恢复的失败也有限（ceiling ~32%），(3) Z=25% 进一步削弱
      实际可实现增益。论文应将此作为 Discussion 的重要部分，展现对方法 limitation 的
      诚实理解——这对 EMNLP reviewers 来说是加分项。

  - name: "Qualitative Examples: Structural Negatives 改变检索结果的 Case Study"
    plan_id: "plan_012"
    description: "挑选 5-10 个 dataflow-aware training 改变了 retrieval ranking 的 case"
    expected_results:
      total_cases_found: 7
      cases_dataflow_improved_ranking: 4
      cases_dataflow_no_change: 2
      cases_dataflow_hurt: 1
      best_case_rank_improvement: "gold file: rank 8→2"
      worst_case_rank_regression: "gold file: rank 3→5"
    result_rationale: >
      在 dataflow ≈ random 的 median 场景下，能找到 dataflow 明确改善的 case 数量有限。
      ~57% 的精选 case 展示了正面效果——这些通常是 medium-size repo 中 gold file 通过
      2-hop call chain 与 buggy file 连接、但命名差异大导致 embedding-only retriever
      rank 不高的情况。Dataflow training 让 encoder 学会了对这类"名字不像但结构相关"的
      文件给予更高 score。但也有 1 个 case 出现了 regression——CodeQL 的 connected set
      恰好包含了一个 misleading file（通过 utility function 间接连接），dataflow training
      错误地提升了它的 rank。这个 mixed picture 反映了 median tier 的现实。
    tables: []
    figures_description:
      - "Side-by-side ranking comparison: 4 positive cases showing rank before/after dataflow training, with call graph visualization."
      - "1 negative case with annotated call graph showing the misleading indirect connection via utility function."
    analysis: >
      Qualitative examples 在论文中起"让 reviewer 相信 method 有道理"的作用。精选 4 个
      compelling 的正面 case + 1 个诚实的负面 case，展现 balanced presentation。负面 case
      自然引出 limitation：utility function 导致的 spurious connectivity 是 2-hop
      analysis 的固有弱点。可在 appendix 扩展到全部 7 个 case。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cecedec1-3450-42de-b22b-88f9857d3749",
  "isSidechain": false,
  "requestId": "req_011CayLK7mz6f5u4wbRbf1n4",
  "type": "assistant",
  "uuid": "48602ad9-f93f-4f0b-93c6-e545feb029d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cPRKqwcqB65hs1iSv1RCQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6356,
      "cache_read_input_tokens": 26076,
      "output_tokens": 11907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6356,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11907,
          "cache_read_input_tokens": 26076,
          "cache_creation_input_tokens": 6356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6356
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Dataflow negatives ≈ random (no clear win), but embedding-harm result is strong and Z% confirms structural signal exists; Claim 1 weakened, Claims 2+3 ho…",
  "leafUuid": "48602ad9-f93f-4f0b-93c6-e545feb029d9",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling structure-grounded hard negatives to 5K repos",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Dataflow negatives ≈ random (no clear win), but embedding-harm result is strong and Z% confirms structural signal exists; Claim 1 weakened, Claims 2+3 ho…",
  "leafUuid": "48602ad9-f93f-4f0b-93c6-e545feb029d9",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling structure-grounded hard negatives to 5K repos",
  "sessionId": "fcae3eab-b048-4c65-b10d-e118231f4669"
}
```

---
