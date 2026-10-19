# diagnose v2 lora failed

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v2_lora_failed_20260516T155337_result.json`
- **Structured JSON:** [`8c9dc29175c445b39ff2.json`](../../sessions/8c/8c9dc29175c445b39ff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 失败根因：外部 kill（tmux session 终止或手动清理）

两个实验在**同一时间**（23:48:51 和 23:49:03）被系统信号终止，无 Python traceback，日志最后一行直接是 "Terminated"：

| 实验 | 信号 | 最后 step | 最后 loss | 最后 checkpoint |
|------|------|-----------|-----------|-----------------|
| v2_lora_spatial_r16 | SIGHUP (129) | 6300 | 0.6840 | step_6000 |
| v2_lora_universal_r16 | SIGTERM (143) | 9300 | 0.6798 | step_9000 |

**排除 OOM**：当前 GPU 显存充足（4×97GB，仅 GPU 0 和 GPU 3 占用 ~8GB），且训练过程中 loss 稳定下降、无显存异常迹象。

**时间线关键点**：
- 四个实验同时启动（~22:17）
- visual 和 physical 在 23:26-23:31 **自然完成**（10000 steps）
- spatial 和 universal 在 ~23:49 **同时被杀**（仍在训练中）

两个成功实验先跑完退出，约 18 分钟后剩余两个被同时终止。SIGHUP = 控制终端断开，SIGTERM = 外部 kill。最可能是**托管进程的 tmux session 被关闭或 SSH 连接断开**导致信号级联。

### 训练进展

两个实验 loss 曲线健康且持续下降：
- **spatial**：从 ~0.76（step 4000）降至 0.684（step 6300），进展 63%（目标 10000 步）
- **universal**：从 ~0.71（step 7000）降至 0.680（step 9300），进展 93%（目标 10000 步）

### 值得重跑

是。训练完全正常，纯属被误杀。

### 重跑策略

**从 checkpoint 恢复**：
- `v2_lora_spatial_r16`：从 `step_6000` 恢复，剩余 ~4000 步（~3.4 小时）
- `v2_lora_universal_r16`：从 `step_9000` 恢复，剩余 ~1000 步（~51 分钟）

建议用 `nohup` 或确保 tmux session 不会被意外清理。如果有自动清理 cron，需要排查 `/etc/crontab` 或 `crontab -l`。

---
