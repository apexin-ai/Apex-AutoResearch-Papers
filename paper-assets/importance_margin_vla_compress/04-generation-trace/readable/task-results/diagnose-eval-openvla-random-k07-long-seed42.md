# diagnose eval openvla random k07 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_random_k07_long_seed42_20260525T172535_result.json`
- **Structured JSON:** [`c4dafe6b83d82e4fe1c2.json`](../../sessions/c4/c4dafe6b83d82e4fe1c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**实验状态：failed（机器重启导致中断）**

- 实验于 22:36 启动，01:09 停止写入日志，01:18 机器重启 — 进程被杀
- 日志无 error/traceback/OOM，纯粹是机器重启导致
- 仅完成 **3/10 tasks**（150/500 episodes）

**已完成的部分结果：**

| Task | SR |
|------|----|
| Task 1: put both the alphabet soup and the tomato sauce in the basket | 0.480 (24/50) |
| Task 2: put both the cream cheese box and the butter in the basket | 0.460 (23/50) |
| Task 3: turn on the stove and put the moka pot on it | 0.580 (29/50) |

Registry 已更新为 failed，需要重跑。

---
