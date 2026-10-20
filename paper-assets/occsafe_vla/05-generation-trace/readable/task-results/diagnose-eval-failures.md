# diagnose eval failures

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_failures_20260523T204644_result.json`
- **Structured JSON:** [`ac81de863b6386be9152.json`](../../sessions/ac/ac81de863b6386be9152.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因
提交命令使用了 **`--num_trials_per_task 50`**，但 `evaluate_safelibero.py` 不支持此参数。正确参数名是 **`--num_rollouts 50`**。

Python argparse 对未识别参数返回 exit code 2 — 这不是 shell 语法错误，而是 argparse 的标准行为。

### 两个实验相同原因
`~/runs/occsafe_vla/` 下两个 log 均显示：
```
evaluate_safelibero.py: error: unrecognized arguments: --num_trials_per_task 50
```

### 后续重试也失败
`/tmp/` 下的 log 显示有人用正确参数重试过（04:44 启动），两个 eval 正常跑到 T0:62%/T0:82%，但在 04:48:43-04:48:44 同时停止（<1s 间隔）。原因可能是 tmux session 被 kill 或 GPU 被抢占。

### Checkpoint 状态
两个 checkpoint 均存在且完整，可直接重跑。

### 修复命令
memory.md 中已记录的正确 eval 命令可直接使用（`--num_rollouts 50`，GPU 2/3）。

---
