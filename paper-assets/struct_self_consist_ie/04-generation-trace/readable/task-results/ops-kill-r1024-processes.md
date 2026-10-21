# ops kill r1024 processes

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_r1024_processes_20260514T222848_result.json`
- **Structured JSON:** [`009b11fb122ce260847f.json`](../../sessions/00/009b11fb122ce260847f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **无 _r1024 进程在运行** — 所有 _r1024 重跑实验已经不在了（可能之前已完成或已被终止）
- **唯一活跃实验**：`exp_017_llama_conll_n16_s123`（tmux session `exp017_s123`，GPU 1）— 不含 _r1024，未动它
- **GPU 状态**：4 卡全部空闲（各 2 MiB 显存占用，0% 利用率）

注意：`exp_017_llama_conll_n16_s123` 的 python 进程虽然还在（PID 108051），但 GPU 显存已释放，可能处于 CPU 阶段或即将结束。该实验不在 kill 范围内，已保留。

---
