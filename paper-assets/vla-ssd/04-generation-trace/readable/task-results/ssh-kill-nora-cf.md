# ssh kill nora cf

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_nora_cf_20260522T024442_result.json`
- **Structured JSON:** [`b142d17d766d5bee1c16.json`](../../sessions/b1/b142d17d766d5bee1c16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

等待脚本已清理。剩余的 579759 是 `openvla_long_cf_trained` 的 tmux session（在 GPU 0 上运行，但当前 GPU 0 显存 0 MiB，说明它内部的实际计算进程可能已结束或尚未启动）。这不是 NORA Spatial untrained CF 进程。

**结果：**
- NORA Spatial untrained CF 主进程及所有等待脚本已全部杀掉
- GPU 0: **0 MiB 显存，0% 利用率** — 已完全释放
- GPU 1: 15291 MiB, 82%（`openvla_long_cf_trained` 在运行，不受影响）

---
