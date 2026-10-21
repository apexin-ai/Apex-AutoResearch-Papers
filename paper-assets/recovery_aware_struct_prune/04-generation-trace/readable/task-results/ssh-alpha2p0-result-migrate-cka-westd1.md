# ssh alpha2p0 result migrate cka westd1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_alpha2p0_result_migrate_cka_westd1_20260522T200435_result.json`
- **Structured JSON:** [`5f0e2f2d10469a770e74.json`](../../sessions/5f/5f0e2f2d10469a770e74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CKA-only eval 正在加载模型（PID 75284, 14.9GB RSS，CPU 阶段）。确认即将移到 GPU:1。

## α=2.0 MATH-500 SFT 结果
- **不存在** — `sft_rasp_alpha2p0_20` 模型目录存在，但从未启动过 MATH-500 eval（无结果文件、无日志）
- 已有 MATH-500 alpha eval: α=0.5 (GPU:2), α=1.0 (已完成), α=3.0 (GPU:0), α=4.0 (GPU:3)

## CKA-only MATH-500 迁移到 westd:1
- 新 PID: **75284**（父进程 75279）
- 状态: 模型加载中（CPU 14.9GB RSS，275% CPU），尚未移入 GPU
- GPU:1 显存: 0 MiB（模型加载后将占用）

## westb:0 CKA-only kill
- PID 234500: **killed**
- Standard Qwen-Math 模型: **not found**（grpo/sft 均不存在）

## westb GPU 状态
```
index, memory.used, utilization.gpu
0, 0 MiB, 100 %     ← 刚 kill，瞬态残留
1, 16547 MiB, 99 %  ← 有其他任务在跑
```

⚠️ α=2.0 MATH-500 eval 需要单独启动，但 westd 4 张卡目前全部占用（GPU:0/1/2/3 分别跑 α=3.0 / CKA-only / α=0.5 / α=4.0）。westb:0 现在空闲，可以考虑在 westb:0 上跑 α=2.0。

---
