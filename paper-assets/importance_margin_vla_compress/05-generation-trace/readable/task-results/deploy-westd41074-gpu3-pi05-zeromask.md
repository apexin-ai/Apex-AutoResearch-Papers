# deploy westd41074 gpu3 pi05 zeromask

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu3_pi05_zeromask_20260526T022142_result.json`
- **Structured JSON:** [`961787176c02d03aae3b.json`](../../sessions/96/961787176c02d03aae3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功。

**结果汇总：**

| 项目 | 值 |
|------|-----|
| Kill | 无需——GPU3 本就空闲 |
| 新进程 PID | 315599 |
| GPU3 显存 | **10348 MiB**（模型已加载） |
| GPU3 利用率 | 7%（开始推理） |
| 实验 | `eval_pi05_zeromask_random_k09_object_seed42_v3` |
| tmux session | `zeromask_random_v3` |

**nvidia-smi 全卡：**
- GPU0: 47%, 16188 MiB（在用）
- GPU1: 0%, 1 MiB（空闲）
- GPU2: 59%, 15980 MiB（attn_prune k=0.7 Object）
- GPU3: 7%, 10348 MiB（**zeromask_random v3 ✓**）

**日志确认关键信息：**
- `ZERO-MASK: zero_mask_random, keep 230/256 tokens/image (seq_len=unchanged)`
- `Suite: libero_object, 10 tasks, max_steps=280`
- 已开始执行 eval episodes

---
