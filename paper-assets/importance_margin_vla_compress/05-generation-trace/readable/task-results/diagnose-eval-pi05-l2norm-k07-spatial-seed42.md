# diagnose eval pi05 l2norm k07 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k07_spatial_seed42_20260521T231804_result.json`
- **Structured JSON:** [`0f172c7c508021361c8e.json`](../../sessions/0f/0f172c7c508021361c8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都**正常完成**，结果文件已保存。监控系统误判——进程正常退出后不存在了，被当成"dead"。

```json
{"exp_id": "eval_pi05_l2norm_k07_spatial_seed42", "root_cause": "False alarm — experiment completed successfully at 07:06:06 with SR=67.0% (335/500). Log: logs/eval_pi05_l2norm_k07_spatial_seed42.log. Result saved: eval_results/pi05_l2norm_k0.70_libero_spatial_seed42.json. Monitoring misclassified normal exit as failure (no sentinel/W&B integration).", "error_type": "infrastructure", "fix_steps": ["No fix needed — experiment succeeded", "Consider adding sentinel file or W&B logging to eval script to prevent future false alarms"], "can_auto_fix": false}
```
```json
{"exp_id": "eval_pi05_random_k085_object_seed42_v2", "root_cause": "False alarm — experiment completed successfully at 07:11:52 with SR=5.0% (25/500). Log: /tmp/eval_pi05_random_k085_object_seed42_v2.log. Result saved: eval_results/pi05_random_k0.85_libero_object_seed42.json. PID 824147 gone because process exited normally.", "error_type": "infrastructure", "fix_steps": ["No fix needed — experiment succeeded", "Note: SR=5.0% is extremely low for random k=0.85 on object suite — may indicate a methodological issue, not a runtime failure"], "can_auto_fix": false}
```

关键数据摘要：
- **l2norm k=0.7 spatial**: SR=67.0%, 耗时 98.8min, 10/10 tasks 全部跑完
- **random k=0.85 object**: SR=5.0%, 耗时 108.5min, 10/10 tasks 全部跑完（SR 极低但脚本本身没出错）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp_id": "eval_pi05_random_k085_object_seed42_v2",
    "root_cause": "False alarm — experiment completed successfully at 07:11:52 with SR=5.0% (25/500). Log: /tmp/eval_pi05_random_k085_object_seed42_v2.log. Result saved: eval_results/pi05_random_k0.85_libero_object_seed42.json. PID 824147 gone because process exited normally.",
    "error_type": "infrastructure",
    "fix_steps": [
      "No fix needed — experiment succeeded",
      "Note: SR=5.0% is extremely low for random k=0.85 on object suite — may indicate a methodological issue, not a runtime failure"
    ],
    "can_auto_fix": false
  }
}
```

</details>

---
