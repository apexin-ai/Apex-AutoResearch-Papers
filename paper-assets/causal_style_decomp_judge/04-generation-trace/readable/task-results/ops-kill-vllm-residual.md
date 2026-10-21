# ops kill vllm residual

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_vllm_residual_20260521T050605_result.json`
- **Structured JSON:** [`dfc5be404ce27b460694.json`](../../sessions/df/dfc5be404ce27b460694.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 vLLM 进程已 kill，GPU 已释放。

| GPU | 显存占用 | 总显存 |
|-----|---------|--------|
| 0 | 0 MiB | 97887 MiB |
| 1 | 0 MiB | 97887 MiB |
| 2 | 0 MiB | 97887 MiB |
| 3 | 0 MiB | 97887 MiB |

Kill 的进程：
- PID 104416/104421 — vLLM on port 8000 (GPU 0,1, tensor-parallel-size=2)
- PID 105392/105397 — vLLM on port 8002 (GPU 2, tensor-parallel-size=1)

---
