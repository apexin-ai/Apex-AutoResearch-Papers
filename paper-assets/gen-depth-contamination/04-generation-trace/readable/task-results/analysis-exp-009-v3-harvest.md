# analysis exp 009 v3 harvest

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_009_v3_harvest_20260517T050332_result.json`
- **Structured JSON:** [`dd9d1951f891c13d1ba7.json`](../../sessions/dd/dd9d1951f891c13d1ba7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 进程状态
| 实验 | PID | GPU | 状态 |
|------|-----|-----|------|
| exp_009_dose_10pct_v3 | 93385 | cuda:1 | 运行中 (4h50m) |
| exp_009_dose_30pct_v3 | 93527 | cuda:2 | 运行中 (4h50m) |
| exp_009_dose_50pct_v3 | 93604 | cuda:3 | 运行中 (4h50m) |

### 进度详情

每个实验 = 5 seeds × 3 strategies = 15 个 train+eval 周期

| 实验 | 已完成 | 当前任务 | 进度 |
|------|--------|----------|------|
| 10pct (ratio=0.1) | 11/15 | seed3 graduated 训练中 (20%) | 73% |
| 30pct (ratio=0.3) | 10/15 | seed3 binary_ours 评估中 (loglikelihood 60%) | 70% |
| 50pct (ratio=0.5) | 10/15 | seed3 binary_ours 评估中 (HellaSwag tokenize 65%) | 70% |

### 时间估算
- 每个 train+eval 周期 ≈ 27-30 min
- 10pct 剩余: ~4 个周期 ≈ **1h 50m**
- 30pct 剩余: ~4.4 个周期 ≈ **2h 10m**
- 50pct 剩余: ~4.5 个周期 ≈ **2h 15m**
- **预计全部完成时间: ~2h 15m 后 (约 UTC 15:20)**

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 0% | 0 / 24564 MiB (空闲) |
| cuda:1 | 97% | 21079 / 24564 MiB (10pct 训练中) |
| cuda:2 | 100% | 17615 / 24564 MiB (30pct eval loglikelihood) |
| cuda:3 | 0% | 3517 / 24564 MiB (50pct CPU tokenize阶段，GPU 等待) |

### 异常
无 OOM 或 crash。cuda:3 当前 0% 利用率是正常的，50pct 实验正在 HellaSwag tokenize (CPU-bound)，tokenize 完成后 GPU 会恢复满载。

---
