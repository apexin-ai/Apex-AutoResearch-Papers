# ssh eval status check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-status-check_20260517T150201_result.json`
- **Structured JSON:** [`9c562d192d4e27ed1b2f.json`](../../sessions/9c/9c562d192d4e27ed1b2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v7.2 Eval 状态汇总

### PID 存活
| 进程 | PID | 状态 | CPU 时间 |
|------|-----|------|----------|
| alpha=0.0 | 40598 | **Rl (running)** | 2068 min |
| alpha=1.0 | 44022 | **Rl (running)** | 2025 min |

### GPU 占用
| GPU | 显存占用 |
|-----|----------|
| 0 | 2782 MiB / 97253 MiB |
| 1 | 2203 MiB / 97252 MiB |

### 当前进度

两个进程都仍在 **第 1 个 suite: `libero_spatial`**（共 4 个 suite: spatial, object, goal, 10）

| 条件 | 已完成 task/episode | 当前 rollout | 当前 suite 进度 |
|------|-------------------|-------------|----------------|
| alpha=0.0 | task 0-8 done (90 eps) | task_9 ep_0, 31%/280 steps | ~90/100 |
| alpha=1.0 | task 0-7 done (80 eps) + task_8 5/10 eps | task_8 ep_5, 82%/280 steps | ~85/100 |

### 总体进度估算
- alpha=0.0: ~90/400 episodes ≈ **22.5%**
- alpha=1.0: ~85/400 episodes ≈ **21.3%**

### Suite 级结果
尚无。第一个 suite (`libero_spatial`) 未完成，无汇总 JSON 输出。

### 状态
正常运行，无崩溃，无 error。`running_success_rate=0.0%` 是当前单个 rollout 的实时指标（还在跑 steps），不是最终结果。

---
