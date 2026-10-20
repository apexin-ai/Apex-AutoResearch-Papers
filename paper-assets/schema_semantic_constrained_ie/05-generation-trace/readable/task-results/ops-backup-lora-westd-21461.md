# ops backup lora westd 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_backup-lora-westd-21461_20260523T201441_result.json`
- **Structured JSON:** [`be6b03ad43ec3800de00.json`](../../sessions/be/be6b03ad43ec3800de00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

备份完成。

**备份报告：**

| Adapter | 子目录 | 大小 |
|---------|--------|------|
| qwen3_8b_lora_wikievents | best + checkpoint-26 + checkpoint-39 | 533M |
| llama_lora_docred | best + checkpoint-382 + checkpoint-573 | 530M |
| 70b_lora_docred | checkpoint-1146 | 267M |
| 70b_lora_scierc | checkpoint-663 | 267M |

共 59 个文件，总计 **1.6GB**。已排除 optimizer.pt / rng_state.pth / scheduler.pt / scaler.pt 等训练状态文件，仅保留 adapter 权重 + tokenizer + 配置文件。通过 westd-16980 中转完成（中转文件已清理）。

---
