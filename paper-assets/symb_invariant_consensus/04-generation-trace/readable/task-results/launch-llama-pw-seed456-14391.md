# launch llama pw seed456 14391

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_llama-pw-seed456-14391_20260523T051353_result.json`
- **Structured JSON:** [`15de8601c5751e457710.json`](../../sessions/15/15de8601c5751e457710.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**冲突：cuda:0 上有正在运行的 seed42 实验，不能启动 seed456。**

当前 westd-14391 cuda:0 状态：
- **vLLM** 在运行：port 8000，模型 `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct`（PID 9284）
- **seed42 实验仍在运行**：`run_full_mvp.py --seed 42 --pw-data data/proofwriter_full.json`（PID 17674，启动于 03:58，已运行约 9 小时）
- GPU 利用率 100%，显存 88GB/97GB

seed42 还没完成，不能在同一 GPU 上启动 seed456。需要等 seed42 跑完后再启动。

---
