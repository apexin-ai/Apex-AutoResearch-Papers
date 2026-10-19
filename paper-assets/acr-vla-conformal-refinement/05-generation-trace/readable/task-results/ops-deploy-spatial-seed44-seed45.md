# ops deploy spatial seed44 seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-spatial-seed44-seed45_20260519T015035_result.json`
- **Structured JSON:** [`ea2654e404d8507c4b21.json`](../../sessions/ea/ea2654e404d8507c4b21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都已启动并在加载模型。

### 部署汇报

| Seed | 服务器 | GPU | tmux session | 状态 |
|------|--------|-----|-------------|------|
| 44 | bjb2-28827 | GPU 3 (5.7GB/24.6GB used) | `eval-spatial-obs-only-norm02-seed44` | 运行中，正在加载模型权重 |
| 45 | bjb1-32546 | GPU 1 (4.8GB/24.6GB used) | `eval-spatial-obs-only-norm02-seed45` | 运行中，正在加载模型权重 |

两台服务器 checkpoint 均存在，GPU headroom 充足（~19GB free），timeout 16h。

---
