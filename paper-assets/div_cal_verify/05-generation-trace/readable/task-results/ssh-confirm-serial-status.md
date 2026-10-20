# ssh confirm serial status

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_confirm-serial-status_20260512T144516_result.json`
- **Structured JSON:** [`3b73e8ee6b43af8afe6e.json`](../../sessions/3b/3b73e8ee6b43af8afe6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**1. mvp_rgds_v3.log 退出原因**
确认是磁盘满崩溃。gen 3 训练阶段 `save_pretrained` 时报 `SafetensorError: No space left on device (os error 28)`。

**2. 串行脚本状态**
- PID 42073 在跑，已运行 ~5 分钟
- 子进程 `run_all_methods.sh` (PID 42074) → `run_mvp.py --method rgds` (PID 42079)
- 当前阶段：**rgds 方法重跑**，已加载模型，正在从 gen 0 重新开始（非断点续跑）
- Gen-0 RankMe baseline: 983.21，generator 已加载完毕

**3. GPU 使用**
- 双卡 RTX PRO 6000 Blackwell (各 98GB)
- GPU 0: 58659MiB / 97887MiB, 64% util（PID 42079）
- GPU 1: 21633MiB / 97887MiB, 0% util（PID 42079）

**4. 各方法已完成 gen 数**
- `rgds`: gen_0, gen_1, gen_2 已有 metrics.json（上次跑的残留），当前正在重跑
- `external_only`: 尚未开始
- `uncurated`: 尚未开始

**5. 磁盘**
- 根分区 `/`: 21G/30G used (68%) — 还剩 9.8G，之前磁盘满已清理过
- 数据盘 `/root/autodl-tmp/`: 3.3G/250G used (2%) — 充裕

根分区 68% 需注意：rgds 4 个 gen 的 checkpoint 如果写根分区可能再次爆盘。确认 `--output_dir ./results` 实际写入的是 `/root/autodl-tmp/` 下的路径（当前 results 目录确实在 autodl-tmp 下），应该没问题。

---
