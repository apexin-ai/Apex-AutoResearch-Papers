# diagnose westd 10894 ablation crash

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-10894-ablation-crash_20260521T045433_result.json`
- **Structured JSON:** [`209b40284130411d7894.json`](../../sessions/20/209b40284130411d7894.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集完所有诊断信息。以下是报告。

---

## 诊断报告：4 个 ablation 实验 SIGTERM 终止

### 失败根因

**外部 SIGTERM 信号同时杀死所有进程，最可能是启动实验的 SSH 会话/父进程超时或终止。**

关键证据：
- 4 个进程在 **完全相同的时刻**（12:52:12 本地时间，精确到秒内）收到 SIGTERM (signal 15)
- **排除 OOM**：OOM killer 发送 SIGKILL (signal 9)，而非 SIGTERM
- **排除磁盘满**：根分区 66% (20G/30G)，数据盘 63% (156G/250G)
- **排除系统重启**：系统运行时间 ~156 天，无重启记录
- **排除手动 kill**：bash_history 中无 kill 命令
- **排除 cron job**：无相关定时任务
- **排除硬件故障**：GPU 驱动正常（NVIDIA RTX PRO 6000 Blackwell Server Edition × 9）

结论：实验通过 `ssh_execute` 启动，当 SSH 会话或父进程终止时，SIGTERM 被传播到所有子进程。这与4个进程在同一秒内被杀的模式完全吻合。

### 各实验训练进度

| 实验 | GPU | 启动时间 | 运行时长 | 最终步数 | 进度 |
|------|-----|----------|----------|----------|------|
| ablation_random_occ_s0 | cuda:0 | 11:44 | ~68 min | 3993/50005 | 8% |
| ablation_occ_detach_s0 | cuda:1 | 11:44 | ~68 min | 4006/50005 | 8% |
| ablation_random_occ_s1 | cuda:2 | 12:22 | ~30 min | 1545/50005 | 3% |
| ablation_occ_detach_s1 | cuda:3 | 12:22 | ~30 min | 1546/50005 | 3% |

### Checkpoint 状态

| 实验 | 2500 步 checkpoint | 可 resume |
|------|-------------------|-----------|
| ablation_random_occ_s0 | ✅ 完整（含 model, action_head, occ_head, proprio_projector, lora_adapter） | ✅ 从 step 2500 |
| ablation_occ_detach_s0 | ✅ 完整 | ✅ 从 step 2500 |
| ablation_random_occ_s1 | ❌ 未到 save_freq（仅 1545 步） | ❌ 需从头开始 |
| ablation_occ_detach_s1 | ❌ 未到 save_freq（仅 1546 步） | ❌ 需从头开始 |

### 服务器当前状态

- **可达**：SSH 连接正常
- **GPU**：9× NVIDIA RTX PRO 6000 Blackwell，驱动正常
- **磁盘**：根分区 11G 可用，数据盘 95G 可用，空间充足
- **无残留进程**：所有训练进程已终止
- **可立即重启实验**

### 建议

重新启动时确保使用 `nohup ... &` 或在 tmux 内运行，使训练进程与 SSH 会话解耦，避免再次因 SSH 断连而被杀。s0 组可从 step 2500 resume，s1 组需从头开始。

---
