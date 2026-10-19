# diag bjb1 18228 gpu collision

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-18228-gpu-collision_20260522T202510_result.json`
- **Structured JSON:** [`0f8bc5fcfbd070672a33.json`](../../sessions/0f/0f8bc5fcfbd070672a33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 冲突报告 — bjb1-18228

### 各 GPU 状态

| GPU | 显存占用 | 进程 | 状态 |
|-----|---------|------|------|
| **0** | 12050 / 24564 MiB (49%) | π0.5 precompute `object` (9874M) + SmolVLA eval `spatial_seed43` (2160M) | **冲突但安全**，12.5GB 余量 |
| **1** | 20720 / 24564 MiB (84%) | π0.5 precompute `spatial` (9874M) + SmolVLA eval `goal_seed43` (2160M) + **18个 forkserver workers** (每个~460M) | **危险**，仅 3.8GB 余量 |
| 2 | 9884 / 24564 MiB (40%) | π0.5 precompute `goal` (9874M) | 无冲突 |
| 3 | 9884 / 24564 MiB (40%) | π0.5 precompute `long` (9874M) | 无冲突 |

### 关键发现

1. **GPU 1 是主要风险**：SmolVLA eval 的 `goal_seed43` 在 GPU 1 上 fork 了 18 个 multiprocessing worker（PID 140253-140272），每个占 460MiB GPU 显存，合计 ~8.3GB。加上 π0.5 precompute 的 9.9GB 和主 eval 进程的 2.2GB，已用 84%。如果 eval 再 fork 更多 worker 或任一进程分配更多显存，将 OOM。

2. **GPU 0 暂时安全**：总占用只有 49%，两个进程共存没有问题。

3. **所有进程均存活**，目前无 OOM kill。

4. **π0.5 precompute 速度极慢**：object 任务 100/72507 samples，2.29s/sample，预计剩余 ~46 小时。这可能是因为与 SmolVLA eval 共享 GPU 导致的性能下降。

### 建议（不执行，仅报告）

- SmolVLA eval 运行了约 3 小时，如果快结束了可以等它跑完自动释放
- 如果 GPU 1 出现 OOM，应 kill SmolVLA eval（PID 116278），保护更重要的 π0.5 precompute（PID 113796）
- 长期看，π0.5 precompute 46 小时的预估时间不合理，可能需要调查为什么这么慢（是否 batch_size=1？是否因共享 GPU 导致 CUDA context 切换开销？）

---
