# diagnose cqa1 cuda3 random k095 s44

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_cuda3_random_k095_s44_20260528T000528_result.json`
- **Structured JSON:** [`67a2ea21a97f794af868.json`](../../sessions/67/67a2ea21a97f794af868.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常运行，无需干预。

**状态**：进程 801342 存活，已运行 1h19m，当前在 Task 2 完成（3/10 tasks done），GPU 0 利用率 99%。

**进度**：
- Task 0: 58.0% (50 eps)
- Task 1: 94.0% (50 eps)  
- Task 2: 68.0% (50 eps)
- 累计: 110/150 = 73.3%

GPU 3 空闲是因为实验跑在 `cuda:0`（`--gpu 0`），不是 GPU 3。注册信息标注 cuda:3 可能有误，但实验本身正常推进中。按当前速度（每 task ~25min），预计还需 ~3h 完成剩余 7 个 tasks。

---
