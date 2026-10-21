# diagnose eval obs only object norm03 seed48

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm03-seed48_20260518T132245_result.json`
- **Structured JSON:** [`68d615abc57a02644a07.json`](../../sessions/68/68d615abc57a02644a07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：**误报（false positive）**。实验正常完成，EXIT_CODE=0，结果已写入 JSON。

监控系统将其标记为失败的原因是：进程正常退出后 PID 消失，但该评估脚本不写 sentinel 文件也不上报 W&B，监控连续 5 次检测到 "process dead" 就自动判定失败。

```json
{"root_cause":"False positive: process completed successfully (EXIT_CODE=0, overall success rate 16.0% (16/100), results saved to eval_object_obs_only_norm03_seed48.json) but monitoring detected 'process dead' because eval script writes no sentinel/W&B","error_type":"infrastructure","fix_steps":["No fix needed — experiment already completed successfully","Retrieve results from /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json","Consider adding sentinel file or W&B logging to evaluate.py to prevent future false positives"],"can_auto_fix":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "False positive: process completed successfully (EXIT_CODE=0, overall success rate 16.0% (16/100), results saved to eval_object_obs_only_norm03_seed48.json) but monitoring detected 'process dead' because eval script writes no sentinel/W&B",
    "error_type": "infrastructure",
    "fix_steps": [
      "No fix needed — experiment already completed successfully",
      "Retrieve results from /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed48.json",
      "Consider adding sentinel file or W&B logging to evaluate.py to prevent future false positives"
    ],
    "can_auto_fix": false
  }
}
```

</details>

---
