# maintenance cleanup checkpoints

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_cleanup_checkpoints_20260522T143052_result.json`
- **Structured JSON:** [`d3680b80b508535de871.json`](../../sessions/d3/d3680b80b508535de871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| | 清理前 | 清理后 |
|---|---|---|
| 磁盘可用 | 46G (82%) | **67G (74%)** |
| 释放空间 | — | **~21G** |

**删除的目录（共 6 个）：**
- `detect_remove_q05_v2_seed456/checkpoint-5500, checkpoint-6000, checkpoint-6103`（各 3.4G）
- `random_reweight_v2_seed456/checkpoint-5500, checkpoint-6000, checkpoint-6103`（各 3.4G）

**保留的内容：**
- `detect_remove_q05_v2_seed456/`: `final/`, `config.json`, `step_metrics.jsonl`
- `random_reweight_v2_seed456/`: `final/`, `config.json`, `step_metrics.jsonl`, `eval_results/`

磁盘可用 67G，未达 80G 阈值，但已从 82% 降至 74%。如需进一步释放空间可清理其他实验的 checkpoint。

---
