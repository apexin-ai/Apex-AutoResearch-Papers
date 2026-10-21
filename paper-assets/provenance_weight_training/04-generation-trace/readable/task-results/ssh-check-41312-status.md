# ssh check 41312 status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_41312_status_20260517T094201_result.json`
- **Structured JSON:** [`ea16b09723bfa1de762d.json`](../../sessions/ea/ea16b09723bfa1de762d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## SSH 连通性：**OK**
- uptime: 50 days, load average: 14.36

## 4 个实验状态

| 实验 | PID | 状态 | 进度 | ETA |
|------|-----|------|------|-----|
| llama3b_uniform_seed42 | 3112 (cuda:0) | **ALIVE** | 5394/6103 (88%) | ~1h02m |
| llama3b_adaptive_seed42 | 4005 (cuda:1) | **ALIVE** | 5278/6103 (86%) | ~1h14m |
| batchsize16_nmin8_seed42 | 50284 (cuda:2) | **ALIVE** | 4066/6103 (67%) | ~1h24m |
| grid_b0_2_seed42 | 45224 (cuda:3) | **ALIVE** | 4836/6103 (79%) | ~44m |

**预计完成顺序**：grid_b0_2 (~44m) → llama3b_uniform (~1h) → llama3b_adaptive (~1h14m) → batchsize16_nmin8 (~1h24m)

所有实验均正常运行，无异常。

---
