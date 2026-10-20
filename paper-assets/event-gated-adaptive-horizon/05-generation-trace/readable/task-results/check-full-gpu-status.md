# check full gpu status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full_gpu_status_20260525T143308_result.json`
- **Structured JSON:** [`9fe9829bcc6a71d5faed.json`](../../sessions/9f/9fe9829bcc6a71d5faed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

### bjb1-45299
| GPU | 型号 | 显存占用 | GPU-Util | 进程 |
|-----|------|---------|----------|------|
| 0 | RTX PRO 6000 (98GB) | 5742MiB | 22% | 3个python进程 (PID 283095, 283930, 285954) |
| 1 | RTX PRO 6000 (98GB) | 6916MiB | 97% | 2个python进程 (PID 283095, 283930) |

### westd-19154
| GPU | 型号 | 显存占用 | GPU-Util | 进程 |
|-----|------|---------|----------|------|
| 0 | RTX PRO 6000 (98GB) | 3242MiB | 4% | 1个python进程 (PID 29484) |
| 1 | RTX PRO 6000 (98GB) | 4656MiB | 16% | 1个python进程 (PID 30586) |

## 实验状态

| exp_id | server | current_step | target | progress | FPS | ETA |
|--------|--------|-------------|--------|----------|-----|-----|
| exp_080 (walker_s1) | bjb1 | 80000 | 105K | 76.2% | 7.1 | ~59 min |
| exp_081 (walker_s2) | bjb1 | 80000 | 105K | 76.2% | 8.9 | ~47 min |
| exp_082 (cheetah_no_dt_emb_s0) | westd | 25000 | 105K | 23.8% | 15.0 | ~89 min |
| exp_083 (cheetah_baseline_s1) | westd | 8000 | 105K | 7.6% | ~13* | ~124 min |

\* exp_083 仅有 step 5000 的初始 fps=0.0，按同环境 exp_078 的 ~13 fps 估算。

## exp_078 状态
- **已结束**，EXIT_CODE=0
- 最终 step: 112000（超过目标 105K 后正常退出）
- step 105000 eval_return: **119.5**
- step 105000 ve_ratio: **0.3**, delta_ve: -1.1, civo_alert: **0.0**
- step 95000 eval_return: 32.5（对比 105K 的 119.5，最后阶段有明显提升）

## 异常
- **westd GPU 利用率偏低**：GPU 0 仅 4%（exp_082 正在 eval 阶段，属正常波动），GPU 1 仅 16%（exp_083 处于早期阶段）
- **bjb1 GPU 0 有 3 个 python 进程**（PID 285954 使用 4673MiB），exp_080/081 之外可能还有一个额外进程占用 GPU 0

---
