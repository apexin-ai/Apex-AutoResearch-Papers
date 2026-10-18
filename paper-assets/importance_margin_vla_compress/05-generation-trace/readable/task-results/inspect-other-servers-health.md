# inspect other servers health

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_inspect_other_servers_health_20260526T013118_result.json`
- **Structured JSON:** [`fcc70d60e25d940a8e35.json`](../../sessions/fc/fcc70d60e25d940a8e35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 健康检查结果

### Server 1: cqa1-33015 — **离线**
- SSH: **失败** — `Unable to connect to port 33015 on 58.144.141.28`（Connection refused）
- 实例可能已关机或端口已变更，需去控制台确认

### Server 2: westd-27271 — **离线**
- SSH: **失败** — `Unable to connect to port 27271 on 36.103.198.204`（Connection refused）
- 实例可能已关机或端口已变更，需去控制台确认

### Server 3: westd-38929 — **正常运行**
- SSH: OK
- GPU 状态：

| GPU | Util | 显存占用 |
|-----|------|---------|
| 0 | 62% | 16118 MiB |
| 1 | 55% | 15780 MiB |
| 2 | 68% | 15780 MiB |
| 3 | 66% | 15780 MiB |

- 4 个 cliff curve 实验**全部在跑**，与预期一致：

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | eval_openvla_attn_k07_long_seed42_v2 | 6815 | Running |
| 1 | eval_openvla_l2norm_k07_long_seed42_v2 | 7009 | Running |
| 2 | eval_openvla_random_k07_long_seed42_v2 | 7384 | Running |
| 3 | eval_openvla_l2norm_k085_long_seed42_v2 | 8069 | Running |

- 4 个 tmux session 均存活，实验从今天 02:12 启动，已运行约 7.3 小时
- **无异常**

---
