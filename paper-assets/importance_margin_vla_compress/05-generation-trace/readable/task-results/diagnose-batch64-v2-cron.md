# diagnose batch64 v2 cron

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_batch64_v2_cron_20260517T072318_result.json`
- **Structured JSON:** [`7d26c38e2e14e036283f.json`](../../sessions/7d/7d26c38e2e14e036283f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**第一次 v2 运行 (09:19–13:08)**: 在 step 3550 静默死亡，和 v1 完全一致。

- 日志最后一行：`step=3550 loss=0.0928 grad=1.14` — 数值正常，非梯度爆炸
- 无 error/traceback，无 checkpoint（save_every=5000 未触发）
- 退出码文件已被新提交清理，dmesg 无权限
- 两次在同一 step 崩溃，高度怀疑 **CPU 内存泄漏** 导致 OOM killer（batch64 的 16x grad_accum + 4 个 dataloader worker 内存开销大）

**当前状态**: 已于 15:13 被重新提交，正在从 step 0 训练中（当前 step ~150）。GPU 1 进程正常。

**不执行 delete_cron 和标记 DONE** — 实验正在运行中，cron 监控仍有必要。如果再次在 step ~3550 崩溃，需要排查内存泄漏（可考虑减少 dataloader workers 或加 `save_every=2000` 保底）。

---
