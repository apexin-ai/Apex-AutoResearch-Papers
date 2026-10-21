# verify gpu deconflict

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_gpu_deconflict_20260514T174413_result.json`
- **Structured JSON:** [`9405558b8d5acae376a5.json`](../../sessions/94/9405558b8d5acae376a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四卡状态确认完毕，每卡只有一个进程，无冲突：

| GPU | PID | 运行时间 | 实验 | 显存 |
|-----|-----|---------|------|------|
| cuda:0 | 112475 | — | grid search (batch) | 46514 MiB |
| cuda:1 | 123836 | 3m34s | adaptive_fix_seed42 (resume ckpt-1500) | 46514 MiB |
| cuda:2 | 109362 | 3h20m | adaptive_fix_seed123 (原始，带 eval) | 74998 MiB |
| cuda:3 | 115071 | 2h27m | adaptive_fix_seed456 (原始，带 eval) | 74998 MiB |

重复进程 125680、125759 已不存在，125297 之前已 kill。四卡各一个进程，全部正常运行（GPU-Util 94-99%）。

---
