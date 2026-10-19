# ops deep eval diagnostic

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deep-eval-diagnostic_20260516T173304_result.json`
- **Structured JSON:** [`ec999f93f999ff38c556.json`](../../sessions/ec/ec999f93f999ff38c556.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有完整画面了。日志揭示了关键信息。

## 诊断报告

### 1. 进程状态

| | PID 104743 (seed1) | PID 111920 (seed2) |
|---|---|---|
| 状态 | `R` (running) — **活跃** | `R` (running) — **活跃** |
| 物理 GPU | GPU 1 (CUDA_VISIBLE_DEVICES=1) | GPU 0 (CUDA_VISIBLE_DEVICES=0) |
| 进程 etime | 11h52m | 7h13m |
| Parent etime | 17h02m | 12h22m |
| RSS | 14.8 GB | 14.3 GB |
| Threads | 160 | 160 |

### 2. 真实时间线 — 极度异常

**seed1 的 eval 实际从 01:21:47 (May 17) 才开始，仅 ~17 分钟前。** 日志头部证实：

```
[ACIB-EVAL] checkpoint=... step=20000
[ACIB-EVAL] base_model=lerobot/smolvla_libero
[ACIB-EVAL] suites=['libero_spatial', ...]
```

时间分解：
- Parent bash 启动 → Python 启动：**5h10m**（conda 激活不应该这么久）
- Python 启动 → 首行 stdout：**11h35m**（`import torch` 或模块初始化卡住）
- 实际 eval 运行：**~17 min**

seed2 类似：run_info.json 创建于 01:26，实际 eval 仅运行 ~12 min。

**根因：Python 进程花了 11+ 小时在 `import` 阶段。** 可能因为训练进程（原 PID 21363/27427，现已终止）占用 GPU 导致 CUDA 初始化极慢。训练进程结束后，eval 才得以正常启动。

### 3. 当前进展

**seed1**（日志 tail）:
- 正在 libero_spatial task1, episode 30/50, success_rate=73.3%
- 速度 ~11.7s/episode, rollout 280 steps at ~15-28 it/s
- task0 已完成（10 videos），task1 进行中

**seed2**:
- libero_spatial task1, ~4/10 videos 已写

### 4. 已产出文件

- seed1: `run_info.json` + task0 (10 videos) + task1 (10 videos, 完成中)
- seed2: `run_info.json` + task0 (10 videos) + task1 (4 videos, 进行中)
- 尚无 `eval_info.json` 或 `summary.json`（未完成任何 suite）

### 5. 完成时间估算

每 task ~10 min。每 suite 10 tasks，4 suites = 40 tasks 总计 ~400 min (~6.7h)。

- **seed1 ETA: ~08:00 CST** (已完成 ~2/40 tasks)
- **seed2 ETA: ~08:10 CST** (已完成 ~1.5/40 tasks)

### 6. 判断

**不是卡死，是正常运行。** 进程经历了异常漫长的初始化阶段（可能与已终止的训练进程 GPU 争抢有关），但现在速率正常。训练进程 21363/27427 已不存在，GPU 资源已释放。

### 7. 建议

**继续等待，不要 kill。** 两个进程都在正常推进，预计 ~6 小时后完成全部 4 suites 的 eval。

---
