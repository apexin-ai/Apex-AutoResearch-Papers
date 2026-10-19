# check spatial completions harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_spatial-completions-harvest_20260525T023635_result.json`
- **Structured JSON:** [`1f938c96bbe0a211e32b.json`](../../sessions/1f/1f938c96bbe0a211e32b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验**全部仍在运行**，没有完成：

### cqa1-32758

| 实验 | PID | CPU | 启动时间 | 状态 |
|------|-----|-----|---------|------|
| **eval-k10-tau025-spatial-s45** | 303884 | 759% | 09:20 | RUNNING (GPU 0) |
| **eval-k10-tau025-spatial-s47** | 304151 | 745% | 09:20 | RUNNING (GPU 1) |

同机还有 s42 canonical adaptive (GPU 2) 和 s42 VLA-only (tmux, GPU 1) 在跑。

### bjb1-32546

| 实验 | PID | CPU | 启动时间 | 状态 |
|------|-----|-----|---------|------|
| **eval-vla-only-spatial-s46** | 869873 | 353% | 09:36 | RUNNING (GPU 5, nohup) |

同机还有 s48/s49 adaptive (GPU 2/3)、s48/s49 VLA-only spatial (GPU 1/4)、s42 obj VLA-only (tmux, GPU 0) 在跑。

### 结论

三个实验都在正常运行，不需要 harvest 或重跑。HW 资源监控可能是因为 `nvidia-smi` 采样时间点不同导致未捕获，或者监控方式与实际进程不一致。它们都是今天 09:19-09:36 启动的，运行约 1 小时，spatial benchmark 20 rollouts 通常需要 3-5 小时，预计下午完成。

---
