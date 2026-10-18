# probe westd 38929 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_westd-38929-gpu-status_20260521T224109_result.json`
- **Structured JSON:** [`9392454a625632e5bbe5.json`](../../sessions/93/9392454a625632e5bbe5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报 — westd-38929

| GPU | 状态 | PID | 进程 | 运行时间 |
|-----|------|-----|------|---------|
| **GPU0** | 占用 (10.2/95.6 GB, 22%) | 788122 | `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_spatial --seed 42` | 1h46m |
| **GPU1** | 占用 (10.3/95.6 GB, 30%) | 829120 | `eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.7 --suite libero_spatial --seed 42` | 1h16m |
| **GPU2** | **空闲** (1 MiB, 0%) | — | — | — |
| **GPU3** | 占用 (10.3/95.6 GB, 40%) | 824152 | `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_object --seed 42` | 1h20m |

**注意**：用户提到的 PID 788113 (GPU0) 和 824147 (GPU3) 与实际 PID 略有偏差（实际为 788122 和 824152），可能是 registry 记录的是父进程。三个任务都活着。

**Tmux sessions**: 仅 1 个 — `eval_pi05_random_k03_spatial_seed42`

### L2norm k=0.7 Spatial 进度

仍在运行，当前进度到 **Task 7**（共 10 个 task），已完成 6 个 task：

| Task | SR |
|------|----|
| T1 | 82% |
| T2 | 94% |
| T3 | 36% |
| T4 | 40% |
| T5 | 50% |
| T6 | 82% |
| T7 | 进行中 (ep20: 80%) |

累计 SR: 235/350 = **67.1%**（前 7 个 task 中已完成 6 个）。T7 当前 16/20 = 80%。预计还需约 20-25 分钟完成剩余 task。

---
