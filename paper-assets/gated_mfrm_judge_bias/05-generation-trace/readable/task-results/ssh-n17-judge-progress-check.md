# ssh n17 judge progress check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_judge_progress_check_20260523T191925_result.json`
- **Structured JSON:** [`67e97614706d0beddb31.json`](../../sessions/67/67e97614706d0beddb31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个 judge 都在运行中，无一完成。当前状态：

## Judge 进度表（目标: 18,000 / judge）

| Judge | 当前行数 | 完成度 | 速率 (items/hr) | 剩余 | 预估完成 |
|-------|---------|--------|----------------|------|---------|
| claude-sonnet-4.6-proxy | 10,615 | 59.0% | ~407 | 7,385 | **~May 25 00:00** |
| qwen3-235b-proxy | 7,786 | 43.3% | ~236 | 10,214 | **~May 25 22:00** |
| deepseek-v4-pro-proxy | 6,540 | 36.3% | ~150 | 11,460 | **~May 27 07:00** |
| gemini-2.5-pro-proxy | 7,399 | 41.1% | ~86 | 10,601 | **~May 29 06:00** |
| **llama-3.3-70b** | 6,370 | 35.4% | **~43** | 11,630 | **~June 4** |
| **qwen2.5-72b** | 9,397 | 52.2% | **~21** | 8,603 | **~June 10** |
| **mistral-large-2** | 9,103 | 50.6% | **~21** | 8,897 | **~June 11** |

## 关键问题：本地 judge 极慢

3 个本地 vLLM judge 的瓶颈：

- vLLM 仅处理 **1 个并发请求**（Running: 1, Waiting: 0），KV cache 利用率仅 1-4%
- 生成速度：llama/qwen ~2.6 tok/s, mistral ~1.4 tok/s
- collect.py 串行发请求（一个完成才发下一个），完全没用上 vLLM 的 batching 能力
- 按当前速度，本地 judge 需要 **11-18 天**才能完成

## 建议

1. **提高本地 judge 并发度**：修改 collect.py 或启动多个 worker 并发向 vLLM 发请求。vLLM 的 continuous batching 在并发时吞吐量会大幅提升（当前 KV cache 有 96-99% 空闲）
2. **API judge 可等**：sonnet/qwen3 在 1-2 天内完成，gemini/deepseek 3-5 天
3. **或者考虑不等本地 judge 全部完成**：先用 API judge 数据启动 MCMC fitting 验证 pipeline

需要我排查 collect.py 的并发设计并修改提速吗？

---
