# ops server maintenance 0514

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-maintenance-0514_20260514T061653_result.json`
- **Structured JSON:** [`fd9baece01d361fadc92.json`](../../sessions/fd/fd9baece01d361fadc92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 维护结果汇报

### 磁盘空间
| 分区 | 清理前 | 清理后 |
|------|--------|--------|
| /root/autodl-tmp | 109G/250G (142G free) | 64G/250G (187G free) |
| / (root) | 8.1G/30G (22G free) | 不变 |

释放 **45GB**，接近50GB目标。

### 清理的目录
| 目录 | 大小 | 实验 | 原因 |
|------|------|------|------|
| `grpo_exec_only/` | 15G | sta-phase1-exec-only-r4/r5 | 早期100步实验，已被500步取代 |
| `grpo_exec_sta/` | 15G | sta-phase1-exec-sta-r4/r5 | 早期100步实验，conclusion=negative |
| `plan005_sta_low_s42/` | 15G | plan005-sta-low-s42 | conclusion=negative |

任务提到的 `plan001_s43_r4` 和 `plan001_s44` 已在之前清理过，不再存在。

### 残留进程
- **PID 261641** (plan017 eval_sta): 已不存在，无需处理
- GPU 上无残留占用（nvidia-smi 仅显示两个 RUNNING 实验的进程）

### RUNNING 实验状态
| 实验 | PID | GPU | 进度 | prove_rate | 状态 |
|------|-----|-----|------|-----------|------|
| plan002-additive-b01-s42 | 262261→262266 | cuda:0 (79.6G) | step 366/500 | 0.625 | 正常 |
| plan016-extended-1000-s42 | 263273 | cuda:1 (80.3G) | step 266/1000 | 0.875 | 正常 |

---
