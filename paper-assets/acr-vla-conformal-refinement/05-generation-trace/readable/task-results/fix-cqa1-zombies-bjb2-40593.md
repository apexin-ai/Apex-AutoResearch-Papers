# fix cqa1 zombies bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1-zombies-bjb2-40593_20260526T033943_result.json`
- **Structured JSON:** [`20d51f8626fae17eadac.json`](../../sessions/20/20d51f8626fae17eadac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. cqa1-32758 清理结果

**GPU 3-5 无需清理** — 僵尸进程已自行退出，GPU 3/4/5 均为空闲状态（1 MiB, 0% util）。

**GPU 0-2 τ-sweep 正常运行中：**
| GPU | PID | τ | CPU% | 运行时间 |
|-----|--------|------|------|----------|
| 0 | 110361 | 0.50 | 546% | ~260 min |
| 1 | 110628 | 0.70 | 563% | ~268 min |
| 2 | 110910 | 0.90 | 566% | ~269 min |

**Registry 已更新：** `pi05-k2mean-goal-s42`、`pi05-adaptive-object-s42-v2`、`pi05-adaptive-long-s42` → status=DONE, conclusion=killed, notes 记录了 crash 原因。

### 2. bjb2-40593 连接状态

**不可达** — `Unable to connect to port 40593 on 106.38.204.136`。实例可能已关机或端口已变更。

---
