# ssh kill qwen vllm

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-qwen-vllm_20260524T183416_result.json`
- **Structured JSON:** [`2adf65f275ea679def51.json`](../../sessions/2a/2adf65f275ea679def51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Kill 的 PID：** 583073, 583078, 583362, 583627, 583628（Qwen vLLM APIServer + EngineCore + Worker_TP0 + Worker_TP1）

**GPU 显存状态：**
| GPU | 已用 | 总量 |
|-----|------|------|
| 0 | 0 MiB | 97887 MiB |
| 1 | 0 MiB | 97887 MiB |
| 2 | 0 MiB | 97887 MiB |
| 3 | 0 MiB | 97887 MiB |

GPU 2,3 已完全释放。

**采集进程正常运行：**
- DeepSeek 采集 (PID 592328) — `config_deepseek-v4-pro-proxy_arena_n17.yaml`
- Qwen3 采集 (PID 592432) — `config_qwen3-235b-proxy_arena_n17.yaml`

两个采集进程走 API，不受影响。

---
