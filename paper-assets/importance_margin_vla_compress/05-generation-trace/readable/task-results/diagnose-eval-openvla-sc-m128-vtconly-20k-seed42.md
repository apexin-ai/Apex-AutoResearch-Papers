# diagnose eval openvla sc m128 vtconly 20k seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_sc_m128_vtconly_20k_seed42_20260520T075058_result.json`
- **Structured JSON:** [`08d9146ca52a26f272cc.json`](../../sessions/08/08d9146ca52a26f272cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**根因：Cron 监控的 session name 格式校验 bug，进程本身正在正常运行。**

关键事实：
- **PID 909497 活着**，CPU 153%，已运行 ~14 分钟
- tmux session `eval_openvla_sc_m128_20k` 存在且进程在其中运行
- 日志最后更新 15:46:23，当前正在执行 Task 0 Ep 2/50（Ep 1 FAIL，280 steps，耗时 ~8 分钟）
- Checkpoint 存在（19.9GB）
- GPU 0 占用 36GB 显存

**Cron 报错原因**：监控系统将 `tmux:eval_openvla_sc_m128_20k` 整串作为 session name 校验，冒号 `:` 不匹配 `[a-zA-Z0-9_-]+` 正则，导致连续 5 次检查失败报 failure。这是 cron 监控侧的 bug，不影响实际进程。

**不需要重试**。进程正常运行中，等它跑完即可。10 tasks × 50 episodes，每个 episode 最多 280 steps（~8 分钟），预计总耗时较长（成功的 episode 会更快结束）。

---
