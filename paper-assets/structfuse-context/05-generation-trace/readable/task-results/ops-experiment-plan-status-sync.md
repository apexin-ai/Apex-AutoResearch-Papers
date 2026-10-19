# ops experiment plan status sync

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_experiment-plan-status-sync_20260513T104040_result.json`
- **Structured JSON:** [`b48b4c756cbac6eb3e3b.json`](../../sessions/b4/b48b4c756cbac6eb3e3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。

**ROADMAP.md 更新内容：**
- M1 进度：27% → **71%** (109/222 repos)，ETA 从 5/14 下午提前到今晚/明早
- m2_embed_verify：random ✅ done，embedding best R@1=**55.6%** (>random 53.6%，+2pp)，dataflow pending
- plan_013：random ✅ + embedding ✅ done，dataflow running step 500
- flash-attn 2.8.3 已装
- Registry experiment_plan 关联标记为已完善（4 个活跃 plan 均已关联）

**Registry 更新内容：**
- m1_extraction / m2_embed_verify / plan_013_starcoder 的 notes 均已同步最新状态

**Plan ↔ Registry 关联检查结果：** 无缺失。plan_001→m1_extraction, plan_002→m2_embed_verify, plan_006→plan_006_scalability, plan_013→plan_013_starcoder 均已正确关联。未启动的 plan (003-005, 007-012, 014-017) 无 registry_id 是预期行为。

---
