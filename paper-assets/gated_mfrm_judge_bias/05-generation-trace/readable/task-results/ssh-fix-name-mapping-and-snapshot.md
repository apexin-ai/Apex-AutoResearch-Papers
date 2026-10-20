# ssh fix name mapping and snapshot

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-name-mapping-and-snapshot_20260524T095707_result.json`
- **Structured JSON:** [`1ef498748e0b04a5f5f7.json`](../../sessions/1e/1ef498748e0b04a5f5f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成。

**任务 1: ARENA_NAME_MAPPING 修复**
- 添加了 4 条 name mapping (`llama-3.3-70b-instruct`, `qwen2.5-72b-instruct`, `gpt-3.5-turbo-0613`, `mistral-large-2407`)
- 添加了 `mistral-large-2407: 1250` 到 ARENA_ELO
- 验证结果：17/18 targets 有 ELO mapping，唯一缺失的 `qwen3-8b` 是预期行为（它在 `ESTIMATED_ELO` 中，没有官方 Arena 排名）

**任务 2: snapshot_judge_data.sh** — 已创建并 chmod +x

**任务 3: check_progress.sh** — 已创建，当前进度快照：

| Judge | Records | Progress |
|-------|---------|----------|
| claude-sonnet-4.6-proxy | 8,541 | 47.4% |
| qwen3-235b-proxy | 6,378 | 35.4% |
| gemini-2.5-pro-proxy | 5,977 | 33.2% |
| deepseek-v4-pro-proxy | 5,071 | 28.1% |
| llama-3.3-70b-local | 2,057 | 11.4% |
| qwen2.5-72b-local | 1,402 | 7.8% |
| mistral-large-2-local | 118 | 0.7% |

GPU 1/2 满载运行（~92GB used, 100% util），GPU 0/3 空闲。磁盘 40% used (12G/30G)。

---
