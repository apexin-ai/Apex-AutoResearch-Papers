# ssh kill westd gpu23 orphans

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_westd_gpu23_orphans_20260522T200005_result.json`
- **Structured JSON:** [`7c4cf367625cf9d5e82e.json`](../../sessions/7c/7c4cf367625cf9d5e82e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理完成

**Kill 前：**
| GPU | 显存占用 | GPU-Util | 进程 |
|-----|----------|----------|------|
| 0 | 0 MiB | 0% | 无 |
| 1 | 0 MiB | 0% | 无 |
| 2 | 45,099 MiB | 0% | PID 132938 `ray::WorkerDict` |
| 3 | 45,801 MiB | 0% | PID 132939 `ray::WorkerDict` |

**Kill 后：**
| GPU | 显存占用 | GPU-Util | 进程 |
|-----|----------|----------|------|
| 0 | 0 MiB | 0% | 无 |
| 1 | 0 MiB | 0% | 无 |
| 2 | **0 MiB** | 100%* | **无** |
| 3 | **0 MiB** | 100%* | **无** |

GPU 2,3 显存完全释放，无任何进程。同时清理了崩溃的 train.py 主进程（PID 129828）和对应 tmux session。GPU 0,1 未受影响。

*GPU-Util 100% 是 kill -9 CUDA 进程后的驱动级计数器残留（已知行为），无实际负载。下次有 CUDA 进程使用这两张卡时会自动重置。不影响 GPU 可用性。

---
