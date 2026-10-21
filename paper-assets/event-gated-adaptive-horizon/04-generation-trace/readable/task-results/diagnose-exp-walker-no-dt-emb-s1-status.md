# diagnose exp walker no dt emb s1 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_walker_no_dt_emb_s1_status_20260528T160009_result.json`
- **Structured JSON:** [`5d73c46eaeca2067a404.json`](../../sessions/5d/5d73c46eaeca2067a404.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B tool is broken. I have enough data from the server. Here's the result:

```json
{
  "actual_status": "completed",
  "final_step": 112000,
  "exit_code": "unknown (log only captured 39 lines of startup, no nohup.out)",
  "metrics": {
    "eval_return_final": 468.83,
    "eval_length": 500.0,
    "eval_episodes": 10,
    "eval_step": 105000,
    "ve_ratio": 0.2301,
    "delta_ve": -0.2915,
    "civo_alert": 0.0,
    "value_mean": 107.88,
    "gate_dt_mean": 2.0,
    "gate_dt_std": 0.0,
    "gate_dt_2_frac": 1.0,
    "gate_empirical_entropy": 0.0,
    "gate_entropy_ratio": 0.0,
    "actor_entropy": -5.05,
    "model_loss": 4.333,
    "fps": 10.01,
    "last_train_return_avg_at_112k": 426.82
  },
  "log_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_no_dt_emb_s1.log",
  "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_no_dt_emb_s1/latest.pt"
}
```

关键发现：
- **进程已结束**，无 dreamer/python 训练进程在运行。最后文件修改时间 May 27 22:24（~26 小时前）。
- **跑到 112K 步**，超过 105K 目标。最后一次 eval 在 105K 步，之后继续训练到 112K 但没有 110K 的 eval 记录，可能被系统终止或训练循环在 episode 边界自然结束。
- **无 DONE/SENTINEL 文件**，无 nohup.out，log 文件仅 39 行（启动日志）。
- **gate 完全固定在 dt=2**（gate_dt_2_frac=1.0, entropy=0.0），符合 no_dt_emb 消融预期——没有 dt embedding 时 gate 退化为常量。
- **eval_return 468.83**，train_return 在 112K 步时均值 ~427。
- Registry 中未找到匹配记录（exp_name 可能不完全匹配），需要更新 registry 状态为 COMPLETED。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "actual_status": "completed",
    "final_step": 112000,
    "exit_code": "unknown (log only captured 39 lines of startup, no nohup.out)",
    "metrics": {
      "eval_return_final": 468.83,
      "eval_length": 500.0,
      "eval_episodes": 10,
      "eval_step": 105000,
      "ve_ratio": 0.2301,
      "delta_ve": -0.2915,
      "civo_alert": 0.0,
      "value_mean": 107.88,
      "gate_dt_mean": 2.0,
      "gate_dt_std": 0.0,
      "gate_dt_2_frac": 1.0,
      "gate_empirical_entropy": 0.0,
      "gate_entropy_ratio": 0.0,
      "actor_entropy": -5.05,
      "model_loss": 4.333,
      "fps": 10.01,
      "last_train_return_avg_at_112k": 426.82
    },
    "log_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_no_dt_emb_s1.log",
    "checkpoint_path": "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_walker_no_dt_emb_s1/latest.pt"
  }
}
```

</details>

---
