# ssh retry crash diagnosis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_retry-crash-diagnosis_20260518T053245_result.json`
- **Structured JSON:** [`40eb608fe4da194a5454.json`](../../sessions/40/40eb608fe4da194a5454.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因找到了。

## 诊断结果

### 崩溃原因：GPU 驱动被宿主机卸载/损坏

`/usr/bin/nvidia-smi` 是一个 **0 字节的空文件**（权限 0644，不可执行），最后修改时间 2026-05-17 19:35:26。这不是 OOM 或进程 kill，而是**云平台宿主机级别的 GPU 驱动异常**：
- `/dev/nvidia*` 设备节点完全消失
- `lsmod` 不存在（容器化环境），内核模块 `nvidia` 未加载
- 内核日志、syslog 均为空（容器内无权限查看宿主机 dmesg）
- 驱动版本文件 `/proc/driver/nvidia/version` 还在（595.58.03），但实际设备已不可用

这是 AutoDL 平台侧问题（GPU 热迁移/宿主机维护/驱动重装），非代码 bug。

### nvidia-smi 状态：**不可恢复**
容器内无法自行修复 GPU 驱动。需要平台侧操作（重启实例或重新分配 GPU）。

### 数据抢救
| Task | Episodes 完成 | 状态 |
|------|-------------|------|
| chemistry-mix | 20/20 | **完整** (ep000-ep019) |
| find-animal | 6/20 | **不完整** (ep000-ep005，ep006 正在跑时崩溃) |
| 剩余 8 个 task | 0/20 | 未开始 |

总计：**26/200 episodes** 已保存为 JSON 文件，数据可用。另外 `retry_dose_response_analysis.json` 包含之前 N=1 的完整 220 episode 分析结果。

### 能否重跑
**当前实例不可用**——GPU 已废。需要：
1. 在 AutoDL 控制台重启此实例（可能恢复 GPU）
2. 或开新实例，从已保存的 26 个 episode JSON 继续（跳过已完成的 chemistry-mix + find-animal 前 6 个 ep）

建议开新实例跑，当前实例的 GPU 状态不可信。

---
