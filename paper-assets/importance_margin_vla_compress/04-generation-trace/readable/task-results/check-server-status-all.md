# check server status all

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server_status_all_20260517T051647_result.json`
- **Structured JSON:** [`394feeab585660456276.json`](../../sessions/39/394feeab585660456276.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 连通性

| 服务器 | 状态 | 错误 |
|--------|------|------|
| **westd-27271** | 不可达 | `Unable to connect to port 27271 on 36.103.198.204` |
| **cqa1-33015** | 不可达 | `Unable to connect to port 33015 on 58.144.141.28` |

两台实例可能已被平台关机或回收（按量计费实例的常见行为）。

### 受影响实验（4 个 RUNNING）

| 实验 | 服务器 | 提交时间 | 状态 |
|------|--------|----------|------|
| `eval_stage1_only` | westd-27271 | 04:27 UTC | **最关键** — 结果未知，需重启后检查 |
| `eval_imm100k_bypass` | westd-27271 | 03:40 UTC | 部分已知：6/10 tasks = 0% SR |
| `eval_k07_bypass_v3` | westd-27271 | 04:00 UTC | 结果未知 |
| `libero_fullft_batch64` | cqa1-33015 | 01:30 UTC | 100K steps 训练中（预计 May 21 完成），进度未知 |

### 下一步行动

1. **重启 westd-27271** — 3 个 eval 任务已提交 8h+，结果大概率已写入磁盘（如果实例数据持久化），重启后立即读取
2. **重启 cqa1-33015** — batch64 训练按预估还需 ~4 天，需确认 checkpoint 是否持久化。若实例被回收且无持久存储，需重新启动训练
3. **seed1 训练** — 未在 registry 中找到独立记录，可能已完成或属于其他实验，重启后确认

Registry 已更新所有断联信息。

---
