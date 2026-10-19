# diagnose exp 003 training health

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-003-training-health_20260521T101552_result.json`
- **Structured JSON:** [`0ae13e69a2540cecf72a.json`](../../sessions/0a/0ae13e69a2540cecf72a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。结果如下：

```json
{
  "exp003_alive": false,
  "last_step": 8000,
  "last_timestamp": "2026-05-21T18:12:00+08:00",
  "exp003_s2_alive": true,
  "issue": "exp-003 (seed 1) 已正常完成全部 8000 步训练，进程自然退出，不是崩溃。checkpoint-8000 和 final 目录均已于 18:12 写入。Cron 误判为异常是因为进程完成后消失但没有 sentinel 文件（exp-003 未通过 agent-ml 框架启动，所以无 sentinel/log 记录）。exp-003-s2 (seed 2) 健康运行中，当前 step 3905/8000 (49%)，GPU 0 利用率 95%，预计约 29 小时后完成。",
  "action_needed": "none"
}
```

**要点：**
- **exp-003 seed 1**：训练已完成，8000/8000 步，checkpoint 完整（500-8000 每 500 步 + final）。Cron 报警是误报——进程正常结束，非崩溃。
- **exp-003-s2 seed 2**：健康，step 3905/8000，~27s/step，ETA 约 29 小时（5月22日 23:00 左右），DDL 前可完成。
- **建议**：在 cron 监控中将 exp-003 标记为已完成，避免继续报警。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp003_alive": false,
    "last_step": 8000,
    "last_timestamp": "2026-05-21T18:12:00+08:00",
    "exp003_s2_alive": true,
    "issue": "exp-003 (seed 1) 已正常完成全部 8000 步训练，进程自然退出，不是崩溃。checkpoint-8000 和 final 目录均已于 18:12 写入。Cron 误判为异常是因为进程完成后消失但没有 sentinel 文件（exp-003 未通过 agent-ml 框架启动，所以无 sentinel/log 记录）。exp-003-s2 (seed 2) 健康运行中，当前 step 3905/8000 (49%)，GPU 0 利用率 95%，预计约 29 小时后完成。",
    "action_needed": "none"
  }
}
```

</details>

---
