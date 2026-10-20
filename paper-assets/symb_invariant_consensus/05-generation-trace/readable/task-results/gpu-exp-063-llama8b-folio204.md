# gpu exp 063 llama8b folio204

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-063-llama8b-folio204_20260519T073755_result.json`
- **Structured JSON:** [`3fe12b90272207604e15.json`](../../sessions/3f/3fe12b90272207604e15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正在处理第 2 题。实验稳定运行中。

**exp-063 状态汇总：**
- **服务器**: westd-16639, GPU cuda:0, vLLM 端口 8004
- **模型**: Meta-Llama-3.1-8B-Instruct
- **数据**: FOLIO-204, K=12, T=0.7, seed=42
- **Dryrun**: 3/3 通过（SICA 66.7%, SC 33.3%）
- **全量**: 已启动，tmux session `exp063_run`，预计 ~5 小时完成
- **Tie-breaking**: 已确认修正版 `max(sorted(groups.keys()), ...)`
- **Registry**: exp-063 → RUNNING, parent=exp-020
- **输出**: `results/exp-063-llama8b-folio204-16639/exp063_results.json`

完成后需检查日志中 `FULL_MVP_DONE` 标志，读取结果获取 SC%、SICA%、Δ(pp)。

---
