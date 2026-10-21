# ops kill rp r1 conflict

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-rp_r1-conflict_20260514T203139_result.json`
- **Structured JSON:** [`cb23fd09ff2fb2f6c55c.json`](../../sessions/cb/cb23fd09ff2fb2f6c55c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。报告：

| 项目 | 状态 |
|------|------|
| **PID 94055 (rp-r1)** | **KILLED** — 已终止，无残留子进程 |
| **PID 94758 (rp-r2)** | **ALIVE** — etime 36:49，正常运行 |
| **cuda:3 显存** | 13636 MiB（仅 PID 94758），冲突已解除 |
| **output_dir** | 空目录（尚未到 save_steps，正常） |

**全 4 卡快照：**

| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| 0 | 66% | 13645/32607 MiB | PID 90085 (13636 MiB) |
| 1 | 94% | 19434/32607 MiB | PID 96500 + 97340 (各 9710 MiB) |
| 2 | 65% | 9411/32607 MiB | PID 95373 (9402 MiB) |
| 3 | 63% | 13645/32607 MiB | PID 94758 (13636 MiB) ← rp_r2 独占 |

cuda:3 现在只有 rp_r2 一个进程，冲突已解决。

---
