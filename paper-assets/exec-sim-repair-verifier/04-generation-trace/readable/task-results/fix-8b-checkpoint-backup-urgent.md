# fix 8b checkpoint backup urgent

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_8b-checkpoint-backup-urgent_20260514T110101_result.json`
- **Structured JSON:** [`0904e7a3f8be70514bc2.json`](../../sessions/09/0904e7a3f8be70514bc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 磁盘
- 总 250G，已用 131G，剩余 120G（53%）
- 单个 8B checkpoint: **176M**
- 备份占用增量: 10 × 176M ≈ 1.7G

### 已备份 checkpoint
**CLS 8B seed123** (5个): checkpoint-200, 800, 1000, 1200, 1400
→ `/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/`

**CWM 8B** (5个): checkpoint-300, 400, 500, 600, 700
→ `/root/autodl-tmp/checkpoints_backup_cwm_8b/`

已丢失无法恢复: CLS ckpt-400/600, CWM ckpt-100/200

### 自动备份
tmux session `ckpt_backup` 已启动，每 60 秒扫描新 checkpoint 并自动备份。日志: `/root/autodl-tmp/backup.log`

### 空间估算
CLS 6633 steps / 200 save_steps ≈ 33 checkpoints × 176M ≈ **5.8G**，120G 剩余空间完全充足。

---
