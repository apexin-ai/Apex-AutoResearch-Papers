# diag v9d sighup fix restart

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_v9d_sighup_fix_restart_20260520T075700_result.json`
- **Structured JSON:** [`aa26a7178a68695d4488.json`](../../sessions/aa/aa26a7178a68695d4488.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。总结：

**SIGHUP 不存在。** 原 failure_reason 记录的 EXIT_CODE=129 与日志不符——所有日志中崩溃均为 EXIT_CODE=1。v9c 的真正根因是 vLLM prompt 长度 16384 = max_model_len，无输出 token 空间。

**当前状态：v9d 已在运行中。**
- 从 `global_step_10` 恢复（实际到了 step 10，不是之前 metrics 记录的 step 7）
- tmux session 活跃，4×GPU 加载完毕，wandb 已连接 (aeml21w9)
- 磁盘 106GB 可用，剩余 20 步 (step 11→30)
- SFT checkpoint 通过 symlink→Qwen3-8B 修复

**风险：** config 中 `max_prompt_length=15360` / `max_model_len=16384` 未变，v9c 的 prompt 溢出崩溃可能在某个 episode 重现。若再崩，建议将 `max_prompt_length` 降至 14336 或提高 `max_model_len`。

诊断报告已注册为 artifact (`art_20260520_c7e223`)，registry notes 已更新。

---
