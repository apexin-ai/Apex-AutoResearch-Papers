# monitoring 1 7b seed456 progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_1_7b_seed456_progress_20260520T164713_result.json`
- **Structured JSON:** [`0d5382b7514104c3f168.json`](../../sessions/0d/0d5382b7514104c3f168.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

### Uniform 1.7B seed456
| 指标 | 值 |
|------|-----|
| 进度 | **982 / 6103** (16%) |
| train_loss | 7.269 (step 980) |
| 训练速度 | 2.85 s/it |
| 已运行 | ~47 min |
| 剩余预估 | **~4h03m** |

### Adaptive 1.7B seed456
| 指标 | 值 |
|------|-----|
| 进度 | **931 / 6103** (15%) |
| train_loss | 9.725 (step 930) |
| 训练速度 | ~3.00 s/it |
| 已运行 | ~47 min |
| 剩余预估 | **~4h18m** |

### GPU 状态
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 0% | 0MiB / 97887MiB | **空闲，无进程** |
| cuda:1 | 0% | 0MiB / 97887MiB | **空闲，无进程** |
| cuda:2 | 100% | 61693MiB / 97887MiB | PID 494630 (uniform) |
| cuda:3 | 100% | 61693MiB / 97887MiB | PID 494711 (adaptive) |

### 注意
总 step 数是 **6103**，不是预期的 ~3052。可能 gradient_accumulation_steps=2 而非 4，或数据量是 400M tokens。两个任务预计还需 **~4-4.5 小时**完成。

---
