# ops urgent gpu2 cleanup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_gpu2_cleanup_20260514T021132_result.json`
- **Structured JSON:** [`a5a99ecd0f08b83f052d.json`](../../sessions/a5/a5a99ecd0f08b83f052d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**(a) Kill 结果**
- PID 254667 — 已 kill（SIGTERM 成功）
- PID 255703 — 已 kill（SIGTERM 成功）

**(b) 输出目录状态**
- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/` — **目录为空**，两个冗余进程运行了 ~45min 但未产出任何文件。无数据损失。

**(c) 合法进程确认**
- PID 256509 — 运行中（39min），在 **GPU 5**（不是 GPU 4），评估 d100_s42，占 3658 MiB
- PID 257034 — 运行中（38min），在 **GPU 2**（接替释放的显存），评估 **d000_s42**，占 3658 MiB

**(d) d005 eval 进程确认**
- PID 255322 — 运行中（43min），在 **GPU 1**，评估 d005_s42，占 3658 MiB

**GPU 2 当前状态**: 3667 MiB used / 35% util — 已释放冗余进程显存，仅剩 PID 257034 (d000_s42 eval) 在使用。

---
