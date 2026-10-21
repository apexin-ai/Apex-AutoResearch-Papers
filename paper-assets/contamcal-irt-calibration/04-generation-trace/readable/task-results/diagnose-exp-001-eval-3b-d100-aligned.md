# diagnose exp 001 eval 3B d100 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_3B_d100_aligned_20260514T153510_result.json`
- **Structured JSON:** [`474e0ef44de9d7e58566.json`](../../sessions/47/474e0ef44de9d7e58566.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。实验**未失败**，是 cron 误报。

```json
{"root_cause":"Cron false positive — wrapper PID 362942 已退出但实际 python eval 进程继续运行并于 23:22:32 正常完成。日志末行: '[Thu May 14 23:22:32 CST 2026] 3B d100 aligned eval DONE.'","error_type":"infrastructure","fix_steps":["无需修复，实验已成功完成","建议修复 cron 监控逻辑：检测 GPU 进程而非 wrapper PID"],"can_auto_fix":false,"partial_results":"全部完成。MMLU=0.6417 (9011/14042), GSM8K=0.6967 (919/1319), ARC_Challenge=0.8396 (984/1172), HumanEval pass@1=0.1220 (20/164)。结果已保存至 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned/"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Cron false positive — wrapper PID 362942 已退出但实际 python eval 进程继续运行并于 23:22:32 正常完成。日志末行: '[Thu May 14 23:22:32 CST 2026] 3B d100 aligned eval DONE.'",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，实验已成功完成",
      "建议修复 cron 监控逻辑：检测 GPU 进程而非 wrapper PID"
    ],
    "can_auto_fix": false,
    "partial_results": "全部完成。MMLU=0.6417 (9011/14042), GSM8K=0.6967 (919/1319), ARC_Challenge=0.8396 (984/1172), HumanEval pass@1=0.1220 (20/164)。结果已保存至 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned/"
  }
}
```

</details>

---
