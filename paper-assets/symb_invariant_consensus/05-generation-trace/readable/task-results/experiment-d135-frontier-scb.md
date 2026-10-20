# experiment d135 frontier scb

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d135-frontier-scb_20260521T135204_result.json`
- **Structured JSON:** [`d13938a30fe14a093b7f.json`](../../sessions/d1/d13938a30fe14a093b7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**20 题汇总出来了！**

## gpt-4.1 FOLIO SC@12 — 20 题中间结果

| 指标 | 值 |
|------|-----|
| **SC accuracy** | **85.0% (17/20)** |
| 速率 | 2.9 q/min |
| ETA | ~63 min |

错误分析：
- folio_7: gold=Unknown, SC=False (7:5)
- folio_18: gold=True, SC=Unknown (11:1) 
- folio_19: gold=True, SC=Unknown (9:3)

**对比开源模型 baseline (FOLIO-204 全集)：**

| Model | SC@12 Accuracy |
|-------|---------------|
| Mistral-7B | 54% |
| Qwen3-32B | 70% |
| Qwen2.5-14B | 74% |
| **gpt-4.1 (前20题)** | **85.0%** |

gpt-4.1 显著超过所有开源模型。趋势：Unknown→True 方向的错误居多（gpt-4.1 倾向保守判断 Unknown）。

3 个进程都在跑。gpt-5.5 约 2/204, o3 遇 500 较多（~1/204）。预计 gpt-4.1 全部完成约 23:15 (CST)。gpt-5.5 和 o3 因 reasoning model 更慢，可能 2-3 小时。

---
