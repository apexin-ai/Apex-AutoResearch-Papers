# ops check 009d progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-009d-progress_20260516T013958_result.json`
- **Structured JSON:** [`1ccfad648e7d2164e641.json`](../../sessions/1c/1ccfad648e7d2164e641.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### exp_009d_baseline_walker_s0
| 项目 | 值 |
|------|-----|
| 状态 | **RUNNING** |
| PID | 149708（已运行 13h15m） |
| 进度 | 312K / 500K（62.4%） |
| FPS | 7.24 |
| 预计剩余 | ~7.2 小时 |
| 最新 eval_return | **925.86**（step 308K） |
| 最新 value_mean | 628.89 |

eval_return 趋势（近 8 个 checkpoint）：
```
238K: 765.9 → 248K: 733.6 → 258K: 758.2 → 268K: 704.9
278K: 802.2 → 288K: 845.7 → 298K: 913.3 → 308K: 925.9
```
持续上升，学习曲线健康。

---

### exp_010a_cheetah_baseline_s1
| 项目 | 值 |
|------|-----|
| 状态 | **RUNNING** |
| PID | 536890（已运行 2h52m） |
| 进度 | 116K / 512K（22.7%） |
| FPS | 11.63 |
| 最新 train_return | ~481–534 |

---

两个实验均正常运行，无需干预。009d 预计约 7 小时后完成（~今晚），届时再收集最终 metrics 并更新 registry。

---
