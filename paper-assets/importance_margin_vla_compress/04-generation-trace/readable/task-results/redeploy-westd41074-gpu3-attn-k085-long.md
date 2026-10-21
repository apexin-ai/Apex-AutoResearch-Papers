# redeploy westd41074 gpu3 attn k085 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_redeploy_westd41074_gpu3_attn_k085_long_20260526T020117_result.json`
- **Structured JSON:** [`bef175deef3f5442ed17.json`](../../sessions/be/bef175deef3f5442ed17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功。

**GPU3 状态：**
- 显存：16188 MiB（模型已加载）
- 进程正在运行，已进入 Task 1/10 评估
- Attention pruning: 256 → 217 vision tokens (k=0.85)

**完整 nvidia-smi：**
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 16188 MiB |
| 1 | 0% | 15980 MiB |
| 2 | 0% | 15980 MiB |
| 3 | 0% | 16188 MiB |

---
