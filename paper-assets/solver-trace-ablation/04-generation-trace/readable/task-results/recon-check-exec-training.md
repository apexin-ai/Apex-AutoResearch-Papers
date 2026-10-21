# recon check exec training

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recon_check-exec-training_20260521T231938_result.json`
- **Structured JSON:** [`31a63f4ee14fbfac255c.json`](../../sessions/31/31a63f4ee14fbfac255c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**exec-only seed 扩展实验进度：**

| Seed | 训练 | Eval | 状态 |
|------|------|------|------|
| s52 | ✅ checkpoint-500 完成 (05:53) | ✅ eval_sta.json 已生成 (06:23) | **完成** |
| s53 | ❌ 目录不存在 | — | 未开始 |
| s54 | ❌ 目录不存在 | — | 未开始 |
| s55 | ❌ 目录不存在 | — | 未开始 |
| s56 | ❌ 目录不存在 | — | 未开始 |

**GPU 状态：** GPU 0 空闲（0MiB / 97887MiB），无运行进程。

**磁盘：** `/root/autodl-tmp/` 已用 238G/250G (96%)，仅剩 13G。**磁盘紧张** — 当前 s52 的模型权重占约 8G，继续训练 s53 前需要清理空间（每个实验约需 8-10G）。

**结论：** 只完成了 s52 的训练+eval，s53-s56 尚未开始。GPU 空闲无活跃任务。磁盘剩余 13G，最多再跑 1 个 seed，之后需要清理。

---
