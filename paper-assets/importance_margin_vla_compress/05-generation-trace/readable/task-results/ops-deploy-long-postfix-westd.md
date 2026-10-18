# ops deploy long postfix westd

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-long-postfix-westd_20260524T113016_result.json`
- **Structured JSON:** [`943ccced5a209fa45575.json`](../../sessions/94/943ccced5a209fa45575.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

| 服务器 | GPU | 实验 | PID | tmux session |
|--------|-----|------|-----|-------------|
| westd-41074 | 0 | Random k=0.95 Long postfix | 271179 | `random_k095_long` |
| westd-41074 | 3 | Random k=0.9 Long postfix | 271362 | `random_k09_long` |
| westd-38929 | 1 | Random k=0.7 Long postfix | 350886 | `random_k07_long` |
| westd-38929 | 3 | Random k=0.5 Long postfix | 350967 | `random_k05_long` |

额外发现：westd-38929 GPU 0 和 GPU 2 仍在使用（分别 10.5GB/43% 和 10.6GB/17%），与任务描述中"GPU 0 已完成"不一致——可能有其他实验占用。westd-38929 GPU 3 的 L2norm k=0.7 Object 已经完成（内存 4MiB）。

---
