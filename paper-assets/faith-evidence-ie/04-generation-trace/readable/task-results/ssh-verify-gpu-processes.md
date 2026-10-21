# ssh verify gpu processes

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-gpu-processes_20260521T071646_result.json`
- **Structured JSON:** [`85a73415f951b253980b.json`](../../sessions/85/85a73415f951b253980b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部存活：

| PID | 实验 | GPU | 显存占用 | GPU利用率 | 运行时长 | 状态 |
|-----|------|-----|---------|----------|---------|------|
| 85668 | d140_4b_sft_s42_no_evi_2048 | cuda:0 | 11,696 MiB | 85% | 10min 57s | Rl (运行中) |
| 70388 | plan017_14b_rsft_eval_2048 | cuda:1 | 32,494 MiB | 83% | 4h 30m 51s | S (睡眠/等IO) |
| 83650 | d140_8b_sft_s42_no_evi_2048 | cuda:2 | 19,590 MiB | 90% | 48min 15s | Ss+ |
| 81857 | d140_8b_sft_s42_with_evi_2048 | cuda:3 | 19,590 MiB | 90% | 1h 14m 21s | Ss+ |

4 张卡全部被占满，所有实验正常推理中。

---
