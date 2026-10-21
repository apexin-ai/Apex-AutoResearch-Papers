# ops pythia14b rerun status check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pythia14b_rerun_status_check_20260521T140727_result.json`
- **Structured JSON:** [`159c29fb8eb6a819ec47.json`](../../sessions/15/159c29fb8eb6a819ec47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### PID 状态
- **PID 422244**：已死
- **PID 421716**：存活，正在运行同一 Pythia-1.4B C4 rerun pipeline（已运行 219 分钟 CPU time）。但从结果文件时间戳看，pipeline 的分析阶段（feature extraction + classification）已于 22:05 完成，当前进程可能停留在某个收尾步骤

### 数据完整性 — 全部完成
| 文件 | 行数 |
|------|------|
| depth_0.jsonl | 5000 |
| depth_1.jsonl | 5000 |
| depth_2.jsonl | 5000 |
| depth_3.jsonl | 5000 |
| depth_4.jsonl | 5000 |
| depth_5.jsonl | 5000 |
| features.csv | 已生成 (7.9MB) |

### AUC 结果 — 全部完成
| 对比 | AUC | 标准差 |
|------|-----|--------|
| 0 vs 1 | **0.9979** | ±0.0006 |
| 1 vs 2 | **0.8786** | ±0.0041 |
| 2 vs 3 | 0.5399 | ±0.0122 |
| 3 vs 4 | 0.5062 | ±0.0104 |
| 4 vs 5 | 0.5025 | ±0.0081 |

**K\* = 2**（最大 AUC > 0.60 的 depth）

### JSD
| 对比 | JSD |
|------|-----|
| 0 vs 1 | 0.5844 |
| 1 vs 2 | 0.0718 |
| 2 vs 3 | 0.0041 |
| 3 vs 4 | 0.0027 |
| 4 vs 5 | 0.0024 |

### Ordinal Classification
- MAE = 0.9901, Accuracy = 0.4407

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 9021 MiB | 37% ← Pythia-6.9B nuc 实验 (PID 438362) |
| 1 | 0 MiB | 0% |
| 2 | 4035 MiB | 0% ← Pythia-1.4B rerun (PID 421716) |
| 3 | 0 MiB | 0% |

### 结论
Pythia-1.4B C4 rerun **pipeline 已完成**，所有 6 个 depth 文件 + features + 全部结果文件均已生成。PID 421716 仍驻留但 GPU 利用率 0%，可能处于空转状态。另外 GPU0 正在跑 Pythia-6.9B nucleus sampling 实验 (PID 438362)。无需恢复任何任务。

---
