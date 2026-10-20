# ops 10894 deep cleanup resume

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-deep-cleanup-resume_20260526T180952_result.json`
- **Structured JSON:** [`2d9e870e4849f70009d5.json`](../../sessions/2d/2d9e870e4849f70009d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 磁盘状态
- **最终可用：124GB**（目标 80GB，超额完成）
- 删除了 3 个损坏的 20K checkpoint，释放 ~5GB（从 119G → 124G）
- 已完成实验只有 50K checkpoint，无中间 checkpoint 可清理

### 2. 删除详情
- `full_occ_ln_v2_s0/--20000_chkpt`（5GB，1/4 shard 部分损坏）
- `full_occ_ln_v2_s1/--20000_chkpt`（304K，完全损坏）
- `detach_ln_v2_s0/--20000_chkpt`（540K，完全损坏）

### 3. 实验启动
3 个实验已成功启动，从 step 0 开始训练（~1 it/s），预计 ~14 小时完成 50K steps。GPU 1/2/3 显存 ~62GB，利用率正常。

**⚠️ 关键变更：无法 resume，改为从头训练。** 3 个实验都不存在 10K checkpoint（磁盘满时只来得及写损坏的 20K），只能从 pretrained 重新开始。按 ~1 it/s 估算，50K steps ≈ 14 小时，预计 5/27 16:20 UTC 完成，在 DDL（5/28 12:00 UTC）前有余量。

**⚠️ 第二个问题：首次启动因 wandb API key 未配置而崩溃。** 已通过设置 `WANDB_MODE=disabled`（与 reverse_cutoff_s2_v2 一致）解决。

### 4. reverse_cutoff_s2_v2 (cuda:0)
正常运行，已保存 20K 和 30K checkpoint，PID 170698 活跃。

### 5. 异常
- 无 10K checkpoint 存在，resume 不可行，已改为从头训练
- wandb 未配置，已用 disabled 模式绕过

---
