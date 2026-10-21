# ssh d064 progress check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_progress_check_20260519T175528_result.json`
- **Structured JSON:** [`2387e033fa45a847b3da.json`](../../sessions/23/2387e033fa45a847b3da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。总结：

**4 个进程全部正常运行，无异常。**

| 服务器 | 进程 | 进度 | ETA |
|--------|------|------|-----|
| 21461 GPU0 | Llama greedy con | 769/998 (77%) | ~50min |
| 21461 GPU1 | Qwen beam-4 con | 415/998 (42%) | ~4.1h ← **瓶颈** |
| 16980 GPU0 | Llama beam-4 unc | 684/998 (69%) | ~1.4h |
| 16980 GPU1 | Llama beam-4 con | 586/998 (59%) | ~2.1h |

已完成：Llama greedy unc (998✓)、Qwen beam-4 unc (998✓)

Option C（16980 补跑 Llama greedy）：beam 完成后约需额外 3.3h（两方向并行）。

---
