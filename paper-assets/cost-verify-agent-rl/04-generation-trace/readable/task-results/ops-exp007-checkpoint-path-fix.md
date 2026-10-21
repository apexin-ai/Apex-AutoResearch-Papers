# ops exp007 checkpoint path fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp007_checkpoint_path_fix_20260514T005045_result.json`
- **Structured JSON:** [`43ec6de97c436c96c62b.json`](../../sessions/43/43ec6de97c436c96c62b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

---

### 诊断结论

1. **exp007 checkpoint 实际保存到哪里？** → **数据盘** `/root/autodl-tmp/checkpoints/exp_007/`（配置中 `local_log_dir` 和 `default_local_dir` 均已正确设置）

2. **是否需要停止重启？** → **否**。路径已正确，训练正常运行中（主 PID 178842，tmux session `exp007`，GPU 0/1 各占 550 MiB）

3. **根分区清理后剩余空间** → 删除 20GB dryrun checkpoint 后：**23GB 可用**（27% 使用率），从 90% → 27%

4. **无需重启**，训练继续运行。首次 checkpoint 将在 step 20 保存到数据盘。

---
