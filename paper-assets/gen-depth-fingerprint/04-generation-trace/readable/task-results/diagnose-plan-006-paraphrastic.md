# diagnose plan 006 paraphrastic

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-006-paraphrastic_20260515T231423_result.json`
- **Structured JSON:** [`d93ad01edddea2ed0ecb.json`](../../sessions/d9/d93ad01edddea2ed0ecb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论清晰了。

**实验 plan-006-paraphrastic 没有失败。** 它成功运行完毕（return_code=0），三个阶段全部完成：

- **generate**: 995 seeds → paraphrastic chains（~5500秒）
- **features**: 提取了 4754 条特征
- **evaluate**: 5-fold CV 完成，结果已存 `results/plan006_paraphrastic_comparison.json`

**Cron 误判原因**：脚本中没有任何 `wandb` 集成（grep 确认零匹配），cron 的判定逻辑是检查 W&B metrics 是否存在，找不到就判 failed——这是 **false negative**。

```json
{"root_cause":"脚本未集成 wandb，cron 以 'no W&B metrics' 为条件判定失败，但实验实际 return_code=0 且结果已保存到 results/plan006_paraphrastic_comparison.json","error_type":"infrastructure","fix_steps":["将 cron 判定逻辑改为同时检查 W&B metrics 和 results JSON 文件是否存在","或在 paraphrastic_chains.py 中添加 wandb.log 调用上报关键指标（3-class F1=0.68, retention=0.89）"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "脚本未集成 wandb，cron 以 'no W&B metrics' 为条件判定失败，但实验实际 return_code=0 且结果已保存到 results/plan006_paraphrastic_comparison.json",
    "error_type": "infrastructure",
    "fix_steps": [
      "将 cron 判定逻辑改为同时检查 W&B metrics 和 results JSON 文件是否存在",
      "或在 paraphrastic_chains.py 中添加 wandb.log 调用上报关键指标（3-class F1=0.68, retention=0.89）"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
