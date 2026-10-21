# deploy westd41074 gpu01 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu01_v2_20260527T093037_result.json`
- **Structured JSON:** [`beea68adde1b1c89bf13.json`](../../sessions/be/beea68adde1b1c89bf13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**问题：GPU 0 和 GPU 1 上已有相同实验在跑。** 17:17 通过 agent-ml 提交的实验已在运行：

| GPU | 旧 PID (17:17) | 新 PID (17:32) | 实验 |
|-----|----------------|----------------|------|
| GPU 0 | **356361** | **371486** | random k=0.9 |
| GPU 1 | **356612** | **371488** | random k=0.5 |
| GPU 2 | 262137 | — | random k=0.95 |
| GPU 3 | 262473 | — | l2norm k=0.95 |

现在每个 GPU 上跑着两份相同实验，会互相争抢显存和算力。需要 kill 掉一组。新启动的 (371486, 371488) 刚开始加载模型，旧的 (356361, 356612) 已跑了 ~15 分钟。

**建议 kill 新启动的重复进程**，保留旧的。是否执行？

---

**cqa1-33015 状态：**
- PID 118726: **存活**
- 4 个 GPU 进程在运行 (PID 109156, 118731, 93525, 897100)

---
