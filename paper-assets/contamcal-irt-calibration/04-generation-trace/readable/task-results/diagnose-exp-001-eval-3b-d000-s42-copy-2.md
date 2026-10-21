# diagnose exp 001 eval 3B d000 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_3B_d000_s42_20260514T064711_result.json`
- **Structured JSON:** [`02426f0b926df7c0e618.json`](../../sessions/02/02426f0b926df7c0e618.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已正常完成，不是 failed。** 进程消失是因为跑完了自然退出。

关键证据：
- PID 249294 已不存在（正常退出）
- 日志最后一行 `14:39:11 [INFO] Item responses saved to ...`，四个 benchmark 全部跑完
- 输出目录有完整的 3 个结果文件：`eval_results.json` (2MB), `correctness_matrix.json` (107KB), `item_responses.json` (2.2MB)
- GPU 1 当前空闲，0MiB 占用

运行时间：08:54 → 14:39，约 5 小时 45 分钟。

部分结果摘要（从日志）：
- humaneval pass@1: **0.1159** (19/164)
- bitsandbytes 的 `libnvJitLink.so.13` 报错是非致命 warning，未影响评估

```json
{"root_cause":"N/A - 实验正常完成，进程自然退出","error_type":"N/A","fix_steps":["无需修复，将 cron 状态标记为 completed"],"can_auto_fix":true,"partial_results":"有完整结果（eval_results.json + correctness_matrix.json + item_responses.json）","process_alive":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "N/A - 实验正常完成，进程自然退出",
    "error_type": "N/A",
    "fix_steps": [
      "无需修复，将 cron 状态标记为 completed"
    ],
    "can_auto_fix": true,
    "partial_results": "有完整结果（eval_results.json + correctness_matrix.json + item_responses.json）",
    "process_alive": false
  }
}
```

</details>

---
