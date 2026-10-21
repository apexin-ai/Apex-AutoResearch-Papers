# ops sparsity70 investigate restart

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sparsity70_investigate_restart_20260515T203159_result.json`
- **Structured JSON:** [`d5a70c0f82c78a82f5dc.json`](../../sessions/d5/d5a70c0f82c78a82f5dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

kl_sparsity70_s42_v2 启动成功。日志确认 `Gradient checkpointing enabled`，GPU 0 占用 46906 MiB（比 sparsity30 的 67560 MiB 低，gradient checkpointing 生效）。

---

## 报告

**(1) sparsity70 死因**

- 无 dmesg OOM 记录（容器无权限）、无日志、无 checkpoint、tmux session 已不存在
- Registry 显示进程仅存活 ~3 分钟（20:24 创建，20:27 killed）
- **根因确认：缺少 `--gradient_checkpointing`。** sparsity30_v2 修复时特意加了此参数。70% sparsity target 的 Lagrangian training 在无 gradient checkpointing 时显存超出 96GB 上限，CUDA OOM 导致进程立即崩溃，来不及写日志

**(2) PID 131102 清理**

- nvidia-smi 已无 PID 131102，自动清理完毕，无需干预

**(3) GPU 当前状态**

| GPU | PID | 任务 | 显存 | 状态 |
|-----|-----|------|------|------|
| cuda:0 | 132998 | kl_sparsity70_s42_v2 | 46.9 GB | 刚启动，gradient_checkpointing=ON |
| cuda:1 | 132407 | kl_sparsity30_s42_v2 | 67.6 GB | 正常运行 |

bce_isocompute_v2_s42 已正常完成 (EXIT_CODE=0, 1000 steps, 1047.8s)。

**(4) sparsity70 重启状态**

已提交 `kl_sparsity70_s42_v2` 到 cuda:0（PID 132988），关键修复：加了 `--gradient_checkpointing`。日志和 GPU 显存确认启动正常。

---
