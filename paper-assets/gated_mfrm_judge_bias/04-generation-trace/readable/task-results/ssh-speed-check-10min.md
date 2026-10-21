# ssh speed check 10min

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_speed_check_10min_20260524T023739_result.json`
- **Structured JSON:** [`339cb8455422b101ebeb.json`](../../sessions/33/339cb8455422b101ebeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 10 分钟速率测量报告

**T0**: 02:38:50 UTC — **T1**: 02:49:29 UTC — **间隔**: 10.65 min

### API Judges

| Judge | T0 | T1 | Δ | items/min | 剩余 | ETA (h) |
|-------|----:|----:|--:|----------:|------:|--------:|
| claude-sonnet-4.6 | 2647 | 2806 | 159 | **14.9** | ~14,200 | 15.9 |
| gemini-2.5-pro | 1566 | 1684 | 118 | **11.1** | ~15,400 | 23.2 |
| deepseek-v4-pro | 1258 | 1368 | 110 | **10.3** | ~15,800 | 25.4 |
| qwen3-235b | 1509 | 1632 | 123 | **11.5** | ~15,300 | 22.0 |
| **API 总计** | | | **510** | **47.9** | | |

### Local Judges

| Judge | T0 | T1 | Δ | items/min | 剩余 | ETA (h) |
|-------|----:|----:|--:|----------:|------:|--------:|
| llama-3.3-70b | 132 | 154 | 22 | 2.1 | ~17,800 | **143** |
| qwen2.5-72b | 83 | 99 | 16 | 1.5 | ~17,900 | **199** |

### 关键判断

**N=17 主路径可行。** API 总速率 47.9/min，远超 8/min 阈值。每个 API judge 单独都在 10-15/min，最慢的 deepseek 也有 10.3/min。API judges 全部在 ~1 天内可完成。

**Local judges 是瓶颈。** LLaMA 和 Qwen2.5 本地推理极慢（1.5-2.1 items/min），ETA 分别 6 天和 8 天。需要关注 local judges 是否有加速空间（增加 batch size、换更快的推理后端等），否则它们会拖住整体进度。

---
