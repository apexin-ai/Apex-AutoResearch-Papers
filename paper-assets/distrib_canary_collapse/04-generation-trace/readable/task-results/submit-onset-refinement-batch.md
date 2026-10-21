# submit onset refinement batch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_onset_refinement_batch_20260519T140336_result.json`
- **Structured JSON:** [`4aee3853e8f6ac29c8dd.json`](../../sessions/4a/4aee3853e8f6ac29c8dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 6 张 GPU（cuda:0-5）均有活跃 python 进程，无空闲 GPU。**

| GPU | PID | 显存占用 |
|-----|-------|---------|
| 0 | 137279 | 14228 MiB |
| 1 | 143075 | 12706 MiB |
| 2 | 122887 | 14494 MiB |
| 3 | 123809 | 14494 MiB |
| 4 | 124519 | 14494 MiB |
| 5 | 121667 | 14494 MiB |

按硬约束要求，**停止提交，不执行 Step 3**。

C4 数据路径已确认：`data/c4_5k`，后续提交时可用。

需要等当前实验完成释放 GPU 后再提交。要我检查 cuda:3/4/5 上运行的是什么实验吗？

---
