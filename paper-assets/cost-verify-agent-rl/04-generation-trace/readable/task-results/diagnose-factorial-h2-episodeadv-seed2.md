# diagnose factorial h2 episodeadv seed2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_factorial_h2_episodeadv_seed2_20260518T105417_result.json`
- **Structured JSON:** [`4a3dc06d0d1efa816d14.json`](../../sessions/4a/4a3dc06d0d1efa816d14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0,1 已空闲。`factorial_seed2` tmux session 已销毁。gsweep 在 GPU 2,3 上正常运行。

---

## 诊断结论

**注意：诊断过程中我发的 `kill -USR1 546362` 杀死了最新的运行实例。该进程当时实际在正常运行 val_before_train 评估阶段。需要重启。**

### 根因分析

**不是代码 bug，不是 OOM，不是 GPU 错误。** 根本原因是 **监控系统误判 + stdout 缓冲**：

1. **`val_before_train: True`** 在训练前执行 134 个 OOD ALFWorld 游戏的评估。每个游戏最多 50 turns，`parallel_friendly=False, max_workers=1` 顺序执行。这个阶段耗时 15-20+ 分钟。
2. **Python stdout 缓冲**：输出重定向到文件时使用 full buffering，评估期间零输出写入日志。
3. **监控系统检测不到生命信号**：无 W&B metrics（第一个训练 step 未开始），无 sentinel 输出 → 5 次声明 "process dead"。
4. **Ray cluster 共享**：seed2 连接到 gsweep 的 Ray cluster（`session_2026-05-18_17-14-56`），而 seed1 启动了**自己的 Ray 实例**。共享集群增加了连接中断风险。

### 对比证据

| | seed1 | seed2 |
|---|---|---|
| Ray cluster | 独立（"Started a local Ray instance"） | 共享 gsweep 的 |
| val_before_train 输出 | 有（line 1656-6431 大量 warnings） | 被缓冲，无输出 |
| 进入训练 | 成功，line 6484 | 从未到达 |

### 最新实例（PID 546362）被 flush 的缓冲输出

```
(WorkerDict pid=546976) NCCL version 2.27.5+cuda12.9
(TaskRunner pid=546362) Initializing AlfredTWEnv...
(TaskRunner pid=546362) Overall we have 3553 games in split=train
(TaskRunner pid=546362) Training with 3553 games
(TaskRunner pid=546362) Initializing AlfredTWEnv...
(TaskRunner pid=546362) Overall we have 134 games in split=eval_out_of_distribution
(TaskRunner pid=546362) Evaluating with 134 games   ← 进程在此正常运行，被 SIGUSR1 杀死
```

```json
{"root_cause":"val_before_train=True 触发 134 游戏的初始评估（顺序执行，15-20min+），期间 Python stdout 完全缓冲无输出、无 W&B metrics，监控系统误判为 dead。seed2 共享 gsweep 的 Ray cluster（seed1 用独立 Ray instance），增加连接不稳定风险。最新实例 PID 546362 被诊断中的 kill -USR1 意外杀死。","error_type":"infrastructure","fix_steps":["重启时加 PYTHONUNBUFFERED=1 确保实时输出","重启前先 ray stop 清理 gsweep 的 Ray session，让 seed2 启动自己的 Ray cluster（或用 RAY_ADDRESS=local 强制新集群）","监控系统对此实验类型增加超时（至少 30 分钟）","GPU 0,1 已空闲可直接重启"],"can_auto_fix":true,"wandb_runs_found":["6rqnrlr7"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "val_before_train=True 触发 134 游戏的初始评估（顺序执行，15-20min+），期间 Python stdout 完全缓冲无输出、无 W&B metrics，监控系统误判为 dead。seed2 共享 gsweep 的 Ray cluster（seed1 用独立 Ray instance），增加连接不稳定风险。最新实例 PID 546362 被诊断中的 kill -USR1 意外杀死。",
    "error_type": "infrastructure",
    "fix_steps": [
      "重启时加 PYTHONUNBUFFERED=1 确保实时输出",
      "重启前先 ray stop 清理 gsweep 的 Ray session，让 seed2 启动自己的 Ray cluster（或用 RAY_ADDRESS=local 强制新集群）",
      "监控系统对此实验类型增加超时（至少 30 分钟）",
      "GPU 0,1 已空闲可直接重启"
    ],
    "can_auto_fix": true,
    "wandb_runs_found": [
      "6rqnrlr7"
    ]
  }
}
```

</details>

---
