# fix disk and exp012 gpu

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_disk_and_exp012_gpu_20260522T000404_result.json`
- **Structured JSON:** [`11f7654cc889dcd71ffa.json`](../../sessions/11/11f7654cc889dcd71ffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 子任务 1: 磁盘清理

| 项目 | 清理量 |
|------|--------|
| Llama-3.3-70B-Instruct-AWQ 下载缓存 | ~14 GB（不完整下载，已 kill 进程） |
| pip 缓存 | 4.3 GB |
| conda 缓存 | 154 KB |

**清理前**: 14G used / 17G free (46%)  
**清理后**: 9.6G used / 21G free (32%)  
**释放**: ~8.4G

磁盘空间充裕，不需要扩容。

### 子任务 2: exp-012 GPU 状态

**exp-012 已经在 GPU 1 上运行**，无需切换：
- PID: 54823
- GPU 显存: 73584 MiB / 97887 MiB
- GPU 利用率: 64%
- 当前进度: error_propagation.csv 已有 21 行

GPU 0 运行 exp-009 (PID 70789, 73556MiB)，GPU 2/3 空闲。

---
