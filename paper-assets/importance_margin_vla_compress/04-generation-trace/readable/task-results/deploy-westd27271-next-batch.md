# deploy westd27271 next batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_next_batch_20260525T075356_result.json`
- **Structured JSON:** [`97d047b444fd541dce48.json`](../../sessions/97/97d047b444fd541dce48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 有 98GB 显存，两个进程各用 16GB，共 32GB，无冲突问题。旧任务（k=0.9 s42 v2）约10分钟完成后 GPU 1 就只剩新实验了。

## 部署报告

| GPU | 实验 | 原因 | PID | 状态 |
|-----|------|------|-----|------|
| 0 | L2norm k=0.5 object seed42 | 填补退化曲线缺口（已有0.9/0.7/0.3缺0.5） | 311603 | Task 1/10 运行中 |
| 1 | Random k=0.7 seed43 object | seed可重复性验证（已有seed42结果） | 312527 | Task 1/10 运行中 |

**验证通过：**
- GPU 0: 88% util, 16GB, L2 Pruning 256→128 tokens
- GPU 1: 92% util, 32GB (两进程共存，旧任务~10min结束), Random Pruning 256→179 tokens
- 磁盘: 48GB可用，充足

两个实验各约4小时完成（10 tasks × 50 eps × ~2 eps/min ≈ 250 min）。

---
