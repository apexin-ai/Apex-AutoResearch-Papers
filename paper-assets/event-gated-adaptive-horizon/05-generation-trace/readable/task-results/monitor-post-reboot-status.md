# monitor post reboot status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_post-reboot-status_20260516T063826_result.json`
- **Structured JSON:** [`dfadbce9c2a305178a71.json`](../../sessions/df/dfadbce9c2a305178a71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 状态
| GPU | 型号 | 显存占用 | GPU利用率 |
|-----|------|---------|----------|
| 0 | RTX PRO 6000 (98GB) | 4.2GB | 10% |
| 1 | RTX PRO 6000 (98GB) | 4.7GB | 22% |

两块 GPU 上各有一个 python 进程 (PID 149708 / 536895)，均含 "dreamer" 关键字，**两个实验都在跑**。

---

### exp_009d — Walker Baseline (cuda:0)
| 指标 | 值 |
|------|-----|
| 当前 step | **436K / 500K** (87.2%) |
| 最新 train_return | ~858–974 (波动) |
| 最新 eval_return | **911.9** @ 428K |
| 峰值 eval_return | **950.96** @ 398K |
| 状态 | **RUNNING** |
| 上次检查 | 344K → 现在 436K，+92K |
| 预计完成 | 剩余 64K steps，按近期速度约 **4-6 小时** |

---

### exp_010a — Cheetah Baseline (cuda:1)
| 指标 | 值 |
|------|-----|
| 当前 step | **312K / 512K** (60.9%) |
| 最新 train_return | ~627–725 |
| 最新 eval_return | **657.9** @ 305K |
| 峰值 eval_return | **732.9** @ 265K |
| 状态 | **RUNNING** |
| 上次检查 | 165K → 现在 312K，+147K |
| 预计完成 | 剩余 200K steps，按近期速度约 **12-16 小时** |

两个实验均正常运行，服务器重启后进程存活。

---
