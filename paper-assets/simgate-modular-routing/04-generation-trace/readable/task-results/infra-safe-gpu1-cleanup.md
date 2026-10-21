# infra safe gpu1 cleanup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_safe-gpu1-cleanup_20260513T080340_result.json`
- **Structured JSON:** [`99315e62723459799d17.json`](../../sessions/99/99315e62723459799d17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成，汇总：

| 项目 | 状态 |
|------|------|
| PID 20301 是否 GPU0 子进程 | **是** — PPID=20300，属于 mvp-p1-gpu0 进程树，未触碰 |
| PID 163319 已清理 | **是** — kill -9 成功 |
| GPU1 显存 | **used: 0 MiB / free: 32110 MiB** — 完全释放 |
| GPU0 进程安全 | **安全** — PID 20301 仍在运行，占用 15816 MiB |
| tmux 旧会话 | mvp-p1-gpu1-v2、mvp-p1-gpu1-v3 已清理，仅剩 mvp-p1-gpu0 |

**注意**: PID 162576/162577 是 GPU1 上的 `phase1_signal.py --use_vllm` 进程（`CUDA_VISIBLE_DEVICES=1`），163319 是其 vLLM 子进程。vLLM 引擎被杀后这两个进程的 GPU 显存已释放（0 MiB），但进程本身仍在。它们大概率会因 vLLM 引擎丢失而报错退出。如需立即清理这两个进程，请确认。

---
