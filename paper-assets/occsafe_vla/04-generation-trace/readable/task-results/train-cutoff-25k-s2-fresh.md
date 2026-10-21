# train cutoff 25k s2 fresh

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_cutoff_25k_s2_fresh_20260525T043816_result.json`
- **Structured JSON:** [`9a1dc5bca3f15b2a603d.json`](../../sessions/9a/9a1dc5bca3f15b2a603d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行。

- **PID**: 11510（worker 进程），11437（nohup 包裹）
- **服务器**: westd-34685, cuda:0
- **状态**: 从 pretrained 权重从头训练（无 resume），step 17/50005，~1.09 it/s
- **首个 step 指标**: occ_loss=0.1304, action_loss=0.6328
- **预计时长**: ~12.7 小时

注意：第一次启动时因 GPU 0 上有其他进程（PID 6112）导致 OOM，第二次启动后 reverse_cutoff_s2 进程（PID 11716，违反 C002 使用了 --resume）短暂出现在 GPU 0 但已自行退出，训练现在独占 GPU 0 正常运行。

---
