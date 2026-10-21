# check exp006 progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp006_progress_20260514T013847_result.json`
- **Structured JSON:** [`79cd4f7a7961e1b8edb7.json`](../../sessions/79/79cd4f7a7961e1b8edb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-006 Graduated Filtering 进度报告

### 状态：运行中
- **PID 46129** 存活，已运行 **4h36m**
- 当前训练：`binary-ours_s123`，步数 760/2814 (27%)

### 进度
| 策略 | 完成 | 总数 |
|------|------|------|
| no-filter | 5/5 | ✓ |
| binary-ours | 1/5 | s123 训练中 |
| binary-drayson | 0/5 | 待开始 |
| graduated | 0/25 | 5α × 5 seeds |
| surprisal | 0/5 | 待开始 |
| dsir | 0/5 | 待开始 |
| **总计** | **6/50** | **12%** |

### 已完成结果

| Run | MMLU | HellaSwag (norm) | MMLU Δ | HS Δ |
|-----|------|-----------------|--------|------|
| base_model | 0.6018 | 0.6821 | — | — |
| **no-filter 均值** | **0.5865** | **0.6637** | **-1.53pp** | **-1.84pp** |
| no-filter_s42 | 0.5883 | 0.6633 | -1.35 | -1.88 |
| no-filter_s123 | 0.5854 | 0.6636 | -1.64 | -1.85 |
| no-filter_s456 | 0.5863 | 0.6626 | -1.55 | -1.95 |
| no-filter_s789 | 0.5867 | 0.6646 | -1.51 | -1.75 |
| no-filter_s1024 | 0.5856 | 0.6646 | -1.62 | -1.75 |
| **binary-ours_s42** | **0.5945** | **0.6701** | **-0.73pp** | **-1.20pp** |

### 初步观察
- **binary-ours 比 no-filter 保留了更多能力**：MMLU 降幅 0.73pp vs 1.53pp，HellaSwag 降幅 1.20pp vs 1.84pp
- no-filter 跨 seed 方差很小（MMLU σ≈0.001），结果稳定

### ETA
- 平均 ~44 min/run，剩余 44 runs
- **预计还需 ~32 小时**，约 **5月15日 17:30** 完成

---
