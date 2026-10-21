# code check 3 experiments eta

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_3_experiments_eta_20260522T202459_result.json`
- **Structured JSON:** [`298d2689ea3ff77c91fb.json`](../../sessions/29/298d2689ea3ff77c91fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

当前服务器时间约 CST 04:25 (UTC 20:25)

### 1. seed_gemma27b_c4_s42 (cuda:0, PID 26893)
| 指标 | 值 |
|------|-----|
| 状态 | RUNNING (10h21m) |
| 当前 depth | **depth 5 / 5** (最后一个 depth) |
| 当前 batch | 137/625 (**22%**) |
| 速度 | ~14.14 s/it |
| 已完成 | depth_0–depth_4 各 5000 行 |
| 整体进度 | **~84%** (4/5 generation depths + 22% of depth 5) |
| depth 5 剩余 | 488 batches × 14.14s ≈ **1h55m** |
| 生成完成 ETA | ~CST 06:20 / **UTC 22:20** |
| GPU 显存 | 53,375 MiB, 93% util |
| 异常 | 无 |

### 2. exp_gemma2b_10k (cuda:3, PID 54709)
| 指标 | 值 |
|------|-----|
| 状态 | RUNNING (2h27m) |
| 当前 depth | **depth 3 / 5** |
| 当前 batch | 427/625 (**68%**) |
| 速度 | ~5.25 s/it |
| 已完成 | depth_0–depth_2 各 10,000 行 |
| 整体进度 | **~54%** (2/5 + 68% of depth 3) |
| 剩余 | depth 3: ~17min + depth 4: ~55min + depth 5: ~55min ≈ **2h7m** |
| 生成完成 ETA | ~CST 06:32 / **UTC 22:32** |
| GPU 显存 | 6,381 MiB, 57% util |
| 异常 | 无 |

### 3. exp_olmo1b_10k (cuda:2, PID 66415)
| 指标 | 值 |
|------|-----|
| 状态 | RUNNING (18min) |
| 当前 depth | **depth 2 / 5** |
| 当前 batch | 201/313 (**64%**) |
| 速度 | ~2.29 s/it |
| 已完成 | depth_0–depth_1 各 10,000 行 |
| 整体进度 | **~33%** (1/5 + 64% of depth 2) |
| 剩余 | depth 2: ~4min + depths 3–5: ~36min ≈ **40min** |
| 生成完成 ETA | ~CST 05:05 / **UTC 21:05** |
| GPU 显存 | 3,977 MiB, 63% util |
| 异常 | 无 |

### GPU 总览
| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 53,375 MiB | 93% | gemma-2-27b |
| 1 | 0 MiB | 0% | 空闲 |
| 2 | 3,977 MiB | 63% | OLMo-1B |
| 3 | 6,381 MiB | 57% | gemma-2-2b |

三个实验均正常运行，无报错。OLMo-1B 最先完成（~40min），Gemma-27B 和 Gemma-2B 大致同时完成（~2h 后）。注意以上 ETA 仅为生成阶段，pipeline 后续可能还有 feature extraction / scoring 阶段。

---
