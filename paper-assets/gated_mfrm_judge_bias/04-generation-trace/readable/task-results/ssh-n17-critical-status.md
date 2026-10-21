# ssh n17 critical status

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_critical_status_20260524T043703_result.json`
- **Structured JSON:** [`22d8abf551bce4460797.json`](../../sessions/22/22d8abf551bce4460797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### N=17 Judge 评测进度（每个 judge × 18 target models × ~1000 items = 17000）

| Judge | 完成量 | 进度 | 每model均值 | 速率来源 |
|---|---|---|---|---|
| **claude-sonnet-4.6** | 4318/17000 | **25.4%** | ~240/1000 | API, 10 workers |
| **qwen3-235b** | 2864/17000 | **16.8%** | ~159/1000 | API, 10 workers |
| **gemini-2.5-pro** | 2799/17000 | **16.5%** | ~155/1000 | API, 10 workers |
| **deepseek-v4-pro** | 2360/17000 | **13.9%** | ~131/1000 | API, 10 workers |
| **llama-3.3-70b** | 414/17000 | **2.4%** | ~23/1000 | 本地 vLLM, 4 workers |
| **qwen2.5-72b** | 261/17000 | **1.5%** | ~14/1000 | 本地 vLLM, 4 workers |

18 个 target models 覆盖完整（claude/gpt/llama/gemma/mistral/mixtral/qwen 系列），各 target model 进度均匀。尚无任何 judge 完成任一 target model（需达 1000）。

### 进程状态

- **6 个 collect.py 进程全部在跑**（PID 503734, 505793, 506658, 506876, 506930, 506990）
- **vLLM**: port 8001 ✅ 200, port 8002 ✅ 200
- 日志显示 API judges ETA ~1500-1800min（约 25-30h），本地 judges ETA ~7500-11400min（约 5-8 天）
- qwen3-235b 最新日志有一条 500 error retry，但在继续

### Exp-017

- **PID 318082 运行中**，已运行 21h34m
- `coverage_simulation.csv`: 225 行（含 header）
- 无单独的 exp017 日志文件

### rtx6000-4x 连通性

- autodl-8gpu 上无 `~/.ssh/config`，无法从 autodl 直连 rtx6000-4x

---
