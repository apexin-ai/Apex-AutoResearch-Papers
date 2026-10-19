# diagnose eval obs only spatial norm02 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-spatial-norm02-seed44_20260519T141510_result.json`
- **Structured JSON:** [`db60f75ce64f79aae743.json`](../../sessions/db/db60f75ce64f79aae743.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验实际上已成功完成，是监控误判。**

输出文件 `logs/eval_spatial_obs_only_norm02_seed44.json` 存在且包含完整结果：

- 10 个 spatial 任务 × 10 rollouts = 100 次评估全部完成
- Overall success rate: **0.36**
- 无 OOM，无基础设施问题

监控系统报 failed 的原因：该实验没有写 sentinel 文件，也没有 W&B 集成，标准日志路径 `~/runs/.../eval-obs-only-spatial-norm02-seed44.log` 不存在。监控轮询 5 次发现进程已退出且无成功标记，就自动判定为失败。实际上进程是正常退出的。

```json
{"root_cause":"False positive: experiment completed successfully (output file exists with full results, 0.36 success rate across 10 tasks × 10 rollouts), but monitoring detected 'process dead 5× with no sentinel/W&B' because no sentinel file was written and no W&B run was configured","error_type":"infrastructure","fix_steps":["Mark this experiment as succeeded with result 0.36","Retrieve results from /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json","Consider adding sentinel file writing to evaluate.py for future monitoring compatibility"],"can_auto_fix":true,"retry_recommended":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "False positive: experiment completed successfully (output file exists with full results, 0.36 success rate across 10 tasks × 10 rollouts), but monitoring detected 'process dead 5× with no sentinel/W&B' because no sentinel file was written and no W&B run was configured",
    "error_type": "infrastructure",
    "fix_steps": [
      "Mark this experiment as succeeded with result 0.36",
      "Retrieve results from /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json",
      "Consider adding sentinel file writing to evaluate.py for future monitoring compatibility"
    ],
    "can_auto_fix": true,
    "retry_recommended": false
  }
}
```

</details>

---
