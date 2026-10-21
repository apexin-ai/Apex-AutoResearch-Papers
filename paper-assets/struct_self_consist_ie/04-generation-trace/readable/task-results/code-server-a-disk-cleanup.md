# code server a disk cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_server_a_disk_cleanup_20260519T084135_result.json`
- **Structured JSON:** [`5c19e7e93267d6ac796f.json`](../../sessions/5c/5c19e7e93267d6ac796f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| | 清理前 | 清理后 |
|---|---|---|
| 已用 | 195G | 154G |
| 可用 | 56G | **97G** |
| 释放 | — | **~41G** |

删除了 5 个目录：
- `qwen3-8b-fewnerd-exp021-merged` (16G)
- `qwen3-8b-scierc-merged-v2` (16G)
- `llama3.1-8b-conll2003-lora` (5.1G)
- `llama3.1-8b-conll2003-lora-3ep` (3.2G)
- `llama3.2-3b-scierc-lora` (1.9G)

保留了 registry 引用的 `llama3.1-8b-fewnerd-lora` 和 `llama3.1-8b-scierc-lora`。97G 可用空间远超 32B LoRA merge 所需的 ~65GB。

---
