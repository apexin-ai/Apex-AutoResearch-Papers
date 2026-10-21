# diagnose eval mbpp grpo rasp 20 death

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_mbpp_grpo_rasp_20_death_20260519T183517_result.json`
- **Structured JSON:** [`61527c28fd17b712e4e5.json`](../../sessions/61/61527c28fd17b712e4e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Run C 存活，GPU 1 现在 97% 利用率，15/374 运行中。诊断完成。

```json
{
  "root_cause": "kill_job 外部终止。Run B（PID 127000）通过 ssh_execute 启动（非 tmux 保护），写日志到 /tmp/。在 Run A（框架提交）于 02:24:04 以 EXIT_CODE=129（SIGHUP，tmux session 被杀）死亡后，agent 检测到失败，对 PID 127000 调用 kill_job（发送 SIGTERM），然后于 02:33:01 重新提交 Run C（当前存活，15/374）。",
  "evidence": [
    "1. 存在三个独立运行：Run A（~/runs/ log, born 02:21:21, died 02:24:04, EXIT_CODE=129）、Run B（/tmp/ log, born 02:22:47, died 02:32:09, 8/374 无 traceback）、Run C（autodl-tmp/logs/, born 02:33:01, 当前 15/374 存活）",
    "2. Exit file 内容 129|2026-05-19T18:24:04Z 属于 Run A（框架 tmux wrapper 写入），不是 Run B",
    "3. Run B 日志路径为 /tmp/（非框架标准路径 ~/runs/），无 EXIT_CODE 行 → 非 tmux wrapper 启动",
    "4. Run B 死亡无 Python traceback → 外部信号杀死（SIGTERM 默认不打 traceback）",
    "5. Run B 死亡（02:32:09）到 Run C 启动（02:33:01）间隔 52 秒 → agent kill 后立即 resubmit",
    "6. 系统 RAM 1TB / 630GB free → 排除系统 OOM",
    "7. GPU 内存 97GB → 排除 GPU OOM（7B 模型约 14GB）",
    "8. 无 crontab → 排除 cron 清理脚本",
    "9. 附带发现：eval_mbpp_grpo_cka_only_20 死于 Errno 28: No space left on device（autodl-tmp 曾满，现 80%）"
  ],
  "cron_involvement": false,
  "oom_involvement": false,
  "recommendation": "Run C（第三次尝试）已在运行中，GPU 1 利用率 97%，当前 15/374。无需重试。需要关注：1) eval_mbpp_grpo_cka_only_20 因磁盘满失败，需在空间充足后重新提交；2) 未来避免用 ssh_execute 启动长时间任务，必须通过 submit_training_job（tmux 保护）。"
}
```

**补充状态：其他 MBPP eval 健康检查**

| 实验 | 状态 | 进度 |
|------|------|------|
| eval_mbpp_dense_unpruned | **完成** | 374/374, pass@1=0.5348 |
| eval_mbpp_grpo_rasp_20 (Run C) | **运行中** | 15/374 |
| eval_mbpp_grpo_standard_20 | **运行中** | 182/374 |
| eval_mbpp_sft_standard_20 | **运行中** | 46/374 |
| eval_mbpp_sft_cka_only_20 | **运行中** | 191/374 |
| eval_mbpp_grpo_cka_only_20 | **失败** | 374/374 完成但写结果时磁盘满 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "kill_job 外部终止。Run B（PID 127000）通过 ssh_execute 启动（非 tmux 保护），写日志到 /tmp/。在 Run A（框架提交）于 02:24:04 以 EXIT_CODE=129（SIGHUP，tmux session 被杀）死亡后，agent 检测到失败，对 PID 127000 调用 kill_job（发送 SIGTERM），然后于 02:33:01 重新提交 Run C（当前存活，15/374）。",
    "evidence": [
      "1. 存在三个独立运行：Run A（~/runs/ log, born 02:21:21, died 02:24:04, EXIT_CODE=129）、Run B（/tmp/ log, born 02:22:47, died 02:32:09, 8/374 无 traceback）、Run C（autodl-tmp/logs/, born 02:33:01, 当前 15/374 存活）",
      "2. Exit file 内容 129|2026-05-19T18:24:04Z 属于 Run A（框架 tmux wrapper 写入），不是 Run B",
      "3. Run B 日志路径为 /tmp/（非框架标准路径 ~/runs/），无 EXIT_CODE 行 → 非 tmux wrapper 启动",
      "4. Run B 死亡无 Python traceback → 外部信号杀死（SIGTERM 默认不打 traceback）",
      "5. Run B 死亡（02:32:09）到 Run C 启动（02:33:01）间隔 52 秒 → agent kill 后立即 resubmit",
      "6. 系统 RAM 1TB / 630GB free → 排除系统 OOM",
      "7. GPU 内存 97GB → 排除 GPU OOM（7B 模型约 14GB）",
      "8. 无 crontab → 排除 cron 清理脚本",
      "9. 附带发现：eval_mbpp_grpo_cka_only_20 死于 Errno 28: No space left on device（autodl-tmp 曾满，现 80%）"
    ],
    "cron_involvement": false,
    "oom_involvement": false,
    "recommendation": "Run C（第三次尝试）已在运行中，GPU 1 利用率 97%，当前 15/374。无需重试。需要关注：1) eval_mbpp_grpo_cka_only_20 因磁盘满失败，需在空间充足后重新提交；2) 未来避免用 ssh_execute 启动长时间任务，必须通过 submit_training_job（tmux 保护）。"
  }
}
```

</details>

---
