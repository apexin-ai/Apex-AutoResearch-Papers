# ssh confirm gpu release

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_confirm_gpu_release_20260518T232402_result.json`
- **Structured JSON:** [`582dc2d3d2906d121f20.json`](../../sessions/58/582dc2d3d2906d121f20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### westd-21461
- **GPU**: 2× RTX PRO 6000 Black，0MiB 占用，无活跃进程 ✓
- **tmux**: 2 个会话 — `model_download`、`p8b_docred_latency`
- **P1 残留进程**: **有**
  - **PID 5964** — `tmux new-session -d -s mistral_v3_full ... python run_constrained_extraction.py --dataset wikievents ... --mode full_s1`（tmux server 进程仍存活，但 GPU 无占用，说明 Python 子进程可能已退出，仅 tmux session 壳残留）

### westd-16980
- **GPU**: 2× RTX PRO 6000 Black，0MiB 占用，无活跃进程 ✓
- **tmux**: 4 个会话 — `llama_beam`、`llama_wikievents`、`llama_wikievents_full`、`qwen_wikievents`
- **P1 残留进程**: 无 ✓

**总结**: 两台服务器 GPU 均空闲。westd-21461 上 PID 5964 是 `mistral_v3_full` 的 tmux server 进程（`run_constrained_extraction.py`），GPU 无占用说明 Python 进程已结束，仅 tmux 会话壳残留。等 Director 指示是否清理。

---
