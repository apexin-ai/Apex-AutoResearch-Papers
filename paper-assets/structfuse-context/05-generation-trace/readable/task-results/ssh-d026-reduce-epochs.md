# ssh d026 reduce epochs

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d026_reduce_epochs_20260514T025646_result.json`
- **Structured JSON:** [`75e39cc3307e9b6b368f.json`](../../sessions/75/75e39cc3307e9b6b368f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| | 修改前 | 修改后 |
|---|---|---|
| `run_m2_full_qwen.sh:67` | `--num-epochs 3` | `--num-epochs 2` |
| `run_m2_full_starcoder.sh:174` | `--num-epochs 3` | `--num-epochs 2` |

s42 进程存活确认：
- PID 73558 (Qwen): `Sl` 状态，已运行 9h17m
- PID 76627 (StarCoder): `Rl` 状态，已运行 8h27m

后续 s43/s44 runs 将使用 2 epochs (2828 steps)，每 encoder 节省 1414 steps × 剩余 runs。

---
