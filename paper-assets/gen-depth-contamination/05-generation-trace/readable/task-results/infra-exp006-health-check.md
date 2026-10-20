# infra exp006 health check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006_health_check_20260513T205932_result.json`
- **Structured JSON:** [`8fd0b50ac94d18dfa637.json`](../../sessions/8f/8fd0b50ac94d18dfa637.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-006 状态：已终止

| 检查项 | 结果 |
|--------|------|
| **PID 44953** | 已死，进程不存在 |
| **GPU 利用率** | 0%，显存 0 MiB / 24564 MiB — GPU 完全空闲 |
| **tmux session** | tmux 命令被 read-only 限制，无法检查 |
| **残留进程** | 无任何 exp006 相关进程在运行 |
| **日志末尾** | 脚本在输出 MMLU 各科分数后，因 `bc: command not found` 失败，退出码 127 |

**根因**：`run_exp006.sh` 第 68 行调用了 `bc` 命令（可能用于计算平均分），但服务器上未安装 `bc`，导致脚本异常退出。

**修复**：安装 `bc`（`apt install bc`）或将脚本中的 `bc` 计算改为 `python3 -c` 实现，然后重新启动实验。

---
