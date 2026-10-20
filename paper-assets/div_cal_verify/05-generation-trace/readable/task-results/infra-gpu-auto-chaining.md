# infra gpu auto chaining

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu_auto_chaining_20260513T193129_result.json`
- **Structured JSON:** [`e5b4de247236ff5d9668.json`](../../sessions/e5/e5b4de247236ff5d9668.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 chain tmux session 已成功创建并在等待中。

**当前 tmux sessions (4个)**:
| Session | 状态 |
|---------|------|
| `seed456_methods` | cuda:1 运行中 |
| `medium_uncurated` | cuda:0 运行中 |
| `chain_cuda1` | 等待 seed456_methods 结束 → 启动 medium_external |
| `chain_cuda0` | 等待 medium_uncurated 结束 → 启动 medium_rgds |

**预计时间线**:
- ~3-4h 后：seed456_methods 完成 → chain_cuda1 自动启动 `run_medium_external.sh 1`
- ~3-4h 后：medium_uncurated 完成 → chain_cuda0 自动启动 `run_medium_rgds.sh 0`
- 上述两个中先完成的 → 自动启动 `run_medium_random50.sh`（互斥检测避免重复启动）

**修正说明**: 任务描述中 `CUDA_VISIBLE_DEVICES=1 bash run_medium_external.sh 0` 会被脚本内部 `export CUDA_VISIBLE_DEVICES=$GPU_ID` 覆盖为 0，导致跑错卡。已改为直接传参 `bash run_medium_external.sh 1`。

---
