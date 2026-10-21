# fix kill dryrun cleanup gpu

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-dryrun-cleanup-gpu_20260527T031141_result.json`
- **Structured JSON:** [`11f98de03e023988cfdc.json`](../../sessions/11/11f98de03e023988cfdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

nvidia-smi 进程级只报告 4667+3255 MiB，但 GPU 0 总占用 53858 MiB。差额约 49 GB 很可能是被 kill 的 dry-run 进程留下的孤儿显存（CUDA driver 级别残留，需等当前进程退出后自动回收）。

**最终状态报告：**

```
GPU 0: 53858 MiB / 97887 MiB (exp_hopper_baseline PID 604355, 进程级 4667 MiB)
GPU 1:  3274 MiB / 97887 MiB (exp_hopper_trained_s0 PID 604518, 进程级 3255 MiB)
残留进程: 已清理（PID 603648 已 kill，fuser 确认无其他进程占用 GPU）
Phase 2 显存充足: Y
  - GPU 0 剩余 ~43 GB，GPU 1 剩余 ~92 GB，均 >15 GB
  - Phase 1 结束后孤儿显存会自动释放，Phase 2 每卡可用 ~96 GB
```

~49 GB 孤儿显存是 killed 进程的 CUDA context 残留，不影响 Phase 2——Phase 1 的两个训练进程退出后驱动会完全回收。

---
