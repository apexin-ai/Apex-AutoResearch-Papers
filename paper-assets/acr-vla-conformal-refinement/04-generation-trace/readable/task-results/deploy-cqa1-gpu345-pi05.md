# deploy cqa1 gpu345 pi05

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-gpu345-pi05_20260526T055153_result.json`
- **Structured JSON:** [`405970c6a740d7971a58.json`](../../sessions/40/405970c6a740d7971a58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。cqa1-32758 状态总结：

| GPU | 实验 | 状态 | 启动时间 | VRAM | Registry |
|-----|------|------|---------|------|----------|
| 0 | τ-sweep τ=0.50 (goal s42) | 运行中 | 10:54 | 10.3GB | — |
| 1 | τ-sweep τ=0.70 (goal s42) | 运行中 | 10:54 | 10.3GB | — |
| 2 | τ-sweep τ=0.90 (goal s42) | 运行中 | 10:54 | 10.3GB | — |
| 3 | **pi05-adaptive-object-s44-cqa1** | 运行中 | 13:54 | 14.0GB | RUNNING |
| 4 | **pi05-adaptive-long-s43-cqa1** | 运行中 | 13:55 | 14.7GB | RUNNING |
| 5 | **pi05-adaptive-long-s44-cqa1** | 运行中 | 13:55 | 14.7GB | RUNNING |

6 个 GPU 全部满载。3 个新实验已在运行约 8 分钟，进程稳定，registry 已补注册。无需额外部署操作。

---
