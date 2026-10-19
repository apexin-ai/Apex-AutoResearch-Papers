# check moto cleanup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_moto-cleanup_20260515T035633_result.json`
- **Structured JSON:** [`771062a31ea41fd3179d.json`](../../sessions/77/771062a31ea41fd3179d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

---

### 子任务 1: moto CodeQL 传播性确认

**结论：隔离失败，不是 OOM，是 query timeout。**

- moto CodeQL DB 创建成功，但 `call_graph.ql` 的 `directCallEdge` predicate 在 moto 这个大 repo 上每次都超过 300s 超时限制（exit code 33）
- 截至 11:58 已累计 28 次超时，每个 moto instance 都会触发
- **不影响后续 repo**：batch_extract 用 4 workers 并行，moto 卡住 1 个 worker，其他 3 个正常处理 pydicom（800/1315）、conan（850/972）、MONAI
- 536 个 moto instances 预计全部 fallback 到 embedding-distance
- 已在 registry notes 中记录

### 子任务 2: 残留进程清理

- PID 465668（旧 evaluate_pool50.py --pool-size 5 --gpu -1）已 kill，确认死亡

---
