# diagnose eval plan a spatial seed42 43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-plan-a-spatial-seed42-43_20260521T000346_result.json`
- **Structured JSON:** [`cddf4af25cf7a59f2150.json`](../../sessions/cd/cddf4af25cf7a59f2150.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都正常完成，cron false positive 确认。日志末尾都有 "Results saved to" 且 return_code=0。

```json
{
  "seed42": {
    "actual_status": "completed",
    "output_json_exists": true,
    "success_rate": "34.0% (34/100)",
    "per_task_results": {
      "between_plate_and_ramekin": "90% (9/10)",
      "next_to_ramekin": "90% (9/10)",
      "from_table_center": "0% (0/10)",
      "on_cookie_box": "40% (4/10)",
      "in_top_drawer": "0% (0/10)",
      "on_ramekin": "0% (0/10)",
      "next_to_cookie_box": "100% (10/10)",
      "on_stove": "0% (0/10)",
      "next_to_plate": "20% (2/10)",
      "on_wooden_cabinet": "0% (0/10)"
    },
    "mean_uncertainty": 0.2679,
    "trigger_rate": 0.976,
    "root_cause": "cron false positive — eval 脚本不写 W&B/sentinel，正常退出后 cron 检测不到标记"
  },
  "seed43": {
    "actual_status": "completed",
    "output_json_exists": true,
    "success_rate": "35.0% (35/100)",
    "per_task_results": {
      "between_plate_and_ramekin": "80% (8/10)",
      "next_to_ramekin": "100% (10/10)",
      "from_table_center": "0% (0/10)",
      "on_cookie_box": "40% (4/10)",
      "in_top_drawer": "10% (1/10)",
      "on_ramekin": "0% (0/10)",
      "next_to_cookie_box": "90% (9/10)",
      "on_stove": "0% (0/10)",
      "next_to_plate": "30% (3/10)",
      "on_wooden_cabinet": "0% (0/10)"
    },
    "mean_uncertainty": 0.2619,
    "trigger_rate": 0.980,
    "root_cause": "cron false positive — eval 脚本不写 W&B/sentinel，正常退出后 cron 检测不到标记"
  },
  "diagnosis": "false_positive",
  "fix_steps": [],
  "summary": "三个 seed 结果一致：seed42=34.0%, seed43=35.0%, seed44=36.0%。方差很小，实验全部有效完成。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "seed42": {
      "actual_status": "completed",
      "output_json_exists": true,
      "success_rate": "34.0% (34/100)",
      "per_task_results": {
        "between_plate_and_ramekin": "90% (9/10)",
        "next_to_ramekin": "90% (9/10)",
        "from_table_center": "0% (0/10)",
        "on_cookie_box": "40% (4/10)",
        "in_top_drawer": "0% (0/10)",
        "on_ramekin": "0% (0/10)",
        "next_to_cookie_box": "100% (10/10)",
        "on_stove": "0% (0/10)",
        "next_to_plate": "20% (2/10)",
        "on_wooden_cabinet": "0% (0/10)"
      },
      "mean_uncertainty": 0.2679,
      "trigger_rate": 0.976,
      "root_cause": "cron false positive — eval 脚本不写 W&B/sentinel，正常退出后 cron 检测不到标记"
    },
    "seed43": {
      "actual_status": "completed",
      "output_json_exists": true,
      "success_rate": "35.0% (35/100)",
      "per_task_results": {
        "between_plate_and_ramekin": "80% (8/10)",
        "next_to_ramekin": "100% (10/10)",
        "from_table_center": "0% (0/10)",
        "on_cookie_box": "40% (4/10)",
        "in_top_drawer": "10% (1/10)",
        "on_ramekin": "0% (0/10)",
        "next_to_cookie_box": "90% (9/10)",
        "on_stove": "0% (0/10)",
        "next_to_plate": "30% (3/10)",
        "on_wooden_cabinet": "0% (0/10)"
      },
      "mean_uncertainty": 0.2619,
      "trigger_rate": 0.98,
      "root_cause": "cron false positive — eval 脚本不写 W&B/sentinel，正常退出后 cron 检测不到标记"
    },
    "diagnosis": "false_positive",
    "fix_steps": [],
    "summary": "三个 seed 结果一致：seed42=34.0%, seed43=35.0%, seed44=36.0%。方差很小，实验全部有效完成。"
  }
}
```

</details>

---
