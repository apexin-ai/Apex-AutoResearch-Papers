# eval 8b ckpt3000 test westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_8b-ckpt3000-test-westd_20260514T202129_result.json`
- **Structured JSON:** [`e9bfa256cfae83e1111c.json`](../../sessions/e9/e9bfa256cfae83e1111c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**checkpoint-3000 不存在，无法执行 eval。**

原因：8B CLS 训练仍在进行中，当前进度 **step 662/6633**（约 10%）。checkpoint 每 200 步保存一次（已有 200/400/600），**step 3000 还没到**。

当前状态：
- **cuda:0**: 被 8B CLS 训练占用（PID 280392, 19234 MiB）— **不空闲**
- **cuda:1**: 同一训练进程占用（PID 281646, 12196 MiB）
- **cuda:2/3**: 其他训练占用（~30.7 GB）

预估 checkpoint-3000 到达时间：还需 2338 步 × ~8.2s/step ≈ **5.3 小时**（约今天晚上）。

**等训练跑到 step 3000 并保存 checkpoint 后才能提交 eval。** 届时 cuda:0 也仍然被训练占用，eval 需要等训练结束或用其他空闲 GPU。

---
