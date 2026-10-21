# diag exp004 failure

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp004-failure_20260518T163248_result.json`
- **Structured JSON:** [`a5d440680d25bfd1b0c0.json`](../../sessions/a5/a5d440680d25bfd1b0c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

**exp-004 并没有 crash。训练正在正常进行。**

### 失败根因

"crash"是 launch 脚本 (`launch_exp004.sh`) 里的 **dry-run 步骤 OOM**，不是实际训练进程。

时间线：
1. **23:55** — 训练进程 (PID 18204) 通过另一条命令直接启动，加载模型到 GPU 0（占用 ~21 GiB）
2. **00:28** — launch 脚本完成模型下载后尝试 dry-run，也在 GPU 0 上加载模型
3. dry-run OOM crash：`CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has ... 70.38 MiB free`
4. `set -e` 导致 launch 脚本退出，看起来像"训练 crash 了"

**实际上是两个进程同时抢 GPU 0 导致的 dry-run 失败。**

### 训练当前状态

训练进程 PID 18204 正常运行中，已到 **step 270/8000**：

| Metric | Step 10 | Step 270 |
|--------|---------|----------|
| sft_loss | 2.586 | 0.013 |
| l2_loss | 2.433 | 0.016 |
| total_loss | 2.830 | 0.014 |
| lr | 2.5e-6 | 4.96e-5 |

Loss 下降健康，每 10 步约 84 秒，预计总时长约 18.7 小时。

### GPU 当前状态

| GPU | 显存 | 状态 |
|-----|------|------|
| GPU 0 | 21.6 / 32.6 GiB | 训练中 (PID 18204, 49% util) |
| GPU 1 | 空闲 | 可用 |
| GPU 2 | 空闲 | 可用 |
| GPU 3 | 空闲 | 可用 |

### 修复建议

无需修复 — 训练正常进行。但 launch 脚本有设计缺陷：dry-run 没有检查 GPU 是否已被占用。如果后续需要复用该脚本，建议在 dry-run 前加 `nvidia-smi` 检查，或直接去掉 dry-run 步骤（训练脚本自身已经能快速失败）。

---
