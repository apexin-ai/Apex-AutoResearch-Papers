# check seed123 remaining alive

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed123_remaining_alive_20260513T104411_result.json`
- **Structured JSON:** [`7ed8eeafa822237b6200.json`](../../sessions/7e/7ed8eeafa822237b6200.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果**: phase2_seed123_remaining 进程正常运行。

| 项目 | 状态 |
|------|------|
| PID | 197481，已运行 ~40 min |
| 当前阶段 | uncurated Gen 3/7（训练中） |
| GPU 1 显存 | 15,409 MiB / 97,887 MiB |
| Gen 1 PPL | 45.29 |
| Gen 2 PPL | 53.76 |

进程没挂，uncurated 7 代跑完后会接着跑 RGDS 7 代，预计还需 10+ 小时。Registry 已更新 current_gen=3。

---
