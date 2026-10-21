# code minihack det heuristic

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_minihack-det-heuristic_20260519T111653_result.json`
- **Structured JSON:** [`869d6ae7e2d86fd0969b.json`](../../sessions/86/869d6ae7e2d86fd0969b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入，语法验证通过。

**`minihack_det_agent.py`** — 核心 agent：
- `ActionMapper`: 从 env 的 action tuple 中通过 NLE enum 值匹配建立 direction/command → action index 映射，兼容不同 task 的 action space
- `parse_map()`: 用 `screen_descriptions` 文本匹配（主）+ NLE glyph 常量范围检查（辅）识别 walkable/goal/monster/item
- `bfs_path()`: 标准 BFS 寻路，支持 avoid set（低血量时绕开怪物）
- 生存优先级：低 HP + 相邻怪物 → 逃跑；饥饿 → 吃；脚下有物品 → 拾取
- 探索策略：goal 不可见时 BFS 到最近未探索 walkable cell
- 卡住检测：连续 5 步原地不动 → 尝试 SEARCH/KICK/OPEN
- 兼容 gym / gymnasium 两种 API（reset 和 step 返回值差异）

**`minihack_episode_runner.py`** — episode 批量运行器：
- 支持 `--strategy deterministic|internal|random`
- LLM agent 是 stub（接口已定义，集成 BALROG + vLLM 后填入 `act()`）
- JSONL 输出格式：`episode_id, task, strategy, score, died, goal_reached, steps, seed, wall_time_s`
- `--tasks-all` 可一次跑所有 5 个 navigation task
- `print_summary()` 汇总 win/death/avg_steps

`blstats` 索引和 hunger 阈值均按 NLE 源码校准（BL_HUNGER=21）。

---
