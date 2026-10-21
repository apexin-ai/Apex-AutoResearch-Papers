# fix and resume exp011

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix-and-resume_exp011_20260514T051004_result.json`
- **Structured JSON:** [`a09812c682644b566d02.json`](../../sessions/a0/a09812c682644b566d02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp011 已注册为 RUNNING。

**总结：**

1. **环境修复完成**：
   - `/tmp` 残留已清理
   - `TMPDIR=/root/autodl-tmp/tmp` 和 `RAY_TMPDIR=/root/autodl-tmp/ray_tmp` 已写入 `.bashrc` 并在训练命令中显式 export
   - 磁盘空间充足（根分区 23G，数据盘 159G）

2. **Checkpoint 恢复确认**：
   - verl 支持 `resume_mode=resume_path` + `resume_from_path`
   - global_step_10 checkpoint 完整（FSDP model + optimizer + rng + lr_scheduler 已加载到 2 个 rank）
   - 训练从 step 11 开始，跑到 step 30（剩余 20 步）

3. **exp011 已启动**：
   - tmux session: `exp011`
   - PID: 208791
   - GPU 0/1 各占用 ~11GB
   - 日志: `/root/autodl-tmp/exp011_grpo.log`
   - val_before_train 正在执行中

---
