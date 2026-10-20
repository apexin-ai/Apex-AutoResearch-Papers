# ssh check all processes

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_processes_20260516T002533_result.json`
- **Structured JSON:** [`9af86ec2add9dd65e8f6.json`](../../sessions/9a/9af86ec2add9dd65e8f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写到 `artifacts/process_check_report.md`。

**汇总：**

| 进程 | 状态 | 关键信息 |
|------|------|---------|
| rsft_ced_s43_train_r3 | **运行中** | GPU 1, 48/510 steps (9.4%), ~45 min 剩余 |
| rsft_ced_s45_train_r3 | **失败 (OOM)** | GPU 2 被残留进程 PID 276148 (rsft-ced-s45-r2) 占满，启动 15s 即崩溃 |
| eval_flat_nli_s44 | **运行中** | GPU 0, 80/247 batches (32%), ~2h 剩余 |
| eval_flat_nli_seed45 | **运行中** | GPU 3, 55/247 batches (22%), ~2.4h 剩余 |

**需要处理：** GPU 2 上 PID 276148 是之前 rsft-ced-s45-r2 的残留训练进程，占用 31.6 GB 显存。需要 kill 它后重新提交 rsft_ced_s45_train_r3。两个 eval 还没出结果，metrics_v2.json 尚未生成。

---
