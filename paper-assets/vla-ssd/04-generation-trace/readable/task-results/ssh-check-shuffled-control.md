# ssh check shuffled control

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-shuffled-control_20260515T194205_result.json`
- **Structured JSON:** [`2d0cd8a3ea5947d8cbf2.json`](../../sessions/2d/2d0cd8a3ea5947d8cbf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### lg_shuffled_token_control
**未启动。** 无相关进程，结果目录不存在，日志文件为空。

### 当前运行的实验（3 个）

| 实验 | PID | GPU | 启动时间 | 状态 |
|------|-----|-----|---------|------|
| PCA-1024 goal_classification (untrained) | 650060 | GPU 0 | 03:41 | 运行中，untrained 阶段（trained 已完成，acc=1.0000） |
| Linear probe goal_classification (untrained) | 648231 | GPU 1 | 03:33 | 运行中，untrained 阶段，Layer 19/33 |
| **Exp-1 pca_linear_probe_perlayer** | 649515 | — | 03:38 | 运行中，trained_vla Layer 0 完成（acc=0.1582），刚开始 |

### GPU 使用率

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU 0 | 561 MiB | 2% |
| GPU 1 | 1713 MiB | 0% |

利用率低说明当前主要在做 CPU 端工作（PCA 降维、数据加载）。

### 注意
- perlayer sweep 的 layer 0 出现 `RuntimeWarning: invalid value encountered in divide`（PCA variance ratio 为 NaN），acc 仅 0.1582 — layer 0 特征可能全零或接近常数。
- tmux 无 session（进程通过 nohup 后台运行）。

---
