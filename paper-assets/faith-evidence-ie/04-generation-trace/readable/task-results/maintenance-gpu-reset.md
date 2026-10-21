# maintenance gpu reset

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_gpu-reset_20260520T083015_result.json`
- **Structured JSON:** [`f7832fa193eecfc1a968.json`](../../sessions/f7/f7832fa193eecfc1a968.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 结果汇总

| 项目 | 结果 |
|------|------|
| **GPU reset** | **失败** — `nvidia-smi --gpu-reset` 不支持 RTX 5090 硬件。cuda:2/3 显存已空（0 MiB）但 GPU-Util 卡在 100%，`/dev/nvidia2` 设备节点不存在。需要通过 AutoDL 控制台重启实例才能恢复。 |
| **进度汇报脚本** | 已部署，PID **6660**，每 30 分钟写入 `/tmp/rsync_progress.log` |
| **当前 rsync 状态** | **6 个 rsync 进程活跃**，已传输 **14G / 350G (4%)**  |

---
