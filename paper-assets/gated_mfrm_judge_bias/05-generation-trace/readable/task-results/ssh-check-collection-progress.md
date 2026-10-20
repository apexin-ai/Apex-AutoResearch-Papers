# ssh check collection progress

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-collection-progress_20260524T083753_result.json`
- **Structured JSON:** [`2f0af840429349854eb4.json`](../../sessions/2f/2f0af840429349854eb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个 judge 均在运行。汇总如下：

## Judge Collection 进度 (exp-020, N=17)

| Judge | 进程 | 已完成 | /18000 | 完成% | 速率 | 预估剩余 |
|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | ✅ PID 506658 | 7,492 | 41.6% | ~17/min | ~10h |
| qwen3-235b | ✅ PID 506990 | 5,537 | 30.8% | ~13/min | ~16h |
| gemini-2.5-pro | ✅ PID 506876 | 5,214 | 29.0% | ~12/min | ~18h |
| deepseek-chat | ✅ PID 506930 | 4,440 | 24.7% | ~10/min | ~23h |
| llama-3.3-70b | ✅ PID 503734 | 1,015 | 5.6% | ~2.4/min | **~4.9天** |
| qwen2.5-72b | ✅ PID 505793 | 676 | 3.8% | ~1.6/min | **~7.2天** |
| mistral-large-2 | ✅ PID 556385 | 74 | 0.4% | ~1.2/min | **~10天** |

## GPU 状态

| GPU | 模型 | 显存占用 | 利用率 |
|---|---|---|---|
| 0 | 空闲 | 0 / 98GB | 0% |
| 1 | LLaMA-3.3-70B (vLLM:8001) | 92 / 98GB | 100% |
| 2 | Qwen2.5-72B (vLLM:8002) | 90 / 98GB | 100% |
| 3 | Mistral-Large (vLLM:8003) | 90 / 98GB | 100% |

## 磁盘
12G / 30G (40%)

## 关键问题

1. **Local judges 极慢**：3 个本地 judge 都只有 workers=4，vLLM 生成吞吐约 5.6 tokens/s（Mistral 日志），导致每分钟仅完成 1-2 条。按当前速率完成全部 18000 条需要 **5-10 天**。

2. **API judges 有间歇 500 错误**：Sonnet、Gemini、DeepSeek、Qwen3 日志中都出现 `Error code: 500 - Internal Server Error`，但有 retry 机制，目前仍在推进。

3. **Qwen2.5-72B 数据路径不一致**：数据写在 `output_n17_qwen2.5-72b-local/` 而非 `results/` 下，后续合并需注意。

4. **Mistral 刚启动不久**（15:16 才启动 vLLM），是 7 个 judge 中最晚的。

API judges 预计 10-23 小时内完成；local judges 按当前速率需要数天，是瓶颈所在。

---
