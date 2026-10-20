# code exp45 check processes

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp45_check_processes_20260522T064227_result.json`
- **Structured JSON:** [`fefcc564e29180351dcc.json`](../../sessions/fe/fefcc564e29180351dcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**GPU 0 上当前只有 1 个 Python 进程：**

| PID | 命令 | GPU 显存 | 状态 |
|-----|------|---------|------|
| **47812** | `python exp45_benign_adaptation_curve.py` | 1914 MiB | Running |

**PID 54587**（`train_deberta.py --train_data exp45_mixed_n10.jsonl`）在第一次 nvidia-smi 时还在（占 10246 MiB），几秒后已退出，可能是刚刚训练完成。

**进程树关系：**
- PID 47801 → tmux session `exp45_benign_adaptation_curve`
- PID 47802 → tmux 内的 bash wrapper
- PID 47812 → `exp45_benign_adaptation_curve.py`（主脚本，仍在运行）
- PID 54587 → `train_deberta.py`（已退出，是主脚本的子任务）

**结论：没有竞争问题。** PID 54587 是 exp45 主脚本（47812）启动的 `train_deberta.py` 子进程，已自然结束。当前 GPU 0 上只剩主脚本一个进程，显存从 ~11GB 降到 ~2GB，GPU 利用率从 94% 降到 5%，说明刚完成一轮训练。tmux session 只有一个 `exp45_benign_adaptation_curve`。

---
