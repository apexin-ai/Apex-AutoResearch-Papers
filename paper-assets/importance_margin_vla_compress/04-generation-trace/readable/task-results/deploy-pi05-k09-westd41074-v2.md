# deploy pi05 k09 westd41074 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-k09-westd41074-v2_20260521T153144_result.json`
- **Structured JSON:** [`82fdbdb7371f1e815ea4.json`](../../sessions/82/82fdbdb7371f1e815ea4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**这两个进程并没有被杀，它们还在运行中。**

| GPU | PID | 进程 | 运行时间 | 状态 |
|-----|-----|------|---------|------|
| 0 | 437038 | l2norm k=0.9 seed42 | 7m03s | Rl (running) |
| 1 | 437312 | random k=0.9 seed42 | 6m32s | Rl (running) |

不需要重新部署。你提到的 PID 437033 和 437307 确实不存在了，但当前 437038 和 437312 是同样的实验且正在正常运行。

要我检查一下它们的日志输出确认进展正常吗？

---
