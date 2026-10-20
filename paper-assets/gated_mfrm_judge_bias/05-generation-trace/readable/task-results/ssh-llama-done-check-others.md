# ssh llama done check others

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama-done-check-others_20260524T160714_result.json`
- **Structured JSON:** [`8b6b9e7072c4b0df38d1.json`](../../sessions/8b/8b6b9e7072c4b0df38d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### LLaMA local (PID 584106) — 已完成 ✅
- **18,093 行**（目标 18,000）— 采满
- 日志: `Done. 11443 pairwise judgments in 209.5min`
- 最后写入: May 25 00:03

### 其余 3 个 judge — 全部在跑

| Judge | PID | 状态 | 运行时长 | 当前行数 | 进度 | 最后写入 |
|-------|-----|------|----------|----------|------|----------|
| Qwen local | 584197 | ALIVE | 3h33m | 12,630 | 70% | 00:08 |
| DeepSeek API | 592328 | ALIVE | 1h08m | 10,790 | 60% | 00:08 |
| Qwen3 API | 592432 | ALIVE | 1h06m | 13,457 | 75% | 00:08 |

### vLLM 进程 — 全部在跑
- LLaMA vLLM (582367): 3h37m — LLaMA collect 已结束但 vLLM 还在，Qwen local 仍需要 Qwen vLLM
- Qwen vLLM (583073): 3h36m

### 预估剩余时间
- **Qwen3 API** 最快完成，约 75% 进度，~30-40min
- **Qwen local** ~70%，按当前速率约 1.5h
- **DeepSeek API** ~60%，约 1-1.5h

LLaMA vLLM 进程可以关掉释放 GPU 0,1，但如果不需要这两张卡做别的事可以先留着。

---
