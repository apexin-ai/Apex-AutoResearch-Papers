# ssh check exp020 progress

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp020-progress_20260524T092543_result.json`
- **Structured JSON:** [`5982df5667ca82646527.json`](../../sessions/59/5982df5667ca82646527.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-020 N=17 Judge Collection 进度

| Judge | 类型 | 进程状态 | 已完成 | /18000 | 完成% | 速率 | 预估剩余 |
|-------|------|---------|--------|--------|-------|------|---------|
| Claude Sonnet 4.6 | API | **运行中** | 8124 | 18000 | 45.1% | 0.2 it/s | ~12h |
| Qwen3 235B | API | **运行中** | 6049 | 18000 | 33.6% | 0.2 it/s | ~18h |
| Gemini 2.5 Pro | API | **运行中** | 5700 | 18000 | 31.7% | 0.2 it/s | ~21h |
| DeepSeek V4 Pro | API | **运行中** | 4863 | 18000 | 27.0% | 0.1 it/s | ~25h |
| LLaMA 3.3 70B | Local | **运行中** | 1504 | 18000 | 8.4% | ~3.2 it/min | ~3.5d |
| Qwen2.5 72B | Local | **运行中** | 1012 | 18000 | 5.6% | ~2.2 it/min | ~5.3d |
| Mistral Large 2 | Local | **已停止** | 118 | 18000 | 0.7% | — | — |

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 0 / 95.6 GB | 0% (空闲) |
| 1 | 90.7 / 95.6 GB | 100% |
| 2 | 89.0 / 95.6 GB | 100% |
| 3 | 0 / 95.6 GB | 0% (空闲) |

### 磁盘
30G 总量，已用 12G (40%)，剩余 19G。

### 问题
**Mistral Large 2 已崩溃** — 进程不存在，文件最后修改时间 17:03（约 25 分钟前停止更新），仅采集 118 条。日志文件为空。GPU 0 和 3 均空闲，可能是 Mistral 释放的。需要重启。

---
