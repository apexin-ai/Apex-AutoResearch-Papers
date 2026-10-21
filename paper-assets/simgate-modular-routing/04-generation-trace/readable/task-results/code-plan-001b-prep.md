# code plan 001b prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-001b-prep_20260513T183608_result.json`
- **Structured JSON:** [`07e4a0d2d30814213825.json`](../../sessions/07/07e4a0d2d30814213825.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，参数解析正常。

产出：
- **远程文件**：`/root/autodl-tmp/simgate-modular-routing/src/collect_trajectories.py`
- **`--help` 验证通过**，所有 CLI 参数可正常解析

与现有 `episode_level_collection.py` 的主要区别：
1. 每步额外记录 `available_actions`、`is_death`、`observation_text`（步骤执行前的 obs）
2. 输出分两层：`raw_episodes.jsonl`（两种 modality 的完整 episode 数据）+ `sft_triples.jsonl`（仅 winning modality 的 (obs, action, label) 三元组）
3. Death episode 自动判负逻辑保持一致，tie 时不产出 SFT 数据
4. 全局统计写入 `collection_summary.json`

---
