# ops interv stale data cleanup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_interv_stale_data_cleanup_20260520T213216_result.json`
- **Structured JSON:** [`9516ec4538975df63509.json`](../../sessions/95/9516ec4538975df63509.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**路径说明**: 新 run 的实际输出路径是 `reactive_d1_s43_fp32/`（不是 `reactive_d1_s43/`）。

**清理内容** (`reactive_d1_s43_fp32/`):
- 删除旧 gen 目录: gen_3, gen_4, gen_5, gen_6, gen_7, gen_8, gen_9, gen_10
- 删除旧 run 产物: all_metrics.json, EXIT_CODE

**当前状态**: 目录只剩 gen_0 (基线), gen_1, gen_2 (新 run 产出, May 21), config.json。新 run 进程正常运行中 (PID 382885 tmux session `interv_react_s43`, GPU 0)。

---
