# ops plan registry association

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan-registry-association_20260513T075624_result.json`
- **Structured JSON:** [`c9c70e9b721362c1392f.json`](../../sessions/c9/c9c70e9b721362c1392f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's the summary:

## 1. 关联状态表

| plan_id | registry_id | mvp_registry_id | registry status |
|---------|-------------|-----------------|----------------|
| plan_001 | m1_extraction | mvp_p1_codeql_feasibility | RUNNING (27%, ETA 5/14 afternoon) |
| plan_002 | m2_embed_verify | mvp_p2b_contrastive_training | RUNNING (random strategy, step 500) |
| plan_006 | **plan_006_scalability** ← 新建 | — | DONE/success |
| plan_013 | plan_013_starcoder | — | RUNNING (random strategy, step 500) |

## 2. 修复内容

- **plan_006**: 创建了 registry entry `plan_006_scalability`（DONE/success），关联了 3 个已注册 artifacts（art_20260513_240352, art_20260513_ef3ab0, art_20260513_eaf24b）。在 `experiment_plan.yaml` 中补上了 `registry_id: plan_006_scalability`。

其余已有关联（plan_001, plan_002, plan_013）的 registry_id 和 mvp_registry_id 均正确，无需修改。

## 3. 未启动 plan 列表

| plan_id | description | priority | blocked by |
|---------|-------------|----------|------------|
| plan_003 | M3a SWE-bench Lite end-to-end eval | P0 | plan_002 |
| plan_004 | M3b RepoBench-R cross-file retrieval | P1 | plan_002 |
| plan_005 | Embedding vs random 深度分析 | P1 | plan_002 |
| plan_007 | Ablation: 1/2/3-hop bounding | P1 | plan_001 |
| plan_008 | Ablation: data size scaling | P1 | plan_001 |
| plan_009 | Ablation: fusion head | P1 | plan_002 |
| plan_010 | Ablation: dataflow-distance weighted negatives | P2 | plan_001 |
| plan_011 | Failure analysis | P1 | plan_003 |
| plan_012 | Qualitative examples | P2 | plan_003 |
| plan_014 | Temperature ablation | P1 | plan_002 |
| plan_015 | Dynamic embedding mining baseline | P1 | plan_002 |
| plan_016 | Bootstrap CI for SWE-bench | P0 | plan_003 |
| plan_017 | Inference-time graph comparison | P1 | plan_002 |

---
