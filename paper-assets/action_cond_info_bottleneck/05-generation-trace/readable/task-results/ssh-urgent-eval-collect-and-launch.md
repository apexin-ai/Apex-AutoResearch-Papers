# ssh urgent eval collect and launch

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-eval-collect-and-launch_20260517T142301_result.json`
- **Structured JSON:** [`fd7009cf3afec6c5121a.json`](../../sessions/fd/fd7009cf3afec6c5121a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

**两个 eval 仍在运行，GPU 不空闲，不启动新任务。**

### 当前进度

| α | PID | 当前 Suite | Episode 进度 | running SR |
|---|-----|-----------|-------------|------------|
| 0.0 | 40598 | libero_spatial (1/4) | 48/50 | ~35.4% |
| 1.0 | 44022 | libero_spatial (1/4) | 45/50 | ~53.3% |

两个进程都只完成了第一个 suite 的大部分 episodes，还有 3 个 suites 待跑 (libero_object, libero_goal, libero_10)。

### 时间估算

每个 episode ~16-18s，每 suite 50 episodes ≈ 13-15 分钟。剩余 3 suites + 当前 suite 剩余 ≈ 还需 **45-50 分钟**完成全部 eval。

### 早期信号（仅 libero_spatial 阶段性数据）

- **α=0.0**: SR ~35% (scorer 完全不参与，纯 base model residual)
- **α=1.0**: SR ~53% (scorer 完全控制)

α=1.0 在 spatial suite 上明显优于 α=0.0，初步表明 scorer 对 spatial tasks 有正向贡献。

### 下一步

等 eval 完成后（预计 ~50 分钟），两个 GPU 释放，立即启动：
- GPU 0: token dropping sweep
- GPU 1: seed2 eval α=1.0

---
