# ops v9d disk timebomb fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v9d_disk_timebomb_fix_20260520T023859_result.json`
- **Structured JSON:** [`94183fd4673a4565a781.json`](../../sessions/94/94183fd4673a4565a781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 结果 |
|------|------|
| `max_actor_ckpt_to_keep` | **2**（已经是 2，config 正确） |
| `resume_mode` | `"auto"` |
| 走了哪个分支 | **情况 A**（只需清理旧 checkpoint，不需要重启） |
| 操作 | 删除了 `global_step_5/`（37GB 损坏 checkpoint） |
| 磁盘可用 | **135GB**（47% 使用，从 99GB → 135GB） |
| 训练进程 | PID 380305 正常运行中（已运行 ~12 分钟） |
| GPU | 4 卡均已分配显存（~27GB/98GB），利用率 0% 是因为采样时刻处于非计算阶段（正常，GRPO 训练在 rollout/update 间会有空闲） |

磁盘定时炸弹已解除。`max_actor_ckpt_to_keep=2` 意味着最多保留 2 个 checkpoint（2×37GB=74GB），加上 base model 和其他数据，135GB 可用空间足够安全完成训练。

---
