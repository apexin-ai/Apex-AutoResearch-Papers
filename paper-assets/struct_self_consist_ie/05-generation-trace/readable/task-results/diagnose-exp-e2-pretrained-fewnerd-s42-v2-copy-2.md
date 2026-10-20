# diagnose exp e2 pretrained fewnerd s42 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_e2_pretrained_fewnerd_s42_v2_20260521T232238_result.json`
- **Structured JSON:** [`eaece3beaa76917ba730.json`](../../sessions/ea/eaece3beaa76917ba730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这个实验实际上**已经成功完成**了。日志显示：

- 37648 个实例全部处理完毕（100%）
- 最终 Verdict: **PASS**
- Greedy F1: 0.5116, Oracle F1: 0.6169, Oracle headroom: +0.1053
- Structural > Surface: YES (delta=+0.0466)
- 报告已保存到 `output/e2_pretrained_fewnerd_s42/report.json`
- vLLM engine 正常 shutdown

日志文件名是 `e2_pretrained_fewnerd_s42.log`（无 `_v2` 后缀），说明这个 v2 重试实际上复用了原始实验的日志路径，并且运行成功了。

```json
{"root_cause":"实验实际已成功完成，Verdict=PASS，无报错。日志末尾显示正常shutdown和完整report输出。","error_type":"infrastructure","fix_steps":["无需修复，实验已成功完成","检查任务管理系统状态标记是否与实际日志不一致"],"can_auto_fix":false,"is_experiment_needed":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "实验实际已成功完成，Verdict=PASS，无报错。日志末尾显示正常shutdown和完整report输出。",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，实验已成功完成",
      "检查任务管理系统状态标记是否与实际日志不一致"
    ],
    "can_auto_fix": false,
    "is_experiment_needed": false
  }
}
```

</details>

---
