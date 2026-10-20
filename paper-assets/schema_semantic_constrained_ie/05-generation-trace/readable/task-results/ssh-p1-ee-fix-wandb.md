# ssh p1 ee fix wandb

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_ee_fix_wandb_20260518T214452_result.json`
- **Structured JSON:** [`ef44ec627aa4977066d4.json`](../../sessions/ef/ef44ec627aa4977066d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**结果**：`/root/schema_semantic_constrained_ie/scripts/train_lora_wikievents.py` line 72 的 `report_to = "wandb"` 改为 `report_to = "none"`。dry_run 和非 dry_run 模式 import 均通过，不再触发 wandb 错误。wandb 未安装在该服务器上，后续如需 wandb 日志需先 `pip install wandb` 再将该行改回。

---
