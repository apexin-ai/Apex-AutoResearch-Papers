# fix copy checkpoint restart

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_copy-checkpoint-restart_20260517T193025_result.json`
- **Structured JSON:** [`8ef38a1ae0e9102e9170.json`](../../sessions/8e/8ef38a1ae0e9102e9170.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### 1. Checkpoint 传输
- **方式**：设置临时 SSH 密钥，从 westd 直接 rsync 拉取 bjb1 的 `final/` 目录（3.4GB model.safetensors + 配置文件）
- **状态**：完成。文件大小完全一致（3441185608 bytes）
- Symlink `qwen3_exp021_ragen_sft_v4 -> exp021_ragen_sft_v4/final` 已重建
- 临时 SSH key 已从 bjb1 清理

### 2. 额外问题修复
- **`/root/autodl-tmp/alfworld/` 也被误删**，导致第一次启动崩溃（`ZeroDivisionError: game_files 为空`）
- 从 `/root/.cache/alfworld/` 恢复数据后重启成功

### 3. 实验状态
- **tmux session**: `factorial_h2_episodeadv_seed1` 存活
- **TaskRunner PID**: 450445（CPU 74%，R 状态）
- **GPU**: 0 → 38GB, 1 → 38GB（vLLM 引擎已加载）
- **数据**: 3553 训练游戏 + 134 OOD 评估游戏已加载
- **wandb run**: `factorial-h2-episode-adv` (ID: `jsrvwcfd`)
- 当前处于 `val_before_train` 阶段，主日志因 Ray log deduplication 暂停更新，但 worker stdout 确认进展正常

---
