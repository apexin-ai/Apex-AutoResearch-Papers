# diagnose cqa1 gpu state and restart baseline

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_gpu_state_and_restart_baseline_20260527T060137_result.json`
- **Structured JSON:** [`7c21c177f9a6014f9045.json`](../../sessions/7c/7c21c177f9a6014f9045.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015 GPU 状态汇报

### 当前 GPU 占用

| GPU | 实验 | PID | 进度 | ETA |
|-----|------|-----|------|-----|
| 0 | `eval_openvla_random_k095_goal_seed42_v2` | 896333 | T7/10 (6 tasks done) | ~1.5-2h |
| 1 | `eval_openvla_attn_k095_goal_seed42_v2` | 11249 | T1/10 ep20/50 | ~5-6h |
| 2 | `eval_pi05_attn_k095_long_seed42_strict` | 938642 | T5/10 ep20/50, 88.4% avg | ~3h |
| 3 | `eval_openvla_attn_k05_goal_seed42_v3` | 897100 | T5/10 (4 tasks done) | ~3h |

### Baseline 重启

**无需手动重启。** `eval_pi05_baseline_goal_seed42_strict` 已有一个 tmux session (PID 17831) 在 GPU 0 上轮询等待：
```
[Wed May 27 13:47:24 CST 2026] Waiting for GPU 0 to be free...
```
每 60s 检查一次。GPU 0 的 random k=0.95 约 1.5-2h 后完成，baseline 将自动启动。baseline 本身运行约 2h，预计总完成时间 ~3.5-4h（约 UTC 10:00-10:30，北京时间 18:00-18:30），在 C002 截止时间前。

### Registry 修复

- **`eval_openvla_attn_k095_goal_seed42_v2`**: 已从 PENDING → QUEUED → RUNNING，PID=11249，GPU 1。
- **旧实验 (PID 790017, 732826)**: 均已完成，registry 已有 DONE 条目（`eval_pi05_l2norm_k085_long_seed42_v4` 和 `eval_pi05_random_k07_long_seed42`）。

### eval_openvla_l2norm_k095_object_seed42

**未在 cqa1 上运行。** Registry 显示 RUNNING 但进程已死。`/tmp/l2norm_k095_object.log` 只有启动记录（T1 刚开始就中断）。第一次运行已成功完成（SR=70.6%，metrics 在 `extra.previous_failure` 中），retry 进程未获 GPU 分配即死亡。此条目为过期 RUNNING 状态。

---
