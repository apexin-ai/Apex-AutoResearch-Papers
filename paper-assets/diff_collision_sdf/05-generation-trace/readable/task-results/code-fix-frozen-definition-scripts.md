# code fix frozen definition scripts

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_frozen_definition_scripts_20260526T095452_result.json`
- **Structured JSON:** [`20399efcd4a418a6a9a4.json`](../../sessions/20/20399efcd4a418a6a9a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

输出确认：已有 reeval 数据的两个模型 frozen 均为 `0.0`（EE-based），terminal header 显示为 `Frz(EE)`。

修改汇总：

**analyze_displacement.py**:
- 新增 `compute_frozen_rate_ee()` — EE displacement frozen 计算（论文定义）
- 新增 `compute_frozen_rate_obs()` — obstacle displacement frozen 计算（旧定义，保留备用）
- `analyze_task()` 第34行：`e["max_displacement"]` → `e.get("max_ee_displacement", float('inf'))`

**reeval_comparison.py**:
- `METRIC_LABELS["frozen"]` → `"Frozen (%, EE-based)"`
- terminal header `New Frz` → `Frz(EE)`
- OLD_DATA/NEW_DATA 顶部添加注释：frozen = EE-based
- `load_json_results()` 新增：从 JSON per-episode 数据中用 `max_ee_displacement` 计算 frozen

---
