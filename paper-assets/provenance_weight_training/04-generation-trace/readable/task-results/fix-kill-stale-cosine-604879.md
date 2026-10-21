# fix kill stale cosine 604879

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_stale_cosine_604879_20260521T121606_result.json`
- **Structured JSON:** [`eb5f424568d3b2a01e0b.json`](../../sessions/eb/eb5f424568d3b2a01e0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕：

| 项目 | 结果 |
|------|------|
| Kill 604879 | 已杀死 |
| cuda:2 进程 | 仅 PID 606296，占用 45634 MiB |
| 4 卡状态 | 每卡 1 个进程，各 ~45.6GB，正常 |
| output 目录 | config.json 中 `lr_scheduler_type: "linear"`，无 cosine 残留，当前 linear 进程已在正常写入（checkpoint-500 + step_metrics.jsonl） |

---
