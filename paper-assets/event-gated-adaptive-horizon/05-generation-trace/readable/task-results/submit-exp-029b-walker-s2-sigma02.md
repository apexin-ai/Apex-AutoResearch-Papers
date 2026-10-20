# submit exp 029b walker s2 sigma02

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_029b_walker_s2_sigma02_20260520T165530_result.json`
- **Structured JSON:** [`37ed136763a98b038efe.json`](../../sessions/37/37ed136763a98b038efe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功。

| 项目 | 值 |
|------|-----|
| **PID** | 75548 |
| **GPU** | cuda:1（CUDA_VISIBLE_DEVICES=1，进程内 cuda:0） |
| **显存占用** | 1079 MiB（启动中，还在增长） |
| **tmux session** | `exp_029b_tcn_walker_s2_sigma02` |

注意：原始命令的 `--device cuda:1` 与 `CUDA_VISIBLE_DEVICES=1` 冲突（进程只能看到一张卡），已修正为 `--device cuda:0`。

---
