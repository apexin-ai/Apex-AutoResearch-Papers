# exp backbone scaling 70b

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_backbone-scaling-70b_20260517T084345_result.json`
- **Structured JSON:** [`8484a7e1d68d79a736cc.json`](../../sessions/84/8484a7e1d68d79a736cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job is running correctly, polling every 30s for shards. The shards download to temp locations first and get moved on completion. Everything is set up:

- **Download**: modelscope downloading 11 shards in parallel at ~16 MB/s total (~40 min estimated)
- **Job script**: `backbone-scaling-70b` tmux session, polling for shard completion
- **Once download finishes**: auto-starts episode collection on 11 task types x 20 episodes with TP=2 across both GPUs

**Code changes made**:
- `src/llm_agent.py`: added `tensor_parallel_size` parameter, auto-sets `CUDA_VISIBLE_DEVICES` for multi-GPU
- `src/episode_level_collection.py`: added `--tp` CLI arg, passes to LLMAgent

**Registry**: `backbone-scaling-70b` = RUNNING on westb-13313, cuda:0+cuda:1, Qwen2.5-72B-Instruct-AWQ

---
