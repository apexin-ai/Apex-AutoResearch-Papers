# diag gpu and baseline status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_and_baseline_status_20260516T005841_result.json`
- **Structured JSON:** [`d935d38c18a70b8ca385.json`](../../sessions/d9/d935d38c18a70b8ca385.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 进程状态
| PID | 状态 | 运行时间 | 当前任务 |
|-----|------|---------|---------|
| 471056 (baseline_plus) | **存活** | 1h44m | libero_goal |
| 508625 (baseline_std) | **存活** | 1h23m | libero_goal |

### GPU 占用
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 2140 MiB / 97887 MiB (2.2%) | 1% |
| cuda:1 | 3068 MiB / 97887 MiB (3.1%) | 0% |

GPU 利用率极低是正常的——eval 推理是 batch_size=1 的序列执行，大部分时间在环境模拟而非 GPU 计算。

### 已完成 Suite 的 Success Rate

| | libero_spatial | libero_object | libero_goal |
|---|---|---|---|
| **baseline_plus** (smolvla_libero_plus) | 408/500 = **81.6%** | 444/500 = **88.8%** | 进行中 |
| **baseline_std** (smolvla_libero) | 330/500 = **66.0%** | 339/500 = **67.8%** | 进行中 |

### 完成情况
- **已完成**: spatial, object（两个 baseline 都完成）
- **进行中**: goal（两个 baseline 都在跑）
- **未开始**: long_horizon（如有计划的话）

### 备注
- 实际输出目录是 `baseline_plus_v2`（不是 v3），`baseline_std_v3` 正确
- baseline_plus 在 spatial 和 object 上都显著优于 baseline_std（+15.6% 和 +21.0%）

---
