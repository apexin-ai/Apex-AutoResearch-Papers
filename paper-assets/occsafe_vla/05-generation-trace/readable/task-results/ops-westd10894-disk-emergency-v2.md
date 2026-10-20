# ops westd10894 disk emergency v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd10894_disk_emergency_v2_20260523T160025_result.json`
- **Structured JSON:** [`a663eda499099e076b2b.json`](../../sessions/a6/a663eda499099e076b2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**任务 1 — 删除旧 crash checkpoint**：
- `/root/occsafe_vla/checkpoints/` 不存在
- `/root/autodl-tmp/checkpoints/` 下 4 个实验目录（detach_ln_s0/s1/s2, cutoff_s2_v2）仅有 `dataset_statistics.json`，无 checkpoint 目录
- 训练尚未到达首次 checkpoint 保存点，无需删除
- 释放空间：0（本来就没有旧 checkpoint）

**任务 2 — Checkpoint rotation 脚本**：
- 创建 `/root/occsafe_vla/cleanup_old_checkpoints.sh`，覆盖 4 个实验目录
- 匹配实际命名格式 `*_chkpt`（非 `checkpoint_NNNNN`）
- 每个实验保留最新 1 个 checkpoint，删除其余
- 日志写入 `/tmp/checkpoint_cleanup.log`
- 服务器无 crontab，改用 nohup 后台循环，每 30 分钟执行一次（PID=453371）
- 手动运行验证通过，无错误

**磁盘状态**：
- `/root/autodl-tmp`: 250G 总量，37G 已用，**214G 可用**（15%）
- `/root`: 30G 总量，21G 已用，9.1G 可用（70%）

> 注意：214G 可支撑首轮 4×30G=120G checkpoint 保存。rotation 脚本启动后，第二轮保存前会自动清理旧 checkpoint，确保持续有足够空间。

---
