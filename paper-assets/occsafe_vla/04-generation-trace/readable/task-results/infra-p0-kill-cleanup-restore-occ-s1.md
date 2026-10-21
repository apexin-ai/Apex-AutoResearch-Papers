# infra P0 kill cleanup restore occ s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_P0_kill_cleanup_restore_occ_s1_20260521T002314_result.json`
- **Structured JSON:** [`b8bd8dda50971f95af12.json`](../../sessions/b8/b8bd8dda50971f95af12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有步骤完成。汇报：

---

**Step 1**: cleanup — **KILLED**（进程 32353 已不存在），残留 — **无**（无 cleanup 进程运行中）

**Step 2**: occ_s0 (PID 27667) — **ALIVE**，occ_s2 (PID 29970) — **ALIVE**。GPU 0 和 GPU 2 各占用 ~62GB，GPU 1/3 空闲。

**Step 3**: 最高 checkpoint — **step 7500**（`openvla-7b+...--image_aug--7500_chkpt`）。恢复训练 — **已提交**，tmux session `mvp_occ_s1`，PID **54250**，cuda:1。日志显示正在加载模型（tensorflow GPU warning 可忽略）。

**Step 4**:
- westd-34685: crontab **无**，cleanup 脚本文件存在于 `/root/autodl-tmp/`（`cleanup_checkpoints.sh`、`cleanup_loop.sh`、`cleanup_loop.log`、`cleanup.log`），但无运行中进程
- westd-10894: cleanup 进程 **无**，crontab **无**

> ⚠️ `/root/autodl-tmp/cleanup_checkpoints.sh` 和 `cleanup_loop.sh` 脚本文件仍在磁盘上。建议后续删除或 rename 防止误启动。

---
