# diagnose exp026 status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp026_status_check_20260515T103447_result.json`
- **Structured JSON:** [`78cf7aa8a604214493f6.json`](../../sessions/78/78cf7aa8a604214493f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 状态：训练已成功启动并运行中

| 项目 | 值 |
|------|-----|
| tmux session | `exp026` |
| 主进程 PID | 781795 (train.py) |
| GPU 0 | 53% util, 41297 MiB / 97887 MiB |
| GPU 1 | 53% util, 41297 MiB / 97887 MiB |
| 磁盘 | /root/autodl-tmp 130G/250G (52%) |
| 数据 | train: 8810 items, val: 494 items |
| 配置 | 150 steps, test_freq=5, save_freq=25 |

### 过程
1. **首次提交失败**：训练因 `wandb.errors.UsageError: No API key configured` 崩溃——服务器上未配置 wandb API key
2. **修复**：添加 `WANDB_MODE=disabled` 环境变量后重新提交
3. **当前状态**：已通过 pre-flight、数据预处理、模型加载（41 GB/GPU），进入 rollout 计算阶段
4. 日志输出有延迟（Ray buffered output），但 GPU 活动确认训练正在运行

### 注意
- 训练无 wandb 日志记录（disabled）。如需恢复，需在服务器上配置 `WANDB_API_KEY`
- GPU 0 之前有 phantom 100% util 状态，新 CUDA 进程启动后自动消失
- 预计 ~21 min/step（基于 dry run），首个 step 指标应在 ~20 分钟后出现在日志中

---
