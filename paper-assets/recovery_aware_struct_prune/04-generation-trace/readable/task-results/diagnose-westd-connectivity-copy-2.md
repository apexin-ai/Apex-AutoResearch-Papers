# diagnose westd connectivity

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_connectivity_20260522T002148_result.json`
- **Structured JSON:** [`b0f89edf507008f7596d.json`](../../sessions/b0/b0f89edf507008f7596d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：westd-29022

| 项目 | 状态 |
|------|------|
| **连接状态** | **失败** |
| **错误信息** | `[Errno None] Unable to connect to port 29022 on 36.103.198.204` |
| **响应时间** | 0.36s（立即拒绝，非超时） |
| **实验进程** | 无法检查 |
| **日志** | 无法检查 |
| **GPU/磁盘** | 无法检查 |

### 判断

连接被立即拒绝（0.36s），说明端口 29022 未在监听。最可能的原因：

1. **AutoDL 实例已关机或重启，SSH 端口已变更**（最大概率）——AutoDL 重启后会分配新端口
2. 实例被释放

### 需要你做的

去 AutoDL 控制台查看 westd-29022 实例的当前状态：
- 如果实例还在运行：查看新的 SSH 端口，更新 `~/.ssh/config` 中 westd-29022 的端口配置
- 如果实例已关机：需要重新开机，开机后端口会变
- 如果实例已释放：需要新建实例

之前在该服务器上运行的实验（包括 PID 412817 的 eval_math500_grpo_alpha4_20 等）如果实例重启过，进程已全部丢失，需要重新启动。

---
