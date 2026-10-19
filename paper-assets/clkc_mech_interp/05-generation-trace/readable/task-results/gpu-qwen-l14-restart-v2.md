# gpu qwen L14 restart v2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_qwen-L14-restart-v2_20260522T150243_result.json`
- **Structured JSON:** [`c852aa0c2d75732a83be.json`](../../sessions/c8/c852aa0c2d75732a83be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### cuda:1/2/3 上的进程

| GPU | PID | 启动时间 | 实验 |
|-----|-----|---------|------|
| cuda:1 | 493129 | 22:37 | **Qwen L14 steering**（已完成，占着显存未退出） |
| cuda:2 | 493756 | 22:39 | Gemma-2 L17 steering |
| cuda:3 | 494291 | 22:40 | Llama-3.1 L13 steering (position=all) |

cuda:1 上的 16GB 就是之前启动的 **Qwen L14 进程 (PID 493129)**——它已经跑完并写出了结果文件，但进程还挂着没退出（可能卡在模型未释放）。结果已完整保存，不需要重跑。

如需释放 cuda:1 显存，可以 kill 掉 PID 493129。要执行吗？

---
