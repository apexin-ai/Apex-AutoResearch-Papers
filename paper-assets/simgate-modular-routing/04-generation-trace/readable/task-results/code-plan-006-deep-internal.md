# code plan 006 deep internal

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-006-deep-internal_20260515T143105_result.json`
- **Structured JSON:** [`a868a709a174c14f66ce.json`](../../sessions/a8/a868a709a174c14f66ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正常运行中。Episode 0 完成（65s），Episode 1 进行中。

**收集已启动，状态总结：**

- **实验**: `plan-006-deep-internal` (RUNNING)
- **服务器**: westb-13313, GPU1
- **任务**: 6 个 det-preferred 最高的 tasks × 20 episodes = 120 episodes
  - identify-life-stages-1 (45%), lifespan-longest-lived (44%), find-non-living-thing (40%), lifespan-longest-lived-then-shortest-lived (40%), inclined-plane-determine-angle (35%), chemistry-mix (30%)
- **模式**: Deep-internal（增强 CoT 系统 prompt + max_new_tokens=768）
- **速度**: ~65s/ep → 预计 120 × 65s ≈ 2.2 小时完成
- **输出**: `results/plan-006-deep-internal/{task}/episodes.jsonl`
- **日志**: `/tmp/plan006_deep_internal.log`
- **代码修改**:
  - `src/llm_agent.py`: 添加 `DEEP_REACT_SYSTEM_PROMPT` 和 `select_action_deep_react()` 方法（5 步结构化推理 prompt，max_tokens 临时提升至 768）
  - `src/episode_level_collection.py`: 添加 `run_episode_deep_internal()` 和 `--deep_internal` flag

---
