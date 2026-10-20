# monitor westd progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-progress-check_20260515T221223_result.json`
- **Structured JSON:** [`7376147aff15cea86a4c.json`](../../sessions/73/7376147aff15cea86a4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态总览 (2026-05-16 06:12 UTC)

### 1. cwm8b-ckpt400-test-eval (PID 381618)
| 项目 | 状态 |
|------|------|
| PID | **ALIVE** (运行 7h34m, CPU 100%) |
| 进度 | **4248/9784 = 43.4%** |
| Accuracy | running_acc = **64.8%** |
| 速度 | ~8.4 samples/min |
| 剩余 | 5536 samples → **~11h** |
| ETA | ~17:12 UTC (May 16) |
| GPU | GPU 3: 22527/32607 MiB (88%) |
| JSONL | 4256 行 (与日志一致) |

### 2. cls8b-s42-resume-val-sweep-seq8192-v2 (PID 398981)
| 项目 | 状态 |
|------|------|
| PID | **ALIVE** (运行 4h30m) |
| 当前 ckpt | **checkpoint-3800** (第 11/21 个) |
| ckpt 内进度 | 2770/9335 = 29.7% |
| 总体进度 | **~49.0%** (10 完成 + 当前 29.7%) |
| Accuracy | running_acc = **90.1%** (当前 ckpt) |
| 速度 | ~5.8 samples/sec (~23 min/ckpt) |
| 剩余 | 当前 ckpt ~19min + 10 个 ckpt → **~4.8h** |
| ETA | ~11:00 UTC |
| GPU | GPU 0: 18477/32607 MiB (76%) |

### 3. repo-level-cwm-8b-conda-v5 (PID 400279)
| 项目 | 状态 |
|------|------|
| PID | **ALIVE** (运行 4h20m) |
| 进度 | **5888/6633 = 88.8%** (epoch 2.58) |
| Loss | eval_loss = **0.5152** (step 5800) |
| 速度 | ~12.1s/step |
| 最新 ckpt | checkpoint-5800 (05:54 保存) |
| 剩余 | 745 steps → **~2.5h** |
| ETA | ~08:42 UTC |
| GPU | GPU 2: 21057/32607 MiB (98%) |

### 4. cls8b-s42-resume-val-sweep-gpu1 (PID 405526)
| 项目 | 状态 |
|------|------|
| PID | **ALIVE** (运行 3h25m) |
| 当前 ckpt | **checkpoint-5600** (第 9/10 个) |
| ckpt 内进度 | 8880/9335 = 95.1% |
| 总体进度 | **~89.5%** (8 完成 + 当前 95.1%) |
| Accuracy | running_acc = **88.5%** (当前 ckpt) |
| 剩余 | ~1min 完成当前 + 1 个 ckpt (~23min) → **~24min** |
| ETA | ~06:37 UTC |
| GPU | GPU 1: 18477/32607 MiB (92%) |

### GPU 总览
| GPU | 利用率 | 显存 | 对应实验 |
|-----|--------|------|----------|
| 0 | 76% | 18477/32607 MiB (57%) | val-sweep-seq8192-v2 |
| 1 | 92% | 18477/32607 MiB (57%) | val-sweep-gpu1 |
| 2 | 98% | 21057/32607 MiB (65%) | CWM 训练 |
| 3 | 88% | 22527/32607 MiB (69%) | CWM eval |

**4 个进程全部存活，4 张 5090 满载。** 最快完成的是 exp 4 (~24min)，其次 exp 3 (~2.5h)。exp 2 和 exp 1 分别还需 ~5h 和 ~11h。

---
