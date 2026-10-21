# infra reduce occ parallelism

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_reduce_occ_parallelism_20260520T112924_result.json`
- **Structured JSON:** [`277c983cf7e2007c25a4.json`](../../sessions/27/277c983cf7e2007c25a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整了。汇总报告：

---

## 结果

### Kill 操作
**已 kill 的 5 个进程**（进度最少）：
| PID | task_id | 文件大小 |
|------|---------|---------|
| 104227 | 1 | 2.73MB |
| 104231 | 5 | 2.72MB |
| 104232 | 6 | 2.85MB |
| 104233 | 7 | 2.69MB |
| 104235 | 9 | 2.79MB |

### 保留的 5 个进程
| PID | task_id | 已完成 demo | 剩余 |
|------|---------|-----------|------|
| 104226 | 0 | 1/50 | 49 |
| 104228 | 2 | 35/50 | 15 |
| 104229 | 3 | 40/50 | 10 |
| 104230 | 4 | 0/50 | 50 |
| 104234 | 8 | 36/50 | 14 |

### 速度对比
| 指标 | Kill 前 (10进程) | Kill 后 (5进程) |
|------|---------------|---------------|
| 帧速度 | ~1750 ms/frame | ~1430 ms/frame |
| CPU/进程 | ~430-460% | ~431-467% |
| **提速** | — | **~18%** |

提速幅度有限，因为机器有 208 核，10 进程时 CPU 就不是瓶颈。瓶颈可能是内存带宽/L3 cache 争抢。

### 预估完成时间（按 1430 ms/frame）
| task_id | 剩余 demo | 帧/demo | 预计耗时 |
|---------|----------|---------|---------|
| 0 | 49 | ~98 | ~1.9h |
| 2 | 15 | ~103 | ~37min |
| 3 | 10 | ~100 | ~24min |
| 4 | 50 | ~153 | **~3.0h**（瓶颈） |
| 8 | 14 | ~115 | ~38min |

**整体瓶颈是 task 4**（153 帧/demo 且刚开始），预计还需 ~3 小时完成。Tasks 2/3/8 约 30-40 分钟内完成。

被 kill 的 5 个 task（1/5/6/7/9）需要后续重新启动。其 HDF5 输出文件可能因进程中断而损坏，建议重跑时用 `"w"` 模式覆盖。

---
