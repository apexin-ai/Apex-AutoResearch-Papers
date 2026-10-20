# data alfworld full 140

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_alfworld-full-140_20260514T135023_result.json`
- **Structured JSON:** [`c7f36c4a5074eaf8bb40.json`](../../sessions/c7/c7f36c4a5074eaf8bb40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 正常运行，总结：

- **tmux session**: `alfworld_cf`
- **GPU**: cuda:1 (RTX 5090, 32GB)
- **模型**: Qwen2.5-7B-Instruct via vLLM
- **Games**: 135 (valid_seen 实际数量，非 140)
- **第一个 episode**: no-preference, 86.4s
- **输出**: `results/alfworld_counterfactual/episodes.jsonl`
- **日志**: `results/alfworld_counterfactual/run.log`
- **预计完成时间**: ~3.5 小时（135 episodes × ~1.5 min/ep）

如需检查进度：`grep "Label" results/alfworld_counterfactual/run.log` 或 `wc -l results/alfworld_counterfactual/episodes.jsonl`。

---
