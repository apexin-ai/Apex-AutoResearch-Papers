# deploy westd41074 gpu2 attn k095

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu2_attn_k095_20260527T101855_result.json`
- **Structured JSON:** [`008f33c5c4f69f1c2936.json`](../../sessions/00/008f33c5c4f69f1c2936.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成：

**任务1** — `eval_pi05_random_k095_long_seed42_strict` 已注册为 DONE/success，metrics: avg_success_rate=0.606, notes: strict 60.6% vs lenient 63.2% Δ=-2.6pp

**任务2** — `eval_pi05_attn_k095_long_seed42_strict_w41` 已部署到 westd-41074 cuda:2
- tmux session `pi05_attn_k095` 运行中
- 日志确认：`suite=libero_10, prune=attention, keep=0.95`，正在加载模型
- 脚本确认 426 行版本
- Registry 状态 RUNNING

---
