# backup discover westd 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_backup_discover-westd-16980_20260525T205606_result.json`
- **Structured JSON:** [`9695dceaef4af0778be3.json`](../../sessions/96/9695dceaef4af0778be3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/backup_discovery_westd16980.md`。

关键发现：
- 项目总计 **596M**，加上 `autodl-tmp/schema_outputs/` 的 98M，rsync 约 **694M**
- `outputs/` 占 469M（大量实验结果 .jsonl 和 violation reports），是最大的部分
- 无 .git、.venv、wandb、LoRA adapter 需要排除
- 排除项仅 `__pycache__/`、`.pytest_cache/`、`*.pyc`
- `autodl-tmp/models/` 103G 全部排除，但其中 4 个 `*-FT-AWQ-INT4` 目录是自训练量化模型，如果需要保留建议单独备份（已在报告中注释掉的命令）

---
