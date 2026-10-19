# check status ssh readonly

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_status-ssh-readonly_20260516T134324_result.json`
- **Structured JSON:** [`f1810e0689f4c48e0b52.json`](../../sessions/f1/f1810e0689f4c48e0b52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 项目 | 状态 |
|------|------|
| **V7 训练 (PID 960110)** | 已死。实际运行进程是 **PID 21363**（58 分钟），step **6100/20000**，1.8 steps/s |
| **V5 eval (PID 970634)** | 已死 |
| **GPU 0** | 100% 利用率，16.2 GiB / 97.9 GiB（V7 训练中） |
| **GPU 1 (cuda:1)** | **空闲**，0% 利用率，0 MiB 占用 |
| **V7 输出目录** | checkpoint-5000 已保存，config.json 存在 |

V7 预计还需 ~(20000-6100)/1.8/3600 ≈ **2.1 小时**完成。cuda:1 完全空闲可用。

---
