# fix kill zombie exp002

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_zombie_exp002_20260517T034052_result.json`
- **Structured JSON:** [`abe9868edb795902db24.json`](../../sessions/ab/abe9868edb795902db24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### 僵尸进程
- **PID 25237 已成功 kill**，cuda:1 显存完全释放（0MiB）
- 无 exp_002 相关 tmux session（仅存 `exp_001_gen4`）

### 磁盘使用

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/`（根） | 30G | 25G | 5.1G | 84% |
| `/root/autodl-tmp`（数据盘） | 250G | 111G | 140G | 45% |

### Checkpoint 存储位置

两个 checkpoint 目录**都已正确 symlink 到数据盘**：
- `/root/spectral_collapse_ews/checkpoints/` → `/root/autodl-tmp/spectral_collapse_ews/checkpoints_410m/`（7.6G）
- `/root/spectral_collapse_ews/checkpoints_1b/` → `/root/autodl-tmp/spectral_collapse_ews/checkpoints_1b/`（16G，含 gen_0~gen_3）

### 1B 实验能否重启

**可以重启**。Checkpoint 写在数据盘（140G 剩余），不会撑爆根分区。根分区 84% 使用率虽偏高但不是 checkpoint 导致的，不影响 1B 训练继续。cuda:1 已空闲，随时可用。

---
