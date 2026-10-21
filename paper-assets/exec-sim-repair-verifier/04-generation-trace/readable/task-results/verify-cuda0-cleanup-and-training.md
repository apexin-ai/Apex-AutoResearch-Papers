# verify cuda0 cleanup and training

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_cuda0-cleanup-and-training_20260515T141637_result.json`
- **Structured JSON:** [`1a527e473ab75a0ad2d2.json`](../../sessions/1a/1a527e473ab75a0ad2d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**验证结果：**

| 检查项 | 状态 |
|--------|------|
| cuda:0 进程 | 仅 1 个 Python 进程 (PID 379614, 20920 MiB)，无 val sweep 残留 |
| tmux session | `cwm-rank32-alpha64-ablation` 存在 |
| 训练进度 | 已正常启动，当前 step 18/1434 (~1%)，速度 ~3.7s/it |
| LoRA 配置 | trainable params 23.6M / 4.0B total (0.58%)，符合 rank32 预期 |

cuda:0 干净，rank32-alpha64 训练正常运行中。PID 是 379614（非 379609），可能是实际训练子进程。

---
