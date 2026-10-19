# ops registry cleanup plan006

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-cleanup-plan006_20260513T041615_result.json`
- **Structured JSON:** [`ad4b0a7c2038fb407ce3.json`](../../sessions/ad/ad4b0a7c2038fb407ce3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

```
=== Registry 清理 ===
p2b_eval_all: DONE (killed) ✓
p2b_dataflow_retrain: DONE (negative) ✓
plan 关联: 2 条已关联
  - plan_001: registry_id=m1_extraction, mvp_registry_id=mvp_p1_codeql_feasibility
  - plan_002: registry_id=m2_early_pilot (更新), mvp_registry_id=mvp_p2b_contrastive_training
  - mvp_p2a_linear_proxy: 无对应 plan 条目（linear proxy 是独立分析）

=== plan_006 Scalability Stats (partial) ===
Repos analyzed: 29/131 (M1 仍在运行)
Instances: 8171 processed + 660 skipped (clone_failed) = 8831
Timeout rate: 0% (0/8171)
Coverage: 100% success rate (已处理的全部成功)
Overall Z%: 72.5%

Z% by repo size:
  Small (<100 instances, 8 repos, 484 inst):    Z=42.6%
  Medium (100-500, 16 repos, 3836 inst):        Z=64.2%
  Large (>500, 5 repos, 3851 inst):             Z=84.5%

Extraction time per instance:
  Mean: 26.5s | Median: 23.7s | P95: 43.7s | Max: 112.9s

Notable: 5 repos Z=0% (bottle, inflect, schema, markdownify, json-logger)
— connected files ⊆ gold files, no extra context. Likely single-file repos.
```

Artifact 已注册：`art_20260513_240352`

---
