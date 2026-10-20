# code episode level collection

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_episode-level-collection_20260513T173842_result.json`
- **Structured JSON:** [`9ee1a7cbaede74993f37.json`](../../sessions/9e/9ee1a7cbaede74993f37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `/root/autodl-tmp/simgate-modular-routing/src/episode_level_collection.py`，`--help` 验证通过，import 无报错。

关键设计：
- 复用 `signal_prescreening.py` 的 episode 运行逻辑，每步额外记录 `action_history`（累积到当前步）
- Death episode 处理：final_score ≤ -100 自动判负，双死判 tie
- 输出 `labeled_steps.jsonl`（训练数据）+ `episode_summary.jsonl`，均为 append mode 支持增量补跑
- `--start_episode` 参数支持从已有数据后接着跑
- 运行结束打印 label 分布、avg score gap、death 统计

---
