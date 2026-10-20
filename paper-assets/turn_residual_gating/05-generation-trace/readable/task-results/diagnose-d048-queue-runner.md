# diagnose d048 queue runner

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d048_queue_runner_20260522T234435_result.json`
- **Structured JSON:** [`9bf0f8cbf9609a397d95.json`](../../sessions/9b/9bf0f8cbf9609a397d95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程没有失败——仍在运行。** Cron 报的是误报。

```json
{
  "root_cause": "进程未退出。tmux session 'queue_runner' (PID 50719) 存活，当前 PID 51492 正在执行 UG s42 AR N=50 eval (β=3.0, Conv 20/50)。Cron 报 'Process exited without valid W&B metrics' 是误报——eval 脚本不使用 W&B，且进程仍在运行。",
  "error_type": "infrastructure",
  "fix_steps": [
    "无需修复，进程正常运行中",
    "Cron 监控需要适配 eval-only 任务：不应以 W&B metrics 作为成功判据",
    "可用 'tail -f runs/queue_runner.log' 或 'tmux attach -t queue_runner' 跟踪进度"
  ],
  "can_auto_fix": false,
  "completed_betas": ["TG s42: β=0.0, 3.0, 5.0 (N=50, done)", "UG s42: β=0.0 (N=50, done), β=3.0 in progress Conv 20/50"],
  "remaining_betas": ["UG s42: β=3.0 (Conv 21-50), β=5.0", "LO s42: β=0.0", "PCGrad s42: β=0.0, 3.0, 5.0"],
  "remaining_queue_items": ["[3/8] SS s123 train+eval", "[4/8] SS s456 train+eval", "[5/8] Base s123 train+eval", "[6/8] Base s456 train+eval", "[7/8] TG s123 train+eval", "[8/8] TG s456 train+eval"],
  "results_paths": ["results/d048_ar_n50_existing/tg_s42_ar_n50.json"]
}
```

**状态**: 队列 [2/8] 的子任务 [2/4]，UG s42 β=3.0 第 20/50 个对话。GPU 占用 22GB/98GB，CPU 101%，磁盘 55%。一切正常，只是跑得慢（每个 checkpoint × 3β × 50 convs）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "进程未退出。tmux session 'queue_runner' (PID 50719) 存活，当前 PID 51492 正在执行 UG s42 AR N=50 eval (β=3.0, Conv 20/50)。Cron 报 'Process exited without valid W&B metrics' 是误报——eval 脚本不使用 W&B，且进程仍在运行。",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，进程正常运行中",
      "Cron 监控需要适配 eval-only 任务：不应以 W&B metrics 作为成功判据",
      "可用 'tail -f runs/queue_runner.log' 或 'tmux attach -t queue_runner' 跟踪进度"
    ],
    "can_auto_fix": false,
    "completed_betas": [
      "TG s42: β=0.0, 3.0, 5.0 (N=50, done)",
      "UG s42: β=0.0 (N=50, done), β=3.0 in progress Conv 20/50"
    ],
    "remaining_betas": [
      "UG s42: β=3.0 (Conv 21-50), β=5.0",
      "LO s42: β=0.0",
      "PCGrad s42: β=0.0, 3.0, 5.0"
    ],
    "remaining_queue_items": [
      "[3/8] SS s123 train+eval",
      "[4/8] SS s456 train+eval",
      "[5/8] Base s123 train+eval",
      "[6/8] Base s456 train+eval",
      "[7/8] TG s123 train+eval",
      "[8/8] TG s456 train+eval"
    ],
    "results_paths": [
      "results/d048_ar_n50_existing/tg_s42_ar_n50.json"
    ]
  }
}
```

</details>

---
