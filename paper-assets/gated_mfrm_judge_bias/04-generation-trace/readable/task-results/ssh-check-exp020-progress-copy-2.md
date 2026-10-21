# ssh check exp020 progress

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp020-progress_20260524T151719_result.json`
- **Structured JSON:** [`d02db5bf5193c6a686fe.json`](../../sessions/d0/d02db5bf5193c6a686fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-020 Judge 评测采集进度汇总

### 进程状态：全部存活 ✓

| PID | 角色 | 状态 | 运行时长 |
|-----|------|------|---------|
| 582367 | vLLM LLaMA (GPU 0,1) | **ALIVE** | 2h47m |
| 583073 | vLLM Qwen (GPU 2,3) | **ALIVE** | 2h46m |
| 584106 | LLaMA local collect | **ALIVE** | 2h44m |
| 584197 | Qwen local collect | **ALIVE** | 2h43m |
| 592328 | DeepSeek API collect | **ALIVE** | 18m |
| 592432 | Qwen3-235B API collect | **ALIVE** | 16m |

### 采集进度（目标 18,000 行/judge）

| Judge | 行数 | 完成度 | 最后写入时间 | 速率 & ETA |
|-------|------|--------|-------------|-----------|
| **LLaMA-3.3-70B local** | 15,534 | **86.3%** | 23:18:05 | 0.9 items/s, ETA ~64min |
| **Qwen2.5-72B local** | 10,692 | **59.4%** | 23:18:04 | 0.6 items/s, ETA ~201min |
| **DeepSeek-V4-Pro API** | 9,988 | **55.5%** | 23:17:37 | 刚启动18min，无速率日志 |
| **Qwen3-235B API** | 12,073 | **67.1%** | 23:18:05 | 刚启动16min，无速率日志 |

### 先前完成的 n17 judges（非本轮进程）

| Judge | 行数 |
|-------|------|
| Claude Sonnet 4.6 | 14,255 |
| Gemini 2.5 Pro | 11,253 |
| Mistral Large 2 | 118 (异常低) |

### 异常

1. **Mistral Large 2 local_n17 只有 118 行**——远低于 18,000 目标，可能采集中断后未重启
2. **DeepSeek / Qwen3 API 进程无独立日志文件**（/tmp 下没有对应 log），无法检查错误。建议确认输出是否重定向到了其他位置
3. **Qwen2.5-72B local ETA ~3.3h**，速率 0.6 items/s 明显低于 LLaMA 的 0.9 items/s

---
