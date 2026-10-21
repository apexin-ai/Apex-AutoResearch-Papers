# ssh fix seed456 collision westb0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_seed456_collision_westb0_20260522T163032_result.json`
- **Structured JSON:** [`1aea70fa27ffaf670377.json`](../../sessions/1a/1aea70fa27ffaf670377.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 冲突修复

- Retrain PID 225466: **killed**
- Eval PID 224705: **alive** — 正常运行中，150/1319 (11%)，当前 acc=0.4933
- Checkpoint-100: **missing**（整个目录被诊断 Worker 删除）
- 最终操作: **eval 继续运行**（模型已在 GPU 内存中，不受磁盘删除影响）

**需要注意**：checkpoint-100 已从磁盘删除。当前 eval 不受影响（模型已加载到 GPU），但 eval 结束后如果需要这个 checkpoint 做其他事（其他 benchmark eval、作为 artifact 保存），需要重新训练。预计 eval 还需约 50 分钟完成（按 ~2.5s/it × 1169 剩余）。

---
