# code fix eval task list

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-eval-task-list_20260514T085940_result.json`
- **Structured JSON:** [`3415caf40b3eae579833.json`](../../sessions/34/3415caf40b3eae579833.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

### eval/eval_tasks_47.json
- **47 个任务**，从 `vanilla_react_baseline.json` 提取，与 baseline 完全一致
- 类型分布：
  - pick_clean_then_place_in_recep: 11
  - pick_and_place_simple: 8
  - pick_heat_then_place_in_recep: 8
  - pick_cool_then_place_in_recep: 7
  - pick_two_obj_and_place: 7
  - look_at_obj_in_light: 6
- 每条记录包含 `task_id`、`task_type`、`gamefile`（完整路径）、`task_desc`

### eval/recovery.py 修改
- **L450-462**: 新增 `load_task_list()` 函数，从 JSON 文件读取任务列表并转换为 `collect_game_files` 相同的 dict 格式
- **L481-482**: 新增 `--task_list` 参数
- **L500-502**: 如果指定了 `--task_list`，用 `load_task_list()` 加载；否则保持原有 `collect_game_files()` 行为

后续评测调用：`--task_list eval/eval_tasks_47.json`

---
