# diagnose repo level cls home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_repo-level-cls-home_20260512T211653_result.json`
- **Structured JSON:** [`3141b01c4608a91f8dc0.json`](../../sessions/31/3141b01c4608a91f8dc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有足够信息做诊断了。

关键发现：

1. **旧运行日志已被覆盖** — 新运行（PID 2880203）在旧运行退出 12 秒后自动启动（21:14:26 UTC），覆盖了同名日志文件
2. **EXIT_CODE=130 = SIGINT** — 外部信号终止，不是 OOM（137）、不是代码错误（1）、不是段错误（139）
3. **新运行正在正常训练** — GPU 100% 利用率，19.4/32.6 GB 显存，step 2/6633，7.2s/step
4. **Checkpoint 目录为空** — 旧运行未达到 save_steps=200 就被杀掉
5. **代码已修复** — eval_strategy="steps"、save_steps=200（D036 的 epoch 问题已修）
6. **无其他干扰进程** — CWM v8 在 seetacloud 上，不在 home

```json
{"root_cause":"EXIT_CODE=130 (SIGINT) — 进程被外部信号终止，旧日志已被自动重启的新运行覆盖无法追溯具体触发源。最可能是 Worker 框架在 D037 策略调整中主动 kill-and-restart","error_type":"infrastructure","fix_steps":["无需修复 — 新运行(PID 2880203)已自动启动并正常训练中(step 2/6633, 7.2s/step)","注册表中 repo-level-cls-home 状态仍为 DONE，需更新为 RUNNING 并绑定新 PID","建议后续日志写入带时间戳的文件名避免覆盖(如 repo-level-cls-home.20260512T211426.log)"],"can_auto_fix":true,"checkpoints_saved":false,"checkpoint_path":null}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "EXIT_CODE=130 (SIGINT) — 进程被外部信号终止，旧日志已被自动重启的新运行覆盖无法追溯具体触发源。最可能是 Worker 框架在 D037 策略调整中主动 kill-and-restart",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复 — 新运行(PID 2880203)已自动启动并正常训练中(step 2/6633, 7.2s/step)",
      "注册表中 repo-level-cls-home 状态仍为 DONE，需更新为 RUNNING 并绑定新 PID",
      "建议后续日志写入带时间戳的文件名避免覆盖(如 repo-level-cls-home.20260512T211426.log)"
    ],
    "can_auto_fix": true,
    "checkpoints_saved": false,
    "checkpoint_path": null
  }
}
```

</details>

---
