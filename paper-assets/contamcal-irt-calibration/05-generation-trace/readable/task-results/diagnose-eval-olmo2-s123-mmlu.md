# diagnose eval olmo2 s123 mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_olmo2_s123_mmlu_20260520T114029_result.json`
- **Structured JSON:** [`a5f3f374273521427636.json`](../../sessions/a5/a5f3f374273521427636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：

```json
{"root_cause":"误报——实验仍在运行。PID 331086(bash)状态S, PID 333043(python eval d005_s123)状态Rl/CPU=160%/elapsed=6min, 进度9694/14042(69%)。日志因progress bar \\r覆写导致tail看到旧进度(57%)而误判为截断。d000已完成(exit=0), d005正在跑, d025/d050/d100排队中。","error_type":"none","fix_steps":["无需修复，等待完成即可。预计d005还需~3min，全部5个dosage约需再30-40min。","可用 tail -f /tmp/eval_olmo2_s123_mmlu.log 实时监控"],"can_auto_fix":false,"gpu_conflict":false}
```

**要点**：
- PID 331086 **未死**（状态 S，sleeping 等子进程）
- PID 333043 是 d005_s123 的 Python 进程，160% CPU，已跑 6 分钟，当前进度 69%（9694/14042）
- d000_s123 已完成（exit=0），d005 正在跑，d025/d050/d100 还在排队
- 日志 `tail` 看到 57% 是因为 tqdm 用 `\r` 覆写行，实际进度已到 69%
- cuda:2 当前仅占用 16.7GB，无冲突

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "误报——实验仍在运行。PID 331086(bash)状态S, PID 333043(python eval d005_s123)状态Rl/CPU=160%/elapsed=6min, 进度9694/14042(69%)。日志因progress bar \\r覆写导致tail看到旧进度(57%)而误判为截断。d000已完成(exit=0), d005正在跑, d025/d050/d100排队中。",
    "error_type": "none",
    "fix_steps": [
      "无需修复，等待完成即可。预计d005还需~3min，全部5个dosage约需再30-40min。",
      "可用 tail -f /tmp/eval_olmo2_s123_mmlu.log 实时监控"
    ],
    "can_auto_fix": false,
    "gpu_conflict": false
  }
}
```

</details>

---
