# submit exp 029b retry

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_029b_retry_20260518T004331_result.json`
- **Structured JSON:** [`d9408f0b03c0870012d9.json`](../../sessions/d9/d9408f0b03c0870012d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

磁盘 100% 满，**无法启动训练**。`checkpoints/` 占 199G，其中大量 merged 模型（每个 ~16G）。

需要你决定清理哪些 checkpoint。当前占用大户：

| 目录 | 大小 | 类型 |
|------|------|------|
| `qwen3-8b-wnut17-merged` | 16G | merged |
| `qwen3-8b-scierc-merged-v2` | 16G | merged |
| `qwen3-8b-scierc-merged-rank8` | 16G | merged |
| `qwen3-8b-fewnerd-merged` | 16G | merged |
| `qwen3-8b-fewnerd-exp021-merged` | 16G | merged |
| `qwen3-8b-fewnerd-5epoch-merged` | 16G | merged |
| `qwen3-8b-conll2003-merged` | 16G | merged |
| `llama3.1-8b-scierc-merged` | 15G | merged |
| `llama3.1-8b-conll2003-merged` | 15G | merged |
| `qwen3-4b-*-merged` (×3) | 23G | merged |
| `llama3.2-3b-scierc-merged` | 6G | merged |
| 各 lora 目录 | ~20G 合计 | lora adapter |

exp_029b 是 SciERC 10-epoch LoRA 训练，训练本身 + checkpoint 估计需要至少 **20-30G** 空闲空间。

**建议**：删除不再需要的 merged 模型（merged 可以从 base + lora 重新生成）。请告知哪些可以删除，或者是否可以删除所有 merged 模型。

---
