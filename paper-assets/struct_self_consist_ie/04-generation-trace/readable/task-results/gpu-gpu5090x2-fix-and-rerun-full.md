# gpu gpu5090x2 fix and rerun full

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gpu5090x2_fix_and_rerun_full_20260514T124323_result.json`
- **Structured JSON:** [`611a90700e1be18f18f0.json`](../../sessions/61/611a90700e1be18f18f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 和 GPU 1 被两个 llamafactory 训练任务占用：
- PID 60975 (GPU 0): `train_config_llama.yaml`，运行 2 分钟
- PID 55644 (GPU 1): `wnut17_lora.yaml`，运行 27 分钟

GPU 2 和 GPU 3 空闲。有两个选择：
1. 杀掉这两个旧进程，用 GPU 0/1/2 跑
2. 先用 GPU 2/3 跑 2 个实验，第 3 个等 GPU 空出来

要杀掉这两个旧训练任务吗？还是用空闲 GPU 先跑？

---
