# diagnose eval obs only object norm003 seed45 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm003-seed45-r2_20260519T044722_result.json`
- **Structured JSON:** [`e467d8c4cb5f40fe1c88.json`](../../sessions/e4/e467d8c4cb5f40fe1c88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。两个实验日志都在 task 6/10 (tomato_sauce) 的中间突然截断，无 Traceback、无 Error、无 OOM，同一时刻停止写入（12:30 server time）。tmux sessions 已不存在，GPU 已被新进程占用。

```json
{"root_cause":"两个进程在同一时刻被 SIGTERM 杀死（seed45 停在 task6 rollout 5/10, seed43 停在 task6 rollout 7/10），日志无 traceback/error 直接截断，tmux sessions 被销毁，GPU 1/3 已被新实验进程占用。与已知调度系统抢占行为一致（批量杀旧进程腾 GPU）。dmesg 无 OOM 记录。实际日志路径在 /root/logs/（非 /root/autodl-tmp/...），因 tmux 从 /root/ 启动且 output_file 用了相对路径。","error_type":"preemption","fix_steps":["在 bjb1-18228 或其他可用服务器上重新提交 r3：seed45 cuda:3 + seed43 cuda:1，确保 tmux 从项目目录启动（cd /root/acr-vla-conformal-refinement 后再 tmux new-session）使日志写入正确位置","或使用绝对路径 --output_file /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed{45,43}.json"],"can_auto_fix":true,"affects_both":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "两个进程在同一时刻被 SIGTERM 杀死（seed45 停在 task6 rollout 5/10, seed43 停在 task6 rollout 7/10），日志无 traceback/error 直接截断，tmux sessions 被销毁，GPU 1/3 已被新实验进程占用。与已知调度系统抢占行为一致（批量杀旧进程腾 GPU）。dmesg 无 OOM 记录。实际日志路径在 /root/logs/（非 /root/autodl-tmp/...），因 tmux 从 /root/ 启动且 output_file 用了相对路径。",
    "error_type": "preemption",
    "fix_steps": [
      "在 bjb1-18228 或其他可用服务器上重新提交 r3：seed45 cuda:3 + seed43 cuda:1，确保 tmux 从项目目录启动（cd /root/acr-vla-conformal-refinement 后再 tmux new-session）使日志写入正确位置",
      "或使用绝对路径 --output_file /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed{45,43}.json"
    ],
    "can_auto_fix": true,
    "affects_both": true
  }
}
```

</details>

---
