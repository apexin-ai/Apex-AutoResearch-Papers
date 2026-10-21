# ssh d064 docred full beam

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_docred_full_beam_20260519T090455_result.json`
- **Structured JSON:** [`9baf5c7434000463412a.json`](../../sessions/9b/9baf5c7434000463412a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验状态总结：

| Task | GPU | Status | ETA |
|------|-----|--------|-----|
| Llama DocRED LoRA 训练 | cuda:0 | 22/573 steps | ~77 min |
| Qwen beam-4 unc | cuda:1 | 15/998 docs | ~5h |
| Qwen beam-4 con | cuda:1 | 等待 unc 完成 | ~5h after |
| Llama beam-4 unc | cuda:0 | 等待训练完成 | ~5h after training |
| Llama beam-4 con | cuda:0 | 等待 unc 完成 | ~5h after unc |

自动化串联脚本已就位，30 分钟后再检查。

---
