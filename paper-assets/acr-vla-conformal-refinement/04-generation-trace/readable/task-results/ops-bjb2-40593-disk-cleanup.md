# ops bjb2 40593 disk cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-40593-disk-cleanup_20260519T140143_result.json`
- **Structured JSON:** [`2e6db4568adb59e56183.json`](../../sessions/2e/2e6db4568adb59e56183.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘清理报告 — bjb2-40593

### 结论：磁盘不需要清理，Director 看到的 90% 是宿主机磁盘，我们无法控制

### 磁盘实际状态

| 分区 | 设备 | 总量 | 已用 | 使用率 | 性质 |
|------|------|------|------|--------|------|
| 根分区 (overlay) | overlay | 30G | 8.9G | **30%** | 容器可写层 |
| 数据盘 | /dev/md0 | 250G | 99G | **40%** | autodl-tmp |
| 宿主机系统盘 | /dev/sda2 | 437G | 369G | **89%** | 只读挂载，不可清理 |

**Director 看到的 89% 是 `/dev/sda2`** — 这是 AutoDL 宿主机的系统盘，以只读方式 bind-mount 进容器（仅挂载 NVIDIA 驱动库文件）。我们无法写入也无法清理。

### 已执行的清理
- conda cache: 已清空（之前就是空的）
- pip cache: 无缓存
- `__pycache__` / `.pyc`: 已清理（量极小）

### 空间大户（autodl-tmp, 99G/250G）

| 路径 | 大小 | 状态 |
|------|------|------|
| libero_data/ | 94G | 运行中实验依赖，**不可删** |
| .hf_cache/ | 2.8G | 运行中实验依赖（HF_HUB_OFFLINE=1），**不可删** |
| models/ | 1.8G | 可能与 .hf_cache 重复，需确认后可清理 |
| checkpoints/ | 86M | 运行中实验依赖，**不可删** |

### 当前运行中的实验（3个）
1. `eval-random-selection-object-seed46` — PID 503784, 9.7GB RSS
2. `eval-obs-only-spatial-norm02-seed43` — PID 508930, 8.5GB RSS
3. `eval-scalar-seed45-r2` — tmux session（Python 进程可能已完成）

### 结论
- **无法将 sda2 降到 <70%** — 宿主机盘只读，360G+ 为系统/Docker 层占用
- **我们可控的两个分区都很健康**（30% 和 40%）
- 数据盘有 **152G 空闲**，完全可以部署新实验
- 如果 Director 需要进一步释放 autodl-tmp 空间，可考虑删除 `models/` 目录（~1.8G，需确认无直接引用后）

---
