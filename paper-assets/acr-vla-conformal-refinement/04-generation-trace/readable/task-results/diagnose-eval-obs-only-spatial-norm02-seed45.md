# diagnose eval obs only spatial norm02 seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-spatial-norm02-seed45_20260519T125406_result.json`
- **Structured JSON:** [`7e34a0d903595226af67.json`](../../sessions/7e/7e34a0d903595226af67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。两个实验的结论如下：

---

**eval-obs-only-spatial-norm02-seed45**：**误报，实验已正常完成。**

- 日志末尾打印 `Overall success rate (crm_obs_only): 34.0% (34/100)` 和 `Results saved to logs/eval_spatial_obs_only_norm02_seed45.json`
- JSON 输出文件完整（10 任务 × 10 rollouts）
- 无 Traceback、无 OOM、无 CUDA 错误
- 进程正常退出后 tmux session 被清理，cron 监控检测到"进程不存在 + 无 W&B"将其判定为失败——但 eval 任务本身不上报 W&B，这是监控的误判

**eval-obs-only-object-norm003-seed48**：该实验的 `obs_only` 版本不在此服务器上（无匹配文件）。服务器上有的是 `eval_object_perdof_norm003_seed48`（也已正常完成，success_rate=0.13），跳过。

```json
{
  "root_cause": "False positive: experiment completed successfully (log shows 'Overall success rate: 34.0% (34/100)' + JSON output written), but cron monitor classified it as failed because process exited normally and no W&B metrics were reported (eval jobs don't use W&B)",
  "error_type": "infrastructure",
  "fix_steps": [
    "Update cron monitor to check for output JSON file existence as a success sentinel for eval jobs",
    "No re-run needed — results are already in logs/eval_spatial_obs_only_norm02_seed45.json"
  ],
  "can_auto_fix": false
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "False positive: experiment completed successfully (log shows 'Overall success rate: 34.0% (34/100)' + JSON output written), but cron monitor classified it as failed because process exited normally and no W&B metrics were reported (eval jobs don't use W&B)",
    "error_type": "infrastructure",
    "fix_steps": [
      "Update cron monitor to check for output JSON file existence as a success sentinel for eval jobs",
      "No re-run needed — results are already in logs/eval_spatial_obs_only_norm02_seed45.json"
    ],
    "can_auto_fix": false
  }
}
```

</details>

---
