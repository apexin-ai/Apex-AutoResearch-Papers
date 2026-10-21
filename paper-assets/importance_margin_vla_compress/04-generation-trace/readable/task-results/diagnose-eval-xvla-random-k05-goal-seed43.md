# diagnose eval xvla random k05 goal seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_xvla_random_k05_goal_seed43_20260523T212752_result.json`
- **Structured JSON:** [`d3f9325615fe95bb808e.json`](../../sessions/d3/d3f9325615fe95bb808e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。实验完成了 Task 0-4（5/10 tasks），在 Task 5 Ep 18/50 处进程被杀。

**根因**：实验直接在 SSH session 中运行（无 tmux 包裹），SSH 断连后进程收到 SIGHUP 被杀死。证据：
- 无 tmux session 对应此实验（ps aux 中无 tmux 记录）
- 无 sentinel exit 文件（未使用标准 framework 的 trap EXIT）
- 日志无 Traceback/OOM/CUDA 错误，进程突然消失
- GPU 1 完全空闲（1MiB），磁盘空间充足（52G可用）
- 同服务器的 `object_seed43` 实验仍在 pts/1 上存活

已完成的中间结果：Task 0: 100%, Task 1: 94%, Task 2: 96%, Task 3: 68%, Task 4: 98%

```json
{"root_cause":"SSH session断连导致SIGHUP杀死进程——实验未在tmux中运行，日志在Task 5 Ep 18/50处中断，无Traceback/OOM/CUDA错误","error_type":"infrastructure","fix_steps":["用tmux包裹重新启动实验：tmux new-session -d -s eval_xvla_random_k05_goal_seed43","使用CUDA_VISIBLE_DEVICES=1（GPU 1当前空闲）重跑完整实验","或实现断点续跑：从domain_id 5（Task 5）开始，合并已完成的Task 0-4结果"],"can_auto_fix":true,"log_path":"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_goal_seed43.log"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "SSH session断连导致SIGHUP杀死进程——实验未在tmux中运行，日志在Task 5 Ep 18/50处中断，无Traceback/OOM/CUDA错误",
    "error_type": "infrastructure",
    "fix_steps": [
      "用tmux包裹重新启动实验：tmux new-session -d -s eval_xvla_random_k05_goal_seed43",
      "使用CUDA_VISIBLE_DEVICES=1（GPU 1当前空闲）重跑完整实验",
      "或实现断点续跑：从domain_id 5（Task 5）开始，合并已完成的Task 0-4结果"
    ],
    "can_auto_fix": true,
    "log_path": "/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_random_k05_goal_seed43.log"
  }
}
```

</details>

---
