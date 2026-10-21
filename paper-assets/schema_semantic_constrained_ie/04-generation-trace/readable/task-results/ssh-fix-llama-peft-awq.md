# ssh fix llama peft awq

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_llama_peft_awq_20260518T220004_result.json`
- **Structured JSON:** [`cea38844680f55944b73.json`](../../sessions/ce/cea38844680f55944b73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

peft AWQ dispatch 错误已修复。脚本成功通过了 import、模型加载、LoRA 注入，进入了训练循环。当前 dry-run 失败在 OOM（GPU 0 上有其他进程占了 54GB），这是 GPU 内存问题，与原来的 peft bug 无关。

**修复内容**：直接修改了 `/root/miniconda3/lib/python3.12/site-packages/peft/import_utils.py` 中 `is_gptqmodel_available()` 函数，将三处 `raise ImportError` 改为 `return False`。训练脚本本身无需改动。

---
