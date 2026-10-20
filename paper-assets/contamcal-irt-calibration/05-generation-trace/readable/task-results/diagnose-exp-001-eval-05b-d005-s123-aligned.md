# diagnose exp 001 eval 05B d005 s123 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_05B_d005_s123_aligned_20260515T031807_result.json`
- **Structured JSON:** [`a396c99f362537fa2575.json`](../../sessions/a3/a396c99f362537fa2575.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 JSON 都正常闭合。两个实验实际上都已**成功完成**，但被监控系统误判。

```json
{
  "exp_001_eval_05B_d005_s123_aligned": {
    "root_cause": "监控误判（false positive）。实验已于 2026-05-15 11:04:22 成功完成全部 4 个 benchmark，结果已保存。进程正常退出后被 cron 检测为 'process dead'，因无 sentinel 文件或 W&B 日志，连续 5 次检测判定为 failed。缺少 `source /etc/network_turbo` 未导致实际失败（数据可能已缓存）。",
    "error_type": "infrastructure",
    "partial_results": "完整结果：mmlu=0.3002, gsm8k=0.3677, arc_challenge=0.2978, humaneval_pass@1=0.0976。输出目录含 eval_results.json / correctness_matrix.json / item_responses.json / eval.log 共 4 个文件。",
    "fix_steps": [
      "将实验状态从 failed 改为 succeeded",
      "无需重跑"
    ],
    "can_auto_fix": true
  },
  "exp_001_eval_15B_d100_s123_aligned": {
    "status": "dead",
    "root_cause": "同实验 1——进程已正常完成全部 4 个 benchmark 后退出，被监控误判为异常退出。GPU 2 当前 0 MiB 显存占用，无残留进程。输出目录缺少 eval.log（可能是脚本版本差异或 stdout 未重定向），但 eval_results.json 完整且 JSON 结构正常闭合。",
    "partial_results": "完整结果：mmlu=0.5956, gsm8k=0.6444, arc_challenge=0.7816, humaneval_pass@1=0.2805。输出目录含 eval_results.json / correctness_matrix.json / item_responses.json 共 3 个文件。",
    "fix_steps": [
      "将实验状态从 RUNNING 改为 succeeded"
    ]
  }
}
```

**总结**：两个实验都已成功完成，产出了全部 4 个 benchmark 的完整结果。监控系统因缺少 sentinel/W&B 信号，在进程正常退出后误判为失败/异常。直接标记为 succeeded 即可，无需重跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp_001_eval_05B_d005_s123_aligned": {
      "root_cause": "监控误判（false positive）。实验已于 2026-05-15 11:04:22 成功完成全部 4 个 benchmark，结果已保存。进程正常退出后被 cron 检测为 'process dead'，因无 sentinel 文件或 W&B 日志，连续 5 次检测判定为 failed。缺少 `source /etc/network_turbo` 未导致实际失败（数据可能已缓存）。",
      "error_type": "infrastructure",
      "partial_results": "完整结果：mmlu=0.3002, gsm8k=0.3677, arc_challenge=0.2978, humaneval_pass@1=0.0976。输出目录含 eval_results.json / correctness_matrix.json / item_responses.json / eval.log 共 4 个文件。",
      "fix_steps": [
        "将实验状态从 failed 改为 succeeded",
        "无需重跑"
      ],
      "can_auto_fix": true
    },
    "exp_001_eval_15B_d100_s123_aligned": {
      "status": "dead",
      "root_cause": "同实验 1——进程已正常完成全部 4 个 benchmark 后退出，被监控误判为异常退出。GPU 2 当前 0 MiB 显存占用，无残留进程。输出目录缺少 eval.log（可能是脚本版本差异或 stdout 未重定向），但 eval_results.json 完整且 JSON 结构正常闭合。",
      "partial_results": "完整结果：mmlu=0.5956, gsm8k=0.6444, arc_challenge=0.7816, humaneval_pass@1=0.2805。输出目录含 eval_results.json / correctness_matrix.json / item_responses.json 共 3 个文件。",
      "fix_steps": [
        "将实验状态从 RUNNING 改为 succeeded"
      ]
    }
  }
}
```

</details>

---
