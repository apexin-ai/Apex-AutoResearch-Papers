# code grid b low script

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grid_b_low_script_20260515T202036_result.json`
- **Structured JSON:** [`90629a3f59da179b2630.json`](../../sessions/90/90629a3f59da179b2630.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪：

- **脚本路径**: `/root/provenance_weight_training/run_grid_b_low_seed42.sh`
- **语法检查**: SYNTAX_OK
- **数据文件**: `data/scored_data.jsonl` 存在 (930MB)
- **模型目录**: `models/Qwen/Qwen3-0.6B` 存在 (符号链接)

脚本串行运行 b=0.1 → 0.2 → 0.3，每次训练完打印时间戳，任一失败即停止。

---
