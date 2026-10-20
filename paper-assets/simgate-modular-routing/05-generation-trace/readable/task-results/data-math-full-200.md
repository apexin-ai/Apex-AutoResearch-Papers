# data math full 200

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_math-full-200_20260514T140908_result.json`
- **Structured JSON:** [`9d65b4886bcc3971835b.json`](../../sessions/9d/9d65b4886bcc3971835b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务正常运行中。

**状态汇总：**
- 进程：tmux session `math200` 正在运行，vLLM server 在 `vllm_server` session
- 输出：`data/math-counterfactual/full_200.jsonl`，JSONL 格式正确
- 速度：~7-8s/题，200 题预计 ~25-28 分钟
- 预计完成时间：约 22:45 (UTC+8)
- 包含 pilot 的前 50 题（同 seed=42，顺序选取），后续用 `episode_id` 去重合并

字段包含：`episode_id`, `internal.correct`, `deterministic.correct`, `label`, `raw_label`, `filtered`, `deterministic.n_rounds` 等，满足要求。

---
