# ops exp029 seed2 oom fix restart

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp029-seed2-oom-fix-restart_20260518T054458_result.json`
- **Structured JSON:** [`ebb41bf2b84595d39c35.json`](../../sessions/eb/ebb41bf2b84595d39c35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。

**汇报：**
- **OOM 原因**：`enable_gradient_checkpointing` 未启用（默认 `False`），full context 模式长序列在 `loss.backward()` 时显存不足。seed1 也同样 OOM，非 seed-specific。
- **修复方案**：方案 2 — 启用 `enable_gradient_checkpointing: true` + 降低 `ppo_max_token_len_per_gpu` 65536→32768
- **新 PID**：6349（tmux session: `exp029_episode_level_seed2`）
- **启动确认**：GPU 0/1 各占 4715 MiB，wandb run `etgc8xjn` 已创建，正在加载数据（val_before_train 阶段）
- **无 checkpoint 可恢复**，从头开始训练
- **注意**：seed1 (`exp029_episode_level`) 也因相同原因 OOM，需要同样修复

---
