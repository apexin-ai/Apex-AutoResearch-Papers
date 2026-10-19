# diagnose eval perdof object norm01 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-perdof-object-norm01-seed44_20260517T105221_result.json`
- **Structured JSON:** [`1a8d25c286c530d1735c.json`](../../sessions/1a/1a8d25c286c530d1735c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**已完整运行并成功结束**。所有 10 个任务 × 10 rollouts = 100 rollouts 全部完成，结果已写入 JSON。

```json
{"root_cause":"nohup 实验无 W&B 集成，cron 监控 5 次检测不到活跃进程/W&B heartbeat，误判为失败。实际 log 末尾显示 'Overall success rate (crm_perdof): 8.0% (8/100)' 并正常写入 JSON","error_type":"cron_misdiagnosis","actually_completed":true,"metrics":{"overall_sr":0.08,"per_task_sr":{"alphabet_soup":0.0,"cream_cheese":0.0,"salad_dressing":0.2,"bbq_sauce":0.1,"ketchup":0.0,"tomato_sauce":0.0,"butter":0.0,"milk":0.0,"chocolate_pudding":0.2,"orange_juice":0.3}},"fix_steps":["无需修复，实验已正常完成","将结果 overall_sr=0.08 录入汇总表"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "nohup 实验无 W&B 集成，cron 监控 5 次检测不到活跃进程/W&B heartbeat，误判为失败。实际 log 末尾显示 'Overall success rate (crm_perdof): 8.0% (8/100)' 并正常写入 JSON",
    "error_type": "cron_misdiagnosis",
    "actually_completed": true,
    "metrics": {
      "overall_sr": 0.08,
      "per_task_sr": {
        "alphabet_soup": 0.0,
        "cream_cheese": 0.0,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.1,
        "ketchup": 0.0,
        "tomato_sauce": 0.0,
        "butter": 0.0,
        "milk": 0.0,
        "chocolate_pudding": 0.2,
        "orange_juice": 0.3
      }
    },
    "fix_steps": [
      "无需修复，实验已正常完成",
      "将结果 overall_sr=0.08 录入汇总表"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
