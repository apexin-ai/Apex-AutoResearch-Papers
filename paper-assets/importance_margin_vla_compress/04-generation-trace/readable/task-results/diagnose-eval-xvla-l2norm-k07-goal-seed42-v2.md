# diagnose eval xvla l2norm k07 goal seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_xvla_l2norm_k07_goal_seed42_v2_20260523T201723_result.json`
- **Structured JSON:** [`16e6f7dc1fec885d168b.json`](../../sessions/16/16e6f7dc1fec885d168b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**失败根因：SIGHUP — tmux session 被终止**

日志最后一行显示 `Terminated` 后紧接 `EXIT_CODE=129`。该实验的 tmux session 已不存在（ps aux 中无对应进程），而同服务器上其他 tmux session（如 `eval_xvla_l2norm_k05_spatial_seed42_v3`）仍然存活。说明是这个特定 session 被 kill 掉了，不是 OOM 也不是 tmux server 崩溃。日志中无任何 OOM/segfault 痕迹。

**完成进度**：
- Task 1: 45/50 = **90.0%** ✓
- Task 2: 36/50 = **72.0%** ✓  
- Task 3 (`open the top drawer and put the bowl inside`): 仅完成 11/50 ep 后被杀（2 success, 9 fail）
- 后续 tasks 未开始

**GPU 1 当前状态**：被占用。PID 788647 正在运行 `eval_xvla_random_k05_goal_seed43`，占用 4838MiB。不可立即重跑。

**GPU 空闲情况**：GPU 0 和 GPU 3 空闲（1MiB）。

**是否建议重跑**：v1 已有 SR=53.4%，v2 目的是验证 mode typo 修复。当前 v2 跑了 2/10 个 task（假设 goal suite 10 tasks），数据不完整，无法得出最终 SR。如果需要完整验证，需等 GPU 1 空闲后重跑，或换到 GPU 0/3。但如果 v1 数据已足够做对比，可以跳过。

---
