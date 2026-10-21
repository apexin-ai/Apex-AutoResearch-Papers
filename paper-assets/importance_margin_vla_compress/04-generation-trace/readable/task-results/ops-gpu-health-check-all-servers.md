# ops gpu health check all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_health_check_all_servers_20260528T161819_result.json`
- **Structured JSON:** [`d308495512e616c78ccb.json`](../../sessions/d3/d308495512e616c78ccb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 服务器 | GPU | 显存 | 状态 |
|--------|-----|------|------|
| cqa1-33015 | 4× RTX 4090 D (24GB) | 全部空闲 | cuda:0-3 可用 |
| westd-27271 | — | — | **连接失败**（端口 27271 不通，实例可能已关机/重启） |
| westd-38929 | 1× RTX PRO 6000 Blackwell (96GB) | 空闲 | cuda:0 可用 |
| westd-41074 | 1× RTX PRO 6000 Blackwell (96GB) | 空闲 | cuda:0 可用 |

所有可达服务器均无运行中的 GPU 进程，全部 GPU 空闲。westd-27271 需要检查实例状态或更新 SSH 端口。

---
