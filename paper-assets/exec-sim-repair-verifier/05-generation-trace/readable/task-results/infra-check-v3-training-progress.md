# infra check v3 training progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-v3-training-progress_20260512T171024_result.json`
- **Structured JSON:** [`e3fdffaa0cb2a6b98183.json`](../../sessions/e3/e3fdffaa0cb2a6b98183.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

**两个实验均已死亡（SIGKILL, EXIT_CODE=137）。**

| 实验 | 实际 PID | 最后 Step | 进度 | 速度 | 训练时长 | 死因 |
|---|---|---|---|---|---|---|
| repo-level-cls-v3 | 69781 | **188/6633** | 2.8% | ~6.9s/it | ~22 min | SIGKILL (137) |
| repo-level-cwm-v3 | 69887 | **119/6633** | 1.8% | ~10.3s/it | ~21 min | SIGKILL (137) |

**GPU 状态**: 4 张 5090 全部空闲（0% 利用率，0 MiB 显存占用）。

**死因分析**: EXIT_CODE=137 = 128+9 (SIGKILL)。容器环境无 `/var/log/syslog` 或 `kern.log`，无法确认是否 OOM。可能原因：
1. **系统/容器内存上限触发 OOM killer**（两个进程几乎同时被杀，最可能）
2. 平台资源管控
3. 人工 kill

**日志时间线**:
- 训练开始: 2026-05-13 00:35~00:37 UTC
- 被杀时间: 约 00:58 UTC（日志最后修改时间）
- 存活约 22 分钟

需要重新启动训练。建议先检查系统内存 (`free -h`) 确认是否为内存不足导致，考虑错开两个实验或减小 batch size。

---
