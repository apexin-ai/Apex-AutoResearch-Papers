# ops fix eval paths urgent

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_eval_paths_urgent_20260523T203758_result.json`
- **Structured JSON:** [`279701cf8efafcefff39.json`](../../sessions/27/279701cf8efafcefff39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**问题已经被修复，两个 eval 都在正常运行。**

当前状态：

| Eval | GPU | PID | 进度 | 显存 | 日志位置 |
|------|-----|-----|------|------|---------|
| cutoff_25k_s0_eval | 3 | 463150 | T2: 60% (30/50) | 16.8 GB | `/tmp/cutoff_25k_s0_eval.log` |
| reverse_cutoff_s0_eval | 2 | 464454 | T2: 36% (18/50) | 16.8 GB | `/tmp/reverse_cutoff_s0_eval.log` |

`/root/runs/occsafe_vla/` 下的日志是之前一次失败尝试的残留（错误参数 `--num_trials_per_task`，脚本不认识）。当前运行的进程已用正确参数 `--num_rollouts 50` 重新启动，路径也是正确的 `cd /root/occsafe_vla/openvla-oft`，无需再操作。

GPU 0/1 训练任务也正常（99% 利用率，~63GB 显存）。

---
