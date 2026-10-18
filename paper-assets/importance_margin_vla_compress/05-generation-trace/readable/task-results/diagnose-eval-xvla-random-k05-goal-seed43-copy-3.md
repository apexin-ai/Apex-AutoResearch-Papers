# diagnose eval xvla random k05 goal seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_xvla_random_k05_goal_seed43_20260523T214528_result.json`
- **Structured JSON:** [`1ae7757b6737c277efb7.json`](../../sessions/1a/1ae7757b6737c277efb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**v2 正在运行中** (PID 979864, Task 0 Ep 28/50, GPU 0)，无需修复。

```json
{"root_cause":"v1 完成 5/10 tasks 后被 kill 重启为 v2; 两次运行日志均写入 /root/autodl-tmp/.../logs/ 而非 CRON 期望的 ~/runs/...，导致 CRON 报 'log not found'; v2 当前正在运行 (Task 0 Ep 28/50, PID 979864)","error_type":"infrastructure","fix_steps":["等待 v2 运行完成（预计约 1.5-2 小时）","完成后从 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_goal_seed43_v2.log 提取最终 SR","将结果注册到 registry，替换当前可能来自 seed42 的错误 metrics (67.2%)","如果需要 CRON 兼容，未来启动时将日志写入 ~/runs/ 路径"],"can_auto_fix":false,"actual_seed43_metrics":"v1 部分结果: T0=100%, T1=94%, T2=96%, T3=68%, T4=98% (5/10 tasks); v2 正在重跑，尚无最终 SR"}
```

关键发现：
- **日志路径不匹配**：手动启动用了 `logs/` 目录，CRON 监控的是 `~/runs/` 目录
- **v1 被中途 kill**：完成 Task 0-4 后在 Task 5（全 FAIL）时终止
- **v2 正常运行中**：刚启动约 2 分钟，Task 0 进行到 Ep 28/50
- **Registry 中 67.2% 不可信**：note 已标记可能来自 seed42

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "v1 完成 5/10 tasks 后被 kill 重启为 v2; 两次运行日志均写入 /root/autodl-tmp/.../logs/ 而非 CRON 期望的 ~/runs/...，导致 CRON 报 'log not found'; v2 当前正在运行 (Task 0 Ep 28/50, PID 979864)",
    "error_type": "infrastructure",
    "fix_steps": [
      "等待 v2 运行完成（预计约 1.5-2 小时）",
      "完成后从 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_goal_seed43_v2.log 提取最终 SR",
      "将结果注册到 registry，替换当前可能来自 seed42 的错误 metrics (67.2%)",
      "如果需要 CRON 兼容，未来启动时将日志写入 ~/runs/ 路径"
    ],
    "can_auto_fix": false,
    "actual_seed43_metrics": "v1 部分结果: T0=100%, T1=94%, T2=96%, T3=68%, T4=98% (5/10 tasks); v2 正在重跑，尚无最终 SR"
  }
}
```

</details>

---
