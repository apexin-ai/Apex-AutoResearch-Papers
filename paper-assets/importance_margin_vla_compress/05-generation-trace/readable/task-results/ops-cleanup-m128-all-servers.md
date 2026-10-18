# ops cleanup m128 all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-m128-all-servers_20260521T090503_result.json`
- **Structured JSON:** [`71de0c9d7b8b5dace129.json`](../../sessions/71/71de0c9d7b8b5dace129.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇总：

| 服务器 | 删除目录 | 释放空间 | 清理后磁盘状态 |
|--------|---------|---------|---------------|
| **westd-27271** | `openvla_sc_m128/` (19G) + `openvla_sc_m128_seed42/` (35G) | **54 GB** | 250G 总量，155G 已用，96G 可用 (62%) |
| **westd-38929** | `openvla_sc_m128/` (19G) | **19 GB** | 250G 总量，192G 已用，59G 可用 (77%) |
| **cqa1-33015** | `openvla_sc_m128/` (19G) | **19 GB** | 250G 总量，195G 已用，56G 可用 (78%) |
| **合计** | — | **92 GB** | — |

---
