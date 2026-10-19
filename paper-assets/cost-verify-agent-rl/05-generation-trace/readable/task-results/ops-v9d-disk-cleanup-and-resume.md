# ops v9d disk cleanup and resume

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v9d_disk_cleanup_and_resume_20260520T022403_result.json`
- **Structured JSON:** [`fa6de2596a39f2a64151.json`](../../sessions/fa/fa6de2596a39f2a64151.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正在健康运行（4 GPU 100% 利用率），当前处于 val_before_train rollout 阶段，需要几分钟才会有 step 日志。

## 执行摘要

**磁盘清理:**
- 删除 scienceworld_sft 3 个中间 checkpoint (global_step_112/224/336)，释放 ~81GB
- 228GB → 147GB 使用，104GB 可用

**配置修改（根因修复）:**
- `resume_mode: "disable"` → `"auto"`
- `max_actor_ckpt_to_keep: 5` → `2` — **这是磁盘满的根因**：5 checkpoint × 37GB = 185GB，超出可用空间。降到 2 后峰值 ~111GB 安全

**Checkpoint:**
- step 5 checkpoint 完整（4 model shard + 4 optimizer shard，共 37GB）

**训练状态:**
- tmux session: `8b_cell_c_episode_v9d`
- W&B run: `vvx8zr0l`
- 4× RTX PRO 6000 100% 利用率，~25-28GB/GPU
- 正在做 val_before_train rollout（32 个 ALFWorld 环境）

**待确认:** 第一个 step 日志出现后才能确认是从 step 5 resume 还是从头开始。需要等 5-15 分钟 rollout 完成。

---
