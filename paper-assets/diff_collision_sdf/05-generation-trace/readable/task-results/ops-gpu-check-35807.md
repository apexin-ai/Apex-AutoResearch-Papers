# ops gpu check 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_35807_20260525T112942_result.json`
- **Structured JSON:** [`3268a5e4fae588513029.json`](../../sessions/32/3268a5e4fae588513029.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 轮 SSH 用完，汇报结果：

## GPU 状态 (westd-35807)

| GPU | 利用率 | 显存 | 温度 | 功耗 |
|-----|--------|------|------|------|
| 0 | **100%** | 38.1G / 97.9G | 69°C | 435W/600W |
| 1 | 空闲 | 0 / 97.9G | 28°C | 33W |
| 2 | 空闲 | 0 / 97.9G | 28°C | 33W |
| 3 | 空闲 | 0 / 97.9G | 28°C | 34W |

**GPU 0 上的进程：** PID 166283 (python, 19046MiB) + PID 168730 (python, 19046MiB)

## PID 存活检查

| PID | 状态 | 运行时长 |
|-----|------|----------|
| 168730 | **ALIVE** (Rl) | 1h28m |
| 166274 | **ALIVE** (Ss+) | 1h33m |
| 170922 | **DEAD** | — |
| 171068 | **DEAD** | — |

## 日志

`/root/colliforce-vla/logs/` 不存在，项目目录下也无 `.log` 文件。**无法定位 170922 和 171068 的崩溃原因。**

---
