# diagnose server status 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_server_status_16980_20260520T033149_result.json`
- **Structured JSON:** [`229ad2d97be64514095c.json`](../../sessions/22/229ad2d97be64514095c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程均在运行，状态如下：

### 1. d065 Llama greedy unc 4096 (unconstrained)

| 项目 | 值 |
|------|-----|
| PID | 697390 |
| GPU | GPU 0 (CUDA_VISIBLE_DEVICES=0), 显存 18266MiB, 利用率 90% |
| 进度 | **486/998** (48.7%) |
| 启动时间 | 今天 09:35 |
| 处理速率 | ROADMAP 记录 372 → 现 486，~117 min 处理 114 docs，约 1.03 min/doc |
| 预计完成 | 剩余 512 docs，约 8.8 小时 → **~20:20** |
| 输出文件 | `/root/autodl-tmp/schema_outputs/d065_llama_docred_greedy_unc_4096.jsonl` (4.4MB) |

### 2. d065 Llama greedy con 4096 (constrained)

| 项目 | 值 |
|------|-----|
| PID | 698086 |
| GPU | GPU 1 (CUDA_VISIBLE_DEVICES=1), 显存 18266MiB, 利用率 88% |
| 进度 | **447/998** (44.8%) |
| 启动时间 | 今天 09:37 |
| 处理速率 | ROADMAP 记录 336 → 现 447，~115 min 处理 111 docs，约 1.04 min/doc |
| 预计完成 | 剩余 551 docs，约 9.5 小时 → **~21:05** |
| 输出文件 | `/root/autodl-tmp/schema_outputs/d065_llama_docred_greedy_con_4096.jsonl` (4.1MB) |

两个进程今天 09:35-09:37 重启后正常运行，输出文件最后写入时间均为 11:32（刚刚），处理速率稳定。预计今晚 20:00-21:00 前后完成。

---
