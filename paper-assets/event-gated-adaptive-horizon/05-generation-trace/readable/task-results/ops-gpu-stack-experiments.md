# ops gpu stack experiments

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-stack-experiments_20260518T235332_result.json`
- **Structured JSON:** [`b02a91fdf3e09f3fbb40.json`](../../sessions/b0/b02a91fdf3e09f3fbb40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。当前服务器状态：

| 实验 | GPU | PID | Seed | Steps | VRAM |
|---|---|---|---|---|---|
| exp_023_cheetah_baseline_s2 | cuda:0 | 753791 | 2 | 200K | ~4.7GB |
| exp_023_cheetah_baseline_s4 | cuda:0 | 774033 | 4 | 200K | ~1.3GB (还在增长) |
| exp_023_cheetah_baseline_s3 | cuda:1 | 768897 | 3 | 200K | ~4.2GB |
| exp_001_baseline_s3 | cuda:1 | 774106 | 3 | 105K | ~1.3GB (还在增长) |

GPU 0 已用 6.5GB/97.9GB，GPU 1 已用 5.5GB/97.9GB，无 OOM 风险。两个新实验 SEED CHECK 均通过，registry 已更新到 RUNNING 并包含完整 spec。

---
