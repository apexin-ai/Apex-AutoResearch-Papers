# diag gpu1 process check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu1_process_check_20260515T185829_result.json`
- **Structured JSON:** [`9f9f7f8fb7467235f371.json`](../../sessions/9f/9f9f7f8fb7467235f371.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

### GPU 1 当前进程

| PID | 身份 | 显存 | 状态 |
|-----|------|------|------|
| 517418 | **exp_009g_008f_walker_s0** (`dreamer.py`, walker_walk, 105k steps, gate_enabled=True, gate_fixed_dt=2) | 794 MiB | 正常运行 |
| 517810 | **test_cuda1_eval** (`dreamer.py`, walker_walk, 8k steps, seed=42) | 794 MiB | 仍在运行 |

### test_cuda1_eval 诊断进程

- 2 个中已退出 1 个（PID 518343，/proc 已消失）
- **PID 517810 仍在运行**，占 794 MiB 显存。它跑 8000 steps，应该快结束了（有 5 分钟 timeout 的话会自动退出）。

### 009g 训练日志

训练正常推进，当前在 **step 5000**，刚开始 evaluation。模型已完成初始化（world model 16.9M params, actor 1.1M, value 1.2M），prefill 2500 steps 完成，日志无报错。

---
