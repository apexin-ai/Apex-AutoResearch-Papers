# verify dual grpo alive

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_dual_grpo_alive_20260514T173102_result.json`
- **Structured JSON:** [`9ba5dae42145ac5f334c.json`](../../sessions/9b/9ba5dae42145ac5f334c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GRPO 进程均存活，训练正常推进。

### 进程状态

| PID | 任务 | GPU | 运行时长 | 状态 |
|-----|------|-----|---------|------|
| 221261 | grpo_rasp_20 | cuda:0 | 22min 49s | ✅ 存活 |
| 221901 | grpo_standard_20 | cuda:1 | 19min 50s | ✅ 存活 |

### GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 72453 MiB | 98% |
| cuda:1 | 72453 MiB | 98% |

### 训练进度

- **grpo_rasp_20**: 6/5604 steps（~17min），~173.85s/step，预计总时长 ~270h
- **grpo_standard_20**: 5/5604 steps（~14min），~173.72s/step，预计总时长 ~270h

两个任务都在正常迭代，没有卡住。

---
