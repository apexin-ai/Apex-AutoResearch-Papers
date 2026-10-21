# fix exp004 tmpdir isolation v7

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp004_tmpdir_isolation_v7_20260515T180845_result.json`
- **Structured JSON:** [`5e448bed0f030fa2c05c.json`](../../sessions/5e/5e448bed0f030fa2c05c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **修复**：`run_sweep.py:296` 的 `_run_condition_wrapper` 中添加了 per-worker TMPDIR 隔离——每个并行 worker 创建独立的 `tempfile.mkdtemp(prefix=f"stan_{cid}_", dir="/home/ubuntu/tmp_cmdstan")`，避免 pymp finalizer 跨 worker 清理临时目录。

2. **v7 已启动**：tmux session `exp_004_sim_sweep_v7`，`--resume` 模式跳过已完成的 8 个条件，正在补跑 4 个全失败条件（auc0.65_n20/50/100, auc0.9_n100，共 40 个 seed）。CmdStan 采样已正常开始。

3. **Registry**：`exp_004_sim_sweep_v7` 已注册为 RUNNING。

---
