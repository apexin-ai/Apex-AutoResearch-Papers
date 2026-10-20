# emergency 19828 disk cleanup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_emergency_19828_disk_cleanup_20260519T232953_result.json`
- **Structured JSON:** [`b184606f0eed6bac0e75.json`](../../sessions/b1/b184606f0eed6bac0e75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 删除项 | 释放空间 |
|--------|---------|
| `smollm3_3b_wiki_a100_s43/` (失败实验整目录) | ~17G |
| `smollm3_3b_wiki_a100_s42/` (未完成，无 analysis) | ~12G |
| `pythia14b_wiki_a100_s43/gen_0` ~ `gen_9` (中间 checkpoint) | ~48G |
| `models/SmolLM3-3B-Base/` | ~5.8G |
| HF cache SmolLM3 | 4K |

**结果：250G 用量从 100% 降至 68%，可用 82G。** opt13b 进程 (PID 452614) 正常运行，pythia14b_s43 保留了 gen_10 + all_metrics.json + analysis。

---
