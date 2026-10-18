# ops westd38929 script sync and launch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-script-sync-and-launch_20260520T190440_result.json`
- **Structured JSON:** [`cc510c16d1fc571709d6.json`](../../sessions/cc/cc510c16d1fc571709d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验正常运行，汇总：

| tmux session | GPU | 实验 | Token pruning | 状态 |
|---|---|---|---|---|
| `eval_random_k095_s43` | GPU 0 (16GB used) | random k=0.95 seed43 | 256→243 | running, Task 1/10 |
| `eval_random_k09_s43` | GPU 1 (16GB used) | random k=0.9 seed43 | 256→230 | running, Task 1/10 |
| `eval_random_k03_s43` | GPU 2 (16GB used) | random k=0.3 seed43 | 256→76 | running, Task 1/10 |
| `eval_l2norm_k09_s43` | GPU 3 (16GB used) | L2 norm k=0.9 seed43 | 256→230 | running, Task 1/10 |

参数修正说明：脚本参数为 `--mode random_prune --k_ratio`（非 `--keep_ratio`），无 `--gpu` 参数。L2 norm 脚本用 `--mode l2norm_prune`。每个实验 10 tasks × 50 episodes = 500 episodes。

---
