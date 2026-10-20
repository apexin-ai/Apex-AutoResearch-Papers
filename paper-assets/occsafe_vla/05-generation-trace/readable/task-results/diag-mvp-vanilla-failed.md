# diag mvp vanilla failed

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp_vanilla_failed_20260520T091618_result.json`
- **Structured JSON:** [`39fa8c9d26b85b73d6e4.json`](../../sessions/39/39fa8c9d26b85b73d6e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论**：三个实验在 `17:15:07.247` 同毫秒被 SIGTERM，根因是 **tmux sessions 被外部命令统一杀掉**（非 OOM、非磁盘满、非重启、非代码错误）。关键证据：10 个 nohup 启动的 `extract_occupancy.py` 进程完全存活，只有 tmux 中的训练进程死亡。

**当前状态**：
- 自动重试已在 17:16-17:17 重启全部 3 个实验，目前正常训练中
- 无 checkpoint 损失（save_freq=10000，仅跑到 ~2000 步）
- 训练从 step 0 重新开始
- GPU/磁盘/内存均正常，可安全继续

**风险提示**：GPU 0 上 10 个 `extract_occupancy.py` 进程（各 557MiB VRAM）与 s0 训练并行，可能有轻微资源竞争。

---
