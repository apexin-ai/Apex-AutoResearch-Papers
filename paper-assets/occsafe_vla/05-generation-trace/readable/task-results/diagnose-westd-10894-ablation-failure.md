# diagnose westd 10894 ablation failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-10894-ablation-failure_20260521T045423_result.json`
- **Structured JSON:** [`324b2ae5f2c339e2070c.json`](../../sessions/32/324b2ae5f2c339e2070c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集。以下是诊断报告。

---

## 诊断报告

### 根本原因：**SSH 会话断开 / 平台级进程管理**（推测，置信度 80%）

证据链：
- 4 个进程在 **12:52:12 UTC+8 的同一秒内**（精确到 ±17ms）同时收到 SIGTERM
- **不是 OOM**：内存 83GB/1TB，无 OOM 记录
- **不是磁盘满**：root 66%，data 51%
- **不是重启**：uptime 156 天，无 reboot 记录
- **不是 cron**：无 crontab
- **无系统日志可查**：容器环境，dmesg 无权限，syslog/kern.log/auth.log 均为空
- `bash_history` 显示此前手动启动实验使用了 `| tee`（非 nohup），如果 ablation 实验也是从 SSH 会话直接启动的，SSH 断连会级联 SIGTERM 到所有子进程

最可能的两种情况：
1. 启动实验的 SSH 会话意外断开，SIGTERM 级联到所有子进程组
2. SeetaCloud 平台级别的资源管理/维护事件

### 训练进度

| 实验 | 最后 step | 进度 | 运行时长 |
|------|-----------|------|----------|
| ablation_occ_detach_s0 | 4006/50005 | 8% | ~1h07m |
| ablation_random_occ_s0 | 3993/50005 | 8% | ~1h07m |
| ablation_occ_detach_s1 | 1546/50005 | 3% | ~29m |
| ablation_random_occ_s1 | 1545/50005 | 3% | ~29m |

### Checkpoint 状态

| 实验 | checkpoint | 可 resume |
|------|-----------|-----------|
| ablation_occ_detach_s0 | 2500_chkpt ✓（完整，含 model shards + action_head + occ_head + proprio_projector + lora_adapter） | **是，从 step 2500** |
| ablation_random_occ_s0 | 2500_chkpt ✓（完整） | **是，从 step 2500** |
| ablation_occ_detach_s1 | 无（save_freq=5000，未到第一个保存点） | **否，需从头开始** |
| ablation_random_occ_s1 | 无 | **否，需从头开始** |

### 服务器当前状态

- **GPU**: 4x NVIDIA RTX PRO 6000 Black (98GB)，全部空闲，0MiB VRAM
- **磁盘**: 正常
- **内存**: 正常 (83GB/1TB)
- **负载**: 7.37（正在回落）
- **进程**: 仅 24 个基础进程，无训练任务运行

### 建议

重启实验时用 `nohup ... &` 或 `tmux`/`screen` 启动，避免 SSH 断连再次杀死进程。s0 两组从 2500 checkpoint resume，s1 两组需完全重跑。可以考虑将 `save_freq` 从 5000 降到 2500 减少损失。

---
