# deploy bjb2 28827 gpu01 spatial s46

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-gpu01-spatial-s46_20260524T071004_result.json`
- **Structured JSON:** [`2a1b3d66442b6ddfee28.json`](../../sessions/2a/2a1b3d66442b6ddfee28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**部署状态：**

| GPU | 实验 | 状态 |
|-----|------|------|
| GPU 0 | `eval-supp-crm-norm005-spatial-s46` | 已启动，模型加载中 |
| GPU 1 | `eval-supp-adapt-tau025-spatial-s46` | **阻塞** — GPU 1 正在运行 `openvla_eval.py --benchmark object`（PID 114990, 19121 MiB） |

GPU 1 的 OpenVLA object eval 需要先跑完才能部署 Adaptive eval。选项：
1. 等它跑完后我再部署（可以用 /loop 轮询）
2. 你手动 kill 掉那个进程腾出 GPU 1

怎么处理？

---
