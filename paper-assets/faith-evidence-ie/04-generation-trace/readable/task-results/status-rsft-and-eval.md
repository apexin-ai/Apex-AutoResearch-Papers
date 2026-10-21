# status rsft and eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_rsft-and-eval_20260515T010836_result.json`
- **Structured JSON:** [`0ceedc81354fdc9a017c.json`](../../sessions/0c/0ceedc81354fdc9a017c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### 1. mvp2_eval_lr5e6_r1_ckpt100 (cuda:3)
| 项目 | 状态 |
|------|------|
| 进程 | PID 117635 存活，已运行 1h29m |
| GPU | 11,243 MiB，利用率 82% |
| 进度 | **56/62 batches = 90%** |
| 速度 | ~96s/batch |
| 预计完成 | **~10 分钟后**（剩余 6 batches × 96s ≈ 576s） |
| 输出目录 | `lr5e6_r1_ckpt100/checkpoint-100/` 已创建，推理完成后写入结果 |

### 2. mvp2_rsft_generate (cuda:1)
| 项目 | 状态 |
|------|------|
| 进程 | PID 122144 存活，已运行 59m |
| GPU | 23,195 MiB，利用率 83% |
| 进度 | **110/1514 batches = 7.3%**（1,744/24,424 行） |
| 速度 | ~33s/batch（波动 25-39s） |
| 预计完成 | **~12.9 小时后** |
| 质量监控 | format_ok 99.8%，truncation 9.9%，diversity 1.0/8 |

### 3. GPU 空闲状态
| GPU | 状态 |
|-----|------|
| cuda:0 | **未空闲** — PID 90085 占用 13,636 MiB，利用率 57% |
| cuda:2 | 空闲（0 MiB，0%） |

注意：cuda:0 有未知进程 PID 90085 在运行，不属于这两个实验。

---
