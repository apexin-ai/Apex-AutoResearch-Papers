# ops gpu utilization check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-utilization-check_20260516T184756_result.json`
- **Structured JSON:** [`4d0803265f6ccac64805.json`](../../sessions/4d/4d0803265f6ccac64805.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**状态：正常运行，无异常。**

### 进程状态
| | PID | GPU | 当前进度 | 状态 |
|---|---|---|---|---|
| seed1 | 104743 | GPU 1 | libero_spatial 完成，正加载 libero_object | 正常 |
| seed2 | 111920 | GPU 0 | libero_spatial task 7, episode 6/10 | 正在写入 |

### GPU 利用率低的原因

**LIBERO eval 是 CPU-bound 任务，非 GPU 异常。** 物理仿真在 CPU 上运行（CPU 利用率 2254% = ~22 线程），GPU 仅在 policy inference step 短暂调用。3.2GB VRAM = 模型已加载，但大部分时间空闲等待 CPU 端仿真完成下一个 observation。

这是 LIBERO 评估的**正常行为模式**。

### 进度估算
- 每个 suite: 8 tasks × 10 episodes = 80 episodes
- 4 suites 共 320 episodes/seed
- libero_spatial 耗时 ~78 min → 总计约 **5-6 小时/seed**
- 当前进度: ~25%（suite 1/4）
- 预计完成时间: ~07:00-08:00 (UTC+8)

### 无需干预
不需要任何操作。seed1 的 5 分钟静默是正在加载下一个 LIBERO 环境（libero_object），属正常初始化延迟。

---
