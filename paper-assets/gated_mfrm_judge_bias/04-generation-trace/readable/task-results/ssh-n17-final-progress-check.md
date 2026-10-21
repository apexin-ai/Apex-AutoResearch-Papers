# ssh n17 final progress check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_final_progress_check_20260524T041046_result.json`
- **Structured JSON:** [`1d575fba333da0edc1fa.json`](../../sessions/1d/1d575fba333da0edc1fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## N=17 数据收集进度汇总

### 进程状态

| 进程 | PID | 状态 | 备注 |
|------|-----|------|------|
| collect.py — llama-3.3-70b-local | 503734 | **运行中** | workers=4 |
| collect.py — qwen2.5-72b-local | 505793 | **运行中** | workers=4 |
| collect.py — claude-sonnet-4.6-proxy | 506658 | **运行中** | workers=10 |
| collect.py — gemini-2.5-pro-proxy | 506876 | **运行中** | workers=10 |
| collect.py — deepseek-v4-pro-proxy | 506930 | **运行中** | workers=10 |
| collect.py — qwen3-235b-proxy | 506990 | **运行中** | workers=10 |
| vLLM — Llama-3.3-70B-AWQ | 502063 | **运行中** | port 8001, GPU 1 |
| vLLM — Qwen2.5-72B-AWQ | 504621 | **运行中** | port 8002, GPU 2 |
| run_exp017.py | 318082 | **运行中** | 已运行 21h07m |

### 数据收集进度

| Judge | 条数 | 进度 |
|-------|------|------|
| claude-sonnet-4.6-proxy | 3,906 / 18,000 | 21.7% |
| qwen3-235b-proxy | 2,526 / 18,000 | 14.0% |
| gemini-2.5-pro-proxy | 2,514 / 18,000 | 14.0% |
| deepseek-v4-pro-proxy | 2,091 / 18,000 | 11.6% |
| llama-3.3-70b-local | 337 / 18,000 | 1.9% |
| qwen2.5-72b-local | 218 / 18,000 | 1.2% |

6 个 judge 的 collect.py 全部在运行。API judge（10 workers）速度明显快于 local judge（4 workers，受 vLLM 吞吐限制）。Local judge 数据写入在 `results/` 目录，API judge 也在 `results/` 目录下。

---
