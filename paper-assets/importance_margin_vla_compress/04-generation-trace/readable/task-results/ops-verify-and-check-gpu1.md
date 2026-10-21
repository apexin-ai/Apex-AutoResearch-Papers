# ops verify and check gpu1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_and_check_gpu1_20260522T031505_result.json`
- **Structured JSON:** [`f35a0891b3593e34dd55.json`](../../sessions/f3/f35a0891b3593e34dd55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

## 1. GPU 0 — v4 (eval_pi05_random_k095_spatial_seed42_v4)

**状态：正常启动中，尚未开始评估。**

- 进程链：bash (PID 13526) → timeout (13534) → python (13535, 运行 ~2 min, 7.3 GB RSS, 546% CPU)
- 模型已加载完成（4143.4M params），环境已创建（libero_spatial, 10 tasks），pruning 配置正确（random, keep 243/256 = 95%）
- GPU 0 显存仅 4 MiB — 模型还在 CPU→GPU 迁移阶段，属正常
- 日志无 Error/Exception，最后一行是 `[PRUNE-DIAG] random: n_keep=243/256`
- 预计 1-2 分钟后 GPU 显存会上涨并开始 T0 评估

## 2. GPU 1 — 两个共享实验

GPU 1 总显存占用 20.9 GB / 97.9 GB，两个进程共享。

### PID 922934: k=0.85 Object seed43 v3
- 运行 59 min，当前在 **T4/10**（ep30/50）
- 已完成 T0-T3（4 个 Task summary 行），中间成绩：
  - T1: 6.0%, T2: 2.0%, T3: 0.0%, T4 暂时 10%
- 每 task 约 12-13 min，剩余 T4(partial) + T5-T9 ≈ **70-80 min**

### PID 942398: k=0.925 Spatial seed42
- 运行 42 min，当前在 **T3/10**（ep20/50）
- 已完成 T0-T2（3 个 Task summary 行），中间成绩：
  - T0: 94.0%, T1: 48.0%, T2: 72.0%, T3 暂时 35%
- 每 task 约 10-11 min，剩余 T3(partial) + T4-T9 ≈ **75-85 min**

## 3. 建议

k=0.85 Object s43 才到 T4/10，离完成还远，不需要特殊处理。两个实验都还需 ~1.5 小时，GPU 1 显存充裕（仅用 21%），共享运行没有瓶颈。v4 在 GPU 0 即将开始正式评估，建议 5-10 分钟后再复查确认 T0 已跑起来。

---
