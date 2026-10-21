# ops kill zombie gpu1 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-zombie-gpu1-25068_20260519T160107_result.json`
- **Structured JSON:** [`8ab91ba8c9bef28a6865.json`](../../sessions/8a/8ab91ba8c9bef28a6865.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 完全释放。

**汇报：**
- Kill 进程：PID 236050（`VLLM::EngineCore`），GPU 1
- 释放显存：90232 MiB → 0 MiB
- tmux：无 exp071 相关 session 残留（现存 session 均为 exp073/model_dl）
- GPU 1 最终状态：0 进程、0 MiB 占用、0% util、30°C、47W idle

GPU 0 上 PID 242845 的 vLLM 进程仍在运行（97% util），未动。

---
