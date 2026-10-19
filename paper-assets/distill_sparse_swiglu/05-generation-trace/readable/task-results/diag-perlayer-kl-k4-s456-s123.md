# diag perlayer kl k4 s456 s123

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_perlayer_kl_k4_s456_s123_20260522T151456_result.json`
- **Structured JSON:** [`4d284faa43b6870ebac5.json`](../../sessions/4d/4d284faa43b6870ebac5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整诊断已出。

---

## 诊断报告

### 结论：实验没有真正失败，当前仍在运行

两个实验的 nohup pipeline 仍在执行，只是**监控系统误判**。

### 证据

| 指标 | s456 | s123 |
|------|------|------|
| Phase 1 训练 | 完成 (Step 2700/2700) | 完成 (Step 2700/2700) |
| 训练 wall time | 5005.2s (~83 min) | 5016.1s (~84 min) |
| avg_kl (final) | 0.0447 | 0.0449 |
| avg_sparsity (final) | 0.280 | 0.284 |
| Checkpoints | 全部存在 (500/1000/1500/2000/2500/2700 + final) | 全部存在 |
| Phase 2 PPL | **8.8828** | **8.8897** |
| Phase 3 Downstream | 正在运行 (~40%) | 正在运行 (~44%) |
| Phase 4 分析 | 未开始 | 未开始 |

**当前 GPU 状态**：两块 RTX PRO 6000 Blackwell 均 97% 利用率，66GB VRAM 占用，PID 65980 (cuda:0) 和 66278 (cuda:1) 活跃。

### 误判根因

监控系统追踪的是**原始 PID**（59879/59565），这些是 Phase 1 训练进程的 PID。Pipeline 脚本是 `set -e` 的 bash 脚本，顺序运行 4 个 phase，每个 phase 启动新的 python 子进程，获得新 PID。当训练结束、eval 开始时：

1. 原始训练进程 PID 退出（正常结束）
2. 新的 eval 进程获得新 PID（65980/66278）
3. 监控系统检查原始 PID → 发现 dead → 5 次检测都 dead → 标记 failed
4. 同时 `WANDB_MODE=disabled`，无 W&B heartbeat 可作为存活信号

**对比 s42 成功案例**：s42 用"直接 python 命令"运行（单个进程），PID 始终不变，监控系统能正确追踪。

### 与 s42 的 metrics 对比

| 种子 | PPL (WikiText-2) | 训练 avg_kl | Model-level sparsity |
|------|-----------------|-------------|---------------------|
| s42 | (需查) | (需查) | (需查) |
| s456 | 8.8828 | 0.0447 | 0.296 |
| s123 | 8.8897 | 0.0449 | 0.297 |

s456 和 s123 训练结果一致性很好。

### 建议

1. **不需要修复，等待完成**：两个 pipeline 仍在运行 Phase 3 downstream eval（58702 个 loglikelihood requests，~40-44% 进度，预计还需 ~8-10 分钟）
2. **在 registry 中将状态改回 running**，或等 Phase 3+4 结束后标记 completed
3. **长期修复监控系统**：pipeline bash 脚本场景下，应追踪 bash 进程组 PID（`$$`）而非子进程 PID，或在每个 phase 写入 heartbeat 文件

---
