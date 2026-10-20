# ops gpu audit 35694

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-35694_20260522T024037_result.json`
- **Structured JSON:** [`6aab2d350d62a621a015.json`](../../sessions/6a/6aab2d350d62a621a015.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**GPU 状态：**

| GPU | 显存占用 | GPU-Util | 进程 |
|-----|---------|----------|------|
| 0 | 0 MiB / 97887 MiB | 100% | 无 |
| 1 | 0 MiB / 97887 MiB | 100% | 无 |
| 2 | 0 MiB / 97887 MiB | 0% | 无 |
| 3 | 0 MiB / 97887 MiB | 0% | 无 |

**Python 进程：** 仅有系统服务（jupyter-lab、tensorboard、supervisord），无任何 train.py 或 contam_5 相关进程。

**结论：** 残留训练进程已不存在，无需 kill。GPU 0/1 显示 100% utilization 但 0 显存、无进程，这是之前训练被强制终止后的 GPU 状态残留（driver 层面的 stale state）。可以通过 `nvidia-smi -r`（GPU reset）清除，或者直接启动新训练即可自动恢复正常。需要我执行 GPU reset 吗？

---
