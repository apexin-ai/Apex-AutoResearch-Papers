# diagnose exp walker 008d s7 s6

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_walker_008d_s7_s6_20260527T232328_result.json`
- **Structured JSON:** [`2f150a01b4a46c4ac706.json`](../../sessions/2f/2f150a01b4a46c4ac706.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总如下：

---

## 诊断结果

### exp_walker_008d_s7

| 项目 | 结果 |
|------|------|
| **失败原因** | SIGTERM (EXIT_CODE=143)，外部 kill。非 OOM（日志无 CUDA OOM 错误，日志仅 45 行/4.3KB）。两个实验在完全相同时间（May 28 07:20）被终止，指向**批量 kill**（手动或调度系统） |
| **训练进度** | 仅到 **step 8000**（约 10 分钟运行时间） |
| **105K 评估数据** | **无**。唯一 eval 在 step 5000：eval_return=31.2 |
| **W&B** | **无** W&B run（日志中无 wandb URL，说明未初始化 W&B 或被 kill 前未来得及连接） |
| **数据可用性** | **不可用于 rebuttal reserve**，训练未达到有意义进度 |

### exp_walker_008d_s6

| 项目 | 结果 |
|------|------|
| **失败原因** | 同上，SIGTERM 批量 kill |
| **训练进度** | 仅到 **step 8000** |
| **105K 评估数据** | **无**。唯一 eval 在 step 5000：eval_return=31.1 |
| **W&B** | **无** |
| **数据可用性** | **不可用于 rebuttal reserve** |

### Kill 原因分析

时间线：
- `exp_cheetah_008a_s3.log` 正常完成于 07:09（27KB，完整训练）
- `exp_walker_008d_s6/s7` 启动约 07:10，被 kill 于 07:20
- 两个进程**同时被杀**，排除 OOM（OOM 通常只杀一个）

最可能原因：**调度系统或手动批量 kill**——可能是启动新一批实验时清理了旧进程，或 AutoDL 实例到期/重启。`dmesg` 受限无法直接确认，但日志特征高度一致。

### 建议

**需要重跑。** 这两个实验完全没有可用数据（step 8000 远未收敛）。如果 Walker 008d seed 6/7 是 D172 Tier 2 rebuttal reserve 所需，需重新提交。考虑到 CoRL DDL 是 UTC 5/28 12:00，距现在不足 5 小时，需立即决定是否值得重跑（Walker 完整训练约需 4-6 小时）。

---
