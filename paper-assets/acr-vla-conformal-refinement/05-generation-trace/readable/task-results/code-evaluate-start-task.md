# code evaluate start task

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_evaluate-start-task_20260515T215024_result.json`
- **Structured JSON:** [`d635cb00a2cddf1fbc56.json`](../../sessions/d6/d635cb00a2cddf1fbc56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结修改：

**evaluate.py**:
- `--start_task` 已存在，新增 `--end_task`（int, default=None，exclusive upper bound）
- Task 切片逻辑改为 `task_envs[start_task:end_idx]`，范围外的 env 正确 close

**src/analysis/merge_eval_results.py**（新建）:
- 合并多个 partial JSON：`python merge_eval_results.py part1.json part2.json -o merged.json`
- 检查 task 不重叠（重复报错退出），mode/benchmark 不一致给 WARNING
- 重新计算 overall_success_rate

**用法示例**（跑 T6-T9）:
```bash
python src/evaluate.py --benchmark spatial --start_task 6 --output_file logs/eval_spatial_part2.json ...
# 合并
python src/analysis/merge_eval_results.py logs/eval_spatial_part1.json logs/eval_spatial_part2.json -o logs/eval_spatial_merged.json
```

---
