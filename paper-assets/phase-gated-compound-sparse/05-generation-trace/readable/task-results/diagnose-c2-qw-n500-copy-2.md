# diagnose c2 qw n500

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_c2_qw_n500_20260514T141557_result.json`
- **Structured JSON:** [`55588b0b63b9df9ddaf5.json`](../../sessions/55/55588b0b63b9df9ddaf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the diagnosis:

```json
{
  "alive": true,
  "gpu2_pid": "131864",
  "gpu3_pid": "132002",
  "gpu2_progress": "49/500 qw_imp_s015",
  "gpu3_progress": "48/500 qw_rand_s015",
  "completed_conditions": [],
  "tmux_sessions": ["c2_n500_gpu0", "c2_n500_gpu1"],
  "estimated_remaining_hours": 3.8,
  "root_cause": "cron false positive: profiling task has no W&B/sentinel, output written at end not incrementally (dirs empty at 49/500)"
}
```

补充细节：
- **4 个进程均存活**：GPU 0/1 跑 DeepSeek (PID 130124/130263)，GPU 2/3 跑 Qwen (PID 131864/132002)
- **日志仍在更新**：最新条目 22:16:51，进度 ~49/500
- **输出目录为空**：profiling 结果在全部 500 题跑完后才写盘，不是增量写入
- **速率**：~0.5 min/problem → 剩余 451 题约 3.8 小时（预计 ~02:00 CST 完成）
- **s020 条件未启动**：当前只跑 s015，s020 的日志是之前被杀掉的重复进程残留

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "alive": true,
    "gpu2_pid": "131864",
    "gpu3_pid": "132002",
    "gpu2_progress": "49/500 qw_imp_s015",
    "gpu3_progress": "48/500 qw_rand_s015",
    "completed_conditions": [],
    "tmux_sessions": [
      "c2_n500_gpu0",
      "c2_n500_gpu1"
    ],
    "estimated_remaining_hours": 3.8,
    "root_cause": "cron false positive: profiling task has no W&B/sentinel, output written at end not incrementally (dirs empty at 49/500)"
  }
}
```

</details>

---
