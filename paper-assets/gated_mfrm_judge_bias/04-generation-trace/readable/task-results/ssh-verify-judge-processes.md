# ssh verify judge processes

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-judge-processes_20260524T095805_result.json`
- **Structured JSON:** [`044f6bea26832078df57.json`](../../sessions/04/044f6bea26832078df57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**监控报告有误——6/7 个 judge 存活，仅 mistral-large-2 真正停止。**

## 存活进程汇总

| Judge | PID | 进度 | 速度 | 数据量 | 最后写入 | 状态 |
|-------|-----|------|------|--------|---------|------|
| claude-sonnet-4.6-proxy | 506658 | 6560/15997 (41%) | 0.2 items/s | 8546行 | 17:58:42 | **ALIVE** |
| gemini-2.5-pro-proxy | 506876 | 4780/17092 (28%) | 0.2 items/s | 5981行 | 17:59:22 | **ALIVE** |
| deepseek-v4-pro-proxy | 506930 | 4100/17138 (24%) | 0.1 items/s | 5076行 | 17:58:56 | **ALIVE** |
| qwen3-235b-proxy | 506990 | 5280/16890 (31%) | 0.2 items/s | 6386行 | 17:58:42 | **ALIVE** |
| llama-3.3-70b-local | 564416 | — | — | 2071行 | 17:59:34 | **ALIVE** |
| qwen2.5-72b-local | 564492 | — | — | 1424行 | 17:59:57 | **ALIVE** |
| **mistral-large-2-local** | **无** | — | — | 118行 | **17:03:28** | **STOPPED** |

## GPU 状态

- GPU 0: 空闲 (0MiB, 0%)
- GPU 1: vLLM LLaMA (PID 502431, 100%, 92.9GB)
- GPU 2: vLLM Qwen (PID 504901, 100%, 91.1GB)
- GPU 3: 空闲 (0MiB, 0%)

## 关键发现

1. **6 个 judge 全部正常运行**，数据文件在最近 1 分钟内都有写入活动，监控脚本的 STOPPED 判断有误。
2. **mistral-large-2-local 确实停了**——无 collect.py 进程、无 vLLM 服务进程、数据文件停留在 17:03（近 1 小时前）、仅 118 行数据。GPU 0 和 GPU 3 空闲，没有为 mistral 提供推理服务。
3. llama 和 qwen local 的 `/tmp/collect_*_w32.log` 日志为空（0 字节），但数据在写入——日志可能重定向到了别处或 stdout 被 buffer。

---
