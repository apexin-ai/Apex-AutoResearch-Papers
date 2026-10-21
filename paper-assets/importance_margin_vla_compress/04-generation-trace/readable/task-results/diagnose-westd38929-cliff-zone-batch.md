# diagnose westd38929 cliff zone batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd38929_cliff_zone_batch_20260525T165609_result.json`
- **Structured JSON:** [`93ed357e07a7a200d305.json`](../../sessions/93/93ed357e07a7a200d305.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 4 个实验仍在运行，无一完成。**

| 实验 | PID | GPU | GPU利用率 | 日志进度 | 结果JSON |
|------|-----|-----|----------|---------|----------|
| attn_k07_long | 214260 | 0 | 72% | Task 3/10, Ep 20/50 | 无 |
| l2norm_k07_long | 214795 | 1 | 67% | Task 3/10, Ep 20/50 | 无 |
| random_k07_long | 215329 | 2 | 70% | Task 3/10, Ep 30/50 | 无 |
| l2norm_k085_long | 215965 | 3 | 85% | Task 3/10, Ep 30/50 | 无 |

**诊断细节：**
- 4 个进程状态均为 `R (running)`，322 线程，~6.5GB RSS
- 4 块 GPU 均有 67-85% 利用率，确认在做计算
- 日志文件修改时间非常近（00:49-00:53），但内容只有 40 行，卡在 Task 3 → **stdout 缓冲问题**，`python -u` 对 `nohup bash -c "... > file 2>&1"` 的 redirect 不完全生效
- 已运行 ~20 小时，按日志中 0.9 eps/min 推算 500 episodes ≈ 8.3h，进程可能已远超 Task 3 但日志未刷新
- 无错误、无崩溃、无 OOM

**操作：**
- Registry：不更新（均未完成）
- Cron：`CronList` 显示当前 session 无 cron。如果 cron 是前一个 session 创建的，需要在那个 session 或通过 `delete_cron` 清除。要我现在用 `delete_cron` 按 exp_id 尝试清除吗？

---
