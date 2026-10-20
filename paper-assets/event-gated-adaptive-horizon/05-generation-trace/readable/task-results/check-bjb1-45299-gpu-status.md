# check bjb1 45299 gpu status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-45299-gpu-status_20260523T034221_result.json`
- **Structured JSON:** [`532521977d4e7cc30aa1.json`](../../sessions/53/532521977d4e7cc30aa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### exp_049_stackcube_civo_trigger_s0
| 项目 | 状态 |
|------|------|
| PID | 91395 **ALIVE**，运行 10h51m |
| GPU | cuda:0 (643MiB) + cuda:1 (2758MiB) |
| 当前步数 | **210,200**（已超过 210K 目标，仍在运行） |
| train_return | 最近: 19.5 → 25.3 → 39.2 → 25.4 → 47.5 |
| eval_return | 202.5K = 23.75（峰值 182.5K = 35.89） |

**ve_ratio 趋势（82.5K 之后）：**

| step | ve_ratio |
|------|----------|
| 82.5K | 1.353 ← 上次关注点 |
| 92.5K | 1.313 |
| 102.5K | 1.462 |
| 112.5K | **0.505** ← 显著下降 |
| 122.5K | 0.480 |
| 132.5K | 0.548 |
| 142.5K | 0.348 |
| 152.5K | 0.478 |
| 162.5K | 0.296 |
| 172.5K | 0.315 |
| 182.5K | 0.185 |
| 192.5K | 0.275 |
| 202.5K | **0.267** |

ve_ratio 从 102.5K 的 1.46 骤降到 112.5K 的 0.51，之后稳定在 0.18-0.55 区间，持续走低。

---

### exp_052_stackcube_civo_trigger_s1
| 项目 | 状态 |
|------|------|
| PID | 103781 **ALIVE**，运行 6h14m |
| GPU | cuda:0 (2849MiB) |
| 当前步数 | **136,600** |
| train_return | 最近: 21.8 → 27.5 → 15.5 → 31.2 → 26.4 |
| eval_return | 132.5K = 33.51（当前最佳） |

---

### exp_048_cheetah_civo_extension
| 项目 | 状态 |
|------|------|
| PID | 88654 **DEAD**（符合预期，已标记 DONE） |

---

**总结**：两个活跃实验进程在服务器重启后均存活，正常运行。exp_049 已超过 210K 步目标仍在继续（可能在做最后的 eval/checkpoint）；exp_052 在 136.6K 步正常推进。exp_049 的 ve_ratio 在 112.5K 后大幅收敛至 0.2-0.5 区间。

---
