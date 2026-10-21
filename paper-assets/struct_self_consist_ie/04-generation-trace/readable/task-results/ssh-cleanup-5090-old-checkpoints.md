# ssh cleanup 5090 old checkpoints

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup-5090-old-checkpoints_20260520T070723_result.json`
- **Structured JSON:** [`45e3aff920961b70a734.json`](../../sessions/45/45e3aff920961b70a734.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理结果

**已删除（5 个目录，~17.5G）：**

| 目录 | 大小 |
|------|------|
| qwen3-8b-wnut17-lora | 5.3G |
| qwen3-4b-conll2003-lora | 4.1G |
| llama3.1-8b-fewnerd-lora | 3.2G |
| llama3.1-8b-scierc-lora | 3.2G |
| ft_fewnerd_smoke | 1.7G |

**磁盘空间对比：**
- 删除前：79G 可用 (69% used)
- 删除后：**97G 可用 (62% used)**
- 释放：~18G

**剩余 checkpoints（8 个）：**
- qwen25-32b-fewnerd-qlora-s42
- qwen3-4b-scierc-lora
- qwen3-8b-conll2003-lora
- qwen3-8b-fewnerd-5epoch-lora
- qwen3-8b-scierc-10epoch-lora
- qwen3-8b-scierc-3epoch-lora
- qwen3-8b-scierc-lora-rank8
- qwen3-8b-scierc-lora-v2

**注意：可用空间 97G < 100G 目标。** `*scierc-v2*` glob 未匹配任何目录（`qwen3-8b-scierc-lora-v2` 的子串是 "scierc-lora-v2" 而非 "scierc-v2"）。如果也需要删除该目录（3.4G），删后可达 ~100G。另外还有 2 个 llama log 文件（共 96K）未删除（非目录，被脚本跳过）。

---
